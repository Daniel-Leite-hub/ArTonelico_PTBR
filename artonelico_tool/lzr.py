from __future__ import annotations

import struct


def decompress(data: bytes) -> bytes:
    if len(data) < 16 or data[:3] != b"LZR":
        raise ValueError("Not an LZR stream")
    flag_bits, data_length, original_length = struct.unpack_from("<III", data, 4)
    flag_length = (flag_bits + 7) // 8
    flags = memoryview(data)[16 : 16 + flag_length]
    source = memoryview(data)[16 + flag_length : 16 + flag_length + data_length]
    output = bytearray()
    fi = si = 0
    while len(output) < original_length:
        flag = flags[fi]
        fi += 1
        for _ in range(4):
            mode = flag >> 6
            flag = (flag << 2) & 0xFF
            if mode == 0:
                output.append(source[si]); si += 1
            elif mode == 1:
                count = source[si]; si += 1
                output.extend(source[si : si + count]); si += count
            elif mode == 2:
                count, value = source[si], source[si + 1]; si += 2
                output.extend(bytes((value,)) * count)
            else:
                distance = (source[si] << 4) | (source[si + 1] >> 4)
                count = source[si + 1] & 0x0F
                si += 2
                for _ in range(count):
                    output.append(output[-distance])
            if len(output) >= original_length:
                break
    return bytes(output[:original_length])


def compress(data: bytes) -> bytes:
    """Create a compatible LZR stream using literal, RLE and short LZ matches."""
    tokens: list[tuple[int, bytes]] = []
    positions: dict[bytes, list[int]] = {}

    def best_match(offset: int) -> tuple[int, int]:
        if offset + 3 > len(data):
            return 0, 0
        candidates = positions.get(data[offset : offset + 3], ())
        best_length = best_distance = 0
        for previous in reversed(candidates):
            distance = offset - previous
            if not 0 < distance <= 0xFFF:
                continue
            length = 3
            while length < 15 and offset + length < len(data) and data[previous + length] == data[offset + length]:
                length += 1
            if length > best_length:
                best_length, best_distance = length, distance
                if length == 15:
                    break
        return best_length, best_distance

    def remember(start: int, length: int) -> None:
        for offset in range(start, min(len(data) - 2, start + length)):
            key = data[offset : offset + 3]
            bucket = positions.setdefault(key, [])
            bucket.append(offset)
            while bucket and offset - bucket[0] > 0xFFF:
                bucket.pop(0)

    offset = 0
    literal = bytearray()
    literal_start = 0

    def flush_literal() -> None:
        nonlocal literal, literal_start
        while literal:
            if len(literal) < 5:
                tokens.append((0, bytes((literal.pop(0),))))
            else:
                chunk = bytes(literal[:255])
                del literal[:255]
                tokens.append((1, bytes((len(chunk),)) + chunk))
        literal_start = offset

    while offset < len(data):
        repeat = 1
        while offset + repeat < len(data) and repeat < 255 and data[offset + repeat] == data[offset]:
            repeat += 1
        match_length, distance = best_match(offset)
        if repeat >= 3 or match_length >= 3:
            flush_literal()
            if repeat >= match_length:
                tokens.append((2, bytes((repeat, data[offset]))))
                length = repeat
            else:
                tokens.append((3, bytes((distance >> 4, ((distance & 0xF) << 4) | match_length))))
                length = match_length
            remember(offset, length)
            offset += length
            literal_start = offset
        else:
            if not literal:
                literal_start = offset
            literal.append(data[offset])
            remember(offset, 1)
            offset += 1
            if len(literal) == 255:
                flush_literal()
    flush_literal()

    flags = bytearray()
    payload = bytearray()
    for group_start in range(0, len(tokens), 4):
        group = tokens[group_start : group_start + 4]
        flag = 0
        for index, (mode, token_data) in enumerate(group):
            flag |= mode << (6 - index * 2)
            payload.extend(token_data)
        flags.append(flag)
    flag_bits = len(tokens) * 2
    return b"LZR\0" + struct.pack("<III", flag_bits, len(payload), len(data)) + bytes(flags) + bytes(payload)

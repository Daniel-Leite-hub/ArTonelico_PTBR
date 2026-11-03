from __future__ import annotations

import re
import struct
import unicodedata
from dataclasses import dataclass

from .portuguese_font import encode_portuguese_character
from .native_menu_font import (
    NativeMenuText,
    ResetMenuText,
    encode_native_menu_character,
)

_ASCII_CONTROL_RE = re.compile(
    r"#0.*?##"
    r"|^#0[ -~]+"
    r"|#0[A-Za-z0-9]+"
    r"|#1(?=[A-Z]{4}_)"
    r"|(?<![A-ZÁÀÂÃÉÊÍÓÔÕÚÜÇ])CR(?!IATURAS)"
    r"|IM\d\d"
    r"|SC\d\d"
    r"|1X"
    r"|VB\d\d"
    r"|CLRE"
)
_NEWLINE_RE = re.compile(r"\s*[\r\n]+\s*")


def _match_ascii_control(value: str, index: int) -> str | None:
    for token in getattr(value, "ascii_format_tokens", ()):
        if value.startswith(token, index):
            return token
    match = _ASCII_CONTROL_RE.match(value, index)
    if match is not None:
        return match.group(0)
    return None


@dataclass(frozen=True)
class Dialogue:
    index: int
    position: int
    name_id: int
    portrait_id: int
    text_id: int
    portrait_type: int
    encoded_length: int
    text: str
    raw: bytes
    padding: bytes
    extra: bytes = b""


@dataclass(frozen=True)
class EvdFile:
    dialogues: tuple[Dialogue, ...]
    trailer: bytes


def decode_game_text(raw: bytes) -> str:
    value = raw.rstrip(b"\0").decode("cp932")
    return unicodedata.normalize("NFKC", value)


def encode_game_text(value: str) -> bytes:
    # The localized game uses full-width Latin glyphs from the Shift-JIS font.
    # A Portuguese glyph is stored as a one-byte alias in FO_HGGBP.  The #1
    # marker must immediately precede EVERY alias: the PS2 engine consumes
    # exactly one glyph from FO_HGGBP and immediately returns to font #0.
    # Consecutive Portuguese aliases must each receive their own #1 marker.
    if "\n" in value or "\r" in value:
        normalized = _NEWLINE_RE.sub(" ", value).strip()
        value = type(value)(normalized) if type(value) is not str else normalized
    output = bytearray()
    skipped_until = 0
    for index, char in enumerate(value):
        if index < skipped_until:
            continue
        token = _match_ascii_control(value, index)
        if token:
            output.extend(token.encode("ascii"))
            skipped_until = index + len(token)
            continue
        if isinstance(value, ResetMenuText):
            portuguese = encode_portuguese_character(char)
            if portuguese is not None:
                # Unlike the dialogue renderer, the inventory renderer does
                # not reliably return to its native font when the following
                # character is Shift-JIS.  Restore it explicitly so a PT-BR
                # alias cannot leak into the rest of the item/menu label.
                output.extend(b"#1")
                output.extend(portuguese)
                output.extend(b"#0")
                continue
        if isinstance(value, NativeMenuText):
            native_menu = encode_native_menu_character(char)
            if native_menu is not None:
                output.extend(native_menu)
                continue
        portuguese = encode_portuguese_character(char)
        if portuguese is not None:
            output.extend(b"#1")
            output.extend(portuguese)
            continue
        code = ord(char)
        if char == " ":
            encoded = "\u3000"
        elif char == '"':
            # Straight double quote: map to Japanese/Shift-JIS curly quotes (0x8167 / 0x8168).
            # The fullwidth form \uff02 encodes to 0xEEFC in cp932, which is an unmapped gaiji
            # slot in the PS2 font and renders as a corrupted vertical-stripe barcode glyph.
            prev_ch = value[index - 1] if index > 0 else "^"
            next_ch = value[index + 1] if index + 1 < len(value) else "$"
            after_cr = (index >= 2 and value[index - 2 : index] == "CR")
            if (
                after_cr
                or prev_ch in "^ \t\r\n([{\u3000<:–—"
                or (prev_ch in ".!?" and next_ch.isalnum())
            ):
                encoded = "\u201c"  # “ (Shift-JIS 0x8167)
            else:
                encoded = "\u201d"  # ” (Shift-JIS 0x8168)
        elif char == "'":
            # Straight single quote / apostrophe: map to curly quotes (0x8165 / 0x8166).
            # The fullwidth form \uff07 encodes to 0xEEFB in cp932, which is also an unmapped
            # slot in the PS2 font and renders as a barcode glyph.
            prev_ch = value[index - 1] if index > 0 else "^"
            next_ch = value[index + 1] if index + 1 < len(value) else "$"
            after_cr = (index >= 2 and value[index - 2 : index] == "CR")
            if prev_ch.isalnum() and next_ch.isalnum():
                encoded = "\u2019"  # ’ (Shift-JIS 0x8166) apostrophe in contraction
            elif (
                after_cr
                or prev_ch in "^ \t\r\n([{\u3000<:–—“"
                or (prev_ch in ".!?" and next_ch.isalnum())
            ):
                encoded = "\u2018"  # ‘ (Shift-JIS 0x8165)
            else:
                encoded = "\u2019"  # ’ (Shift-JIS 0x8166)
        elif 0x21 <= code <= 0x7E:
            encoded = chr(code + 0xFEE0)
        else:
            encoded = char
        output.extend(encoded.encode("cp932"))
    output.append(0)
    return bytes(output)


def parse(data: bytes) -> EvdFile:
    if len(data) < 4:
        raise ValueError("EVD is too small")
    count = struct.unpack_from("<I", data, 0)[0]
    cursor = 4
    rows: list[Dialogue] = []
    for index in range(count):
        if cursor + 24 > len(data):
            raise ValueError(f"Truncated EVD entry {index}")
        position, name_id, portrait_id, text_id, portrait_type, length = struct.unpack_from(
            "<IIIIII", data, cursor
        )
        cursor += 24
        # SLUS_214.45, 0x196FD0..0x196FE8: (length // 4) * 4 + 4.
        # This is the NEXT boundary, not ceil4: multiples of four need a
        # complete padding word too. Omitting it desynchronizes the loader.
        padded = (length // 4 + 1) * 4
        if length == 0 or cursor + padded > len(data):
            raise ValueError(f"Truncated or empty EVD text {index}")
        raw = data[cursor : cursor + length]
        if len(raw) != length:
            raise ValueError(f"Truncated EVD text {index}")
        padding = data[cursor + length : cursor + padded]
        cursor += padded
        if raw[-1:] != b"\0":
            raise ValueError(f"Unterminated EVD text {index}")
        rows.append(Dialogue(index, position, name_id, portrait_id, text_id, portrait_type, length, decode_game_text(raw), raw, padding))
    return EvdFile(tuple(rows), data[cursor:])


def validate_runtime_layout(data: bytes, reference: EvdFile) -> int:
    """Walk like the MIPS loader, without parse/build or header recovery.

    Check all non-text fields and the exact script tail against the original.
    Returns the script offset; a round trip through our own parser alone is
    insufficient evidence of compatibility with the game's loader.
    """
    if len(data) < 4 or struct.unpack_from('<I', data)[0] != len(reference.dialogues):
        raise ValueError('EVD runtime dialogue count mismatch')
    cursor = 4
    for row in reference.dialogues:
        if cursor + 24 > len(data):
            raise ValueError(f'EVD runtime header overrun at {row.index}')
        header = struct.unpack_from('<6I', data, cursor)
        if header[:5] != (row.position, row.name_id, row.portrait_id, row.text_id, row.portrait_type):
            raise ValueError(f'EVD runtime header mismatch at {row.index}')
        length = header[5]
        text_start = cursor + 24
        cursor = text_start + ((length >> 2) << 2) + 4
        if not 0 < length < 0x80000000 or cursor > len(data):
            raise ValueError(f'EVD runtime text overrun at {row.index}')
        if data[text_start + length - 1] != 0:
            raise ValueError(f'EVD runtime unterminated text at {row.index}')
    if data[cursor:] != reference.trailer:
        raise ValueError('EVD runtime script tail shifted or modified')
    return cursor


def build(evd: EvdFile, replacements: dict[int, str] | None = None) -> bytes:
    replacements = replacements or {}
    output = bytearray(struct.pack("<I", len(evd.dialogues)))
    for row in evd.dialogues:
        changed = row.index in replacements
        encoded = encode_game_text(replacements[row.index]) if changed else row.raw
        output.extend(struct.pack("<IIIIII", row.position, row.name_id, row.portrait_id, row.text_id, row.portrait_type, len(encoded)))
        output.extend(encoded)
        output.extend(b"\0" * (4 - len(encoded) % 4) if changed else row.padding)
        output.extend(row.extra)
    output.extend(evd.trailer)
    return bytes(output)

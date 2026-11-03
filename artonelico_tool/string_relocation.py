"""Conservative experimental reuse of owned string tails, never arbitrary caves.

Static eligibility is not a proof against computed runtime addresses. Keep this
feature opt-in until boot, inventory, menus and battle have been tested in game.
"""
from __future__ import annotations

import bisect
import struct
from dataclasses import dataclass

from .executable_text import extract_executable_texts
from .mips_text_reference import adjacent_address_pairs, rewrite_pair


# Scoped exception: conversation entry in a 24-byte record table, not a
# contiguous pointer vector. Exact source, pointer and neighboring records
# are checked against the ORIGINAL executable; do not generalize this rule.
MISHA_SOURCE = 0x8D4F70
MISHA_POINTER = 0x5B394C


def misha_record_reference(original: bytes, offset: int, references: list[int], by_address: dict) -> bool:
    if offset != MISHA_SOURCE or references != [MISHA_POINTER]:
        return False
    expected = (3, 1, 0, 0, 0xFFFF, 0x9D3F70)
    if struct.unpack_from("<6I", original, MISHA_POINTER-20) != expected:
        return False
    # Pointer field at +20 in adjacent 24-byte records; both names must match.
    for pos, expected_text in ((MISHA_POINTER-24, "Hey, Lyner...I’ve been waiting for you. Um...you’re not going back today, are you? Can I stay by your side..."),
                               (MISHA_POINTER+24, "Oh, Lyner. What’s up?")):
        value = struct.unpack_from("<I", original, pos)[0]
        if value not in by_address or by_address[value].text != expected_text:
            return False
    return True


@dataclass(frozen=True)
class Move:
    source: int
    destination: int
    payload: bytes
    pointers: tuple[int, ...]
    shared: bool = False
    instructions: tuple = ()


def plan_string_moves(original: bytes, selected: dict[int, bytes], priority: tuple[int, ...] = (), arena_offset: int | None = None):
    if original[:6] != b"\x7fELF\x01\x01":
        raise ValueError("Esperado ELF32 little-endian")
    shoff = struct.unpack_from("<I", original, 32)[0]
    shsize, count = struct.unpack_from("<HH", original, 46)
    sections = [struct.unpack_from("<10I", original, shoff+i*shsize) for i in range(count)]
    names_index=struct.unpack_from('<H',original,50)[0]
    names_section=sections[names_index]
    section_names=original[names_section[4]:names_section[4]+names_section[5]]
    cpu_sections=[s for s in sections if s[2]&6==6
                  and section_names[s[0]:].split(b'\0')[0] not in (b'.vutext',)]
    instruction_refs = adjacent_address_pairs(original,cpu_sections) if arena_offset is not None else {}
    phoff = struct.unpack_from("<I", original, 28)[0]
    phsize, phcount = struct.unpack_from("<HH", original, 42)
    loads = [struct.unpack_from("<8I", original, phoff+i*phsize) for i in range(phcount)]
    loads = [p for p in loads if p[0] == 1]
    def address(offset):
        for p in loads:
            if p[1] <= offset < p[1]+p[4]:
                return offset+p[2]-p[1]
        raise ValueError("Texto fora dos segmentos carregados")
    texts = extract_executable_texts(original)
    slots = {t.offset: t for t in texts}
    starts = sorted(address(t.offset) for t in texts)
    by_address = {address(t.offset): t for t in texts}
    refs = {t.offset: [] for t in texts}
    interior = set()
    # Include unaligned literals, not just the aligned pointer table scan.
    for pos in range(len(original)-3):
        value = struct.unpack_from("<I", original, pos)[0]
        if not starts or value < starts[0] or value > starts[-1]+slots[texts[-1].offset].encoded_length:
            continue
        index = bisect.bisect_right(starts, value)-1
        t = by_address[starts[index]]
        if value == starts[index]:
            refs[t.offset].append(pos)
        elif value < starts[index]+t.encoded_length:
            interior.add(t.offset)
    pages = set()
    for s in sections:
        if s[2]&4 and s[1] != 8:
            for pos in range(s[4], s[4]+s[5]-3, 4):
                word = struct.unpack_from("<I", original, pos)[0]
                if word >> 26 == 15:  # Any LUI using this page blocks it.
                    pages.add(word&0xffff)
    def data_pointer(pos):
        return pos % 4 == 0 and any(s[1] != 8 and s[2]&2 and not s[2]&4
                                    and s[4] <= pos and pos+4 <= s[4]+s[5] for s in sections)
    def table_pointer(pos):
        if not data_pointer(pos):
            return False
        # Three consecutive full string-start pointers, including this one.
        for base in (pos-8, pos-4, pos):
            if base >= 0 and base+12 <= len(original) and all(
                data_pointer(p) and struct.unpack_from("<I", original, p)[0] in by_address
                for p in (base, base+4, base+8)
            ):
                return True
        return False
    def conversation_record(pos):
        # Generalize the tested +20 pointer field ONLY within runs of three
        # compatible 24-byte records. Never reinterpret isolated data words.
        def record(pointer):
            if pointer < 20 or not data_pointer(pointer):
                return False
            words = struct.unpack_from("<6I", original, pointer-20)
            return (words[0] in (2, 3) and words[1] <= 255
                    and words[2] <= 65535 and words[3] <= 255
                    and words[4] in (0, 1, 2, 65535)
                    and words[5] in by_address)
        return any(all(record(p) for p in (base, base+24, base+48))
                   for base in (pos-48, pos-24, pos))
    def strided_pointer(pos):
        # Arena copy-only mode can update a repeated pointer field in other
        # record layouts without rewriting any neighboring metadata.
        if not data_pointer(pos):
            return False
        for stride in (8,12,16,20,24,28,32,36,40,44,48,52,56,64,68,72,80,96,104,108,
                       120,128,144,156,160,168,192,204,256,260):
            for base in (pos-2*stride,pos-stride,pos):
                fields=(base,base+stride,base+2*stride)
                if not any(s[1]!=8 and s[2]&2 and not s[2]&4 and s[4]<=base
                           and fields[-1]+4<=s[4]+s[5] for s in sections):
                    continue
                if all(data_pointer(p) and struct.unpack_from('<I',original,p)[0] in by_address
                       for p in fields):
                    return True
        return False
    def eligible(t, moving=False):
        va = address(t.offset)
        end = va+t.encoded_length-1
        scoped_record = misha_record_reference(original, t.offset, refs[t.offset], by_address)
        structured = bool(refs[t.offset]) and all(conversation_record(p) for p in refs[t.offset])
        repeated_field = arena_offset is not None and bool(refs[t.offset]) and all(strided_pointer(p) for p in refs[t.offset])
        # This source remains byte-identical and is NEVER a donor. Unaligned
        # interior-looking literals are left intact along with its old content.
        return ((t.offset not in interior or (moving and (scoped_record or structured or arena_offset is not None))) and not t.locked
                and (arena_offset is not None or all(page not in pages for page in (va>>16, (va+0x8000)>>16,
                                                      end>>16, (end+0x8000)>>16)))
                and bool(refs[t.offset]) and (all(table_pointer(p) for p in refs[t.offset])
                    or scoped_record or structured or repeated_field))
    available = []
    blocked = {}
    requests = []
    moves = []
    packed = set()
    if arena_offset is not None:
        # Copy-only: preserve ALL old slots, even where instructions may still
        # form an old address. Update identified data-table paths only. No donor
        # reclamation or instruction-address rewriting is enabled in this mode.
        cursor = arena_offset
        copies = {}
        for offset,payload in sorted(selected.items()):
            t = slots.get(offset)
            if t is None or not payload.endswith(b'\0'):
                raise ValueError('Catálogo incompatível com o executável')
            if len(payload) <= t.encoded_length:
                continue
            pairs=tuple(instruction_refs.get(address(offset),()))
            if not eligible(t, moving=True) and not (not refs[offset] and pairs and not t.locked):
                blocked[offset] = 'no_direct_reference' if not refs[offset] else 'references_not_proven'
                continue
            shared = payload in copies
            if not shared:
                copies[payload] = cursor
                cursor = (cursor+len(payload)+3)&~3
            moves.append(Move(offset,copies[payload],payload,tuple(refs[offset]),shared,pairs))
        return moves,blocked
    # Compact only adjacent OWNED slots where EVERY literal reference passed
    # the strict (non-interior, no LUI) gate. Never merge across unknown bytes.
    runs = []
    run = []
    for t in texts:
        if t.offset in selected and eligible(t):
            if run and run[-1].offset+run[-1].encoded_length != t.offset:
                runs.append(run)
                run = []
            run.append(t)
        else:
            if run:
                runs.append(run)
                run = []
    if run:
        runs.append(run)
    for run in runs:
        if not any(len(selected[t.offset]) > t.encoded_length for t in run):
            continue
        cursor = run[0].offset
        proposed = []
        for t in run:
            payload = selected[t.offset]
            proposed.append(Move(t.offset, cursor, payload, tuple(refs[t.offset])))
            cursor = (cursor+len(payload)+3)&~3
        end = run[-1].offset+run[-1].encoded_length
        if cursor > end:
            continue
        moves.extend(proposed)
        packed.update(t.offset for t in run)
        if cursor < end:
            available.append([cursor, end])
    for offset, payload in selected.items():
        t = slots.get(offset)
        if t is None or not payload.endswith(b"\0"):
            raise ValueError("Catálogo/terminador incompatível com ELF original")
        if offset in packed:
            continue
        if len(payload) > t.encoded_length:
            if eligible(t, moving=True):
                requests.append((offset, payload))
            else:
                va = address(offset)
                if t.locked:
                    blocked[offset] = "locked_identifier"
                elif not refs[offset]:
                    blocked[offset] = "no_direct_reference"
                elif any(page in pages for page in (va>>16, (va+0x8000)>>16,
                            (va+t.encoded_length-1)>>16, (va+t.encoded_length-1+0x8000)>>16)):
                    blocked[offset] = "instruction_address_page"
                else:
                    blocked[offset] = "references_not_proven"
        elif eligible(t):
            # Only bytes owned by this original string, after the NEW terminator.
            begin = (offset+len(payload)+3)&~3
            end = offset+t.encoded_length
            if end > begin:
                available.append([begin, end])
    # Largest first; best fitting tail. No moved-source reuse and no heap growth.
    existing_payloads = {payload: offset for offset,payload in selected.items()
                         if offset not in packed and len(payload) <= slots[offset].encoded_length}
    existing_payloads.update({m.payload:m.destination for m in moves})
    priority_rank = {offset: i for i,offset in enumerate(priority)}
    for offset, payload in sorted(requests, key=lambda x: (
            priority_rank.get(x[0],len(priority)), -len(x[1]), x[0])):
        if payload in existing_payloads:
            moves.append(Move(offset, existing_payloads[payload], payload, tuple(refs[offset]), True))
            continue
        candidates = [(end-begin, i) for i,(begin,end) in enumerate(available)
                      if end-begin >= len(payload)]
        if not candidates:
            blocked[offset] = "no_verified_tail_capacity"
            continue
        _, index = min(candidates)
        begin, end = available[index]
        moves.append(Move(offset, begin, payload, tuple(refs[offset])))
        existing_payloads[payload] = begin
        available[index][0] = (begin+len(payload)+3)&~3
    return moves, blocked


def apply_string_moves(executable: bytearray, original: bytes, moves: list[Move]):
    phoff = struct.unpack_from("<I", original, 28)[0]
    phsize, count = struct.unpack_from("<HH", original, 42)
    loads = [struct.unpack_from("<8I", original, phoff+i*phsize) for i in range(count)]
    def address(offset):
        for p in loads:
            if p[0] == 1 and p[1] <= offset < p[1]+p[4]:
                return offset+p[2]-p[1]
        raise ValueError("Destino não carregável")
    # Check all pointer preconditions BEFORE any mutation.
    if any(m.instructions for m in moves):
        probe=bytearray(executable)
        for m in moves:
            for pair in m.instructions:
                rewrite_pair(probe,pair,address(m.destination))
    for m in moves:
        for pos in m.pointers:
            if struct.unpack_from("<I", executable, pos)[0] != address(m.source):
                raise ValueError("Referência mudou antes da realocação")
    for m in moves:
        executable[m.destination:m.destination+len(m.payload)] = m.payload
        for pos in m.pointers:
            struct.pack_into("<I", executable, pos, address(m.destination))
        for pair in m.instructions:
            rewrite_pair(executable,pair,address(m.destination))
    return [{"source": m.source, "destination": m.destination,
             "bytes": len(m.payload), "pointers": list(m.pointers),
             "shared": m.shared,
             "instruction_pairs": [{"hi":p.hi,"lo":p.lo,"old_address":p.value,"ori":p.ori} for p in m.instructions],
             "destination_address": address(m.destination)} for m in moves]

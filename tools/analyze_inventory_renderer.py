from __future__ import annotations

import argparse
import struct
from pathlib import Path


LOAD_OFFSET = 0x1000
LOAD_VA = 0x100000
TEXT_END_VA = 0x3E1160


REG = (
    "zero", "at", "v0", "v1", "a0", "a1", "a2", "a3",
    "t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7",
    "s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7",
    "t8", "t9", "k0", "k1", "gp", "sp", "fp", "ra",
)


def sign16(value: int) -> int:
    return value - 0x10000 if value & 0x8000 else value


def va_to_offset(va: int) -> int:
    return LOAD_OFFSET + va - LOAD_VA


def instruction(data: bytes, va: int) -> int:
    return struct.unpack_from("<I", data, va_to_offset(va))[0]


def target_of_jump(word: int, va: int) -> int:
    return ((va + 4) & 0xF0000000) | ((word & 0x03FFFFFF) << 2)


def disasm(word: int, va: int) -> str:
    op = word >> 26
    rs = (word >> 21) & 31
    rt = (word >> 16) & 31
    rd = (word >> 11) & 31
    imm = word & 0xFFFF
    fn = word & 63
    if word == 0:
        return "nop"
    if op == 0:
        names = {0x08: "jr", 0x09: "jalr", 0x21: "addu", 0x23: "subu", 0x2A: "slt"}
        name = names.get(fn, f"special_{fn:02x}")
        if fn in (0x08, 0x09):
            return f"{name} {REG[rs]}"
        return f"{name} {REG[rd]},{REG[rs]},{REG[rt]}"
    if op in (2, 3):
        return f"{'jal' if op == 3 else 'j'} 0x{target_of_jump(word, va):08x}"
    names = {
        0x04: "beq", 0x05: "bne", 0x08: "addi", 0x09: "addiu",
        0x0A: "slti", 0x0B: "sltiu", 0x0C: "andi", 0x0D: "ori",
        0x0E: "xori", 0x0F: "lui", 0x20: "lb", 0x21: "lh",
        0x23: "lw", 0x24: "lbu", 0x25: "lhu", 0x28: "sb",
        0x29: "sh", 0x2B: "sw",
    }
    name = names.get(op, f"op_{op:02x}")
    if op == 0x0F:
        return f"lui {REG[rt]},0x{imm:04x}"
    if op in (0x04, 0x05):
        return f"{name} {REG[rs]},{REG[rt]},0x{va + 4 + sign16(imm) * 4:08x}"
    if op in (0x20, 0x21, 0x23, 0x24, 0x25, 0x28, 0x29, 0x2B):
        return f"{name} {REG[rt]},{sign16(imm):#x}({REG[rs]})"
    return f"{name} {REG[rt]},{REG[rs]},{sign16(imm):#x}"


def nearest_prologue(data: bytes, va: int, limit: int = 0x400) -> int:
    # Most game functions begin by reserving stack space.
    for candidate in range(va & ~3, max(LOAD_VA, va - limit), -4):
        word = instruction(data, candidate)
        if (word >> 26) == 0x09 and ((word >> 21) & 31) == 29 and ((word >> 16) & 31) == 29:
            if sign16(word & 0xFFFF) < 0:
                return candidate
    return va


def dump(data: bytes, start: int, count: int = 32) -> None:
    for va in range(start, start + count * 4, 4):
        word = instruction(data, va)
        print(f"{va:08x}  {word:08x}  {disasm(word, va)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("executable", type=Path)
    parser.add_argument("--lo", type=lambda x: int(x, 0), default=0x68E000)
    parser.add_argument("--hi", type=lambda x: int(x, 0), default=0x692000)
    args = parser.parse_args()
    data = args.executable.read_bytes()
    hits: list[tuple[int, int, int]] = []
    for va in range(LOAD_VA, TEXT_END_VA, 4):
        word = instruction(data, va)
        if word >> 26 != 0x0F:
            continue
        register = (word >> 16) & 31
        high = (word & 0xFFFF) << 16
        for delta in range(1, 9):
            next_va = va + delta * 4
            next_word = instruction(data, next_va)
            op = next_word >> 26
            rs = (next_word >> 21) & 31
            rt = (next_word >> 16) & 31
            if rs != register or rt != register or op not in (0x09, 0x0D):
                continue
            low = next_word & 0xFFFF
            address = high + (sign16(low) if op == 0x09 else low)
            if args.lo <= address < args.hi:
                hits.append((va, next_va, address))
            break
    seen: set[int] = set()
    for lui_va, low_va, address in hits:
        function = nearest_prologue(data, lui_va)
        key = (function << 32) | address
        if key in seen:
            continue
        seen.add(key)
        print(f"\n# ref 0x{address:08x} at 0x{lui_va:08x}; function ~0x{function:08x}")
        dump(data, max(function, lui_va - 8 * 4), 28)


if __name__ == "__main__":
    main()

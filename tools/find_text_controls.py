from __future__ import annotations

import struct
from pathlib import Path


ELF = Path(__file__).resolve().parents[1] / "work" / "SLUS_214.45"
FILE_BASE = 0x1000
VIRTUAL_BASE = 0x100000


def li_value(word: int) -> int | None:
    opcode = word >> 26
    rs = (word >> 21) & 31
    imm = word & 0xFFFF
    if rs == 0 and opcode in (9, 13):  # addiu/ori rt, zero, immediate
        return imm
    return None


REGS = (
    "zero", "at", "v0", "v1", "a0", "a1", "a2", "a3",
    "t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7",
    "s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7",
    "t8", "t9", "k0", "k1", "gp", "sp", "fp", "ra",
)


def disassemble(word: int, address: int) -> str:
    op = word >> 26
    rs, rt, rd = (word >> 21) & 31, (word >> 16) & 31, (word >> 11) & 31
    signed = struct.unpack("<h", struct.pack("<H", word & 0xFFFF))[0]
    unsigned = word & 0xFFFF
    if word == 0:
        return "nop"
    if op == 0:
        funct = word & 63
        names = {8: "jr", 9: "jalr", 33: "addu", 35: "subu", 36: "and", 37: "or", 38: "xor", 42: "slt", 43: "sltu"}
        name = names.get(funct, f"special_{funct:02x}")
        if funct == 8:
            return f"jr ${REGS[rs]}"
        return f"{name} ${REGS[rd]}, ${REGS[rs]}, ${REGS[rt]}"
    if op in (2, 3):
        target = ((address + 4) & 0xF0000000) | ((word & 0x03FFFFFF) << 2)
        return f"{'jal' if op == 3 else 'j'} 0x{target:08X}"
    if op in (4, 5, 6, 7):
        names = {4: "beq", 5: "bne", 6: "blez", 7: "bgtz"}
        target = address + 4 + signed * 4
        return f"{names[op]} ${REGS[rs]}, ${REGS[rt]}, 0x{target:08X}"
    if op == 1:
        target = address + 4 + signed * 4
        return f"regimm_{rt:02x} ${REGS[rs]}, 0x{target:08X}"
    immediate = {8: "addi", 9: "addiu", 10: "slti", 11: "sltiu", 12: "andi", 13: "ori", 14: "xori"}
    if op in immediate:
        value = unsigned if op >= 12 else signed
        return f"{immediate[op]} ${REGS[rt]}, ${REGS[rs]}, {value:#x}"
    if op == 15:
        return f"lui ${REGS[rt]}, {unsigned:#x}"
    memory = {32: "lb", 33: "lh", 35: "lw", 36: "lbu", 37: "lhu", 40: "sb", 41: "sh", 43: "sw", 49: "lwc1", 57: "swc1"}
    if op in memory:
        return f"{memory[op]} ${REGS[rt]}, {signed}(${REGS[rs]})"
    return f"word 0x{word:08X}"


def main() -> None:
    data = ELF.read_bytes()
    words = [struct.unpack_from("<I", data, offset)[0] for offset in range(0, len(data) - 3, 4)]
    candidates: list[int] = []
    for index, word in enumerate(words):
        if li_value(word) != 0x23:
            continue
        constant_register = (word >> 16) & 31
        compared = False
        for j in range(index + 1, min(len(words), index + 13)):
            candidate = words[j]
            opcode = candidate >> 26
            rs, rt = (candidate >> 21) & 31, (candidate >> 16) & 31
            if opcode in (4, 5) and constant_register in (rs, rt):
                compared = True
                break
        if compared:
            candidates.append(index * 4)
    print(f"candidates={len(candidates)}")
    for offset in candidates:
        virtual = offset - FILE_BASE + VIRTUAL_BASE
        print(f"file=0x{offset:08X} virtual=0x{virtual:08X}")
        start = max(FILE_BASE, offset - 64)
        end = min(len(data), offset + 68)
        for current in range(start, end, 4):
            word = struct.unpack_from("<I", data, current)[0]
            address = current - FILE_BASE + VIRTUAL_BASE
            marker = ">" if current == offset else " "
            print(f" {marker} {address:08X}: {word:08X}  {disassemble(word, address)}")


if __name__ == "__main__":
    main()

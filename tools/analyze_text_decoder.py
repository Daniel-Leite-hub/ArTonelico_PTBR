"""Locate likely Shift-JIS decoder functions in the PS2 executable."""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path("work/pydeps314").resolve()))

from capstone import CS_ARCH_MIPS, CS_MODE_LITTLE_ENDIAN, CS_MODE_MIPS64, Cs
from capstone.mips import MIPS_OP_IMM


data = Path("work/SLUS_214.45").read_bytes()
code = data[0x1000 : 0x1000 + 0x2E1160]
md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS64 | CS_MODE_LITTLE_ENDIAN)
md.detail = True
md.skipdata = True
instructions = list(md.disasm(code, 0x100000))

# Typical Shift-JIS lead/trail bounds and text escape constants.
interesting = {0x23, 0x40, 0x7E, 0x80, 0x81, 0x9F, 0xA0, 0xDF, 0xE0, 0xEF, 0xFC, 0xFF}
hit_values: dict[int, set[int]] = defaultdict(set)
for index, insn in enumerate(instructions):
    if insn.mnemonic == ".byte":
        continue
    for operand in insn.operands:
        if operand.type == MIPS_OP_IMM and (operand.imm & 0xFFFF) in interesting:
            hit_values[index].add(operand.imm & 0xFFFF)

reported = -1
for index in sorted(hit_values):
    if index <= reported:
        continue
    start = max(0, index - 40)
    end = min(len(instructions), index + 81)
    constants = set().union(*(hit_values.get(i, set()) for i in range(start, end)))
    if len(constants & {0x40, 0x7E, 0x80, 0x81, 0x9F, 0xA0, 0xDF, 0xE0, 0xFC}) < 3:
        continue
    reported = end
    print(f"\n=== {instructions[start].address:08X}-{instructions[end - 1].address:08X} constants={sorted(constants)}")
    for insn in instructions[start:end]:
        print(f"{insn.address:08X}  {insn.mnemonic:8} {insn.op_str}")

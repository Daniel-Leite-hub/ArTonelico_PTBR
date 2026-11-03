from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path("work/pydeps311").resolve()))
from capstone import Cs, CS_ARCH_MIPS, CS_MODE_LITTLE_ENDIAN, CS_MODE_MIPS64


data = Path("work/SLUS_214.45").read_bytes()
code = data[0x1000 : 0x1000 + 0x2E1160]
md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS64 | CS_MODE_LITTLE_ENDIAN)
md.skipdata = True

pattern = re.compile(r"(?<![0-9a-f])(?:0x(?:81|82|83)[0-9a-f]{2}|-0x7[de][0-9a-f]{2})(?![0-9a-f])")
for insn in md.disasm(code, 0x100000):
    if insn.mnemonic != ".byte" and pattern.search(insn.op_str.lower()):
        print(f"{insn.address:08X}  {insn.mnemonic:8} {insn.op_str}")

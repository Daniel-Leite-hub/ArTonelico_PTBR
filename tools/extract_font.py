from __future__ import annotations

import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artonelico_tool.lzr import decompress


elf = Path("work/SLUS_214.45").read_bytes()
fp = Path("work/font_extract/fpack/font.fp").read_bytes()
table = 0x301058
out = Path("work/fonts")
out.mkdir(parents=True, exist_ok=True)
for i in range(9):
    pointer, sector, size = struct.unpack_from("<III", elf, table + i * 12)
    name_offset = pointer - 0x100000 + 0x1000
    end = elf.index(0, name_offset)
    name = elf[name_offset:end].decode("ascii")
    packed = fp[sector * 2048 : sector * 2048 + size]
    raw = decompress(packed)
    target = out / Path(name).name.removesuffix(".lzr")
    target.write_bytes(raw)
    print(i, name, len(packed), len(raw), target)

from __future__ import annotations

import struct
from pathlib import Path


elf = Path("work/SLUS_214.45").read_bytes()
target = b"Event/906.evd\0"
pos = elf.find(target)
print(f"first name file offset: 0x{pos:X}")

# ELF32 little-endian load segments and file-offset -> virtual-address mapping.
phoff = struct.unpack_from("<I", elf, 28)[0]
phentsize, phnum = struct.unpack_from("<HH", elf, 42)[0], struct.unpack_from("<H", elf, 44)[0]
segments = []
for i in range(phnum):
    values = struct.unpack_from("<IIIIIIII", elf, phoff + i * phentsize)
    p_type, p_offset, p_vaddr, _, p_filesz, p_memsz, flags, align = values
    if p_type == 1:
        segments.append(values)
        print(f"LOAD off=0x{p_offset:X} va=0x{p_vaddr:X} filesz=0x{p_filesz:X} memsz=0x{p_memsz:X}")

for values in segments:
    _, p_offset, p_vaddr, _, p_filesz, *_ = values
    if p_offset <= pos < p_offset + p_filesz:
        va = p_vaddr + pos - p_offset
        print(f"name VA: 0x{va:08X}")
        needle = struct.pack("<I", va)
        refs = [i for i in range(0, len(elf) - 3, 4) if elf[i:i+4] == needle]
        print("aligned direct refs:", [f"0x{x:X}" for x in refs[:30]])

start = max(0, pos - 512)
for off in range(start, pos + 64, 16):
    chunk = elf[off:off+16]
    words = struct.unpack("<IIII", chunk)
    asc = ''.join(chr(x) if 32 <= x < 127 else '.' for x in chunk)
    print(f"{off:08X}  {' '.join(f'{x:08X}' for x in words)}  {asc}")

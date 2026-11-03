from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path


SECTOR_SIZE = 2048


@dataclass(frozen=True)
class RpkEntry:
    name: str
    sector: int
    size: int
    table_offset: int

    @property
    def offset(self) -> int:
        return self.sector * SECTOR_SIZE


def _load_segments(elf: bytes) -> list[tuple[int, int, int]]:
    phoff = struct.unpack_from("<I", elf, 28)[0]
    phentsize, phnum = struct.unpack_from("<HH", elf, 42)
    segments = []
    for index in range(phnum):
        p_type, p_offset, p_vaddr, _, p_filesz, *_ = struct.unpack_from(
            "<IIIIIIII", elf, phoff + index * phentsize
        )
        if p_type == 1:
            segments.append((p_offset, p_vaddr, p_filesz))
    return segments


def _va_to_offset(segments: list[tuple[int, int, int]], address: int) -> int | None:
    for file_offset, virtual_address, file_size in segments:
        if virtual_address <= address < virtual_address + file_size:
            return file_offset + address - virtual_address
    return None


def _path_at(elf: bytes, segments: list[tuple[int, int, int]], address: int) -> str | None:
    offset = _va_to_offset(segments, address)
    if offset is None:
        return None
    end = elf.find(b"\0", offset, min(len(elf), offset + 260))
    if end < 0 or end == offset:
        return None
    raw = elf[offset:end]
    if any(byte < 0x20 or byte >= 0x7F for byte in raw) or b"/" not in raw:
        return None
    try:
        return raw.decode("ascii")
    except UnicodeDecodeError:
        return None


def read_index(executable: Path, rpk_size: int) -> list[RpkEntry]:
    elf = executable.read_bytes()
    segments = _load_segments(elf)
    best: list[RpkEntry] = []
    current: list[RpkEntry] = []
    for offset in range(0, len(elf) - 11, 4):
        pointer, sector, size = struct.unpack_from("<III", elf, offset)
        name = _path_at(elf, segments, pointer)
        valid = (
            name is not None
            and size > 0
            and sector * SECTOR_SIZE + size <= rpk_size
            and (not current or sector >= current[-1].sector)
        )
        if valid:
            if current and offset != current[-1].table_offset + 12:
                current = []
            current.append(RpkEntry(name, sector, size, offset))
            if len(current) > len(best):
                best = current.copy()
        elif current and offset == current[-1].table_offset + 12:
            current = []
    if len(best) < 100:
        raise ValueError("Could not locate the RPK index in the executable")
    return best


def extract(rpk: Path, executable: Path, output: Path, suffix: str | None = None) -> list[RpkEntry]:
    entries = read_index(executable, rpk.stat().st_size)
    output.mkdir(parents=True, exist_ok=True)
    with rpk.open("rb") as source:
        for entry in entries:
            if suffix and not entry.name.casefold().endswith(suffix.casefold()):
                continue
            target = output / Path(entry.name)
            target.parent.mkdir(parents=True, exist_ok=True)
            source.seek(entry.offset)
            target.write_bytes(source.read(entry.size))
    return entries

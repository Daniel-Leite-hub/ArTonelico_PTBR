from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path


SECTOR = 2048


@dataclass(frozen=True)
class IsoEntry:
    path: str
    extent: int
    size: int
    is_dir: bool


def _record(record: bytes) -> tuple[int, int, bool, bytes]:
    extent = struct.unpack_from("<I", record, 2)[0]
    size = struct.unpack_from("<I", record, 10)[0]
    return extent, size, bool(record[25] & 2), record[33 : 33 + record[32]]


def list_files(path: Path) -> list[IsoEntry]:
    with path.open("rb") as fp:
        descriptor = None
        for sector in range(16, 64):
            fp.seek(sector * SECTOR)
            item = fp.read(SECTOR)
            if item[1:6] == b"CD001" and item[0] == 1:
                descriptor = item
                break
        if descriptor is None:
            raise ValueError("A imagem não possui um volume ISO9660 válido")
        root = descriptor[156 : 156 + descriptor[156]]
        extent, size, _, _ = _record(root)
        output: list[IsoEntry] = []

        def walk(dir_extent: int, dir_size: int, prefix: str) -> None:
            fp.seek(dir_extent * SECTOR)
            data = fp.read(dir_size)
            cursor = 0
            while cursor < len(data):
                length = data[cursor]
                if not length:
                    cursor = ((cursor // SECTOR) + 1) * SECTOR
                    continue
                child_extent, child_size, is_dir, raw = _record(data[cursor : cursor + length])
                cursor += length
                if raw in (b"\0", b"\1"):
                    continue
                name = raw.decode("ascii", errors="replace").split(";", 1)[0]
                child_path = f"{prefix}/{name}" if prefix else name
                output.append(IsoEntry(child_path, child_extent, child_size, is_dir))
                if is_dir:
                    walk(child_extent, child_size, child_path)

        walk(extent, size, "")
        return output


def find(path: Path, name: str) -> IsoEntry:
    wanted = name.replace("\\", "/").casefold()
    for entry in list_files(path):
        if entry.path.casefold() == wanted:
            return entry
    raise FileNotFoundError(name)


def read_entry(path: Path, entry: IsoEntry) -> bytes:
    with path.open("rb") as fp:
        fp.seek(entry.extent * SECTOR)
        return fp.read(entry.size)

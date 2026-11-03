from __future__ import annotations

import argparse
import struct
from dataclasses import dataclass
from pathlib import Path


SECTOR = 2048


@dataclass
class Entry:
    path: str
    extent: int
    size: int
    is_dir: bool


def u32_both(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def parse_record(record: bytes) -> tuple[int, int, bool, bytes]:
    extent = u32_both(record, 2)
    size = u32_both(record, 10)
    is_dir = bool(record[25] & 2)
    name_len = record[32]
    name = record[33 : 33 + name_len]
    return extent, size, is_dir, name


def clean_name(raw: bytes, joliet: bool) -> str:
    if joliet:
        name = raw.decode("utf-16-be", errors="replace")
    else:
        name = raw.decode("ascii", errors="replace")
    return name.split(";", 1)[0]


def walk(fp, extent: int, size: int, prefix: str, joliet: bool, out: list[Entry]) -> None:
    fp.seek(extent * SECTOR)
    payload = fp.read(size)
    offset = 0
    while offset < len(payload):
        length = payload[offset]
        if not length:
            offset = ((offset // SECTOR) + 1) * SECTOR
            continue
        record = payload[offset : offset + length]
        child_extent, child_size, is_dir, raw_name = parse_record(record)
        offset += length
        if raw_name in (b"\x00", b"\x01"):
            continue
        name = clean_name(raw_name, joliet)
        path = f"{prefix}/{name}" if prefix else name
        entry = Entry(path, child_extent, child_size, is_dir)
        out.append(entry)
        if is_dir:
            walk(fp, child_extent, child_size, path, joliet, out)


def list_iso(path: Path) -> list[Entry]:
    with path.open("rb") as fp:
        selected = None
        joliet = False
        for sector in range(16, 64):
            fp.seek(sector * SECTOR)
            desc = fp.read(SECTOR)
            if len(desc) < SECTOR or desc[1:6] != b"CD001":
                continue
            dtype = desc[0]
            if dtype == 2 and desc[88:91] in (b"%/@", b"%/C", b"%/E"):
                selected = desc
                joliet = True
                break
            if dtype == 1 and selected is None:
                selected = desc
            if dtype == 255:
                break
        if selected is None:
            raise RuntimeError("No ISO9660 volume descriptor found")
        root_len = selected[156]
        extent, size, _, _ = parse_record(selected[156 : 156 + root_len])
        entries: list[Entry] = []
        walk(fp, extent, size, "", joliet, entries)
        return entries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("iso", type=Path)
    parser.add_argument("--tsv", action="store_true")
    parser.add_argument("--extract", metavar="ISO_PATH")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    entries = list_iso(args.iso)
    if args.extract:
        wanted = args.extract.replace("\\", "/").lstrip("/").casefold()
        entry = next((item for item in entries if item.path.casefold() == wanted), None)
        if entry is None or entry.is_dir:
            raise SystemExit(f"File not found in ISO: {args.extract}")
        output = args.output or Path(Path(entry.path).name)
        output.parent.mkdir(parents=True, exist_ok=True)
        with args.iso.open("rb") as src, output.open("wb") as dst:
            src.seek(entry.extent * SECTOR)
            remaining = entry.size
            while remaining:
                chunk = src.read(min(1024 * 1024, remaining))
                if not chunk:
                    raise EOFError(entry.path)
                dst.write(chunk)
                remaining -= len(chunk)
        print(output)
        return
    for entry in entries:
        if args.tsv:
            print(f"{'D' if entry.is_dir else 'F'}\t{entry.size}\t{entry.extent}\t{entry.path}")
        else:
            print(f"{'D' if entry.is_dir else 'F'} {entry.size:12d} {entry.extent:8d} {entry.path}")


if __name__ == "__main__":
    main()

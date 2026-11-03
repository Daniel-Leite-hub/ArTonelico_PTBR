from __future__ import annotations

import hashlib
import struct
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from artonelico_tool.evd import parse
from artonelico_tool.iso import SECTOR, find, read_entry
from artonelico_tool.portuguese_font import ACCENT_TO_ALIAS
from artonelico_tool.rpk import read_index


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Ar tonelico - Melody of Elemia (Undub).iso"
DEFAULT_OUTPUT = ROOT / "testes pt br" / "Ar tonelico - PTBR fonte portuguesa marcadores locais.iso"
TARGETS = {"Event/107.evd": 5, "Event/108.evd": 0}


def index_for(iso: Path):
    executable_entry = find(iso, "SLUS_214.45")
    rpk_entry = find(iso, "RPK.BIN")
    executable = read_entry(iso, executable_entry)
    with tempfile.NamedTemporaryFile(suffix=".elf", delete=False) as temporary:
        temporary.write(executable)
        temporary_path = Path(temporary.name)
    try:
        index = read_index(temporary_path, rpk_entry.size)
    finally:
        temporary_path.unlink(missing_ok=True)
    return executable_entry, rpk_entry, executable, index


def hash_range(path: Path, start: int, end: int) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        source.seek(start)
        remaining = end - start
        while remaining:
            block = source.read(min(4 * 1024 * 1024, remaining))
            if not block:
                raise EOFError(path)
            digest.update(block)
            remaining -= len(block)
    return digest.hexdigest()


def main() -> None:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    source_exe_entry, source_rpk, source_exe, source_index = index_for(SOURCE)
    output_exe_entry, output_rpk, output_exe, output_index = index_for(output)
    if (source_exe_entry.extent, source_rpk.extent) != (output_exe_entry.extent, output_rpk.extent):
        raise AssertionError("LBAs principais mudaram")
    source_by_name = {entry.name: entry for entry in source_index}
    output_by_name = {entry.name: entry for entry in output_index}

    expected_exe_offsets = {source_by_name[name].table_offset + 8 for name in TARGETS}
    expected_exe_offsets.add(0x3010A8)
    actual_exe_offsets = {index for index, (before, after) in enumerate(zip(source_exe, output_exe)) if before != after}
    if not actual_exe_offsets <= {offset + delta for offset in expected_exe_offsets for delta in range(4)}:
        raise AssertionError(f"Mudanças inesperadas no SLUS: {sorted(actual_exe_offsets)}")

    allowed: list[tuple[int, int]] = []
    rpk_base = source_rpk.extent * SECTOR
    for name in (*TARGETS, "fpack/font.fp"):
        entry = source_by_name[name]
        position = source_index.index(entry)
        next_sector = source_index[position + 1].sector if position + 1 < len(source_index) else source_rpk.size // SECTOR
        capacity = (next_sector - entry.sector) * SECTOR
        allowed.append((rpk_base + entry.offset, rpk_base + entry.offset + capacity))
    for offset in expected_exe_offsets:
        allowed.append((source_exe_entry.extent * SECTOR + offset, source_exe_entry.extent * SECTOR + offset + 4))
    allowed.sort()
    cursor = 0
    for start, end in allowed:
        if cursor < start and hash_range(SOURCE, cursor, start) != hash_range(output, cursor, start):
            raise AssertionError(f"Diferença fora das áreas autorizadas: {cursor:#x}-{start:#x}")
        cursor = max(cursor, end)
    if cursor < SOURCE.stat().st_size and hash_range(SOURCE, cursor, SOURCE.stat().st_size) != hash_range(
        output, cursor, output.stat().st_size
    ):
        raise AssertionError("Diferença após a última área autorizada")

    with output.open("rb") as image:
        for name, row_index in TARGETS.items():
            entry = output_by_name[name]
            image.seek(output_rpk.extent * SECTOR + entry.offset)
            row = parse(image.read(entry.size)).dialogues[row_index]
            if row.raw.count(b"#1") != 5:
                raise AssertionError(f"{name}:{row_index} não possui os cinco trechos latinos esperados")
            print(f"{name}:{row_index} bytes={row.encoded_length} raw={row.raw!r}")

    print(f"SLUS bytes alterados: {len(actual_exe_offsets)}")
    print("ISO integra: somente 107.evd, 108.evd, FO_HGGBP e seus campos de tamanho mudaram")
    print(hash_range(output, 0, output.stat().st_size).upper())


if __name__ == "__main__":
    main()

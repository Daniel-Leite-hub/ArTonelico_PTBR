from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from artonelico_tool.evd import parse
from artonelico_tool.rpk import read_index


root = Path("work/extracted/Event")
rows = []
failures = []
for path in sorted(root.glob("*.evd"), key=lambda p: int(p.stem)):
    try:
        evd = parse(path.read_bytes())
        rows.extend((path.name, row) for row in evd.dialogues)
    except Exception as exc:
        failures.append((path.name, str(exc)))
print(f"dialogues={len(rows)} failures={len(failures)}")
print("failures:", failures[:20])
for name, row in rows[:30]:
    print(f"{name}:{row.index} speaker={row.name_id} bytes={row.encoded_length}: {row.text}")

entries = read_index(Path("work/SLUS_214.45"), Path("work/RPK.BIN").stat().st_size)
for entry in entries:
    low = entry.name.casefold()
    if any(word in low for word in ("font", "moji", "mes", "face", "window")):
        print(f"RESOURCE {entry.size:8d} {entry.name}")

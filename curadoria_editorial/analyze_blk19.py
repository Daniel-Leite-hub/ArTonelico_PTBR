import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path("Ferramentas_Traducao")
with open(BASE_DIR / "curadoria_editorial/curadoria_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()
rows = c.execute("SELECT id, event_file, original_bytes, original_jp, original, translation FROM dialogues WHERE id BETWEEN 25514 AND 25801 ORDER BY id").fetchall()
conn.close()

files = {}
for r in rows:
    fid = r[1]
    files.setdefault(fid, []).append(r)

print(f"Total rows: {len(rows)}")
print(f"Files involved:")
for fid, rlist in files.items():
    print(f"  File: {fid} -> IDs {rlist[0][0]} to {rlist[-1][0]} ({len(rlist)} lines)")

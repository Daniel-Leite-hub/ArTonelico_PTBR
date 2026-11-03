import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path("Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

with open(BASE_DIR / "curadoria_editorial/curadoria_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()
rows = c.execute("SELECT id, event_file, original_bytes, original_jp, original, translation FROM dialogues WHERE id BETWEEN 25514 AND 25801 ORDER BY id").fetchall()
conn.close()

with open(BASE_DIR / "curadoria_editorial/blk19_overview.txt", "w", encoding="utf-8") as out:
    for did, ef, limit, jp, en, pt in rows:
        enc = encoded_size(pt or "")
        diff = enc - limit
        status = f"OVERFLOW (+{diff}B)" if diff > 0 else f"OK ({enc}/{limit}B)"
        out.write(f"=== ID {did} | {ef} | Limit: {limit}B | Enc: {enc}B | {status} ===\n")
        out.write(f"JP: {jp}\n")
        out.write(f"EN: {en}\n")
        out.write(f"PT: {pt}\n\n")

print(f"Generated blk19_overview.txt with {len(rows)} lines.")

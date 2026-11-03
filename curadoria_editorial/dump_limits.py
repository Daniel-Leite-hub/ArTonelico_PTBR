import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path("Ferramentas_Traducao")
with open(BASE_DIR / "curadoria_editorial/curadoria_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25514 AND 25801").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial/limits_blk19.json", "w", encoding="utf-8") as f:
    json.dump(limits, f, indent=2)

print(f"Dumped {len(limits)} limits to limits_blk19.json.")

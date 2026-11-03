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
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25514 AND 25801").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial/blocos/BLK_SYS_019_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

overflows = []
for d in input_data["dialogues"]:
    did = d["id"]
    limit = limits.get(did, 0)
    pt = d.get("current_ptbr", "")
    enc = encoded_size(pt)
    if enc > limit:
        overflows.append((did, enc, limit, enc - limit, pt))

print(f"Total dialogues: {len(input_data['dialogues'])}")
print(f"Total overflows in current_ptbr: {len(overflows)}")
for did, enc, limit, diff, pt in overflows[:25]:
    print(f"ID {did}: enc {enc}B > limit {limit}B (+{diff}) | {pt[:60]}...")
if len(overflows) > 25:
    print(f"... and {len(overflows) - 25} more.")

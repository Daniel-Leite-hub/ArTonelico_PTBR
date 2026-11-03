import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))

from artonelico_tool.project import encoded_size

with open(BASE_DIR / "curadoria_editorial" / "curadoria_config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

conn = sqlite3.connect(cfg["database_path"])
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25226 AND 25513").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

overflows = []
for d in data["dialogues"]:
    did = d["id"]
    pt = d.get("current_ptbr", "")
    max_b = limits.get(did, 0)
    enc_b = encoded_size(pt)
    if enc_b > max_b:
        overflows.append((did, enc_b, max_b, enc_b - max_b, pt, d.get("original_jp", ""), d.get("original_en", "")))

print(f"Total dialogues: {len(data['dialogues'])}")
print(f"Initial overflows: {len(overflows)}")
for did, enc_b, max_b, diff, pt, jp, en in overflows:
    print(f"ID {did}: enc={enc_b} max={max_b} diff=+{diff}")
    print(f"  JP: {jp}")
    print(f"  EN: {en}")
    print(f"  PT: {pt}\n")

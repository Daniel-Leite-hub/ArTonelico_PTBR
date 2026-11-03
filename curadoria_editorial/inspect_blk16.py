import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))

from artonelico_tool.project import encoded_size

input_path = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_016_input.json"
config_path = BASE_DIR / "curadoria_editorial" / "curadoria_config.json"

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()
rows = c.execute("SELECT id, original_bytes, current_bytes, japanese, english, current_ptbr FROM dialogues WHERE id BETWEEN 24650 AND 24937").fetchall()
conn.close()
db_rows = {r[0]: r[1:] for r in rows}

dialogues = data.get("dialogues", [])
print(f"Total dialogues in input: {len(dialogues)}")
print(f"ID range: {dialogues[0]['id']} to {dialogues[-1]['id']}")

overflow_count = 0
total_bytes_cur = 0
total_bytes_orig = 0

for d in dialogues:
    d_id = d["id"]
    pt = d.get("current_ptbr") or ""
    enc_sz = encoded_size(pt)
    orig_b = d.get("original_bytes") or db_rows[d_id][0]
    total_bytes_cur += enc_sz
    total_bytes_orig += orig_b
    if enc_sz > orig_b:
        overflow_count += 1

print(f"Current overflows: {overflow_count} / {len(dialogues)}")
print(f"Total cur bytes: {total_bytes_cur}, orig bytes: {total_bytes_orig}")

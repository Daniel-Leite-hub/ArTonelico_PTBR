import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
from artonelico_tool.project import encoded_size

conn = sqlite3.connect(BASE_DIR / "ArTonelico_PTBR.atproj")
cur = conn.cursor()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_034_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

dialogues = data["dialogues"]
print(f"Total dialogues in input: {len(dialogues)}")

files = {}
overflows_current = []
for d in dialogues:
    d_id = d["id"]
    ef = d.get("event_file", "unknown")
    files.setdefault(ef, []).append(d)
    
    cur.execute("SELECT original_bytes FROM dialogues WHERE id = ?", (d_id,))
    row = cur.fetchone()
    cap = row[0] if row else 0
    
    cur_text = d.get("current_ptbr", "")
    enc = encoded_size(cur_text) if cur_text else 0
    if cap and enc > cap:
        overflows_current.append((d_id, enc, cap, cur_text))

print("Files breakdown:")
for ef, lines in sorted(files.items()):
    print(f"  {ef}: IDs {lines[0]['id']} to {lines[-1]['id']} ({len(lines)} lines)")

print(f"\nCurrent overflows in current_ptbr: {len(overflows_current)}")
for item in overflows_current[:20]:
    print(f"  ID {item[0]}: enc={item[1]}B > cap={item[2]}B | '{item[3]}'")

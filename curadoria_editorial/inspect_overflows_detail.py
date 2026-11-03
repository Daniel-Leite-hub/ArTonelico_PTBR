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

print("DETALHES DOS 28 OVERFLOWS:\n")
for d in data["dialogues"]:
    d_id = d["id"]
    cur.execute("SELECT original_bytes FROM dialogues WHERE id = ?", (d_id,))
    cap = cur.fetchone()[0]
    pt = d.get("current_ptbr", "")
    enc = encoded_size(pt) if pt else 0
    if enc > cap:
        print(f"ID {d_id} ({d['event_file']}): cap={cap}B, enc={enc}B (over {enc-cap}B, max_chars={(cap-1)//2}, cur_chars={len(pt)})")
        print(f"  JP: {d['original_jp']}")
        print(f"  EN: {d['original_en']}")
        print(f"  PT: {pt}\n")

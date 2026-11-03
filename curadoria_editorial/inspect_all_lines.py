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

for d in data["dialogues"]:
    d_id = d["id"]
    ef = d.get("event_file", "")
    jp = d.get("original_jp", "")
    en = d.get("original_en", "")
    pt = d.get("current_ptbr", "")
    
    cur.execute("SELECT original_bytes FROM dialogues WHERE id = ?", (d_id,))
    cap = cur.fetchone()[0]
    enc = encoded_size(pt) if pt else 0
    over = enc - cap if (cap and enc > cap) else 0
    
    print(f"[{d_id}] {ef} cap={cap}B enc={enc}B over={over}B")
    print(f"  JP: {jp}")
    print(f"  EN: {en}")
    print(f"  PT: {pt}")

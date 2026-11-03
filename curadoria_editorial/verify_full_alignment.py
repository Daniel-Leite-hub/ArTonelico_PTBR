import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

conn = sqlite3.connect(str(BASE_DIR / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj"))
c = conn.cursor()
db_info = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 24650 AND 24937").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_016_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

for d in input_data["dialogues"]:
    d_id = d["id"]
    lim = db_info[d_id]
    jp = d.get("original_jp", "")
    en = d.get("original_en", "")
    pt = d.get("current_ptbr", "")
    print(f"[{d_id}] Lim:{lim}B | JP: {jp}")

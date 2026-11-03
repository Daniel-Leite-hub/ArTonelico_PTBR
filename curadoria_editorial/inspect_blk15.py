import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

conn = sqlite3.connect(str(BASE_DIR / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj"))
c = conn.cursor()
rows = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 24351 AND 24649").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_015_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

overflows = []
for d in data['dialogues']:
    d_id = d['id']
    limit = rows.get(d_id, 0)
    pt = d.get('current_ptbr', '')
    sz = encoded_size(pt)
    if sz > limit:
        overflows.append((d_id, sz, limit, sz - limit, pt, d.get('original_jp', ''), d.get('original_en', '')))

print(f"Total dialogues: {len(data['dialogues'])}")
print(f"Overflows in current_ptbr: {len(overflows)}")
for item in overflows:
    print(f"ID {item[0]}: size={item[1]} limit={item[2]} (+{item[3]}B)")
    print(f"   PT: {item[4]}")
    print(f"   EN: {item[6]}")
    print(f"   JP: {item[5]}")
    print("-" * 50)

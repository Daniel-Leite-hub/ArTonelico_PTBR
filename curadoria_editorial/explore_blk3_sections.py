import json
import sqlite3
import sys

sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
from artonelico_tool.project import encoded_size

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\curadoria_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()

c.execute("""
    SELECT id, event_file, original, original_jp, original_bytes, automatic, reviewed 
    FROM dialogues 
    WHERE id BETWEEN 20883 AND 21170 
    ORDER BY id
""")
rows = c.fetchall()

print(f"Total rows: {len(rows)}")

# Print in groups of files
current_file = None
for r in rows:
    d_id, ef, en, jp, cap, auto, rev = r
    cur = rev or auto or ""
    if ef != current_file:
        current_file = ef
        print(f"\n==================== {ef} ====================")
    sz = encoded_size(cur)
    print(f"[{d_id}] Cap:{cap:3d}B (CurSz:{sz:3d}B) | EN: {en:<28} | JP: {jp:<28} | Cur: {cur}")

conn.close()

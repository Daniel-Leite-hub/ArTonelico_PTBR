import json
import sqlite3
import sys
from pathlib import Path

sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
from artonelico_tool.project import encoded_size

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\curadoria_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()
c.execute("""
    SELECT id, event_file, original, original_jp, original_bytes, automatic, reviewed 
    FROM dialogues 
    WHERE id BETWEEN 21021 AND 21170 
    ORDER BY id
""")
desc_rows = [r for r in c.fetchall() if r[4] > 60]  # Only descriptions
conn.close()

print(f"Total monster descriptions: {len(desc_rows)}")

# Output a clean list of each description with its Cap, CurrPT, and JP
for r in desc_rows:
    d_id, ef, en, jp, cap, auto, rev = r
    cur = rev or auto or ""
    sz = encoded_size(cur)
    print(f"ID {d_id} | Cap: {cap}B | CurrSz: {sz}B")
    print(f"  JP: {jp}")
    print(f"  EN: {en}")
    print(f"  Cur: {cur}\n")

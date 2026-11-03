import sqlite3
import json
import sys
sys.path.insert(0, r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

db_path = r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\release\ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("SELECT id, event_file, original_jp, original, original_bytes, automatic, reviewed FROM dialogues WHERE id BETWEEN 22042 AND 22340 ORDER BY id ASC")
rows = c.fetchall()
conn.close()

print(f"Loaded {len(rows)} rows.")

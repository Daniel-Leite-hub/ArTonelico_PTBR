import json
import sqlite3
import sys
from pathlib import Path

sys.path.append(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao')
import artonelico_tool.project as proj
from curadoria_validate import validate_line

# Database connection to pull exact metadata
with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\curadoria_config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

conn = sqlite3.connect(cfg['database_path'])
c = conn.cursor()
c.execute('SELECT id, event_file, speaker_id, original_jp, original, translation, reviewed, original_bytes FROM dialogues WHERE id BETWEEN 22917 AND 23204 ORDER BY id')
db_rows = {r[0]: r for r in c.fetchall()}

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_SYS_010_input.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

print(f"Loaded {len(db_rows)} database rows and {len(input_data['dialogues'])} input dialogues.")

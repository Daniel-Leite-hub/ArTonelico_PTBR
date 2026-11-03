import json
import sqlite3
import sys

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_038_input.json', 'r', encoding='utf-8') as f:
    inp = json.load(f)

for d in inp['dialogues']:
    c.execute('SELECT original_bytes FROM dialogues WHERE id = ?', (d['id'],))
    ob = c.fetchone()[0]
    d['original_bytes'] = ob

files = {}
for d in inp['dialogues']:
    files.setdefault(d['event_file'], []).append(d)

for ef, lines in files.items():
    print(f"\n==================== {ef} ({lines[0]['id']} - {lines[-1]['id']}) ====================")
    for d in lines:
        cur_sz = encoded_size(d.get('current_ptbr') or '')
        print(f"ID {d['id']:5d} | Cap: {d['original_bytes']:3d}B | Cur: {cur_sz:3d}B")
        print(f"   JP: {d.get('original_jp')}")
        print(f"   EN: {d.get('original_en')}")
        print(f"   PT: {d.get('current_ptbr')}")

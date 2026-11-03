import sys
import json
import sqlite3

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_041_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

files = {}
for d in data['dialogues']:
    fn = d.get('event_file')
    if fn not in files:
        files[fn] = []
    d_id = d['id']
    row = c.execute('SELECT original_bytes, original_jp, original, translation FROM dialogues WHERE id = ?', (d_id,)).fetchone()
    d['orig_b'] = row[0]
    d['orig_jp'] = row[1] or d.get('original_jp', '')
    d['orig_en'] = row[2] or d.get('original_en', '')
    d['cur_pt'] = row[3] or d.get('current_ptbr', '')
    d['cur_sz'] = encoded_size(d['cur_pt'])
    files[fn].append(d)

print('Files breakdown in BLK_SYS_041:')
for fn, dlist in files.items():
    ovs = sum(1 for x in dlist if x['cur_sz'] > x['orig_b'])
    start_id = dlist[0]['id']
    end_id = dlist[-1]['id']
    print(f'File {fn}: {len(dlist)} lines, {ovs} overflows, IDs {start_id}..{end_id}')

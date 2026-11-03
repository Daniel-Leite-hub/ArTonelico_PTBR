# -*- coding: utf-8 -*-
import json
import sqlite3
import sys

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

for d in data['dialogues']:
    d_id = d['id']
    c.execute('SELECT original_bytes FROM dialogues WHERE id = ?', (d_id,))
    row = c.fetchone()
    d['original_bytes'] = row[0] if row else 0
    d['cur_size'] = encoded_size(d.get('current_ptbr') or '')

for i in range(0, len(data['dialogues']), 24):
    chunk = data['dialogues'][i:i+24]
    fn = chunk[0]['event_file']
    ovs = sum(1 for d in chunk if d['cur_size'] > d['original_bytes'])
    print(f"\n=======================================================")
    print(f"FILE {fn} | IDs {chunk[0]['id']}..{chunk[-1]['id']} | Total: {len(chunk)} | Overflows: {ovs}")
    print(f"=======================================================")
    for d in chunk[:6]:
        diff = d['cur_size'] - d['original_bytes']
        flag = f" [OVERFLOW +{diff}B]" if diff > 0 else " [OK]"
        print(f"ID {d['id']:5d} (Cap: {d['original_bytes']:3d}B, Cur: {d['cur_size']:3d}B){flag}")
        print(f"  JP: {d['original_jp']}")
        print(f"  EN: {d['original_en']}")
        print(f"  PT: {d.get('current_ptbr', '')}")

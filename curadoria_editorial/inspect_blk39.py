# -*- coding: utf-8 -*-
import json
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

files = defaultdict(list)
for d in data['dialogues']:
    d_id = d['id']
    c.execute('SELECT original_bytes FROM dialogues WHERE id = ?', (d_id,))
    row = c.fetchone()
    d['original_bytes'] = row[0] if row else 0
    d['cur_size'] = encoded_size(d.get('current_ptbr') or '')
    files[d['event_file']].append(d)

print(f"Total dialogues: {len(data['dialogues'])}")
for fn, lines in sorted(files.items()):
    ov_count = sum(1 for l in lines if l['cur_size'] > l['original_bytes'])
    print(f"\n=== File: {fn} ({len(lines)} lines, IDs {lines[0]['id']}..{lines[-1]['id']}) - Overflows: {ov_count} ===")
    for l in lines[:3]:
        print(f"  [{l['id']}] (cap {l['original_bytes']}B, cur {l['cur_size']}B)")
        print(f"    JP: {l['original_jp']}")
        print(f"    EN: {l['original_en']}")
        print(f"    PT: {l['current_ptbr']}")

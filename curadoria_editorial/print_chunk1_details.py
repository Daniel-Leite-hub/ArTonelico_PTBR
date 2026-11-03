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

lines = [d for d in data['dialogues'] if 31269 <= d['id'] <= 31316]
for d in lines:
    c.execute('SELECT original_bytes FROM dialogues WHERE id = ?', (d['id'],))
    ob = c.fetchone()[0]
    cur = d.get('current_ptbr', '')
    sz = encoded_size(cur)
    diff = sz - ob
    ov = f"OVERFLOW +{diff}B" if diff > 0 else "OK"
    print(f"ID: {d['id']} | Cap: {ob:3d}B | Cur: {sz:3d}B ({ov})")
    print(f"  JP: {d['original_jp']}")
    print(f"  EN: {d['original_en']}")
    print(f"  PT: {cur}")

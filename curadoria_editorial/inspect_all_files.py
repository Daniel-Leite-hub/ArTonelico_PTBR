# -*- coding: utf-8 -*-
import json
import sqlite3
import sys

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for f_idx in range(481, 493):
    fn = f"SLUS/TEXT/{f_idx:04d}"
    chunk = [d for d in data['dialogues'] if d['event_file'] == fn]
    print(f"\n==================== {fn} ({chunk[0]['id']}..{chunk[-1]['id']}) ====================")
    # Check topics by looking at first lines of conversation pairs
    for i in [0, 3, 6, 9, 12, 15, 18, 21]:
        if i < len(chunk):
            d = chunk[i]
            print(f"[{d['id']}] JP: {d['original_jp']}")
            print(f"       EN: {d['original_en']}")

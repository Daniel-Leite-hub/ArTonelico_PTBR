# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for f_idx in range(484, 490):
    fn = f"SLUS/TEXT/{f_idx:04d}"
    group = [d for d in data['dialogues'] if d['event_file'] == fn]
    print(f"\n==================== {fn} ({group[0]['id']}..{group[-1]['id']}) ====================")
    for d in group:
        print(f"[{d['id']}] {d['original_jp']}")

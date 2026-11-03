# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_058_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for item in d['dialogues']:
    if item['event_file'] == 'Event/109.evd':
        print(f"[{item['id']}] {item['speaker']}")
        print(f"  JP: {repr(item['original_jp'])}")
        print(f"  EN: {repr(item['original_en'])}")
        print(f"  PT: {repr(item['current_ptbr'])}")
        print("-" * 50)

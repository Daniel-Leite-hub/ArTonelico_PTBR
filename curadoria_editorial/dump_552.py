# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_086_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data['dialogues']:
    if d['event_file'] == 'Event/552.evd':
        print(f"[{d['id']}] {d['speaker']}:")
        print(f"  JP: {d['original_jp']}")
        print(f"  EN: {d['original_en']}")
        print(f"  PT: {d['current_ptbr']}")

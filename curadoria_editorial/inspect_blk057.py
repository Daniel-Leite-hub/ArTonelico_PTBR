# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_057_input.json', encoding='utf-8') as f:
    d = json.load(f)

for ef in ['Event/297.evd', 'Event/542.evd', 'Event/739.evd', 'Event/444.evd']:
    lines = [x for x in d['dialogues'] if x['event_file'] == ef]
    print(f"=== {ef} ({len(lines)} lines: {lines[0]['id']}..{lines[-1]['id']}) ===")
    speakers = list(dict.fromkeys(x['speaker'] for x in lines))
    print('Speakers in scene:', speakers)
    for x in lines[:6]:
        print(f"  [{x['id']}] {x['speaker']}:")
        print(f"    JP: {x['original_jp']}")
        print(f"    EN: {x['original_en']}")
        print(f"    PT: {x['current_ptbr']}")

# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_086_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data['dialogues']:
    if d['event_file'] == 'Event/552.evd' and 19440 <= d['id'] <= 19505:
        print(f"ID: {d['id']} | Speaker: {d['speaker']} ({d.get('speaker_id')})")
        print(f"  JP: {repr(d['original_jp'])}")
        print(f"  EN: {repr(d['original_en'])}")
        print(f"  PT: {repr(d['current_ptbr'])}")
        print("-" * 50)

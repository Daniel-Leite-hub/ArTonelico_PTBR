# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_076_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

events = {}
for d in data['dialogues']:
    ev = d['event_file']
    if ev not in events:
        events[ev] = []
    events[ev].append(d)

for ev, lines in events.items():
    print("=" * 80)
    print(f"EVENT: {ev} ({len(lines)} lines, IDs {lines[0]['id']}..{lines[-1]['id']})")
    print("=" * 80)
    for l in lines:
        print(f"[{l['id']}] {l['speaker']}:")
        print(f"  JP: {l['original_jp']}")
        print(f"  EN: {l['original_en']}")
        print(f"  PT: {l['current_ptbr']}")

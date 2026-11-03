# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_086_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def show_event(event_file):
    print(f"=== {event_file} ===")
    for d in data['dialogues']:
        if d['event_file'] == event_file:
            print(f"ID: {d['id']} | Speaker: {d['speaker']} ({d.get('speaker_id')})")
            print(f"  JP: {repr(d['original_jp'])}")
            print(f"  EN: {repr(d['original_en'])}")
            print(f"  PT: {repr(d['current_ptbr'])}")
            print("-" * 50)

if __name__ == "__main__":
    import sys
    ev = sys.argv[1] if len(sys.argv) > 1 else 'Event/448.evd'
    show_event(ev)

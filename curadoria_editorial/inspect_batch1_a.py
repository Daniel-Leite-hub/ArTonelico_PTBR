import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_067_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

lines = [x for x in d['dialogues'] if x['event_file'] == 'Event/118.evd']

for x in lines[:35]:
    print(f"ID {x['id']} | {x['speaker']} ({x['speaker_id']})")
    print(f"  JP: {repr(x['original_jp'])}")
    print(f"  EN: {repr(x['original_en'])}")
    print(f"  PT: {repr(x['current_ptbr'])}")

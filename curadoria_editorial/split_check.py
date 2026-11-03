import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_067_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

lines_118 = [x for x in d['dialogues'] if x['event_file'] == 'Event/118.evd']
lines_294 = [x for x in d['dialogues'] if x['event_file'] == 'Event/294.evd']
lines_642 = [x for x in d['dialogues'] if x['event_file'] == 'Event/642.evd']

print(f"118: {len(lines_118)}, 294: {len(lines_294)}, 642: {len(lines_642)}")

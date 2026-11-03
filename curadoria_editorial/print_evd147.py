import json

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_079_input.json', encoding='utf-8'))
for d in data['dialogues']:
    if d['event_file'] == 'Event/147.evd':
        print(f"--- ID {d['id']} | {d.get('speaker')} ---")
        print(f"JP: {d.get('original_jp')}")
        print(f"EN: {d.get('original_en')}")
        print(f"PT: {d.get('current_ptbr')}\n")

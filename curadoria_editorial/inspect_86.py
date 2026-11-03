import json
data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_086_output.json', encoding='utf-8'))
for d in data['dialogues']:
    if d['id'] in range(19360, 19400):
        print(f"ID {d['id']} | {d['speaker']} | {d['event_file']}")
        print(f"  JP: {d['original_jp']}")
        print(f"  PT: {d['curated_ptbr']}")

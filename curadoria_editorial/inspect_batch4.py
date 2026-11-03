import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_087_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for x in d['dialogues']:
    if 19737 <= x['id'] <= 19807:
        print(f"[{x['id']}] {x['speaker']} ({x['speaker_id']}):")
        print(f"  JP: {x['original_jp']}")
        print(f"  EN: {x['original_en']}")
        print(f"  PT: {x['current_ptbr']}")

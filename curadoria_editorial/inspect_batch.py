import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_045_input.json', encoding='utf-8') as f:
    data = json.load(f)

dialogues = data['dialogues']

def dump_range(start, end):
    for i in range(start, min(end, len(dialogues))):
        d = dialogues[i]
        print(f"=== [{i:03d}|ID {d['id']}] Speaker: {d.get('speaker')} ===")
        print(f"JP: {d.get('original_jp')}")
        print(f"EN: {d.get('original_en')}")
        print(f"PT: {d.get('current_ptbr')}")
        print()

dump_range(225, 279)

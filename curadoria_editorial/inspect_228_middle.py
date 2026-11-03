import json

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_079_input.json', encoding='utf-8'))
for d in data['dialogues']:
    if 17964 <= d['id'] <= 17990:
        print(f"[{d['id']}] {d.get('speaker')}:")
        print(f"  JP: {d.get('original_jp')}")
        print(f"  EN: {d.get('original_en')}")
        print(f"  PT: {d.get('current_ptbr')}")

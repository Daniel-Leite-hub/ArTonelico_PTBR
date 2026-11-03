import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_088_output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data['dialogues'][:15]:
    print(f"[{d['id']}] JP: {d['original_jp']!r}")
    print(f"       PT: {d['curated_ptbr']!r}")

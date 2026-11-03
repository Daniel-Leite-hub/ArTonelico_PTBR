import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_086_output.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for x in d['dialogues'][:20]:
    if 'CR' in x['original_jp'] or '\n' in x['curated_ptbr']:
        print(f"ID {x['id']}:")
        print("  JP:  ", repr(x['original_jp']))
        print("  EN:  ", repr(x['original_en']))
        print("  PTBR:", repr(x['curated_ptbr']))

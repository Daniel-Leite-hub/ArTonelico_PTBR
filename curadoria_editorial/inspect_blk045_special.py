import json
import re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_045_input.json', encoding='utf-8') as f:
    data = json.load(f)

dialogues = data['dialogues']

for d in dialogues:
    d_id = d['id']
    en = d.get('original_en', '')
    jp = d.get('original_jp', '')
    pt = d.get('current_ptbr', '')

    for s, name in [(jp, 'JP'), (en, 'EN'), (pt, 'PT')]:
        if '#' in s:
            print(f"[#] ID {d_id} in {name}: {s}")
        if '{' in s or '}' in s:
            print(f"[BRACE] ID {d_id} in {name}: {s}")
        if '<' in s or '>' in s:
            print(f"[ANGLE] ID {d_id} in {name}: {s}")
        if '【' in s or '】' in s:
            print(f"[LENTICULAR] ID {d_id} in {name}: {s}")

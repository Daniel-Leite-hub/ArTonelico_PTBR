import json, re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_075_input.json', encoding='utf-8') as f:
    data = json.load(f)

for d in data['dialogues']:
    for fld in ['original_jp', 'original_en', 'current_ptbr']:
        txt = d.get(fld, '')
        if any(c in txt for c in ['[', ']', '%', '@', '#', '{', '}', '<', '>', '\\']):
            print(f"ID {d['id']} ({fld}): {txt!r}")

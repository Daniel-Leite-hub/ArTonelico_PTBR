# -*- coding: utf-8 -*-
import json, re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_076_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

found = False
for d in data['dialogues']:
    for fld in ['original_jp', 'original_en', 'current_ptbr']:
        val = d.get(fld, '')
        tags = re.findall(r'(%[sd]|%[0-9]+\$[sd]|\{[^}]+\}|\[[0-9A-Fa-f]{4}\]|@[0-9A-Fa-f]+|#[0-9]+)', val)
        if tags:
            print(f"Line {d['id']} ({fld}): {tags}")
            found = True

if not found:
    print("No variable or bracket tags (%s, %d, [00XX], etc.) found in any line of BLK_EVD_076!")

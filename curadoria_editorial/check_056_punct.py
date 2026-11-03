# -*- coding: utf-8 -*-
import json

with open(r'Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_056_output.json', encoding='utf-8') as f:
    d = json.load(f)

starts_with_dots = 0
after_newline_dots = 0
for item in d['dialogues']:
    trad = item['curated_ptbr']
    parts = trad.split('\n')
    if parts[0].startswith('...'):
        starts_with_dots += 1
    for i, p in enumerate(parts[1:], 1):
        if p.startswith(('.', ',', '!', '?', ';', ':', '-', '—')):
            after_newline_dots += 1
            print(f"Line {i} starts with punct in ID {item['id']}: {trad!r}")

print(f"Starts with dots at line 0: {starts_with_dots}")
print(f"After newline starts with punct: {after_newline_dots}")

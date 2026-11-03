import json
import re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_027_input.json', encoding='utf-8') as f:
    data = json.load(f)

for d in data['dialogues']:
    for fld in ['original_jp', 'original_en', 'current_ptbr']:
        txt = d[fld]
        vars_found = re.findall(r'%[sSdD0-9]+', txt)
        hex_found = re.findall(r'\[[0-9A-Fa-f]{4}\]', txt)
        at_found = re.findall(r'@[0-9A-Fa-f]+', txt)
        im_found = re.findall(r'IM[0-9]{2}', txt)
        hymm_found = re.findall(r'#[0-9]', txt)
        if any([vars_found, hex_found, at_found, im_found, hymm_found]):
            print(f"ID {d['id']} ({fld}): vars={vars_found}, hex={hex_found}, at={at_found}, im={im_found}, hymm={hymm_found}")

import json
import re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_087_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for item in d['dialogues']:
    jp = item['original_jp']
    en = item['original_en']
    pt = item['current_ptbr']
    for b in ['【', '】', '「', '」', '『', '』', '«', '»', '[', ']', '{', '}', '<', '>']:
        if b in jp or b in en or b in pt:
            print(f"ID {item['id']}: JP='{jp}' | EN='{en}' | PT='{pt}'")
            break

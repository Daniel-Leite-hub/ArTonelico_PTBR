# -*- coding: utf-8 -*-
import json

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_043_input.json', 'r', encoding='utf-8'))
for d in data['dialogues'][43:120]:
    print(f"ID {d['id']} | {d.get('speaker')}")
    print(f"  JP: {d.get('original_jp')}")
    print(f"  EN: {d.get('original_en')}")
    print(f"  PT: {d.get('current_ptbr')}\n")

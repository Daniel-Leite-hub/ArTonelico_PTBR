# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data['dialogues']:
    if 31389 <= d['id'] <= 31412:
        print(f"[{d['id']}] {d['original_jp']}")

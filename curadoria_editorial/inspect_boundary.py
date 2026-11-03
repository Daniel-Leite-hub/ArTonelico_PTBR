# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data['dialogues']:
    if 31408 <= d['id'] <= 31415:
        print(f"[{d['id']}] {d['event_file']} | {d['original_jp']}")

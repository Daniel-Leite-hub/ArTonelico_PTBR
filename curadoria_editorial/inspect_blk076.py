# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_075_output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i in range(5):
    d = data['dialogues'][i]
    print(f"--- Line {d['id']} ({d['speaker']}) ---")
    print("JP:", repr(d['original_jp']))
    print("curated_ptbr:", repr(d['curated_ptbr']))
    print("notes:", repr(d.get('notes')))

# -*- coding: utf-8 -*-
import json

data = json.load(open('G:/JOGO/PS2/Ar tonelico - Melody of Elemia (Undub)/Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_083_output.json', encoding='utf-8'))
for d in data['dialogues']:
    if '『' in d['original_jp'] or '【' in d['original_jp']:
        print(f"ID: {d['id']}")
        print(f"  JP: {repr(d['original_jp'])}")
        print(f"  PT: {repr(d['curated_ptbr'])}")
        if len(d['curated_ptbr']) > 0:
            pass

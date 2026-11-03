# -*- coding: utf-8 -*-
import json, glob

for f in sorted(glob.glob('G:/JOGO/PS2/Ar tonelico - Melody of Elemia (Undub)/Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_*_output.json'))[-5:]:
    data = json.load(open(f, encoding='utf-8'))
    for d in data['dialogues']:
        if '『' in d['original_jp']:
            print(f"{f[-19:]} ID {d['id']}: JP: {d['original_jp']} -> PT: {d.get('curated_ptbr')}")
            break

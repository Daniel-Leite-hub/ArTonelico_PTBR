# -*- coding: utf-8 -*-
import json, glob

for f in sorted(glob.glob('G:/JOGO/PS2/Ar tonelico - Melody of Elemia (Undub)/Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_*_output.json')):
    data = json.load(open(f, encoding='utf-8'))
    for d in data.get('dialogues', []):
        t = d.get('curated_ptbr', '')
        jp = d.get('original_jp', '')
        if 'リンカ' in jp or 'ブースター' in jp or '寺院' in jp:
            print(f"{f[-19:]} ID {d['id']}: JP: {jp} -> PT: {t}")

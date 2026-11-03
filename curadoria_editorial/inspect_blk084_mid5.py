# -*- coding: utf-8 -*-
import json

data = json.load(open('G:/JOGO/PS2/Ar tonelico - Melody of Elemia (Undub)/Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_084_input.json', encoding='utf-8'))

for d in data['dialogues'][150:200]:
    print(f"[{d['id']}] {d.get('speaker')}:")
    print(f"  JP: {d.get('original_jp')}")
    print(f"  EN: {d.get('original_en')}")
    print(f"  BR: {d.get('current_ptbr')}")

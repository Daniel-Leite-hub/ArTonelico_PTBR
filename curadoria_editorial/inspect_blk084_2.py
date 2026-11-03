# -*- coding: utf-8 -*-
import json

data = json.load(open('G:/JOGO/PS2/Ar tonelico - Melody of Elemia (Undub)/Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_084_input.json', encoding='utf-8'))

print("=== EVENT 2: Event/956.evd (18959 - 18995) ===")
for d in data['dialogues'][46:83]:
    print(f"[{d['id']}] {d.get('speaker')}:")
    print(f"  JP: {d.get('original_jp')}")
    print(f"  EN: {d.get('original_en')}")
    print(f"  BR: {d.get('current_ptbr')}")

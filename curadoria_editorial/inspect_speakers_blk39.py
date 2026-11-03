# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i in range(0, len(data['dialogues']), 24):
    group = data['dialogues'][i:i+24]
    fn = group[0]['event_file']
    print(f"\n==================== {fn} (IDs {group[0]['id']}..{group[-1]['id']}) ====================")
    # Print lines that reveal speakers or character interactions
    for d in group:
        # Check mentions of names or characteristic speech particles (e.g. なの, わよ, だぜ, ライナー, オリカスタ, ミーシャ, シュレリア)
        jp = d['original_jp']
        en = d['original_en']
        print(f"[{d['id']}] {jp}")

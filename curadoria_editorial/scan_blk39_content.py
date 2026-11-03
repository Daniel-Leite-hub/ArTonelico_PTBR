# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/blk39_full_scan.txt', 'w', encoding='utf-8') as out:
    for i in range(0, len(data['dialogues']), 24):
        group = data['dialogues'][i:i+24]
        fn = group[0]['event_file']
        out.write(f"\n==================== {fn} (IDs {group[0]['id']}..{group[-1]['id']}) ====================\n")
        for d in group:
            out.write(f"[{d['id']}] JP: {d['original_jp']}\n")
            out.write(f"       EN: {d['original_en']}\n")
            out.write(f"       PT: {d.get('current_ptbr', '')}\n")

print("Wrote blk39_full_scan.txt successfully")

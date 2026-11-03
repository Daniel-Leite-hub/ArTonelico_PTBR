# -*- coding: utf-8 -*-
import json

with open(r'Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_078_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'Ferramentas_Traducao/curadoria_editorial/blk078_raw.txt', 'w', encoding='utf-8') as out:
    for d in data['dialogues']:
        out.write(f"[{d['id']}] ({d.get('event_file')}) {d.get('speaker')}:\n")
        out.write(f"  JP: {d.get('original_jp')}\n")
        out.write(f"  EN: {d.get('original_en')}\n")
        out.write(f"  PT: {d.get('current_ptbr')}\n\n")

print("Exported", len(data['dialogues']), "dialogues to blk078_raw.txt")

# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_057_input.json', encoding='utf-8') as f:
    d = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/blk057_full_dump.txt', 'w', encoding='utf-8') as out:
    for item in d['dialogues']:
        out.write(f"[{item['id']}] ({item['event_file']}) {item['speaker']} (id={item.get('speaker_id')}):\n")
        out.write(f"  JP: {item['original_jp']}\n")
        out.write(f"  EN: {item['original_en']}\n")
        out.write(f"  PT_RAW: {item['current_ptbr']}\n\n")

print(f"Dumped {len(d['dialogues'])} items to blk057_full_dump.txt.")

# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_056_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/blocos/dump_056.txt', 'w', encoding='utf-8') as out:
    for item in d['dialogues']:
        out.write(f"ID: {item['id']} | File: {item.get('event_file')} | Speaker: {item.get('speaker')} (ID {item.get('speaker_id')})\n")
        out.write(f"  JP: {item.get('original_jp')}\n")
        out.write(f"  EN: {item.get('original_en')}\n")
        out.write(f"  PT: {item.get('current_ptbr')}\n\n")

print(f"Dumped {len(d['dialogues'])} dialogues to dump_056.txt")

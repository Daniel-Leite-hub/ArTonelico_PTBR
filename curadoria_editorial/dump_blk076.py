# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_076_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/blk076_full_dump.txt', 'w', encoding='utf-8') as out:
    for d in data['dialogues']:
        out.write(f"=== ID: {d['id']} | Event: {d['event_file']} | Speaker: {d['speaker']} (ID: {d.get('speaker_id')}) ===\n")
        out.write(f"JP: {d['original_jp']}\n")
        out.write(f"EN: {d['original_en']}\n")
        out.write(f"PT: {d['current_ptbr']}\n\n")

print(f"Dumped {len(data['dialogues'])} lines to blk076_full_dump.txt")

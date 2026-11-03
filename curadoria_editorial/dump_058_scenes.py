# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_058_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = data['dialogues']
print(f"Total lines: {len(lines)}")

with open('Ferramentas_Traducao/curadoria_editorial/dump_058.txt', 'w', encoding='utf-8') as out:
    for d in lines:
        out.write(f"ID: {d['id']} | File: {d['event_file']} | Speaker: {d['speaker']} (ID: {d.get('speaker_id')})\n")
        out.write(f"  JP: {d['original_jp']}\n")
        out.write(f"  EN: {d['original_en']}\n")
        out.write(f"  PT: {d['current_ptbr']}\n\n")

print("Dumped to dump_058.txt successfully.")

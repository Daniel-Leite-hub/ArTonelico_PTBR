# -*- coding: utf-8 -*-
import json

input_path = r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_010_input.json'
with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

output_path = r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blk010_raw_dump.txt'
with open(output_path, 'w', encoding='utf-8') as out:
    for d in data['dialogues']:
        out.write(f"=== ID: {d['id']} | Event: {d['event_file']} | Speaker: {d['speaker']} (ID: {d.get('speaker_id')}) ===\n")
        out.write(f"JP: {d['original_jp']}\n")
        out.write(f"EN: {d['original_en']}\n")
        out.write(f"PT: {d['current_ptbr']}\n\n")

print(f"Successfully dumped {len(data['dialogues'])} dialogues to {output_path}")

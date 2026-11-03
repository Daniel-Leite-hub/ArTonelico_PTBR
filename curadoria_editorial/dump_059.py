# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_059_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

dialogues = d['dialogues']

def dump_range(start_id, end_id, filename):
    subset = [x for x in dialogues if start_id <= x['id'] <= end_id]
    with open(filename, 'w', encoding='utf-8') as out:
        for item in subset:
            out.write(f"=== ID {item['id']} | {item['event_file']} | Speaker: {item.get('speaker')} (ID: {item.get('speaker_id')}) ===\n")
            out.write(f"JP: {item['original_jp']}\n")
            out.write(f"EN: {item['original_en']}\n")
            out.write(f"PT: {item.get('current_ptbr') or item.get('curated_ptbr') or item.get('text_ptbr')}\n\n")

dump_range(13702, 13734, 'Ferramentas_Traducao/curadoria_editorial/blocos/evd_857_dump.txt')
dump_range(13735, 13792, 'Ferramentas_Traducao/curadoria_editorial/blocos/evd_14_dump.txt')
dump_range(13793, 13815, 'Ferramentas_Traducao/curadoria_editorial/blocos/evd_485_dump.txt')
dump_range(13816, 13854, 'Ferramentas_Traducao/curadoria_editorial/blocos/evd_205_dump.txt')
dump_range(13855, 13916, 'Ferramentas_Traducao/curadoria_editorial/blocos/evd_808_dump.txt')
print('Dumped 5 scene files successfully.')

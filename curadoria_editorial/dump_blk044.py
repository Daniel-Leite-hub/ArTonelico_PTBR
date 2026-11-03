# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_044_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/blk044_dump.txt', 'w', encoding='utf-8') as out:
    for item in d['dialogues']:
        out.write(f"=== ID: {item['id']} | Event: {item.get('event_file')} | Speaker: {item.get('speaker')} ===\n")
        out.write(f"JP: {item.get('original_jp')}\n")
        out.write(f"EN: {item.get('original_en')}\n")
        out.write(f"PT: {item.get('text_ptbr')}\n\n")

print('Dumped 209 lines to blk044_dump.txt')

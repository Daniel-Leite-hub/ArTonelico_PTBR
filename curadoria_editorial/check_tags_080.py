# -*- coding: utf-8 -*-
import json, re

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_080_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Checking for tags in dialogues:")
for d in data['dialogues']:
    for p in [r'%[sd]', r'\{.*?\}', r'\[.*?\]', r'＠.*?#', r'\x1b']:
        if re.search(p, d['original_jp']) or re.search(p, d['original_en']):
            print(f"ID {d['id']} has tag/pattern {p}: JP={d['original_jp']} || EN={d['original_en']}")

print("Check finished.")

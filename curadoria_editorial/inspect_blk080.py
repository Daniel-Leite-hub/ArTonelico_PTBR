# -*- coding: utf-8 -*-
import json
import sys

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_080_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def show_range(start_id, end_id):
    lines = [d for d in data['dialogues'] if start_id <= d['id'] <= end_id]
    for d in lines:
        print(f"ID: {d['id']} | Speaker: {d['speaker']} (ID {d['speaker_id']}) | File: {d['event_file']}")
        print(f"  JP: {d['original_jp']}")
        print(f"  EN: {d['original_en']}")
        print(f"  PT: {d['current_ptbr']}")
        print("-" * 50)

if __name__ == '__main__':
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 18020
    e = int(sys.argv[2]) if len(sys.argv) > 2 else 18075
    show_range(s, e)

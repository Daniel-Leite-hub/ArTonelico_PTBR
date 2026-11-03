# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_078_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def show_range(start_idx, end_idx):
    for d in data['dialogues'][start_idx:end_idx]:
        print(f"ID {d['id']} | {d.get('speaker')} | {d.get('event_file')}")
        print(f"  JP: {d.get('original_jp')}")
        print(f"  EN: {d.get('original_en')}")
        print(f"  PT: {d.get('current_ptbr')}")
        print("-" * 60)

if __name__ == '__main__':
    import sys
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    e = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    show_range(s, e)

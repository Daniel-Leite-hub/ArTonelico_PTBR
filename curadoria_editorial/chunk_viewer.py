# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_078_input.json', 'r', encoding='utf-8') as f:
    dialogues = json.load(f)['dialogues']

def dump_chunk(s_id, e_id):
    for d in dialogues:
        if s_id <= d['id'] <= e_id:
            print(f"=== ID {d['id']} | {d.get('speaker')} ===")
            print(f"JP: {d.get('original_jp')}")
            print(f"EN: {d.get('original_en')}")
            print(f"PT: {d.get('current_ptbr')}")

if __name__ == '__main__':
    import sys
    dump_chunk(int(sys.argv[1]), int(sys.argv[2]))

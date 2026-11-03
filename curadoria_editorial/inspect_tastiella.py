# -*- coding: utf-8 -*-
import json

for blk in ['021', '026', '027', '048']:
    fpath = f'Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_{blk}_output.json'
    d = json.load(open(fpath, encoding='utf-8'))
    for line in d['dialogues']:
        if line.get('speaker') == 'Tastiella':
            print(f"{blk}: speaker={line.get('speaker')}, JP={line['original_jp'][:30]} | PT={line['curated_ptbr'][:50]}")
            break

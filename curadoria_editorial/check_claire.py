# -*- coding: utf-8 -*-
import glob, json

for f in glob.glob('Ferramentas_Traducao/curadoria_editorial/blocos/*output.json'):
    with open(f, encoding='utf-8') as jf:
        data = json.load(jf)
    for d in data.get('dialogues', []):
        jp = d.get('original_jp', '')
        if 'クレアお姉ちゃん' in jp:
            print(f"[{d['id']}]: JP={jp} | EN={d.get('original_en')} | PT={d.get('curated_ptbr')}")

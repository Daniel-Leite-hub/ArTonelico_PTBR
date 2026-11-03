# -*- coding: utf-8 -*-
import glob
import json

for fpath in glob.glob('Ferramentas_Traducao/curadoria_editorial/blocos/*output.json'):
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for line in d.get('dialogues', []):
            jp = line.get('original_jp', '')
            if 'プラズマベル' in jp or 'Plasma Bell' in line.get('original_en', ''):
                print(f"ID {line['id']}: JP: {jp}")
                print(f"  PT: {line.get('curated_ptbr')}")
    except Exception as e:
        pass

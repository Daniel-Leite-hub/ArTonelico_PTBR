# -*- coding: utf-8 -*-
import glob
import json

for fpath in glob.glob('Ferramentas_Traducao/curadoria_editorial/blocos/*output.json'):
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for line in d.get('dialogues', []):
            spk = line.get('speaker', '')
            if 'falss' in spk.lower() or 'caill' in spk.lower() or 'kyle' in spk.lower():
                print(f"Found Falss speaker: {spk} with speaker_id: {line.get('speaker_id')} in {fpath}")
                break
    except Exception as e:
        pass

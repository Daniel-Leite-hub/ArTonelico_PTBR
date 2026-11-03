# -*- coding: utf-8 -*-
import glob
import json

speakers = {}
for fpath in glob.glob('Ferramentas_Traducao/curadoria_editorial/blocos/*output.json'):
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for line in d.get('dialogues', []):
            sid = line.get('speaker_id')
            spk = line.get('speaker')
            if sid == 20:
                speakers[spk] = speakers.get(spk, 0) + 1
    except Exception as e:
        pass
print("Speaker_id 20 occurrences:", speakers)

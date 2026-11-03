import glob
import json

for f in sorted(glob.glob('Ferramentas_Traducao/curadoria_editorial/blocos/*_output.json')):
    data = json.load(open(f, encoding='utf-8'))
    for d in data.get('dialogues', []):
        t = d.get('curated_ptbr', '')
        if 'Orika' in t or '織香' in d.get('original_jp', ''):
            print(f"{f} ID {d.get('id')}: {t}")

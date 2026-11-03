import glob, json

files = sorted(glob.glob('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_*_output.json'))
for f in files:
    try:
        data = json.load(open(f, encoding='utf-8'))
        for d in data.get('dialogues', []):
            if '酒場' in d.get('original_jp', ''):
                print(d['id'], d.get('original_jp'), '-->', d.get('curated_ptbr'))
    except: pass

import glob
import json

files = sorted(glob.glob('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_*_output.json'))
for f in files:
    try:
        data = json.load(open(f, encoding='utf-8'))
        dialogues = data.get('dialogues', [])
        for d in dialogues:
            jp = d.get('original_jp', '')
            if '聖女' in jp:
                print(f"{f} | ID {d.get('id')} | Speaker: {d.get('speaker')}")
                print(f"JP: {jp}")
                print(f"EN: {d.get('original_en')}")
                print(f"PT: {d.get('curated_ptbr')}")
                print("-" * 50)
    except Exception as e:
        pass

import json

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_078_output.json', encoding='utf-8'))
for d in data['dialogues'][:20]:
    print(f"[{d['id']}] {d['speaker']}: {repr(d['curated_ptbr'])}")

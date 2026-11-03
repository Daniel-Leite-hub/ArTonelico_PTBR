import json, glob

terms = ['クロニクルキー', 'Chronicle Key', 'クレセントクロニクル', 'Crescent Chronicle', '六角板', 'Hexagonal Plate', 'パージャ', 'Purger', 'アル兄ぃ']

for path in glob.glob('Ferramentas_Traducao/curadoria_editorial/blocos/*output.json'):
    try:
        data = json.load(open(path, encoding='utf-8'))
        for d in data.get('dialogues', []):
            jp = d.get('original_jp', '')
            en = d.get('original_en', '')
            for t in terms:
                if t in jp or t in en:
                    print(f"Found in {path} [{d.get('id')}]: JP={jp} | Curated={d.get('curated_ptbr')}")
                    break
    except Exception as e:
        pass

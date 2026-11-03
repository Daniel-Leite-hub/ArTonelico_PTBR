import json

with open('Ferramentas_Traducao/curadoria_editorial/glossario_mestre.json', 'r', encoding='utf-8') as f:
    gm = json.load(f)

terms = gm.get('terms', {})
queries = ['Horus', 'Hymn', 'Brooch', 'Purger', 'Ambience', 'Doryoku', 'Apostle', 'Altar', 'Platina', 'Virus', 'ston', 'Wings', 'CR']
for q in queries:
    matches = {k: v for k, v in terms.items() if q.lower() in k.lower() or any(q.lower() in str(val).lower() for val in v.values())}
    print(f'Query [{q}]: {len(matches)} matches')
    for k, v in list(matches.items())[:5]:
        print(f"  {k} -> {v.get('pt')} | {v.get('note', '')[:70]}")

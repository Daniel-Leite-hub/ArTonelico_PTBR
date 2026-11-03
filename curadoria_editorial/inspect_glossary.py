import json

glossary = json.load(open('Ferramentas_Traducao/curadoria_editorial/glossario_mestre.json', encoding='utf-8'))
terms_dict = glossary.get('terms', {})
chars_dict = glossary.get('characters', {})

terms = ['Crescent', 'Chronicle', 'Purger', 'Hexagonal', 'Wharf', 'Lune', 'Lünn', 'Hyogo', 'Gelo', 'Mir', 'Tastiella', 'Ayano', 'Radolf', 'Dokkoi', 'Harm', 'Yuteroid', 'Tokoyo', 'Bourd']

print("--- TERMS ---")
for k, v in terms_dict.items():
    for q in terms:
        if q.lower() in k.lower() or (isinstance(v, dict) and any(q.lower() in str(x).lower() for x in v.values())):
            print(f"Term: {k} => {v.get('pt') if isinstance(v, dict) else v}")
            break

print("\n--- CHARACTERS ---")
for k, v in chars_dict.items():
    for q in terms:
        if q.lower() in k.lower() or (isinstance(v, dict) and any(q.lower() in str(x).lower() for x in v.values())):
            print(f"Char: {k} => {v.get('pt') if isinstance(v, dict) else v}")
            break

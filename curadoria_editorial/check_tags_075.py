import json, re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_075_input.json', encoding='utf-8') as f:
    data = json.load(f)

found_tags = []
for d in data['dialogues']:
    for fld in ['original_jp', 'original_en', 'current_ptbr']:
        txt = d.get(fld, '')
        matches = re.findall(r'\[[0-9A-Za-z_:#@-]+\]|%[sd]|@[0-9]+#[0-9]+|#[0-9].*?##|<.*?>|\{.*?\}', txt)
        if matches:
            found_tags.append((d['id'], fld, matches, txt))

print(f"Total entries with tags: {len(found_tags)}")
for item in found_tags:
    print(item)

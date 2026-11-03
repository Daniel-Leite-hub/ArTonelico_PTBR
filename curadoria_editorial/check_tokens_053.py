import json, re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_053_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

found_any = False
for d in data['dialogues']:
    for f in ['original_jp', 'original_en', 'current_ptbr']:
        txt = d.get(f, '')
        tags = re.findall(r'(%[sd]|\bIM\d+\b|\[\d+\]|\[[0-9A-Fa-f]{4}\]|＠\d+|#[0-9A-Za-z#]+)', txt)
        if tags:
            print(f"ID {d['id']} [{f}]: {tags}")
            found_any = True

if not found_any:
    print("No procedural tokens (%s, %d, IM##, [00XX], @######, #...) found in BLK_EVD_053!")

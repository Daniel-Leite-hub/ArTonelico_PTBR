import json, re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_089_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data.get('dialogues', []):
    jp = d.get('original_jp', '')
    en = d.get('original_en', '')
    tags = re.findall(r'%[0-9]*[a-zA-Z]|IM\d+|\[00[0-9A-Fa-f]{2}\]|＠[0-9A-Fa-f]{6}|#0.*', jp)
    if tags:
        print(f"ID {d['id']}: {tags} in JP: {jp}")
    tags_en = re.findall(r'%[0-9]*[a-zA-Z]|IM\d+|\[00[0-9A-Fa-f]{2}\]|＠[0-9A-Fa-f]{6}|#0.*', en)
    if tags_en:
        print(f"ID {d['id']}: {tags_en} in EN: {en}")

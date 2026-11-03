import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_067_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for item in d['dialogues']:
    # Check if there are any formatting codes like %s, %d, [00XX], @######, IM##
    import re
    tags = re.findall(r'%[0-9]*[a-zA-Z]|\[[0-9A-Fa-f]{4}\]|＠[0-9A-Fa-f]{6}|IM\d+', item['original_jp'] + item['original_en'])
    if tags:
        print(f"Tag found in ID {item['id']}: {tags}")
print("Tag search complete.")

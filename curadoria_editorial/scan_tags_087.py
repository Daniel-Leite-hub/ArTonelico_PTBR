import json
import re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_087_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total lines: {len(d['dialogues'])}")

tags_found = []
for item in d['dialogues']:
    jp = item['original_jp']
    en = item['original_en']
    pt = item['current_ptbr']
    # find tags
    for text in (jp, en, pt):
        for pattern in [r'\[[0-9A-Za-z_:#@-]+\]', r'＠[0-9]{6}#[0-9]{2}', r'\{[0-9A-Za-z_:]+\}', r'%[sd]', r'IM\d+', r'#\d+.*?##']:
            m = re.findall(pattern, text)
            if m:
                tags_found.append((item['id'], pattern, m, text))

print(f"Tags found count: {len(tags_found)}")
for t in tags_found:
    print(t[0], t[1], t[2])

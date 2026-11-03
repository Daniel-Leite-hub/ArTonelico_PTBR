import json
import re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_058_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

lines = d['dialogues']
print(f"Total lines: {len(lines)}")

control_patterns = [
    re.compile(r'%[0-9]*[sd%]'),
    re.compile(r'\[00[0-9A-Fa-f]{2}\]'),
    re.compile(r'IM[0-9]{2}'),
    re.compile(r'＠[0-9A-Fa-f]+'),
    re.compile(r'#[0-9].*?##'),
    re.compile(r'\{[0-9]+\}'),
]

for item in lines:
    jp = item['original_jp']
    en = item['original_en']
    pt = item['current_ptbr']
    
    # Check special patterns
    for pat in control_patterns:
        m_jp = pat.findall(jp)
        m_en = pat.findall(en)
        m_pt = pat.findall(pt)
        if m_jp or m_en or m_pt:
            print(f"ID {item['id']} has tag {pat.pattern}: JP={m_jp}, EN={m_en}, PT={m_pt}")

print("Check finished.")

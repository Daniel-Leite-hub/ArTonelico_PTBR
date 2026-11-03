import json
import re

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_045_input.json', encoding='utf-8') as f:
    data = json.load(f)

dialogues = data['dialogues']

print(f"Total lines: {len(dialogues)}")

# Check variables, tags, stage directions in current_ptbr and original_en
for d in dialogues:
    d_id = d['id']
    en = d.get('original_en', '')
    jp = d.get('original_jp', '')
    pt = d.get('current_ptbr', '')

    # check asterisks
    if '*' in pt or '*' in en:
        print(f"[AST] ID {d_id}: EN='{en}' | PT='{pt}'")
    # check tags
    for tag_pat in [r"\[[0-9A-Fa-f]{4}\]", r"＠[0-9A-Fa-f]{6}#[0-9A-Fa-f]{2}", r"IM[0-9]{2}", r"(%[sSdD]|%[0-9]+[sSdD]|{[0-9]+}|{[a-zA-Z0-9_]+})"]:
        m_en = re.findall(tag_pat, en)
        m_jp = re.findall(tag_pat, jp)
        m_pt = re.findall(tag_pat, pt)
        if m_en or m_jp or m_pt:
            print(f"[TAG {tag_pat}] ID {d_id}: JP={m_jp} EN={m_en} PT={m_pt}")

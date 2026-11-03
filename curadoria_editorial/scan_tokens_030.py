import json
import re

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_030_input.json', encoding='utf-8'))
dialogues = data['dialogues']

print(f"Total dialogues: {len(dialogues)}")

RE_TAG_BRACKETS = re.compile(r"\[[0-9A-Fa-f]{4}\]")
RE_TAG_AT = re.compile(r"＠[0-9A-Fa-f]{6}#[0-9A-Fa-f]{2}")
RE_VARIABLES = re.compile(r"(%[sSdD]|%[0-9]+[sSdD]|{[0-9]+}|{[a-zA-Z0-9_]+})")
RE_IMAGE_TAGS = re.compile(r"IM[0-9]{2}")

for d in dialogues:
    d_id = d['id']
    en = d.get('original_en', '')
    jp = d.get('original_jp', '')
    pt = d.get('current_ptbr', '')
    
    vars_found = RE_VARIABLES.findall(en) + RE_VARIABLES.findall(jp)
    brackets = RE_TAG_BRACKETS.findall(en) + RE_TAG_BRACKETS.findall(jp)
    ats = RE_TAG_AT.findall(en) + RE_TAG_AT.findall(jp)
    imgs = RE_IMAGE_TAGS.findall(en) + RE_IMAGE_TAGS.findall(jp)
    
    if vars_found or brackets or ats or imgs:
        print(f"Special tokens in [{d_id}]: vars={vars_found}, brackets={brackets}, ats={ats}, imgs={imgs}")

print("Token scan complete.")

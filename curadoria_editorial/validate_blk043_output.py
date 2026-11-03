# -*- coding: utf-8 -*-
import json
import re
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_043_output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

block_id = data.get('block_id')
dialogues = data.get('dialogues', [])

print(f"Block ID: {block_id}")
print(f"Total dialogues: {len(dialogues)}")

assert block_id == "BLK_EVD_043"
assert len(dialogues) == 231

ids = [d['id'] for d in dialogues]
assert ids == list(range(10128, 10359))

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_043_input.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)
input_map = {d['id']: d for d in input_data['dialogues']}

errors = []
for d in dialogues:
    i = d['id']
    pt = d['pt_curated']
    notes = d['curation_notes']
    inp = input_map[i]
    jp = inp.get('original_jp', '')
    
    if not pt or not pt.strip():
        errors.append(f"Empty pt_curated at ID {i}")
    if not notes or not notes.strip():
        errors.append(f"Empty curation_notes at ID {i}")
        
    # Check newline orphan punctuation
    lines = pt.split('\n')
    for idx, l in enumerate(lines):
        if idx > 0 and l:
            if l[0] in '.,!?:;)]}':
                errors.append(f"ID {i}: Line starts with '{l[0]}': {repr(l)}")
            if l.startswith('...'):
                errors.append(f"ID {i}: Line starts with '...': {repr(l)}")

    # Check rubrics
    if re.search(r'\*[^*]+\*', pt):
        errors.append(f"ID {i}: Scenic rubric found: {repr(pt)}")
        
    # Check quotes and brackets
    if pt.count('"') % 2 != 0:
        errors.append(f"ID {i}: Double quotes unbalanced: {repr(pt)}")
    if pt.count('«') != pt.count('»'):
        errors.append(f"ID {i}: Guillemets unbalanced: {repr(pt)}")
    if pt.count('[') != pt.count(']'):
        errors.append(f"ID {i}: Brackets unbalanced: {repr(pt)}")
    if pt.count('(') != pt.count(')'):
        errors.append(f"ID {i}: Parentheses unbalanced: {repr(pt)}")

    # Check hard gate against JP
    valido, erros_hg = validador_editorial.validar_hard_gate(
        original=jp,
        traduzido=pt,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        for e in erros_hg:
            errors.append(f"ID {i} Hard Gate: {e}")

if errors:
    print(f"Validation found {len(errors)} errors:")
    for e in errors:
        print("  *", e)
    sys.exit(1)
else:
    print("ALL 231 DIALOGUES VALIDATED PERFECTLY! 100% COMPLIANT.")

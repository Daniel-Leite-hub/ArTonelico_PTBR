# -*- coding: utf-8 -*-
import json
import os
import re
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

from batch1_043 import dialogues as b1
from batch2_043 import dialogues as b2
from batch3_043 import dialogues as b3
from batch4_043 import dialogues as b4
from batch5_043 import dialogues as b5
from batch6_043 import dialogues as b6
from batch7_043 import dialogues as b7

all_dialogues = b1 + b2 + b3 + b4 + b5 + b6 + b7
print(f"Total dialogues assembled: {len(all_dialogues)}")

assert len(all_dialogues) == 231, f"Expected 231, got {len(all_dialogues)}"
expected_ids = list(range(10128, 10359))
actual_ids = [d['id'] for d in all_dialogues]
assert actual_ids == expected_ids, "IDs do not match expected range 10128..10358"

# Load input for hard gate comparison
with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_043_input.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

input_map = {d['id']: d for d in input_data['dialogues']}

hard_gate_errors = []
lint_warnings = []
formatting_errors = []

for d in all_dialogues:
    lid = d['id']
    pt = d['pt_curated']
    notes = d['curation_notes']
    inp = input_map[lid]
    jp = inp.get('original_jp', '')
    en = inp.get('original_en', '')

    # Check non-empty
    if not pt or not pt.strip():
        formatting_errors.append(f"ID {lid}: empty pt_curated")
    if not notes or not notes.strip():
        formatting_errors.append(f"ID {lid}: empty curation_notes")

    # Hard gate against Japanese
    valido, erros = validador_editorial.validar_hard_gate(
        original=jp,
        traduzido=pt,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        for e in erros:
            hard_gate_errors.append(f"ID {lid}: {e}")

    # Lint check
    avisos = validador_editorial.auditar_estilo_editorial(pt)
    if avisos:
        for a in avisos:
            lint_warnings.append(f"ID {lid}: {a}")

    # Check orphan punctuation
    lines = pt.split('\n')
    for idx, l in enumerate(lines):
        if idx > 0 and l:
            if l[0] in '.,!?:;)]}':
                formatting_errors.append(f"ID {lid}: Line starts with '{l[0]}': {repr(l)}")
            if l.startswith('...'):
                formatting_errors.append(f"ID {lid}: Line starts with '...': {repr(l)}")

    # Check rubrics
    if re.search(r'\*[^*]+\*', pt):
        formatting_errors.append(f"ID {lid}: Scenic rubric found: {repr(pt)}")

    # Check quote and bracket balances
    if pt.count('"') % 2 != 0:
        formatting_errors.append(f"ID {lid}: Double quotes unbalanced: {repr(pt)}")
    if pt.count('«') != pt.count('»'):
        formatting_errors.append(f"ID {lid}: Guillemets unbalanced: {repr(pt)}")
    if pt.count('[') != pt.count(']'):
        formatting_errors.append(f"ID {lid}: Brackets unbalanced: {repr(pt)}")
    if pt.count('(') != pt.count(')'):
        formatting_errors.append(f"ID {lid}: Parentheses unbalanced: {repr(pt)}")

    # Hymmnos verse check
    if jp.startswith('#0'):
        if not pt.startswith('#0'):
            formatting_errors.append(f"ID {lid}: Hymmnos prefix #0 missing in {repr(pt)}")
        if pt.strip() != jp.strip():
            formatting_errors.append(f"ID {lid}: Hymmnos mismatch: {repr(pt)} vs {repr(jp)}")

print(f"Hard gate errors: {len(hard_gate_errors)}")
for e in hard_gate_errors:
    print("  [HG ERROR]", e)

print(f"Lint warnings: {len(lint_warnings)}")
for w in lint_warnings:
    print("  [LINT WARN]", w)

print(f"Formatting errors: {len(formatting_errors)}")
for f in formatting_errors:
    print("  [FMT ERROR]", f)

assert len(hard_gate_errors) == 0, "Hard gate errors must be 0"
assert len(formatting_errors) == 0, "Formatting errors must be 0"

# Assemble output dict
output_dict = {
    "block_id": "BLK_EVD_043",
    "dialogues": all_dialogues
}

output_path = 'Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_043_output.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output_dict, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully wrote {len(all_dialogues)} curated dialogues to {output_path}!")

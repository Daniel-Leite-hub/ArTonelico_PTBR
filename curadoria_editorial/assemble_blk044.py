# -*- coding: utf-8 -*-
import json
import os
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
sys.path.insert(0, r"Ferramentas_Traducao\tools")
sys.path.insert(0, r"Ferramentas_Traducao\curadoria_editorial")

import validador_editorial
from curadoria_validate import validate_line, validate_batch

from batch1_044 import dialogues as b1
from batch2_044 import dialogues as b2
from batch3_044 import dialogues as b3
from batch4_044 import dialogues as b4
from batch5_044 import dialogues as b5
from batch6_044 import dialogues as b6
from batch7_044 import dialogues as b7

all_dialogues = b1 + b2 + b3 + b4 + b5 + b6 + b7
print(f"Total dialogues assembled: {len(all_dialogues)}")

assert len(all_dialogues) == 209, f"Expected 209, got {len(all_dialogues)}"
expected_ids = list(range(10359, 10568))
actual_ids = [d['id'] for d in all_dialogues]
assert actual_ids == expected_ids, f"IDs mismatch! First: {actual_ids[0]}, Last: {actual_ids[-1]}"

# Load input for hard gate comparison
with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_044_input.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

input_map = {d['id']: d for d in input_data['dialogues']}

hard_gate_errors = []
lint_warnings = []
formatting_errors = []

for d in all_dialogues:
    lid = d['id']
    pt = d['pt_curated']
    notes = d['notes']
    inp = input_map[lid]
    jp = inp.get('original_jp', '')
    en = inp.get('original_en', '')

    if not pt or not pt.strip():
        formatting_errors.append(f"ID {lid}: empty text")
    if not notes or not notes.strip():
        formatting_errors.append(f"ID {lid}: empty notes")

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

    # curadoria_validate
    c_errs = validate_line(lid, en, pt)
    if c_errs:
        for ce in c_errs:
            hard_gate_errors.append(f"ID {lid} (curadoria_validate): {ce}")

    # Lint check
    avisos = validador_editorial.auditar_estilo_editorial(pt)
    if avisos:
        for a in avisos:
            lint_warnings.append(f"ID {lid}: {a}")

    # Delimiter balancing
    if pt.count('«') != pt.count('»'):
        formatting_errors.append(f"ID {lid}: Guillemets unbalanced: {repr(pt)}")
    if pt.count('[') != pt.count(']'):
        formatting_errors.append(f"ID {lid}: Brackets unbalanced: {repr(pt)}")
    if pt.count('(') != pt.count(')'):
        formatting_errors.append(f"ID {lid}: Parentheses unbalanced: {repr(pt)}")

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
    "block_id": "BLK_EVD_044",
    "dialogues": all_dialogues
}

output_path = 'Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_044_output.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output_dict, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully wrote {len(all_dialogues)} curated dialogues to {output_path}!")

# Test validate_batch on final output file
with open(output_path, 'r', encoding='utf-8') as f:
    final_data = json.load(f)

is_batch_valid, batch_errors = validate_batch(final_data)
print(f"Batch validation: is_valid={is_batch_valid}, errors={len(batch_errors)}")
assert is_batch_valid, f"Batch validation failed with {batch_errors}"
print("ALL VERIFICATIONS COMPLETED WITH 100% SUCCESS!")

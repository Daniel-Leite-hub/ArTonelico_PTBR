# -*- coding: utf-8 -*-
"""
test_curated_056.py - Teste de validação técnica e editorial determinística de curate_blk056.py
"""
import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

sys.path.insert(0, r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial")
from curate_blk056 import CURATED

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_056_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

lines = input_data["dialogues"]
print(f"Total lines in input: {len(lines)}")
assert len(lines) == 198, f"Expected 198 lines, got {len(lines)}"

hard_gate_errors = 0
lint_warnings = 0

for item in lines:
    item_id = item["id"]
    if item_id not in CURATED:
        print(f"[MISSING ID] ID {item_id} not in CURATED!")
        hard_gate_errors += 1
        continue

    orig_jp = item["original_jp"]
    trad, note = CURATED[item_id]

    # Hard gate
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=trad,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {item_id}: {e}")

    # Lint editorial
    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

    # Check for \r
    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    # Check orphan line start with punctuation
    for line_part in trad.split("\n"):
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")) and not line_part.startswith("..."):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation: {line_part!r}")
            hard_gate_errors += 1

print("\n--- Summary ---")
print(f"Total evaluated: {len(lines)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("\n>>> ALL 198 LINES PASSED PERFECTLY WITH ZERO ERRORS AND ZERO WARNINGS! <<<")
else:
    print("\n>>> ISSUES DETECTED. FIX THEM. <<<")
    sys.exit(1)

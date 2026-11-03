# -*- coding: utf-8 -*-
"""
test_pre_assembly_087.py - Verificação preliminar das 291 falas curadas de BLK_EVD_087
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

from data_blk087_part1 import LINES_PART1
from data_blk087_part2 import LINES_PART2

all_lines = {}
all_lines.update(LINES_PART1)
all_lines.update(LINES_PART2)

print(f"Total curated entries: {len(all_lines)}")
assert len(all_lines) == 291, f"Expected 291, got {len(all_lines)}"

# Check sequential range
expected_ids = list(range(19517, 19808))
for i in expected_ids:
    assert i in all_lines, f"Missing ID {i}"

input_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_087_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

hard_gate_errors = 0
lint_warnings = 0

for item in input_data["dialogues"]:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    trad, note = all_lines[item_id]

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

    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

    # Check for \r
    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    # Check orphan line start with punctuation after \n
    parts = trad.split("\n")
    for line_part in parts[1:]:
        line_strip = line_part.strip()
        if line_strip.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1
        if line_part.startswith("..."):
            print(f"[ERROR] ID {item_id}: Line starts with reticências after newline: {line_part!r}")
            hard_gate_errors += 1

    # Check syntactic fracture before \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r} in text:\n{trad}")
        hard_gate_errors += 1

print("\n--- RESUMO DE TESTE PRÉ-MONTAGEM ---")
print(f"Total lines tested: {len(all_lines)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("\n[PERFEIÇÃO] Todas as 291 falas passaram com ZERO erros e ZERO avisos!")
else:
    print(f"\n[ATENÇÃO] Encontrados {hard_gate_errors} erros e {lint_warnings} avisos.")
    sys.exit(1)

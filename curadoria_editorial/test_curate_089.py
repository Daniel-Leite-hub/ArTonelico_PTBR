# -*- coding: utf-8 -*-
"""
test_curate_089.py - Validação prévia de curate_blk089.py
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

from curate_blk089 import curated_data

# Load input
input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_089_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

lines = input_data["dialogues"]
print(f"Total input lines: {len(lines)}")
assert len(lines) == 217, f"Expected 217 lines, got {len(lines)}"
assert len(curated_data) == 217, f"Expected 217 curated entries, got {len(curated_data)}"

hard_gate_errors = 0
lint_warnings = 0

for item in lines:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    if item_id not in curated_data:
        print(f"[MISSING ID] ID {item_id} not in curated_data!")
        hard_gate_errors += 1
        continue

    trad, note = curated_data[item_id]

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
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

print(f"\nPre-Validation Summary:")
print(f"Total lines: {len(lines)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

# -*- coding: utf-8 -*-
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

from curated_data_blk078 import CURATED_LINES

input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_078_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

dialogues = input_data["dialogues"]
print(f"Total dialogues in input: {len(dialogues)}")
print(f"Total entries in CURATED_LINES: {len(CURATED_LINES)}")

assert len(CURATED_LINES) == 234, f"Expected 234, got {len(CURATED_LINES)}"

hard_gate_errors = 0
lint_warnings = 0

for d in dialogues:
    line_id = d["id"]
    if line_id not in CURATED_LINES:
        print(f"[MISSING ID] {line_id}")
        hard_gate_errors += 1
        continue

    item = CURATED_LINES[line_id]
    trad = item["text"]
    orig_jp = d["original_jp"]

    # Hard gate
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=trad,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        for e in erros:
            print(f"[HARD GATE ERROR] ID {line_id}: {e}")
            hard_gate_errors += 1

    # Lint
    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        for a in avisos:
            print(f"[LINT WARNING] ID {line_id}: {a}")
            lint_warnings += 1

    # Carriage return
    if "\r" in trad:
        print(f"[ERROR] ID {line_id}: Carriage return found")
        hard_gate_errors += 1

    # Orphan punctuation after \n
    parts = trad.split("\n")
    for p in parts[1:]:
        p_strip = p.strip()
        if p_strip.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {line_id}: Orphan punctuation after \\n: {p!r}")
            hard_gate_errors += 1
        if p.startswith("..."):
            print(f"[ERROR] ID {line_id}: Reticências after \\n: {p!r}")
            hard_gate_errors += 1

    # Syntactic fracture before \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {line_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

print("\n--- RESUMO DA VALIDAÇÃO PRELIMINAR ---")
print(f"Hard gate errors: {hard_gate_errors}")
print(f"Lint warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("[SUCESSO TOTAL] Todas as 234 falas passaram 100% limpas!")
else:
    print("[ATENÇÃO] Há problemas a serem corrigidos.")

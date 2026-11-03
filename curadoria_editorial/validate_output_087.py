# -*- coding: utf-8 -*-
"""
validate_output_087.py - Validação rigorosa determinística de BLK_EVD_087_output.json
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_087_output.json")
with open(output_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Verifica campos de topo
assert data["block_id"] == "BLK_EVD_087", f"Expected BLK_EVD_087, got {data.get('block_id')}"
assert "stats" in data, "Missing stats"
assert "curated_lines" in data, "Missing curated_lines"
assert "dialogues" in data, "Missing dialogues"
assert "scene_handoff" in data, "Missing scene_handoff"
assert "glossary_additions" in data, "Missing glossary_additions"

lines = data["dialogues"]
curated_lines = data["curated_lines"]
print(f"Loaded {len(lines)} lines from output JSON.")
assert len(lines) == 291, f"Expected 291 lines, got {len(lines)}"
assert len(curated_lines) == 291, f"Expected 291 curated_lines, got {len(curated_lines)}"

required_fields = [
    "id", "event_file", "speaker_id", "speaker", "original_jp", "original_en",
    "curated_ptbr", "review_status", "reviewed"
]

missing_field_errors = 0
for d in lines:
    for field in required_fields:
        if field not in d:
            print(f"[SCHEMA ERROR] ID {d.get('id')}: Missing field '{field}'")
            missing_field_errors += 1

hard_gate_errors = 0
lint_warnings = 0

for item in lines:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    trad = item["curated_ptbr"]

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

print(f"\nValidation Summary for BLK_EVD_087:")
print(f"Total lines evaluated: {len(lines)}")
print(f"Missing Field Errors: {missing_field_errors}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if missing_field_errors == 0 and hard_gate_errors == 0 and lint_warnings == 0:
    print("\n[PERFECTION] All 291 lines passed all technical and editorial checks with ZERO errors and ZERO warnings!")
else:
    print(f"\n[FAILURE] Validation detected {missing_field_errors} schema errors, {hard_gate_errors} hard gate errors, {lint_warnings} lint warnings.")
    sys.exit(1)

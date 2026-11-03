# -*- coding: utf-8 -*-
"""
assemble_and_validate_058.py - Montagem e validação de BLK_EVD_058
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

from scene1_data import scene1
from scene2_data import scene2
from scene3_data import scene3
from scene4_data import scene4

# Merge all scenes
all_scenes = {}
all_scenes.update(scene1)
all_scenes.update(scene2)
all_scenes.update(scene3)
all_scenes.update(scene4)

print(f"Total curated lines mapped: {len(all_scenes)}")
assert len(all_scenes) == 204, f"Expected 204 lines, got {len(all_scenes)}"

# Load input
input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_058_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_lines = input_data["dialogues"]
assert len(input_lines) == 204

output_dialogues = []
missing_field_errors = 0
hard_gate_errors = 0
lint_warnings = 0

for item in input_lines:
    item_id = item["id"]
    if item_id not in all_scenes:
        print(f"[ERROR] Missing curated text for ID {item_id}")
        missing_field_errors += 1
        continue
    
    curated_text, curation_note = all_scenes[item_id]
    orig_jp = item["original_jp"]

    # Run hard gate validation
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=curated_text,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {item_id}: {e}")

    # Run linting
    avisos = validador_editorial.auditar_estilo_editorial(curated_text)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

    # Check for \r
    if "\r" in curated_text:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    # Check orphan line start with punctuation after \n
    parts = curated_text.split("\n")
    for line_part in parts[1:]:
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1

    # Check syntactic fracture before \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(curated_text)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

    # Build dialogue entry matching BLK_EVD_057 schema
    entry = {
        "id": item_id,
        "event_file": item["event_file"],
        "speaker_id": item.get("speaker_id"),
        "speaker": item.get("speaker"),
        "original_jp": orig_jp,
        "original_en": item["original_en"],
        "curated_ptbr": curated_text,
        "final_ptbr": curated_text,
        "texto_ptbr_curado": curated_text,
        "custom_text": curated_text,
        "review_status": "approved",
        "reviewed": True,
        "notes": curation_note,
        "curation_notes": curation_note
    }
    output_dialogues.append(entry)

print("\n--- Validation Summary ---")
print(f"Total lines evaluated: {len(output_dialogues)}")
print(f"Missing Field Errors: {missing_field_errors}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if missing_field_errors == 0 and hard_gate_errors == 0 and lint_warnings == 0:
    print("\n[PERFECTION] All 204 lines passed all validation gates cleanly!")
else:
    print("\n[FAILED] Issues detected, fixing required.")
    sys.exit(1)

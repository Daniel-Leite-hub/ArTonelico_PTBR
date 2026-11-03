# -*- coding: utf-8 -*-
"""
validate_output_056.py - Validação rigorosa determinística de BLK_EVD_056_output.json
"""
import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_056_output.json"
with open(output_path, "r", encoding="utf-8") as f:
    data = json.load(f)

lines = data["dialogues"]
print(f"Loaded {len(lines)} lines from output JSON.")
assert len(lines) == 198, f"Expected 198 lines, got {len(lines)}"

required_fields = [
    "id", "event_file", "speaker", "original_jp", "original_en",
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

    # Check orphan line start with punctuation
    for line_part in trad.split("\n"):
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")) and not line_part.startswith("..."):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation: {line_part!r}")
            hard_gate_errors += 1

print(f"\nValidation Summary for BLK_EVD_056:")
print(f"Total lines evaluated: {len(lines)}")
print(f"Missing Field Errors: {missing_field_errors}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if missing_field_errors == 0 and hard_gate_errors == 0 and lint_warnings == 0:
    print("\n[PERFECTION] All 198 lines passed all technical and editorial checks with ZERO errors and ZERO warnings!")
else:
    print("\n[FAILURE] Validation detected issues that must be resolved.")
    sys.exit(1)

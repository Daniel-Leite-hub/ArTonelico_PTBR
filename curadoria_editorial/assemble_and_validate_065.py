# -*- coding: utf-8 -*-
"""
assemble_and_validate_065.py - Gera e valida BLK_EVD_065_output.json
"""
import sys
import json
import os
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial
import build_and_validate_065 as b

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_065_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_065_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

curated_dict = b.curated_dict

curated_lines = []
dialogues_out = []

for item in input_data["dialogues"]:
    item_id = item["id"]
    cur_info = curated_dict[item_id]
    pt_text = cur_info["pt"]
    rat = cur_info["rationale"]

    curated_lines.append({
        "id": item_id,
        "ptbr_curated": pt_text,
        "rationale": rat
    })

    d_entry = dict(item)
    d_entry["review_status"] = "approved"
    d_entry["curated_ptbr"] = pt_text
    d_entry["final_ptbr"] = pt_text
    d_entry["texto_ptbr_curado"] = pt_text
    d_entry["custom_text"] = pt_text
    d_entry["ptbr_curated"] = pt_text
    d_entry["reviewed"] = True
    d_entry["notes"] = rat
    d_entry["curation_notes"] = rat

    dialogues_out.append(d_entry)

glossary_additions = {
    "Ambience Field": {
        "pt": "Campo de Ambiência",
        "gender": "masculino",
        "number": "singular",
        "category": "Combate / Magia da Canção",
        "note": "Campo sônico de ressonância projetado pela Reyvateil sobre os inimigos antes do desencadeamento da Magia da Canção (JP アンビエンスフィールド)."
    },
    "Symphonic Power Line": {
        "pt": "Linha de Condução de Doryoku",
        "gender": "feminino",
        "number": "singular",
        "category": "Tecnologia / Infraestrutura da Torre",
        "note": "Malha condutora de energia sônica e mágica (doryoku) que percorre a superestrutura da Torre e sustenta o funcionamento de Platina (JP 導力ライン)."
    },
    "Sealed Airship": {
        "pt": "Aeronave Selada",
        "gender": "feminino",
        "number": "singular",
        "category": "Veículo / Lore",
        "note": "Veículo voador sagrado e proibido, guardado em Platina atrás de anteparas seladas, concedido por Shurelia a Lyner em estado de emergência para atravessar a Blastline rumo ao Mundo Inferior (JP 封印されし飛空挺)."
    }
}

output_data = {
    "block_id": "BLK_EVD_065",
    "axis_id": input_data.get("axis_id", "AXIS_3"),
    "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
    "category": input_data.get("category", "Event Dialogue"),
    "line_count": len(dialogues_out),
    "id_range": [dialogues_out[0]["id"], dialogues_out[-1]["id"]],
    "curated_lines": curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": dialogues_out
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"Saved {len(dialogues_out)} lines to {output_path}")

# Rigorous validation suite
with open(output_path, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

assert loaded_data["block_id"] == "BLK_EVD_065"
assert "curated_lines" in loaded_data
assert "glossary_additions" in loaded_data
assert "dialogues" in loaded_data

lines = loaded_data["dialogues"]
c_lines = loaded_data["curated_lines"]
assert len(lines) == 182, f"Expected 182 lines, got {len(lines)}"
assert len(c_lines) == 182, f"Expected 182 curated_lines, got {len(c_lines)}"

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

    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    parts = trad.split("\n")
    for line_part in parts[1:]:
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1

    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

print(f"\nFinal Validation Summary for BLK_EVD_065:")
print(f"Total lines evaluated: {len(lines)}")
print(f"Missing Field Errors: {missing_field_errors}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if missing_field_errors == 0 and hard_gate_errors == 0 and lint_warnings == 0:
    print("\n[PERFECTION] All 182 lines passed all technical and editorial checks with ZERO errors and ZERO warnings!")
else:
    print("\n[FAILURE] Validation detected issues that must be resolved.")
    sys.exit(1)

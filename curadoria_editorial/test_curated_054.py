# -*- coding: utf-8 -*-
import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

from curated_lines_054_p1 import CURATED_LINES as P1
from curated_lines_054_p2 import CURATED_LINES as P2
from curated_lines_054_p3 import CURATED_LINES as P3

ALL_LINES = {}
ALL_LINES.update(P1)
ALL_LINES.update(P2)
ALL_LINES.update(P3)

print(f"Total curated entries: {len(ALL_LINES)}")
assert len(ALL_LINES) == 268, f"Expected 268 lines, got {len(ALL_LINES)}"

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_054_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_dict = {d["id"]: d for d in input_data["dialogues"]}
assert len(input_dict) == 268

hard_gate_errors = 0
lint_warnings = 0

for item_id, item_in in sorted(input_dict.items()):
    assert item_id in ALL_LINES, f"Missing ID {item_id}"
    curated = ALL_LINES[item_id]
    orig_jp = item_in["original_jp"]
    trad = curated["ptbr"]

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

print(f"\n--- Preliminary Validation Results ---")
print(f"Total evaluated: {len(ALL_LINES)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

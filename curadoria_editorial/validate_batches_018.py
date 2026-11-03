# -*- coding: utf-8 -*-
import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_018_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

batches = [
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_018.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_018.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch3_018.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_018.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_018.json"
]

all_items = []
for b_file in batches:
    with open(b_file, "r", encoding="utf-8") as f:
        items = json.load(f)
        all_items.extend(items)

print(f"Total items in all batches: {len(all_items)}")
assert len(all_items) == 208, f"Expected 208 items, got {len(all_items)}"

hard_gate_errors = 0
lint_warnings = 0

for item in all_items:
    item_id = item["id"]
    inp = input_map[item_id]
    orig_jp = inp["original_jp"]
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

print(f"\nPre-Assembly Validation Summary for BLK_EVD_018:")
print(f"Total items checked: {len(all_items)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("\nALL BATCHES PERFECT! ZERO HARD GATE ERRORS, ZERO LINT WARNINGS!")
else:
    print("\nISSUES FOUND!")
    sys.exit(1)

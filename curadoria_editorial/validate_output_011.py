import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_output.json"
with open(output_path, "r", encoding="utf-8") as f:
    data = json.load(f)

lines = data["curated_lines"]
print(f"Loaded {len(lines)} lines from output JSON.")

hard_gate_errors = 0
lint_warnings = 0

for item in lines:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    orig_en = item["original_en"]
    trad = item["texto_ptbr_curado"]
    
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

print(f"\nValidation Summary for BLK_EVD_011:")
print(f"Total lines evaluated: {len(lines)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("\nPERFECT SCORE: ZERO Hard Gate Errors, ZERO Lint Warnings!")

import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_015_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)
input_map = {d["id"]: d for d in input_data["dialogues"]}

batch_num = sys.argv[1] if len(sys.argv) > 1 else "2"
batch_path = rf"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch{batch_num}_015.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch = json.load(f)

hard_gate_errors = 0
lint_warnings = 0

for item in batch:
    item_id = item["id"]
    orig_jp = input_map[item_id]["original_jp"]
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

print(f"Summary for Batch {batch_num}:")
print(f"Items: {len(batch)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

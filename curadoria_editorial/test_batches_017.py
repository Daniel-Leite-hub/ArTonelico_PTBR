import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_017_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)
inp_map = {d["id"]: d for d in input_data["dialogues"]}

batch_files = sys.argv[1:]
if not batch_files:
    print("No batch files provided.")
    sys.exit(1)

total_items = 0
total_errors = 0
total_warnings = 0

for bf in batch_files:
    with open(bf, "r", encoding="utf-8") as f:
        items = json.load(f)
    print(f"\n--- Checking {bf} ({len(items)} items) ---")
    b_errors = 0
    b_warnings = 0
    for item in items:
        item_id = item["id"]
        orig = inp_map[item_id]["original_jp"]
        trad = item["curated_ptbr"]
        val, errs = validador_editorial.validar_hard_gate(
            original=orig,
            traduzido=trad,
            ignorar_quebras=True,
            permitir_colisao_variavel=True
        )
        if not val:
            b_errors += len(errs)
            for e in errs:
                print(f"[HARD GATE ERROR] ID {item_id}: {e}")
        avs = validador_editorial.auditar_estilo_editorial(trad)
        if avs:
            b_warnings += len(avs)
            for a in avs:
                print(f"[LINT WARNING] ID {item_id}: {a}")
    print(f"Summary for {bf}: {b_errors} errors, {b_warnings} warnings.")
    total_items += len(items)
    total_errors += b_errors
    total_warnings += b_warnings

print(f"\nTOTAL: {total_items} items evaluated. {total_errors} errors, {total_warnings} warnings.")
if total_errors == 0 and total_warnings == 0:
    print("ALL CLEAN: ZERO errors, ZERO warnings!")
else:
    sys.exit(1)

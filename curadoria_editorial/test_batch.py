import json
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

def test_batch(batch_path, input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        inp = json.load(f)
    inp_map = {d["id"]: d for d in inp["dialogues"]}
    
    with open(batch_path, "r", encoding="utf-8") as f:
        batch = json.load(f)
        
    hard_errors = 0
    lint_warns = 0
    
    for item in batch:
        i_id = item["id"]
        orig = inp_map[i_id]
        cur = item["curated_ptbr"]
        
        ok, errs = validador_editorial.validar_hard_gate(
            original=orig["original_jp"],
            traduzido=cur,
            ignorar_quebras=True,
            permitir_colisao_variavel=True
        )
        if not ok:
            hard_errors += len(errs)
            for e in errs:
                print(f"[HARD GATE ERROR] ID {i_id}: {e}")
                
        warns = validador_editorial.auditar_estilo_editorial(cur)
        if warns:
            lint_warns += len(warns)
            for w in warns:
                print(f"[LINT WARNING] ID {i_id}: {w}")
                
    print(f"Results for {batch_path}: {len(batch)} lines, {hard_errors} Hard Errors, {lint_warns} Lint Warnings.")
    return hard_errors, lint_warns

if __name__ == "__main__":
    b_path = sys.argv[1] if len(sys.argv) > 1 else r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_012.json"
    inp_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_012_input.json"
    test_batch(b_path, inp_path)

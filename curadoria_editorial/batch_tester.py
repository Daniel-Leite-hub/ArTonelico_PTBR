import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

def check_lines(test_list):
    total = len(test_list)
    errors = 0
    overflows = 0
    for d_id, orig_en, text, cap in test_list:
        sz = encoded_size(text)
        diff = sz - cap
        errs = validate_line(d_id, orig_en, text)
        if sz > cap:
            overflows += 1
            print(f"[OVERFLOW +{diff}B] ID {d_id} ({sz}B / {cap}B): {text}")
        if errs:
            errors += 1
            print(f"[GATE ERROR] ID {d_id}: {errs}")
    print(f"Checked {total} lines: {overflows} overflows, {errors} gate errors.")

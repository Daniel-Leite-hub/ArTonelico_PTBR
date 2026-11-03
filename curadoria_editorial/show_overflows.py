import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "curadoria_editorial"))

from generate_curated_blk_sys_010 import CURATED_MAP, db_rows
import artonelico_tool.project as proj

overflows = []
for d_id, (text, just) in CURATED_MAP.items():
    limit = db_rows[d_id][7]
    sz = proj.encoded_size(text)
    if sz > limit:
        jp = db_rows[d_id][3]
        en = db_rows[d_id][4]
        old = db_rows[d_id][6] or db_rows[d_id][5] or ""
        old_sz = proj.encoded_size(old)
        overflows.append((d_id, limit, sz, sz - limit, old, old_sz, jp, en, text))

print(f"Total overflows: {len(overflows)}")
for d_id, limit, sz, diff, old, old_sz, jp, en, text in overflows:
    print(f"ID {d_id}: limit={limit}B | cur={sz}B (+{diff}B) | old={old_sz}B ('{old}')")
    print(f"  JP: {jp}")
    print(f"  EN: {en}")
    print(f"  PROPOSED: {text}")

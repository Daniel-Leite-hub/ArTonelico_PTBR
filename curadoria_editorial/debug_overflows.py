import sqlite3
import json
import sys

sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
from artonelico_tool.project import encoded_size

from generate_curated_blk_sys_003 import CURATION, db_rows

overflows = []
for d_id, (cur_text, just) in CURATION.items():
    db_row = db_rows[d_id]
    cap = db_row[4]
    en = db_row[2]
    jp = db_row[3]
    curr_pt = db_row[5]
    sz = encoded_size(cur_text)
    if sz > cap:
        overflows.append({
            "id": d_id,
            "cap": cap,
            "sz": sz,
            "diff": sz - cap,
            "cur": cur_text,
            "en": en,
            "en_sz": encoded_size(en),
            "curr_pt": curr_pt,
            "curr_sz": encoded_size(curr_pt)
        })

print(f"Total overflows: {len(overflows)}")
for o in overflows:
    print(f"ID {o['id']} (Cap: {o['cap']}B, CurSz: {o['sz']}B, Diff: +{o['diff']}B):")
    print(f"  EN ({o['en_sz']}B): {o['en']}")
    print(f"  CurrPT ({o['curr_sz']}B): {o['curr_pt']}")
    print(f"  OurPT ({o['sz']}B): {o['cur']}\n")

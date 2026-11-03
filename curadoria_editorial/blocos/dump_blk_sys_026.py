import sqlite3
import json
import sys
sys.path.insert(0, "Ferramentas_Traducao")
from artonelico_tool.project import encoded_size

db_path = r"Ferramentas_Traducao\release\ArTonelico_PTBR_adaptado_108_20260926.atproj"
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("""
    SELECT id, event_file, original_bytes, original_jp, original, translation, reviewed, automatic
    FROM dialogues
    WHERE id BETWEEN 27530 AND 27817
    ORDER BY id
""")
rows = c.fetchall()

dump_data = []
for r in rows:
    d_id, ev_file, orig_b, jp, en, trans, rev, auto = r
    cur = rev or trans or auto or ""
    sz = encoded_size(cur) if cur else 0
    dump_data.append({
        "id": d_id,
        "file": ev_file,
        "max_bytes": orig_b,
        "cur_bytes": sz,
        "jp": jp,
        "en": en,
        "cur_pt": cur
    })

with open("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_026_dump.json", "w", encoding="utf-8") as f:
    json.dump(dump_data, f, ensure_ascii=False, indent=2)

print(f"Dumped {len(dump_data)} records to BLK_SYS_026_dump.json")

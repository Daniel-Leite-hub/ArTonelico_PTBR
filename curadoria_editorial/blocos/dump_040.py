import json
import sqlite3
import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size

conn = sqlite3.connect(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\release\ArTonelico_PTBR_adaptado_108_20260926.atproj")
c = conn.cursor()
db_sizes = {r[0]: r[1] for r in c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 31557 AND 31844").fetchall()}

with open(r"Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_040_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open(r"Ferramentas_Traducao/curadoria_editorial/blocos/blk040_full_dump.txt", "w", encoding="utf-8") as out:
    for d in data["dialogues"]:
        orig_b = db_sizes[d["id"]]
        cur_b = encoded_size(d["current_ptbr"])
        diff = cur_b - orig_b
        status = f"OVERFLOW +{diff}B ({cur_b}/{orig_b}B)" if diff > 0 else f"OK ({cur_b}/{orig_b}B)"
        out.write(f"=== ID {d['id']} | {d['event_file']} | {status} ===\n")
        out.write(f"JP: {d['original_jp']}\n")
        out.write(f"EN: {d['original_en']}\n")
        out.write(f"PT: {d['current_ptbr']}\n\n")

print("Dumped blk040_full_dump.txt successfully!")

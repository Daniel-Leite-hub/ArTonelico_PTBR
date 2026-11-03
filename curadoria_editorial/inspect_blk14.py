import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

input_file = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_014_input.json"
config_file = BASE_DIR / "curadoria_editorial" / "curadoria_config.json"
out_txt = BASE_DIR / "curadoria_editorial" / "blk14_clean_overview.txt"

with open(input_file, "r", encoding="utf-8") as f:
    input_data = json.load(f)

with open(config_file, "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 24069 AND 24350").fetchall())
conn.close()

by_file = {}
for d in input_data["dialogues"]:
    f = d.get("event_file", "unknown")
    by_file.setdefault(f, []).append(d)

with open(out_txt, "w", encoding="utf-8") as out:
    out.write(f"Total dialogues in BLK_SYS_014: {len(input_data['dialogues'])}\n")
    for f, items in by_file.items():
        out.write(f"\n==================== {f} (Count: {len(items)}, IDs: {items[0]['id']} - {items[-1]['id']}) ====================\n")
        for it in items:
            d_id = it["id"]
            cap = limits.get(d_id, 0)
            curr = it.get("current_ptbr", "")
            sz = encoded_size(curr)
            over = f"OVERFLOW +{sz - cap}B" if sz and sz > cap else "OK"
            out.write(f"ID {d_id} [Cap: {cap}B, CurSz: {sz}B, Status: {over}]\n")
            out.write(f"  JP: {it.get('original_jp')}\n")
            out.write(f"  EN: {it.get('original_en')}\n")
            out.write(f"  PT: {curr}\n")

print(f"Generated {out_txt} successfully.")

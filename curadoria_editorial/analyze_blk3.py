import sqlite3
import json
from pathlib import Path
import sys

sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
from artonelico_tool.project import encoded_size

config_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\curadoria_config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()

c.execute("""
    SELECT id, event_file, original, original_jp, original_bytes, automatic, reviewed 
    FROM dialogues 
    WHERE id BETWEEN 20883 AND 21170 
    ORDER BY id
""")
rows = c.fetchall()

analysis = []
for r in rows:
    d_id, event_file, en, jp, cap, auto, rev = r
    cur = rev if rev else (auto if auto else "")
    sz = encoded_size(cur) if cur else 0
    fits = (sz <= cap) if (sz is not None and cap is not None) else None
    analysis.append({
        "id": d_id,
        "event_file": event_file,
        "en": en,
        "jp": jp,
        "cap": cap,
        "cur": cur,
        "cur_bytes": sz,
        "fits": fits
    })

print(f"Total lines: {len(analysis)}")
overflows = [a for a in analysis if a["fits"] is False]
print(f"Current lines overflowing capacity: {len(overflows)}")
for o in overflows[:10]:
    print(f"  ID {o['id']}: Cap={o['cap']}B, Current={o['cur_bytes']}B -> '{o['cur']}'")

# Save complete analysis to json for deep inspection
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blk3_all_lines.json", "w", encoding="utf-8") as f:
    json.dump(analysis, f, ensure_ascii=False, indent=2)

print("Saved blk3_all_lines.json successfully.")

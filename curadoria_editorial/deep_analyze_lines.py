import sqlite3
import json
import sys
from pathlib import Path

sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
from artonelico_tool.project import encoded_size

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\curadoria_config.json", "r", encoding="utf-8") as f:
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

def print_range(start_id, end_id):
    sub = [r for r in rows if start_id <= r[0] <= end_id]
    for r in sub:
        d_id, ef, en, jp, cap, auto, rev = r
        cur = rev or auto or ""
        sz = encoded_size(cur)
        status = "OK" if sz <= cap else f"OVERFLOW({sz}B>{cap}B)"
        print(f"ID {d_id} [{ef}] Cap:{cap}B ({status}):\n  EN: {en}\n  JP: {jp}\n  PT: {cur}\n")

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 20883
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 20930
    print_range(start, end)

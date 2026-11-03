import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
from artonelico_tool.project import encoded_size

conn = sqlite3.connect(BASE_DIR / "ArTonelico_PTBR.atproj")
cur = conn.cursor()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_034_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def show_range(start_id, end_id):
    lines = [d for d in data["dialogues"] if start_id <= d["id"] <= end_id]
    for d in lines:
        d_id = d["id"]
        cur.execute("SELECT original_bytes FROM dialogues WHERE id = ?", (d_id,))
        cap = cur.fetchone()[0]
        pt = d.get("current_ptbr", "")
        enc = encoded_size(pt) if pt else 0
        diff = enc - cap
        status = f"OVERFLOW +{diff}B!" if diff > 0 else f"OK ({enc}/{cap}B)"
        print(f"=== ID {d_id} ({d['event_file']}) [{status}] ===")
        print(f"JP: {d['original_jp']}")
        print(f"EN: {d['original_en']}")
        print(f"PT: {pt}\n")

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 29836
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 29859
    show_range(start, end)

import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

conn = sqlite3.connect(str(BASE_DIR / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj"))
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 24650 AND 24937").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_016_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def show_batch(start_id, end_id):
    print(f"\n==================== BATCH {start_id} - {end_id} ====================")
    for d in data['dialogues']:
        d_id = d['id']
        if start_id <= d_id <= end_id:
            lim = limits.get(d_id, 0)
            pt = d.get('current_ptbr', '')
            sz = encoded_size(pt)
            diff = sz - lim
            status = f"OVERFLOW +{diff}B" if diff > 0 else f"OK ({lim - sz}B free)"
            print(f"[{d_id}] Lim:{lim}B Cur:{sz}B -> {status}")
            print(f"  JP: {d.get('original_jp')}")
            print(f"  EN: {d.get('original_en')}")
            print(f"  PT: {pt}")

if __name__ == "__main__":
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 24650
    e = int(sys.argv[2]) if len(sys.argv) > 2 else 24699
    show_batch(s, e)

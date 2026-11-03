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

overflow_count = 0
with open(BASE_DIR / "curadoria_editorial" / "blk16_overview.txt", "w", encoding="utf-8") as out:
    for d in data['dialogues']:
        d_id = d['id']
        lim = limits.get(d_id, 0)
        pt = d.get('current_ptbr', '')
        sz = encoded_size(pt)
        diff = sz - lim
        if diff > 0:
            overflow_count += 1
            status = f"OVERFLOW +{diff}B"
        else:
            status = f"OK ({lim - sz}B remaining)"
        out.write(f"=== ID {d_id} | Event: {d.get('event_file')} | Limit: {lim}B | CurSize: {sz}B | {status} ===\n")
        out.write(f"JP: {d.get('original_jp', '')}\n")
        out.write(f"EN: {d.get('original_en', '')}\n")
        out.write(f"PT: {pt}\n\n")

print(f"Exported blk16_overview.txt! Total dialogues: {len(data['dialogues'])}, Overflows: {overflow_count}")

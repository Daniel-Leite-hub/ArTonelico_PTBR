import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
from artonelico_tool.project import encoded_size

with open(BASE_DIR / "curadoria_editorial/blocos/BLK_SYS_031_output.json", encoding="utf-8") as f:
    data = json.load(f)

conn = sqlite3.connect(BASE_DIR / "release/ArTonelico_PTBR_adaptado_108_20260926.atproj")
c = conn.cursor()

overruns = []
for dlg in data["dialogues"]:
    did = dlg["id"]
    pt = dlg["curated_ptbr"]
    c.execute("SELECT original_bytes FROM dialogues WHERE id = ?", (did,))
    orig_b = c.fetchone()[0]
    sz = encoded_size(pt)
    if sz > orig_b:
        overruns.append((did, orig_b, sz, pt))

print(f"Total de falas analisadas: {len(data['dialogues'])}")
print(f"Total de estouros de buffer: {len(overruns)}")
if overruns:
    for item in overruns:
        print(f"OVER: ID {item[0]} cap={item[1]}B sz={item[2]}B -> {item[3]}")
else:
    print("ZERO ESTOUROS DE BUFFER! 100% de conformidade métrica confirmada no banco SQLite!")

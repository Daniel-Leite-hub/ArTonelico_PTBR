import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "tools"))

from artonelico_tool.project import encoded_size

inp_path = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_017_input.json"
with open(inp_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Keys in input:", list(data.keys()))
print("Line count in data:", len(data.get("dialogues", [])))
print("id_range:", data.get("id_range"))
print("scene_handoff_received:", json.dumps(data.get("scene_handoff_received", {}), ensure_ascii=False, indent=2))

conn = sqlite3.connect(BASE_DIR / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj")
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 24938 AND 25225").fetchall())
conn.close()

overflows = []
for d in data["dialogues"]:
    did = d["id"]
    pt = d.get("curated_ptbr") or d.get("current_ptbr", "")
    sz = encoded_size(pt)
    lim = limits.get(did, 9999)
    if sz > lim:
        overflows.append((did, sz, lim, sz - lim, pt))

print(f"Total dialogues: {len(data['dialogues'])}")
print(f"Initial overflows: {len(overflows)}")
for did, sz, lim, diff, pt in overflows[:15]:
    print(f"ID {did}: {sz}B > {lim}B (+{diff}B) -> {pt[:60]}...")

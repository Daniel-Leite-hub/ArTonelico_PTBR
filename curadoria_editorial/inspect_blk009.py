import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
from artonelico_tool.project import encoded_size

with open(BASE_DIR / "curadoria_editorial/blocos/BLK_SYS_009_input.json", encoding="utf-8") as f:
    data = json.load(f)

conn = sqlite3.connect(BASE_DIR / "release/ArTonelico_PTBR_adaptado_108_20260926.atproj")
c = conn.cursor()
byte_limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 22629 AND 22916").fetchall())

print("=== ALL NAMES WITH LIMIT <= 24 BYTES ===")
for d in data["dialogues"]:
    d_id = d["id"]
    limit = byte_limits[d_id]
    jp = d["original_jp"]
    en = d["original_en"]
    pt = d["current_ptbr"]
    if "CR" not in jp and limit <= 24:
        sz_pt = encoded_size(pt)
        print(f"ID {d_id} [{limit}B] (current PT: {sz_pt}B) JP: {jp} | EN: {en} | PT: {pt}")

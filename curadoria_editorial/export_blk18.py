import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))

from artonelico_tool.project import encoded_size

with open(BASE_DIR / "curadoria_editorial" / "curadoria_config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

conn = sqlite3.connect(cfg["database_path"])
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25226 AND 25513").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open(BASE_DIR / "curadoria_editorial" / "blk18_overview.txt", "w", encoding="utf-8") as out:
    for d in data["dialogues"]:
        did = d["id"]
        max_b = limits.get(did, 0)
        pt = d.get("current_ptbr", "")
        enc_b = encoded_size(pt)
        jp = d.get("original_jp", "")
        en = d.get("original_en", "")
        diff = enc_b - max_b
        status = f"OVERFLOW +{diff}" if diff > 0 else f"OK ({enc_b}/{max_b})"
        out.write(f"=== ID {did} [{status}] (max: {max_b}B, cur: {enc_b}B) ===\n")
        out.write(f"JP: {jp}\n")
        out.write(f"EN: {en}\n")
        out.write(f"PT: {pt}\n\n")

print("Generated blk18_overview.txt successfully.")

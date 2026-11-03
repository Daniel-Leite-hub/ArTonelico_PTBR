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

conn = sqlite3.connect(BASE_DIR / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj")
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 24938 AND 25225").fetchall())
conn.close()

out_txt = BASE_DIR / "curadoria_editorial" / "blk17_overview.txt"
with open(out_txt, "w", encoding="utf-8") as f:
    for d in data["dialogues"]:
        did = d["id"]
        jp = d.get("original_jp", "")
        en = d.get("original_en", "")
        pt = d.get("curated_ptbr") or d.get("current_ptbr", "")
        lim = limits.get(did, 0)
        sz = encoded_size(pt)
        diff = sz - lim
        status = f"OVERFLOW (+{diff}B)" if diff > 0 else f"OK ({sz}/{lim}B)"
        f.write(f"=== ID {did} | Limite: {lim}B | Atual: {sz}B | {status} ===\n")
        f.write(f"JP: {jp}\n")
        f.write(f"EN: {en}\n")
        f.write(f"PT: {pt}\n\n")

print(f"Exported to {out_txt}")

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
    input_data = json.load(f)

# Load CURATED from generate_curated_blk_sys_016.py without running the bottom code
curated_dict = {}
with open(BASE_DIR / "curadoria_editorial" / "generate_curated_blk_sys_016.py", "r", encoding="utf-8") as f:
    code = f.read()

# Extract CURATED definition
start = code.find("CURATED = {")
end = code.find("\n# Verificação de integridade")
curated_code = code[start:end]
exec(curated_code, globals())
curated_dict = globals()["CURATED"]

print(f"Total entries in CURATED: {len(curated_dict)}")

issues = []
for d in input_data["dialogues"]:
    d_id = d["id"]
    lim = limits[d_id]
    jp = d.get("original_jp", "")
    en = d.get("original_en", "")
    pt = d.get("current_ptbr", "")
    
    if d_id not in curated_dict:
        issues.append((d_id, "MISSING_IN_CURATED", lim, 0, "", jp, en))
        continue
        
    cur_text, rat, ver = curated_dict[d_id]
    sz = encoded_size(cur_text)
    
    # Check limit overflow
    if sz > lim:
        issues.append((d_id, f"OVERFLOW (+{sz - lim}B)", lim, sz, cur_text, jp, en))

print(f"Total issues found: {len(issues)}")
for iss in issues:
    print(f"ID {iss[0]} | {iss[1]} | Lim: {iss[2]}B, Sz: {iss[3]}B")
    print(f"  JP: {iss[5]}")
    print(f"  EN: {iss[6]}")
    print(f"  CUR: {iss[4]}")
    print("-" * 50)

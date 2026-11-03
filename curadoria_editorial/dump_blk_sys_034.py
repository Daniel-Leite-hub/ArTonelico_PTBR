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

dialogues = data["dialogues"]

with open(BASE_DIR / "curadoria_editorial" / "blk_sys_034_analysis.txt", "w", encoding="utf-8") as out:
    current_file = None
    for d in dialogues:
        d_id = d["id"]
        ef = d.get("event_file", "unknown")
        if ef != current_file:
            current_file = ef
            out.write(f"\n{'='*80}\nFILE: {ef}\n{'='*80}\n")
        
        cur.execute("SELECT original_bytes FROM dialogues WHERE id = ?", (d_id,))
        row = cur.fetchone()
        cap = row[0] if row else 0
        
        cur_text = d.get("current_ptbr", "")
        enc = encoded_size(cur_text) if cur_text else 0
        overflow = enc - cap if (cap and enc > cap) else 0
        
        out.write(f"ID: {d_id} | Cap: {cap}B | CurEnc: {enc}B | Overflow: {overflow}B\n")
        out.write(f"  JP: {d.get('original_jp', '')}\n")
        out.write(f"  EN: {d.get('original_en', '')}\n")
        out.write(f"  PT: {cur_text}\n")
        out.write("-" * 40 + "\n")

print("Dump completed to blk_sys_034_analysis.txt")

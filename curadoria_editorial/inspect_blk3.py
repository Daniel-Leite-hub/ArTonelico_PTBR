import sqlite3
import json
from pathlib import Path

config_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\curadoria_config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()

for f_num in range(27, 39):
    ef = f"SLUS/TEXT/00{f_num}"
    c.execute("SELECT id, original, original_jp, original_bytes, automatic FROM dialogues WHERE event_file = ? ORDER BY id LIMIT 3", (ef,))
    print(f"=== {ef} ===")
    for r in c.fetchall():
        print(f"  ID {r[0]}: EN='{r[1]}' | JP='{r[2]}' | Cap={r[3]}B | Cur='{r[4]}'")

conn.close()

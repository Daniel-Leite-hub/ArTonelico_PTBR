import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

conn = sqlite3.connect(str(BASE_DIR / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj"))
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 24351 AND 24649").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_015_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

print(f"Total lines in input: {len(input_data['dialogues'])}")

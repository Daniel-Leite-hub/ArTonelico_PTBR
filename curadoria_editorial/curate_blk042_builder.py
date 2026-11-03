import json
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

# Carregar arquivo de entrada
input_file = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_042_input.json")
with open(input_file, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Carregar limites do banco
import sqlite3
with open("Ferramentas_Traducao/curadoria_editorial/curadoria_config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)
conn = sqlite3.connect(cfg["database_path"])
c = conn.cursor()

caps = {}
for row in c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 32133 AND 32420").fetchall():
    caps[row[0]] = row[1]
conn.close()

print(f"Loaded {len(caps)} caps.")

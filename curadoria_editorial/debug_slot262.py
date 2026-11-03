import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from pathlib import Path
from artonelico_tool.iso import find, read_entry
from artonelico_tool.evd import encode_game_text

ROOT = Path('Ferramentas_Traducao')
iso_path = Path("G:/JOGO/PS2/Ar tonelico - Melody of Elemia (Undub)/Ar tonelico - Melody of Elemia (Undub).iso")

executable_entry = find(iso_path, "SLUS_214.45")
executable = bytearray(read_entry(iso_path, executable_entry))

MAP = 0x547CF0
index = 262
old_bytes = executable[MAP+index*2:MAP+index*2+2]
print(f"Slot {index} bytes: {old_bytes.hex()} -> {old_bytes}")
try:
    decoded = old_bytes.decode('cp932')
    print(f"Decodificado em cp932: {repr(decoded)} (U+{ord(decoded):04X})")
except Exception as e:
    print(f"Erro ao decodificar: {e}")

db = sqlite3.connect(ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
cur = db.cursor()

found = []
for col in ['reviewed', 'translation', 'automatic']:
    cur.execute(f"SELECT id, event_file, entry_index, {col} FROM dialogues WHERE {col} LIKE '%{decoded}%'")
    rows = cur.fetchall()
    for r in rows:
        found.append((col, r))

print(f"Total de ocorrências do caractere {repr(decoded)}: {len(found)}")
for col, r in found:
    print(f"[{col}] ID {r[0]} ({r[1]}[{r[2]}]): {repr(r[3][:60])}")

db.close()

import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from pathlib import Path
from artonelico_tool.evd import encode_game_text

ROOT = Path('Ferramentas_Traducao')
db = sqlite3.connect(ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
cur = db.cursor()

old = b'\x81_'

# Testar raw cp932
cur.execute("SELECT id, event_file, entry_index, reviewed, translation, automatic, original FROM dialogues")
rows = cur.fetchall()

matches = []
for r in rows:
    row_id, ev_file, idx, rev, tra, auto, orig = r
    for field_name, val in [("reviewed", rev), ("translation", tra), ("automatic", auto), ("original", orig)]:
        if not val:
            continue
        raw_cp932 = val.encode('cp932', errors='replace')
        if old in raw_cp932:
            matches.append((row_id, ev_file, idx, field_name, "raw_cp932", val))
        try:
            enc_game = encode_game_text(val)
            if old in enc_game:
                matches.append((row_id, ev_file, idx, field_name, "encode_game_text", val))
        except Exception:
            pass

print(f"Total de matches para b'\\x81_': {len(matches)}")
for m in matches:
    print(f"ID {m[0]} ({m[1]}[{m[2]}]) [{m[3]} - {m[4]}]: {repr(m[5])}")

db.close()

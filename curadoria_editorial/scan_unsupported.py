import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from pathlib import Path
from artonelico_tool.evd import encode_game_text, NativeMenuText

ROOT = Path('Ferramentas_Traducao')
db_path = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT id, event_file, entry_index, reviewed, translation FROM dialogues")
rows = cur.fetchall()

unsupported_chars = set()
bad_rows = []

for row_id, ev_file, entry_idx, reviewed, translation in rows:
    text = reviewed or translation or ""
    if not text:
        continue
    # Testar com NativeMenuText pois o test_formats usa 'native-menu-font'
    val = NativeMenuText(text)
    try:
        encode_game_text(val)
    except Exception as e:
        for ch in text:
            try:
                encode_game_text(NativeMenuText(ch))
            except Exception:
                unsupported_chars.add((ch, hex(ord(ch)), ord(ch)))
        bad_rows.append((row_id, ev_file, entry_idx, str(e), text))

print(f"Caracteres não suportados encontrados: {len(unsupported_chars)}")
for ch, hx, code in sorted(unsupported_chars, key=lambda x: x[2]):
    print(f"Char: {repr(ch)} | Hex: {hx} | Code: {code}")

print(f"\nTotal de linhas com erro: {len(bad_rows)}")
for r in bad_rows[:10]:
    print(f"ID {r[0]} ({r[1]}[{r[2]}]): {r[3]} -> {repr(r[4][:60])}")

conn.close()

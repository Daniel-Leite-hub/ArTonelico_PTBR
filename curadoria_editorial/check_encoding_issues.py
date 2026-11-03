import sqlite3
import sys

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.evd import encode_game_text

conn = sqlite3.connect('Ferramentas_Traducao/release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cur.fetchall()]
print("Tabelas no banco:", tables)

target_table = "dialogues" if "dialogues" in tables else tables[0]
print(f"Auditando tabela: {target_table}")

cur.execute(f"PRAGMA table_info({target_table})")
cols = [r[1] for r in cur.fetchall()]
print("Colunas:", cols)

text_col = "translation"
cur.execute(f"SELECT id, event_file, {text_col} FROM dialogues")
rows = cur.fetchall()

errors = []
for row_id, file_orig, text in rows:
    if not text:
        continue
    try:
        encode_game_text(text)
    except Exception as e:
        errors.append((row_id, file_orig, text, str(e)))

print(f"Total de falhas no encode_game_text: {len(errors)}")
for row_id, file_orig, text, err in errors:
    print(f"ID {row_id} ({file_orig}): {err} -> {repr(text[:60])}")

conn.close()

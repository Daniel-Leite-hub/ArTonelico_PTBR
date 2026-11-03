import sqlite3

db = sqlite3.connect('Ferramentas_Traducao/release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
cur = db.cursor()

cur.execute("SELECT id, event_file, entry_index, reviewed, translation FROM dialogues WHERE reviewed LIKE '%\\n%' OR translation LIKE '%\\n%'")
# Atenção: no SQL LIKE, '\\' é escape, então vamos varrer via Python
cur.execute("SELECT id, event_file, entry_index, reviewed, translation, automatic FROM dialogues")
rows = cur.fetchall()

escaped_newlines = []
for r in rows:
    row_id, ev_file, idx, rev, tra, auto = r
    for field_name, val in [("reviewed", rev), ("translation", tra), ("automatic", auto)]:
        if val and "\\n" in val:
            escaped_newlines.append((row_id, ev_file, idx, field_name, val))

print(f"Total de ocorrências com '\\\\n' literal: {len(escaped_newlines)}")
for row_id, ev_file, idx, field_name, val in escaped_newlines[:20]:
    print(f"ID {row_id} ({ev_file}[{idx}]) [{field_name}]: {repr(val[:70])}")

db.close()

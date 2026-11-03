import sqlite3

db_path = r'Ferramentas_Traducao\release\ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT id, original_jp, original, automatic, reviewed FROM dialogues WHERE original_jp LIKE '%オボンヌ%'")
for r in c.fetchall():
    print(f"ID {r[0]} | JP: {r[1]} | EN: {r[2]} | PT: {r[4] or r[3]}")
conn.close()

import sqlite3

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
cur = conn.cursor()
cur.execute("SELECT id, translation, original_jp, original FROM dialogues WHERE original_jp LIKE '%魔神シャドウ%'")
rows = cur.fetchall()
for r in rows:
    print(r)

print('--- Red Magic items in general ---')
cur.execute("SELECT id, translation, original_jp, original FROM dialogues WHERE original_jp LIKE '%赤魔法【%' LIMIT 10")
for r in cur.fetchall():
    print(r)

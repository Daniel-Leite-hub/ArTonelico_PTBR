import sqlite3

conn = sqlite3.connect('Ferramentas_Traducao/traducao.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = c.fetchall()
print('Tables:', tables)

for t in tables:
    table_name = t[0]
    c.execute(f"PRAGMA table_info({table_name})")
    cols = [col[1] for col in c.fetchall()]
    print(f"Table {table_name}: {cols}")
    c.execute(f"SELECT COUNT(*) FROM {table_name}")
    print(f"Count in {table_name}: {c.fetchone()[0]}")

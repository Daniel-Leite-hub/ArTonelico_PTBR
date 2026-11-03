# -*- coding: utf-8 -*-
import sqlite3, json

cfg = json.load(open('Ferramentas_Traducao/curadoria_editorial/curadoria_config.json', 'r', encoding='utf-8'))
conn = sqlite3.connect(cfg['database_path'])
c = conn.cursor()

rows = c.execute("SELECT id, original_jp, original, translation FROM dialogues WHERE original_jp LIKE '%紡ぎ出した%'").fetchall()
for r in rows:
    print(f"ID {r[0]}: JP={repr(r[1])} | PT={repr(r[3])}")

conn.close()

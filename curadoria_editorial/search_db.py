# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect(r'Ferramentas_Traducao\release\ArTonelico_PTBR_adaptado_108_20260926.atproj')
cur = conn.cursor()
cur.execute("SELECT id, original_jp, original, translation FROM dialogues WHERE original_jp LIKE '%赤魔法%' OR original_jp LIKE '%青魔法%'")
for r in cur.fetchall():
    print(r)
conn.close()

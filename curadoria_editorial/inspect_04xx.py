# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

c.execute("SELECT event_file, MIN(id), MAX(id), count(*) FROM dialogues WHERE event_file LIKE 'SLUS/TEXT/04%' GROUP BY event_file ORDER BY MIN(id)")
for r in c.fetchall():
    print(r)

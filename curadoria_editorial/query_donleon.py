import sqlite3
import json

with open('Ferramentas_Traducao/curadoria_editorial/curadoria_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

conn = sqlite3.connect(config['database_path'])
c = conn.cursor()

c.execute("SELECT id, original_jp, original, reviewed, automatic FROM dialogues WHERE original LIKE '%Don Leon%' AND original LIKE '%Eruption%'")
for row in c.fetchall():
    print(row)

c.execute("SELECT id, original_jp, original, reviewed, automatic FROM dialogues WHERE original LIKE '%Don Leon%' LIMIT 10")
for row in c.fetchall():
    print(row)

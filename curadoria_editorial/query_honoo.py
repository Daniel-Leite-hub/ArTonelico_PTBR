import sqlite3
import json

with open('Ferramentas_Traducao/curadoria_editorial/curadoria_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

conn = sqlite3.connect(config['database_path'])
c = conn.cursor()

c.execute("SELECT id, original_jp, original, reviewed, automatic FROM dialogues WHERE original_jp LIKE '%メッソー%'")
for row in c.fetchall():
    print(f"ID {row[0]}: JP: {row[1]} | EN: {row[2]} | REV: {row[3]} | AUTO: {row[4]}")

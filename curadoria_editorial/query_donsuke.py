import sqlite3
import json

with open('Ferramentas_Traducao/curadoria_editorial/curadoria_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

conn = sqlite3.connect(config['database_path'])
c = conn.cursor()

print("--- Query ドン助大噴火 ---")
c.execute("SELECT id, original_jp, original, reviewed, automatic FROM dialogues WHERE original_jp LIKE '%ドン助大噴火%'")
for row in c.fetchall():
    print(row)

print("--- Query 動力部 ---")
c.execute("SELECT id, original_jp, original, reviewed, automatic FROM dialogues WHERE original_jp LIKE '%動力部%' LIMIT 5")
for row in c.fetchall():
    print(row)

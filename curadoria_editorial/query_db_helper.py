import sqlite3
import json

with open('Ferramentas_Traducao/curadoria_editorial/curadoria_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

conn = sqlite3.connect(config['database_path'])
c = conn.cursor()

print("--- Query 星詠 in reviewed dialogues ---")
c.execute("SELECT id, original_jp, original, reviewed FROM dialogues WHERE original_jp LIKE '%星詠%' AND reviewed != '' LIMIT 10")
for row in c.fetchall():
    print(f"ID {row[0]}: JP: {row[1]} | EN: {row[2]} | REV: {row[3]}")

print("\n--- Query アンビエンスフィールド in DB ---")
c.execute("SELECT id, original_jp, original, reviewed FROM dialogues WHERE original_jp LIKE '%アンビエンス%' LIMIT 5")
for row in c.fetchall():
    print(f"ID {row[0]}: JP: {row[1]} | EN: {row[2]} | REV: {row[3]}")

print("\n--- Query 炎打撃 in DB ---")
c.execute("SELECT id, original_jp, original, reviewed FROM dialogues WHERE original_jp LIKE '%炎打撃%' LIMIT 5")
for row in c.fetchall():
    print(f"ID {row[0]}: JP: {row[1]} | EN: {row[2]} | REV: {row[3]}")

print("\n--- Query ストーンヘンジ in reviewed dialogues ---")
c.execute("SELECT id, original_jp, original, reviewed FROM dialogues WHERE original_jp LIKE '%ストーンヘンジ%' AND reviewed != '' LIMIT 5")
for row in c.fetchall():
    print(f"ID {row[0]}: JP: {row[1]} | EN: {row[2]} | REV: {row[3]}")

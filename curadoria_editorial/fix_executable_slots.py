import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from pathlib import Path
from artonelico_tool.project import text_digest

ROOT = Path('Ferramentas_Traducao')
db_path = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 1. ID 20374 -> 'Lento'
text_20374 = 'Lento'
digest_20374 = text_digest(text_20374)
cur.execute(
    "UPDATE dialogues SET reviewed = ?, translation = ?, automatic = ?, reviewed_hash = ? WHERE id = 20374",
    (text_20374, text_20374, text_20374, digest_20374)
)

# 2. ID 20384 -> 'Cosmosfera Máx'
text_20384 = 'Cosmosfera Máx'
digest_20384 = text_digest(text_20384)
cur.execute(
    "UPDATE dialogues SET reviewed = ?, translation = ?, automatic = ?, reviewed_hash = ? WHERE id = 20384",
    (text_20384, text_20384, text_20384, digest_20384)
)

conn.commit()
print("IDs 20374 e 20384 atualizados e hasheados com sucesso!")
conn.close()

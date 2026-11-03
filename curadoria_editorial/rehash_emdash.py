import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from pathlib import Path
from artonelico_tool.project import text_digest

ROOT = Path('Ferramentas_Traducao')
db_path = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

ids_to_rehash = [42, 14916, 14923, 14934, 14936, 14937, 19518, 19524, 19652]
for row_id in ids_to_rehash:
    cur.execute("SELECT id, event_file, entry_index, reviewed FROM dialogues WHERE id = ?", (row_id,))
    r = cur.fetchone()
    if r:
        digest = text_digest(r[3])
        cur.execute("UPDATE dialogues SET reviewed_hash = ? WHERE id = ?", (digest, row_id))

conn.commit()
print("Hashes criptográficos atualizados com sucesso para todas as linhas ajustadas!")
conn.close()

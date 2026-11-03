import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from pathlib import Path
from artonelico_tool.project import text_digest

ROOT = Path('Ferramentas_Traducao')
db_path = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT id, event_file, entry_index, reviewed, translation FROM dialogues WHERE reviewed LIKE '%«%' OR reviewed LIKE '%»%' OR translation LIKE '%«%' OR translation LIKE '%»%'")
rows = cur.fetchall()
print(f"Total de linhas com guillemets no banco: {len(rows)}")

for row_id, ev_file, entry_idx, reviewed, translation in rows:
    new_rev = reviewed.replace("«", '"').replace("»", '"') if reviewed else reviewed
    new_tra = translation.replace("«", '"').replace("»", '"') if translation else translation
    digest = text_digest(new_rev) if new_rev else None
    
    cur.execute(
        "UPDATE dialogues SET reviewed = ?, translation = ?, automatic = ?, reviewed_hash = ? WHERE id = ?",
        (new_rev, new_tra, new_rev, digest, row_id)
    )

conn.commit()
print("Todas as linhas com guillemets foram convertidas para aspas canônicas e re-hasheadas com sucesso!")
conn.close()

import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from pathlib import Path
from artonelico_tool.project import text_digest

ROOT = Path('Ferramentas_Traducao')
db_path = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

ids_to_fix = [2465, 2466, 2467, 2530, 2531]
for row_id in ids_to_fix:
    cur.execute("SELECT id, reviewed, translation, automatic FROM dialogues WHERE id = ?", (row_id,))
    r = cur.fetchone()
    rev = r[1].replace("\\n", "\n") if r[1] else r[1]
    tra = r[2].replace("\\n", "\n") if r[2] else r[2]
    auto = r[3].replace("\\n", "\n") if r[3] else r[3]
    digest = text_digest(rev)
    cur.execute(
        "UPDATE dialogues SET reviewed = ?, translation = ?, automatic = ?, reviewed_hash = ? WHERE id = ?",
        (rev, tra, auto, digest, row_id)
    )
    print(f"ID {row_id} corrigido: {repr(rev)}")

conn.commit()
print("Todas as quebras literais \\n foram convertidas para quebras reais de linha e re-hasheadas!")
conn.close()

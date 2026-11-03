import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from pathlib import Path

ROOT = Path('Ferramentas_Traducao')
db_path = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT id, event_file, entry_index, reviewed, translation FROM dialogues WHERE reviewed LIKE '%\u2014%' OR translation LIKE '%\u2014%'")
rows = cur.fetchall()
print(f"Total de linhas com em-dash no banco: {len(rows)}")
for r in rows:
    row_id, ev_file, entry_idx, reviewed, translation = r
    print(f"ID {row_id} | {ev_file} [{entry_idx}]:")
    
    # Ajustar reviewed
    new_rev = reviewed.replace(" — ", " - ").replace("—", "-") if reviewed else reviewed
    new_tra = translation.replace(" — ", " - ").replace("—", "-") if translation else translation
    
    print(f"  Old reviewed: {repr(reviewed)}")
    print(f"  New reviewed: {repr(new_rev)}")
    
    cur.execute("UPDATE dialogues SET reviewed = ?, translation = ?, automatic = ? WHERE id = ?", (new_rev, new_tra, new_rev, row_id))

conn.commit()
print("Atualizações gravadas com sucesso no banco!")
conn.close()

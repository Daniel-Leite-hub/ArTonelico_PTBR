import sqlite3
import json

db_path = 'Ferramentas_Traducao/release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('SELECT count(*) FROM dialogues')
total_dialogues = c.fetchone()[0]

c.execute("SELECT count(*) FROM dialogues WHERE review_status = 'approved' AND review_origin = 'curadoria_editorial'")
curated_dialogues = c.fetchone()[0]

conn.close()

ledger_path = 'Ferramentas_Traducao/curadoria_editorial/scene_breakdown_ledger.json'
with open(ledger_path, 'r', encoding='utf-8') as f:
    ledger = json.load(f)

blocks = ledger['blocks']
total_blocks = len(blocks)
completed_blocks = sum(1 for b in blocks if b['status'] == 'concluido')

sys_blocks = [b for b in blocks if b['block_id'].startswith('BLK_SYS')]
evd_blocks = [b for b in blocks if b['block_id'].startswith('BLK_EVD')]

completed_sys = sum(1 for b in sys_blocks if b['status'] == 'concluido')
completed_evd = sum(1 for b in evd_blocks if b['status'] == 'concluido')

print(f"TOTAL_DIALOGUES: {total_dialogues}")
print(f"CURATED_DIALOGUES: {curated_dialogues} ({curated_dialogues/total_dialogues*100:.2f}%)")
print(f"TOTAL_BLOCKS: {total_blocks}")
print(f"COMPLETED_BLOCKS: {completed_blocks} ({completed_blocks/total_blocks*100:.2f}%)")
print(f"SYS_BLOCKS: {completed_sys}/{len(sys_blocks)} ({completed_sys/len(sys_blocks)*100:.2f}%)")
print(f"EVD_BLOCKS: {completed_evd}/{len(evd_blocks)} ({completed_evd/len(evd_blocks)*100:.2f}%)")

lote_ids = ['BLK_EVD_032', 'BLK_EVD_033', 'BLK_EVD_034', 'BLK_EVD_035', 'BLK_EVD_036', 'BLK_EVD_037']
lote_lines = sum(b['line_count'] for b in blocks if b['block_id'] in lote_ids)
print(f"LOTE_LINES: {lote_lines}")

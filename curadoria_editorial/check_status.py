import sqlite3
import json

conn = sqlite3.connect('Ferramentas_Traducao/release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
cur = conn.cursor()
cur.execute('SELECT COUNT(1) FROM dialogues')
total = cur.fetchone()[0]
cur.execute("SELECT COUNT(1) FROM dialogues WHERE review_status = 'approved'")
apr = cur.fetchone()[0]

with open('Ferramentas_Traducao/curadoria_editorial/scene_breakdown_ledger.json', 'r', encoding='utf-8') as f:
    ledger = json.load(f)

blocks_done = sum(1 for b in ledger['blocks'] if b['status'] == 'concluido')
blocks_total = len(ledger['blocks'])

axis_stats = {}
for b in ledger['blocks']:
    axis = b.get('axis', 'UNKNOWN')
    axis_stats.setdefault(axis, [0, 0])
    axis_stats[axis][1] += 1
    if b['status'] == 'concluido':
        axis_stats[axis][0] += 1

print(f"FALAS: {apr} de {total} ({apr/total*100:.2f}%)")
print(f"BLOCOS: {blocks_done} de {blocks_total} ({blocks_done/blocks_total*100:.2f}%)")
for ax, (done, tot) in sorted(axis_stats.items()):
    print(f"  {ax}: {done}/{tot} ({done/tot*100:.2f}%)")

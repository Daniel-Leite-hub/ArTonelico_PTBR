import sys
import json
import sqlite3

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_041_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/blk041_full_dump.txt', 'w', encoding='utf-8') as out:
    for d in data['dialogues']:
        d_id = d['id']
        row = c.execute('SELECT original_bytes, original_jp, original, translation FROM dialogues WHERE id = ?', (d_id,)).fetchone()
        orig_b = row[0]
        orig_jp = row[1] or d.get('original_jp', '')
        orig_en = row[2] or d.get('original_en', '')
        cur_pt = row[3] or d.get('current_ptbr', '')
        cur_sz = encoded_size(cur_pt)
        ov = 'OVERFLOW' if cur_sz > orig_b else 'OK'
        
        out.write(f"ID: {d_id} | File: {d.get('event_file')} | Bytes: {cur_sz}/{orig_b} [{ov}]\n")
        out.write(f"  JP: {orig_jp}\n")
        out.write(f"  EN: {orig_en}\n")
        out.write(f"  PT: {cur_pt}\n\n")

print("Dumped blk041_full_dump.txt")

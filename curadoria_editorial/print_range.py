import json
import sqlite3
import sys

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_038_input.json', 'r', encoding='utf-8') as f:
    inp = json.load(f)

for d in inp['dialogues']:
    c.execute('SELECT original_bytes FROM dialogues WHERE id = ?', (d['id'],))
    d['original_bytes'] = c.fetchone()[0]

def print_file_range(start_id, end_id):
    lines = [d for d in inp['dialogues'] if start_id <= d['id'] <= end_id]
    for d in lines:
        cur_sz = encoded_size(d.get('current_ptbr') or '')
        diff = cur_sz - d['original_bytes']
        tag = f"+{diff}" if diff > 0 else f"{diff}"
        print(f"[{d['id']}] (cap {d['original_bytes']}B, cur {cur_sz}B, {tag})")
        print(f"  JP: {d.get('original_jp')}")
        print(f"  EN: {d.get('original_en')}")
        print(f"  PT: {d.get('current_ptbr')}")

if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    print_file_range(start, end)

# -*- coding: utf-8 -*-
import json, sqlite3, sys
sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

chunk4 = [x for x in d['dialogues'] if 31413 <= x['id'] <= 31460]
print(f"Chunk 4 lines: {len(chunk4)}")

with open('Ferramentas_Traducao/curadoria_editorial/chunk4_view.txt', 'w', encoding='utf-8') as out:
    for x in chunk4:
        c.execute('SELECT original_bytes FROM dialogues WHERE id = ?', (x['id'],))
        ob = c.fetchone()[0]
        sz = encoded_size(x.get('current_ptbr') or '')
        diff = sz - ob
        flag = f"[OVERFLOW +{diff}B]" if diff > 0 else "[OK]"
        out.write(f"[{x['id']}] Cap:{ob:3d}B Cur:{sz:3d}B {flag} File:{x['event_file']}\n")
        out.write(f"  JP: {x['original_jp']}\n")
        out.write(f"  EN: {x['original_en']}\n")
        out.write(f"  PT: {x.get('current_ptbr', '')}\n\n")

print("Wrote chunk4_view.txt successfully")

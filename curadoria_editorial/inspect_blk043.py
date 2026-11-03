import json, sqlite3, sys
from collections import defaultdict
sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

cfg = json.load(open('Ferramentas_Traducao/curadoria_editorial/curadoria_config.json', 'r', encoding='utf-8'))
conn = sqlite3.connect(cfg['database_path'])
c = conn.cursor()
caps = {row[0]: row[1] for row in c.execute('SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 32421 AND 32708').fetchall()}
conn.close()

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_043_input.json', 'r', encoding='utf-8'))
dialogues = data['dialogues']

by_file = defaultdict(list)
for d in dialogues:
    by_file[d.get('event_file')].append(d)

for f in sorted(by_file.keys()):
    lines = by_file[f]
    first_id = lines[0]['id']
    last_id = lines[-1]['id']
    print(f'=== {f} ({len(lines)} lines: {first_id}..{last_id}) ===')
    for l in lines[:3]:
        lid = l['id']
        jp = l.get('original_jp', '').replace(chr(10), ' ')
        en = l.get('original_en', '').replace(chr(10), ' ')
        pt = l.get('current_ptbr', '').replace(chr(10), ' ')
        sz = encoded_size(l.get('current_ptbr', ''))
        cap = caps.get(lid, 0)
        print(f'  [{lid}] ({sz}B/{cap}B) JP: {jp}')
        print(f'       EN: {en}')
        print(f'       PT: {pt}')

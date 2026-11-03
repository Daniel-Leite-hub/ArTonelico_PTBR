import json
import sys

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_079_input.json', encoding='utf-8'))
dialogues = data['dialogues']

start = 0
count = 35
if len(sys.argv) > 1:
    start = int(sys.argv[1])
if len(sys.argv) > 2:
    count = int(sys.argv[2])

for d in dialogues[start:start+count]:
    spk = d.get('speaker', 'Unknown')
    line_id = d['id']
    ev = d.get('event_file')
    jp = d.get('original_jp', '').replace('\n', '\\n')
    en = d.get('original_en', '').replace('\n', '\\n')
    pt = d.get('current_ptbr', '').replace('\n', '\\n')
    print(f"[{line_id}] ({ev}) {spk}:")
    print(f"  JP: {jp}")
    print(f"  EN: {en}")
    print(f"  PT: {pt}")

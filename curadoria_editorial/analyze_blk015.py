import json
from itertools import groupby

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_015_input.json', encoding='utf-8') as f:
    d = json.load(f)

for ev, group in groupby(d['dialogues'], key=lambda x: x['event_file']):
    lines = list(group)
    spks = sorted(list(set(x['speaker'] for x in lines)))
    print(f"{ev}: IDs {lines[0]['id']}..{lines[-1]['id']} ({len(lines)} lines) | Speakers: {spks}")

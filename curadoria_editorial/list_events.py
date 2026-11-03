import json

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_008_input.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

events = {}
for d in data['dialogues']:
    events.setdefault(d['event_file'], []).append(d)

print("List of events and count:")
for ef, lines in events.items():
    print(f"{ef:16} | {len(lines):2d} lines | IDs: {lines[0]['id']}..{lines[-1]['id']}")

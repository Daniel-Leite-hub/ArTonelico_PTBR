import json

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_008_input.json"
with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

events = {}
for d in data.get('dialogues', []):
    ef = d.get('event_file')
    if ef not in events:
        events[ef] = []
    events[ef].append(d)

print(f"Total events: {len(events)}, Total lines: {len(data['dialogues'])}")
for idx, (ef, lines) in enumerate(events.items(), 1):
    spk = sorted(list(set(x['speaker'] for x in lines)))
    print(f"{idx:02d}. {ef:16} | lines: {len(lines):2d} | IDs: {lines[0]['id']:4d}..{lines[-1]['id']:4d} | Speakers: {spk}")

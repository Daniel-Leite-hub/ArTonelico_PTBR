import json

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_008_input.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

events = {}
for d in data['dialogues']:
    events.setdefault(d['event_file'], []).append(d)

for ef, lines in list(events.items())[6:12]:
    print(f"\n=======================================================")
    print(f"FILE: {ef} ({len(lines)} lines)")
    print(f"=======================================================")
    for l in lines:
        print(f"ID {l['id']} [{l['speaker']}]:")
        print(f"  JP: {l['original_jp']}")
        print(f"  EN: {l['original_en']}")
        print(f"  PT: {l['current_ptbr']}")

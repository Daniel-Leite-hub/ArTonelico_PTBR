import json

data = json.load(open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_083_input.json', encoding='utf-8'))

for ev in ['Event/323.evd', 'Event/598.evd', 'Event/953.evd', 'Event/766.evd']:
    dl = [d for d in data['dialogues'] if d.get('event_file') == ev]
    id_start = dl[0]['id']
    id_end = dl[-1]['id']
    speakers = list(dict.fromkeys(d.get('speaker') for d in dl))
    print(f"=== {ev}: {len(dl)} lines, IDs {id_start} to {id_end} ===")
    print("  Speakers:", speakers)

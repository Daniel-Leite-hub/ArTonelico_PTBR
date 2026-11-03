import json

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_079_input.json', encoding='utf-8'))
for ev_target in ['Event/603.evd', 'Event/228.evd', 'Event/116.evd']:
    print(f"\n==================== {ev_target} ====================")
    for d in data['dialogues']:
        if d['event_file'] == ev_target:
            print(f"--- ID {d['id']} | {d.get('speaker')} ---")
            print(f"JP: {d.get('original_jp')}")
            print(f"EN: {d.get('original_en')}")
            print(f"PT: {d.get('current_ptbr')}\n")

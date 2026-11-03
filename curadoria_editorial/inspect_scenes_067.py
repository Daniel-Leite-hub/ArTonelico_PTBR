import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_067_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for ev in ['Event/118.evd', 'Event/294.evd', 'Event/642.evd']:
    lines = [x for x in d['dialogues'] if x['event_file'] == ev]
    print(f"=== {ev} (Total: {len(lines)}) ===")
    id0 = lines[0]['id']
    id1 = lines[-1]['id']
    print(f"ID range: {id0} - {id1}")
    speakers = set(x['speaker'] for x in lines)
    print(f"Speakers: {speakers}")
    print("First 3 lines:")
    for x in lines[:3]:
        print(f"  [{x['id']}] {x['speaker']}: JP: {x['original_jp']} | EN: {x['original_en']}")
    print("Last 2 lines:")
    for x in lines[-2:]:
        print(f"  [{x['id']}] {x['speaker']}: JP: {x['original_jp']} | EN: {x['original_en']}")
    print()

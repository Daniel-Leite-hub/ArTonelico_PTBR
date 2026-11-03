import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_075_input.json', encoding='utf-8') as f:
    data = json.load(f)

lines = data['dialogues']
events = {}
for l in lines:
    ev = l['event_file']
    events.setdefault(ev, []).append(l)

for ev, dlist in events.items():
    speakers = set(d['speaker'] for d in dlist)
    print(f"=== Event: {ev} ({len(dlist)} lines) ===")
    print("Speakers:", speakers)
    print(f"Range: {dlist[0]['id']} - {dlist[-1]['id']}")
    print("Sample 0 (JP):", repr(dlist[0]['original_jp']))
    print("Sample 0 (EN):", repr(dlist[0]['original_en']))
    print("Sample 0 (PT):", repr(dlist[0]['current_ptbr']))
    print("Sample mid (JP):", repr(dlist[len(dlist)//2]['original_jp']))
    print("Sample mid (EN):", repr(dlist[len(dlist)//2]['original_en']))
    print("Sample mid (PT):", repr(dlist[len(dlist)//2]['current_ptbr']))
    print()

import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_089_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = data.get('dialogues', [])
print(f"Total lines: {len(lines)}")
print(f"ID range: {lines[0]['id']} to {lines[-1]['id']}")

events = {}
for i, d in enumerate(lines):
    ef = d.get('event_file')
    if ef not in events:
        events[ef] = []
    events[ef].append((i, d['id'], d.get('speaker', 'N/A'), d))

for ef, items in events.items():
    print(f"\n--- {ef}: {len(items)} lines (IDs {items[0][1]} to {items[-1][1]}) ---")
    speakers = set(x[2] for x in items)
    print(f"Speakers: {speakers}")
    print("First 3 lines:")
    for x in items[:3]:
        d = x[3]
        print(f"  [{d['id']}] {d.get('speaker')}: JP='{d.get('original_jp')}' | EN='{d.get('original_en')}' | PT='{d.get('current_ptbr')}'")
    print("Last 3 lines:")
    for x in items[-3:]:
        d = x[3]
        print(f"  [{d['id']}] {d.get('speaker')}: JP='{d.get('original_jp')}' | EN='{d.get('original_en')}' | PT='{d.get('current_ptbr')}'")

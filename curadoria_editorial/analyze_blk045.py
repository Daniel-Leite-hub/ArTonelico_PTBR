import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_045_input.json', encoding='utf-8') as f:
    data = json.load(f)

dialogues = data['dialogues']
print(f"Total lines: {len(dialogues)}")
speakers = {}
for d in dialogues:
    spk = d.get('speaker', 'Unknown')
    speakers[spk] = speakers.get(spk, 0) + 1
print("Speakers count:", speakers)

for i in [0, 20, 50, 80, 120, 160, 200, 240, 278]:
    if i < len(dialogues):
        d = dialogues[i]
        print(f"--- Line {i} (ID {d['id']}) [{d.get('speaker')}] ---")
        print("JP:", repr(d.get('original_jp')))
        print("EN:", repr(d.get('original_en')))
        print("PT:", repr(d.get('current_ptbr')))

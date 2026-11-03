# -*- coding: utf-8 -*-
import json
from collections import Counter

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_043_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

dialogues = data['dialogues']
print("Total dialogues:", len(dialogues))
print("First ID:", dialogues[0]['id'], "Last ID:", dialogues[-1]['id'])
print("Keys in dialogue[0]:", list(dialogues[0].keys()))

speakers = Counter(d.get('speaker', 'Unknown') for d in dialogues)
print("\nSpeakers breakdown:")
for spk, cnt in speakers.most_common():
    print(f"  {spk}: {cnt}")

print("\nFirst 10 dialogues:")
for d in dialogues[:10]:
    print(f"--- ID {d['id']} ({d.get('speaker', '')}) ---")
    print("  JP:", repr(d.get('original_jp', '')))
    print("  EN:", repr(d.get('original_en', '')))
    print("  PT:", repr(d.get('current_pt', '')))

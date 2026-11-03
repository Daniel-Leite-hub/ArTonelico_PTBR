import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_090_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/all_090_raw.txt', 'w', encoding='utf-8') as f:
    for d in data['dialogues']:
        f.write(f"=== ID: {d['id']} | File: {d['event_file']} | Speaker: {d['speaker']} ({d['speaker_id']}) ===\n")
        f.write(f"JP: {d['original_jp']}\n")
        f.write(f"EN: {d['original_en']}\n")
        f.write(f"PT: {d.get('curated_ptbr') or d.get('text_ptbr') or d.get('current_ptbr')}\n\n")

print(f"Dumped successfully, total lines: {len(data['dialogues'])}")

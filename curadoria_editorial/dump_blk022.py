import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_022_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/all_blk022_raw.txt', 'w', encoding='utf-8') as out:
    for d in data['dialogues']:
        out.write(f"=== ID: {d['id']} | Event: {d['event_file']} | Speaker: {d['speaker']} (ID {d.get('speaker_id')}) ===\n")
        out.write(f"JP: {d.get('original_jp', '')}\n")
        out.write(f"EN: {d.get('original_en', '')}\n")
        out.write(f"PT: {d.get('current_ptbr', '')}\n\n")

print(f"Dumped {len(data['dialogues'])} dialogues to all_blk022_raw.txt")

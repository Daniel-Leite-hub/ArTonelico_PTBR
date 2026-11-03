import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_065_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/all_blk065_raw.txt', 'w', encoding='utf-8') as out:
    for item in d['dialogues']:
        out.write(f"=== ID: {item['id']} | Speaker: {item['speaker']} ({item.get('speaker_id')}) | File: {item['event_file']} ===\n")
        out.write(f"JP: {item['original_jp']}\n")
        out.write(f"EN: {item['original_en']}\n")
        out.write(f"PT: {item['current_ptbr']}\n\n")

print(f"Wrote {len(d['dialogues'])} lines to all_blk065_raw.txt")

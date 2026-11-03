import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_075_input.json', encoding='utf-8') as f:
    data = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/all_blk075_raw.txt', 'w', encoding='utf-8') as out:
    for d in data['dialogues']:
        out.write(f"ID: {d['id']} | Event: {d['event_file']} | Speaker: {d['speaker']}\n")
        out.write(f"JP: {d['original_jp']}\n")
        out.write(f"EN: {d['original_en']}\n")
        out.write(f"PT: {d['current_ptbr']}\n")
        out.write("-" * 80 + "\n")

print("Dumped 189 lines to all_blk075_raw.txt")

import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_087_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/blk087_inspection.txt', 'w', encoding='utf-8') as out:
    for item in d['dialogues']:
        out.write(f"[{item['id']}] ({item['event_file']}) {item['speaker']} (ID:{item['speaker_id']}):\n")
        out.write(f"  JP:   {item['original_jp']}\n")
        out.write(f"  EN:   {item['original_en']}\n")
        out.write(f"  PTBR: {item['current_ptbr']}\n\n")

print(f"Dumped {len(d['dialogues'])} lines to blk087_inspection.txt")

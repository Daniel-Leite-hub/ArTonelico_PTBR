import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_053_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/all_blk053_raw.txt', 'w', encoding='utf-8') as f:
    for d in data['dialogues']:
        f.write(f"[{d['id']}] ({d.get('event_file')}) {d.get('speaker')} [{d.get('speaker_id')}]:\n")
        f.write(f"  JP: {d.get('original_jp')}\n")
        f.write(f"  EN: {d.get('original_en')}\n")
        f.write(f"  PT: {d.get('current_ptbr')}\n\n")

print(f"Dumped {len(data['dialogues'])} lines to all_blk053_raw.txt")

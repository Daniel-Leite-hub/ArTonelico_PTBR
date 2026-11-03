import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_061_input.json', encoding='utf-8') as f:
    data = json.load(f)

with open('Ferramentas_Traducao/curadoria_editorial/blk061_lines_dump.txt', 'w', encoding='utf-8') as out:
    for d in data['dialogues']:
        out.write(f"=== ID {d['id']} | {d.get('event_file')} | {d.get('speaker')} (ID {d.get('speaker_id')}) ===\n")
        out.write(f"JP: {d.get('original_jp')}\n")
        out.write(f"EN: {d.get('original_en')}\n")
        out.write(f"DRAFT: {d.get('text_ptbr')}\n\n")

print("Dumped 185 lines successfully.")

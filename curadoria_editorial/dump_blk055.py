import json

input_path = "Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_055_input.json"
output_dump = "Ferramentas_Traducao/curadoria_editorial/blocos/dump_055.txt"

with open(input_path, "r", encoding="utf-8") as f:
    d = json.load(f)

with open(output_dump, "w", encoding="utf-8") as f:
    for line in d["dialogues"]:
        f.write(f"[{line['id']}] [{line.get('event_file')}] {line.get('speaker')} (ID: {line.get('speaker_id')})\n")
        f.write(f"JP: {line.get('original_jp')}\n")
        f.write(f"EN: {line.get('original_en')}\n")
        f.write(f"PT: {line.get('current_ptbr')}\n")
        f.write("-" * 60 + "\n")

print(f"Dumped {len(d['dialogues'])} lines to {output_dump}")

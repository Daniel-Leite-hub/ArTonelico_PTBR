import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_089_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = data.get('dialogues', [])
with open('Ferramentas_Traducao/curadoria_editorial/all_089_raw.txt', 'w', encoding='utf-8') as out:
    for i, d in enumerate(lines):
        out.write(f"=== [{i}] ID: {d['id']} | Event: {d.get('event_file')} | Speaker: {d.get('speaker')} (ID: {d.get('speaker_id')}) ===\n")
        out.write(f"JP: {d.get('original_jp')}\n")
        out.write(f"EN: {d.get('original_en')}\n")
        out.write(f"PT: {d.get('current_ptbr')}\n\n")

print(f"Dumped {len(lines)} lines to Ferramentas_Traducao/curadoria_editorial/all_089_raw.txt")

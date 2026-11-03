import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_001_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = []
for d in data['dialogues']:
    lines.append(f"=== ID {d['id']} | File: {d['event_file']} | Speaker: {d.get('speaker', 'Unknown')} (ID {d.get('speaker_id')}) ===")
    lines.append(f"JP: {d.get('original_jp', '')}")
    lines.append(f"EN: {d.get('original_en', '')}")
    lines.append(f"PT: {d.get('current_ptbr', '')}")
    lines.append("")

with open('Ferramentas_Traducao/curadoria_editorial/blk_evd_001_raw_dump.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Dumped {len(data['dialogues'])} dialogues successfully.")

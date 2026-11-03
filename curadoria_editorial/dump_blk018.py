import json

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_018_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\all_blk018_raw.txt", "w", encoding="utf-8") as out:
    for d in data["dialogues"]:
        out.write(f"ID: {d['id']} | Event: {d['event_file']} | Speaker: {d['speaker']} (ID: {d.get('speaker_id')})\n")
        out.write(f"JP: {d['original_jp']}\n")
        out.write(f"EN: {d['original_en']}\n")
        out.write(f"PT: {d['current_ptbr']}\n")
        out.write("-" * 80 + "\n")
print(f"Dumped {len(data['dialogues'])} dialogues.")

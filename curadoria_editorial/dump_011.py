import json

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blk011_raw_dump.txt"

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(output_path, "w", encoding="utf-8") as out:
    for d in data["dialogues"]:
        out.write(f"=== ID {d['id']} | {d['event_file']} | {d['speaker']} ===\n")
        out.write(f"JP: {d['original_jp']}\n")
        out.write(f"EN: {d['original_en']}\n")
        out.write(f"PT: {d['current_ptbr']}\n\n")

print(f"Dumped {len(data['dialogues'])} dialogues successfully.")

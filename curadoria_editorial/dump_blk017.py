import json

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_017_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\all_blk017_raw.txt"

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

lines = data if isinstance(data, list) else data.get("dialogues", data.get("lines", []))

with open(output_path, "w", encoding="utf-8") as out:
    for item in lines:
        out.write(f"=== ID {item['id']} | {item.get('event_file')} | {item.get('speaker')} ===\n")
        out.write(f"JP: {item.get('original_jp')}\n")
        out.write(f"EN: {item.get('original_en')}\n")
        out.write(f"PT: {item.get('current_ptbr')}\n\n")

print(f"Dumped {len(lines)} lines to {output_path}")

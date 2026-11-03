import json
import sys

path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_014_input.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

start_id = int(sys.argv[1]) if len(sys.argv) > 1 else 3464
end_id = int(sys.argv[2]) if len(sys.argv) > 2 else 3520

items = [d for d in data["dialogues"] if start_id <= d["id"] <= end_id]

out_txt = []
for d in items:
    out_txt.append(f"=== ID {d['id']} | {d['event_file']} | {d['speaker']} ===")
    out_txt.append(f"JP: {d['original_jp']}")
    out_txt.append(f"EN: {d['original_en']}")
    out_txt.append(f"PT: {d['current_ptbr']}")
    out_txt.append("")

output_file = f"dump_{start_id}_{end_id}.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(out_txt))

print(f"Dumped {len(items)} items to {output_file}")

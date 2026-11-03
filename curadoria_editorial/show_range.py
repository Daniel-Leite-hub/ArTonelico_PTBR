import sys
import json

start_id = int(sys.argv[1])
end_id = int(sys.argv[2])

p = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_013_input.json"
with open(p, "r", encoding="utf-8") as f:
    d = json.load(f)

for item in d["dialogues"]:
    if start_id <= item["id"] <= end_id:
        print(f"=== ID: {item['id']} | Event: {item['event_file']} | Speaker: {item['speaker']} ===")
        print("JP:", repr(item["original_jp"]))
        print("EN:", repr(item["original_en"]))
        print("PT:", repr(item["current_ptbr"]))
        print()

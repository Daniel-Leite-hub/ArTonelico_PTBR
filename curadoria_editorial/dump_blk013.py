import json

p = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_013_input.json"
out_p = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blk013_raw_dump.txt"

with open(p, "r", encoding="utf-8") as f:
    d = json.load(f)

with open(out_p, "w", encoding="utf-8") as out:
    for item in d["dialogues"]:
        out.write(f"=== ID: {item['id']} | Event: {item['event_file']} | Speaker: {item['speaker']} ===\n")
        out.write(f"JP: {repr(item['original_jp'])}\n")
        out.write(f"EN: {repr(item['original_en'])}\n")
        out.write(f"PT: {repr(item['current_ptbr'])}\n\n")

print(f"Dumped {len(d['dialogues'])} items to {out_p}")

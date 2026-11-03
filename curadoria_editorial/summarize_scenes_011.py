import json

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

current_file = None
file_info = []
cur = None

for d in data["dialogues"]:
    f = d["event_file"]
    if f != current_file:
        if cur:
            file_info.append(cur)
        current_file = f
        cur = {
            "file": f,
            "start_id": d["id"],
            "end_id": d["id"],
            "count": 0,
            "speakers": set(),
            "first_line_jp": d["original_jp"],
            "first_line_en": d["original_en"]
        }
    cur["end_id"] = d["id"]
    cur["count"] += 1
    cur["speakers"].add(d["speaker"])

if cur:
    file_info.append(cur)

print(f"Total scenes/files: {len(file_info)}")
for fi in file_info:
    spk = ", ".join(sorted(list(fi["speakers"])))
    print(f"File {fi['file']} (IDs {fi['start_id']}-{fi['end_id']}, {fi['count']} lines) | Speakers: {spk}")
    print(f"   First: JP: {fi['first_line_jp'][:60]} | EN: {fi['first_line_en'][:60]}")

import json

path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_014_input.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

dialogues = data["dialogues"]
print("Total:", len(dialogues))

scenes = []
current_scene = None
for d in dialogues:
    ef = d.get("event_file")
    if current_scene is None or current_scene["event_file"] != ef:
        if current_scene is not None:
            scenes.append(current_scene)
        current_scene = {"event_file": ef, "start_id": d["id"], "end_id": d["id"], "count": 1, "speakers": {d["speaker"]}}
    else:
        current_scene["end_id"] = d["id"]
        current_scene["count"] += 1
        current_scene["speakers"].add(d["speaker"])
if current_scene:
    scenes.append(current_scene)

cum = 0
for i, s in enumerate(scenes):
    cum += s["count"]
    print(f"Scene {i+1:02d}: {s['event_file']} (IDs {s['start_id']}-{s['end_id']}, {s['count']} lines, cum {cum}) - Speakers: {list(s['speakers'])}")

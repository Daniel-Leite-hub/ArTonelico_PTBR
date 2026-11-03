import json
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find topic boundaries (often short dialogue chunks or distinctive starts)
for i, d in enumerate(data["dialogues"]):
    # Print lines that look like topic titles or conversation starters
    en = d.get("original_en", "")
    jp = d.get("original_jp", "")
    did = d["id"]
    # Check if previous line ended or if this looks like a new topic
    if i == 0 or len(d.get("lead_in", [])) > 0:
        pass
    print(f"[{did}] {jp[:30]} | {en[:30]}")

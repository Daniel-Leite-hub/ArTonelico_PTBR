import json
from pathlib import Path

gloss_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")
output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_089_output.json")

with open(gloss_path, "r", encoding="utf-8") as f:
    gloss = json.load(f)

with open(output_path, "r", encoding="utf-8") as f:
    blk_out = json.load(f)

# Merge glossary additions
for k, v in blk_out.get("glossary_additions", {}).items():
    if k not in gloss.get("terms", {}):
        gloss["terms"][k] = v
        print(f"Added new term: {k}")
    else:
        print(f"Term already present: {k}")

# Update last_scene_handoff
gloss["last_scene_handoff"] = blk_out.get("scene_handoff", {})

with open(gloss_path, "w", encoding="utf-8") as f:
    json.dump(gloss, f, ensure_ascii=False, indent=2)

print("glossario_mestre.json successfully updated with BLK_EVD_089 terms and handoff.")

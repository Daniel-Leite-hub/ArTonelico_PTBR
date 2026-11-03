# -*- coding: utf-8 -*-
import json
from pathlib import Path

gloss_path = Path("Ferramentas_Traducao/curadoria_editorial/glossario_mestre.json")
with open(gloss_path, "r", encoding="utf-8") as f:
    gloss = json.load(f)

out_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_086_output.json")
with open(out_path, "r", encoding="utf-8") as f:
    blk = json.load(f)

# Archive previous last_scene_handoff to handoff_history if not already there
prev_handoff = gloss.get("last_scene_handoff")
if prev_handoff:
    if "handoff_history" not in gloss["metadata"]:
        gloss["metadata"]["handoff_history"] = []
    
    # Check if already present
    exists = any(
        h.get("last_line_id") == prev_handoff.get("last_line_id") and
        h.get("last_scene_id") == prev_handoff.get("last_scene_id")
        for h in gloss["metadata"]["handoff_history"]
    )
    if not exists:
        gloss["metadata"]["handoff_history"].append(prev_handoff)

# Set new last_scene_handoff
gloss["last_scene_handoff"] = blk["scene_handoff"]

# Add new terms
for term, tdata in blk["glossary_additions"].items():
    if term not in gloss["terms"]:
        gloss["terms"][term] = tdata
        print(f"Added new term to glossary: {term}")
    else:
        print(f"Term already in glossary, updating: {term}")
        gloss["terms"][term].update(tdata)

with open(gloss_path, "w", encoding="utf-8") as f:
    json.dump(gloss, f, ensure_ascii=False, indent=2)

print("Glossary successfully updated.")

# -*- coding: utf-8 -*-
import json
import glob

for f in sorted(glob.glob("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_07*_output.json")):
    with open(f, "r", encoding="utf-8") as jf:
        data = json.load(jf)
    for c in data.get("curated_lines", []):
        t = c.get("text", "")
        if "Magia" in t or "obteve" in t or "Receb" in t or "teceu" in t:
            print(f"[{data['block_id']}] ID {c['id']}: {t}")

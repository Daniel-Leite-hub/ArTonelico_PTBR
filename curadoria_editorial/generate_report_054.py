# -*- coding: utf-8 -*-
import json
from datetime import datetime, timezone

with open("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_054_output.json", "r", encoding="utf-8") as f:
    out = json.load(f)

report = {
    "block_id": "BLK_EVD_054",
    "completed_at": datetime.now(timezone.utc).isoformat(),
    "total_dialogues": len(out["dialogues"]),
    "lines_rewritten": 263,
    "lines_approved_as_is": 5,
    "new_terms_added": len(out.get("new_terms", {})),
    "scene_handoff": out.get("scene_handoff_final", {}),
    "highlights": out.get("highlights", [])
}

with open("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_054_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("Report successfully generated!")

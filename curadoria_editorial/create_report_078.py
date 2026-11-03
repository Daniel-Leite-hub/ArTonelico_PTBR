# -*- coding: utf-8 -*-
"""Cria o arquivo BLK_EVD_078_report.json."""

import json
from pathlib import Path
from datetime import datetime, timezone

output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_078_output.json")
with open(output_path, "r", encoding="utf-8") as f:
    out_data = json.load(f)

report_data = {
    "block_id": "BLK_EVD_078",
    "completed_at": datetime.now(timezone.utc).isoformat(),
    "backup_created": "G:\\JOGO\\PS2\\Ar tonelico - Melody of Elemia (Undub)\\Ferramentas_Traducao\\backups\\curadoria\\ArTonelico_backup_pre_BLK_EVD_078_20261101_195500.atproj",
    "total_dialogues": 234,
    "lines_rewritten": 234,
    "lines_approved_as_is": 0,
    "new_terms_added": 6,
    "scene_handoff": out_data["scene_handoff"],
    "highlights": []
}

report_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_078_report.json")
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print(f"Relatório salvo em {report_path}")

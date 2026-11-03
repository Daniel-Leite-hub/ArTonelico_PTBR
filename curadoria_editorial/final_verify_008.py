# -*- coding: utf-8 -*-
import json

output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_008_output.json"
with open(output_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Block ID:", data["block_id"])
print("Axis ID:", data["axis_id"])
print("Axis Name:", data["axis_name"])
print("Total lines:", data["total_lines"])
print("Rewritten:", data["lines_rewritten"])
print("Approved as is:", data["lines_approved_as_is"])
print("Curated lines count:", len(data["curated_lines"]))
print("Scene handoff keys:", list(data["scene_handoff"].keys()))

assert data["block_id"] == "BLK_EVD_008"
assert data["axis_id"] == "AXIS_3"
assert data["axis_name"] == "HISTÓRIA E EVENTOS"
assert data["total_lines"] == 227
assert len(data["curated_lines"]) == 227
assert data["lines_rewritten"] + data["lines_approved_as_is"] == 227

for idx, line in enumerate(data["curated_lines"]):
    assert isinstance(line["id"], int)
    assert isinstance(line["file"], str)
    assert isinstance(line["speaker"], str)
    assert isinstance(line["original_jp"], str)
    assert isinstance(line["original_en"], str)
    assert isinstance(line["texto_ptbr_anterior"], str)
    assert isinstance(line["texto_ptbr_curado"], str)
    assert line["status"] in ("rewritten", "approved_as_is")
    assert isinstance(line["justificativa"], str)
    assert len(line["texto_ptbr_curado"]) > 0
    assert len(line["justificativa"]) > 0

print("ALL FINAL ASSERTIONS PASSED PERFECTLY!")

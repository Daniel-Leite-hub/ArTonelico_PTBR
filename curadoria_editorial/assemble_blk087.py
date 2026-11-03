# -*- coding: utf-8 -*-
"""
assemble_blk087.py - Montagem e auto-validação de BLK_EVD_087_output.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Carregar input
input_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_087_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

dialogues_input = input_data["dialogues"]
print(f"Total lines in input: {len(dialogues_input)}")

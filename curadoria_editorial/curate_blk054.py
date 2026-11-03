# -*- coding: utf-8 -*-
"""
curate_blk054.py - Script de montagem e validação da curadoria editorial do BLK_EVD_054
"""
import sys
import json
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Carregar dados de entrada
input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_054_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_lines = {d["id"]: d for d in input_data["dialogues"]}
print(f"Total lines in input: {len(input_lines)}")

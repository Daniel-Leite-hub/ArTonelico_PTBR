# -*- coding: utf-8 -*-
"""
curate_blk075.py - Curadoria editorial completa e rigorosa para BLK_EVD_075
"""
import json
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Carrega arquivo de entrada
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_075_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

dialogues = input_data["dialogues"]
print(f"Loaded {len(dialogues)} dialogues from input.")

# -*- coding: utf-8 -*-
"""
build_and_validate_blk078.py
Gera e valida deterministamente o arquivo BLK_EVD_078_output.json
com os mais altos padrões de Curadoria Editorial e LQA para PT-BR.
"""

import sys
import os
import json
from pathlib import Path

# Adiciona o caminho dos scripts da skill
sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

print("Carregando BLK_EVD_078_input.json...")
input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_078_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

assert input_data["block_id"] == "BLK_EVD_078"
assert len(input_data["dialogues"]) == 234

print("Preparando mapeamento editorial para as 234 falas...")

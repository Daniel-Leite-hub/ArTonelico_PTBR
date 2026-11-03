# -*- coding: utf-8 -*-
"""
test_all_065.py - Rascunho e validação preliminar dos 182 diálogos do BLK_EVD_065
"""
import sys
import json
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_065_input.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

dialogues = input_data['dialogues']
print(f"Total dialogues in input: {len(dialogues)}")

print("Test complete setup.")

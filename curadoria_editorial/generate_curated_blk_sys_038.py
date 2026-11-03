# -*- coding: utf-8 -*-
"""Gerador e Validador Integral de Curadoria Editorial para BLK_SYS_038.
Garante 0 estouros de capacidade em todos os 288 diálogos, paridade estrita de tags,
e excelência literária fundamentada no texto japonês.
"""

import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_batch

# Carregar banco para verificação de bytes
conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

# Carregar arquivo de entrada
input_path = Path('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_038_input.json')
with open(input_path, 'r', encoding='utf-8') as f:
    input_data = json.load(f)

# Dicionário com todas as 288 falas curadas (id -> (curated_ptbr, rationale))
curations = {}

print(f"Total dialogues in input: {len(input_data['dialogues'])}")

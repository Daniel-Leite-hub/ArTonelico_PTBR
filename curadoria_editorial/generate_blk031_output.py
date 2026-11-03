# -*- coding: utf-8 -*-
"""Script gerador e validador da curadoria editorial do bloco BLK_EVD_031."""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

# Adiciona o diretório de ferramentas ao sys.path para importar o validador oficial
sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\tools")
from curadoria_validate import validate_line, validate_batch

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_031_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_031_output.json")
REPORT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_031_report.json")
GLOSSARY_PATH = Path("Ferramentas_Traducao/curadoria_editorial/glossario_mestre.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

raw_dialogues = input_data["dialogues"]
assert len(raw_dialogues) == 225, f"Esperado 225 falas, obtido {len(raw_dialogues)}"

# Rationales and curated map from our validated dataset
# (Imported or embedded)
with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    out_data = json.load(f)

is_valid, all_errors = validate_batch(out_data)
if is_valid:
    print(f"[OK] Bloco BLK_EVD_031 validado com sucesso! Total: {len(out_data['dialogues'])} falas.")
else:
    print(f"[FALHA] Bloco BLK_EVD_031 possui erros: {all_errors}")

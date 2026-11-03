# -*- coding: utf-8 -*-
"""Builder para BLK_EVD_051 de Ar tonelico: Melody of Elemia (Undub)
Gera BLK_EVD_051_output.json com todas as 222 falas lapidadas segundo a
skill curadoria-editorial-game-localization (v4.5.0).
"""

import json
from pathlib import Path

# Carregar input original para preservar metadados e IDs
input_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_051_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

print(f"Carregado {len(input_data['dialogues'])} dialogos de {input_path.name}")

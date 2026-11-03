import json
import re
import sys
from pathlib import Path

# Load input
with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_089_input.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

input_dialogues = input_data.get('dialogues', [])
print(f"Loaded {len(input_dialogues)} input dialogues.")

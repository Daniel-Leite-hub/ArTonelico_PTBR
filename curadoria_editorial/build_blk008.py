# Draft builder for BLK_EVD_008
# Let's inspect the exact lines and refine each one.
import json

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_008_input.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Loaded {len(data['dialogues'])} lines.")

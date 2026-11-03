import json
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

with open('Ferramentas_Traducao/curadoria_editorial/blocos/blk042_dump.json', encoding='utf-8') as f:
    lines = json.load(f)

print(f"Total lines: {len(lines)}")
overflows = [l for l in lines if l['diff'] > 0]
print(f"Overflowing lines: {len(overflows)}")

# Check for CR tags and newlines
cr_diffs = []
for l in lines:
    jp_cr = l['jp'].count('CR')
    en_cr = l['en'].count('CR')
    pt_cr = l['pt'].count('CR')
    if '\n' in l['jp'] or '\n' in l['en'] or '\n' in l['pt']:
        print(f"ID {l['id']} has newline")

print("Analysis of CR counts and differences done.")

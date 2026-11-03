import json
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

with open('Ferramentas_Traducao/curadoria_editorial/blocos/blk042_dump.json', encoding='utf-8') as f:
    lines = json.load(f)

def dump_file(file_name):
    print(f"==================== {file_name} ====================")
    file_lines = [l for l in lines if l['file'] == file_name]
    for l in file_lines:
        status = f"OVERFLOW +{l['diff']}B" if l['diff'] > 0 else f"OK ({l['diff']}B)"
        print(f"ID {l['id']} [{l['sz']}B / {l['cap']}B -> {status}]")
        print(f"  JP: {l['jp']}")
        print(f"  EN: {l['en']}")
        print(f"  PT: {l['pt']}")
        print("-" * 50)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "SLUS/TEXT/0517"
    dump_file(target)

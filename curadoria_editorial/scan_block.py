import json
import sys
sys.path.append(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao')
import artonelico_tool.project as proj

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\inspect_blk010.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def show_range(start_idx, end_idx):
    for it in items[start_idx:end_idx]:
        mark = " [OVERFLOW]" if it["overflow"] else ""
        print(f"{it['id']} ({it['orig_b']}B / cur={it['cur_size']}B){mark}:")
        print(f"  JP: {it['jp']}")
        print(f"  EN: {it['en']}")
        print(f"  PT: {it['pt']}")

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else len(items)
    show_range(start, end)

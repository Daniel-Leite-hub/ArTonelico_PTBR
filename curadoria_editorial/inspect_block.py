import json
import sys
sys.path.insert(0, r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

with open('all_blk_sys_007.json', 'r', encoding='utf-8') as f:
    lines = json.load(f)

def show_range(start_idx, end_idx):
    for l in lines[start_idx:end_idx]:
        lid = l['id']
        ob = l['ob']
        jp = l['jp']
        en = l['en']
        pt = l['rev'] if l['rev'] else l['auto']
        enc = encoded_size(pt) if pt else 0
        diff = enc - ob if enc is not None else 999
        status = f"OVERFLOW (+{diff}B)" if diff > 0 else f"OK ({enc}B <= {ob}B)"
        print(f"{lid} [{l['file']}] OB:{ob} | {status} | JP: {jp} | EN: {en} | PT: {pt}")

if __name__ == '__main__':
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else len(lines)
    show_range(start, end)

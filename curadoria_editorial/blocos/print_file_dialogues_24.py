import json
import sys

def print_file(target_file):
    with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_024_dump.json', 'r', encoding='utf-8') as f:
        dump = json.load(f)
    
    lines = [d for d in dump if d['file'] == f"SLUS/TEXT/{target_file}"]
    print(f"=== ARQUIVO {target_file} ({len(lines)} falas) ===")
    for d in lines:
        print(f"ID {d['id']} | Max: {d['max_bytes']}B | PT: {d['pt_bytes']}B | Over: {d['overflow']}")
        print(f"  JP: {d['jp']}")
        print(f"  EN: {d['en']}")
        print(f"  PT: {d['pt']}")
        print("-" * 60)

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '0283'
    print_file(target)

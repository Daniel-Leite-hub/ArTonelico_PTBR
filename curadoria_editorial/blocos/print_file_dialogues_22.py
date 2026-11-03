import json
import sys

def show_file(file_code):
    with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_022_dump.json', encoding='utf-8') as f:
        data = json.load(f)
    items = [x for x in data if file_code in x['file']]
    print(f"=== DETALHES DO ARQUIVO {file_code} ({len(items)} falas) ===")
    for x in items:
        status = "OK" if x['pt_bytes'] <= x['max_bytes'] else f"OVERFLOW (+{x['pt_bytes'] - x['max_bytes']})"
        print(f"ID {x['id']} | Max: {x['max_bytes']}B | Cur: {x['pt_bytes']}B | {status}")
        print(f"  JP: {x['jp']}")
        print(f"  EN: {x['en']}")
        print(f"  PT: {x['pt']}")
        print("-" * 60)

if __name__ == '__main__':
    fc = sys.argv[1] if len(sys.argv) > 1 else '0259'
    show_file(fc)

import json
import sys

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_021_dump.json', encoding='utf-8') as f:
    dump = json.load(f)

file_filter = sys.argv[1] if len(sys.argv) > 1 else '0247'
items = [x for x in dump if file_filter in x['file']]

print(f"=== {file_filter} ({len(items)} falas) ===")
for x in items:
    print(f"ID {x['id']} | Max: {x['max_bytes']}B | Cur: {x['pt_bytes']}B")
    print(f"  JP: {x['jp']}")
    print(f"  EN: {x['en']}")
    print(f"  PT: {x['pt']}")
    print("-" * 50)

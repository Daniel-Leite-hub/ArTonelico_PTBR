import json
import sys

file_to_show = sys.argv[1] if len(sys.argv) > 1 else "0271"

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_023_dump.json', encoding='utf-8') as f:
    dump = json.load(f)

for item in dump:
    if file_to_show in item['file']:
        over_str = f"OVERFLOW (+{item['diff']})" if item['overflow'] else "OK"
        print(f"ID {item['id']} [{item['pt_bytes']}B/{item['max_bytes']}B] {over_str}:")
        print(f"  JP: {item['jp']}")
        print(f"  EN: {item['en']}")
        print(f"  PT: {item['pt']}")
        print()

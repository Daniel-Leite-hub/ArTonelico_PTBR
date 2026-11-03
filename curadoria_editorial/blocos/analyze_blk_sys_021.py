import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_021_dump.json', encoding='utf-8') as f:
    dump = json.load(f)

overflows = [x for x in dump if x['pt_bytes'] > x['max_bytes']]
print(f'Total de falas: {len(dump)}')
print(f'Total de overflows atuais em current_ptbr: {len(overflows)}')
for x in overflows[:20]:
    print(f"ID {x['id']} ({x['file']}): {x['pt_bytes']}B > {x['max_bytes']}B (+{x['pt_bytes'] - x['max_bytes']})")
    print(f"  JP: {x['jp']}")
    print(f"  EN: {x['en']}")
    print(f"  PT: {x['pt']}")
    print()

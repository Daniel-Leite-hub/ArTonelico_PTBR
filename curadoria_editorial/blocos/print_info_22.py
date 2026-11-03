import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_021_output.json', encoding='utf-8') as f:
    d21 = json.load(f)

print("=== ÚLTIMAS 12 FALAS DO BLOCO BLK_SYS_021 (LEAD-IN) ===")
for x in d21['dialogues']:
    if x['id'] >= 26366:
        print(f"ID {x['id']}: JP: {x['original_jp']}")
        print(f"        EN: {x['original_en']}")
        print(f"        PT: {x['curated_ptbr']}")
        print("-" * 50)

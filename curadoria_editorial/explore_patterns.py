import json

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_SYS_009_output.json', 'r', encoding='utf-8') as f:
    d9 = json.load(f)

print("Sample equipment lines from BLK_SYS_009:")
for d in d9['dialogues']:
    if '【装備品用】' in d['original_jp']:
        print(f"{d['id']}: JP={d['original_jp']} -> PT={d['curated_ptbr']}")

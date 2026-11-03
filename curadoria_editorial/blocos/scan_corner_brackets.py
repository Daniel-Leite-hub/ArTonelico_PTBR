import json, re

data = json.load(open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_083_input.json', encoding='utf-8'))

for d in data['dialogues']:
    jp = d.get('original_jp', '')
    tags = re.findall(r'【.*?】', jp)
    if tags:
        print(f"ID {d['id']}: tags={tags} (JP: {jp})")

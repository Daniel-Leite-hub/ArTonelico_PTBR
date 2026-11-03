import json

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_030_input.json', encoding='utf-8'))
dialogues = {d['id']: d for d in data['dialogues']}

for d_id in range(7483, 7596):
    d = dialogues[d_id]
    spk = d.get('speaker')
    jp = d.get('original_jp', '')
    en = d.get('original_en', '')
    pt = d.get('current_ptbr', '')
    print(f"ID {d_id} ({spk}):")
    print(f"  JP: {jp}")
    print(f"  EN: {en}")
    print(f"  PT: {pt}")

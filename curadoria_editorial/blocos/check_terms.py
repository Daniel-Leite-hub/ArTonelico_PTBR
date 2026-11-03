import json

for fn in [
    r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_050_output.json',
    r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_076_output.json'
]:
    data = json.load(open(fn, encoding='utf-8'))
    print('===', fn, '===')
    lines = data.get('curated_lines') or data.get('dialogues', [])
    for d in lines:
        txt = d.get('ptbr_text') or d.get('text') or d.get('ptbr_curated') or d.get('curated_ptbr')
        notes = d.get('notes') or d.get('rationale')
        if any(w in str(d).lower() for w in ['tatoolist', 'taturista', '延命剤', 'prolongador']):
            print(f"ID {d.get('id')}: {txt}")
            print(f"  Notes: {notes}")

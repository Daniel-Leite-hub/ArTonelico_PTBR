import glob, json

for fn in sorted(glob.glob(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\*_output.json')):
    with open(fn, encoding='utf-8') as f:
        data = json.load(f)
    for d in data.get('curated_lines') or data.get('dialogues', []):
        orig = str(d.get('original_jp', ''))
        if '紡ぎ出した' in orig:
            txt = d.get('ptbr_text') or d.get('text') or d.get('ptbr_curated') or d.get('curated_ptbr')
            print(f"{d.get('id')}: {orig} -> {txt}")

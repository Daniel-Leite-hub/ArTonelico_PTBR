import json, glob

for fn in glob.glob(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\*_output.json'):
    with open(fn, encoding='utf-8') as f:
        content = f.read()
        if 'シルフ' in content or 'Sylph' in content or 'Silfa' in content:
            print(f"Match in {fn}")
            data = json.loads(content)
            for d in data.get('curated_lines') or data.get('dialogues', []):
                s = str(d)
                if 'シルフ' in s or 'sylph' in s.lower() or 'silfa' in s.lower():
                    print(f"  Line: {d.get('ptbr_text') or d.get('text')}")
                    print(f"  Notes: {d.get('notes')}")

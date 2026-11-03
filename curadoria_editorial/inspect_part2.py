import json

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_008_input.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = [d for d in data['dialogues'] if 1943 <= d['id'] <= 2009]
for l in lines:
    print(f"--- ID {l['id']} | {l['event_file']} | {l['speaker']} ---")
    print(f"JP:   {repr(l['original_jp'])}")
    print(f"EN:   {repr(l['original_en'])}")
    print(f"PTBR: {repr(l['current_ptbr'])}")

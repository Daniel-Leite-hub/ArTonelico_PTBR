import json

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_083_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\dump_blk_083.txt', 'w', encoding='utf-8') as out:
    for d in data['dialogues']:
        out.write(f"[{d['id']}] [{d.get('event_file')}] {d.get('speaker')} (id {d.get('speaker_id')}):\n")
        out.write(f"  JP: {d.get('original_jp')}\n")
        out.write(f"  EN: {d.get('original_en')}\n")
        out.write(f"  PT: {d.get('current_ptbr')}\n\n")

print(f"Dumped {len(data['dialogues'])} dialogues.")

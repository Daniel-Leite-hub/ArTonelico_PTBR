import json

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_015_input.json', encoding='utf-8') as f:
    d = json.load(f)

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\all_blk015_raw.txt', 'w', encoding='utf-8') as out:
    for item in d['dialogues']:
        out.write(f"ID: {item['id']} | Event: {item['event_file']} | Speaker: {item['speaker']} (ID {item.get('speaker_id')})\n")
        out.write(f"  JP: {item['original_jp']}\n")
        out.write(f"  EN: {item['original_en']}\n")
        out.write(f"  PT: {item['current_ptbr']}\n\n")

print(f"Dumped {len(d['dialogues'])} dialogues.")

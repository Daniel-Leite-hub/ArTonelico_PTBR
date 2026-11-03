import json

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_008_input.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = data['dialogues']
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blk008_raw_dump.txt", 'w', encoding='utf-8') as out:
    current_file = None
    for item in lines:
        if item['event_file'] != current_file:
            current_file = item['event_file']
            out.write(f"\n=======================================================\n")
            out.write(f"=== EVENT FILE: {current_file} ===\n")
            out.write(f"=======================================================\n\n")
        
        out.write(f"ID: {item['id']} | Speaker: {item['speaker']} (ID: {item.get('speaker_id')})\n")
        out.write(f"  JP:   {item['original_jp']}\n")
        out.write(f"  EN:   {item['original_en']}\n")
        out.write(f"  PTBR: {item['current_ptbr']}\n\n")

print(f"Dumped {len(lines)} lines successfully.")

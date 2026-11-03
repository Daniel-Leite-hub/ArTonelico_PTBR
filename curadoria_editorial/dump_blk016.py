import json

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_016_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

lines = d['dialogues']
with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\all_blk016_raw.txt', 'w', encoding='utf-8') as f_out:
    for l in lines:
        f_out.write(f"=== ID {l['id']} | {l['event_file']} | Speaker: {l['speaker']} ===\n")
        f_out.write(f"JP: {l['original_jp']}\n")
        f_out.write(f"EN: {l['original_en']}\n")
        f_out.write(f"PT: {l['current_ptbr']}\n\n")

print(f"Dumped {len(lines)} lines to all_blk016_raw.txt")

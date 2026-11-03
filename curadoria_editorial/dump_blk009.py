import json

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_009_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blk009_raw_dump.txt', 'w', encoding='utf-8') as out:
    for x in d['dialogues']:
        line_id = x['id']
        efile = x['event_file']
        spk = x['speaker']
        jp = x['original_jp']
        en = x['original_en']
        pt = x['current_ptbr']
        out.write(f"=== ID {line_id} | {efile} | {spk} ===\nJP: {jp}\nEN: {en}\nPT: {pt}\n\n")

print("Dumped 224 lines successfully!")

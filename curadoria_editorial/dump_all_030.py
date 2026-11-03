import json

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_030_input.json', encoding='utf-8'))
dialogues = data['dialogues']

with open('Ferramentas_Traducao/curadoria_editorial/blk030_full_dump.txt', 'w', encoding='utf-8') as out:
    for i, d in enumerate(dialogues):
        d_id = d['id']
        ev = d.get('event_file')
        spk = d.get('speaker')
        jp = d.get('original_jp', '')
        en = d.get('original_en', '')
        pt = d.get('current_ptbr', '')
        out.write(f"=== [{i}] ID: {d_id} | Ev: {ev} | Spk: {spk} ===\n")
        out.write(f"JP: {jp}\n")
        out.write(f"EN: {en}\n")
        out.write(f"PT: {pt}\n\n")

print(f"Dumped {len(dialogues)} dialogues to blk030_full_dump.txt")

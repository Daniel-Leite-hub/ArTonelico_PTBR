# -*- coding: utf-8 -*-
import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_043_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

dialogues = data['dialogues']

with open('Ferramentas_Traducao/curadoria_editorial/blk043_full_dump.txt', 'w', encoding='utf-8') as out:
    for idx, d in enumerate(dialogues):
        lid = d['id']
        spk = d.get('speaker', '')
        spk_id = d.get('speaker_id', '')
        ev = d.get('event_file', '')
        jp = d.get('original_jp', '')
        en = d.get('original_en', '')
        pt = d.get('current_ptbr', '')
        out.write(f"=== [{idx}] ID: {lid} | Event: {ev} | Speaker: {spk} ({spk_id}) ===\n")
        out.write(f"JP: {jp}\n")
        out.write(f"EN: {en}\n")
        out.write(f"PT: {pt}\n\n")

print(f"Dumped {len(dialogues)} dialogues to blk043_full_dump.txt")

# -*- coding: utf-8 -*-
import json

with open("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_062_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("Ferramentas_Traducao/curadoria_editorial/inspect_blk062_utf8.txt", "w", encoding="utf-8") as out:
    for ef in ['Event/703.evd', 'Event/640.evd', 'Event/238.evd', 'Event/538.evd']:
        lines = [d for d in data['dialogues'] if d['event_file'] == ef]
        out.write(f"\n==================== {ef} ({len(lines)} lines) ====================\n")
        for d in lines:
            jp = repr(d['original_jp'])
            en = repr(d['original_en'])
            pt = repr(d.get('current_ptbr', ''))
            spk = d['speaker']
            out.write(f"[{d['id']}] {spk} ({d.get('speaker_id')}):\n")
            out.write(f"  JP: {jp}\n")
            out.write(f"  EN: {en}\n")
            out.write(f"  PT: {pt}\n")

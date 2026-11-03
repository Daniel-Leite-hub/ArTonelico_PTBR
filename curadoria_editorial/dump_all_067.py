import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_067_input.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for ev in ['Event/118.evd', 'Event/294.evd', 'Event/642.evd']:
    lines = [x for x in d['dialogues'] if x['event_file'] == ev]
    out_file = f"Ferramentas_Traducao/curadoria_editorial/dump_{ev.replace('/', '_').replace('.evd', '')}.txt"
    with open(out_file, 'w', encoding='utf-8') as out:
        out.write(f"=== {ev} (Total: {len(lines)}) ===\n\n")
        for x in lines:
            out.write(f"ID: {x['id']} | Speaker: {x['speaker']} (ID: {x['speaker_id']})\n")
            out.write(f"JP: {x['original_jp']}\n")
            out.write(f"EN: {x['original_en']}\n")
            out.write(f"PT (current): {x['current_ptbr']}\n")
            out.write("-" * 60 + "\n")
    print(f"Wrote {out_file} with {len(lines)} lines")

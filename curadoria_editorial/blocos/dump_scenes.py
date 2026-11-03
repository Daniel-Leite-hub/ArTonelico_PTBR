import json

data = json.load(open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_083_input.json', encoding='utf-8'))

for ev, fname in [
    ('Event/323.evd', 'scene1_323.txt'),
    ('Event/598.evd', 'scene2_598.txt'),
    ('Event/953.evd', 'scene3_953.txt'),
    ('Event/766.evd', 'scene4_766.txt'),
]:
    dl = [d for d in data['dialogues'] if d.get('event_file') == ev]
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(f"=== {ev} ({len(dl)} lines, IDs {dl[0]['id']} - {dl[-1]['id']}) ===\n\n")
        for d in dl:
            f.write(f"[{d['id']}] {d.get('speaker')} (id {d.get('speaker_id')}):\n")
            f.write(f"  JP: {repr(d.get('original_jp'))}\n")
            f.write(f"  EN: {repr(d.get('original_en'))}\n")
            f.write(f"  PT: {repr(d.get('current_ptbr'))}\n\n")
    print(f"Wrote {fname}")

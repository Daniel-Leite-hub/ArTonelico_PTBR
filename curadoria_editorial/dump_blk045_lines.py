import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_045_input.json', encoding='utf-8') as f:
    data = json.load(f)

dialogues = data['dialogues']

with open('Ferramentas_Traducao/curadoria_editorial/blk045_summary_utf8.txt', 'w', encoding='utf-8') as out:
    out.write(f"Total lines: {len(dialogues)}\n")
    for idx, d in enumerate(dialogues):
        spk = d.get('speaker', '')
        jp = d.get('original_jp', '').replace('\n', '\\n')
        en = d.get('original_en', '').replace('\n', '\\n')
        pt = d.get('current_ptbr', '').replace('\n', '\\n')
        out.write(f"[{idx:03d}|ID {d['id']}] {spk}:\n  JP: {jp}\n  EN: {en}\n  PT: {pt}\n")

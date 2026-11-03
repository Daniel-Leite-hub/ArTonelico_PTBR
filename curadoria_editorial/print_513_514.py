import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_041_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def print_file(fn_idx):
    fn = f"SLUS/TEXT/0{fn_idx}"
    lines = [d for d in data['dialogues'] if d.get('event_file') == fn]
    print(f"\n==================== {fn} ({len(lines)} lines: {lines[0]['id']}..{lines[-1]['id']}) ====================")
    for d in lines:
        print(f"[{d['id']}] JP: {d['original_jp']}")
        print(f"       EN: {d['original_en']}")

print_file(513)
print_file(514)

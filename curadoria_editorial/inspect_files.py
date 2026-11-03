import json

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_041_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i in range(0, 288, 24):
    chunk = data['dialogues'][i:i+24]
    fn = chunk[0]['event_file']
    start_id = chunk[0]['id']
    end_id = chunk[-1]['id']
    print(f'=== FILE {fn} (IDs {start_id}..{end_id}) ===')
    for d in chunk[:4]:
        print(f"  [{d['id']}] JP: {d['original_jp']}")
        print(f"        EN: {d['original_en']}")

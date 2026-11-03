import json

data = json.load(open('Ferramentas_Traducao/curadoria_editorial/all_288_raw.json', encoding='utf-8'))
id_map = {d['id']: d for d in data}

print("=== SLICE 27978 - 27988 ===")
for i in range(27978, 27989):
    d = id_map[i]
    print(f"[{d['id']}] max={d['original_bytes']}B | JP: {d['original_jp']} | EN: {d['original_en']}")

print("\n=== SLICE 28025 - 28040 ===")
for i in range(28025, 28041):
    d = id_map[i]
    print(f"[{d['id']}] max={d['original_bytes']}B | JP: {d['original_jp']} | EN: {d['original_en']}")

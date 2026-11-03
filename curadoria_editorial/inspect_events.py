import json

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_018_input.json", "r", encoding="utf-8") as f:
    d = json.load(f)

dialogues = d["dialogues"]

def print_range(start_id, end_id):
    for item in dialogues:
        if start_id <= item["id"] <= end_id:
            print(f"[{item['id']}] {item['event_file']} | {item['speaker']} (spk_id: {item.get('speaker_id')})")
            print(f"  JP: {item['original_jp']}")
            print(f"  EN: {item['original_en']}")
            print(f"  PT: {item['current_ptbr']}")
            print()

if __name__ == "__main__":
    import sys
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 4511
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 4540
    print_range(start, end)

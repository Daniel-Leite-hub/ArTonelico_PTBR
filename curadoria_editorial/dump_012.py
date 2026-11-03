import json

inp_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_012_input.json"
out_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blk012_raw_dump.txt"

with open(inp_path, "r", encoding="utf-8") as f:
    inp = json.load(f)

with open(out_path, "w", encoding="utf-8") as f:
    f.write(f"BLOCK: {inp.get('block_id')} | TOTAL: {len(inp.get('dialogues', []))}\n")
    f.write(f"ID RANGE: {inp.get('id_range')}\n\n")
    
    current_event = None
    for d in inp.get("dialogues", []):
        ev = d.get("event_file", "UNKNOWN")
        if ev != current_event:
            current_event = ev
            f.write(f"\n####################################################################\n")
            f.write(f"### EVENT FILE: {current_event}\n")
            f.write(f"####################################################################\n\n")
            
        f.write(f"--- ID: {d['id']} | Speaker: {d.get('speaker', 'None')} ---\n")
        f.write(f"JP: {d.get('original_jp', '')}\n")
        f.write(f"EN: {d.get('original_en', '')}\n")
        f.write(f"PT: {d.get('current_ptbr', '')}\n\n")

print("Dumped 012 raw successfully.")

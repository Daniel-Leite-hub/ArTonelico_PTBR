import json
import sys

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_006_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1296
end_id = int(sys.argv[2]) if len(sys.argv) > 2 else 1359

for d in data['dialogues']:
    if start_id <= d['id'] <= end_id:
        print(f"[{d['id']}] {d['event_file']} | {d.get('speaker', 'None')} (id:{d.get('speaker_id')})")
        print(f"  JP: {repr(d.get('original_jp'))}")
        print(f"  EN: {repr(d.get('original_en'))}")
        print(f"  PT: {repr(d.get('current_ptbr'))}")
        print("-" * 60)

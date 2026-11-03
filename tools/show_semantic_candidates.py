from pathlib import Path
import json,sys,re
sys.stdout.reconfigure(encoding='utf8')
d=json.loads((Path(__file__).resolve().parents[1]/'work/curadoria_20261001/semantic_triage.json').read_text(encoding='utf8'))
for key in sys.argv[1:] or ('negative_missing',):
    print('###',key)
    for r in d[key]:
        if key=='negative_missing' and re.search(r'\b(?:No\.\d|No more|No matter|long time no see|never mind|can.t wait|Why don.t|don.t know|don.t care|don.t mind)\b',r['original'],re.I):continue
        print(r['id'],repr(r['original']),' => ',repr(r['automatic']))

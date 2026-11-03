from pathlib import Path
import re,sqlite3,sys,collections,json
sys.stdout.reconfigure(encoding='utf8')
root=Path(__file__).resolve().parents[1]
db=sqlite3.connect(root/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj');db.row_factory=sqlite3.Row
rows=db.execute("SELECT id,event_file,entry_index,speaker_id,original,automatic,translation_track FROM dialogues WHERE locked=0 AND length(trim(automatic))>0 ORDER BY id").fetchall()
tests={
'negative_missing':lambda o,a:bool(re.search(r"\b(?:not|never|no|neither|nobody|nothing|without|don.t|doesn.t|didn.t|isn.t|aren.t|wasn.t|weren.t|can.t|couldn.t|won.t|wouldn.t|shouldn.t|haven.t|hasn.t|hadn.t)\b",o,re.I)) and not bool(re.search(r'\b(?:não|nem|nunca|jamais|ninguém|nada|sem|nenhum[ao]?|impossível|incapaz|proibido|falta|faltam|deixou de|longe de|sequer|recus[ao]|evit[ao])\b',a,re.I)),
'negative_added':lambda o,a:not bool(re.search(r"\b(?:not|never|no|neither|nobody|nothing|without|don.t|doesn.t|didn.t|isn.t|aren.t|wasn.t|weren.t|can.t|couldn.t|won.t|wouldn.t|shouldn.t|haven.t|hasn.t|hadn.t)\b",o,re.I)) and bool(re.search(r'\b(?:não|nem|nunca|jamais|ninguém|nada|sem)\b',a,re.I)),
'future_mismatch':lambda o,a:bool(re.search(r"\b(?:will|gonna|going to)\b",o,re.I)) and not bool(re.search(r'\b(?:vai|vão|irei|iremos|irá|terá|será|estará|fará|deverá|poderá|haverá|pretend[oe]|planej[ao]|quer[oe]|vou|vamos|logo|amanhã|depois|futuro)\b|\b\w+(?:rá|rão|rei|remos)\b',a,re.I)),
'strange_mixed':lambda o,a:bool(re.search(r'\b(?:você\s+(?:eu|ele|ela)|eu\s+você|de\s+de|para\s+para|com\s+com|que\s+que|o\s+o|a\s+a)\b',a,re.I)),
'literal':lambda o,a:bool(re.search(r'\b(?:fazer sentido|tomar lugar|ter um bom tempo|no fim do dia|dar-lhe|isso é porque|o que é que|no entanto|de qualquer maneira|em primeiro lugar)\b',a,re.I)),
'placeholder':lambda o,a:bool(re.search(r'(?:\bCR(?=[A-ZÁÉÍÓÚN])|[\ufffd]|\?\w+\?)',a)),
}
report={k:[] for k in tests}
for r in rows:
    for key,fn in tests.items():
        if fn(r['original'],r['automatic']):report[key].append(dict(r))
out=root/'work/curadoria_20261001';out.mkdir(exist_ok=True)
(out/'semantic_triage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
for key,items in report.items():
    print('\n###',key,len(items))
    for x in items[:28]:print(x['id'],repr(x['original'][:105]),'=>',repr(x['automatic'][:125]))

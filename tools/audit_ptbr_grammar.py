"""Read-only triage of high-risk automatic PT-BR text."""
from pathlib import Path
import collections,json,re,sqlite3,sys
sys.stdout.reconfigure(encoding='utf8')
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
PATTERNS={
    'duplicate_pronoun':r'\b(?:you|I|he|she|we|they)\s*[,;:]\s*(?:você|eu|ele|ela|nós|eles|elas)\b',
    'english_leftover':r'\b(?:the|you|your|with|what|would|could|should|have|there|this|that|please|from|about|because|already)\b',
    'word_glue':r'[a-záàâãéêíóôõúç][A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][a-záàâãéêíóôõúç]',
    'repeated_word':r'\b([A-Za-zÀ-ÿ]{3,})\s+\1\b',
    'double_negation':r'\bnão\s+não\b',
    'spacing':r'\s{2,}|\s+[,;:!?]|[,;:!?](?![\s\n\r]|$)',
    'question_mismatch':r'(?!)',
}
db=sqlite3.connect(DB);db.row_factory=sqlite3.Row
rows=db.execute("SELECT id,event_file,entry_index,original,automatic,reviewed,review_status,translation_track FROM dialogues WHERE locked=0 AND length(trim(automatic))>0").fetchall()
report={k:[] for k in PATTERNS}
report['question_mismatch']=[]
for row in rows:
    a=row['automatic'];o=row['original']
    for key,pat in PATTERNS.items():
        if key=='question_mismatch':flag=('?' in o) != ('?' in a)
        else:flag=bool(re.search(pat,a,0 if key=='word_glue' else re.IGNORECASE))
        if flag:report[key].append({k:row[k] for k in row.keys()})
OUT=ROOT/'work/curadoria_20261001';OUT.mkdir(exist_ok=True)
(OUT/'audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('total',len(rows))
for key,items in report.items():
    print('\n',key,len(items))
    for item in items[:18]:print(item['id'],item['event_file'],repr(item['original'][:90]),' => ',repr(item['automatic'][:110]))

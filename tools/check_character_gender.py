import sqlite3,re,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf8')
db=sqlite3.connect(Path(__file__).resolve().parents[1]/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
for name in ('Mir','Claire','Krusche','Leila','Mei Mei','Tastiella','Eizel','Misha','Aurica','Shurelia'):
    pattern=r'\b(?:o|do|no|ao|pelo|um|esse|aquele|ele|dele|meu)\s+'+re.escape(name)+r'\b'
    found=[]
    for id,original,automatic in db.execute('SELECT id,original,automatic FROM dialogues WHERE length(trim(automatic))>0'):
        if re.search(pattern,automatic,re.I):found.append((id,original,automatic))
    print('\n',name,len(found))
    for row in found[:12]:print(row)

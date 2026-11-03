from pathlib import Path
import sqlite3,re,sys,collections
sys.stdout.reconfigure(encoding='utf8')
db=sqlite3.connect(Path(__file__).resolve().parents[1]/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj');db.row_factory=sqlite3.Row
rows=db.execute("SELECT id,event_file,entry_index,speaker_id,original,automatic FROM dialogues WHERE locked=0 AND length(trim(automatic))>0").fetchall()
tests={
'misha_gender':r'\b(?:o|um|do|no|ao|pelo|esse|aquele|ele|dele|seu)\s+Misha\b|\bMisha\s+(?:está|ficou|era|foi|é|parece|parecia)\s+(?:cansado|pronto|sozinho|assustado|feliz|preocupado|morto|vivo|certo|bom|melhor|maluco|ferido|perdido|louco|bobo|ocupado|estranho)\b',
'aurica_gender':r'\b(?:o|um|do|no|ao|pelo|esse|aquele|ele|dele|seu)\s+Aurica\b',
'shurelia_gender':r'\b(?:o|um|do|no|ao|pelo|esse|aquele|ele|dele|seu)\s+Shurelia\b',
'lyner_gender':r'\b(?:a|uma|da|na|pela|essa|aquela|ela|dela|sua)\s+Lyner\b',
'double_article':r'\b(?:o|a)\s+(?:o|a)\s+\w+|\b(?:um|uma)\s+(?:um|uma)\s+\w+',
'unsound':r'\b(?:eu estou|você está|ele está|ela está|nós estamos|vocês estão|eles estão)\s+indo\s+a\s+\w+|\b(?:tomar uma decisão|fazer uma decisão|realizar um erro|dar uma olhada em você|deixar você saber)\b',
'cosmosphere':r'\bCosmosphere\b',
'hymmnos':r'\b(?:Hymn Crystal|Reyvateil|Hymmnos|Virus)\b',
'duplicate_tag':r'CR[A-ZÁÉÍÓÚ][a-záéíóú]',
}
for name,pat in tests.items():
    found=[r for r in rows if re.search(pat,r['automatic'],re.I)]
    print('\n###',name,len(found))
    for r in found[:55]:print(r['id'],repr(r['original'][:105]),'=>',repr(r['automatic'][:130]))

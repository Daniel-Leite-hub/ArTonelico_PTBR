"""Apply explicit editorial translations by stable original-text snapshot."""
from pathlib import Path
import sys,json,sqlite3,hashlib,re
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.project import connect,backup_project,encoded_size
from artonelico_tool.manual_effects import effect_translation
ROOT=Path(__file__).resolve().parents[1]
SNAPSHOT=ROOT/'work/manual_pending_snapshot.json'

def main():
    if not SNAPSHOT.exists():
        db=connect(ROOT/'release/ArTonelico_PTBR.atproj')
        texts=[r[0] for r in db.execute("SELECT DISTINCT original FROM dialogues WHERE translation_track='localization' AND locked=0 AND automatic='' AND translation='' ORDER BY id")]
        SNAPSHOT.write_text(json.dumps(texts,ensure_ascii=False,indent=2),encoding='utf-8'); db.close()
    texts=json.loads(SNAPSHOT.read_text(encoding='utf-8'))
    targets={}
    for path in sorted((ROOT/'localization_manual').glob('*.txt')):
        for line in path.read_text(encoding='utf-8').splitlines():
            if not line or line.startswith('#'): continue
            key,target=line.split('|',1); index=int(key)
            if index in targets: raise ValueError(f'Duplicate {index}')
            if not target.strip() or encoded_size(target) is None: raise ValueError(f'Invalid {index}')
            targets[index]=target
    for index,source in enumerate(texts):
        if index not in targets:
            target=effect_translation(source)
            if target is not None: targets[index]=target
    references={
        'Firefly Alley':'Beco Firefly','Silver Horn':'Chifre de Prata',
        'Sharing Core':'Núcleo Compartilhado','Flipper':'Nadadeira',
        'Teletransportador Circula':'Teleporte Circula','Calor da Vida':'Calor Vital',
        'Bola de Energia':'Orbe de Energia','Estrondo do Trovão':'Trovoada',
        '[Conexão com a Torre]':'[Conexão da Torre]',
        '[Magia de Canção] Corte de Espada':'[Magia de Canção] Golpe de Espada',
        '[Magia de Canção] Deus das Lágrimas':'[Magia de Canção] Lágrima Divina',
    }
    for index,target in list(targets.items()):
        for source,replacement in references.items(): target=target.replace(source,replacement)
        targets[index]=target
        tokens=re.compile(r'IM[0-9]{2}|CR|%[a-zA-Z]|#[01][A-Za-z0-9_./-]*')
        if tokens.findall(texts[index]) != tokens.findall(target):
            raise ValueError(f'Control mismatch {index}')
        if encoded_size(target) is None: raise ValueError(f'Unsupported character {index}')
    if len(targets)!=len(texts): raise ValueError('Incomplete editorial mapping')
    report=[]
    for path in (ROOT/'ArTonelico_PTBR.atproj',ROOT/'release/ArTonelico_PTBR.atproj'):
        db=connect(path); backup=backup_project(db,path,'antes_curadoria_pendentes_20260926')
        changed=oversized=0
        eligible={}
        for row in db.execute("SELECT id,original,original_bytes FROM dialogues WHERE translation_track='localization' AND locked=0 AND reviewed='' AND ((automatic='' AND translation='') OR (provider='curadoria_contextual_ptbr' AND automatic=translation))"):
            eligible.setdefault(row['original'],[]).append(row)
        for index,target in targets.items():
            original=texts[index]; size=encoded_size(target)
            rows=eligible.get(original,[])
            for row in rows:
                fits=int(size<=row['original_bytes'])
                db.execute("UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=?,provider='curadoria_contextual_ptbr',error='' WHERE id=?",(target,target,size,fits,row['id']))
                changed+=1; oversized+=1-fits
        db.commit()
        pending=db.execute("SELECT COUNT(*) FROM dialogues WHERE translation_track='localization' AND locked=0 AND automatic='' AND translation='' AND reviewed=''").fetchone()[0]
        print(path.name,changed,oversized,pending,backup.name); db.close()
        report.append({'project':str(path),'localized':changed,'over_conservative_capacity':oversized,'pending':pending,'backup':str(backup)})
    (ROOT/'work/manual_localization_report.json').write_text(json.dumps({'unique_sources':len(texts),'projects':report},ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__': main()

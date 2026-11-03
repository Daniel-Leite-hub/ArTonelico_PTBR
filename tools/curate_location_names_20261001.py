"""Unify Firefly Alley across text tracks without changing unrelated names."""
from pathlib import Path
import json,re,sqlite3,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.project import encoded_size
from artonelico_tool.quality import GAME_COMMAND_PATTERN
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
BACKUP=ROOT/'release/backups/ArTonelico_PTBR_antes_localidades_20261001.atproj'
OUT=ROOT/'work/curadoria_20261001';OUT.mkdir(exist_ok=True)
ALIASES=(
 'Beco dos Vaga-lumes','Beco das Vaga-lumes','Beco do Vaga-lume','Beco do Vaga-Lume',
 'Beco da Luz-de-fogo','Beco do Pirilampo','Beco do Luciolinho','Beco Firefly',
 'Rua dos Vaga-lumes','Firefly Alley',
)
MANUAL={
 804:'Tenho uma amiga chamada [Eizel] na academia. Quero que você pergunte a ela por que não consigo criar um Meteoro.',
 6452:'Não. Estou procurando Eizel...',
 11165:'Ha... ha...CRReceio que não.',
 16943:'Volto para o Beco Vagalume. Aprendi muito sobre dirigíveis.',
}
def improve(value):
    for alias in ALIASES:
        value=re.sub(re.escape(alias), 'Beco Vagalume', value, flags=re.I)
    for before,after in (
      ('de Beco Vagalume','do Beco Vagalume'),('em Beco Vagalume','no Beco Vagalume'),
      ('da Beco Vagalume','do Beco Vagalume'),('na Beco Vagalume','no Beco Vagalume'),
      ('à Beco Vagalume','ao Beco Vagalume'),('a Beco Vagalume','ao Beco Vagalume'),
      ('para Beco Vagalume','para o Beco Vagalume'),
      ('o Firefly Alley','o Beco Vagalume'),
    ):
        value=re.sub(r'(?<!\w)'+re.escape(before)+r'(?!\w)',after,value)
    return value
def main():
    db=sqlite3.connect(DB);db.row_factory=sqlite3.Row
    changes=[]
    for row in db.execute("SELECT id,event_file,entry_index,original,automatic,translation,reviewed,original_bytes FROM dialogues WHERE locked=0 AND length(trim(automatic))>0"):
        if row['reviewed'].strip():continue
        if row['id'] not in MANUAL and 'Firefly Alley' not in row['original']:continue
        after=MANUAL.get(row['id'],improve(row['automatic']))
        if after==row['automatic']:continue
        if GAME_COMMAND_PATTERN.findall(after)!=GAME_COMMAND_PATTERN.findall(row['automatic']):raise ValueError(row['id'])
        if row['automatic'].count('CR')!=after.count('CR'):raise ValueError(row['id'])
        size=encoded_size(after)
        if size is None:raise ValueError(row['id'])
        changes.append({'id':row['id'],'original':row['original'],'before':row['automatic'],'after':after,
          'original_bytes':row['original_bytes'],'before_bytes':encoded_size(row['automatic']),
          'after_bytes':size,'translation_matched':row['translation']==row['automatic']})
    print('changes',len(changes),'capacity_crossings',sum(c['before_bytes']<=c['original_bytes']<c['after_bytes'] for c in changes))
    for c in changes:print(c['id'],repr(c['before']),'→',repr(c['after']))
    if '--apply' not in sys.argv:return
    if BACKUP.exists():raise FileExistsError(BACKUP)
    with sqlite3.connect(BACKUP) as dst:db.backup(dst)
    try:
        db.execute('BEGIN')
        for c in changes:
            if c['translation_matched']:
                db.execute('UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=? WHERE id=? AND automatic=? AND translation=?',
                  (c['after'],c['after'],c['after_bytes'],int(c['after_bytes']<=c['original_bytes']),c['id'],c['before'],c['before']))
            else:
                db.execute('UPDATE dialogues SET automatic=? WHERE id=? AND automatic=?',(c['after'],c['id'],c['before']))
            if db.execute('SELECT changes()').fetchone()[0]!=1:raise RuntimeError(c['id'])
        db.commit()
    except:db.rollback();raise
    (OUT/'location_names_applied.json').write_text(json.dumps({'backup':str(BACKUP),'changes':changes},ensure_ascii=False,indent=2),encoding='utf8')
if __name__=='__main__':main()

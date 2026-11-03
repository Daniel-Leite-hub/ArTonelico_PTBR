"""Second documented pass: character gender confirmed by nearby original dialogue."""
from pathlib import Path
import json,re,sqlite3,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.project import encoded_size
from artonelico_tool.quality import GAME_COMMAND_PATTERN
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
BACKUP=ROOT/'release/backups/ArTonelico_PTBR_antes_genero_personagens_20261001.atproj'
OUT=ROOT/'work/curadoria_20261001';OUT.mkdir(exist_ok=True)
MANUAL={
 10642:'Mas farei tudo ao meu alcance para ajudar vocês a deter Bourd e Mir, seja lá quem ela for.',
 10676:'Eu... o Crescent Chronicle foi feito para servir de caixão à Mir selada.',
 10727:'Então, Misha... você está mesmo pronta para cantar?',
 18022:'Misha... você está pronta?',
 9791:'Ah... então Mir ainda está viva? Não esperava por isso.',
 10662:'Vou ser direto com você. Mir ainda está viva.',
 10859:'Talvez você não saiba, mas Mir ainda está viva!',
 10875:'Para manter Mir selada, você precisa dormir...',
 12116:'Sim, ela sacrificou a vida quando Mir foi selada.',
 12141:'Sim, ela sacrificou a vida quando Mir foi selada.',
 16837:'Mir está selada... mais uma vez.',
 16850:'Mir foi selada mais uma vez.',
 17957:'Meu único objetivo é manter Mir selada para sempre.',
  19270:'Meu único objetivo é manter Mir selada para sempre.',
 19277:'Preciso te contar sobre a Mir, que foi ativada recentemente.',
}
def improve(value):
    for name in ('Mir','Krusche','Eizel','Misha'):
        for before,after in (
          ('do ','da '),('no ','na '),('ao ','à '),('pelo ','pela '),
          ('um ','uma '),('o ','a '),('esse ','essa '),('aquele ','aquela '),
          ('O ','A '),('Do ','Da '),('No ','Na '),('Ao ','À '),
        ):
            value=re.sub(r'(?<!\w)'+re.escape(before+name)+r'(?!\w)',after+name,value)
    return value
def main():
    db=sqlite3.connect(DB);db.row_factory=sqlite3.Row
    changes=[]
    for row in db.execute("SELECT id,event_file,entry_index,original,automatic,translation,reviewed,original_bytes FROM dialogues WHERE locked=0 AND length(trim(automatic))>0"):
        if row['reviewed'].strip():continue
        after=MANUAL.get(row['id'],improve(row['automatic']))
        if after==row['automatic']:continue
        if GAME_COMMAND_PATTERN.findall(after)!=GAME_COMMAND_PATTERN.findall(row['automatic']):raise ValueError(row['id'])
        if row['automatic'].count('CR')!=after.count('CR'):raise ValueError(row['id'])
        size=encoded_size(after)
        if size is None:raise ValueError(row['id'])
        changes.append({'id':row['id'],'event_file':row['event_file'],'original':row['original'],
          'before':row['automatic'],'after':after,'before_bytes':encoded_size(row['automatic']),
          'after_bytes':size,'original_bytes':row['original_bytes'],'translation_matched':row['automatic']==row['translation']})
    print('candidate changes',len(changes),'capacity_crossings',sum(x['before_bytes']<=x['original_bytes']<x['after_bytes'] for x in changes))
    for item in changes:print(item['id'],repr(item['before']),'→',repr(item['after']))
    if '--apply' not in sys.argv:return
    if BACKUP.exists():raise FileExistsError(BACKUP)
    with sqlite3.connect(BACKUP) as target:db.backup(target)
    try:
        db.execute('BEGIN')
        for item in changes:
            if item['translation_matched']:
                db.execute('UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=? WHERE id=? AND automatic=? AND translation=?',
                  (item['after'],item['after'],item['after_bytes'],int(item['after_bytes']<=item['original_bytes']),item['id'],item['before'],item['before']))
            else:
                db.execute('UPDATE dialogues SET automatic=? WHERE id=? AND automatic=?',(item['after'],item['id'],item['before']))
            if db.execute('SELECT changes()').fetchone()[0]!=1:raise RuntimeError(item['id'])
        db.commit()
    except:db.rollback();raise
    (OUT/'character_gender_applied.json').write_text(json.dumps({'backup':str(BACKUP),'changes':changes},ensure_ascii=False,indent=2),encoding='utf8')
if __name__=='__main__':main()

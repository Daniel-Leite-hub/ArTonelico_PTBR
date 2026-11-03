"""Conservative, auditable terminology and grammar pass; never marks human approval."""
from pathlib import Path
import json,re,sqlite3,sys,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.project import encoded_size
from artonelico_tool.quality import GAME_COMMAND_PATTERN

ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
OUT=ROOT/'work/curadoria_20261001';OUT.mkdir(exist_ok=True)
BACKUP=ROOT/'release/backups/ArTonelico_PTBR_antes_curadoria_20261001.atproj'
MANUAL={
 912:'Vamos usar minha receita...CRComa este prato!CRDelicioso, não?CR...Aqui diz [LEG]. Entendeu?',
 1985:'Achei que ele fosse morrer...CRQue bom que vai ficar bem.',
 6970:'*uf* *uf*CRNão ligo de correr, mas te segurar quando cai não é nada fácil...',
 15828:'(Droga, nem tive tempo de copiarCRo da Aurica...)',
 17197:'Mas depende do estrago e das peças necessárias. Só vou saber quando vir.',
 17311:'Que chato! Aquela despedida emocionante foi à toa.',
 21934:'Muitas visitas ao quarto de Lyner têm a ver com a Magia da Canção. Se você não usar uma em batalha ou proteger a Reyvateil, ela pode vir agradecer.',
 4104:'Não é verdade. Grande ou pequena, você ainda é a Misha.',
 4105:'Como pode provar? Mostre que vai continuar gostando da Misha adulta!',
 5077:'Misha tem razão. Após derrotar Mir, não ligaremos mais para o que Ayatane disse.',
 14191:'Sim, sou a Misha que rege as regras e a racionalidade. Estou destinada a salvar este mundo.',
 14622:'Sou a Misha, presidente do grêmio! Como pôde esquecer!?',
 4103:'Você trata bem a Misha pequena, mas talvez não trate a adulta da mesma forma.',
 2978:'Quando ela canta Magia da Canção, o MP diminui aos poucos.',
 2983:'Ajuda a manter a Magia da Canção ativa e elevar seu poder.',
 4062:'Misha, sabe cantar aquela Magia da Canção?',
 8905:'Sim. É disso que trata a Magia da Canção.',
 28283:'Sobre a Magia: Sword Slash',
 28284:'Sobre a Magia: My Hero',
 28285:'Sobre a Magia: Analyzer',
 28287:'Sobre a Magia: Seraphiflyer',
 28442:'Sobre a Magia: ABR',
 28443:'Sobre a Magia: Apostle of Mir',
 28444:'Sobre a Magia: ELMA-DS',
 28445:'Sobre a Magia: Shadow',
}

def improve(text):
    value=text
    # Do not change proper names or game control tokens. Misha is female even
    # when depicted at different ages in the Cosmosphere.
    for before,after in (
      ('do Misha','da Misha'),('no Misha','na Misha'),('ao Misha','à Misha'),
      ('pelo Misha','pela Misha'),('um Misha','uma Misha'),('o Misha','a Misha'),
      ('esse Misha','essa Misha'),('aquele Misha','aquela Misha'),
      ('seu Misha','sua Misha'),('meu Misha','minha Misha'),
      ('do Aurica','da Aurica'),('no Aurica','na Aurica'),('ao Aurica','à Aurica'),('o Aurica','a Aurica'),
      ('do Cosmosphere','da Cosmosfera'),('no Cosmosphere','na Cosmosfera'),
      ('ao Cosmosphere','à Cosmosfera'),('pelo Cosmosphere','pela Cosmosfera'),
      ('um Cosmosphere','uma Cosmosfera'),('o Cosmosphere','a Cosmosfera'),
      ('esse Cosmosphere','essa Cosmosfera'),('este Cosmosphere','esta Cosmosfera'),
      ('meu Cosmosphere','minha Cosmosfera'),('seu Cosmosphere','sua Cosmosfera'),
      ('verdadeiro Cosmosphere','verdadeira Cosmosfera'),
      ('do Song Magic','da Magia da Canção'),('no Song Magic','na Magia da Canção'),
      ('o Song Magic','a Magia da Canção'),('um Song Magic','uma Magia da Canção'),
    ):
        value=re.sub(r'(?<!\w)'+re.escape(before)+r'(?!\w)',after,value)
    value=value.replace('Cosmosphere','Cosmosfera')
    value=re.sub(r'(?<!\w)Song Magic(?!\w)','Magia da Canção',value)
    value=re.sub(r'(?<!\w)Magia de Canção(?!\w)','Magia da Canção',value)
    value=value.replace('Cristais Hymn','Cristais do Hino')
    value=value.replace('Misha está certo','Misha tem razão')
    value=value.replace('o Misha pequeno','a Misha pequena').replace('o Misha grande','a Misha adulta')
    value=value.replace('Misha grandão','Misha adulta').replace('Misha grande','Misha adulta')
    return value

def candidates(db):
    rows=db.execute("SELECT id,event_file,entry_index,original,automatic,translation,reviewed,review_status,original_bytes FROM dialogues WHERE locked=0 AND length(trim(automatic))>0 ORDER BY id").fetchall()
    changes=[]
    for r in rows:
        before=r['automatic'];after=MANUAL.get(r['id'],improve(before))
        if before==after:continue
        if r['reviewed'].strip():continue
        if GAME_COMMAND_PATTERN.findall(before)!=GAME_COMMAND_PATTERN.findall(after):
            raise ValueError(f'Game command changed at {r["id"]}')
        if before.count('CR')!=after.count('CR'):
            raise ValueError(f'CR count changed at {r["id"]}')
        size=encoded_size(after)
        if size is None:raise ValueError(f'Unencodable text at {r["id"]}')
        changes.append({'id':r['id'],'event_file':r['event_file'],'entry_index':r['entry_index'],
          'original':r['original'],'before':before,'after':after,'before_bytes':encoded_size(before),
          'after_bytes':size,'original_bytes':r['original_bytes'],'translation_matched':r['translation']==before})
    return changes

def main():
    if '--reconstruct' in sys.argv:
        if not BACKUP.exists():raise FileNotFoundError(BACKUP)
        with sqlite3.connect(BACKUP) as old, sqlite3.connect(DB) as new:
            old.row_factory=sqlite3.Row;new.row_factory=sqlite3.Row
            old_rows={r['id']:r for r in old.execute('SELECT * FROM dialogues')}
            changes=[]
            for row in new.execute('SELECT * FROM dialogues ORDER BY id'):
                prev=old_rows[row['id']]
                if row['automatic']==prev['automatic']:continue
                changes.append({'id':row['id'],'event_file':row['event_file'],'entry_index':row['entry_index'],
                    'original':row['original'],'before':prev['automatic'],'after':row['automatic'],
                    'before_bytes':encoded_size(prev['automatic']),'after_bytes':encoded_size(row['automatic']),
                    'original_bytes':row['original_bytes'],'translation_matched':prev['translation']==prev['automatic']})
        (OUT/'changes_applied.json').write_text(json.dumps({'applied':True,'database':str(DB),'backup':str(BACKUP),'changes':changes},ensure_ascii=False,indent=2),encoding='utf8')
        print('reconstructed changes',len(changes));return
    db=sqlite3.connect(DB);db.row_factory=sqlite3.Row
    changes=candidates(db)
    report=OUT/('changes_applied.json' if '--apply' in sys.argv else 'changes_dry_run.json')
    if '--apply' in sys.argv:
        if BACKUP.exists():raise FileExistsError(f'Backup already exists: {BACKUP}')
        BACKUP.parent.mkdir(exist_ok=True)
        with sqlite3.connect(BACKUP) as destination:db.backup(destination)
        try:
            db.execute('BEGIN')
            for item in changes:
                if item['translation_matched']:
                    db.execute('UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=? WHERE id=? AND automatic=? AND translation=?',
                      (item['after'],item['after'],item['after_bytes'],int(item['after_bytes']<=item['original_bytes']),item['id'],item['before'],item['before']))
                else:
                    db.execute('UPDATE dialogues SET automatic=? WHERE id=? AND automatic=?',
                      (item['after'],item['id'],item['before']))
                if db.execute('SELECT changes()').fetchone()[0]!=1:raise RuntimeError(f'Concurrent row change at {item["id"]}')
            db.commit()
        except:db.rollback();raise
    report.write_text(json.dumps({'applied':'--apply' in sys.argv,'database':str(DB),'backup':str(BACKUP) if '--apply' in sys.argv else None,'changes':changes},ensure_ascii=False,indent=2),encoding='utf8')
    print('changes',len(changes),'manual',sum(c['id'] in MANUAL for c in changes),'size_increases',sum(c['after_bytes']>c['before_bytes'] for c in changes),'above_original',sum(c['after_bytes']>c['original_bytes'] for c in changes))
    for c in changes[:25]:print(c['id'],repr(c['before']),'→',repr(c['after']))

if __name__=='__main__':main()

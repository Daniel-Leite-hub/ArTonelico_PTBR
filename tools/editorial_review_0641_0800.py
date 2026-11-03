"""Fifth line-read editorial batch, IDs 641-800."""
from pathlib import Path
import hashlib
import json
import sqlite3
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artonelico_tool.project import encoded_size
from artonelico_tool.quality import GAME_COMMAND_PATTERN

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
BACKUP = ROOT / 'release/backups/ArTonelico_PTBR_antes_leitura_editorial_0641_0800.atproj'
OUT = ROOT / 'work/curadoria_editorial_20261001/batch_0641_0800.json'

EDIT = {
    642: 'Ao obter um Cartão de Receita, você aprende a receita do item.',
    644: 'Conhecendo a receita, você pode registrar na lista até itens que nunca usou.',
    647: 'Quanto mais receitas aprender, mais perto estará de se tornar Mestre da Fusão.',
    663: 'Você levou tanto tempo fazendo isso. Nem sabia se eu conseguiria ver tudo de você.',
    664: 'Não fiquei preocupada com isso.',
    671: 'Entendi. Vou cuidar bem dela. Logo lhe darei um nome, como dei a Hama.',
    695: 'As Reyvateils pesquisavam sua própria Magia da Canção aqui.',
    696: 'Havia muitos laboratórios no subsolo. Com os experimentos extremos, o chão ficou instável e...',
    705: '...Pensei em tudo de que me arrependeria.',
    710: 'Mas agora não parece a hora certa...',
    712: 'E, se eu tivesse morrido, nunca poderia ter dito o que sentia.',
    719: 'Eu me odiava... Achava que estava condenada a cantar sozinha... para sempre... mas...',
    749: 'Peça Estelar...? Pra que você precisa disso?',
    757: 'Sim, encontramos.',
    767: 'Vamos voltar. Ela já pode fazer um [Meteor], né?',
    795: 'Misha!? Por que você está vestida assim?',
    799: 'Tentei criar um Meteor, mas falhei.',
}


def sha(value):
    return hashlib.sha256(value.encode('utf8')).hexdigest()


def main():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    inspected, changes = [], []
    for row in db.execute('SELECT id,original,automatic,translation,reviewed,locked,original_bytes '
                          'FROM dialogues WHERE id BETWEEN 641 AND 800 ORDER BY id'):
        if not row['automatic'].strip():
            continue
        inspected.append({'id': row['id'], 'original_sha256': sha(row['original']),
                          'automatic_sha256_before': sha(row['automatic'])})
        if row['id'] not in EDIT:
            continue
        before, after = row['automatic'], EDIT[row['id']]
        if row['locked'] or row['reviewed'].strip() or before == after:
            raise ValueError(f'Protected or unchanged: {row["id"]}')
        if GAME_COMMAND_PATTERN.findall(before) != GAME_COMMAND_PATTERN.findall(after):
            raise ValueError(f'Game command changed: {row["id"]}')
        if before.count('CR') != after.count('CR'):
            raise ValueError(f'CR marker changed: {row["id"]}')
        before_bytes, after_bytes = encoded_size(before), encoded_size(after)
        if after_bytes is None or before_bytes <= row['original_bytes'] < after_bytes:
            raise ValueError(f'New capacity overrun: {row["id"]}')
        changes.append({'id': row['id'], 'original': row['original'], 'before': before,
                        'after': after, 'original_bytes': row['original_bytes'],
                        'before_bytes': before_bytes, 'after_bytes': after_bytes,
                        'translation_matched': row['translation'] == before})
    if {x['id'] for x in changes} != set(EDIT):
        raise ValueError('Missing edit ID')
    print(f'inspected={len(inspected)} changes={len(changes)} capacity_crossings=0')
    for x in changes:
        print(x['id'], repr(x['before']), '->', repr(x['after']))
    if '--apply' not in sys.argv:
        return
    if BACKUP.exists():
        raise FileExistsError(BACKUP)
    OUT.parent.mkdir(exist_ok=True)
    with sqlite3.connect(BACKUP) as dst:
        db.backup(dst)
    try:
        db.execute('BEGIN')
        for x in changes:
            if x['translation_matched']:
                db.execute('UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=? '
                           'WHERE id=? AND automatic=? AND translation=?',
                           (x['after'], x['after'], x['after_bytes'],
                            int(x['after_bytes'] <= x['original_bytes']),
                            x['id'], x['before'], x['before']))
            else:
                db.execute('UPDATE dialogues SET automatic=? WHERE id=? AND automatic=?',
                           (x['after'], x['id'], x['before']))
            if db.execute('SELECT changes()').fetchone()[0] != 1:
                raise RuntimeError(x['id'])
        db.commit()
    except Exception:
        db.rollback()
        raise
    OUT.write_text(json.dumps({'inspection_scope': 'all automatic entries with IDs 641-800',
                               'inspected_entries': inspected, 'changes': changes,
                               'backup': str(BACKUP)}, ensure_ascii=False, indent=2), encoding='utf8')


if __name__ == '__main__':
    main()

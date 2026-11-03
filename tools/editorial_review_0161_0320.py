"""Second line-read editorial batch, IDs 161–320."""
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
BACKUP = ROOT / 'release/backups/ArTonelico_PTBR_antes_leitura_editorial_0161_0320.atproj'
OUT = ROOT / 'work/curadoria_editorial_20261001/batch_0161_0320.json'

EDIT = {
    166: 'Então... esta é Platina, que a Igreja chama de Terra Santa!',
    183: 'Hama! Você está viva de novo!',
    186: 'Acho que posso voltar desta vez por você. Te devo uma, então obrigada.',
    201: 'Quem é ela?',
    205: 'Juntas, elas formam o [Trio de Elemia].',
    206: 'Elas não são só um mito. Existiram de verdade.',
    222: 'Que bom que gostou. Fui eu que fiz.',
    230: 'Lembrança... você quer dizer...?',
    245: 'É melhor contar à Hama sobre o mundo virtual da Senhora Shurelia.',
    267: '...Na verdade, não. Devia usá-los logo, mas não tenho tantas receitas.',
    286: 'Já que gostou tanto, vou fazer um cartão de receita. Tente preparar também. É fácil.',
    299: 'Você pode ficar brava comigo de novo, mas... não consegui lembrar o que sentia quando fiz a antiga...',
    301: 'Quero que esta ocarina te dê apoio. E quero fazer o mesmo. Foi esse desejo que coloquei nela.',
    303: '...Lyner, obrigada. Você já me apoiou bastante.',
    304: 'Obrigada por estar sempre comigo...',
}


def main():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    inspected, changes = [], []
    for row in db.execute('SELECT id,original,automatic,translation,reviewed,locked,original_bytes '
                          'FROM dialogues WHERE id BETWEEN 161 AND 320 ORDER BY id'):
        if not row['automatic'].strip():
            continue
        inspected.append({'id': row['id'],
                          'original_sha256': hashlib.sha256(row['original'].encode('utf8')).hexdigest(),
                          'automatic_sha256_before': hashlib.sha256(row['automatic'].encode('utf8')).hexdigest()})
        if row['id'] not in EDIT:
            continue
        after = EDIT[row['id']]
        before = row['automatic']
        if row['locked'] or row['reviewed'].strip() or after == before:
            raise ValueError(f'Protected or unchanged: {row["id"]}')
        if GAME_COMMAND_PATTERN.findall(after) != GAME_COMMAND_PATTERN.findall(before):
            raise ValueError(f'Game command: {row["id"]}')
        if after.count('CR') != before.count('CR'):
            raise ValueError(f'CR marker: {row["id"]}')
        new_size = encoded_size(after)
        old_size = encoded_size(before)
        if new_size is None or old_size <= row['original_bytes'] < new_size:
            raise ValueError(f'Capacity: {row["id"]}')
        changes.append({'id': row['id'], 'original': row['original'], 'before': before,
                        'after': after, 'original_bytes': row['original_bytes'],
                        'before_bytes': old_size, 'after_bytes': new_size,
                        'translation_matched': row['translation'] == before})
    if {c['id'] for c in changes} != set(EDIT):
        raise ValueError('Missing edit ID')
    print(f'inspected={len(inspected)} changes={len(changes)} capacity_crossings=0')
    for c in changes:
        print(c['id'], repr(c['before']), '->', repr(c['after']))
    if '--apply' not in sys.argv:
        return
    if BACKUP.exists():
        raise FileExistsError(BACKUP)
    OUT.parent.mkdir(exist_ok=True)
    with sqlite3.connect(BACKUP) as dst:
        db.backup(dst)
    try:
        db.execute('BEGIN')
        for c in changes:
            if c['translation_matched']:
                db.execute('UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=? '
                           'WHERE id=? AND automatic=? AND translation=?',
                           (c['after'], c['after'], c['after_bytes'],
                            int(c['after_bytes'] <= c['original_bytes']),
                            c['id'], c['before'], c['before']))
            else:
                db.execute('UPDATE dialogues SET automatic=? WHERE id=? AND automatic=?',
                           (c['after'], c['id'], c['before']))
            if db.execute('SELECT changes()').fetchone()[0] != 1:
                raise RuntimeError(c['id'])
        db.commit()
    except Exception:
        db.rollback()
        raise
    OUT.write_text(json.dumps({'inspection_scope': 'all automatic entries with IDs 161-320',
                               'inspected_entries': inspected, 'changes': changes,
                               'backup': str(BACKUP)}, ensure_ascii=False, indent=2), encoding='utf8')


if __name__ == '__main__':
    main()

"""Third line-read editorial batch, IDs 321-480."""
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
BACKUP = ROOT / 'release/backups/ArTonelico_PTBR_antes_leitura_editorial_0321_0480.atproj'
OUT = ROOT / 'work/curadoria_editorial_20261001/batch_0321_0480.json'

EDIT = {
    327: 'Mir!? Você quer dizer [o Vírus-Mãe]!?',
    347: 'Será que alguém parou aquele robô? Foi tudo tão rápido, né?',
    348: 'É! Fico imaginando o que aconteceu com ele... hahaha!',
    371: 'Obrigada, Lyner. Desculpe por ter que visitar tantos mundos estranhos dentro de mim...',
    372: 'Não sei como será o próximo, mas adoraria que você viesse conhecê-lo comigo.',
    405: 'Você entrou no mundo virtual.',
    413: 'Não, hoje não quero Kitty Candy. Vim te pedir um favor.',
    414: 'Qual favor?',
    416: 'Uau, qual é?',
    421: 'Eu ficaria cercada de caras que fariam tudo por mim!',
    428: 'Então você é a maioral do Beco Vagalume?',
    432: 'Bem a sua cara. Tomara que se realize.',
    433: 'Obrigada!',
    438: 'Ei, calma. Por que está tão nervosa?',
    449: 'Pra falar a verdade, isso me incomoda tanto que talvez eu nem durma à noite.',
    459: '...Um carteiro não entregaria esta carta para essa pessoa.',
    475: '...Sim?',
    477: 'Aconteça o que acontecer comigo, confie em mim... e siga seu caminho.',
}


def sha(value):
    return hashlib.sha256(value.encode('utf8')).hexdigest()


def main():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    inspected, changes = [], []
    for row in db.execute('SELECT id,original,automatic,translation,reviewed,locked,original_bytes '
                          'FROM dialogues WHERE id BETWEEN 321 AND 480 ORDER BY id'):
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
    OUT.write_text(json.dumps({'inspection_scope': 'all automatic entries with IDs 321-480',
                               'inspected_entries': inspected, 'changes': changes,
                               'backup': str(BACKUP)}, ensure_ascii=False, indent=2), encoding='utf8')


if __name__ == '__main__':
    main()

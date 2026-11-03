"""Fourth line-read editorial batch, IDs 481-640."""
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
BACKUP = ROOT / 'release/backups/ArTonelico_PTBR_antes_leitura_editorial_0481_0640.atproj'
OUT = ROOT / 'work/curadoria_editorial_20261001/batch_0481_0640.json'

EDIT = {
    490: 'E, se tiver um assunto, você pode visitar o quarto dela.',
    494: 'Juntando esses selos, você pode [Mergulhar] mais fundo no Espaço da Alma delas. O [Sistema de Mergulho] será explicado depois.',
    491: 'Ao visitar um quarto com assunto disponível, surgem as opções de conversa. Escolha uma e aproveite.',
    500: 'Quando houver algo para conversar, as opções de assunto aparecerão. Escolha uma.',
    501: 'Você tem algo para conversar, né? Me conta.',
    504: 'Hã... Estou exausto. Desde que cheguei ao Mundo Inferior, não tive um dia de descanso...',
    516: 'A mente de Aurica está se voltando aos poucos para o lado negativo. Minha força está enfraquecendo.',
    520: 'Agora, a Aurica verdadeira só se vê como fonte de fracasso e desgraça.',
    523: 'Não é verdade. Havia sinais. Você viu a Aurica diabólica várias vezes.',
    531: 'Lute ao meu lado. Preciso enfrentar o rei do mundo negativo...',
    534: '...Tudo bem. Vou fazer o possível para ajudar você.',
    536: 'O rei negativo vive no Castelo dos Monstros. Vamos lá.',
    551: 'O que é isso? É só doce.',
    558: '...Então é da Lyra que vêm os itens e informações da Spica...',
    562: '...Quem é ela?',
    575: 'Só você.',
    590: 'Muito obrigada! Vai ser muito útil.',
    601: 'Sinceramente, nem sei o que faria com ele.',
    609: 'Mas, quando a música ficar pronta, teremos que nos despedir.',
    616: '...Uau. Que plano específico. Tomara que seu sonho se realize.',
    619: 'É...?',
}


def sha(value):
    return hashlib.sha256(value.encode('utf8')).hexdigest()


def main():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    inspected, changes = [], []
    for row in db.execute('SELECT id,original,automatic,translation,reviewed,locked,original_bytes '
                          'FROM dialogues WHERE id BETWEEN 481 AND 640 ORDER BY id'):
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
    OUT.write_text(json.dumps({'inspection_scope': 'all automatic entries with IDs 481-640',
                               'inspected_entries': inspected, 'changes': changes,
                               'backup': str(BACKUP)}, ensure_ascii=False, indent=2), encoding='utf8')


if __name__ == '__main__':
    main()

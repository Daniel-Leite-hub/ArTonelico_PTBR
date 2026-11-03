"""Fourth, conservative PT-BR terminology pass for the active project."""
from pathlib import Path
import json
import re
import sqlite3
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artonelico_tool.project import encoded_size
from artonelico_tool.quality import GAME_COMMAND_PATTERN

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
BACKUP = ROOT / 'release/backups/ArTonelico_PTBR_antes_termos_20261001.atproj'
OUT = ROOT / 'work/curadoria_20261001/terms_applied.json'


def improve(source, value):
    if 'Blastline' in source and 'create a sea of death' not in source:
        value = re.sub('Linha de Explosão', 'Blastline', value, flags=re.I)
        value = re.sub('linha de explosão', 'Blastline', value, flags=re.I)
    if 'Grathnode Crystal' in source:
        value = value.replace('Cristais de Grathnode', 'Cristais Grathnode')
        value = value.replace('Cristal de Grathnode', 'Cristal Grathnode')
    if 'Crescent Chronicle' in source:
        variants = ('Crescent Chronicle', 'Crônica da Lua Crescente',
                    'Cronículo da Lua Crescente', 'Crônica do Crescente',
                    'Crônica crescente')
        for term in variants:
            value = re.sub(re.escape(term), 'Crônica Crescente', value, flags=re.I)
        # The site/altar is feminine in the localized name.
        for old, new in ((r'\bdo\s+(?=[“"\[]?Crônica Crescente\b)', 'da '),
                         (r'\bno\s+(?=[“"\[]?Crônica Crescente\b)', 'na '),
                         (r'\bao\s+(?=[“"\[]?Crônica Crescente\b)', 'à '),
                         (r'\bpelo\s+(?=[“"\[]?Crônica Crescente\b)', 'pela '),
                         (r'\bo\s+(?=[“"\[]?Crônica Crescente\b)', 'a ')):
            value = re.sub(old, new, value)
        value = re.sub(r'\bO (?=[“"\[]?Crônica Crescente\b)', 'A ', value)
        value = re.sub(r'\bO (?=\[Crônica Crescente\])', 'A ', value)
        value = value.replace('Bem-vindo à Crônica Crescente', 'Boas-vindas à Crônica Crescente')
        value = value.replace('A [Crônica Crescente] foi adicionado', 'A [Crônica Crescente] foi adicionada')
        value = value.replace('A Crônica Crescente foi feito', 'A Crônica Crescente foi feita')
        value = value.replace('A Crônica Crescente está fechado', 'A Crônica Crescente está fechada')
        value = value.replace('A Crônica Crescente for destruído', 'A Crônica Crescente for destruída')
        value = value.replace('a “Crônica Crescente” for destruído', 'a “Crônica Crescente” for destruída')
        value = value.replace('Este é a Crônica Crescente', 'Esta é a Crônica Crescente')
        value = value.replace('Isso aqui é a Crônica Crescente', 'Isto aqui é a Crônica Crescente')
        value = value.replace('todo a “Crônica Crescente”', 'toda a “Crônica Crescente”')
        value = value.replace('tornou... este vaso sagrado, a Crônica Crescente',
                              'tornou... a Crônica Crescente, este vaso sagrado')
        if 'the Crescent Chronicle was made to be a coffin' in source:
            value = 'Eu... tornei-me a Crônica Crescente, um caixão para Mir selada.'
    return value


def main():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    changes = []
    for row in db.execute('SELECT id,original,automatic,translation,reviewed,locked,original_bytes '
                          'FROM dialogues WHERE length(trim(automatic))>0'):
        if row['locked'] or row['reviewed'].strip():
            continue
        if not any(term in row['original'] for term in
                   ('Blastline', 'blastline', 'Grathnode Crystal', 'Crescent Chronicle')):
            continue
        after = improve(row['original'], row['automatic'])
        if after == row['automatic']:
            continue
        if GAME_COMMAND_PATTERN.findall(after) != GAME_COMMAND_PATTERN.findall(row['automatic']):
            raise ValueError(f'Game command changed: {row["id"]}')
        if after.count('CR') != row['automatic'].count('CR'):
            raise ValueError(f'CR marker changed: {row["id"]}')
        size = encoded_size(after)
        if size is None:
            raise ValueError(f'Cannot encode: {row["id"]}')
        before_size = encoded_size(row['automatic'])
        changes.append({'id': row['id'], 'original': row['original'],
                        'before': row['automatic'], 'after': after,
                        'original_bytes': row['original_bytes'],
                        'before_bytes': before_size, 'after_bytes': size,
                        'translation_matched': row['translation'] == row['automatic']})
    crossings = [c['id'] for c in changes if c['before_bytes'] <= c['original_bytes'] < c['after_bytes']]
    if crossings:
        raise ValueError(f'New capacity overruns: {crossings}')
    print(f'changes={len(changes)} capacity_crossings={len(crossings)}')
    for c in changes:
        print(c['id'], repr(c['before']), '->', repr(c['after']))
    if '--apply' not in sys.argv:
        return
    if BACKUP.exists():
        raise FileExistsError(BACKUP)
    with sqlite3.connect(BACKUP) as dst:
        db.backup(dst)
    try:
        db.execute('BEGIN')
        for c in changes:
            if c['translation_matched']:
                db.execute('UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=? '
                           'WHERE id=? AND automatic=? AND translation=?',
                           (c['after'], c['after'], c['after_bytes'],
                            int(c['after_bytes'] <= c['original_bytes']), c['id'], c['before'], c['before']))
            else:
                db.execute('UPDATE dialogues SET automatic=? WHERE id=? AND automatic=?',
                           (c['after'], c['id'], c['before']))
            if db.execute('SELECT changes()').fetchone()[0] != 1:
                raise RuntimeError(c['id'])
        db.commit()
    except Exception:
        db.rollback()
        raise
    OUT.write_text(json.dumps({'backup': str(BACKUP), 'changes': changes},
                              ensure_ascii=False, indent=2), encoding='utf8')


if __name__ == '__main__':
    main()

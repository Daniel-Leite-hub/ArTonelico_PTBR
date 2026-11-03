"""Apply evidence-checked first editorial batch; keep inspection distinct from approval."""
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
BACKUP = ROOT / 'release/backups/ArTonelico_PTBR_antes_leitura_editorial_20261001.atproj'
OUT = ROOT / 'work/curadoria_editorial_20261001'

# Read against original English and adjacent dialogue, IDs 1–160.
FIRST = {
    26: 'Recebi [500 Leaf]!',
    41: 'Então vou deixar você provar meu refrigerante definitivo.',
    48: 'Porque sou esperto! Estou tentando salvar minha vida!',
    53: 'O que houve? Por que está tremendo? Está com frio?',
    59: 'Por que se despediu? Não devia dizer “Saúde”?',
    60: '*suspiro* ...Saúde.',
    65: 'Só posso dizer uma coisa: “É o poder do amor.”',
    90: '...Não. Estou bem. Já estou em pedaços...',
    91: 'O quê!? Em pedaços? Como assim?',
    94: 'Tudo bem... obrigada...',
    101: 'Fiz especialmente para você. Deve caber direitinho.',
    102: 'Sério? ...Você tem razão! Coube certinho no meu dedo!',
    103: 'Que bom. Fiquei preocupada que não servisse.',
    104: 'Se tivesse perguntado, eu teria dito o tamanho do meu dedo.',
    105: 'Mas, se eu perguntasse, não seria uma surpresa, né?',
    107: '...Se eu te der agora, será como um prêmio por ter vencido o jogo nos nossos Mergulhos.',
    122: 'Bispo Falss...? Será que as lembranças da infância dela se misturaram com o presente...?',
    130: 'Ah, mas é assim que deveria ser a verdadeira Lenda de Elemia.',
    143: 'Sim. Obrigada por me salvar, Don Leon!',
    144: 'Foi um prazer! Chame-me se precisar de mim de novo.',
}

# Currency, not the botanical noun; the latter is left untouched.
CURRENCY = {
    603: 'Recebi [300 Leaf].',
    2599: 'Você tem 1.000 Leaf?',
    3753: 'Sim, temos. Custa só 10 mil Leaf agora.',
    3754: '10 mil Leaf!? Não tenho tanto dinheiro!',
    4194: 'Quantos Kitty Candies você quer? São 12 Leaf por doce.',
    4201: 'Vou dar um ótimo desconto. Vai custar só 1.000 Leaf.',
    4202: 'Mil Leaf!? Não tenho tanto dinheiro.',
    6324: 'Quantos Kitty Candies você quer? São 12 Leaf por doce♪',
    7069: 'Vai custar 18.326.991 Leaf para consertar.',
    8099: 'Os dois saem por 400 Leaf!',
    12806: 'Como diz o ditado: de grão em grão se enche o papo. Um Leaf poupado é um Leaf ganho.',
    13567: 'Ah, oi, Misha! São 12 Leaf por doce. Quantos você quer?',
    13606: 'Agora, quando eu disser: “São 12 Leaf por doce...”',
    19234: 'Não brinque com os sentimentos das garotas. Pode acabar pagando um milhão de Leaf para uma que achou que você a amava.',
    20005: 'É raro, então custa 2.000 Leaf... mas...',
    28082: 'São só 12 Leaf. Não deve ser problema, por mais que a gente compre!',
    28085: 'Se couberem cerca de 2.800 unidades, serão 33.600 Leaf. Para nós dois, 67.200 Leaf.',
    28598: 'O famoso Kitty Candy do Beco Vagalume! Só 12 Leaf cada!',
    30525: 'Quer provar o famoso Kitty Candy do Beco Vagalume? São 12 Leaf por doce.',
    30535: 'São %s Leaf. Você pode pagar?',
    30580: 'Com licença, vou precisar de %s Leaf pela manutenção...',
    32678: 'São... 100 Leaf pela aposta de que você conseguiria sem saber o que significava.',
    32749: 'O item novo foi vendido por %s Leaf. Agora você tem [%s] x%s de qualidade %s.',
}


def digest(text):
    return hashlib.sha256(text.encode('utf8')).hexdigest()


def main():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    changes = []
    inspection = []
    edits = {**FIRST, **CURRENCY}
    for row in db.execute('SELECT id,original,automatic,translation,reviewed,locked,original_bytes '
                          'FROM dialogues WHERE length(trim(automatic))>0 ORDER BY id'):
        id_ = row['id']
        if id_ <= 160:
            inspection.append({'id': id_, 'original_sha256': digest(row['original']),
                               'automatic_sha256_before': digest(row['automatic'])})
        if id_ not in edits:
            continue
        if row['locked'] or row['reviewed'].strip():
            raise ValueError(f'Protected entry: {id_}')
        after = edits[id_]
        if after == row['automatic']:
            raise ValueError(f'No-op: {id_}')
        if GAME_COMMAND_PATTERN.findall(after) != GAME_COMMAND_PATTERN.findall(row['automatic']):
            raise ValueError(f'Game command changed: {id_}')
        if after.count('CR') != row['automatic'].count('CR'):
            raise ValueError(f'CR count changed: {id_}')
        before_size = encoded_size(row['automatic'])
        after_size = encoded_size(after)
        if after_size is None:
            raise ValueError(f'Unencodable: {id_}')
        if before_size <= row['original_bytes'] < after_size:
            raise ValueError(f'New capacity overrun: {id_}')
        changes.append({'id': id_, 'original': row['original'], 'before': row['automatic'],
                        'after': after, 'original_bytes': row['original_bytes'],
                        'before_bytes': before_size, 'after_bytes': after_size,
                        'translation_matched': row['translation'] == row['automatic']})
    if set(edits) != {item['id'] for item in changes}:
        raise ValueError('Missing IDs')
    print(f'inspected={len(inspection)} changes={len(changes)} capacity_crossings=0')
    for c in changes:
        print(c['id'], repr(c['before']), '->', repr(c['after']))
    if '--apply' not in sys.argv:
        return
    if BACKUP.exists():
        raise FileExistsError(BACKUP)
    OUT.mkdir(exist_ok=True)
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
    (OUT / 'batch_0001_0160.json').write_text(json.dumps({
        'inspection_scope': 'all automatic entries with IDs 1-160; currency rows additionally inspected',
        'inspected_entries': inspection, 'changes': changes,
        'currency_ids': sorted(CURRENCY), 'backup': str(BACKUP)},
        ensure_ascii=False, indent=2), encoding='utf8')


if __name__ == '__main__':
    main()

"""Apply one manually read editorial proposal file with immutable evidence."""
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
OUT_DIR = ROOT / 'work/curadoria_editorial_20261001'


def sha(text):
    return hashlib.sha256(text.encode('utf8')).hexdigest()


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: editorial_batch_engine.py proposal.json [--apply]')
    proposal = Path(sys.argv[1]).resolve()
    if proposal.parent != OUT_DIR.resolve() or not proposal.name.startswith('proposal_'):
        raise ValueError('Proposal must be in the editorial work directory')
    data = json.loads(proposal.read_text(encoding='utf8'))
    lo, hi = data['first_id'], data['last_id']
    if not (isinstance(lo, int) and isinstance(hi, int) and 0 < lo <= hi <= 32853):
        raise ValueError('Invalid ID range')
    edits = {int(k): v for k, v in data['edits'].items()}
    if not all(lo <= k <= hi and isinstance(v, str) and v for k, v in edits.items()):
        raise ValueError('Edits outside range or empty')
    stem = f'{lo:04d}_{hi:04d}'
    backup = ROOT / f'release/backups/ArTonelico_PTBR_antes_leitura_editorial_{stem}.atproj'
    output = OUT_DIR / f'batch_{stem}.json'
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    inspected, changes = [], []
    for row in db.execute('SELECT id,original,automatic,translation,reviewed,locked,original_bytes '
                          'FROM dialogues WHERE id BETWEEN ? AND ? ORDER BY id', (lo, hi)):
        if not row['automatic'].strip():
            continue
        inspected.append({'id': row['id'], 'original_sha256': sha(row['original']),
                          'automatic_sha256_before': sha(row['automatic'])})
        if row['id'] not in edits:
            continue
        before, after = row['automatic'], edits[row['id']]
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
    if {x['id'] for x in changes} != set(edits):
        raise ValueError('Missing edit ID')
    print(f'inspected={len(inspected)} changes={len(changes)} capacity_crossings=0')
    for x in changes:
        print(x['id'], repr(x['before']), '->', repr(x['after']))
    if '--apply' not in sys.argv:
        return
    if backup.exists() or output.exists():
        raise FileExistsError(f'{backup} or {output}')
    with sqlite3.connect(backup) as dst:
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
    output.write_text(json.dumps({'inspection_scope': f'all automatic entries with IDs {lo}-{hi}',
                                  'inspected_entries': inspected, 'changes': changes,
                                  'backup': str(backup)}, ensure_ascii=False, indent=2), encoding='utf8')


if __name__ == '__main__':
    main()

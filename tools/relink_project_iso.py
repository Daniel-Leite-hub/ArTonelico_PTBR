"""Reconnect a restored project to an identical original ISO, without API calls."""
import argparse
import hashlib
import json
import sqlite3
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artonelico_tool.iso import find, read_entry

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    parser.add_argument('original_iso', type=Path)
    args = parser.parse_args()
    if not args.project.is_file() or not args.original_iso.is_file():
        raise FileNotFoundError('Project and original ISO must exist')
    db = sqlite3.connect(args.project)
    try:
        assert db.execute('PRAGMA quick_check').fetchone()[0] == 'ok'
        meta = {k: json.loads(v) for k, v in db.execute('SELECT key,value FROM meta')}
        source = args.original_iso.resolve()
        if source.stat().st_size != meta['iso_size']:
            raise ValueError('Original ISO size mismatch')
        elf = read_entry(source, find(source, 'SLUS_214.45'))
        if hashlib.sha256(elf).hexdigest() != meta['executable_sha256']:
            raise ValueError('Original executable hash mismatch')
        db.execute('UPDATE meta SET value=? WHERE key=?', (json.dumps(str(source)), 'iso_path'))
        db.commit()
        print('Source ISO reconnected; translations unchanged')
    finally:
        db.close()

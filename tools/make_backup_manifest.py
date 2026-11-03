"""Inventory every file in the backup package with SHA-256."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]

if __name__ == '__main__':
    target = ROOT / 'MANIFESTO_BACKUP.json'
    records = []
    paths = sorted(p for p in ROOT.rglob('*') if p.is_file() and p != target)
    for number, path in enumerate(paths, 1):
        with path.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        records.append(dict(path=path.relative_to(ROOT).as_posix(), bytes=path.stat().st_size, sha256=digest))
        if number % 500 == 0:
            print(f'Hashed {number}/{len(paths)} files', flush=True)
    output = dict(schema=1, created_utc=datetime.now(timezone.utc).isoformat(),
                  files=len(records), total_bytes=sum(r['bytes'] for r in records), records=records)
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps({k: v for k, v in output.items() if k != 'records'}), flush=True)

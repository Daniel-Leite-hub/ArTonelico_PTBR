"""Check that only intended automatic/draft fields changed since the baseline."""
from pathlib import Path
import json,sqlite3,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.quality import GAME_COMMAND_PATTERN
from artonelico_tool.project import encoded_size,planned_iso_counts
root=Path(__file__).resolve().parents[1]
before=root/'release/backups/ArTonelico_PTBR_antes_curadoria_20261001.atproj'
after=root/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
old=sqlite3.connect(before);new=sqlite3.connect(after)
old.row_factory=new.row_factory=sqlite3.Row
old_rows={r['id']:r for r in old.execute('SELECT * FROM dialogues')}
changes=[]
allowed={'automatic','translation','translated_bytes','size_ok'}
for r in new.execute('SELECT * FROM dialogues ORDER BY id'):
    prior=old_rows.pop(r['id'])
    differing={field for field in r.keys() if r[field]!=prior[field]}
    if not differing:continue
    if not differing<=allowed:raise ValueError(f'Unexpected field change {r["id"]}: {differing}')
    if not r['automatic'].strip() or r['locked'] or r['reviewed'].strip():raise ValueError(f'Unsafe row {r["id"]}')
    if GAME_COMMAND_PATTERN.findall(r['automatic'])!=GAME_COMMAND_PATTERN.findall(prior['automatic']):raise ValueError(f'Game command {r["id"]}')
    if r['automatic'].count('CR')!=prior['automatic'].count('CR'):raise ValueError(f'CR marker {r["id"]}')
    if encoded_size(r['automatic']) is None:raise ValueError(f'Unencodable row {r["id"]}')
    if prior['translation']==prior['automatic'] and r['translation']!=r['automatic']:raise ValueError(f'Unsynced draft {r["id"]}')
    if encoded_size(prior['automatic'])<=r['original_bytes']<encoded_size(r['automatic']):raise ValueError(f'New capacity overrun {r["id"]}')
    changes.append(r['id'])
if old_rows:raise ValueError(f'Missing rows: {len(old_rows)}')
if new.execute('PRAGMA integrity_check').fetchone()[0]!='ok':raise ValueError('Database integrity failure')
counts=planned_iso_counts(new)
report={'baseline':str(before),'current':str(after),'changed_dialogues':len(changes),
        'changed_ids':changes,'allowed_fields':sorted(allowed),'sqlite_integrity':'ok',
        'game_commands_preserved':True,'no_new_capacity_overrun':True,
        'human_review_unchanged':True,'planned_iso_counts':counts}
out=root/'work/curadoria_20261001/verification.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='changed_ids'},ensure_ascii=False,indent=2))

"""Fix six audited encoding errors, with a SQLite snapshot and row archive."""
from pathlib import Path
import sys,sqlite3,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.evd import encode_game_text

fixes={
29176:'Pq. Pedra-Canto-Noite',
29211:'Silva U - Portão D',
29219:'Blindagem - Setor L',
29223:'Blindagem - Setor U',
29267:'Prisma G - Fundos',
30691:'Criando dados salvos. Não desligue o PlayStation 2 nem remova o Memory Card (8 MB) do PlayStation 2.',
}

if __name__=='__main__':
    root=Path(__file__).resolve().parents[1]
    path=root/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
    backup=root/'release/backups/ArTonelico_antes_6_erros_20260926.atproj'
    db=sqlite3.connect(path);db.row_factory=sqlite3.Row
    rows=db.execute("SELECT * FROM dialogues WHERE error<>''").fetchall()
    assert {r['id'] for r in rows}==set(fixes),'Error set changed; do not apply blindly'
    for row in rows:
        assert not row['reviewed'].strip(),'Preserve user review'
        assert len(encode_game_text(fixes[row['id']]))<=row['original_bytes'],row['id']
    if backup.exists():raise FileExistsError(backup)
    backup.parent.mkdir(parents=True,exist_ok=True)
    snapshot=sqlite3.connect(backup);db.backup(snapshot);snapshot.close()
    with db:
        db.execute('CREATE TABLE IF NOT EXISTS correction_archive_20260926 (id INTEGER PRIMARY KEY, before_json TEXT NOT NULL, adapted TEXT NOT NULL)')
        for row in rows:
            text=fixes[row['id']]
            db.execute('INSERT INTO correction_archive_20260926 VALUES(?,?,?)',(row['id'],json.dumps(dict(row),ensure_ascii=False),text))
            db.execute("UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=1,error='',provider='local-adaptation' WHERE id=?",(text,text,len(encode_game_text(text)),row['id']))
    assert db.execute("SELECT COUNT(*) FROM dialogues WHERE error<>''").fetchone()[0]==0
    assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
    for row in rows:
        r=db.execute('SELECT * FROM dialogues WHERE id=?',(row['id'],)).fetchone()
        assert len(encode_game_text(r['automatic']))<=r['original_bytes'] and r['size_ok']==1 and not r['error']
    print('6 corrected; encoding and capacity validated; errors=0; SQLite integrity OK; snapshot retained; no ISO generated')
    db.close()

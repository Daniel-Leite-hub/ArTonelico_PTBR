from __future__ import annotations

import json
import hashlib
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from .evd import encode_game_text, parse
from .executable_text import extract_executable_texts
from .iso import SECTOR, find, read_entry
from .rpk import read_index
from .text_roles import translation_track


SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS dialogues (
 id INTEGER PRIMARY KEY,
 event_file TEXT NOT NULL,
 entry_index INTEGER NOT NULL,
 text_id INTEGER NOT NULL,
 speaker_id INTEGER NOT NULL,
 original TEXT NOT NULL,
 automatic TEXT NOT NULL DEFAULT '',
 translation TEXT NOT NULL DEFAULT '',
 reviewed TEXT NOT NULL DEFAULT '',
 original_bytes INTEGER NOT NULL,
 translated_bytes INTEGER NOT NULL DEFAULT 0,
 size_ok INTEGER NOT NULL DEFAULT 1,
 locked INTEGER NOT NULL DEFAULT 0,
 provider TEXT NOT NULL DEFAULT '',
 error TEXT NOT NULL DEFAULT '',
 review_status TEXT NOT NULL DEFAULT 'unreviewed',
 review_origin TEXT NOT NULL DEFAULT '',
 reviewed_at TEXT NOT NULL DEFAULT '',
 reviewed_hash TEXT NOT NULL DEFAULT '',
 translation_track TEXT NOT NULL DEFAULT 'dialogue',
 UNIQUE(event_file, entry_index)
);
CREATE INDEX IF NOT EXISTS dialogue_event ON dialogues(event_file, entry_index);
CREATE INDEX IF NOT EXISTS dialogue_status ON dialogues(size_ok, translation, reviewed);
"""


def connect(path: Path) -> sqlite3.Connection:
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    table_exists = db.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='dialogues'"
    ).fetchone()
    if table_exists:
        existing = {row[1] for row in db.execute("PRAGMA table_info(dialogues)")}
        if "review_status" not in existing or "automatic" not in existing:
            backup_dir = path.parent / "backups" / path.stem
            backup_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            destination = backup_dir / f"{path.stem}_antes_migracao_v2_{timestamp}.atproj"
            target = sqlite3.connect(destination)
            try:
                db.backup(target)
            finally:
                target.close()
    db.executescript(SCHEMA)
    _migrate(db)
    return db


def _migrate(db: sqlite3.Connection) -> None:
    columns = {row[1] for row in db.execute("PRAGMA table_info(dialogues)")}
    additions = {
        "automatic": "TEXT NOT NULL DEFAULT ''",
        "review_status": "TEXT NOT NULL DEFAULT 'unreviewed'",
        "review_origin": "TEXT NOT NULL DEFAULT ''",
        "reviewed_at": "TEXT NOT NULL DEFAULT ''",
        "reviewed_hash": "TEXT NOT NULL DEFAULT ''",
        "translation_track": "TEXT NOT NULL DEFAULT 'dialogue'",
    }
    for name, declaration in additions.items():
        if name not in columns:
            db.execute(f"ALTER TABLE dialogues ADD COLUMN {name} {declaration}")
    db.execute(
        "UPDATE dialogues SET automatic=translation "
        "WHERE automatic='' AND translation<>'' AND provider<>''"
    )
    legacy = db.execute(
        "SELECT id,reviewed FROM dialogues "
        "WHERE length(trim(reviewed))>0 AND review_status='unreviewed'"
    ).fetchall()
    for row in legacy:
        db.execute(
            "UPDATE dialogues SET review_status='approved',review_origin='legado',reviewed_hash=? "
            "WHERE id=?",
            (text_digest(row["reviewed"]), row["id"]),
        )
    if get_meta(db, "translation_track_version") != 6:
        for row in db.execute(
            "SELECT id,event_file,entry_index FROM dialogues WHERE event_file LIKE 'SLUS/TEXT/%'"
        ):
            db.execute(
                "UPDATE dialogues SET translation_track=? WHERE id=?",
                (translation_track(row["event_file"], row["entry_index"]), row["id"]),
            )
        _set_meta(db, "translation_track_version", 6)
    _set_meta(db, "schema_version", 3)
    db.commit()


def _set_meta(db: sqlite3.Connection, key: str, value: object) -> None:
    db.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", (key, json.dumps(value, ensure_ascii=False)))


def get_meta(db: sqlite3.Connection, key: str, default=None):
    row = db.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
    return json.loads(row[0]) if row else default


def ensure_source_identity(db: sqlite3.Connection) -> dict[str, object] | None:
    source_value = get_meta(db, "iso_path")
    if not source_value:
        return None
    iso_path = Path(source_value)
    if not iso_path.is_file():
        return None
    iso_size = iso_path.stat().st_size
    executable_hash = get_meta(db, "executable_sha256")
    executable_entry = find(iso_path, "SLUS_214.45")
    executable = read_entry(iso_path, executable_entry)
    if not executable_hash:
        executable_hash = hashlib.sha256(executable).hexdigest()
    if get_meta(db, "executable_text_version") != 3:
        database_file = db.execute("PRAGMA database_list").fetchone()[2]
        if database_file and db.execute("SELECT COUNT(*) FROM dialogues").fetchone()[0]:
            backup_project(db, Path(database_file), "antes_textos_slus")
    imported = ensure_executable_texts(db, executable)
    _set_meta(db, "iso_size", iso_size)
    _set_meta(db, "executable_sha256", executable_hash)
    db.commit()
    return {
        "iso_size": iso_size,
        "executable_sha256": executable_hash,
        "executable_texts_imported": imported,
    }


def ensure_executable_texts(db: sqlite3.Connection, executable: bytes) -> int:
    if get_meta(db, "executable_text_version") == 3:
        return 0
    texts = extract_executable_texts(executable)
    preserved = {
        row["entry_index"]: row
        for row in db.execute(
            "SELECT * FROM dialogues WHERE event_file LIKE ?",
            ("SLUS/TEXT/%",),
        )
    }
    db.execute("DELETE FROM dialogues WHERE event_file LIKE ?", ("SLUS/TEXT/%",))
    for item in texts:
        db.execute(
            """INSERT INTO dialogues(
               event_file,entry_index,text_id,speaker_id,original,original_bytes,locked
               ) VALUES(?,?,?,?,?,?,?)""",
            (
                item.event_file,
                item.offset,
                item.offset,
                0,
                item.text,
                item.encoded_length,
                int(item.locked),
            ),
        )
        previous = preserved.get(item.offset)
        if previous is not None:
            db.execute(
                """UPDATE dialogues SET automatic=?,translation=?,reviewed=?,translated_bytes=?,
                   size_ok=?,provider=?,error=?,review_status=?,review_origin=?,reviewed_at=?,
                   reviewed_hash=? WHERE event_file=? AND entry_index=?""",
                (
                    previous["automatic"],
                    previous["translation"],
                    previous["reviewed"],
                    previous["translated_bytes"],
                    previous["size_ok"],
                    previous["provider"],
                    previous["error"],
                    previous["review_status"],
                    previous["review_origin"],
                    previous["reviewed_at"],
                    previous["reviewed_hash"],
                    item.event_file,
                    item.offset,
                ),
            )
    _set_meta(db, "executable_text_version", 3)
    _set_meta(db, "executable_text_count", len(texts))
    for item in texts:
        db.execute(
            "UPDATE dialogues SET translation_track=? WHERE event_file=? AND entry_index=?",
            (translation_track(item.event_file, item.offset), item.event_file, item.offset),
        )
    db.commit()
    return len(texts)


def create_from_iso(iso_path: Path, project_path: Path, progress=None) -> int:
    executable_entry = find(iso_path, "SLUS_214.45")
    rpk_entry = find(iso_path, "RPK.BIN")
    executable = read_entry(iso_path, executable_entry)
    temp_exe = project_path.with_suffix(".slus.tmp")
    temp_exe.write_bytes(executable)
    try:
        index = read_index(temp_exe, rpk_entry.size)
    finally:
        temp_exe.unlink(missing_ok=True)
    events = [entry for entry in index if entry.name.casefold().endswith(".evd")]
    db = connect(project_path)
    db.execute("DELETE FROM dialogues")
    with iso_path.open("rb") as source:
        for event_number, entry in enumerate(events, 1):
            source.seek(rpk_entry.extent * SECTOR + entry.offset)
            evd = parse(source.read(entry.size))
            for row in evd.dialogues:
                locked = int(not row.text.strip() or row.text.lstrip().startswith("#"))
                db.execute(
                    """INSERT INTO dialogues(event_file,entry_index,text_id,speaker_id,original,
                       original_bytes,locked) VALUES(?,?,?,?,?,?,?)""",
                    (entry.name, row.index, row.text_id, row.name_id, row.text, row.encoded_length, locked),
                )
            if progress:
                progress(event_number, len(events), entry.name)
    ensure_executable_texts(db, executable)
    _set_meta(db, "iso_path", str(iso_path.resolve()))
    _set_meta(db, "executable_extent", executable_entry.extent)
    _set_meta(db, "rpk_extent", rpk_entry.extent)
    _set_meta(db, "rpk_size", rpk_entry.size)
    _set_meta(db, "iso_size", iso_path.stat().st_size)
    _set_meta(db, "executable_sha256", hashlib.sha256(executable).hexdigest())
    _set_meta(db, "format", 2)
    db.commit()
    count = db.execute("SELECT COUNT(*) FROM dialogues").fetchone()[0]
    db.close()
    return count


def encoded_size(text: str) -> int | None:
    try:
        return len(encode_game_text(text))
    except UnicodeEncodeError:
        return None


def project_stats(db: sqlite3.Connection) -> dict[str, int]:
    row = db.execute(
        """SELECT
        COUNT(*) AS total,
        COALESCE(SUM(locked=0),0) AS eligible,
        COALESCE(SUM(locked=1),0) AS protected,
        COALESCE(SUM(locked=0 AND length(trim(reviewed))>0 AND review_status='approved'),0) AS reviewed,
        COALESCE(SUM(locked=0 AND length(trim(reviewed))>0 AND review_status<>'approved'),0) AS review_drafts,
        COALESCE(SUM(locked=0 AND (length(trim(automatic))>0 OR length(trim(translation))>0)),0) AS translated,
        COALESCE(SUM(
            locked=0 AND (length(trim(automatic))>0 OR length(trim(translation))>0 OR length(trim(reviewed))>0)
            AND size_ok=1 AND error=''
        ),0) AS correct,
        COALESCE(SUM(
            locked=0 AND (length(trim(automatic))>0 OR length(trim(translation))>0 OR length(trim(reviewed))>0)
            AND error<>''
        ),0) AS errors,
        COALESCE(SUM(
            locked=0 AND (length(trim(automatic))>0 OR length(trim(translation))>0 OR length(trim(reviewed))>0)
            AND size_ok=0 AND error=''
        ),0) AS oversized,
        COALESCE(SUM(
            locked=0 AND length(trim(automatic))=0 AND length(trim(translation))=0 AND length(trim(reviewed))=0
        ),0) AS pending
        FROM dialogues"""
    ).fetchone()
    return {key: int(row[key]) for key in row.keys()}


def backup_project(db: sqlite3.Connection, project_path: Path, label: str) -> Path:
    from datetime import datetime

    backup_dir = project_path.parent / "backups" / project_path.stem
    backup_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination = backup_dir / f"{project_path.stem}_{label}_{timestamp}.atproj"
    target = sqlite3.connect(destination)
    try:
        db.backup(target)
    finally:
        target.close()
    return destination


def clear_all_translations(db: sqlite3.Connection) -> dict[str, int]:
    before = db.execute(
        """SELECT
        COALESCE(SUM(length(trim(automatic))>0),0),
        COALESCE(SUM(length(trim(translation))>0),0),
        COALESCE(SUM(length(trim(reviewed))>0),0)
        FROM dialogues"""
    ).fetchone()
    db.execute(
        """UPDATE dialogues SET
        automatic='', translation='', reviewed='', translated_bytes=0, size_ok=1,
        provider='', error='', review_status='unreviewed', review_origin='',
        reviewed_at='', reviewed_hash=''"""
    )
    db.commit()
    return {"automatic": int(before[0]), "translation": int(before[1]), "reviewed": int(before[2])}


def save_text(
    db: sqlite3.Connection,
    row_id: int,
    translation: str,
    reviewed: str,
    commit: bool = True,
) -> None:
    row = db.execute(
        "SELECT original_bytes,reviewed,review_status,review_origin,reviewed_at,reviewed_hash "
        "FROM dialogues WHERE id=?", (row_id,)
    ).fetchone()
    if row is None:
        raise ValueError(f"Linha inexistente: {row_id}")
    size = encoded_size(reviewed or translation) if (reviewed or translation) else 0
    ok = int(size is not None and (not size or size <= row[0]))
    error = "" if size is not None else "Caractere não suportado pela codificação do jogo"
    changed_final = reviewed != row["reviewed"]
    if not reviewed.strip():
        review_status, review_origin, reviewed_at, reviewed_hash = "unreviewed", "", "", ""
    elif changed_final:
        review_status, review_origin, reviewed_at, reviewed_hash = "draft", "", "", ""
    else:
        review_status = row["review_status"]
        review_origin = row["review_origin"]
        reviewed_at = row["reviewed_at"]
        reviewed_hash = row["reviewed_hash"]
    db.execute(
        "UPDATE dialogues SET translation=?,reviewed=?,translated_bytes=?,size_ok=?,error=?,"
        "review_status=?,review_origin=?,reviewed_at=?,reviewed_hash=? WHERE id=?",
        (translation, reviewed, size or 0, ok, error, review_status, review_origin,
         reviewed_at, reviewed_hash, row_id),
    )
    if commit:
        db.commit()


def text_digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def mark_reviewed(
    db: sqlite3.Connection,
    row_id: int,
    translation: str,
    reviewed: str,
    origin: str = "usuario",
) -> None:
    if not reviewed.strip():
        raise ValueError("Preencha o texto final antes de marcar como revisado")
    if encoded_size(reviewed) is None:
        raise ValueError("O texto final contém caractere não suportado pelo jogo")
    save_text(db, row_id, translation, reviewed, commit=False)
    db.execute(
        "UPDATE dialogues SET review_status='approved',review_origin=?,reviewed_at=?,reviewed_hash=? "
        "WHERE id=?",
        (origin, datetime.now(timezone.utc).isoformat(timespec="seconds"), text_digest(reviewed), row_id),
    )
    db.commit()


def approved_review(row) -> str | None:
    reviewed = row["reviewed"]
    if row["review_status"] != "approved" or not reviewed.strip():
        return None
    if row["reviewed_hash"] != text_digest(reviewed):
        raise ValueError(
            f"A revisão aprovada de {row['event_file']}:{row['entry_index']} foi alterada sem nova aprovação"
        )
    return reviewed


def select_final_text(row, mode: str = "automatic_fallback") -> tuple[str, str]:
    if row["locked"]:
        return row["original"], "original"
    reviewed = approved_review(row)
    if reviewed is not None:
        return reviewed, "reviewed"
    if mode == "automatic_fallback" and row["automatic"].strip():
        automatic = row["automatic"]
        if encoded_size(automatic) is not None:
            from .quality import GAME_COMMAND_PATTERN

            if GAME_COMMAND_PATTERN.findall(automatic) == GAME_COMMAND_PATTERN.findall(row["original"]):
                return automatic, "automatic"
    return row["original"], "original"


def planned_iso_counts(db: sqlite3.Connection) -> dict[str, int]:
    counts = {"reviewed": 0, "automatic": 0, "original": 0, "oversized": 0, "drafts": 0}
    for row in db.execute("SELECT * FROM dialogues ORDER BY id"):
        value, source = select_final_text(row)
        counts[source] += 1
        if row["reviewed"].strip() and row["review_status"] != "approved":
            counts["drafts"] += 1
        if source != "original" and (size := encoded_size(value)) is not None:
            counts["oversized"] += int(size > row["original_bytes"])
    return counts

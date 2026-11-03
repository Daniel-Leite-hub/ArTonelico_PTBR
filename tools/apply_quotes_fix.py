import hashlib
import os
import shutil
import sqlite3
import sys
from datetime import datetime

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.evd import encode_game_text


def convert_straight_quotes(text: str) -> str:
    if not text:
        return text
    chars = list(text)
    # First pass: double quotes
    for i, ch in enumerate(chars):
        if ch == '"':
            prev_ch = chars[i - 1] if i > 0 else "^"
            next_ch = chars[i + 1] if i + 1 < len(chars) else "$"
            after_cr = (i >= 2 and text[i - 2 : i] == "CR")
            if after_cr or prev_ch in "^ \t([{<:–—" or (prev_ch in ".!?" and next_ch.isalnum()):
                chars[i] = "“"
            else:
                chars[i] = "”"
    # Second pass: single quotes and apostrophes
    for i, ch in enumerate(chars):
        if ch == "'":
            prev_ch = chars[i - 1] if i > 0 else "^"
            next_ch = chars[i + 1] if i + 1 < len(chars) else "$"
            after_cr = (i >= 2 and text[i - 2 : i] == "CR")
            if prev_ch.isalnum() and next_ch.isalnum():
                chars[i] = "’"
            elif after_cr or prev_ch in "^ \t([{<:–—“" or (prev_ch in ".!?" and next_ch.isalnum()):
                chars[i] = "‘"
            else:
                chars[i] = "’"
    return "".join(chars)


def main():
    db_path = 'Ferramentas_Traducao/release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
    backup_dir = 'Ferramentas_Traducao/backups/curadoria'
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'ArTonelico_backup_pre_fix_quotes_{ts}.atproj')
    
    print(f"1. Criando backup do banco em {backup_path}...")
    shutil.copyfile(db_path, backup_path)
    print("   Backup concluído.")

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Query all rows with quotes in reviewed or translation
    c.execute(
        "SELECT id, event_file, entry_index, reviewed, translation, original_bytes, review_status, reviewed_hash "
        "FROM dialogues WHERE reviewed LIKE '%\"%' OR reviewed LIKE \"%'%\" OR translation LIKE '%\"%' OR translation LIKE \"%'%\""
    )
    rows = c.fetchall()
    print(f"2. Linhas identificadas para higienização de aspas: {len(rows)}")

    updated_reviewed = 0
    updated_translation = 0

    for r in rows:
        row_id, ev_file, entry_idx, reviewed, translation, orig_bytes, status, cur_hash = r
        new_reviewed = reviewed
        new_trans = translation
        changed_rev = False
        changed_trans = False

        if reviewed and ('"' in reviewed or "'" in reviewed):
            new_reviewed = convert_straight_quotes(reviewed)
            changed_rev = True
            updated_reviewed += 1

        if translation and ('"' in translation or "'" in translation):
            new_trans = convert_straight_quotes(translation)
            changed_trans = True
            updated_translation += 1

        if changed_rev or changed_trans:
            # Recompute translated_bytes and size_ok for the final text
            final_text = new_reviewed if (new_reviewed and new_reviewed.strip()) else new_trans
            new_bytes = len(encode_game_text(final_text))
            new_size_ok = 1 if (orig_bytes == 0 or new_bytes <= orig_bytes) else 0

            # Recompute reviewed_hash if reviewed was changed and approved
            if changed_rev and status == 'approved':
                new_hash = hashlib.sha256(new_reviewed.encode('utf-8')).hexdigest()
            else:
                new_hash = cur_hash

            c.execute(
                "UPDATE dialogues SET reviewed=?, translation=?, translated_bytes=?, size_ok=?, reviewed_hash=? WHERE id=?",
                (new_reviewed, new_trans, new_bytes, new_size_ok, new_hash, row_id)
            )

    conn.commit()
    print(f"3. Atualização concluída no SQLite:")
    print(f"   - Linhas em 'reviewed' atualizadas: {updated_reviewed}")
    print(f"   - Linhas em 'translation' atualizadas: {updated_translation}")

    # Sanity verification
    c.execute("SELECT count(*) FROM dialogues WHERE reviewed LIKE '%\"%' OR reviewed LIKE \"%'%\"")
    rem_rev = c.fetchone()[0]
    c.execute("SELECT count(*) FROM dialogues WHERE translation LIKE '%\"%' OR translation LIKE \"%'%\"")
    rem_trans = c.fetchone()[0]
    print(f"4. Verificação pós-aplicação:")
    print(f"   - Restantes em 'reviewed': {rem_rev}")
    print(f"   - Restantes em 'translation': {rem_trans}")

    # Inspect our two target IDs from user's screenshots: ID 15056 and ID 15082
    c.execute("SELECT id, event_file, entry_index, reviewed FROM dialogues WHERE id IN (15056, 15082)")
    print("\n5. Inspeção das duas falas mostradas pelo usuário:")
    for row in c.fetchall():
        print(f"   ID {row[0]} | {row[1]}[{row[2]}]:")
        print(f"     {repr(row[3])}")
        enc = encode_game_text(row[3])
        print(f"     Encoded hex slice around Purger: {enc[enc.find(b'Purger')-4 : enc.find(b'Purger')+10].hex(' ')}")
        print(f"     Gaiji byte 0xEEFC in output: {b'\xee\xfc' in enc}")

    conn.close()


if __name__ == '__main__':
    main()

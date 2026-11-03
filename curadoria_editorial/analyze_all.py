import sqlite3
import json
import sys
sys.path.insert(0, r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

db_path = r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\release\ArTonelico_PTBR_adaptado_108_20260926.atproj'
conn = sqlite3.connect(db_path)
c = conn.cursor()

def check_file(event_file):
    print(f"=== Event File: {event_file} ===")
    c.execute("SELECT id, entry_index, speaker_id, original_jp, original, original_bytes, automatic, reviewed FROM dialogues WHERE event_file = ? ORDER BY id ASC", (event_file,))
    for row in c.fetchall():
        d_id, e_idx, spk, jp, en, ob, auto, rev = row
        cur = rev if rev else auto
        enc = encoded_size(cur) if cur else 0
        diff = enc - ob if enc else 0
        status = f"OVERFLOW (+{diff}B)" if (enc and enc > ob) else f"OK ({enc}B <= {ob}B)"
        print(f"ID {d_id} (idx:{e_idx}) | OB:{ob} | {status} | JP: {jp} | EN: {en} | Cur: {cur}")

def search_term(pattern):
    print(f"=== Search: {pattern} ===")
    c.execute("SELECT id, event_file, original_jp, original, original_bytes, reviewed, automatic FROM dialogues WHERE original_jp LIKE ? OR original LIKE ? LIMIT 40", (f"%{pattern}%", f"%{pattern}%"))
    for r in c.fetchall():
        d_id, ef, jp, en, ob, rev, auto = r
        cur = rev if rev else auto
        enc = encoded_size(cur) if cur else 0
        print(f"ID {d_id} [{ef}] | OB:{ob} | {enc}B | JP: {jp} | EN: {en} | PT: {cur}")

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--search':
        search_term(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1].startswith('SLUS'):
        check_file(sys.argv[1])
    else:
        for i in range(76, 89):
            ef = f"SLUS/TEXT/00{i:02d}"
            check_file(ef)


def show_prev_highlights():
    import glob
    for p in sorted(glob.glob(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_SYS_*_output.json")):
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        bid = d.get('block_id')
        for h in d.get('highlights', []):
            reason = h.get('reason', '')
            if '<=' in reason or 'elimina estouro' in reason:
                print(f"[{bid}] ID {h.get('id')}: '{h.get('before')}' -> '{h.get('after')}' | {reason}")


def match_enemies():
    print("=== Matching BLK_SYS_007 against DB ===")
    c.execute("SELECT id, original_jp, original, original_bytes, automatic, reviewed FROM dialogues WHERE id BETWEEN 22221 AND 22340 ORDER BY id ASC")
    block_enemies = c.fetchall()
    for row in block_enemies:
        d_id, jp, en, ob, auto, rev = row
        c.execute("SELECT id, event_file, original_bytes, automatic, reviewed FROM dialogues WHERE original_jp = ? AND id NOT BETWEEN 22221 AND 22340 ORDER BY id ASC", (jp,))
        matches = c.fetchall()
        match_str = ""
        if matches:
            m = matches[0]
            m_text = m[4] if m[4] else m[3]
            m_enc = encoded_size(m_text) if m_text else 0
            match_str = f"--> MATCH in {m[1]} (ID {m[0]}): '{m_text}' (OB:{m[2]}, {m_enc}B)"
        else:
            match_str = "--> NO MATCH"
        cur = rev if rev else auto
        enc = encoded_size(cur) if cur else 0
        status = f"OVERFLOW (+{enc - ob}B)" if (enc and enc > ob) else f"OK ({enc}B <= {ob}B)"
        print(f"ID {d_id} | OB:{ob} | {status} | JP: {jp} | EN: {en} | Cur: '{cur}' {match_str}")

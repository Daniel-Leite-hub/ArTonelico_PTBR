import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from pathlib import Path
from artonelico_tool.project import connect, select_final_text
from artonelico_tool.executable_text import EXECUTABLE_TEXT_PREFIX, executable_slot_capacity
from artonelico_tool.evd import encode_game_text
from artonelico_tool.string_relocation import plan_string_moves
from artonelico_tool.text_arena import arena_layout
from artonelico_tool.iso import find, read_entry
from artonelico_tool.patcher import selected_replacements

ROOT = Path('Ferramentas_Traducao')
db = connect(ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
iso_path = Path("G:/JOGO/PS2/Ar tonelico - Melody of Elemia (Undub)/Ar tonelico - Melody of Elemia (Undub).iso")

executable_entry = find(iso_path, "SLUS_214.45")
executable = bytearray(read_entry(iso_path, executable_entry))
original_executable = bytes(executable)

arena_file_offset, _ = arena_layout(original_executable)

executable_groups = [
    row[0]
    for row in db.execute(
        "SELECT DISTINCT event_file FROM dialogues WHERE event_file LIKE ? ORDER BY event_file",
        (EXECUTABLE_TEXT_PREFIX + "%",),
    )
]

outgoing = {}
for group in executable_groups:
    chosen, _, _ = selected_replacements(db, group, "native-menu-font")
    outgoing.update({offset: encode_game_text(value) for offset, value in chosen.items()})

string_moves, string_blocked = plan_string_moves(original_executable, outgoing, arena_offset=arena_file_offset)
moved = {m.source: m for m in string_moves}

overflows = []
for event_file in executable_groups:
    replacements, event_counts, sources = selected_replacements(db, event_file, "native-menu-font")
    for offset, value in list(replacements.items()):
        row = db.execute(
            "SELECT id, original, automatic, reviewed, original_bytes FROM dialogues WHERE event_file=? AND entry_index=?",
            (event_file, offset),
        ).fetchone()
        encoded = encode_game_text(value)
        capacity = executable_slot_capacity(executable, offset, row["original_bytes"])
        if offset in moved:
            continue
        if len(encoded) > capacity:
            overflows.append({
                "id": row["id"],
                "event_file": event_file,
                "offset": hex(offset),
                "original": row["original"],
                "reviewed": row["reviewed"],
                "automatic": row["automatic"],
                "source": sources.get(offset),
                "capacity": capacity,
                "len_encoded": len(encoded)
            })

print(f"Total de overflows em slots fixos do executável: {len(overflows)}")
for o in overflows:
    print(f"ID {o['id']} | {o['event_file']}:{o['offset']} | cap {o['capacity']} vs len {o['len_encoded']} | src: {o['source']}")
    print(f"  Orig: {repr(o['original'])}")
    print(f"  Rev:  {repr(o['reviewed'])}")
    print(f"  Auto: {repr(o['automatic'])}\n")

db.close()

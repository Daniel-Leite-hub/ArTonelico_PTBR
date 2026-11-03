import sys
sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import connect
from artonelico_tool.patcher import selected_replacements
from artonelico_tool.evd import parse, build
from pathlib import Path

ROOT = Path('Ferramentas_Traducao')
db = connect(ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj')

found = []
for path in (ROOT / 'work/extracted/Event').glob('*.evd'):
    evd = parse(path.read_bytes())
    replacements, _, _ = selected_replacements(db, 'Event/' + path.name, 'native-menu-font')
    for index, text in replacements.items():
        if '\u2014' in text:
            found.append((path.name, index, text))

print(f"Total de replacements com em-dash: {len(found)}")
for fname, index, text in found:
    print(f"{fname} [{index}]: {repr(text)}")

db.close()

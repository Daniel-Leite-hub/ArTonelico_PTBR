"""Build a new curated test ISO without overwriting any previous image."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from artonelico_tool.patcher import build_iso

if __name__ == '__main__':
    target = ROOT / 'isos_teste/ArTonelico_PTBR_revisado_20261006.iso'
    target.parent.mkdir(exist_ok=True)
    if target.exists():
        raise FileExistsError(f'Preserve existing ISO: {target}')
    result = build_iso(
        ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj',
        target, 'native-menu-font', relocate=True,
        relocate_strings=True, expand_text_arena=True,
        progress=lambda *args: print(*args, flush=True),
    )
    summary = {k: v for k, v in result.items() if k != 'capacity_fallbacks'}
    target.with_suffix('.build.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps(summary, ensure_ascii=True, indent=2), flush=True)

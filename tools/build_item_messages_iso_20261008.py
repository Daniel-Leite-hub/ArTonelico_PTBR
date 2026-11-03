"""Build a separate test image with ASCII item-acquisition substitutions."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from artonelico_tool.patcher import build_iso

if __name__ == '__main__':
    target = ROOT / 'release/iso/ArTonelico_PTBR_mensagens_itens_20261008.iso'
    if target.exists():
        raise FileExistsError(target)
    result = build_iso(
        ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj',
        target, 'native-menu-font', relocate=True,
        relocate_strings=True, expand_text_arena=True,
        progress=lambda n, total, name: print(n, total, name, flush=True) if n % 200 == 0 else None,
    )
    assert result['lines'] == result['verified_lines'] == 32641
    assert result['capacity_fallback_count'] == 0
    summary = {k: v for k, v in result.items() if k != 'capacity_fallbacks'}
    target.with_suffix('.build.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps(summary, ensure_ascii=True, indent=2), flush=True)

"""Controlled comparison: no ELF string relocation and no extra text arena."""
from pathlib import Path
import hashlib
import json
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from artonelico_tool.patcher import build_iso
from artonelico_tool.iso import find, read_entry
from artonelico_tool.text_arena import HEAP_HI, HEAP_LO, HEAP_POINTER


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


if __name__ == '__main__':
    target = ROOT / 'isos_teste/ArTonelico_PTBR_diagnostico_sem_arena_20261008.iso'
    project = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
    source = ROOT / 'Ar tonelico - Melody of Elemia (Undub).iso'
    if target.exists():
        raise FileExistsError(f'Preserve existing ISO: {target}')
    before = {str(p): digest(p) for p in (source, project)}
    result = build_iso(project, target, 'native-menu-font', relocate=True,
                       relocate_strings=False, expand_text_arena=False)
    original = read_entry(source, find(source, 'SLUS_214.45'))
    rebuilt = read_entry(target, find(target, 'SLUS_214.45'))
    assert len(original) == len(rebuilt), 'Executable expanded unexpectedly'
    assert original[52:116] == rebuilt[52:116], 'ELF load headers changed'
    assert struct.unpack_from('<H', rebuilt, 44)[0] == 1
    for offset in (HEAP_HI, HEAP_LO, HEAP_POINTER):
        assert original[offset:offset+4] == rebuilt[offset:offset+4], offset
    assert result['relocated_strings'] == 0 and not result['text_arena']
    assert all(digest(Path(p)) == h for p, h in before.items()), 'Protected input changed'
    summary = {k: v for k, v in result.items() if k != 'capacity_fallbacks'}
    summary['diagnostic_checks'] = {
        'original_heap_preserved': True, 'original_elf_load_headers_preserved': True,
        'executable_original_size': True, 'inputs_unchanged': True,
        'runtime_validated': False,
    }
    target.with_suffix('.build.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps(summary, ensure_ascii=True, indent=2), flush=True)

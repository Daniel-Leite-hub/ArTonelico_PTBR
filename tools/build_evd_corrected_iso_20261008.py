"""Rebuild full translations and audit native EVD traversal, old vs new."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from artonelico_tool.evd import parse, validate_runtime_layout
from artonelico_tool.iso import find, read_entry, SECTOR
from artonelico_tool.patcher import build_iso
from artonelico_tool.rpk import read_index


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def audit_iso(path, label):
    rpk = find(path, 'RPK.BIN')
    elf = read_entry(path, find(path, 'SLUS_214.45'))
    # Preserve each extracted binary as audit evidence, never touch the original.
    elf_path = ROOT / 'work/evd_padding_20261008' / (label + '.elf')
    elf_path.parent.mkdir(exist_ok=True)
    elf_path.write_bytes(elf)
    failures, offsets, count = {}, {}, 0
    with path.open('rb') as stream:
        for entry in read_index(elf_path, rpk.size):
            if not entry.name.endswith('.evd'):
                continue
            reference = parse((ROOT / 'work/extracted' / entry.name).read_bytes())
            stream.seek(rpk.extent * SECTOR + entry.offset)
            payload = stream.read(entry.size)
            try:
                offsets[entry.name] = validate_runtime_layout(payload, reference)
            except ValueError as exc:
                failures[entry.name] = str(exc)
            count += 1
    return {'events': count, 'valid': count - len(failures),
            'failures': failures, 'script_offsets': offsets}


if __name__ == '__main__':
    target = ROOT / 'release/iso/ArTonelico_PTBR_EVD_corrigido_20261008.iso'
    project = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
    source = ROOT / 'Ar tonelico - Melody of Elemia (Undub).iso'
    if target.exists():
        raise FileExistsError(f'Preserve existing ISO: {target}')
    before = {str(p): digest(p) for p in (source, project)}
    old_image = ROOT / 'isos_teste/ArTonelico_PTBR_diagnostico_sem_arena_20261008.iso'
    if old_image.exists():
        old = audit_iso(old_image, 'old')
    else:
        evidence = ROOT / 'relatorios/testes/evd_padding_20261008.build.json'
        old = json.loads(evidence.read_text(encoding='utf8'))['native_layout_audit']['old']
    assert 'Event/5.evd' in old['failures'], 'Expected old post-prologue regression'
    print(f"Old image: {len(old['failures'])}/{old['events']} invalid EVD layouts", flush=True)
    result = build_iso(project, target, 'native-menu-font', relocate=True,
                       relocate_strings=True, expand_text_arena=True,
                       progress=lambda n, total, name: print(n, total, name, flush=True) if n % 100 == 0 else None)
    new = audit_iso(target, 'corrected')
    assert new['events'] == 976 and not new['failures'], new['failures']
    assert result['capacity_fallback_count'] == 0
    assert result['lines'] == result['verified_lines'] == 32641
    assert all(digest(Path(p)) == h for p, h in before.items()), 'Protected input changed'
    summary = {k: v for k, v in result.items() if k != 'capacity_fallbacks'}
    summary.update(inputs_unchanged=True, input_sha256=before,
                   runtime_validated=False, native_layout_audit={'old': old, 'corrected': new})
    target.with_suffix('.build.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps({k: v for k, v in summary.items() if k != 'native_layout_audit'}, ensure_ascii=True, indent=2), flush=True)

"""Generate the final curated complete localization ISO for Ar tonelico (Undub)."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from artonelico_tool.patcher import build_iso

if __name__ == '__main__':
    project = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
    output_dir = ROOT.parent / 'ISOs' if ROOT.name == 'Ferramentas_Traducao' else ROOT / 'ISOs'
    output_dir.mkdir(exist_ok=True)
    target = output_dir / 'ArTonelico_PTBR_completo_curado_20261101.iso'
    
    if target.exists():
        print(f"Alvo {target} já existe. Removendo versão antiga para reconstrução limpa...")
        target.unlink()
    
    with project.open('rb') as stream:
        before = hashlib.file_digest(stream, 'sha256').hexdigest()
    
    print("Iniciando reconstrução completa da ISO com a Curadoria Editorial 100%...")
    result = build_iso(
        project, target, 'native-menu-font', relocate=True,
        relocate_strings=True, expand_text_arena=True,
        progress=lambda n, total, name: print(f"[{n}/{total}] Processando {name}...", flush=True) if n % 200 == 0 or n == total else None
    )
    
    print("\nVerificando integridade da compilação...")
    assert result['lines'] == result['verified_lines'] == 32641, f"Mismatch nas linhas: {result['lines']} vs {result['verified_lines']}"
    assert result['capacity_fallback_count'] == 0, f"Fallbacks de capacidade encontrados: {result['capacity_fallback_count']}"
    
    with project.open('rb') as stream:
        assert hashlib.file_digest(stream, 'sha256').hexdigest() == before, "Banco de dados foi alterado durante o build!"
        
    summary = {k: v for k, v in result.items() if k != 'capacity_fallbacks'}
    summary['project_unchanged'] = True
    summary['project_sha256'] = before
    
    target.with_suffix('.build.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf8')
    print("\n[SUCESSO] ISO Final Curada gerada com perfeição absoluta!")
    print(json.dumps(summary, ensure_ascii=True, indent=2), flush=True)

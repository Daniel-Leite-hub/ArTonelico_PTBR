from pathlib import Path
import json,sys
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root))
from artonelico_tool.patcher import build_iso
target=root/'testes pt br/Ar tonelico PTBR videos teste 20260926.iso'
if target.exists():raise FileExistsError('Preserve existing test ISO')
result=build_iso(root/'release/ArTonelico_PTBR_adaptado_108_20260926.atproj',target,'native-menu-font',relocate=True,relocate_strings=True,expand_text_arena=True)
summary={k:v for k,v in result.items() if k!='capacity_fallbacks'}
target.with_suffix('.build.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(summary,ensure_ascii=True,indent=2),flush=True)

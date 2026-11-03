from pathlib import Path
import sys, struct, json, collections
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.patcher import build_iso
from artonelico_tool.iso import find,read_entry

root=Path(__file__).resolve().parents[1]
p=root/'testes pt br/Ar tonelico PTBR bancos de conversa expandidos v2 20260926.iso'
r=build_iso(root/'release/ArTonelico_PTBR.atproj',p,'native-menu-font',relocate=True,relocate_strings=True)
a=(root/'work/SLUS_214.45').read_bytes();b=read_entry(p,find(p,'SLUS_214.45'))
so=struct.unpack_from('<I',a,32)[0];size,count=struct.unpack_from('<HH',a,46)
for i in range(count):
    s=struct.unpack_from('<10I',a,so+i*size)
    if s[2]&4:
        assert a[s[4]:s[4]+s[5]]==b[s[4]:s[4]+s[5]]
assert a[:0x1000]==b[:0x1000]
assert a[0x97be30:0x97c230]==b[0x97be30:0x97c230]
report=json.loads(p.with_suffix('.string_relocation.json').read_text(encoding='utf8'))
intervals=sorted(set((m['destination'],m['destination']+m['bytes']) for m in report['moves']))
assert all(end<=nxt for (_,end),(nxt,_) in zip(intervals,intervals[1:]))
ptrs={q for m in report['moves'] for q in m['pointers']}
for m in report['moves']:
    for q in m['pointers']:
        for delta in (-20,-16,-12,-8,-4):
            if q+delta not in ptrs:
                assert a[q+delta:q+delta+4]==b[q+delta:q+delta+4]
summary={k:v for k,v in r.items() if k!='capacity_fallbacks'}
summary['blocked_reasons']=dict(collections.Counter(report['blocked'].values()))
summary['shared_copies']=sum(m.get('shared',False) for m in report['moves'])
summary['code_headers_active_table_record_fields_audit']=True
summary['in_game_validated']=False
p.with_suffix('.audit.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(summary,ensure_ascii=True,indent=2))

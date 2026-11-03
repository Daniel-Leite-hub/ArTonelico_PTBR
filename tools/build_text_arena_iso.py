"""Build experimental expanded bank and perform structural, not runtime, QA."""
from pathlib import Path
import sys,struct,json,collections
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.patcher import build_iso
from artonelico_tool.iso import find,read_entry
from artonelico_tool.text_arena import HEAP_HI,HEAP_LO,HEAP_POINTER

root=Path(__file__).resolve().parents[1]
p=root/(sys.argv[1] if len(sys.argv)>1 else 'testes pt br/Ar tonelico PTBR banco adicional experimental 20260926.iso')
if p.exists():raise ValueError('ISO existente preservada: escolha outro nome')
r=build_iso(root/'release/ArTonelico_PTBR.atproj',p,'native-menu-font',relocate=True,
            relocate_strings=True,expand_text_arena=True)
a=(root/'work/SLUS_214.45').read_bytes();b=read_entry(p,find(p,'SLUS_214.45'))
manifest=json.loads(p.with_suffix('.string_relocation.json').read_text(encoding='utf8'))
so=struct.unpack_from('<I',a,32)[0];ss,count=struct.unpack_from('<HH',a,46)
expected=bytearray(a)
expected[HEAP_HI:HEAP_HI+4]=b[HEAP_HI:HEAP_HI+4]
expected[HEAP_LO:HEAP_LO+4]=b[HEAP_LO:HEAP_LO+4]
instruction_patches=[HEAP_HI,HEAP_LO]
for m in manifest['moves']:
    for pair in m.get('instruction_pairs',[]):
        for pos in (pair['hi'],pair['lo']):
            assert a[pos+2:pos+4]==b[pos+2:pos+4]
            expected[pos:pos+4]=b[pos:pos+4]
            instruction_patches.append(pos)
        hi,lo=struct.unpack_from('<2I',b,pair['hi']);low=lo&65535
        value=((hi&65535)<<16)|low if pair['ori'] else ((hi&65535)<<16)+(low if low<32768 else low-65536)
        assert value==m['destination_address']
for i in range(count):
    s=struct.unpack_from('<10I',a,so+i*ss)
    if s[2]&4:assert expected[s[4]:s[4]+s[5]]==b[s[4]:s[4]+s[5]]
assert a[52:84]==b[52:84]  # original PT_LOAD + BSS unchanged
assert a[0x1134:0x1140]==b[0x1134:0x1140]  # BSS clear stop unchanged
assert a[0x97be30:0x97c230]==b[0x97be30:0x97c230]
arena=manifest['arena'];ph=struct.unpack_from('<8I',b,84)
assert ph==(1,arena['file_offset'],arena['virtual_address'],arena['virtual_address'],
            arena['capacity_bytes'],arena['capacity_bytes'],4,4096)
assert struct.unpack_from('<I',b,HEAP_POINTER)[0]==arena['heap_new_start']
intervals=sorted(set((m['destination'],m['destination']+m['bytes']) for m in manifest['moves']))
assert all(end<=nxt for (_,end),(nxt,_) in zip(intervals,intervals[1:]))
ptrs={p for m in manifest['moves'] for p in m['pointers']}
for m in manifest['moves']:
    # Every moved original is retained, including padding up to next text start.
    end=a.index(b'\0',m['source'])+1
    assert a[m['source']:end]==b[m['source']:end]
    assert arena['file_offset']<=m['destination']<arena['file_offset']+arena['capacity_bytes']
    for pos in m['pointers']:
        for delta in (-20,-16,-12,-8,-4):
            if pos+delta not in ptrs:
                assert a[pos+delta:pos+delta+4]==b[pos+delta:pos+delta+4]
summary={k:v for k,v in r.items() if k!='capacity_fallbacks'}
summary['blocked_reasons']=dict(collections.Counter(manifest['blocked'].values()))
summary['instruction_patches']=instruction_patches
summary['original_sources_bss_jump_table_audit']=True
summary['runtime_validated']=False
p.with_suffix('.arena_audit.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(summary,ensure_ascii=True,indent=2))

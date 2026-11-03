"""Scene-focused allocator test; does not change the default EXE policy."""
from pathlib import Path
import sys,struct,json,zipfile,hashlib,sqlite3
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.patcher import build_iso,selected_replacements
from artonelico_tool.iso import find,read_entry
from artonelico_tool.evd import encode_game_text

root=Path(__file__).resolve().parents[1]
targets=(0x8a39b8,0x8a3a38,0x8a3ab0,0x8a3ae8)
state=Path('C:/Users/Daniel/Documents/PCSX2/sstates/SLUS-21445 (3C231DE5).01.p2s')
a=(root/'work/SLUS_214.45').read_bytes()
with zipfile.ZipFile(state) as z:
    memory=z.read('eeMemory.bin')
state_digest=hashlib.sha256(state.read_bytes()).hexdigest()
evidence=[]
for off in targets:
    va=off+0xff000
    needle=struct.pack('<I',va)
    refs=[p for p in range(0,len(a)-3,4) if a[p:p+4]==needle]
    assert len(refs)==1
    p=refs[0]
    assert memory[p+0xff000:p+0xff000+4]==needle
    assert memory[va:va+48]==a[off:off+48]
    evidence.append({'source':off,'virtual_address':va,'pointer_file':p,
                     'pointer_ram':p+0xff000,'snapshot_pointer_matches':True,
                     'metadata_original':struct.unpack_from('<5I',a,p-20),
                     'metadata_snapshot':struct.unpack_from('<5I',memory,p+0xff000-20)})
p=root/'testes pt br/Ar tonelico PTBR cena Firefly textos completos 20260926.iso'
r=build_iso(root/'release/ArTonelico_PTBR.atproj',p,'native-menu-font',relocate=True,
            relocate_strings=True,string_priority=targets)
b=read_entry(p,find(p,'SLUS_214.45'))
manifest=json.loads(p.with_suffix('.string_relocation.json').read_text(encoding='utf8'))
moves={m['source']:m for m in manifest['moves']}
c=sqlite3.connect(root/'release/ArTonelico_PTBR.atproj');c.row_factory=sqlite3.Row
for row in evidence:
    off=row['source'];assert off in moves
    record=c.execute('select event_file,original,original_bytes from dialogues where entry_index=? and event_file like ?',
                     (off,'SLUS/TEXT/%')).fetchone()
    chosen,_,_=selected_replacements(c,record['event_file'],'native-menu-font')
    payload=encode_game_text(chosen[off]);m=moves[off]
    assert b[m['destination']:m['destination']+len(payload)]==payload
    assert b[off:off+record['original_bytes']]==a[off:off+record['original_bytes']]
    row.update({'original':record['original'],'binary_selected_text':chosen[off],
                'translated_bytes':len(payload),'destination':m['destination']})
so=struct.unpack_from('<I',a,32)[0];size,count=struct.unpack_from('<HH',a,46)
for i in range(count):
    s=struct.unpack_from('<10I',a,so+i*size)
    if s[2]&4:assert a[s[4]:s[4]+s[5]]==b[s[4]:s[4]+s[5]]
assert a[:0x1000]==b[:0x1000]
assert a[0x97be30:0x97c230]==b[0x97be30:0x97c230]
assert hashlib.sha256(state.read_bytes()).hexdigest()==state_digest
summary={k:v for k,v in r.items() if k!='capacity_fallbacks'}
summary.update({'scene':evidence,'original_savestate_sha256':state_digest,
    'scene_in_game_validated':False,'allocator_priority_only':True,
    'warning':'Other translations may fall back: this is not a global capacity fix.'})
p.with_suffix('.scene_audit.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in summary.items() if k!='scene'},ensure_ascii=True,indent=2))

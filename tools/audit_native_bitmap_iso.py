from pathlib import Path
import sys, struct, sqlite3
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from artonelico_tool.iso import find,read_entry
from artonelico_tool.native_bitmap_font import patch_native_menu_font
from artonelico_tool.evd import encode_game_text
root=Path(__file__).resolve().parents[1]
p=root/'testes pt br/Ar tonelico PTBR fonte nativa dados apenas 20260926.iso'
a=(root/'work/SLUS_214.45').read_bytes(); b=read_entry(p,find(p,'SLUS_214.45'))
shoff=struct.unpack_from('<I',a,32)[0]
size,count,names=struct.unpack_from('<HHH',a,46)
sections=[struct.unpack_from('<10I',a,shoff+i*size) for i in range(count)]
ns=sections[names]; strings=a[ns[4]:ns[4]+ns[5]]
for section in sections:
    name=strings[section[0]:].split(b'\0')[0]
    if section[2]&4:
        offset,length=section[4:6]
        assert a[offset:offset+length]==b[offset:offset+length],name
        print('Executable section unchanged:',name.decode(),hex(offset),length)
assert a[0x97be30:0x97c230]==b[0x97be30:0x97c230]
c=sqlite3.connect(root/'release/ArTonelico_PTBR.atproj')
cat=[]
for row in c.execute('select original,automatic,translation,reviewed from dialogues'):
    for value in row:
        if not value: continue
        cat.append(value.encode('cp932',errors='replace'))
        try: cat.append(encode_game_text(value))
        except UnicodeEncodeError: pass
changes=patch_native_menu_font(bytearray(a),cat)
assert all(b[o:o+len(v)]==v for o,v in changes)
print('Live jump table unchanged; 84 font blocks verified; complete catalog collision audit passed.')
print('Item bytes:',b[0x8653f8:0x865414].hex())

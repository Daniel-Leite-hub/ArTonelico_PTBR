from pathlib import Path
import struct
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
data = (root / 'work/SLUS_214.45').read_bytes()
mapping = data[0x547cf0:0x547cf0+810]
out = Image.new('RGB', (500, 100), '#182030')
draw = ImageDraw.Draw(out)
for j, c in enumerate('aeio uAEIOUç'.replace(' ', '')):
    if c == 'ç':
        continue
    code = chr(ord(c)+0xfee0).encode('cp932')
    index = next(i for i in range(405) if mapping[2*i:2*i+2] == code)
    raw = data[0x548020+index*288:0x548020+(index+1)*288]
    pixels = [n*17 for b in raw for n in (b&15,b>>4)]
    im = Image.new('L',(24,24)); im.putdata(pixels)
    draw.text((j*45,0),c,fill='white')
    out.paste(im.resize((48,48)),(j*45,20))
    print(c,index,im.getbbox(),data[0x490a0e+index*2:0x490a10+index*2].hex())
out.save(root/'work/fonts/native_body_specimen.png')

import sys
sys.path.insert(0,str(root))
from artonelico_tool.native_bitmap_font import make_glyph
from artonelico_tool.native_menu_font import NATIVE_MENU_CODES
import unicodedata
out = Image.new('RGB',(14*100,2*125),'#182030')
draw = ImageDraw.Draw(out)
for j,c in enumerate(NATIVE_MENU_CODES):
    base = {'ª':'a','º':'o'}.get(c,unicodedata.normalize('NFD',c)[0])
    code = chr(ord(base)+0xfee0).encode('cp932')
    index = next(i for i in range(405) if mapping[2*i:2*i+2]==code)
    x,y = (j%14)*100,(j//14)*125
    draw.text((x,y),c,fill='white')
    out.paste(make_glyph(data,c,index).resize((96,96)),(x,y+20))
out.save(root/'work/fonts/native_portuguese_specimen.png')

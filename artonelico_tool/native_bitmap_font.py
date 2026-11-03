"""Data-only extension of the original 24x24, 4-bit menu font."""
import unicodedata
from PIL import Image, ImageDraw
from .native_menu_font import NATIVE_MENU_CODES

MAP = 0x547CF0
BANK = 0x548020
METRICS = 0x490A0E
SLOTS = (233,234,242,243,244,245,246,247,248,250,251,252,253,254,
         255,256,257,258,259,260,262,264,265,278,267,275,279,274)
# Slot 268 is the left curly quote (CP932 8165), used by reviewed dialogue.
# Preserve it; slot 275 (CP932 816C) is unused in the current catalog.
# The collision guard below remains mandatory for this replacement as well.

def read_glyph(data, index):
    raw = data[BANK+index*288:BANK+(index+1)*288]
    im = Image.new('L', (24,24))
    im.putdata([n*17 for b in raw for n in (b&15,b>>4)])
    return im

def make_glyph(data, character, base_index):
    im = read_glyph(data, base_index)
    if character in 'ªº':
        small = im.crop(im.getbbox()).resize((9,10), Image.Resampling.LANCZOS)
        im = Image.new('L',(24,24)); im.paste(small,(7,2))
        return im
    mark = unicodedata.normalize('NFD',character)[1:]
    if character.isupper() and mark != '\u0327':
        body = im.crop((0,1,24,22)).resize((24,17),Image.Resampling.LANCZOS)
        im = Image.new('L',(24,24)); im.paste(body,(0,5))
    elif character == 'í':
        ImageDraw.Draw(im).rectangle((0,0,23,5),fill=0)
    draw = ImageDraw.Draw(im)
    if mark == '\u0301': draw.line((10,3,14,0),fill=255,width=2)
    elif mark == '\u0300': draw.line((9,0,13,3),fill=255,width=2)
    elif mark == '\u0302': draw.line((8,3,11,0,14,3),fill=255,width=2)
    elif mark == '\u0303': draw.line((7,3,9,1,12,3,15,1),fill=255,width=2)
    elif mark == '\u0308':
        draw.rectangle((8,1,9,2),fill=255); draw.rectangle((14,1,15,2),fill=255)
    elif mark == '\u0327': draw.line((12,21,11,23,8,23),fill=255,width=1)
    return im

def patch_native_menu_font(executable, catalog):
    original = bytes(executable)
    mapping = original[MAP:MAP+810]
    # Reject collisions before mutation, including translated catalog strings.
    for index in SLOTS:
        old = mapping[index*2:index*2+2]
        if any(old in value for value in catalog):
            raise ValueError(f'Entrada da fonte {index} ainda usada no catálogo')
    changes = []
    for (character, code), slot in zip(NATIVE_MENU_CODES.items(), SLOTS, strict=True):
        base = unicodedata.normalize('NFD',character)[0]
        if character in 'ªº': base = {'ª':'a','º':'o'}[character]
        base_code = chr(ord(base)+0xFEE0).encode('cp932')
        index = next(i for i in range(405) if mapping[i*2:i*2+2] == base_code)
        im = make_glyph(original,character,index)
        pixels = [min(15,(p+8)//17) for p in im.getdata()]
        raw = bytes(pixels[i] | pixels[i+1]<<4 for i in range(0,576,2))
        changes.extend(((MAP+slot*2,code),(BANK+slot*288,raw),
                        (METRICS+slot*2,original[METRICS+index*2:METRICS+index*2+2])))
    for offset,value in changes: executable[offset:offset+len(value)] = value
    return changes

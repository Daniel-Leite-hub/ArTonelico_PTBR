"""Repack RPK in index order and relocate the ISO file, without code injection."""
import struct
from .iso import SECTOR, list_files

def plan_rpk(entries, original_size, modifications):
    changed = {offset:(payload,capacity) for offset,payload,capacity in modifications}
    plans=[]; cursor=0
    for i,entry in enumerate(entries):
        end=entries[i+1].offset if i+1<len(entries) else original_size
        old_capacity=end-entry.offset
        payload=changed.get(entry.offset,(None,0))[0]
        capacity=max(old_capacity, ((len(payload)+SECTOR-1)//SECTOR)*SECTOR if payload is not None else 0)
        plans.append((entry,cursor,capacity,payload,old_capacity))
        cursor+=capacity
    return plans,cursor

def move_iso_file_record(path, entry, extent, size):
    # Resolve the exact ISO9660 directory record, including both endian fields.
    dirs=[item for item in list_files(path) if item.is_dir]
    with path.open('r+b') as fp:
        fp.seek(16*SECTOR+156); root=fp.read(34)
        ranges=[(struct.unpack_from('<I',root,2)[0],struct.unpack_from('<I',root,10)[0])]
        ranges.extend((d.extent,d.size) for d in dirs)
        matches=[]
        for sector,length in ranges:
            fp.seek(sector*SECTOR); data=fp.read(length); pos=0
            while pos<len(data):
                n=data[pos]
                if not n: pos=(pos//SECTOR+1)*SECTOR; continue
                record=data[pos:pos+n]
                if (struct.unpack_from('<I',record,2)[0]==entry.extent
                    and struct.unpack_from('<I',record,10)[0]==entry.size
                    and record[33:33+record[32]].split(b';')[0]==entry.path.rsplit('/',1)[-1].encode('ascii')):
                    matches.append(sector*SECTOR+pos)
                pos+=n
        if len(matches)!=1: raise ValueError(f'Registro ISO de {entry.path} ambíguo')
        fp.seek(matches[0]+2); fp.write(struct.pack('<I',extent)+struct.pack('>I',extent))
        fp.seek(matches[0]+10); fp.write(struct.pack('<I',size)+struct.pack('>I',size))
        sectors=(path.stat().st_size+SECTOR-1)//SECTOR
        for sector in range(16,64):
            fp.seek(sector*SECTOR); header=fp.read(7)
            if header[1:6]!=b'CD001' or header[0]==255: break
            if header[0] in (1,2):
                fp.seek(sector*SECTOR+80)
                fp.write(struct.pack('<I',sectors)+struct.pack('>I',sectors))

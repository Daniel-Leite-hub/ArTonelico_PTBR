"""Read-only PCSX2 save-state evidence capture; never loads or modifies states."""
from pathlib import Path
import hashlib
import json
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'work/falha_prologo_20261008'
STATES = Path('C:/Users/Daniel/Documents/PCSX2/sstates')

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    for suffix, label in (('.p2s', 'falha'), ('.p2s.backup', 'antes')):
        source = STATES / ('SLUS-21445 (D6EBF965).01'+suffix)
        with zipfile.ZipFile(source) as z:
            memory = z.read('eeMemory.bin')
            internals = z.read('PCSX2 Internal Structures.dat')
            (OUT / (label+'.png')).write_bytes(z.read('Screenshot.png'))
            (OUT / (label+'_structures.bin')).write_bytes(internals)
            (OUT / (label+'_eeMemory.bin')).write_bytes(memory)
        summary = {'source':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                   'code_at_failure':[[hex(i),hex(struct.unpack_from('<I',memory,i)[0])]
                                      for i in range(0x1961c0,0x196280,4)]}
        (OUT / (label+'.json')).write_text(json.dumps(summary,indent=2),encoding='utf8')
    log = Path('C:/Users/Daniel/Documents/PCSX2/logs/emulog.txt')
    (OUT/'emulog.txt').write_bytes(log.read_bytes())
    print(OUT)

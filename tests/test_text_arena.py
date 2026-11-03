import struct
import unittest
from artonelico_tool.text_arena import arena_layout,install_arena,OLD_END,HEAP_POINTER,HEAP_HI,HEAP_LO
from artonelico_tool.string_relocation import Move


def specimen():
    b=bytearray(HEAP_POINTER+32)
    b[:6]=b'\x7fELF\x01\x01'
    struct.pack_into('<I',b,28,52)
    struct.pack_into('<HH',b,42,32,1)
    struct.pack_into('<8I',b,52,1,4096,0x100000,0x100000,len(b)-4096,OLD_END-0x100000,7,4096)
    guards={HEAP_HI:0x3C0400D4,HEAP_LO:0x24844AFA,HEAP_POINTER:OLD_END,
        0x11F4:0x2403003D,0x11F8:12,0x1134:0x3C0300D4,0x113C:0x24634AFA,
        0x246428:0x8E425C64,0x24642C:0x8E425C64}
    for pos,val in guards.items():struct.pack_into('<I',b,pos,val)
    return bytes(b)


class ArenaTests(unittest.TestCase):
    def test_load_and_heap_reservation_without_extending_bss_clear(self):
        old=specimen();off,va=arena_layout(old);b=bytearray(old)
        info=install_arena(b,old,[Move(0x400,off,b'test\0',())])
        self.assertEqual(struct.unpack_from('<H',b,44)[0],2)
        ph=struct.unpack_from('<8I',b,84)
        self.assertEqual(ph,(1,off,va,va,4096,4096,4,4096))
        self.assertEqual(struct.unpack_from('<I',b,HEAP_POINTER)[0],va+4096)
        hi=struct.unpack_from('<I',b,HEAP_HI)[0]&65535
        lo=struct.unpack_from('<I',b,HEAP_LO)[0]&65535
        self.assertEqual((hi<<16)+(lo if lo<32768 else lo-65536),va+4096)
        self.assertEqual(b[0x1134:0x1140],old[0x1134:0x1140])
        self.assertLess(info['heap_reserved_bytes'],1024*1024)

    def test_oversized_bank_fails_before_mutation(self):
        old=specimen();off,_=arena_layout(old);b=bytearray(old)
        with self.assertRaises(ValueError):install_arena(b,old,[Move(0x400,off+1024*1024,b'x\0',())])
        self.assertEqual(bytes(b),old)

    def test_unknown_heap_initialization_is_rejected(self):
        old=bytearray(specimen());old[HEAP_POINTER]=0
        with self.assertRaises(ValueError):arena_layout(bytes(old))

    def test_original_program_segment_is_preserved(self):
        old=specimen();off,_=arena_layout(old);b=bytearray(old)
        install_arena(b,old,[Move(0x400,off,b'x\0',())])
        self.assertEqual(b[52:84],old[52:84])

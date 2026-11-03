import struct,unittest
from artonelico_tool.mips_text_reference import adjacent_address_pairs,rewrite_pair


def specimen(ori=False):
    b=bytearray(64)
    struct.pack_into('<2I',b,8,0x3c080094,0x35081234 if ori else 0x25081234)
    sections=[(0,1,6,0x100000,0,len(b),0,0,4,0)]
    return b,sections


class MipsReferenceTests(unittest.TestCase):
    def test_nonallocated_executable_overlay_is_excluded(self):
        b,s=specimen();s[0]=(*s[0][:2],5,*s[0][3:])
        self.assertFalse(adjacent_address_pairs(b,s))

    def test_signed_low_half_and_opcodes_are_preserved(self):
        b,s=specimen();p=adjacent_address_pairs(b,s)[0x941234][0]
        rewrite_pair(b,p,0xe1f123)
        hi,lo=struct.unpack_from('<2I',b,8)
        self.assertEqual(hi,0x3c0800e2)
        self.assertEqual(lo,0x2508f123)

    def test_ori_uses_unsigned_low_half(self):
        b,s=specimen(True);p=adjacent_address_pairs(b,s)[0x941234][0]
        rewrite_pair(b,p,0xe1f123)
        self.assertEqual(struct.unpack_from('<2I',b,8),(0x3c0800e1,0x3508f123))

    def test_branch_into_low_half_is_rejected(self):
        b,s=specimen();struct.pack_into('<I',b,32,0x1000fffa) # PC+4 - 24 -> low VA +12
        self.assertFalse(adjacent_address_pairs(b,s))

    def test_delay_slot_pair_is_rejected(self):
        b,s=specimen();struct.pack_into('<I',b,4,0x08040010)
        self.assertFalse(adjacent_address_pairs(b,s))

    def test_shared_base_register_is_not_rewritten(self):
        b,s=specimen();struct.pack_into('<I',b,12,0x25041234)
        self.assertFalse(adjacent_address_pairs(b,s))

    def test_changed_pair_is_rejected(self):
        b,s=specimen();p=adjacent_address_pairs(b,s)[0x941234][0]
        b[8]=1;before=bytes(b)
        with self.assertRaises(ValueError):rewrite_pair(b,p,0xe1f123)
        self.assertEqual(bytes(b),before)

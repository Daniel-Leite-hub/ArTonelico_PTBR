import struct
import unittest
from types import SimpleNamespace
from artonelico_tool.evd import encode_game_text
from artonelico_tool.string_relocation import plan_string_moves, apply_string_moves
from artonelico_tool.string_relocation import misha_record_reference, MISHA_POINTER, MISHA_SOURCE


def specimen():
    data = bytearray(0x1000)
    data[:6] = b'\x7fELF\x01\x01'
    struct.pack_into('<I', data, 28, 0x40)
    struct.pack_into('<I', data, 32, 0x80)
    struct.pack_into('<HH', data, 42, 32, 1)
    struct.pack_into('<HH', data, 46, 40, 2)
    struct.pack_into('<8I', data, 0x40, 1, 0, 0x100000, 0x100000, len(data), len(data), 7, 16)
    struct.pack_into('<10I', data, 0x80, 0, 1, 6, 0x100200, 0x200, 0x40, 0, 0, 4, 0)
    struct.pack_into('<10I', data, 0xa8, 0, 1, 2, 0x100300, 0x300, 0x900, 0, 0, 4, 0)
    for offset, text in ((0x400, 'A very long donor sentence here'), (0x480, 'Short'), (0x500, 'Another sentence')):
        raw = encode_game_text(text)
        data[offset:offset+len(raw)] = raw
    struct.pack_into('<3I', data, 0x300, 0x100400, 0x100480, 0x100500)
    selected = {0x400: encode_game_text('Tiny'), 0x480: encode_game_text('A longer replacement')}
    return bytes(data), selected


class StringRelocationTests(unittest.TestCase):
    def test_arena_copies_full_text_without_tail_limit(self):
        original, _=specimen()
        payload=encode_game_text('A translation far longer than the original and any available tiny slot')
        moves,blocked=plan_string_moves(original,{0x480:payload},arena_offset=0x2000)
        self.assertFalse(blocked)
        self.assertEqual(moves[0].destination,0x2000)
        self.assertEqual(moves[0].payload,payload)

    def test_arena_recognizes_repeated_pointer_field(self):
        original,_=specimen();data=bytearray(original)
        data[0x300:0x310]=b'\0'*16
        for pos,va in ((0x320,0x100400),(0x360,0x100480),(0x3a0,0x100500)):
            struct.pack_into('<I',data,pos,va)
        chosen={0x480:encode_game_text('A longer replacement')}
        moves,blocked=plan_string_moves(bytes(data),chosen,arena_offset=0x2000)
        self.assertFalse(blocked)
        self.assertEqual(moves[0].pointers,(0x360,))

    def test_arena_does_not_relocate_unknown_isolated_pointer(self):
        original,_=specimen();data=bytearray(original)
        data[0x300:0x310]=b'\0'*16
        struct.pack_into('<I',data,0x360,0x100480)
        moves,blocked=plan_string_moves(bytes(data),{0x480:encode_game_text('A longer replacement')},arena_offset=0x2000)
        self.assertFalse(moves)
        self.assertEqual(blocked[0x480],'references_not_proven')

    def test_priority_selects_scene_without_relaxing_reference_gate(self):
        original, _ = specimen()
        chosen={0x400:encode_game_text('Tiny'),0x480:encode_game_text('A longer replacement'),
                0x500:encode_game_text('Another replacement is longer')}
        moves,blocked=plan_string_moves(original,chosen,priority=(0x500,))
        self.assertEqual([m.source for m in moves],[0x500])
        self.assertEqual(blocked[0x480],'no_verified_tail_capacity')
        data=bytearray(original)
        struct.pack_into('<I',data,0x200,(15<<26)|(8<<16)|0x10)
        moves,blocked=plan_string_moves(bytes(data),chosen,priority=(0x500,))
        self.assertFalse(moves)
        self.assertEqual(blocked[0x500],'instruction_address_page')

    def test_identical_full_translation_shares_existing_copy(self):
        original, _ = specimen()
        payload = encode_game_text('A longer replacement')
        selected = {0x400: payload, 0x480: payload}
        moves, blocked = plan_string_moves(original, selected)
        self.assertFalse(blocked)
        self.assertEqual(len(moves),1)
        self.assertTrue(moves[0].shared)
        self.assertEqual(moves[0].destination,0x400)
        self.assertEqual(moves[0].payload,payload)

    def test_structured_conversation_table(self):
        original, selected = specimen()
        data = bytearray(original)
        data[0x300:0x310] = b'\0'*16
        for pos, target in ((0x330,0x100400),(0x348,0x100480),(0x360,0x100500)):
            struct.pack_into('<6I',data,pos-20,3,1,0,0,65535,target)
        moves, blocked = plan_string_moves(bytes(data),selected)
        self.assertEqual(len(moves),1)
        self.assertFalse(blocked)
        self.assertEqual(moves[0].pointers,(0x348,))

    def test_invalid_record_neighbors_are_not_accepted(self):
        original, selected = specimen()
        data = bytearray(original)
        data[0x300:0x310] = b'\0'*16
        for pos, target in ((0x330,0x100400),(0x348,0x100480),(0x360,0x100500)):
            struct.pack_into('<6I',data,pos-20,99,1,0,0,65535,target)
        moves, blocked = plan_string_moves(bytes(data),selected)
        self.assertFalse(moves)
        self.assertEqual(blocked[0x480],'references_not_proven')

    def test_scoped_record_guard(self):
        data = bytearray(MISHA_POINTER+32)
        struct.pack_into('<6I', data, MISHA_POINTER-20, 3, 1, 0, 0, 65535, 0x9d3f70)
        struct.pack_into('<I', data, MISHA_POINTER-24, 0x9d3e90)
        struct.pack_into('<I', data, MISHA_POINTER+24, 0x9d3fa8)
        entries = {0x9d3e90: SimpleNamespace(text='Hey, Lyner...I’ve been waiting for you. Um...you’re not going back today, are you? Can I stay by your side...'),
                   0x9d3fa8: SimpleNamespace(text='Oh, Lyner. What’s up?')}
        self.assertTrue(misha_record_reference(bytes(data), MISHA_SOURCE, [MISHA_POINTER], entries))
        self.assertFalse(misha_record_reference(bytes(data), MISHA_SOURCE+8, [MISHA_POINTER], entries))
        self.assertFalse(misha_record_reference(bytes(data), MISHA_SOURCE, [MISHA_POINTER, 0x300], entries))
        data[MISHA_POINTER-20] = 4
        self.assertFalse(misha_record_reference(bytes(data), MISHA_SOURCE, [MISHA_POINTER], entries))

    def test_owned_tail_and_pointer_without_code_change(self):
        original, selected = specimen()
        moves, blocked = plan_string_moves(original, selected)
        self.assertEqual(len(moves), 1)
        self.assertFalse(blocked)
        result = bytearray(original)
        result[0x400:0x400+len(selected[0x400])] = selected[0x400]
        manifest = apply_string_moves(result, original, moves)
        m = moves[0]
        self.assertGreaterEqual(m.destination, 0x400+len(selected[0x400]))
        self.assertEqual(result[0x480:0x490], original[0x480:0x490])
        self.assertEqual(result[0x200:0x240], original[0x200:0x240])
        self.assertEqual(len(result), len(original))
        self.assertEqual(struct.unpack_from('<I', result, 0x304)[0], manifest[0]['destination_address'])

    def test_interior_reference_rejects_donor(self):
        original, selected = specimen()
        data = bytearray(original)
        struct.pack_into('<I', data, 0x350, 0x100410)
        moves, blocked = plan_string_moves(bytes(data), selected)
        self.assertFalse(moves)
        self.assertEqual(blocked[0x480], 'no_verified_tail_capacity')

    def test_lui_page_blocks_relocation(self):
        original, selected = specimen()
        data = bytearray(original)
        struct.pack_into('<I', data, 0x200, (15<<26)|(8<<16)|0x10)
        moves, blocked = plan_string_moves(bytes(data), selected)
        self.assertFalse(moves)
        self.assertEqual(blocked[0x480], 'instruction_address_page')

    def test_compaction_only_within_contiguous_owned_slots(self):
        original, _ = specimen()
        data = bytearray(original)
        data[0x400:0x600] = b'\0'*0x200
        a = encode_game_text('A donor with enough room')
        data[0x400:0x400+len(a)] = a
        # Leave exactly four alignment bytes between original strings.
        second = 0x400+len(a)+4
        b = encode_game_text('Short')
        data[second:second+len(b)] = b
        third = second+len(b)+4
        z = encode_game_text('Third text')
        data[third:third+len(z)] = z
        struct.pack_into('<3I', data, 0x300, 0x100400, 0x100000+second, 0x100000+third)
        selected = {0x400: encode_game_text('Tiny'), second: encode_game_text('A longer replacement'), third: z}
        moves, blocked = plan_string_moves(bytes(data), selected)
        self.assertFalse(blocked)
        self.assertGreaterEqual(len(moves), 2)
        intervals = sorted((m.destination,m.destination+len(m.payload)) for m in moves)
        self.assertTrue(all(end <= nxt for (_,end),(nxt,_) in zip(intervals,intervals[1:])))
        self.assertTrue(all(0x400 <= m.destination < third+len(z)+15 for m in moves))

    def test_changed_pointer_is_rejected_before_mutation(self):
        original, selected = specimen()
        moves, _ = plan_string_moves(original, selected)
        data = bytearray(original)
        struct.pack_into('<I', data, 0x304, 0)
        before = bytes(data)
        with self.assertRaises(ValueError):
            apply_string_moves(data, original, moves)
        self.assertEqual(bytes(data), before)

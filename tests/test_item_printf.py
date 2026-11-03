import unittest
from artonelico_tool.evd import encode_game_text
from artonelico_tool.native_menu_font import NativePrintfText

class ItemPrintfTests(unittest.TestCase):
    def test_runtime_token_is_ascii_and_fits_original_slot(self):
        result=encode_game_text(NativePrintfText('Use [%s]'))
        self.assertEqual(result,bytes.fromhex('8274829382858140816d2573816e00'))
        self.assertLessEqual(len(result),16)

    def test_normal_text_encoding_is_unchanged(self):
        self.assertNotIn(b'%s',encode_game_text('Usar [%s]'))

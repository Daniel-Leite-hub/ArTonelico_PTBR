import unittest
from artonelico_tool.evd import encode_game_text
from artonelico_tool.native_menu_font import NativePrintfText

class ItemPrintfTests(unittest.TestCase):
    def test_runtime_token_is_ascii_and_fits_original_slot(self):
        result=encode_game_text(NativePrintfText('Use [%s]'))
        self.assertEqual(result,bytes.fromhex('8274829382858140816d2573816e00'))
        self.assertLessEqual(len(result),16)

    def test_grathmeld_and_skill_runtime_tokens_are_ascii(self):
        cases = [
            ("Criar %s,", [b"%s"]),
            ("Feito %s [%s].", [b"%s", b"%s"]),
            ("Itens unidos: %s qual. [%s] x%s.", [b"%s", b"%s", b"%s"]),
            ("Vendeu o antigo por %s Leaf. Agora: qualidade %s [%s] x%s.", [b"%s", b"%s", b"%s", b"%s"]),
            ("%s aprendeu:CR%s.", [b"%s", b"%s"]),
            ("Obteve %d Cole.", [b"%d"]),
        ]
        for text, tokens in cases:
            encoded = encode_game_text(NativePrintfText(text))
            for tok in tokens:
                self.assertIn(tok, encoded, f"Token {tok} ausente no payload de {text}")

    def test_normal_text_encoding_is_unchanged(self):
        self.assertNotIn(b'%s',encode_game_text('Usar [%s]'))

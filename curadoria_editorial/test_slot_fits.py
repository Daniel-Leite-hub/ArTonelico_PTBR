import sys
sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.evd import encode_game_text
from artonelico_tool.native_menu_font import NativeMenuText

print("--- ID 20374 (Capacidade: 16 bytes) ---")
for candidate in ["Lenta", "Preguiçosa", "Inerte", "Calma", "Vagarosa", "Descansada"]:
    enc = encode_game_text(candidate)
    enc_menu = encode_game_text(NativeMenuText(candidate))
    print(f"'{candidate}': len={len(enc)}, menu_len={len(enc_menu)}")

print("\n--- ID 20384 (Capacidade: 32 bytes) ---")
for candidate in ["Magias obtidas", "Magias Obtidas", "Magias ganhas", "Magias aprendidas"]:
    enc = encode_game_text(candidate)
    enc_menu = encode_game_text(NativeMenuText(candidate))
    print(f"'{candidate}': len={len(enc)}, menu_len={len(enc_menu)}")

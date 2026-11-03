import sys
sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.evd import encode_game_text

text = '"Relatório sobre os Efeitos e Alterações\ndo Experimento de Separação de Misha..."'
enc = encode_game_text(text)
idx = enc.find(b'\x81_')
print('Index de b"\\x81_":', idx)
print('Bytes ao redor:', enc[max(0, idx-4):idx+6])

for i, ch in enumerate(text):
    try:
        c_enc = encode_game_text(ch)
        if b'\x81_' in c_enc:
            print(f"Caractere: {repr(ch)} (U+{ord(ch):04X}) em pos {i}")
    except Exception:
        pass

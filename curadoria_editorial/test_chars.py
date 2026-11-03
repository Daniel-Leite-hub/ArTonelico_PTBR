import sys
sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.evd import encode_game_text, NativeMenuText

print("Aspas duplas \" :", encode_game_text(NativeMenuText('"')))
print("Aspas simples ' :", encode_game_text(NativeMenuText("'")))
print("Colchete [ :", encode_game_text(NativeMenuText("[")))
print("Colchete ] :", encode_game_text(NativeMenuText("]")))

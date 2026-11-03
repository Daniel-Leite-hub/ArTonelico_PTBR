import sys
sys.path.insert(0, 'Ferramentas_Traducao')
import sqlite3
from artonelico_tool.evd import encode_game_text

db = sqlite3.connect('Ferramentas_Traducao/release/ArTonelico_PTBR_adaptado_108_20260926.atproj')
cur = db.cursor()
cur.execute("SELECT id, reviewed, automatic FROM dialogues WHERE id = 2465")
r = cur.fetchone()
print(f"ID {r[0]}:")
print("reviewed:", repr(r[1]))
enc = encode_game_text(r[1])
old = b'\x81_'
print(f"b'\\x81_' in enc: {old in enc}")
idx = enc.find(old)
print("idx:", idx)
print("Bytes:", enc[idx-4:idx+6])
# Que dois bytes formam 0x81 0x5F?
# 0x5F é '_' em ASCII!
# E 0x81 é o segundo byte de um caractere anterior?
print("Byte em idx:", hex(enc[idx]))
print("Byte em idx+1:", hex(enc[idx+1]), chr(enc[idx+1]))
print("Byte em idx-1:", hex(enc[idx-1]))
db.close()

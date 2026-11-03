import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

variants = [
    # 25505 (lim 120)
    (25505, 120, "Mas na Terceira Era vivi só. Sem ninguém pra confiar..."),
    (25505, 120, "Mas na Terceira Era estive só. Sem ninguém pra confiar..."),
    (25505, 120, "Na Terceira Era... estive só. Sem ninguém pra confiar..."),
    (25505, 120, "Na Terceira Era estive só. Sem ninguém em quem confiar..."),
    # 25506 (lim 168)
    (25506, 168, "No fim da Segunda Era fui traída... e na calamidade, perdi a confiança em todos..."),
    (25506, 168, "Fui traída no fim da Segunda Era... e na calamidade, deixei de confiar em todos..."),
    (25506, 168, "Traída no fim da Segunda Era... e com a calamidade, perdi a fé nas pessoas..."),
    (25506, 168, "No fim da Segunda Era fui traída... Na calamidade, perdi a fé nas pessoas..."),
    # 25510 (lim 112)
    (25510, 112, "Não aguento mais...CRViajar com você fez o fardo pesar..."),
    (25510, 112, "Não suporto mais...CRViajar com você fez o peso sufocar..."),
    (25510, 112, "Não aguento mais...CREstar com você fez esse fardo pesar..."),
    (25510, 112, "Mas não aguento mais...CREstar com você me fez ver a solidão..."),
    (25510, 112, "Não suporto mais...CREstar com você tornou esse fardo pesado..."),
    (25510, 112, "Não aguento mais...CRViajar com você tornou esse fardo insuportável..."),
    (25510, 112, "Não aguento mais...CRViajar com você fez a solidão doer mais..."),
]

for did, lim, text in variants:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

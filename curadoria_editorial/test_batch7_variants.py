import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

variants = [
    # 25473 (lim 112)
    (25473, 112, "Claro, quando quiser. Também te procuro se precisar."),
    (25473, 112, "Claro, venha sempre. Também te procuro se precisar."),
    (25473, 112, "Claro, quando quiser. Também vou até você."),
    # 25482 (lim 72)
    (25482, 72, "Fiquei feliz na hora, mas..."),
    (25482, 72, "Fiquei contente na hora, mas..."),
    (25482, 72, "Fiquei feliz pelo seu feito, mas..."),
    # 25505 (lim 120)
    (25505, 120, "Mas na Terceira Era... estive só. Não confiava em ninguém..."),
    (25505, 120, "Mas na Terceira Era... foi só solidão. Ninguém pra me abrir..."),
    (25505, 120, "Mas na Terceira Era... vivi só. Sem ninguém pra confiar..."),
    (25505, 120, "Mas na Terceira Era... foi a solidão. Sem ninguém pra confiar..."),
    (25505, 120, "Na Terceira Era... vivi na solidão. Não confiava em ninguém..."),
    # 25506 (lim 168)
    (25506, 168, "No fim da Segunda Era fui traída e houve a calamidade... Nunca mais confiei em ninguém..."),
    (25506, 168, "Traída no fim da Segunda Era... e com a calamidade, não pude mais confiar em ninguém..."),
    (25506, 168, "No fim da Segunda Era fui traída... e na calamidade, perdi a confiança em todos..."),
    (25506, 168, "Fui traída no fim da Segunda Era... e após a tragédia, nunca mais confiei nas pessoas..."),
    # 25508 (lim 96)
    (25508, 96, "Entendo...CRPor isso agia de modo tão frio."),
    (25508, 96, "Entendo...CRPor isso agia de forma tão formal."),
    (25508, 96, "Entendo...CRPor isso era tão estrita e formal."),
    (25508, 96, "Entendo...CRPor isso era tão rigorosa."),
    # 25510 (lim 112)
    (25510, 112, "Mas não aguento mais...CRViajar com você fez esse fardo pesar..."),
    (25510, 112, "Mas não aguento mais...CRViajar com você tornou o fardo pesado..."),
    (25510, 112, "Não aguento mais...CRViajar com você fez esse fardo pesar..."),
    (25510, 112, "Mas não suporto mais...CRViajar com você fez esse peso sufocar..."),
    # 25513 (lim 120)
    (25513, 120, "Obrigada...CRMas queria ficar mais perto... só mais um pouco."),
    (25513, 120, "Obrigada...CRMas quero me aproximar... só mais um pouco."),
    (25513, 120, "Obrigada... Mas queria me aproximar... só um pouco mais."),
]

for did, lim, text in variants:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

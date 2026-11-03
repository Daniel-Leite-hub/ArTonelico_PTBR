import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = [
    # 25467: lim 216
    (25467, 216, "Devemos muito à Krusche. Se qualquer um tivesse agido diferente, aquele milagre não aconteceria."),
    # 25470: lim 64
    (25470, 64, "Desculpe vir tão tarde..."),
    (25470, 64, "Desculpe pelo horário..."),
    # 25473: lim 112
    (25473, 112, "Claro, quando quiser. Também vou te procurar se tiver algo."),
    (25473, 112, "Claro, apareça quando quiser. Também vou ao seu quarto se precisar."),
    # 25475: lim 96
    (25475, 96, "D-desculpe... Se atrapalhei, avise."),
    (25475, 96, "Se for incômodo, é só me avisar."),
    # 25476: lim 168
    (25476, 168, "N-não é isso... Mas já tá tarde, vim só agradecer. Melhor eu ir pro quarto."),
    # 25480: lim 144
    (25480, 144, "Lyner, sobre você ter me reativado... não posso elogiar sua decisão."),
    (25480, 144, "Lyner, sobre ter me reativado... não posso aprovar isso."),
    # 25482: lim 72
    (25482, 72, "Fiquei feliz de ver seu crescimento, mas..."),
    (25482, 72, "Fiquei feliz com sua atitude, mas..."),
    # 25483: lim 80
    (25483, 80, "Ainda acho que me acordar foi um erro."),
    (25483, 80, "Me reativar não foi a decisão correta."),
    # 25485: lim 120
    (25485, 120, "Ainda assim, não aceito sacrifícios!"),
    (25485, 120, "Mas não aceito sacrificar ninguém!"),
    # 25487: lim 120
    (25487, 120, "Respeito sua visão, mas foi errado."),
    (25487, 120, "Entendo seu lado, mas não posso elogiar."),
    # 25488: lim 112
    (25488, 112, "Tudo bem, assumo total responsabilidade."),
    (25488, 112, "Assumo total responsabilidade pelos meus atos."),
    # 25489: lim 56
    (25489, 56, "Já passou, não adianta discutir."),
    (25489, 56, "O que passou, passou..."),
    # 25491: lim 104
    (25491, 104, "Tudo bem... Eu não devia ser tão dura."),
    (25491, 104, "Tudo bem... Não serei tão severa."),
    # 25492: lim 112
    (25492, 112, "Fiquei feliz ao ouvir que sou importante pra você."),
    (25492, 112, "Fiquei feliz quando me disse que sou importante."),
    # 25499: lim 56
    (25499, 56, "Como amigos..."),
    (25499, 56, "Como... bons amigos."),
    (25499, 56, "Falar... como bons amigos."),
    (25499, 56, "Falar com você como amigos."),
    (25499, 56, "Conversar... como amigos."),
    # 25500: lim 88
    (25500, 88, "S-Senhora Shurelia!?CRDo nada...!?"),
    (25500, 88, "S-Senhora Shurelia!?CRPor que isso agora!?"),
    # 25501: lim 88
    (25501, 88, "Lyner... OuviriaCRo que sinto agora?..."),
    (25501, 88, "Lyner... OuviriaCRmeus sentimentos?..."),
    # 25504: lim 240
    (25504, 240, "Na Primeira Era, tive alguém como um pai. Na Segunda Era, tive companheiros com quem reconstruí o mundo."),
    (25504, 240, "Na Primeira Era, eu tinha uma figura paterna. Na Segunda Era, tive companheiros valorosos para reconstruir o mundo."),
    # 25505: lim 120
    (25505, 120, "Mas na Terceira Era... estive sempre em solidão. Sem ninguém com quem me abrir..."),
    (25505, 120, "Mas na Terceira Era... estive só. Não tinha ninguém em quem confiar..."),
    (25505, 120, "Mas na Terceira Era... vivi na solidão. Não havia ninguém em quem confiar..."),
    # 25506: lim 168
    (25506, 168, "No fim da Segunda Era, fui traída e houve a grande calamidade... Desde então, deixei de confiar nas pessoas..."),
    # 25507: lim 112
    (25507, 112, "Evitei o contato humano e fiz do dever um tabu a sentimentos."),
    (25507, 112, "Evitei contato e fiz de sentimentos pessoais um tabu."),
    (25507, 112, "Evitei contato humano e proibi sentimentos pessoais."),
    # 25508: lim 96
    (25508, 96, "Entendo...CRPor isso agia de forma tão fria e formal."),
    (25508, 96, "Entendo...CRPor isso agia tão estritamente formal."),
    # 25510: lim 112
    (25510, 112, "Mas não aguento mais...CRViajar com você fez esse peso sufocar..."),
    (25510, 112, "Mas não aguento mais...CRViajar com você tornou esse fardo pesado..."),
    # 25511: lim 56
    (25511, 56, "Não quero mais ficar só..."),
    (25511, 56, "Não quero ficar sozinha..."),
    # 25512: lim 136
    (25512, 136, "Senhora Shurelia... Estarei sempre ao seu lado, não se preocupe."),
    # 25513: lim 120
    (25513, 120, "Obrigada... Mas queria me aproximar mais... só mais um pouco."),
]

for did, lim, text in tests:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

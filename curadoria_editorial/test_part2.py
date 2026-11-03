import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

candidates = [
    # 24425 (limit 48B)
    ("24425", 48, "Importância ★★★CR【Canção】"),
    ("24425", 48, "Import. ★★★CR【Canção】"),
    ("24425", 48, "Valor ★★★CR【Canção】"),
    ("24425", 48, "Importância ★★★CR【Hino】"),
    ("24425", 48, "Importância ★★★CR【Som】"),
    # 24429 (limit 56B)
    ("24429", 56, "Importância ★★★CR【Canção】【Arte】"),
    ("24429", 56, "Import. ★★★CR【Canção】【Arte】"),
    ("24429", 56, "Valor ★★★CR【Canção】【Arte】"),
    # 24430 (limit 64B)
    ("24430", 64, "Importância ★★☆CR【Loja de Músicas】"),
    ("24430", 64, "Importância ★★☆CR【Loja de Canção】"),
    ("24430", 64, "Importância ★★☆CR【Loja Canção】"),
    ("24430", 64, "Importância ★★☆CR【Loja Magia】"),
    ("24430", 64, "Import. ★★☆CR【Loja de Canções】"),
    ("24430", 64, "Import. ★★☆CR【Loja de Magias】"),
    # 24432 (limit 64B)
    ("24432", 64, "Importância ★★★CR【Música】【DP】【Arte】"),
    ("24432", 64, "Import. ★★★CR【Canção】【DP】【Arte】"),
    ("24432", 64, "Valor ★★★CR【Canção】【DP】【Arte】"),
    # 24488 (limit 48B)
    ("24488", 48, "Importância ★★☆CR【Canção】"),
    ("24488", 48, "Import. ★★☆CR【Canção】"),
    ("24488", 48, "Valor ★★☆CR【Canção】"),
    # Nomes de Locais
    ("24434", 24, "Torre Vital"),
    ("24434", 24, "Torre-Vida"),
    ("24436", 32, "Vila Crepúsculo"),
    ("24438", 32, "Vila de Aurica"),
    ("24439", 24, "Estalagem"),
    ("24439", 24, "Hospedaria"),
    ("24439", 24, "Casa Gruta"),
    ("24443", 32, "Monte Esperança"),
    ("24443", 32, "Monte da Esperança"),
    ("24447", 32, "Mansão Antiga"),
    ("24447", 32, "Mansão Velha"),
    ("24448", 32, "Castelo Soberano"),
    ("24448", 32, "Castelo do Mal"),
    ("24450", 16, "Academia"),
    ("24450", 16, "Colégio"),
    ("24450", 16, "Escola"),
    ("24451", 24, "Armaria"),
    ("24451", 24, "Armeiro"),
    ("24460", 32, "Bosque do Sono"),
    ("24460", 32, "Mata do Sono"),
    ("24461", 24, "Salão Vital"),
    ("24461", 24, "Paço Vital"),
    ("24467", 32, "Planalto Leste"),
    ("24471", 24, "Piscina"),
    # Falas de entrada e DP
    # 24475 (limit 72B)
    ("24475", 72, "Entrar custa CR%s DP.CRTem o bastante?"),
    ("24475", 72, "Requer CR%s DP paraCRentrar. Tem o bastante?"),
    ("24475", 72, "Custa CR%s DP paraCRentrar. Tem bastante?"),
    ("24475", 72, "Precisa de CR%s DP.CRTudo pronto?"),
    # 24476 (limit 120B)
    ("24476", 120, "Caramba!CRFaltam Pontos de Mergulho!CRVolte outro dia!"),
    ("24476", 120, "Gah!CRPontos de Mergulho insuficientes!CRVolte mais tarde!"),
    # 24477 (limit 72B)
    ("24477", 72, "O quê, vai voltar para a realidade?"),
    ("24477", 72, "O quê, vai voltar à realidade?"),
    # 24478 (limit 136B)
    ("24478", 136, "Você precisa de CR%s DP para entrar.CRDeseja entrar agora?"),
    ("24478", 136, "Custa CR%s DP para entrar.CRQuer entrar agora?"),
    # 24479 (limit 120B)
    ("24479", 120, "Faltam Pontos de Mergulho.CRNão posso deixar você entrar."),
    ("24479", 120, "Pontos de Mergulho insuficientes.CRNão posso te deixar entrar."),
    # 24482 (limit 120B)
    ("24482", 120, "Pontos de Mergulho insuficientes.CRUma pena, mas..."),
    ("24482", 120, "Parece que faltam Pontos de Mergulho.CRQue pena..."),
    # 24484 (limit 104B)
    ("24484", 104, "Parece que preciso de CR%s DP.CRDevo entrar?"),
    # 24485 (limit 64B)
    ("24485", 64, "Droga...CRFalta DP..."),
    ("24485", 64, "Droga...CRNão tenho DP suficiente..."),
]

for tag, lim, txt in candidates:
    sz = encoded_size(txt)
    ok = "OK" if sz <= lim else f"OVERFLOW (+{sz-lim}B)"
    print(f"[{ok:15s}] ID {tag} (lim {lim}B, cur {sz}B) -> '{txt}'")

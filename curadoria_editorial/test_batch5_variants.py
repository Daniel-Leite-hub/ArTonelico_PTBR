import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

variants = [
    (25396, 120, "Usar Tranquilidade após uma Magia forte é muito bom."),
    (25396, 120, "Tranquilidade após uma Magia forte é reconfortante."),
    (25396, 120, "Tomar Tranquilidade após uma Magia forte faz bem."),
    (25409, 120, "Lyner, não exagere nas lutas! Você está aos trapos."),
    (25409, 120, "Lyner, não se force tanto nas lutas! Tá todo ferido."),
    (25409, 120, "Lyner, não lute com tanto exagero! Tá todo ferido."),
    (25410, 88, "Desse jeito, seu corpo não aguenta."),
    (25410, 88, "Lutando assim, seu corpo não aguenta."),
    (25410, 88, "Assim seu corpo não vai aguentar."),
    (25412, 40, "S-Shurelia..."),
    (25412, 40, "Senhora Shurelia..."),
    (25412, 40, "S-Senhora..."),
    (25413, 104, "Lyner, sinto que você anda se forçando demais..."),
    (25413, 104, "Lyner, acho que está se desgastando demais..."),
    (25413, 104, "Lyner, sinto que você se esforça em excesso..."),
    (25414, 96, "Lutando desse jeito, seu corpo não aguenta."),
    (25414, 96, "Desse jeito, seu corpo não vai aguentar."),
    (25414, 96, "Lutando assim, seu corpo não suporta."),
    (25420, 64, "Não me faça me preocupar..."),
    (25420, 64, "Não me preocupe tanto..."),
    (25420, 64, "Não me deixe preocupada..."),
    (25421, 48, "Olá, Senhora Shurelia."),
    (25421, 48, "Senhora Shurelia..."),
    (25421, 48, "Olá, Senhora."),
]

for did, lim, text in variants:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

variants = [
    (25468, 48, "Você vai viver muito!"),
    (25468, 48, "Vai viver muito!"),
    (25493, 72, "Voltarei se houver algo. Até mais."),
    (25493, 72, "Se precisar, eu volto. Até mais."),
    (25493, 72, "Voltarei se algo acontecer."),
    (25494, 64, "Lyner...CRVim falar com você."),
    (25494, 64, "Lyner...CRQueria conversar."),
    (25498, 24, "Comigo..."),
    (25498, 24, "Se puder..."),
    (25498, 24, "Com você..."),
    (25502, 16, "Eu..."),
    (25502, 16, "..Eu.."),
]

for did, lim, text in variants:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

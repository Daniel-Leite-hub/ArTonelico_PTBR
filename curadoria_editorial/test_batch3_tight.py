import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = [
    (25315, 40, "Eu... sinto muito."),
    (25315, 40, "Desculpe... Falhei."),
    (25315, 40, "Perdão... Foi mal."),
    (25315, 40, "Desculpe..."),
    (25316, 80, "Vê se me protege direito!"),
    (25316, 80, "Capricha da próxima vez!"),
    (25316, 80, "Vê se capricha da próxima!"),
    (25316, 80, "Poxa! Capricha da próxima!"),
    (25317, 80, "Lyner, podemos conversar?"),
    (25317, 80, "Lyner, tem um minutinho?"),
    (25317, 80, "Lyner, tem um tempinho?"),
    (25317, 80, "Lyner, podemos bater um papo?"),
]

for did, lim, text in tests:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

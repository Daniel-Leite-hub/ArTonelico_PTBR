import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = [
    "Meu canto anda ótimo graças a você.",
    "Meu canto melhorou muito graças a você.",
    "Meu canto anda ótimo porque me dá espaço.",
    "Meu canto anda ótimo, você me apoia bem.",
]

for t in tests:
    enc = encoded_size(t)
    print(f"enc={enc} (lim 104) -> '{t}'")

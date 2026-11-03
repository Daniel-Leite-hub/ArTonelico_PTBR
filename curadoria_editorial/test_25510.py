import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = [
    "Não aguento mais...CRCom você, esse fardo pesou...",
    "Não aguento mais...CRCom você, o fardo pesou...",
    "Não suporto mais...CRCom você, o fardo pesou...",
    "Não aguento mais...CRCom você, o fardo me sufocou...",
    "Não aguento mais...CRCom você, a solidão doeu...",
    "Mas não aguento mais...CREstar com você pesou tanto...",
    "Não suporto mais...CRViajar com você pesou tanto...",
]

for t in tests:
    enc = encoded_size(t)
    diff = enc - 112
    status = "OK" if enc <= 112 else f"OVERFLOW +{diff}"
    print(f"enc={enc} [{status}] -> '{t}'")

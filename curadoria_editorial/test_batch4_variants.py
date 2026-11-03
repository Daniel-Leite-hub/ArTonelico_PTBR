import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

variants = [
    (25351, 96, "...Não ficou só olhando pro meu decote, né!?"),
    (25351, 96, "...Não ficou só encarando meu decote, né!?"),
    (25351, 96, "...Você não ficou só olhando meus seios, né!?"),
    (25369, 120, "Você é Cavaleiro de Elemia,CRtenha mais postura. Entendido?"),
    (25369, 120, "Como Cavaleiro de Elemia,CRtenha mais postura. Entendeu?"),
    (25369, 120, "Você é um Cavaleiro de Elemia,CRtenha postura. Entendido?"),
    (25374, 40, "Sim, Senhora?"),
    (25374, 40, "Pois não, Senhora?"),
    (25374, 40, "Sim, Senhora Shurelia."),
    (25374, 40, "Pois não, Shurelia?"),
    (25375, 104, "Meu canto anda ótimo. Você me dá espaço pra cantar."),
    (25375, 104, "Meu canto anda ótimo. Você me deixa livre pra cantar."),
    (25375, 104, "Meu canto anda ótimo graças ao seu suporte nas lutas."),
    (25381, 56, "Senhora Shurelia, que foi?"),
    (25381, 56, "Senhora Shurelia, o que há?"),
    (25381, 56, "O que houve, Senhora?"),
]

for did, lim, text in variants:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

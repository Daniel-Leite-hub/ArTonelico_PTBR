import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

variants = [
    (25430, 64, "Senhora Shurelia? Está feliz?"),
    (25430, 64, "Shurelia? Parece tão feliz."),
    (25430, 64, "Shurelia? Parece tão alegre."),
    (25436, 40, "Hã? Não sei."),
    (25436, 40, "Hã? Nem ideia."),
    (25438, 72, "Senhora Shurelia?CREstá feliz?"),
    (25438, 72, "Shurelia?CRParece bem disposta."),
    (25438, 72, "Shurelia?CRParece tão alegre."),
    (25440, 72, "É porque você instalou com carinho."),
    (25440, 72, "Deve ser porque instalou com carinho."),
    (25440, 72, "É porque você instalou muito bem."),
    (25449, 64, "Foi por causa da instalação?"),
    (25449, 64, "Foi culpa da minha instalação?"),
    (25456, 64, "Foi por causa da instalação?"),
    (25456, 64, "Foi culpa da minha instalação?"),
    (25458, 88, "Assim cantar é mais revigorante."),
    (25458, 88, "Assim cantar dá mais prazer, relaxe."),
    (25458, 88, "Assim sinto mais prazer ao cantar."),
    (25462, 112, "B-bem... deixa pra lá...CRNão quero incomodar..."),
    (25462, 112, "B-bem... já vou indo...CRNão quero atrapalhar..."),
    (25462, 112, "B-bem... vou pro quarto...CRNão quero atrapalhar..."),
]

for did, lim, text in variants:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

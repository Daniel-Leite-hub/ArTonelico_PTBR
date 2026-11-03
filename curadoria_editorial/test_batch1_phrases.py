import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

variants = [
    (25230, 32, "Oi, Aurica. Tudo bem?"),
    (25230, 32, "Aurica? O que há?"),
    (25230, 32, "Oi, Aurica."),
    (25230, 32, "Aurica? O que foi?"),
    (25230, 32, "Aurica? Tudo bem?"),
    (25230, 32, "E aí, Aurica?"),
    (25246, 80, "...! Peguei pesado na instalação!?"),
    (25246, 80, "...! A instalação foi pesada demais!?"),
    (25246, 80, "...! A instalação te machucou!?"),
    (25249, 64, "...Obrigada. Você é gentil..."),
    (25249, 64, "...Obrigada. Você é tão bom..."),
    (25249, 64, "...Obrigada. Você é um doce."),
    (25255, 72, "Não! Foi descuido meu não notar."),
    (25255, 72, "A culpa foi minha por não notar."),
    (25255, 72, "Não! A culpa é minha por não ver."),
    (25256, 144, "Você juntou poder e eu desperdicei... Desculpe, vou tomar cuidado."),
    (25256, 144, "Você acumulou poder e eu desperdicei... Desculpe, terei mais cuidado."),
    (25256, 144, "Você guardou tanta força e eu desperdicei... Vou ter mais cuidado.")
]

for did, lim, text in variants:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

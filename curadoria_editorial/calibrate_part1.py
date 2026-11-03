import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = [
    (32145, '...É sério?! Menos malCRnão ser no passado...', 96),
    (32145, '...É sério?! Que bomCRnão ser no passado...', 96),
    (32149, 'Quem nada sabe,CRnada teme...', 80),
    (32149, 'Dizem que ignorarCRé uma bênção...', 80),
    (32197, 'Não teorize no puro instinto!CREm termos técnicos, seria umCR"Oscilador de Pressão Diferencial".', 200),
    (32197, 'Não use puro instinto na ciência!CREm termos técnicos, seria umCR"Oscilador de Pressão Diferencial".', 200),
    (32197, 'Não improvise na alta ciência!CREm termos técnicos, seria umCR"Oscilador de Pressão Diferencial".', 200),
    (32226, 'Lyner... O que vocêCRcriou aqui?!', 64),
    (32226, 'Lyner... O que foiCRque você fez?!', 64),
    (32227, 'Hã?! É que...CRAr tonelico?', 64),
    (32227, 'Hã?! É...CRAr tonelico?', 64),
]

for d_id, s, cap in tests:
    sz = encoded_size(s)
    diff = sz - cap
    status = "OK" if diff <= 0 else f"+{diff}B"
    print(f"ID {d_id} ({sz}B / {cap}B -> {status}): {s}")

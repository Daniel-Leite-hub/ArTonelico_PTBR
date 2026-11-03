import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

variants = [
    (25308, 72, "E ainda levei um baita golpe..."),
    (25308, 72, "E acabei levando um golpe feio..."),
    (25308, 72, "Mas levei um golpe daqueles..."),
    (25309, 104, "Mentiroso! Se rolar de novo,CRnão vou te perdoar!"),
    (25309, 104, "Mentiroso! Se ocorrer de novo,CRnão te perdoo!"),
    (25311, 32, "Ué? Que foi?"),
    (25311, 32, "Hã? Que foi?"),
    (25311, 32, "Hã? O que foi?"),
    (25312, 64, "Ai, ai... Ainda dói tudo..."),
    (25312, 64, "Ai... Os golpes ainda doem..."),
    (25312, 64, "Ai, ai... O corpo ainda dói..."),
    (25315, 40, "Desculpe não te proteger."),
    (25315, 40, "Foi mal não te proteger."),
    (25315, 40, "Desculpa... Não te salvei."),
    (25315, 40, "Perdão... Não te protegi."),
    (25316, 80, "Capricha! Fora a magia,CRsomos garotas comuns..."),
    (25316, 80, "Capricha! Fora a magia,CRsomos garotas normais..."),
    (25316, 80, "Poxa! Fora a magia,CRsomos só garotas normais..."),
    (25317, 80, "Lyner...CRTem um tempinho pra conversar?"),
    (25317, 80, "Lyner, tem um minuto?CRQueria falar com você."),
    (25324, 64, "Não lute até cair em pedaços!"),
    (25324, 64, "Não lute até desabar!"),
    (25324, 64, "Não se desgaste até desabar!"),
    (25335, 128, "D-desculpa. Mas vou voltar a fazer isso, me aguente, tá?"),
    (25335, 128, "Desculpa. Mas vou fazer isso de novo, me aguente, tá?"),
    (25337, 64, "O que houve? Parece tão feliz!"),
    (25337, 64, "Que foi? Parece tão animada!"),
    (25343, 168, "Meu corpo ficou leve e meu canto tá ótimo! É vidente ou o quê!? Que demais!"),
    (25343, 168, "Corpo leve e canto impecável! Você é vidente ou o quê!? Que incrível!"),
    (25345, 152, "...A não ser que você só tenha tirado Cristais Grathnode, aí seria piada."),
    (25345, 152, "...A menos que você só tenha tirado Cristais Grathnode, aí seria piada."),
]

for did, lim, text in variants:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

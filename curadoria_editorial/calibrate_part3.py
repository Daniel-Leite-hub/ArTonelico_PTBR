import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = [
    # 32325: cap 96
    (32325, "Além de forte, qualquer umCRconsegue disparar!", 96),
    # 32327: cap 96
    (32327, "...E-então até eu mesmaCRconsigo disparar?", 96),
    # 32329: cap 168
    (32329, "E-eu queria tentar atirar uma vez...CRMas o coice me faria cair sentada.", 168),
    # 32330: cap 112
    (32330, "(Acho que ela tropeçaCRantes mesmo de atirar...)", 112),
    # 32334: cap 104
    (32334, "Acho que sim... A correnteCRimita a barbatana?", 104),
    (32334, "Creio que sim... A correnteCRlembra a barbatana?", 104),
    # 32344: cap 104
    (32344, "Isso é um problemão,CRnão um pequeno defeito!", 104),
    # 32345: cap 120
    (32345, "Em troca ela é forte e dobraCRos acertos críticos!", 120),
    # 32350: cap 104
    (32350, "Dá pra notar... O canoCRestá gigante de novo.", 104),
    # 32355: cap 48
    (32355, "...Onde é motosserra?", 48),
    # 32358: cap 128
    (32358, "Forjar a espada que vou usarCRdá uma sensação boa demais...", 128),
    # 32359: cap 112
    (32359, "Espada magnífica.CRO poder deve ser formidável.", 112),
    # 32360: cap 152
    (32360, "Nem se compara à de antes!CREstá num nível bem superior.", 152),
    # 32372: cap 112
    (32372, "...Infernal?! Nem penseiCRque me diria uma dessas...", 112),
    # 32375: cap 128
    (32375, "As asas deram trabalho,CRmas enfim posso respirar.", 128),
    # 32387: cap 56
    (32387, "Jaqueta Airmetal pronta!", 56),
    # 32388: cap 80
    (32388, "...Ficou boa? Parece bem pesada.", 80),
    # 32389: cap 192
    (32389, "Aparências enganam! Ela é feitaCRde Yuteria pura, é ultraleve!", 192),
    # 32390: cap 112
    (32390, "Pesada assim e é leve?!CRImpressionante...", 112),
    # 32391: cap 200
    (32391, "Até eu me surpreendi. Mas olhando...CRparece tão pesada que ninguémCRvai querer vestir, né?", 200),
    # 32392: cap 24
    (32392, "Concordo.", 24),
    (32392, "Pois é.", 24),
    # 32393: cap 88
    (32393, "...Podia me dar um apoio.", 88),
    (32393, "...Dá uma forcinha, poxa.", 88),
    # 32394: cap 64
    (32394, "Pronto!CRSupremo no Céu e Terra!", 64),
    (32394, "Pronto!CR\"Supremo do Universo\"!", 64),
    # 32395: cap 96
    (32395, "...Lyner, sabe o significadoCRdo que acabou de dizer?", 96),
    # 32396: cap 40
    (32396, "Claro que não sei!", 40),
    (32396, "Claro que não!", 40),
    # 32400: cap 48
    (32400, "Ceroula Marrom pronta!", 48),
    # 32405: cap 96
    (32405, "Camiseta Ardente pronta!CRVou provar agora!", 96),
    # 32410: cap 56
    (32410, "...L-Lyner... Tudo bem?", 56),
    # 32412: cap 104
    (32412, "Lyner... Acho melhor vocêCRtirar essa camiseta...", 104),
    # 32413: cap 32
    (32413, "Ah... coelha.", 32),
    # 32416: cap 96
    (32416, "...Infelizmente, a senhoraCRnão pode equipar.", 96),
    # 32417: cap 104
    (32417, "...É...? Queria tanto usarCRessas orelhinhas...", 104),
]

for d_id, s, cap in tests:
    sz = encoded_size(s)
    diff = sz - cap
    status = "OK" if diff <= 0 else f"+{diff}B"
    print(f"ID {d_id} ({sz}B / {cap}B -> {status}): {s}")

import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0291 = {
    27146: 32, 27147: 96, 27148: 112, 27149: 104, 27150: 192, 27151: 184,
    27152: 40, 27153: 120, 27154: 104, 27155: 208, 27156: 16, 27157: 136,
    27158: 104, 27159: 40, 27160: 136, 27161: 152, 27162: 96, 27163: 136,
    27164: 48, 27165: 112, 27166: 88, 27167: 112, 27168: 176, 27169: 112
}

calib_0291 = {
    27146: ("Será?...", "Lyner intrigado com a colocação de Misha. (19B <= 32B)"),
    27147: ("É sim! Ah, Lyner,CRme empresta a cabeça!", "Misha pedindo para encostar a testa com CR. (73B <= 96B)"),
    27148: ("Hã? Emprestar como?... Eita!", "Lyner sendo pego de surpresa pelo movimento de Misha. (59B <= 112B)"),
    27149: ("Não se mexe! Se bater a cabeçaCRvai doer...", "Misha advertindo para evitar batida acidental com CR. (89B <= 104B)"),
    27150: ("Mas... ficar colando a sua testaCRna minha não ajuda muito...CREu não tô com febre, sabia?", "Lyner desconcertado com a proximidade física com CRs. (178B <= 192B)"),
    27151: ("Eu sei disso! É que, fazendo isso,CRparece que consigo sentirCRo que você tá pensando...", "Misha justificando o contato íntimo pela leitura mental com CRs. (166B <= 184B)"),
    27152: ("...Dá pra saber?", "Lyner perguntando com hesitação tímida. (37B <= 40B)"),
    27153: ("Hum... Dá pra sentir que vocêCRtá supernervoso agora.", "Misha provocando com doçura e perspicácia com CR. (103B <= 120B)"),
    27154: ("...Você só tá zombando de mim,CRnão tá?", "Lyner na defensiva percebendo a provocação com CR. (77B <= 104B)"),
    27155: ("Nada disso! Eu sinto de verdadeCRquando fico coladinha assim...CRE além do mais...", "Misha justificando o carinho íntimo com CRs. (162B <= 208B)"),
    27156: ("...E?", "Lyner aguardando a continuação da confissão. (13B <= 16B)"),
    27157: ("...Não, esquece. E não se afasta!CRAinda não descobri nada.", "Misha disfarçando o constrangimento amoroso com CR. (111B <= 136B)"),
    27158: ("...Ei, Lyner.CRPosso chegar mais pertinho?", "Misha pedindo autorização tímida para se aconchegar com CR. (71B <= 104B)"),
    27159: ("Hã? É, pode ser.", "Lyner concedendo com gentileza espontânea. (33B <= 40B)"),
    27160: ("Uhum... Hehehe, fico tão felizCRde conversar assim com você.", "Misha expressando gratidão pela privacidade a dois com CR. (112B <= 136B)"),
    27161: ("É?... Bem, se só isso já te alegra,CRé o mínimo que posso fazer.", "Lyner acolhendo o afeto de Misha com humildade com CR. (127B <= 152B)"),
    27162: ("Mas a gente conversaCRsempre que quiser, né?", "Lyner sugerindo que o diálogo pode ser constante com CR. (90B <= 96B)"),
    27163: ("Mas aí é com todos em volta!CRÉ bem diferente de nós dois.", "Misha demarcando a exclusividade da intimidade com CR. (121B <= 136B)"),
    27164: ("É? O que muda?", "Lyner ingênuo perguntando sobre a diferença prática. (31B <= 48B)"),
    27165: ("Hmm... Tipo ficar agarradinhaCRassim em você?", "Misha demonstrando fisicamente o dengo com CR. (91B <= 112B)"),
    27166: ("Ei, você grudou de verdade?!", "Lyner reagindo chocado e corado ao abraço repentino. (63B <= 88B)"),
    27167: ("Hehehe, não dá pra fazerCRisso na frente dos outros!", "Misha rindo triunfante da ousadia em segredo com CR. (107B <= 112B)"),
    27168: ("Até dava, mas aí Aurica e ShureliaCRvirariam minhas inimigas na hora.", "Misha citando com humor o ciúme das companheiras com CR. (135B <= 176B)"),
    27169: ("I-Inimigas?... Vocês não se dãoCRbem por acaso?", "Lyner temendo conflitos entre as heroínas com CR. (87B <= 112B)")
}

all_ok = True
for tid, (txt, rat) in calib_0291.items():
    maxb = max_map_0291[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        errs = validate_line(tid, "", txt)
        if errs:
            all_ok = False
            print(f"ERRO VALIDACAO ID {tid}: {errs} -> {txt}")
        else:
            print(f"OK ID {tid}: {sz}B <= {maxb}B")

if all_ok:
    print("=== 0291 100% PERFEITO ===")

import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0277 = {
    26810: 88, 26811: 56, 26812: 136, 26813: 48, 26814: 128, 26815: 192,
    26816: 192, 26817: 128, 26818: 128, 26819: 112, 26820: 128, 26821: 112,
    26822: 48, 26823: 112, 26824: 128, 26825: 80, 26826: 32, 26827: 224,
    26828: 200, 26829: 40, 26830: 192, 26831: 64, 26832: 48, 26833: 128
}

calib_0277 = {
    26810: ("Vou tentar usar o quanto antes...", "Lyner prometendo usar a viga de metal logo."),
    26811: ("Ah, tanto faz isso aí.", "Misha desdenhando a urgência."),
    26812: ("Mas se for pra usar viga de aço,CRqueria que fizesse uma casa...", "Misha sugerindo a construção de um lar conjugal com CR."),
    26813: ("Uma casa?! Pra quê?", "Lyner surpreso com o pedido inusitado."),
    26814: ("Base de aço é bem mais seguraCRque de madeira. Dá outra paz.", "Misha justificando a estabilidade da casa com CR."),
    26815: ("E quero uma casa espaçosa!CRCom o tempo, a gente pode... sabe...CRaumentar a família...", "Misha corando ao insinuar filhos e futuro a dois com quebras CR."),
    26816: ("Não entendi nada desse papo,CRmas quem sabe quando eu melhorarCRno Grathmeld e tiver tempo.", "Lyner denso prometendo tentar a síntese no futuro com quebras CR."),
    26817: ("Nunca pensei que você veria aCRCrônica Crescente um dia.", "Misha mencionando a Crônica Crescente com quebra CR."),
    26818: ("E logo aquela sala onde eu ficava...CRFiquei até com vergonha.", "Misha constrangida por ter sua antiga câmara revelada com CR."),
    26819: ("Hã? Mas por que teria vergonhaCRdisso?", "Lyner sem entender o constrangimento de Misha com CR."),
    26820: ("Porque aquele lugar era tipoCRo meu lar, minha terra natal.", "Misha explicando o vínculo afetivo com sua câmara na Torre com CR."),
    26821: ("Vivia trancada lá dentro...CRou melhor, só cantando.", "Misha relembrando o isolamento forçado cantando Magias da Canção com CR."),
    26822: ("Ah... é verdade.", "Lyner se compadecendo do passado de Misha."),
    26823: ("Mas é um lugar pro qualCRnão quero voltar nunca mais.", "Misha rejeitando reviver o confinamento doloroso com CR."),
    26824: ("Sabe a camiseta do Funbun queCRvocê comprou em Platina...?", "Misha puxando o assunto cômico da vestimenta com CR."),
    26825: ("Não me diz que...CRv-vai usar aquilo?", "Misha incrédula com o gosto de vestimenta de Lyner com CR."),
    26826: ("Que foi agora?", "Lyner na defensiva sobre a camiseta."),
    26827: ("Gostar de Funbun é uma coisa,CRmas querer vestir camiseta de pãozinhoCRjá é passar dos limites!", "Misha achando ridículo estampar o pãozinho na roupa com quebras CR."),
    26828: ("Aquilo tem toda a cara de lembrancinhaCRque a gente compra no impulsoCRe nunca usa na vida!", "Misha ridicularizando o suvenir inútil com quebras CR."),
    26829: ("...Não posso negar.", "Lyner admitindo que é verdade."),
    26830: ("Até que é uma camiseta boa,CRmas admito que não tenho coragemCRde sair na rua com aquilo.", "Lyner admitindo a vergonha de desfilar com a estampa com quebras CR."),
    26831: ("...Ou seja, querCRvestir, né?", "Misha flagrando a vontade oculta de Lyner com CR."),
    26832: ("Ei, você tá bem?", "Misha preocupada com o estado físico de Lyner."),
    26833: ("Você me protegeu daquele golpeCRoutro dia... Doeu muito, né?", "Misha perguntando pelo golpe sofrido em combate com CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0277.items():
    maxb = max_map_0277[tid]
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
    print("=== 0277 100% PERFEITO ===")

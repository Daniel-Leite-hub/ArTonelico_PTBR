import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0289 = {
    27098: 96, 27099: 152, 27100: 96, 27101: 88, 27102: 136, 27103: 88,
    27104: 88, 27105: 192, 27106: 120, 27107: 224, 27108: 80, 27109: 152,
    27110: 96, 27111: 56, 27112: 32, 27113: 64, 27114: 176, 27115: 112,
    27116: 112, 27117: 72, 27118: 88, 27119: 96, 27120: 160, 27121: 216
}

calib_0289 = {
    27098: ("Minha visão sobre magiaCRtá desmoronando...", "Lyner perplexo com o pragmatismo cômico das canções com CR. (89B <= 96B)"),
    27099: ("Fico tão feliz de ver que ficoCRmais forte a cada Mergulho seu!", "Misha comemorando a evolução mágica com termo canônico e CR. (128B <= 152B)"),
    27100: ("Essa Canção TrovoadaCRfoi sensacional!", "Misha elogiando Shippu Jinrai / Canção Trovoada com CR. (77B <= 96B)"),
    27101: ("Como ela me ajuda,CRtambém fico feliz!", "Lyner agradecendo a proteção em combate com CR. (78B <= 88B)"),
    27102: ("Mas... esses nomes de magiaCRnão podiam ser menos sinistros?", "Lyner implicando com os nomes extravagantes com CR. (122B <= 136B)"),
    27103: ("Como assim?!CRÉ superestiloso!", "Misha defendendo a estética épica com CR. (62B <= 88B)"),
    27104: ("Se você diz...CRpor mim tudo bem...", "Lyner cedendo sem contra-argumentar com CR. (72B <= 88B)"),
    27105: ("Ficamos tantos anos longe e você me esqueceu...CRNão sou tão útil assim pra você?", "Misha expressando insegurança de não ser suficiente para Lyner com CR. (168B <= 192B)"),
    27106: ("Hã?! Que ideia! Pelo contrário,CRvocê me ajuda direto!", "Lyner rebatendo enfaticamente a insegurança de Misha com CR. (112B <= 120B)"),
    27107: ("...Mas você mergulha mais na menteCRde Shurelia, mesmo ela tendo chegado depois,CRe vocês tão superíntimos...", "Misha com ciúmes da intimidade recente com Shurelia com CRs. (223B <= 224B)"),
    27108: ("...É isso!CRNão vou ficar pra trás!!", "Misha reagindo com determinação competitiva com CR. (76B <= 80B)"),
    27109: ("Lyner! Pode mergulhar com tudoCRna minha mente, sem cerimônia!", "Misha autorizando mergulhos profundos sem hesitação com CR. (126B <= 152B)"),
    27110: ("Nem acredito que elaCRte deixou mergulhar nela.", "Misha espantada com a permissão concedida por Shurelia com CR. (95B <= 96B)"),
    27111: ("Ela confia muito em você.", "Misha constatando a enorme confiança mútua. (52B <= 56B)"),
    27112: ("Hã? S-Será?...", "Lyner tímido e reticente. (31B <= 32B)"),
    27113: ("Tá corando por quê?!CRAff!!", "Misha implicando com o rubor de Lyner com CR. (57B <= 64B)"),
    27114: ("Mas não me esqueça! Pode mergulharCRna minha mente quando quiser, ouviu?!", "Misha reivindicando dedicação e mergulhos com CR. (149B <= 176B)"),
    27115: ("...Isso não é meio ousadoCRpra uma Reyvateil falar?", "Lyner apontando a audácia da proposta com termo canônico e CR. (105B <= 112B)"),
    27116: ("Urgh... Puxa vida!CRNão joga na cara, que vergonha...", "Misha desconcertada com vocalização original 'Urgh' fiel ao JP com CR. (108B <= 112B)"),
    27117: ("Lyner, você deviaCRvir mais cedo!", "Misha fazendo bico dengoso pela demora com CR. (68B <= 72B)"),
    27118: ("Fazer garota esperarCRpega muito mal!", "Misha ensinando etiqueta amorosa a Lyner com CR. (75B <= 88B)"),
    27119: ("Ué? Mas achei que tinhaCRvindo correndo...", "Lyner se defendendo com naturalidade com CR. (86B <= 96B)"),
    27120: ("Será?... Bem, só de você ter vindoCRjá fico feliz, então dou um desconto.", "Misha amolecendo carinhosamente com CR. (152B <= 160B)"),
    27121: ("Fiquei preocupado em como você tava...CRMas já vi que tá tudo numa boa,CRentão fico mais tranquilo.", "Lyner demonstrando afeto protetor com CRs. (203B <= 216B)")
}

all_ok = True
for tid, (txt, rat) in calib_0289.items():
    maxb = max_map_0289[tid]
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
    print("=== 0289 100% PERFEITO ===")

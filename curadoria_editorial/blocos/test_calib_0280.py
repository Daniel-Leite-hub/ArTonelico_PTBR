import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0280 = {
    26882: 232, 26883: 128, 26884: 40, 26885: 144, 26886: 88, 26887: 64,
    26888: 184, 26889: 176, 26890: 168, 26891: 168, 26892: 160, 26893: 136,
    26894: 152, 26895: 112, 26896: 208, 26897: 96, 26898: 176, 26899: 40,
    26900: 56, 26901: 120, 26902: 192, 26903: 144, 26904: 112, 26905: 128
}

calib_0280 = {
    26882: ("Passei por muito sufoco!CRUns caras estranhos ficaram me secandoCRoutro dia, fiquei com tanto medo!", "Misha relatando os olhares lascivos e o pavor que sentiu com CR."),
    26883: ("Você nem notou, mas eles ficaramCRseguindo a gente um tempão!", "Misha revelando a perseguição que sofreram com CR."),
    26884: ("É sério isso?!", "Lyner indignado com o assédio sofrido por Misha."),
    26885: ("Fica atento! Senão fico comCRtanto medo que nem visto mais aquilo!", "Misha cobrando proteção atenta de Lyner com CR."),
    26886: ("O Sheep Sweets é um pijama,CRnão é?", "Misha percebendo o teor de pijama do figurino Sheep Sweets com CR."),
    26887: ("É... O que mais seria?", "Lyner confirmando com óbvio humor."),
    26888: ("...Como é que eu lutei normalmenteCRcom aquilo até agora sem nem ligar,CRhein?", "Misha incrédula de ter ido à batalha de pijama com quebras CR."),
    26889: ("Hahaha, relaxa! Você é tão baixinhaCRque ninguém liga pra isso.", "Lyner rindo e chamando Misha de pequena com CR."),
    26890: ("Sei que foi pra consolar, e como é você,CRvou deixar passar dessa vez.", "Misha perdoando Lyner pelo comentário da altura com CR."),
    26891: ("Mas se falar de novo, solto uma CançãoCRcom tudo pra cima de você! Fica esperto!", "Misha ameaçando lançar Magia da Canção nele com CR."),
    26892: ("Aquele Vestido Chinês marca o corpoCRdemais, fico com tanta vergonha...", "Misha envergonhada com as curvas expostas no traje Tenshin Ranman com CR."),
    26893: ("É bom pra se mexer, mas no fimCRdas contas eu só fico cantando.", "Misha ponderando a mobilidade inútil para quem só entoa magia com CR."),
    26894: ("Mas você fica no maior estilo com ele!CRAcho que fica linda demais.", "Lyner elogiando a beleza e a elegância de Misha no traje com CR."),
    26895: ("É-é mesmo...? Ouvir isso de vocêCRme deixa feliz...", "Misha corando desarmada com o elogio de Lyner com CR."),
    26896: ("Mas ainda tenho vergonha em público...CRQue tal se eu usar só pra seduzir vocêCRa sós?", "Misha sugerindo usar o traje exclusivamente para seduzir Lyner com quebras CR."),
    26897: ("O SHINOBI tem um corteCRousado até demais, né?", "Misha comentando a sensualidade extrema do traje ninja com CR."),
    26898: ("Marca o corpo todo e mal cobre nada.CRNão tem uma roupa um pouco maisCRdiscreta, não?", "Misha pedindo figurinos mais comportados com quebras CR."),
    26899: ("...Tipo macacão?", "Lyner sugerindo roupas utilitárias."),
    26900: ("Zero estilo, nem pensar!", "Misha rejeitando a falta de moda."),
    26901: ("Com o SHINOBI, até esqueçoCRque sou péssima de exercício.", "Misha sentindo agilidade fantasiada no traje ninja com CR."),
    26902: ("Dá a sensação de que consigo me moverCRrápido e fazer acrobacias insanas!CRÉ muito louco.", "Misha fantasiando manobras acrobáticas com quebras CR."),
    26903: ("Fica só na imaginação mesmo.CRSe tentar, vai se quebrar todinha.", "Lyner cortando as ilusões acrobáticas de Misha com CR."),
    26904: ("...Nem sei como interpretarCRum comentário desses...", "Misha em dúvida se fica brava ou desconcertada com CR."),
    26905: ("Aquele traje KASYA...CRé mais uma armadura do que roupa, né?", "Misha comentando a couraça pesada do traje KASYA com CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0280.items():
    maxb = max_map_0280[tid]
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
    print("=== 0280 100% PERFEITO ===")

import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0288 = {
    27074: 56, 27075: 176, 27076: 96, 27077: 184, 27078: 240, 27079: 136,
    27080: 112, 27081: 232, 27082: 168, 27083: 120, 27084: 64, 27085: 232,
    27086: 168, 27087: 120, 27088: 128, 27089: 152, 27090: 200, 27091: 120,
    27092: 96, 27093: 72, 27094: 120, 27095: 152, 27096: 112, 27097: 168
}

calib_0288 = {
    27074: ("Enfim, agora saquei tudo.", "Misha compreendendo a situação com concisão e naturalidade. (51B <= 56B)"),
    27075: ("No fim, você prefere garotasCRcomo eu a mulheres adultas, né?", "Misha concluindo o gosto de Lyner por sua forma jovem com CR. (125B <= 176B)"),
    27076: ("Ei... Por favor, não faleCRisso em público!", "Lyner implorando discrição a Misha com CR. (89B <= 96B)"),
    27077: ("Fica calmo. Não importa o seuCRgosto, eu nunca deixaria deCRgostar de você por isso.", "Misha tranquilizando Lyner com afeto incondicional restaurando JP soberano com CRs. (171B <= 184B)"),
    27078: ("Além do mais, ser pequena é prático.CRMesmo se a gente andar grudado,CRninguém olha torto pra nós.", "Misha exaltando as vantagens da forma miúda com CRs. (202B <= 240B)"),
    27079: ("...Só não exagera, por favor...CRMorro de medo das consequências.", "Lyner pedindo moderação no afeto público com CR. (134B <= 136B)"),
    27080: ("Nunca mais quero voltarCRà Crônica Crescente, ouviu?", "Misha jurando jamais retornar ao confinamento com termo canônico e CR. (107B <= 112B)"),
    27081: ("Quando achei que tinha saído, me prenderam de novo; saí outra vez e me trancaram de volta,CRe depois me tiraram...", "Misha descrevendo o ciclo sufocante de prisões com CR. (231B <= 232B)"),
    27082: ("Ninguém iria pra lá por querer...CRTomara que seja a última vez,CRouviu bem?", "Misha selando o fim definitivo do cativeiro com CRs. (156B <= 168B)"),
    27083: ("Ultimamente você vem papearCRcomigo toda noite, né?", "Misha comentando sobre as visitas noturnas assíduas com CR. (105B <= 120B)"),
    27084: ("É... pensando bem, é verdade.", "Lyner concordando sobre a rotina noturna. (61B <= 64B)"),
    27085: ("Ficar indo e voltando de quarto em quarto cansa tanto... Que tal a gente ficar no mesmo quarto daqui pra frente?", "Misha sugerindo com malícia ingênua dividirem o mesmo quarto. (225B <= 232B)"),
    27086: ("I-Isso não... Sinto que coisas muitoCRperigosas podem acontecer, então melhor não.", "Lyner em pânico cômico recusando a proposta com CR. (168B <= 168B)"),
    27087: ("Tsc... Tá!CREntão continue vindoCRao meu quarto, ouviu?", "Misha cobrando as visitas noturnas com CRs. (113B <= 120B)"),
    27088: ("A Canção Pai Teimoso é bemCRassustadora em vários sentidos.", "Misha comentando sobre a Canção Pai Teimoso com CR. (121B <= 128B)"),
    27089: ("Quando canto, surge um coroaCRna minha cabeça que fica vermelho!", "Misha descrevendo os efeitos bizarros da canção cômica com CR. (130B <= 152B)"),
    27090: ("É... eu entendo perfeitamente.CRQuando aquilo apareceu, nem eu conseguiCRme concentrar na batalha.", "Lyner compartilhando o choque cômico em batalha com CRs. (198B <= 200B)"),
    27091: ("Como mulher, prefiro evitarCRusar essa magia...", "Misha expressando repulsa feminina pela evocação com CR. (95B <= 120B)"),
    27092: ("O Gaia Bombard pode serCRchamado de Canção?", "Lyner questionando a natureza marcial de Gaia Bombard com termo canônico e CR. (87B <= 96B)"),
    27093: ("Hum? Tem algum problema com ela?", "Misha defendendo seu ataque sísmico. (65B <= 72B)"),
    27094: ("Não é problema, mas dá margemCRpra tanta pergunta...", "Lyner intrigado com a lógica do ataque com CR. (108B <= 120B)"),
    27095: ("No fundo, você só joga um marteloCRgigante e esmaga todo mundo, não é?", "Lyner apontando o pragmatismo brutal do golpe com CR. (145B <= 152B)"),
    27096: ("Isso não é magia,CRtá mais pra ataque físico, né?", "Lyner diferenciando dano mágico de força bruta com CR. (104B <= 112B)"),
    27097: ("O martelo e quem arremessa vêmCRda magia, então qual é o problema?", "Misha justificando a origem mágica do golpe com CR. (136B <= 168B)")
}

all_ok = True
for tid, (txt, rat) in calib_0288.items():
    maxb = max_map_0288[tid]
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
    print("=== 0288 100% PERFEITO ===")

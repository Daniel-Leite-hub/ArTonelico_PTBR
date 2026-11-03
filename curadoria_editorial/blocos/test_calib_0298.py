import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0298 = {
    27314: 168, 27315: 176, 27316: 184, 27317: 56, 27318: 240, 27319: 72,
    27320: 136, 27321: 48, 27322: 176, 27323: 160, 27324: 48, 27325: 80,
    27326: 128, 27327: 184, 27328: 32, 27329: 96, 27330: 160, 27331: 168,
    27332: 168, 27333: 112, 27334: 176, 27335: 144, 27336: 176, 27337: 144
}

calib_0298 = {
    27314: ("Que bom que teve um guia...CREntão, da próxima vez, vocêCRpoderia ser o meu guia?", "Shurelia sugerindo timidamente um passeio a dois com CRs. (166B <= 168B)"),
    27315: ("Nunca andei por uma cidade assim.CRQuando houver paz, quero passearCRcom calma por lá.", "Shurelia sonhando com tempos de paz com CRs. (174B <= 176B)"),
    27316: ("Lyner... Meio de repente, mas...CRvou ao parque agora.CRVenha me escoltar.", "Shurelia convidando Lyner para o parque com pretexto de guarda com CRs. (149B <= 184B)"),
    27317: ("Hã!? Agora?CRMas por quê?", "Lyner surpreso com o chamado repentino com CR. (53B <= 56B)"),
    27318: ("T-Tenho uma coisa pra investigar!CRMas se eu for só e um vírus atacar, será terrível, né? Me proteja!", "Shurelia disfarçando o encontro com nervosismo adorável e CR. (208B <= 240B)"),
    27319: ("Sim... Por mim tudo bem, mas...", "Lyner concordando hesitante. (63B <= 72B)"),
    27320: ("Não seria mais seguro irmosCRcom todos na próxima vez?", "Lyner com sua densidade crônica sugerindo chamar o grupo com CR. (111B <= 136B)"),
    27321: ("N-Não pode ser assim!", "Shurelia rejeitando a ideia de levar os outros. (44B <= 48B)"),
    27322: ("É uma investigação em segredo...CRPara a Senhora da Torre e o Cavaleiro...", "Shurelia apelando para a confidencialidade oficial com CR. (150B <= 176B)"),
    27323: ("É? Melhor passar em PlatinaCRe levar outros cavaleiros...", "Lyner insistindo na segurança com mais soldados com CR. (116B <= 160B)"),
    27324: ("...Chega. Idiota.", "Shurelia desistindo e xingando a lerdeza dele. (35B <= 48B)"),
    27325: ("Hã!?CRFalei besteira de novo?", "Lyner confuso sem entender por que ela se irritou com CR. (60B <= 80B)"),
    27326: ("Lyner, para que você vai usarCRaquele [Fio do Vínculo]?", "Shurelia perguntando sobre o item de síntese com colchetes e CR. (113B <= 128B)"),
    27327: ("Eu uso em combate.CRSe equipar aquilo, nossa sintoniaCRfica bem mais forte.", "Lyner explicando o bônus de harmonia do item com CRs. (151B <= 184B)"),
    27328: ("...Com quem?", "Shurelia ciumenta querendo saber o parceiro. (25B <= 32B)"),
    27329: ("Com quem for minha parceiraCRna hora, eu acho.", "Lyner respondendo ingenuamente com CR. (93B <= 96B)"),
    27330: ("Precisa recorrer a um fio dessesCRpara fortalecer seus laços...?", "Shurelia questionando o uso de artifícios mágicos no afeto com CR. (130B <= 160B)"),
    27331: ("Não é isso, mas achei bomCRse pudesse unir ainda mais...", "Lyner justificando a intenção de aproximação com CR. (115B <= 168B)"),
    27332: ("Tentar mudar os sentimentosCRcom um objeto externo...CRIsso é distorcido!", "Shurelia repreendendo com rigor moral e CRs. (148B <= 168B)"),
    27333: ("P-Peço desculpas...CRVou evitar usar daqui em diante.", "Lyner aceitando a repreensão com humildade e CR. (108B <= 112B)"),
    27334: ("...Mas como as batalhas põem a vidaCRem risco... abro uma exceção.", "Shurelia ponderando e recuando por zelo à vida dele com CR. (134B <= 176B)"),
    27335: ("Hã? Mas usar isso na batalhaCRnão salva vidas nem nada...", "Lyner rebatendo a lógica tática com CR. (117B <= 144B)"),
    27336: ("Aumentar a união eleva a chance de vitória. Portanto, não me oponho.", "Shurelia autorizando o uso com formalidade inventada. (140B <= 176B)"),
    27337: ("É? Então vou aproveitar e pôrCRna Aurica da próxima vez.", "Lyner aceitando a deixa e citando Aurica com CR (expurga erro do EN). (117B <= 144B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0298.items():
        maxb = max_map_0298[tid]
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
        print("=== 0298 100% PERFEITO ===")

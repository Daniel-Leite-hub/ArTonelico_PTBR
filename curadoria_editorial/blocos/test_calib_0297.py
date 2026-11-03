import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0297 = {
    27290: 152, 27291: 192, 27292: 88, 27293: 192, 27294: 96, 27295: 120,
    27296: 104, 27297: 184, 27298: 200, 27299: 240, 27300: 96, 27301: 128,
    27302: 272, 27303: 280, 27304: 200, 27305: 80, 27306: 176, 27307: 168,
    27308: 32, 27309: 168, 27310: 112, 27311: 136, 27312: 88, 27313: 192
}

calib_0297 = {
    27290: ("É, tem razão.CRDe agora em diante uso remédiosCRde ação rápida.", "Lyner concordando em usar remédios convencionais com CRs. (131B <= 152B)"),
    27291: ("...Mas... se tiver um motivoCRpara só poder usar o Parfait Dokkoi,CReu respeito sua decisão.", "Shurelia recuando sem jeito e respeitando a preferência com CRs. (187B <= 192B)"),
    27292: ("Não, não tenho um motivo assim...", "Lyner esclarecendo sem rodeios. (69B <= 88B)"),
    27293: ("...É mesmo?...CRSe for inevitável, tudo bem usarCRo Parfait Dokkoi também.", "Shurelia abrindo concessão fofa para o doce com CRs. (152B <= 192B)"),
    27294: ("Não é que haja uma situaçãoCRassim nem nada...", "Lyner sem jeito diante da insistência dela com CR. (95B <= 96B)"),
    27295: ("...A-Ah, é?... Enfim, euCRnem falei tão a sério...", "Shurelia desconcertada minimizando a bronca com CR. (104B <= 120B)"),
    27296: ("Se quiser mesmo usar,CRfique à vontade.", "Shurelia permitindo o uso com CR. (80B <= 104B)"),
    27297: ("Na verdade, prefiro comer assim,CRfora da batalha... É bem gostoso.", "Lyner elogiando o sabor do parfait fora de combate com CR. (136B <= 184B)"),
    27298: ("A cidade de Nemo é vasta demais. Fico impressionada como se desenvolveu tanto.", "Shurelia admirando o progresso da metrópole. (158B <= 200B)"),
    27299: ("É verdade. Fiquei chocado de início.CRAquele parque é enorme e tem atéCRuma imensa Pedra da Canção.", "Lyner recordando o impacto visual do parque e da Pedra da Canção com CRs. (203B <= 240B)"),
    27300: ("Parece até um grande desperdícioCRde espaço...", "Lyner comentando sobre a amplitude desmedida com CR. (96B <= 96B)"),
    27301: ("Você pensa assim porque sempreCRviveu em Platina, Lyner.", "Shurelia pontuando a perspectiva restrita da vida em Platina com CR. (114B <= 128B)"),
    27302: ("Na Primeira Era, havia muito mais desperdício de espaço. A Grande Pedra da Canção não é nada comparada àquela época.", "Shurelia resgatando memórias milenares da Primeira Era. (239B <= 272B)"),
    27303: ("Na base da Torre, onde não podemos mais ir, havia uma estátua sem sentido num vão colossal, mesmo sendo dentro da Torre.", "Shurelia descrevendo a arquitetura suntuosa e perdida da base da Torre. (244B <= 280B)"),
    27304: ("Só o monumento tinha três stons de diâmetro, era imenso. Eu brincava muito naquela praça...", "Shurelia lembrando com nostalgia da infância no monumento de três stons. (187B <= 200B)"),
    27305: ("Nossa, como o povo antigo esbanjava.", "Lyner surpreso com a opulência dos tempos antigos. (73B <= 80B)"),
    27306: ("Sim... Mas se as nuvens abaixoCRfossem terra, ainda achariaCRque era esbanjamento?", "Shurelia provocando uma reflexão profunda sobre o Mar de Nuvens com CRs. (165B <= 176B)"),
    27307: ("Quando a terra sumiu deste mundo...CRo que era comum virou um luxo...", "Shurelia lamentando poeticamente a perda da terra com CR. (139B <= 168B)"),
    27308: ("...Shurelia...", "Lyner tocado pela melancolia da deusa. (29B <= 32B)"),
    27309: ("Nemo é uma cidade imensa. Você jáCRandou por boa parte dela, né?", "Shurelia puxando assunto sobre a exploração urbana com CR. (133B <= 168B)"),
    27310: ("Que nada. Nunca tive tempoCRpara passear por aí.", "Lyner admitindo que não teve tempo para turismo com CR. (98B <= 112B)"),
    27311: ("E não é um lugar que dê pra verCRtodo num único dia.", "Lyner explicando a grandiosidade de Nemo com CR. (109B <= 136B)"),
    27312: ("É, aquela cidade é mesmo bem grande...", "Shurelia concordando sobre as dimensões de Nemo. (79B <= 88B)"),
    27313: ("Se o Jack não tivesse me guiado da primeira vez em Nemo, com certeza eu teria me perdido.", "Lyner reconhecendo a ajuda indispensável de Jack. (180B <= 192B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0297.items():
        maxb = max_map_0297[tid]
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
        print("=== 0297 100% PERFEITO ===")

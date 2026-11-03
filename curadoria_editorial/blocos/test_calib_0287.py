import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0287 = {
    27050: 152, 27051: 88, 27052: 136, 27053: 176, 27054: 104, 27055: 128,
    27056: 104, 27057: 176, 27058: 96, 27059: 96, 27060: 64, 27061: 136,
    27062: 104, 27063: 136, 27064: 160, 27065: 176, 27066: 88, 27067: 96,
    27068: 80, 27069: 168, 27070: 184, 27071: 104, 27072: 112, 27073: 104
}

calib_0287 = {
    27050: ("Além disso, você foca tanto na lutaCRque nem olha pra mim, né?", "Misha reclamando que Lyner não a admira em combate com CR. (128B <= 152B)"),
    27051: ("Se eu me distrair,CRacabo derrotado!", "Lyner justificando a seriedade do combate com CR. (73B <= 88B)"),
    27052: ("É, tem razão, mas...CREntão vou me transformar aqui mesmo!", "Misha propondo trocar de roupa fora de batalha com CR. (120B <= 136B)"),
    27053: ("Se ao menos olhar bem pra mim agora,CReu continuo usando o quimono brancoCRpor você.", "Misha negociando o uso do quimono nupcial com CRs. (170B <= 176B)"),
    27054: ("Tô tão feliz de viajar com vocêCRde novo, Lyner!", "Misha expressando júbilo ao viajar com Lyner com CR. (100B <= 104B)"),
    27055: ("É?... Eu acho que viver de boa,CRdescansando, é bem melhor.", "Lyner ponderando sobre o conforto do sedentarismo com CR. (121B <= 128B)"),
    27056: ("Hmm... Essa vida mansaCRtambém não é ruim, mas...", "Misha avaliando a rotina pacata com CR. (102B <= 104B)"),
    27057: ("Mas em vez de ficar parada,CRprefiro andar e viajar por toda parteCRao seu lado.", "Misha preferindo o nomadismo a dois com CRs. (161B <= 176B)"),
    27058: ("Você gosta mais de mimCRadulta, né, Lyner?", "Misha indagando sobre a preferência física de Lyner com CR. (87B <= 96B)"),
    27059: ("Hã?! N-Não fiz você crescerCRpor isso...", "Lyner desconcertado e na defensiva com CR. (84B <= 96B)"),
    27060: ("Não precisa se justificar!", "Misha provocando com irreverência e malícia. (54B <= 64B)"),
    27061: ("Hehehe, você é só um garotoCRcomum afinal. Que alívio.", "Misha aliviada ao constatar os instintos comuns de Lyner com CR. (113B <= 136B)"),
    27062: ("Ou você prefere quando eu souCRpequenininha?", "Misha questionando a atração por sua forma infantil com CR. (90B <= 104B)"),
    27063: ("Desse jeito parece que tenhoCRgostos estranhos! Dá um tempo.", "Lyner reclamando da insinuação embaraçosa com CR. (122B <= 136B)"),
    27064: ("E daí? No fundo, você deve terCRuma queda por esse tipo mesmo.", "Misha insistindo na implicância bem-humorada com CR. (127B <= 160B)"),
    27065: ("Tô mais acostumada com esse corpo,CRe não vejo problema se esseCRfor o seu gosto.", "Misha tranquilizando Lyner sobre preferências com CRs. (165B <= 176B)"),
    27066: ("Pelo visto você prefereCRmulheres adultas.", "Misha deduzindo a preferência de Lyner por adultas com CR. (86B <= 88B)"),
    27067: ("Já disse que o meu gostoCRnão tem nada a ver!", "Lyner protestando contra a dedução precipitada com CR. (93B <= 96B)"),
    27068: ("Não precisa se fazerCRde durão comigo!", "Misha desarmando as evasivas de Lyner com CR. (79B <= 80B)"),
    27069: ("Garotos normais admiram mulheresCRmaduras mesmo. Pode bater no peitoCRcom orgulho!", "Misha validando com ironia as atrações de Lyner com CRs. (165B <= 168B)"),
    27070: ("Garoto?... Parece que tá me tratandoCRcomo criança. Que sensação esquisita.", "Lyner estranhando o tom condescendente com CR. (153B <= 184B)"),
    27071: ("Pensando bem, sou mais velhaCRque você, Lyner!", "Misha lembrando de sua precedência etária com CR. (94B <= 104B)"),
    27072: ("Pode vir pedir dengoCRpra sua irmã mais velha!", "Misha sugerindo dengos fraternais com CR. (94B <= 112B)"),
    27073: ("...Você nem tá ouvindoCRo que eu tô dizendo.", "Lyner suspirando diante da tagarelice de Misha com CR. (92B <= 104B)")
}

all_ok = True
for tid, (txt, rat) in calib_0287.items():
    maxb = max_map_0287[tid]
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
    print("=== 0287 100% PERFEITO ===")

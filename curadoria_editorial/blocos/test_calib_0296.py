import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0296 = {
    27266: 48, 27267: 80, 27268: 64, 27269: 128, 27270: 40, 27271: 160,
    27272: 24, 27273: 16, 27274: 152, 27275: 112, 27276: 152, 27277: 144,
    27278: 40, 27279: 152, 27280: 176, 27281: 160, 27282: 120, 27283: 128,
    27284: 32, 27285: 96, 27286: 64, 27287: 144, 27288: 120, 27289: 216
}

calib_0296 = {
    27266: ("Uau!? Tá tudo bem!?", "Lyner reagindo ao espirro repentino de Shurelia. (40B <= 48B)"),
    27267: ("...Ué? Cadê o Pó de Polimento?", "Shurelia procurando o pó soprado pelo espirro. (64B <= 80B)"),
    27268: ("...Voou tudo com o espirro.", "Lyner explicando o sumiço do pó. (55B <= 64B)"),
    27269: ("...Poxa! Da próxima vez, façaCRalgo pesado que não voe!", "Shurelia emburrada culpando Lyner com CR. (114B <= 128B)"),
    27270: ("A culpa é minha!?", "Lyner indignado com o timing cômico. (36B <= 40B)"),
    27271: ("Diga, Lyner... Quando desceuCRao Mundo Inferior, o que sentiu?", "Shurelia indagando sobre as primeiras impressões do Mundo Inferior com CR. (125B <= 160B)"),
    27272: ("Hã, eu?", "Lyner pego de surpresa. (16B <= 24B)"),
    27273: ("Sim.", "Shurelia confirmando com serenidade. (9B <= 16B)"),
    27274: ("Bem... na verdade, eu nem tiveCRtempo pra pensar nisso.", "Lyner relembrando a queda frenética com CR. (111B <= 152B)"),
    27275: ("Cheguei quase morrendo e comCRmuita pressa.", "Lyner citando a gravidade da chegada com CR. (87B <= 112B)"),
    27276: ("Mas ao chegar à Vila Karulu,CRachei o lugar bem animado.", "Lyner elogiando a Vila Karulu com topônimo canônico e CR. (114B <= 152B)"),
    27277: ("...Ou seja: quase morreu logoCRno início da missão, né?", "Shurelia resumindo a imprudência com ironia afetuosa e CR. (114B <= 144B)"),
    27278: ("É... Desculpe.", "Lyner sem graça admitindo o aperto. (30B <= 40B)"),
    27279: ("A culpa também foi minha.CRVocê não tem que se desculpar.", "Shurelia assumindo sua parcela de culpa com nobreza e CR. (118B <= 152B)"),
    27280: ("É minha primeira vez vendo as AsasCRde Hórus desde a Terceira Era.", "Shurelia citando as Asas de Hórus e a Terceira Era com CR. (135B <= 176B)"),
    27281: ("É tudo tão cheio de vida.CRTodos se esforçam tanto pra viver...", "Shurelia comovida com a vitalidade humana com CR. (130B <= 160B)"),
    27282: ("Sinto na pele a incrível forçaCRvital da humanidade.", "Shurelia maravilhada com a resiliência dos povos com CR. (107B <= 120B)"),
    27283: ("Por esse povo, preciso manterCReste mundo em paz...", "Shurelia renovando seus votos solenes de guardiã com CR. (103B <= 128B)"),
    27284: ("Com certeza.", "Lyner apoiando a determinação de Shurelia. (25B <= 32B)"),
    27285: ("Lyner... Tem algo que precisoCRte dizer.", "Shurelia mudando de tom com seriedade e CR. (81B <= 96B)"),
    27286: ("Sim... Mas tá brava comigo?", "Lyner percebendo a irritação iminente. (56B <= 64B)"),
    27287: ("Como assim você se cura comCRum Parfait Dokkoi na batalha!?", "Shurelia escandalizada com a sobremesa em combate com CR. (120B <= 144B)"),
    27288: ("Ai, desculpe! Pra gente é tãoCRcomum... Pegou mal...?", "Lyner desconcertado tentando se justificar com CRs. (109B <= 120B)"),
    27289: ("É uma batalha! Numa tensão de vida ou morte, como pode comer parfait na maior calma!?", "Shurelia indignada com o deboche tático da sobremesa. (173B <= 216B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0296.items():
        maxb = max_map_0296[tid]
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
        print("=== 0296 100% PERFEITO ===")

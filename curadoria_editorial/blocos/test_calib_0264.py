import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0264 = {
    26498: ("O parque?CRPor mim tudo bem ir lá.", "Lyner concordando de forma despreocupada com o passeio."),
    26499: ("...E se for um encontro em Nemo?", "Misha especificando o caráter romântico do passeio no parque."),
    26500: ("Parque em Nemo?!CRMas lá é...!", "Lyner surpreso ao reconhecer a reputação de ponto de encontro do local."),
    26501: ("Não pode?CREu tava com tanta esperança...", "Misha demonstrando sua expectativa carinhosa pelo encontro."),
    26502: ("...É... bem...", "Lyner sem jeito diante da meiguice de Misha."),
    26503: ("...Quando der uma chance.", "Lyner aceitando o convite de encontro quando houver folga."),
    26504: ("...Que bom! Fico feliz.", "Misha comemorando aliviada e contente a aceitação de Lyner."),
    26505: ("Lyner, tudo bem mesmo vocêCRentrar na equipe de busca?", "Misha sondando se Lyner se arrepende de ter seguido com a Tenba em vez da Igreja."),
    26506: ("Hã? Como assim?", "Lyner sem entender o motivo da dúvida de Misha."),
    26507: ("Você prometeu retribuirCRa ajuda da Igreja, não foi?", "Misha lembrando da dívida de gratidão de Lyner com a Igreja e Aurica."),
    26508: ("E a Aurica te ajudou muitoCRquando você caiu no Mundo Inferior...", "Misha demonstrando sua pontinha de ciúme e consideração por Aurica."),
    26509: ("É, tem isso também, mas...", "Lyner reconhecendo o fato sem saber bem o que responder."),
    26510: ("...Tá arrependido?", "Misha perguntando diretamente sobre o arrependimento."),
    26511: ("Eu penso nisso,CRmas não me arrependo.", "Lyner reafirmando sua escolha convicta de acompanhar Misha."),
    26512: ("Não dá pra ir agora,CRmas posso retribuir assim queCRa missão terminar.", "Lyner planejando honrar sua palavra após concluir a busca na Torre."),
    26513: ("A Aurica me ajudou, sim,CRmas você também me ajudou demais.", "Lyner valorizando o apoio essencial que recebeu de Misha."),
    26514: ("Mas fica preocupado com ela, né?", "Misha testando os sentimentos de Lyner em relação a Aurica."),
    26515: ("Lá é mais seguro do que na Torre,CRnão preciso me preocupar com ela.", "Lyner argumentando a segurança do santuário em comparação aos perigos da Torre."),
    26516: ("...Quer dizer que você se preocupaCRcomigo?", "Misha sorrindo dengosa ao perceber que a preocupação dele é com ela."),
    26517: ("Sei lá!", "Lyner desconversando encabulado com a conclusão íntima."),
    26518: ("Seu chato!", "Misha reclamando com carinho da esquiva de Lyner."),
    26519: ("Lyner, você ainda ama Funbuns?", "Misha mudando de assunto e perguntando sobre a guloseima favorita de Lyner."),
    26520: ("É claro!!", "Lyner respondendo de pronto com entusiasmo gastronômico."),
    26521: ("Não existe ninguém em PlatinaCRque não ame aquilo!", "Lyner defendendo o doce tradicional com orgulho patriótico."),
}

max_map = {
    26498: 72, 26499: 72, 26500: 64, 26501: 96, 26502: 40, 26503: 56,
    26504: 48, 26505: 128, 26506: 48, 26507: 128, 26508: 144, 26509: 72,
    26510: 64, 26511: 80, 26512: 152, 26513: 144, 26514: 80, 26515: 144,
    26516: 88, 26517: 16, 26518: 24, 26519: 72, 26520: 24, 26521: 104
}

all_ok = True
for tid, (txt, rat) in calib_0264.items():
    maxb = max_map[tid]
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
    print("=== 0264 100% PERFEITO ===")

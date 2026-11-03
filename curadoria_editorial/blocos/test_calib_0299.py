import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0299 = {
    27338: 144, 27339: 64, 27340: 144, 27341: 160, 27342: 80, 27343: 88,
    27344: 104, 27345: 200, 27346: 120, 27347: 120, 27348: 72, 27349: 152,
    27350: 144, 27351: 72, 27352: 224, 27353: 104, 27354: 16, 27355: 192,
    27356: 104, 27357: 232, 27358: 128, 27359: 136, 27360: 32, 27361: 312
}

calib_0299 = {
    27338: ("Lembra daquele [Fio do Vínculo]?CRVocê ainda está com ele...?", "Shurelia trazendo à tona o fio vermelho com colchetes e CR. (126B <= 144B)"),
    27339: ("Sim, tá aqui. Veja.", "Lyner mostrando o item prontamente. (40B <= 64B)"),
    27340: ("Descobri o jeito certo de usar.CRQueria experimentar...", "Shurelia propondo o uso romântico disfarçado com CR. (111B <= 144B)"),
    27341: ("Sério!? Que alívio!CRNão tinha muita certezaCRde como usar isso.", "Lyner ingênuo aceitando a sugestão com CRs. (132B <= 160B)"),
    27342: ("Então abra as mãos e estenda.", "Shurelia instruindo com timidez. (61B <= 80B)"),
    27343: ("Sim... Amarra no mindinhoCRpra usar...?", "Lyner estranhando o laço no dedo mindinho com CR. (79B <= 88B)"),
    27344: ("A-Acho que sim...CRAmarro no meu também...", "Shurelia envergonhada amarrando o próprio mindinho com CR. (86B <= 104B)"),
    27345: ("Esse é o jeito certo...?CRAssim vamos ficar nos puxandoCRdurante o combate...", "Lyner questionando a viabilidade tática do laço com CRs. (156B <= 200B)"),
    27346: ("M-Mas parece que assim o poderCRaumenta umas cem vezes...", "Shurelia inventando a desculpa do poder multiplicado com CR. (115B <= 120B)"),
    27347: ("Mesmo que aumente...CRcomo vou brandir minha espada?", "Lyner apontando a óbvia restrição motora com CR. (105B <= 120B)"),
    27348: ("O-O quê!?CRDê um jeito de brandir!", "Shurelia sem argumentos insistindo com energia e CR. (71B <= 72B)"),
    27349: ("Não tem como... É impossível!CRDeixe eu usar do jeito de antes...", "Lyner implorando para desfazer a amarração com CR. (134B <= 152B)"),
    27350: ("Viu o bicho de pelúcia na lojaCRgeral da Vila Karulu?", "Lyner puxando o assunto do sapo de pelúcia com CR. (108B <= 144B)"),
    27351: ("...Está falando daquele sapo?", "Shurelia reconhecendo o sapo com cautela. (60B <= 72B)"),
    27352: ("Esse mesmo! Que gosto bizarro, né?CRComo alguém cria um designCRtão desajeitado daqueles?", "Lyner zombando do design esquisito com CRs. (182B <= 224B)"),
    27353: ("Quase caí no riso quandoCRvi pela primeira vez!", "Lyner admitindo que quase gargalhou com CR. (96B <= 104B)"),
    27354: ("É...?!", "Shurelia ofendida engolindo a indignação. (14B <= 16B)"),
    27355: ("Isso é desrespeito com quem fez! Cavaleiros de Elemia devem ser tolerantes com todos!", "Shurelia repreendendo Lyner em causa própria. (172B <= 192B)"),
    27356: ("É verdade... Me desculpe,CRExagerei no comentário.", "Lyner se desculpando desconcertado com CR. (103B <= 104B)"),
    27357: ("Aquele sapo de pelúcia da loja da Vila Karulu... ainda estava lá outro dia, né?", "Shurelia voltando ao assunto do sapo encalhado com topônimo canônico. (162B <= 232B)"),
    27358: ("É... Estava! Tomara que alguémCRcompre logo, né?", "Lyner tentando amenizar a situação com CR. (100B <= 128B)"),
    27359: ("Lyner, compre aquele sapoCRde pelúcia da loja.", "Shurelia dando a ordem expressa com CR. (94B <= 136B)"),
    27360: ("Eu!? Por quê!?", "Lyner chocado com a imposição. (30B <= 32B)"),
    27361: ("Se a loja falir porque o sapo não vendeu, os aldeões vão sofrer. Compre para ajudar a comunidade!", "Shurelia construindo uma justificativa mirabolante e altruísta. (198B <= 312B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0299.items():
        maxb = max_map_0299[tid]
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
        print("=== 0299 100% PERFEITO ===")

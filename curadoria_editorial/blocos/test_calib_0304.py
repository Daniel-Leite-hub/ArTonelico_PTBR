import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0304 = {
    27458: 32, 27459: 176, 27460: 136, 27461: 168, 27462: 192, 27463: 168,
    27464: 232, 27465: 72, 27466: 56, 27467: 120, 27468: 136, 27469: 104,
    27470: 80, 27471: 88, 27472: 152, 27473: 32, 27474: 128, 27475: 128,
    27476: 136, 27477: 96, 27478: 32, 27479: 88, 27480: 48, 27481: 176
}

calib_0304 = {
    27458: ("Claro que não!", "Shurelia rejeitando a ideia com veemência. (30B <= 32B)"),
    27459: ("Só fiquei confusa com seu gosto.CRSe dissesse que queria vestir,CRo que eu faria...?", "Shurelia constrangida imaginando Lyner com trajes bizarros com CRs. (170B <= 176B)"),
    27460: ("Desculpe... Mas se meu gostoCRfor ruim, a senhora se incomoda?", "Lyner perguntando a razão da preocupação dela com CR. (125B <= 136B)"),
    27461: ("C-Claro! Como sua acompanhante,CReu não suportaria ver vocêCRvestido desse jeito!", "Shurelia zangada e envergonhada com CRs. (165B <= 168B)"),
    27462: ("E como Cavaleiro de Elemia, prefiro que não use roupas vergonhosas no cotidiano.", "Shurelia impondo decoro à ordem dos cavaleiros. (162B <= 192B)"),
    27463: ("S-Sim... É bem rígido ser um Cavaleiro de Elemia. Tem até restrição de roupa...", "Lyner surpreso com o código de conduta civil da ordem. (162B <= 168B)"),
    27464: ("...N-Não é bem isso... É que com você... nunca se sabe o que vai aprontar se passar do ponto!", "Shurelia justificando sua vigilância sobre a impulsividade dele. (191B <= 232B)"),
    27465: ("É...? Não confia em mim, né?", "Lyner cabisbaixo com a falta de crédito. (60B <= 72B)"),
    27466: ("N-Não, não é nada disso!!", "Shurelia desesperada tentando desfazer a impressão ruim. (54B <= 56B)"),
    27467: ("Fazia tempo que a gente não iaCRao Altar dos Apóstolos.", "Lyner relembrando o Altar dos Apóstolos com termo canônico e CR. (113B <= 120B)"),
    27468: ("Após a luta com os vírus,CReu não queria me aproximar...", "Shurelia confessando o trauma com os vírus com CR. (116B <= 136B)"),
    27469: ("Normalmente nem há motivoCRpra chegar perto dali.", "Lyner concordando sobre o isolamento do altar com CR. (100B <= 104B)"),
    27470: ("É... Mas eu gostavaCRmuito da ELMA.", "Shurelia expressando carinho pela guardiã ELMA com CR. (72B <= 80B)"),
    27471: ("A Guardiã branca da senhora, né?", "Lyner lembrando da aparência da guardiã. (67B <= 88B)"),
    27472: ("Sim... Eram diferentes, mas a cópiaCRera idêntica. Foi bem amargo.", "Shurelia relembrando a duplicata viral ELMA-DS com CR. (135B <= 152B)"),
    27473: ("Ah... Entendi.", "Lyner compreendendo a tristeza dela. (29B <= 32B)"),
    27474: ("Se possível, não quero chegarCRperto de lá por um bom tempo...", "Shurelia querendo distância do altar com CR. (128B <= 128B)"),
    27475: ("Será por ter começado a viajarCRcom você recentemente?", "Shurelia ponderando sobre a influência da jornada com CR. (112B <= 128B)"),
    27476: ("Acho que vai doer voltarCRpara o Rinkernator...", "Shurelia sentindo o peso do isolamento cósmico iminente com CR. (95B <= 136B)"),
    27477: ("Lá... vou ter que ficarCRsozinha de novo...", "Shurelia admitindo a solidão do Rinkernator com CR. (88B <= 96B)"),
    27478: ("...É verdade.", "Lyner concordando em silêncio solidário. (28B <= 32B)"),
    27479: ("O que costuma fazer láCRno dia a dia?", "Lyner curioso com a rotina no topo da torre com CR. (76B <= 88B)"),
    27480: ("Dia a dia?CRPor quê!?", "Shurelia desconfiada e na defensiva com CR. (44B <= 48B)"),
    27481: ("Não imagino a senhora num dia comum, fiquei curioso pra saber o que faz.", "Lyner explicando seu fascínio pelo cotidiano da deusa. (146B <= 176B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0304.items():
        maxb = max_map_0304[tid]
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
        print("=== 0304 100% PERFEITO ===")

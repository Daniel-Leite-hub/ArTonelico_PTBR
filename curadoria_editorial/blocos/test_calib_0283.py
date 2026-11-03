import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0283 = {
    26954: 104, 26955: 232, 26956: 24, 26957: 144, 26958: 120, 26959: 96,
    26960: 232, 26961: 120, 26962: 184, 26963: 88, 26964: 96, 26965: 176,
    26966: 136, 26967: 56, 26968: 176, 26969: 216, 26970: 120, 26971: 64,
    26972: 128, 26973: 104, 26974: 168, 26975: 104, 26976: 104, 26977: 104
}

calib_0283 = {
    26954: ("...Não que eu seja perfeitaCRnem nada disso.", "Misha admitindo humildemente suas limitações com quebra CR. (90B <= 104B)"),
    26955: ("É só que, pra parecer exemplar, passeiCRa vida toda dando um jeito de esconderCRminhas imperfeições...", "Misha confessando o esforço de esconder falhas para parecer perfeita com CRs. (207B <= 232B)"),
    26956: ("...Misha?", "Lyner surpreso e desconcertado diante da quebra de pose de Misha. (19B <= 24B)"),
    26957: ("Hã? Ah, não, esquece! O que importaCRé que sou um prodígio,CRnão é?", "Misha retomando depressa sua fachada alegre e confiante com CRs. (141B <= 144B)"),
    26958: ("Nunca imaginei que um dia viajaria com você, Lyner.", "Misha expressando a surpresa feliz de viajar com Lyner. (104B <= 120B)"),
    26959: ("Não é entediante?CRViver só andando por aí.", "Lyner questionando a monotonia da vida de andarilho com CR. (91B <= 96B)"),
    26960: ("Que nada, de jeito nenhum!CRÉ tudo novidade pra mim, então é bem divertido, e quero conhecer um monte de lugares.", "Misha maravilhada com a liberdade das viagens e novos horizontes. (230B <= 232B)"),
    26961: ("Na Tenba, você ficava sempreCRno Beco Vagalume, né?", "Lyner relembrando a rotina de Misha em Tenba com termos canônicos e CR. (105B <= 120B)"),
    26962: ("É... Mas até que lá era bom.CRNo Beco Vagalume eu podia circular livremente.", "Misha comparando a liberdade do Beco Vagalume com CR. (156B <= 184B)"),
    26963: ("Antes disso... era só um quarto escuro...", "Misha revelando o passado sombrio de confinamento. (84B <= 88B)"),
    26964: ("Quarto escuro?CRFicou em cativeiro ou o quê?", "Lyner reagindo chocado à revelação do quarto escuro com CR. (90B <= 96B)"),
    26965: ("Hmm... Um dia te conto sobre isso.CRNão é algo que eu queira lembrar...", "Misha hesitando em tocar nas lembranças traumáticas com CR. (145B <= 176B)"),
    26966: ("Ei, Lyner... Promete não me odiar se eu te confessar uma coisa?", "Misha introduzindo uma confissão delicada com hesitação carinhosa. (128B <= 136B)"),
    26967: ("Dá até medo... O que é?", "Lyner reagindo curioso e apreensivo à pergunta de Misha. (50B <= 56B)"),
    26968: ("É que... Na verdade, como posso dizer...CReu detestava fazer coisas pelos outros.", "Misha admitindo sua aversão pretérita ao altruísmo forçado com CR. (164B <= 176B)"),
    26969: ("Eu achava que, antes de pensar em ajudarCRalguém, eu mesma devia ser prioridade...", "Misha explicando sua filosofia de autopreservação no passado com CR. (166B <= 216B)"),
    26970: ("É?... Mas comigo você sempreCRfoi gentil e fez de tudo.", "Lyner lembrando a dedicação imediata de Misha com CR. (113B <= 120B)"),
    26971: ("Você é exceção.CRÉ o Lyner.", "Misha expressando afeto e singularidade por Lyner com CR. (58B <= 64B)"),
    26972: ("Não entendi a lógica, mas que bom,CRfico muito agradecido.", "Lyner aceitando a exceção carinhosa com gratidão e CR. (119B <= 128B)"),
    26973: ("Ufufu... Mas acho que mudeiCRum pouco ultimamente.", "Misha rindo meigamente ao notar sua própria transformação com CR. (101B <= 104B)"),
    26974: ("Eu detestava tanto ajudar os outros,CRmas parece que essa aversão tá sumindo...", "Misha refletindo sobre a evolução da sua empatia com CR. (161B <= 168B)"),
    26975: ("Ei, Lyner...CRVocê gosta de mimCRadulta?", "Misha perguntando timidamente sobre a preferência de Lyner por sua forma adulta com CRs. (82B <= 104B)"),
    26976: ("Como assim?... Que pergunta maisCRcomplicada, hein.", "Lyner ficando desconcertado com a pergunta súbita com CR. (103B <= 104B)"),
    26977: ("Desculpa... É que antes eu nãoCRqueria crescer.", "Misha explicando por que tinha medo da vida adulta com CR. (97B <= 104B)")
}

all_ok = True
for tid, (txt, rat) in calib_0283.items():
    maxb = max_map_0283[tid]
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
    print("=== 0283 100% PERFEITO ===")

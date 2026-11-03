import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0259 = {
    26378: ('Acho que um "bom trabalho" serve, né?CRVocê passou por muito sufoco...', "Aurica parabenizando Lyner pelo avanço na Cosmosfera com tom doce e quebra CR."),
    26379: ("É, por aí... Mas ainda tô vivo,CRentão tá valendo...", "Lyner aliviado por sobreviver aos perigos da mente de Aurica."),
    26380: ("P-parece que foi bem puxado...CRDesculpa de verdade.", "Aurica constrangida e se desculpando sinceramente pelos perigos internos."),
    26381: ("Dizer que não foi duro seria mentira,CRmas até que me diverti.", "Lyner equilibrando a dureza dos testes com a diversão da companhia de Aurica."),
    26382: ("Conheci várias versões suas,CRsempre me metendo em encrenca...", "Lyner relembrando as facetas de Aurica nos níveis da Cosmosfera."),
    26383: ("...Nem sei como saí vivo dessa.", "Lyner surpreso com a própria sobrevivência após os testes."),
    26384: ("...Minha mente era tão perigosa assim?", "Aurica espantada com o relato do perigo de seu subconsciente."),
    26385: ("Mas é assim com qualquer um.CRQuanto mais fundo você vai,CRmais perigoso fica.", "Lyner explicando a mecânica natural da profundidade dos mundos mentais."),
    26386: ("É? Fico mais tranquila, então.CROdiaria que você achasse que euCRnão gosto de você.", "Aurica respirando aliviada ao saber que o perigo não era rejeição a Lyner."),
    26387: ("Se você me deixou mergulhar,CRjá imaginei que não me odiasse.", "Lyner deduzindo a afeição pelo simples fato de ter recebido autorização de Mergulho."),
    26388: ("Que ideia boba!CRNão deixo mergulharem em mimCRsó por não odiar a pessoa!", "Aurica repreendendo a dedução superficial de Lyner e afirmando seus sentimentos."),
    26389: ("Odiaria ter tanta genteCRmergulhando em mim...", "Aurica expressando a exclusividade e intimidade do Mergulho."),
    26390: ("...Mas já que te dei tanto trabalho,CRacho que posso fazerCRpelo menos isso pra você.", "Aurica decidindo retribuir o esforço com um gesto terno de carinho."),
    26391: ("Isso tudo...? Uou!CRD-deitar no seu colo?!", "Reação surpresa e embaraçada de Lyner ao receber o afeto de colo (hizamakura)."),
    26392: ("Opa... Hehe, sua cabeçaCRé bem levinha, Lyner.", "Aurica acariciando a cabeça de Lyner descansando em seu colo."),
    26393: ("Não fala como se eu não tivesse cérebro!CRE por que isso do nada?", "Lyner protestando comicamente contra a provocação carinhosa de Aurica."),
    26394: ("Como você passou por tanto sufoco,CRé uma forma de te agradecer, sabe?", "Aurica justificando o cafuné como recompensa merecida pela dedução da jornada."),
    26395: ("Na verdade eu queria colo também,CRmas mudei de ideia.", "Aurica confessando travessa o desejo recíproco de dengo e carinho."),
    26396: ("Tá cansado, né?CRSe quiser, pode dormir assim.", "Aurica oferecendo o colo aconchegante para Lyner descansar."),
    26397: ("É que... até quero dormir, mas tô tãoCRnervoso que duvido conseguir...", "Lyner admitindo que a proximidade e o coração acelerado impedem o sono."),
    26398: ("Quer que eu pare?", "Aurica perguntando manhosa se deve interromper o cafuné."),
    26399: ("...Tinha que perguntar isso...?", "Lyner desconcertado diante da pergunta capciosa de Aurica."),
    26400: ("Hehe, brincadeira...CRBoa noite, Lyner...", "Aurica sussurrando meiga e desejando boa noite a Lyner."),
    26401: ("Sabe, Lyner... Tem algoCRque queria muito te perguntar.", "Aurica introduzindo com curiosidade a conversa íntima seguinte."),
}

max_map = {
    26378: 160, 26379: 128, 26380: 144, 26381: 128, 26382: 160, 26383: 120,
    26384: 80, 26385: 160, 26386: 192, 26387: 152, 26388: 160, 26389: 96,
    26390: 208, 26391: 96, 26392: 96, 26393: 160, 26394: 144, 26395: 152,
    26396: 104, 26397: 176, 26398: 56, 26399: 64, 26400: 104, 26401: 112
}

all_ok = True
for tid, (txt, rat) in calib_0259.items():
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
    print("=== 0259 100% PERFEITO ===")

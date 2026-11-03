import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0275 = {
    26762: 40, 26763: 112, 26764: 152, 26765: 176, 26766: 176, 26767: 96,
    26768: 88, 26769: 200, 26770: 128, 26771: 72, 26772: 24, 26773: 152,
    26774: 200, 26775: 168, 26776: 168, 26777: 40, 26778: 184, 26779: 144,
    26780: 8, 26781: 144, 26782: 200, 26783: 48, 26784: 184, 26785: 120
}

calib_0275 = {
    26762: ("Ué, por que isso?", "Lyner surpreso com a pergunta súbita."),
    26763: ("Você já viu quase a metadeCRde mim, né, Lyner?", "Misha calculando a profundidade do Mergulho com CR."),
    26764: ("Ouvi dizer que mergulhar tão fundoCRassim começa a ficar bem perigoso...", "Misha temendo pelos riscos mentais com quebra CR."),
    26765: ("Ah... Puxado até é, mas não diriaCRque é 'perigoso' bem nesse sentido...", "Lyner ponderando o teor insólito da mente de Misha com CR."),
    26766: ("...Tô curiosa, mas se souber, vou quererCRme enfiar num buraco.CRMelhor nem perguntar.", "Misha constrangida desistindo de perguntar detalhes com quebras CR."),
    26767: ("Mas me diz... ainda querCRmergulhar em mim?", "Misha perguntando tímida se Lyner continuará o Mergulho com CR."),
    26768: ("Se você deixar, vou mergulharCRaté o fim.", "Lyner reafirmando sua fidelidade com quebra CR."),
    26769: ("Mas você já passou por tanto aperto!CRSe for mais fundo, não vai sofrerCRmuito mais?", "Misha preocupada com o sofrimento de Lyner com quebras CR."),
    26770: ("Pensar nisso me deixa preocupada demais...", "Misha aflita pelo bem-estar de Lyner."),
    26771: ("Não precisa se preocuparCRcom isso.", "Lyner tranquilizando Misha com quebra CR."),
    26772: ("M-mas...", "Misha hesitante diante do carinho de Lyner."),
    26773: ("Posso até passar sufoco, mas no fundoCRé bem divertido, sabia?", "Lyner revelando que se diverte na Cosmosfera com CR."),
    26774: ("Conheço várias versões suas e me metoCRem encrenca, mas não desgosto de nada disso.", "Lyner valorizando cada faceta de Misha com quebra CR."),
    26775: ("...Pode ser bem assustador, viu?CRNem eu sei o que penso no fundo da mente...", "Misha alertando sobre os segredos de seu inconsciente com CR."),
    26776: ("Se me deixar mergulhar, nem precisaCRfalar. Eu vou lá e vejo com meus olhos.", "Lyner determinado a desvendar a mente de Misha com CR."),
    26777: ("...Temerário.", "Misha chamando Lyner de imprudente com carinho."),
    26778: ("...Mas tô feliz. Então vou abrir meu coraçãoCRtodinho pra você sem reservas.", "Misha prometendo entrega total e transparência afetiva com CR."),
    26779: ("...C-calma, se for fundo demais de repente,CRaté eu fico com medo!", "Lyner desconcertado pedindo calma no avanço mental com CR."),
    26780: ("Hm?", "Interjeição breve de atenção."),
    26781: ("Ouvi passos agora há pouco...CRAchei que alguém vinha pra cá.", "Lyner ouvindo passos no acampamento com CR."),
    26782: ("Não era ninguém, mas... não precisaCRficar tão tensa assim, né?", "Lyner acalmando Misha com quebra CR."),
    26783: ("É, eu sei, mas...", "Misha justificando seu ciúme protetor."),
    26784: ("Agora é o meu momento com você.CRNão quero ninguém atrapalhando a gente.", "Misha exigindo exclusividade dengosa no descanso com CR."),
    26785: ("...Ah, já sei! Você tem aquele Peeka, né?CRBora usar ele!", "Misha sugerindo o item de camuflagem Peeka com quebra CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0275.items():
    maxb = max_map_0275[tid]
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
    print("=== 0275 100% PERFEITO ===")

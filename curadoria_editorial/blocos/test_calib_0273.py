import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0273 = {
    26714: 72, 26715: 80, 26716: 104, 26717: 40, 26718: 72, 26719: 104,
    26720: 216, 26721: 80, 26722: 48, 26723: 56, 26724: 112, 26725: 80,
    26726: 104, 26727: 88, 26728: 24, 26729: 64, 26730: 48, 26731: 104,
    26732: 80, 26733: 120, 26734: 184, 26735: 96, 26736: 96, 26737: 96
}

calib_0273 = {
    26714: ("Não é isso...CRD-dá uma trégua!", "Lyner desconcertado pedindo trégua a Misha com CR."),
    26715: ("Ai, ai... Mas que frouxo.CRHehehe...", "Misha rindo da covardia de Lyner sem rubricas com CR."),
    26716: ("A propósito, você tem um Anel Branco,CRné, Lyner?", "Misha reparando no Anel Branco no inventário de Lyner."),
    26717: ("Tenho sim.", "Lyner confirmando a posse do anel."),
    26718: ("Vai dar de presente pra alguém?", "Misha sondando se o anel tem destino romântico."),
    26719: ("Hã? Se for pra alguém equipar,CRacho que sim...", "Lyner respondendo pragmaticamente sobre utilidade de combate com CR."),
    26720: ("Ele protege contra sono e essas coisasCRquando equipado. E ainda dá um empurrãozinhoCRna defesa...", "Lyner listando atributos defensivos do anel com quebras CR."),
    26721: ("Ah, deixa pra lá...CRSe for só isso...", "Misha murchando desapontada com a insensibilidade de Lyner com CR."),
    26722: ("Ué, como assim?", "Lyner sem entender o desapontamento."),
    26723: ("Esquece...CRSem graça...", "Misha desdenhando a falta de tato de Lyner com CR."),
    26724: ("Tava pensando aqui...CRVocê tem o Anel Branco, né?", "Misha retomando o tópico do anel em outro momento de descanso."),
    26725: ("É... tipo... um presente pra alguém?", "Misha perguntando timidamente se o anel é presente."),
    26726: ("Hã? Não guardei com essa intenção.", "Lyner negando qualquer intenção de presente."),
    26727: ("Se você quiser, posso te dar.", "Lyner oferecendo o anel despretensiosamente."),
    26728: ("Por quê?", "Misha indagando o motivo da oferta de Lyner."),
    26729: ("Achei que você queria...", "Lyner justificando a oferta."),
    26730: ("...Não, não quero.", "Misha recusando dengosa o anel sem valor afetivo."),
    26731: ("Só perguntei por curiosidade.CRNem liga.", "Misha disfarçando o interesse com quebra CR."),
    26732: ("É? Se você diz, tudo bem...", "Lyner aceitando a recusa sem desconfiar."),
    26733: ("...Se fosse pra fazer par com você,CRaí eu queria...", "Misha murmurando seu desejo de um anel de casal com quebra CR."),
    26734: ("Você me disse que antigamente mais deCR30% da população era Reyvateil, né?", "Lyner lembrando a alta proporção histórica de Reyvateils com CR."),
    26735: ("Hã? É, mas isso foi há muito tempo.", "Misha confirmando o dado histórico ancestral."),
    26736: ("Nem imagino. Tantas ReyvateilsCRjuntas assim...", "Lyner imaginando o mundo antigo repleto de Reyvateils com CR."),
    26737: ("É? Eu acho bem melhor agora.", "Misha preferindo os dias atuais.")
}

all_ok = True
for tid, (txt, rat) in calib_0273.items():
    maxb = max_map_0273[tid]
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
    print("=== 0273 100% PERFEITO ===")

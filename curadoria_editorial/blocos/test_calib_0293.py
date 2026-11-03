import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0293 = {
    27194: 80, 27195: 168, 27196: 160, 27197: 136, 27198: 168, 27199: 208,
    27200: 48, 27201: 160, 27202: 144, 27203: 160, 27204: 136, 27205: 152,
    27206: 112, 27207: 176, 27208: 152, 27209: 136, 27210: 152, 27211: 112,
    27212: 112, 27213: 136, 27214: 112, 27215: 240, 27216: 176, 27217: 104
}

calib_0293 = {
    27194: ("Mesmo sendo um agrado... er...", "Lyner sem jeito com o mimo recebido. (64B <= 80B)"),
    27195: ("Foi mal! No colo de uma gataCRcomo eu, você nem consegueCRrelaxar de nervoso, né?", "Misha gabando-se de sua beleza deitada no colo com CRs. (150B <= 168B)"),
    27196: ("...Vejo que a sua modéstia continuaCRintacta. Mas isso me fez relaxar.", "Lyner ironizando a vaidade de Misha com afeto com CR. (136B <= 160B)"),
    27197: ("Uau, isso foi uma alfinetada?CRTá se vingando de mim?", "Misha fingindo ofensa divertida com CR. (104B <= 136B)"),
    27198: ("Mas brincadeiras à parte, me sintoCRmuito mais calma assim, e fico feliz.", "Misha admitindo o conforto e apego sinceros com CR. (136B <= 168B)"),
    27199: ("Então lá vou eu. Faz tempo,CRentão posso dar umas desafinadas,CRmas não vai rir de mim, ouviu?", "Misha avisando antes de tocar a ocarina Hama com CRs. (168B <= 208B)"),
    27200: ("Poxa... que pena...", "Misha lamentando com beicinho. (39B <= 48B)"),
    27201: ("A Provação da Lua! É mó injustiçaCRsó eu ter ficado de fora.", "Misha reclamando de ter sido excluída da Provação da Lua com termo canônico e CR. (111B <= 160B)"),
    27202: ("Se tivéssemos feito dupla,CRteria sido moleza passar.", "Misha confiante na força do vínculo com Lyner com CR. (102B <= 144B)"),
    27203: ("Queria reviver o clima de nós doisCRa sós, como no nosso reencontro...", "Misha nostálgica do reencontro a sós com CR. (143B <= 160B)"),
    27204: ("Como quando fugimos batendoCRnos soldados da Tenba?", "Lyner lembrando a fuga agitada de Tenba com CR. (94B <= 136B)"),
    27205: ("Isso! E agora tô muito mais forte.CRAmassava o Flute num segundo...", "Misha gabando-se de seu crescimento mágico contra Flute com CR. (122B <= 152B)"),
    27206: ("Digo... derrubava ele comCRum golpe só, fácil!", "Misha corrigindo o exagero agressivo com CR. (85B <= 112B)"),
    27207: ("...Pelo bem do Sr. Flute,CRacho que fiz bem em formarCRdupla com a Aurica.", "Lyner brincando sobre poupar Flute com CRs. (143B <= 176B)"),
    27208: ("Quem diria que a moça da autorizaçãoCRestaria num lugar daqueles.", "Misha comentando sobre o encontro inesperado com Mei Mei com CR. (132B <= 152B)"),
    27209: ("É. Mas o que mais me surpreendeuCRfoi ela estar tão diferente.", "Lyner surpreso com o contraste de Mei Mei com CR. (119B <= 136B)"),
    27210: ("Normalmente ela parece tão sériaCRe competente no trabalho, sabe?", "Lyner descrevendo a postura profissional de Mei Mei com CR. (123B <= 152B)"),
    27211: ("É, pensando bem, ela passaCRessa impressão mesmo.", "Misha concordando sobre a fachada profissional com CR. (95B <= 112B)"),
    27212: ("Mas vendo de perto...CRé até difícil descrever.", "Lyner comentando a personalidade peculiar da guardiã com CR. (87B <= 112B)"),
    27213: ("Hmm... Ela parece mais uma garotaCRcomum, pra falar a verdade.", "Misha definindo a normalidade de Mei Mei com CR. (119B <= 136B)"),
    27214: ("Mas você tá reparando demaisCRna Mei Mei, né?", "Misha manifestando ciúme dengoso com termo canônico e CR. (87B <= 112B)"),
    27215: ("É que eu a via toda manhã.CRNunca imaginei que conversaria com elaCRfora do serviço de autorização.", "Lyner justificando a curiosidade casual com CRs. (184B <= 240B)"),
    27216: ("Será que é só isso mesmo?CRVocê tem uma queda por garotas comCRar infantil, Lyner...", "Misha implicando com o gosto de Lyner por meninas jovens com CRs. (156B <= 176B)"),
    27217: ("E ao contrário de mim,CRlembrou dela na hora...", "Misha cobrando com ciúme o esquecimento do passado com CR. (96B <= 104B)")
}

all_ok = True
for tid, (txt, rat) in calib_0293.items():
    maxb = max_map_0293[tid]
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
    print("=== 0293 100% PERFEITO ===")

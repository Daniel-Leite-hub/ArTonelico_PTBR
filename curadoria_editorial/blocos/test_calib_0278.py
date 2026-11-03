import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0278 = {
    26834: 88, 26835: 136, 26836: 176, 26837: 136, 26838: 216, 26839: 112,
    26840: 152, 26841: 88, 26842: 104, 26843: 112, 26844: 64, 26845: 56,
    26846: 104, 26847: 64, 26848: 216, 26849: 96, 26850: 64, 26851: 112,
    26852: 152, 26853: 184, 26854: 40, 26855: 192, 26856: 120, 26857: 112
}

calib_0278 = {
    26834: ("Tô ótimo! Aquilo não foi nada.", "Lyner minimizando o golpe recebido em combate."),
    26835: ("É... Graças à sua proteção,CReu consigo cantar com toda a alma.", "Misha agradecendo a segurança para entoar Canções com CR."),
    26836: ("Obrigada. Mas se você me preocupar,CRnem consigo cantar direito.CRNão esquece disso!", "Misha avisando que a preocupação atrapalha o canto com quebras CR."),
    26837: ("Ei, Lyner. Lembra de quando vocêCRme protegeu na batalha outro dia?", "Misha retomando o tópico do combate com CR."),
    26838: ("Ah, proteger é exagero...CRDepois daquele golpe, eu mal conseguiaCRficar de pé...", "Lyner admitindo que ficou debilitado com quebras CR."),
    26839: ("...Obrigada. Mas não quero queCRfaça isso nunca mais.", "Misha pedindo para Lyner não se arriscar com CR."),
    26840: ("Ver você se ferir pra me proteger...CRNão me deixa nada feliz.", "Misha triste ao ver o sacrifício de Lyner com quebra CR."),
    26841: ("Também sei lutarCRum pouco, não esquece!", "Misha lembrando que sabe se defender com CR."),
    26842: ("Quando vi, já tava cheia de magiasCRnovas pra usar.", "Misha notando a ampliação de seu repertório mágico com CR."),
    26843: ("É porque você explorouCRa minha Cosmosfera, né?", "Misha atribuindo o poder ao Mergulho profundo de Lyner com CR."),
    26844: ("É, bem... é por aí.", "Lyner confirmando o avanço na Cosmosfera."),
    26845: ("...O quanto você já viu?", "Misha perguntando tímida sobre a profundidade vista."),
    26846: ("Quanto? Bom... fui bem fundoCRna sua mente...", "Lyner admitindo o mergulho em níveis profundos com CR."),
    26847: ("Ou seja, quase tudo...", "Misha constatando a transparência de sua alma."),
    26848: ("E-então... se eu tentasse esconderCRalguma coisa de você... você já saberiaCRde tudo na hora?", "Misha receosa de que Lyner leia todos os seus segredos com CR."),
    26849: ("N-não é como se eu lesseCRa sua mente!", "Lyner negando telepatia com quebra CR."),
    26850: ("Mas não é quase isso?", "Misha insistindo na proximidade psicológica."),
    26851: ("...Talvez um pouco.CRSerá que tô me achando?", "Lyner admitindo intuição com quebra CR."),
    26852: ("Acho que não. Pelo menos pareceCRque você entende o que sinto agora.", "Misha validando a sintonia afetiva de Lyner com CR."),
    26853: ("...Deixar um homem entrar no meu quartoCRà noite exige coragem e determinação,CRsabia...?", "Misha revelando a ousadia e o afeto de acolhê-lo à noite com CR."),
    26854: ("...É-é mesmo?", "Lyner desconcertado com a revelação."),
    26855: ("É sim! Mas sem pressa.CRSendo você, nem crio tanta expectativa...CRmas mesmo assim...", "Misha conformada e provocante sobre a lerdeza de Lyner com CR."),
    26856: ("Não posso esperar pra sempre!CRTrata de lembrar disso!", "Misha intimando Lyner a agir no futuro com CR."),
    26857: ("Pretende carregar essa ocarinaCRpra todo canto?", "Lyner reparando na ocarina de Misha com CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0278.items():
    maxb = max_map_0278[tid]
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
    print("=== 0278 100% PERFEITO ===")

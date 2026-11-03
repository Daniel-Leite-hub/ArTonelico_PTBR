import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0272 = {
    26690: 208, 26691: 72, 26692: 176, 26693: 56, 26694: 176, 26695: 152,
    26696: 120, 26697: 152, 26698: 88, 26699: 120, 26700: 184, 26701: 120,
    26702: 128, 26703: 112, 26704: 48, 26705: 136, 26706: 136, 26707: 112,
    26708: 104, 26709: 120, 26710: 56, 26711: 136, 26712: 96, 26713: 96
}

calib_0272 = {
    26690: ("Nunca comprei uma, mas dizem que essasCRcartas fazem o maior sucesso com todo mundo.", "Misha explicando a popularidade febril das cartas colecionáveis com CR."),
    26691: ("Nossa, então virou febre mesmo.", "Lyner impressionado com o sucesso das cartas."),
    26692: ("Comprou uma, quer colecionar todas.CRDizem que tem gente gastando fortunas.", "Misha detalhando a compulsão dos colecionadores de cartas com CR."),
    26693: ("I-isso já é loucura...", "Lyner perplexo com o fanatismo pelas cartas."),
    26694: ("Não vou te impedir de comprar,CRmas vê se não perde a cabeça.", "Misha aconselhando Lyner a ter moderação nas compras."),
    26695: ("Não quero ver você na rua da amarguraCRporque torrou tudo em cartinhas.", "Misha preocupada com a falência de Lyner por cartas colecionáveis."),
    26696: ("Isso é mais perigoso que vírus, credo...", "Lyner comparando o vício em cartas a um vírus perigoso."),
    26697: ("Ah é! Você tá com Água dos Sonhos, né?CRMe empresta um pouquinho?", "Misha pedindo emprestada a poção sonífera Água dos Sonhos."),
    26698: ("Empresto, mas... o que vai fazer?", "Lyner desconfiado da intenção de Misha."),
    26699: ("Tô com crises de insônia bem chatas.", "Misha revelando dificuldade para dormir."),
    26700: ("Aí tomo um gole antes de dormirCRpra apagar feito uma pedra na hora.", "Misha planejando tomar a poção para dormir rápido com CR."),
    26701: ("S-só eu acho isso perigoso pra caramba?", "Lyner achando arriscado o uso doméstico do sonífero."),
    26702: ("Acha? Se dá pra usar no dia a dia,CRé uma mão na roda, ué.", "Misha defendendo a praticidade doméstica do item com CR."),
    26703: ("Ei, Lyner.CRVocê tem a Água dos Sonhos, né?", "Misha pedindo a Água dos Sonhos em outro diálogo de descanso."),
    26704: ("Hum? Tenho sim.", "Lyner confirmando que possui o item."),
    26705: ("Minha insônia anda tão brava...CRSerá que você me dá um pouco?", "Misha pedindo a poção para aliviar sua insônia forte."),
    26706: ("Claro, toma aí. Se não dormir direito,CRo cansaço não passa.", "Lyner compreensivo entregando a poção para Misha descansar."),
    26707: ("Valeu! Em troca, vou te contarCRuma coisa bem legal.", "Misha agradecendo e prometendo uma confidência provocante com CR."),
    26708: ("Tomando isso, eu caio num sonoCRtão pesado...", "Misha descrevendo o efeito profundo do sono da poção com CR."),
    26709: ("Se quiser invadir minha cama à noite,CRa hora é essa.", "Misha provocando Lyner dengosa sugerindo o costume yobai com CR."),
    26710: ("O quê?! Ficou doida?!", "Lyner escandalizado e desconcertado com a insinuação."),
    26711: ("Não acordo por nada.CRMas nada de me machucar, tá?", "Misha fingindo submissão travessa com quebra CR."),
    26712: ("Não é essa a questão!...", "Lyner protestando contra o absurdo da conversa."),
    26713: ("Ué, por quê?CRComigo você não se anima?", "Misha cobrando atrevida se Lyner não tem desejo por ela com CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0272.items():
    maxb = max_map_0272[tid]
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
    print("=== 0272 100% PERFEITO ===")

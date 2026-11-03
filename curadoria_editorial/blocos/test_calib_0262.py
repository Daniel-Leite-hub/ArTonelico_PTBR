import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0262 = {
    26450: ("E-espera aí!CRNão é como se eu...", "Lyner tentando se justificar sem jeito sobre o fetiche."),
    26451: ("Não precisa entrar em pânico...CRAcertei na mosca?", "Misha provocando Lyner ao notar o constrangimento dele."),
    26452: ("Não", "Lyner negando de prontidão a acusação."),
    26453: ("Quer que eu vista?CRSe quiser, posso pôr agora mesmo!", "Misha oferecendo atrevidamente provar a lingerie para Lyner."),
    26454: ("Q-quê?! Já disse que não!CRNão é nada disso...", "Lyner em pânico cômico recusando a oferta indecente."),
    26455: ("Acha que não combina comigo...?", "Misha fingindo mágoa com carinha dengosa."),
    26456: ("N-não é isso...CRÉ que...", "Lyner se enrolando todo tentando não ofender Misha."),
    26457: ("...Pff!", "Misha segurando o riso diante do desespero de Lyner."),
    26458: ("Ahahaha! Brincadeirinha!CRTava só te provocando!", "Misha caindo na gargalhada e desfazendo a brincadeira."),
    26459: ("Provocando...?CRQual é, me dá um tempo...", "Lyner suspirando aliviado e repreendendo a pegadinha."),
    26460: ("Ahaha, foi mal!CRNão achei que vocêCRia entrar em pânico!", "Misha pedindo desculpas entre risos pelo susto de Lyner."),
    26461: ("Ai, que graça... E aí?", "Misha ainda rindo e retomando a pergunta."),
    26462: ("Visto ou não?", "Misha insistindo travessa na escolha da roupa."),
    26463: ("...Faz o que quiser.", "Lyner jogando a toalha desconcertado."),
    26464: ("Ah, lembrei de algoCRpra te falar.", "Misha mudando de tom para dar uma bronca séria."),
    26465: ("Um lugar alto à toa, bem na beiradaCRdo Porto Gaivota... No que tava pensando?!", "Misha repreendendo Lyner por se arriscar na ponta do abismo."),
    26466: ("Hã?! Em nada demais...CRSó queria ver a vista lá de cima...", "Lyner justificando inocentemente sua curiosidade pelo visual."),
    26467: ("Mas não precisava irCRtão perto da beirada!", "Misha cobrando prudência diante do perigo de queda."),
    26468: ("Quase não tinha chão e aquelas hélicesCRgirando lá embaixo... Aquele lugarCRé assustador demais!", "Misha descrevendo o pânico de altura e as hélices giratórias."),
    26469: ("Sério?CRNão achei tão assustador assim...", "Lyner demonstrando sua coragem e hábito de alturas."),
    26470: ("Mas eu tenho medo!!", "Misha berrando com sinceridade sobre seu pavor de altura."),
    26471: ("D-desculpa!", "Lyner se encolhendo e pedindo desculpas pelo susto."),
    26472: ("Poxa!... Só de ficar no Beco VagalumeCReu já morro de medo.", "Misha desabafando seu pavor crônico da fragilidade das cidades flutuantes sem rubrica teatral."),
    26473: ("E se der algo erradoCRe a gente cair a qualquer hora...?", "Misha explicando a ansiedade constante de queda no Mundo Inferior."),
}

max_map = {
    26450: 72, 26451: 104, 26452: 8, 26453: 128, 26454: 112, 26455: 88,
    26456: 72, 26457: 16, 26458: 136, 26459: 96, 26460: 120, 26461: 56,
    26462: 40, 26463: 56, 26464: 80, 26465: 168, 26466: 168, 26467: 104,
    26468: 200, 26469: 96, 26470: 48, 26471: 32, 26472: 128, 26473: 120
}

all_ok = True
for tid, (txt, rat) in calib_0262.items():
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
    print("=== 0262 100% PERFEITO ===")

import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0263 = {
    26474: ("Não seja tão pessimista...", "Lyner tentando amenizar a preocupação de Misha."),
    26475: ("Morando aqui, o perigo é real.", "Misha justificando o medo da instabilidade das plataformas."),
    26476: ("Enfim! Nada de ficarCRna beirada de novo à toa. Ouviu?!", "Misha impondo uma ordem expressa para a segurança de Lyner."),
    26477: ("Dizem que o parque em NemoCRé ótimo pra um encontro, né?", "Misha puxando assunto dengosa sobre o parque romântico."),
    26478: ("É, o Jack comentouCRalgo assim uma vez.", "Lyner lembrando dos comentários de Jack sobre o parque."),
    26479: ("Tinha casal lá em plena luz do dia...CRQue inveja boa.", "Misha confessando o desejo de viver um romance à luz do dia."),
    26480: ("É? Ficar grudado o dia inteiro assimCRnão me parece grande coisa...", "Lyner com seu ceticismo ingênuo sobre o grude dos casais."),
    26481: ("Mas a gente já tá assim!CRPassamos o dia juntos e dormimosCRna mesma estalagem.", "Misha apontando com picardia a rotina de intimidade dos dois."),
    26482: ("Mas é diferente.", "Lyner sem jeito tentando separar dever de romance."),
    26483: ("Ah! Vamos naquele parqueCRjuntos da próxima vez!", "Misha aproveitando a deixa para convidar Lyner."),
    26484: ("Hã? Por mim tudo bem ir lá...", "Lyner aceitando com despretensão o passeio."),
    26485: ("Ah, e vai ser um encontro.", "Misha soltando a bomba de que o passeio será um encontro a dois."),
    26486: ("Calma aí!CRAssim do nada...?", "Lyner pego no contrapé com a definição romântica."),
    26487: ("Nada disso! A gente vai!!", "Misha batendo o pé com determinação irresistível."),
    26488: ("Se não for, posso acabar confundindoCRa magia vermelha com a azulCRe disparar em você!", "Misha fazendo chantagem cômica sobre usar magia de combate (vermelha) em vez de suporte (azul)."),
    26489: ("...A-aí você me assusta...", "Lyner temendo a ameaça mágica de Misha."),
    26490: ("Então a gente vai, sim!", "Misha comemorando a vitória indiscutível."),
    26491: ("Nem posso recusar...", "Lyner resignado diante da pressão bem-humorada."),
    26492: ("Ah, sim.CRQueria te pedir um favor...", "Misha mudando de tom e ficando tímida."),
    26493: ("...Ué? O que foi?", "Lyner estranhando a hesitação repentina de Misha."),
    26494: ("Não é nada...CRSó fiquei com medoCRde você recusar...", "Misha demonstrando sua vulnerabilidade e medo de rejeição."),
    26495: ("Não vai ser nada absurdo, né?CREu tenho limites, sabia?", "Lyner tentando se precaver contra pedidos malucos."),
    26496: ("Não é nada demais... eu acho.", "Misha minimizando com modéstia o pedido."),
    26497: ("É que... queria ir ao parque com você...", "Misha revelando com doçura seu desejo sincero de passear no parque."),
}

max_map = {
    26474: 56, 26475: 96, 26476: 152, 26477: 128, 26478: 96, 26479: 128,
    26480: 176, 26481: 176, 26482: 48, 26483: 104, 26484: 80, 26485: 64,
    26486: 72, 26487: 56, 26488: 200, 26489: 64, 26490: 56, 26491: 48,
    26492: 80, 26493: 40, 26494: 128, 26495: 128, 26496: 64, 26497: 112
}

all_ok = True
for tid, (txt, rat) in calib_0263.items():
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
    print("=== 0263 100% PERFEITO ===")

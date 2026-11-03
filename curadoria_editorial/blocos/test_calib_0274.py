import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0274 = {
    26738: 184, 26739: 144, 26740: 160, 26741: 104, 26742: 136, 26743: 56,
    26744: 168, 26745: 64, 26746: 192, 26747: 104, 26748: 64, 26749: 136,
    26750: 136, 26751: 112, 26752: 136, 26753: 168, 26754: 64, 26755: 184,
    26756: 112, 26757: 104, 26758: 120, 26759: 72, 26760: 96, 26761: 128
}

calib_0274 = {
    26738: ("Se tivesse tantas assim, certo alguém bonzinhoCRia ficar bancando o herói pra todas elas.", "Misha justificando o ciúme de um mundo cheio de Reyvateils com CR."),
    26739: ("Aí ia chover de rivais,CRe a concorrência ia ser feroz...", "Misha temendo a concorrência pelo afeto de Lyner com CR."),
    26740: ("Ei, ei, tá falando sozinha sobre o quê?CRNão tô entendendo nada...", "Lyner confuso com os resmungos de Misha com CR."),
    26741: ("...É, mas a sua lerdezaCRnão tem cura mesmo.", "Misha alfinetando a falta de perspicácia de Lyner com CR."),
    26742: ("O Cais Flutuante na tormenta...CRSó de lembrar já me dá pavor.", "Misha relembrando o terror no Cais Flutuante com CR."),
    26743: ("Disso eu não discordo.", "Lyner concordando sobre o perigo do cais."),
    26744: ("Achei que se bobeasse um segundo,CRo vento ia me jogar pro além.", "Misha descrevendo a fúria dos ventos com CR."),
    26745: ("Quase chorei de verdade.", "Misha confessando o pavor sincero que sentiu."),
    26746: ("Lá não tem corrimão nem nada.CRSe o vento empurrasse mais forte,CRa queda era certeira.", "Lyner explicando o risco fatal da queda com quebras CR."),
    26747: ("...E-eu imaginei agora!CRIdiota, idiota, idiota!!", "Misha apavorada xingando Lyner em pânico com CR."),
    26748: ("D-desculpa!CRJá tá tudo bem.", "Lyner tranquilizando Misha desajeitado com CR."),
    26749: ("Uuh... Acho que fiquei com traumaCRdaquele Cais Flutuante...", "Misha traumatizada com a lembrança do local com CR."),
    26750: ("Como você sobe o Silvaplate daqueleCRjeito sem nem cansar, Lyner?", "Misha questionando o vigor físico sobre-humano de Lyner com CR."),
    26751: ("Hã? Não é como se fosse fácil subir lá.", "Lyner minimizando a escalada do Silvaplate."),
    26752: ("Não disse isso!CRMas você tá com garotas junto, sabia?", "Misha cobrando consideração com o ritmo feminino com CR."),
    26753: ("Até a Aurica cansou!CRCom o meu preparo físico zero,CReu fico no pó bem antes!", "Misha expondo seu sedentarismo cômico com quebras CR."),
    26754: ("É... tem razão.CRDesculpa.", "Lyner reconhecendo o erro com CR."),
    26755: ("Realmente, não precisava subir tudoCRde uma vez. Vou prestar mais atençãoCRda próxima vez.", "Lyner prometendo moderar o ritmo no futuro com CR."),
    26756: ("Pois é... Mas tem gente queCRmora num lugar daqueles.", "Misha admirada com os moradores do Silvaplate com CR."),
    26757: ("É. Tinha até umas velhinhasCRde idade lá, né?", "Lyner destacando a presença de idosas com CR."),
    26758: ("Tinha criança pequena e até meninaCRda minha idade.", "Misha lembrando crianças e jovens no local com CR."),
    26759: ("...O povo de lá tem muita energia.", "Lyner comentando o vigor dos habitantes."),
    26760: ("Normal não é, né?CRSó de escolher morar lá...", "Misha achando bizarro morar naquele precipício com CR."),
    26761: ("Lyner, você tá passando muito apertoCRna minha Cosmosfera?", "Misha puxando o gancho íntimo sobre sua mente com CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0274.items():
    maxb = max_map_0274[tid]
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
    print("=== 0274 100% PERFEITO ===")

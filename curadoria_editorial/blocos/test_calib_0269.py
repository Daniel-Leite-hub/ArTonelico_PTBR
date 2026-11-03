import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0269 = {
    26618: ("I-isso aí também seriaCRum problemão...", "Lyner desconcertado com a insinuação íntima de Misha."),
    26619: ("Nfufu~ No que tá pensando?CRTarado!", "Misha rindo travessa da mente fértil de Lyner."),
    26620: ("Hum... Será que fica estranhoCRse for só você?", "Misha comentando sobre o figurino tradicional masculino."),
    26621: ("Do que cê tá falando do nada?", "Lyner sem entender o tema do novo traje."),
    26622: ("Do hakama com brasão, ué.", "Misha esclarecendo que se refere ao traje tradicional montsuki hakama."),
    26623: ("Sabe em que ocasiãoCRse veste isso?", "Misha testando o conhecimento cerimonial de Lyner."),
    26624: ("Acho que é pra cerimônias,CRmas a defesa é tão altaCRque ajuda até em batalha.", "Lyner justificando a utilidade defensiva do traje cerimonial."),
    26625: ("Se você for lutar de hakama,CRtalvez eu devesse usar um quimono branco!", "Misha propondo usar a veste nupcial branca feminina (shiromuku) para combinar."),
    26626: ("P-por que faria isso?!", "Lyner em choque com a ideia de formarem um casal nupcial em campo."),
    26627: ("Se o hakama protege tanto,CRo quimono branco também deve proteger!", "Misha rebatendo com lógica cômica sobre trajes de casamento."),
    26628: ("Já que temos, por que não?CRTodo mundo vai se espantar!", "Misha animada com o escândalo cômico que causariam."),
    26629: ("Vão se espantar de qualquer jeito!CRGente lutando vestida de noivos...", "Lyner visualizando o absurdo de irem à guerra vestidos para casar."),
    26630: ("Ainda nem acredito que fomosCRàquele lugar de lembranças juntos.", "Misha emocionada ao recordar o regresso ao local nostálgico de infância."),
    26631: ("E que você finalmenteCRse lembrou do nosso passado...", "Misha comovida com o resgate das memórias compartilhadas."),
    26632: ("É... eu também me espantei.", "Lyner admitindo a surpresa por ter recuperado as lembranças."),
    26633: ("Como pude esquecer daquilo?CRMisha, fui injusto com você.", "Lyner se desculpando sinceramente pelo esquecimento."),
    26634: ("Tudo bem, você lembrou.CRIsso já basta.", "Misha perdoando Lyner com afeto sublime."),
    26635: ("E como eu disse lá: você continuarCRse esforçando tanto por mimCRjá é mais que suficiente!", "Misha expressando gratidão plena pela dedicação heróica de Lyner."),
    26636: ("...Ouvir isso me alivia tanto.", "Lyner reconfortado pela acolhida generosa de Misha."),
    26637: ("Não esquece de novo, ouviu?", "Misha pedindo com biquinho dócil para ele nunca mais esquecer."),
    26638: ("Ah, é. Tinha uma coisaCRque eu queria te dizer agora.", "Misha mudando de tom para introduzir a questão familiar."),
    26639: ("Lyner, faz as pazes com o Leard!CRFaça isso agora.", "Misha exigindo que Lyner se reconcilie com o pai Leard."),
    26640: ("Q-quer me obrigar?!", "Lyner espantado com a ordem categórica."),
    26641: ("Se eu não mandar,CRvocês nunca vão se acertar!", "Misha conhecendo a teimosia crônica de pai e filho."),
}

max_map = {
    26618: 96, 26619: 96, 26620: 112, 26621: 64, 26622: 64, 26623: 80,
    26624: 184, 26625: 144, 26626: 48, 26627: 160, 26628: 128, 26629: 152,
    26630: 136, 26631: 112, 26632: 64, 26633: 120, 26634: 88, 26635: 192,
    26636: 72, 26637: 64, 26638: 128, 26639: 112, 26640: 48, 26641: 112
}

all_ok = True
for tid, (txt, rat) in calib_0269.items():
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
    print("=== 0269 100% PERFEITO ===")

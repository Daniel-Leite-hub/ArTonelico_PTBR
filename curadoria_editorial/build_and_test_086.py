# -*- coding: utf-8 -*-
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

curated_translations = {
    # Event/448.evd (19361..19395)
    19361: "Lyner! Mas não é que é você mesmo?!",
    19362: "Quanto tempo, Radolf!",
    19363: "Tem passado bem?!",
    19364: "E você, Aurica? Quanto tempo também!",
    19365: "Ah, sim. Fico muito feliz em constatar\no perfeito bem-estar do Comandante-Geral Radolf.",
    19366: "Hahaha, \"Comandante-Geral\"?\nFazia um bom tempo que eu não ouvia esse título.",
    19367: "A verdade é que... depois de todos aqueles eventos,\nacabei sendo promovido a Bispo...",
    19368: "É sério?!\nMas isso é maravilhoso!",
    19369: "Pois é. Pelo visto, nunca houve precedentes\nde um cavaleiro ingressar no clero...",
    19370: "Mas disseram que fui sagrado Bispo\npor salvar a Igreja inteira daquela crise terrível.",
    19371: "Meus parabéns, Radolf!",
    19372: "Muitos parabéns, senhor!",
    19373: "Não, por favor... Ouvir vocês falarem\ncom tanta cerimônia assim me deixa até sem jeito!",
    19374: "Sendo assim, este lugar sagrado\njá não é mais uma igreja a serviço de Mir.",
    19375: "Agora, ela pertence ao povo e existe para o povo.",
    19376: "Então o seu sonho finalmente se realizou.",
    19377: "Pois é. Só que isto aqui é apenas a linha de partida.\nO trabalho duro começa de verdade agora! Hahaha!",
    19378: "...",
    19379: "Lyner...\nPrecisamos falar daquele assunto com ele...",
    19380: "O que foi?\nPor acaso vocês dois pretendem se casar?",
    19381: "C-claro que não...!\nPoxa vida...",
    19382: "Na verdade...\nTrata-se da Senhora Shurelia.",
    19383: "Compreendo! Então... isso quer dizer\nque ela talvez possa despertar de volta?!",
    19384: "Se encontrarmos o cristal chamado [RE Nation]...",
    19385: "Mas que esplêndida notícia! Sendo sincero, eu também fiquei arrasado naquela ocasião...\nQue alívio imenso... que alívio!",
    19386: "Por isso... pensamos se você não poderia\nnos ajudar na busca por esse cristal.",
    19387: "...Entendo. Então era isso.",
    19388: "Perdoe-me. Eu não posso deixar meus deveres agora.",
    19389: "...Radolf.",
    19390: "Nos velhos tempos, quando existia alguém acima de mim e eu só precisava cuidar dos meus próprios passos, tudo era mais simples.",
    19391: "Só que agora a realidade é outra. Se eu partir daqui, esta Igreja vai...",
    19392: "...Sinto muito.",
    19393: "N-não se preocupe,\nvocê não precisa se culpar por isso.",
    19394: "Fui eu quem chegou de repente com esse pedido. Diante das suas novas responsabilidades... é totalmente compreensível.",
    19395: "...Obrigado pela compreensão.",

    # Event/125.evd (19396..19428)
    19396: "Bom dia a todos.\nConseguiram repousar com tranquilidade esta noite?",
    19397: "Fiz diversas pesquisas desde ontem e, como imaginei,\no cristal parece mesmo repousar na [Colina do Canto].",
    19398: "A menos que o sítio tenha sido profanado por saqueadores,\ncom certeza ainda estará lá.",
    19399: "Que alívio... Finalmente poderei resgatar o cristal.\nVou partir para lá sem demora!",
    19400: "Ah, e mais uma coisa, Senhor Lyner.",
    19401: "Pode ser apenas um receio infundado da minha parte,\nmas...",
    19402: "Mesmo tratando-se de um valoroso Apóstolo de Elemia,\ndesbravar ruínas antigas sem uma Reyvateil ao seu lado será uma empreitada perigosa.",
    19403: "Se não for um incômodo, aceitaria levar Aurica\nconsigo como sua parceira de jornada?",
    19404: "...Eh?!",
    19405: "Como? Mas... Não seria abusar demais da sua bondade...?",
    19406: "Aurica ainda não foi vinculada a um parceiro, contudo,\nenxergo um potencial ilimitado florescendo dentro dela.",
    19407: "...Senhor Bispo?!",
    19408: "Minha querida Aurica, você aceitaria? A escolha final cabe unicamente ao seu coração.",
    19409: "...Sim! Se a minha presença puder ajudar...\ncumprirei este chamado com toda a minha dedicação!",
    19410: "E quanto a vós, Senhor Lyner? O que me diz?",
    19411: "Muito obrigado por essa oportunidade!",
    19412: "Aurica entrou para o grupo!",
    19413: "E você também, Radolf.\nAcompanhe-os e preste-lhes todo o auxílio necessário.",
    19414: "Às ordens, Eminência.",
    19415: "Radolf entrou para o grupo!",
    19416: "Obrigado por tudo o que fez por nós,\ndo fundo do coração.",
    19417: "Ah, mais um momento, Senhor Lyner.",
    19418: "Sim? O que deseja?",
    19419: "Aurica... é uma donzela que carrega o fardo doloroso de um passado cruel.",
    19420: "Por esse motivo, ela fechou o próprio coração\nem uma armadura impenetrável.",
    19421: "Para uma Reyvateil, sentimentos transbordantes e extrema sensibilidade são a fonte primordial para manifestar uma poderosa Magia da Canção.",
    19422: "...",
    19423: "Rogo-lhe encarecidamente... Traga paz e consolo\nao coração ferido daquela jovem.",
    19424: "...Sim, pode deixar comigo.",
    19425: "Que as bênçãos sagradas do Trio de Elemia recaiam sobre vós, Senhor Lyner...",
    19426: "Conto com você, Aurica.",
    19427: "...Sim!",
    19428: "O local [Colina do Canto] foi liberado no Mapa-Múndi!",

    # Event/552.evd (19429..19516)
    19429: "Ayatane!!",
    19430: "...Lyner.\nComo foi que você descobriu este local...?",
    19431: "Percorri o mundo inteiro investigando a verdade...\nSobre você e sobre Mir...",
    19432: "Ayatane... Por acaso pretende destruir a Plasma Bell?",
    19433: "Exatamente como naquela tragédia do passado,\nquando Mir foi selada...?!",
    19434: "...Acertou em cheio.",
    19435: "A missão que me foi outorgada\né destruir a Plasma Bell\ne precipitar a queda das Asas de Hórus...",
    19436: "Ayatane... Derrubando as Asas de Hórus,\no que você pretende alcançar com tanta destruição...?!",
    19437: "...O que pretendo alcançar?\nEu não sei disso, e nem tenho interesse em saber.",
    19438: "Esta é uma ordem expressa da minha Mãe.\nAcima de qualquer desejo próprio,\né um desígnio que tenho o dever de executar.",
    19439: "Mas e você, Ayatane...?\nO que o seu próprio íntimo deseja fazer?!",
    19440: "Para mim... basta construir um mundo\nonde a minha Mãe possa viver em felicidade e paz.",
    19441: "E farei qualquer sacrifício por esse objetivo.",
    19442: "Se for por essa razão, queremos o mesmo!\nEu também... desejo criar um mundo onde Mir viva em harmonia!",
    19443: "...O que você disse?!",
    19444: "Só que, para mim, não faz sentido\nse as pessoas deste mundo não puderem alcançar a felicidade juntas!",
    19445: "...",
    19446: "Ayatane, tente me compreender.\nEu não quero pura e simplesmente aniquilar Mir.",
    19447: "Ao escutar os relatos de incontáveis pessoas\nao longo da minha jornada, compreendi uma grande verdade.",
    19448: "Mir infligiu terríveis ataques ao povo, é fato,\nmas os seres humanos cometeram atrocidades ainda mais vis contra ela.",
    19449: "...",
    19450: "Se Mir não for um demônio corrompido pela maldade pura...",
    19451: "Acredito que, se acolhermos a dor dela com sinceridade absoluta, ela certamente compreenderá os nossos sentimentos.",
    19452: "Por isso... desista desse plano insano\nde derrubar as Asas de Hórus, eu te imploro...",
    19453: "Lamento decepcioná-lo, mas chegaram um instante tarde demais. O processo de \"reescrita\" da Criança da Luz já foi consumado.",
    19454: "A Plasma Bell só pode ser destruída pelo poder exercido por sua própria guardiã, a Criança da Luz.",
    19455: "E agora, ela está pronta para despedaçar a Plasma Bell com as próprias mãos.",
    19456: "O-o quê...?!",
    19457: "Você é a Kanade, não é?!\nÉ você mesma, Kanade?!",
    19458: "...",
    19459: "Lembro-me do apelo da Mei Mei.\nSe houver escolha, eu não quero lutar contra você...",
    19460: "Senhora Shurelia!\nNão existe nada que possamos fazer?!",
    19461: "...Nesta circunstância extrema,\nnão há outra saída senão forçar a sua paralisação emergencial.",
    19462: "Não é possível...",
    19463: "Ela... foi desativada?!",
    19464: "O-o quê?!",
    19465: "A Criança da Luz é a guardiã suprema dos sistemas da Torre. Nenhum golpe convencional será capaz de desativá-la.",
    19466: "Mas então... o que podemos fazer?!",
    19467: "Ayatane!!\nPor favor! Ajude-nos com o seu poder!!",
    19468: "...Eu...",
    19469: "Eu te imploro!!",
    19470: "...O que... acabou de acontecer...?!",
    19471: "Ayatane!!",
    19472: "Ayatane... Você está ferido...?!",
    19473: "Fufufu... Logo eu, cometer um disparate desses...\nO que foi que me deu na cabeça...?",
    19474: "Foi você quem neutralizou a Criança da Luz...?! Mas por que você...",
    19475: "...Quem sabe?\nTalvez eu também tenha querido... arriscar tudo... e apostar no seu ideal ingênuo...",
    19476: "...Ugh...",
    19477: "Não force a voz!",
    19478: "Eu estou... bem.\nBasta descansar um momento...\nque logo me recupero...",
    19479: "Lyner. Minha Mãe... Mir...\nestá com o espírito completamente aprisionado pelo ódio neste momento...",
    19480: "Contudo... em uma única ocasião no passado,\nela chegou a tecer uma canção pelos seres humanos...",
    19481: "Cantem essa canção para ela, por favor...",
    19482: "Você aguenta continuar?!",
    19483: "Mas é evidente...\nNão seria por tão pouco...\nque eu acabaria me desvanecendo...",
    19484: "E o que você pretende fazer\ndaqui para a frente, Ayatane...?",
    19485: "Pois é... o que farei?\nTalvez procurar algum refúgio solitário... onde possa desaparecer em silêncio...",
    19486: "Afinal, cometi a traição contra minha Mãe... É questão de tempo até que ela me apague da existência.",
    19487: "Se as coisas estão assim, venha conosco!\nVamos salvar Mir lado a lado!",
    19488: "...Percebo que você...\né um tolo ainda mais incorrigível do que eu julgava...",
    19489: "Deve ser justamente por isso que você tem tantos companheiros que confiam a própria vida a você.",
    19490: "Permita-me ser um deles também.\nAinda que eu não saiba quantos dias... ou quantos segundos de fôlego me restam...",
    19491: "Ayatane... muito obrigado!\nPode ter certeza de que eu jamais deixarei você se apagar.",
    19492: "De agora em diante...\nconto mais uma vez com a sua ajuda, amigo.",
    19493: "...",
    19494: "Ayatane entrou para o grupo!",
    19495: "E quanto à Criança da Luz...?",
    19496: "Não há com o que se afligir. Ela apenas despendeu energia sinfônica em demasia, mas não corre perigo.",
    19497: "Essas unidades recuperam o poder sinfônico adormecendo. Em breve despertará cheia de energia.",
    19498: "...Acabamos fazendo ela sofrer sem necessidade.",
    19499: "...",
    19500: "Isto aqui foi a mana Mei Mei\nque me pediu para lhe entregar...",
    19501: "Você colocou o [Pingente de Memória] no pescoço dela.",
    19502: "Vamos sair daqui por enquanto.",
    19503: "E afinal, onde fica guardada essa canção\nque Mir entoou no passado?",
    19504: "Com toda a certeza,\nela está guardada no interior do Silver Horn.",
    19505: "Dentro do Silver Horn?!\nSerá que é viável adentrar aquele local?",
    19506: "Em condições normais,\naquele não é um ambiente acessível a seres humanos em carne e osso.",
    19507: "Pois no âmago do chifre flui uma voragem descomunal de poder sinfônico, conhecida como o [Rugido dos Deuses].",
    19508: "Caso uma pessoa vulnerável encoste nessa torrente, poderá se desintegrar num átimo...",
    19509: "E-esperem aí, alto lá!...\nQuerem dizer que a gente vai se meter num lugar tenebroso desses?!",
    19510: "Creio que... com o vigor que possuímos agora,\nnossas vidas não devam correr perigo mortal.",
    19511: "Mir viveu encarcerada ali dentro.\nPor longas décadas... na mais absoluta solidão...",
    19512: "Até o momento de ser selada por Shurelia,\nela jamais dera um único passo no mundo exterior.",
    19513: "Naquele confinamento, Mir foi obrigada a tecer inúmeras canções.",
    19514: "E uma daquelas melodias\né o hino que viemos resgatar.",
    19515: "Compreendido.\nVamos partir... rumo ao Silver Horn!",
    19516: "O local [Silver Horn] foi liberado no Mapa-Múndi!"
}

with open("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_086_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

print(f"Total curated translations: {len(curated_translations)}")
assert len(curated_translations) == len(input_data["dialogues"])

hard_gate_errors = 0
lint_warnings = 0

for d in input_data["dialogues"]:
    item_id = d["id"]
    orig_jp = d["original_jp"]
    trad = curated_translations[item_id]

    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=trad,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {item_id}: {e}")

    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    parts = trad.split("\n")
    for line_part in parts[1:]:
        line_strip = line_part.strip()
        if line_strip.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1
        if line_part.startswith("..."):
            print(f"[ERROR] ID {item_id}: Line starts with reticências after newline: {line_part!r}")
            hard_gate_errors += 1

    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

print(f"\nPre-check results:")
print(f"Hard gate errors: {hard_gate_errors}")
print(f"Lint warnings: {lint_warnings}")

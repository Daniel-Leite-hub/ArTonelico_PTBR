# -*- coding: utf-8 -*-
"""
assemble_blk077.py - Montagem, Curadoria Editorial e LQA de Elite para BLK_EVD_077
Ar tonelico: Melody of Elemia (Undub) - Localizacao PT-BR
"""

import os
import sys
import json
import re
from pathlib import Path

# Inserir caminho do validador editorial da skill
sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

INPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_077_input.json")
OUTPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_077_output.json")
REPORT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_077_report.json")

# Carregar dados de entrada
with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Dicionario com textos curados e notas criticas para cada uma das 194 falas
CURATED_MAP = {
    # =========================================================================
    # CENA 1: Event/372.evd (17407 - 17465, 59 falas)
    # Reunião no Alto Comando de Platina: Radolf ajoelhado diante de Leard,
    # revelação de Kyle Clancy / Falss, retorno de Jack e Krusche com o hino
    # de Misha, Shurelia exausta e despedida de Ayatane.
    # =========================================================================
    17407: (
        "Desta vez, os membros de nossa Igreja causaram\ntranstornos incomensuráveis a Platina.",
        "Radolf assume com reverência e pesar o fardo dos atos da Igreja de Elemia perante o Comandante Leard."
    ),
    17408: (
        "Incontáveis feridos e danos catastróficos...\nPara expiar tamanha culpa, ofereço minha própria vida...",
        "Radolf ajoelha-se e oferece a própria vida em expiação militar e religiosa."
    ),
    17409: (
        "Espere um momento!\nDeixe de se prostrar desse jeito e levante a cabeça.",
        "Leard rejeita o sacrifício cego e ordena que Radolf se levante com dignidade."
    ),
    17410: (
        "Mas, senhor Comandante...!",
        "Radolf hesita, constrangido pela própria honra."
    ),
    17411: (
        "Radolf?!",
        "Lyner entra na sala e se espanta com a postura de Radolf."
    ),
    17412: (
        "Lyner!",
        "Shurelia reconhece a chegada de Lyner."
    ),
    17413: (
        "Radolf, o que você pensa que está fazendo?!",
        "Lyner reage indignado ao ver o companheiro subjugado."
    ),
    17414: (
        "Lyner... Eu estava prestando\nminhas desculpas ao senhor Comandante.",
        "Radolf explica com sobriedade sua atitude de penitência."
    ),
    17415: (
        "Pai! Não precisava deixá-lo ir tão longe!!",
        "Lyner confronta o próprio pai em defesa de Radolf."
    ),
    17416: (
        "Espere, Lyner! Eu agi por vontade própria.\nNão foi uma ordem do senhor Comandante.",
        "Radolf esclarece que o ato de penitência partiu de si mesmo."
    ),
    17417: (
        "Você não tem jeito...\nQuantas vezes já disse para não se precipitar?\nVocê nunca aprende mesmo.",
        "Leard repreende o ímpeto impulsivo do filho com autoridade paternal."
    ),
    17418: (
        "O quê?!",
        "Lyner protesta indignado com a frieza do pai."
    ),
    17419: (
        "Enfim, deixemos isso de lado.\nVamos voltar ao assunto principal.",
        "Leard retoma a pauta estratégica da reunião."
    ),
    17420: (
        "Já ouvi o relato do jovem Radolf.\nConfesso que não pude esconder o meu espanto.",
        "Leard expressa a gravidade das revelações sobre Falss."
    ),
    17421: (
        "O homem que se apresentava como Falss\natende na verdade por Kyle Clancy.",
        "Revelação da verdadeira identidade do Bispo Falss como Kyle Clancy."
    ),
    17422: (
        "Ele era o Magistrado Técnico aqui em Platina no passado.",
        "Histórico de Falss como ex-autoridade técnica e administrativa de Platina."
    ),
    17423: (
        "O quê?! Então o Bispo Falss era...\num Apóstolo de Elemia...?!",
        "Lyner descobre a identidade conspiratória de Falss."
    ),
    17424: (
        "Exatamente.",
        "Leard confirma a conclusão estarrecida de Lyner."
    ),
    17425: (
        "Aquele homem cobiçava o poder.\nE, nessa ambição, acabou descobrindo sobre Mir.",
        "Leard expõe a ambição desmedida que levou Clancy à corrupção."
    ),
    17426: (
        "Contudo, pensar que aquele homem, dado como morto,\nestava vivo na Igreja de El Elemia...",
        "Leard reflete sobre a sobrevivência secreta de Kyle Clancy nas fileiras eclesiásticas."
    ),
    17427: (
        "Nós também não soubemos distinguir o sublime\nTrio de Elemia de Mir, caindo nessa cega insensatez.",
        "Radolf confessa com amargura a ingenuidade da Igreja ao confundir Mir com as Deusas de Elemia."
    ),
    17428: (
        "Estou plenamente resignado a acatar qualquer punição.",
        "Radolf reitera sua submissão disciplinar irrestrita."
    ),
    17429: (
        "Não se martirize por isso.\nNo caso presente, não cabe culpar este ou aquele lado.",
        "Leard desfaz o clima punitivo com sabedoria política e bom senso."
    ),
    17430: (
        "Vossa generosidade é maior do que mereço...",
        "Radolf agradece com humilde reverência a compaixão de Leard."
    ),
    17431: (
        "Opa!!\nPelo visto, acabei voltando numa hora bem tensa...",
        "Jack entra quebrando o tom solene com seu humor descontraído."
    ),
    17432: (
        "Deixe de falar bobagens.",
        "Krusche corta a ironia de Jack com sua objetividade ríspida."
    ),
    17433: (
        "Jack! Krusche!",
        "Lyner saúda o retorno tempestivo dos companheiros."
    ),
    17434: (
        "O Esquadrão de Busca acaba de retornar!\nA busca pelo hino da Cantora das Estrelas\ne o selamento de Mir foram concluídos.",
        "Jack reporta a conclusão oficial da missão de resgate do hino de Misha e contenção de Mir."
    ),
    17435: (
        "Então o canto que ressoou naquela hora era mesmo...\no hino da Misha!",
        "Aurica compreende que a melodia salvadora foi tecida pelo sacrifício de Misha."
    ),
    17436: (
        "Excelente trabalho na missão de busca.",
        "Leard elogia formalmente a eficácia da equipe expedicionária."
    ),
    17437: (
        "Mas digam uma coisa:\npor que as ruas de Platina estão tão devastadas?",
        "Krusche questiona a destruição generalizada ao redor da cidade flutuante."
    ),
    17438: (
        "Porque a divisão de nossa Igreja de El Elemia\nse descontrolou e causou desordem na cidade.",
        "Radolf assume a responsabilidade militar pelas invasões dos cavaleiros corrompidos."
    ),
    17439: (
        "...Eu já desconfiava.\nAo ver o estado de Em Pheyna, imaginei que a coisa estivesse feia.",
        "Jack conecta o caos de Platina aos distúrbios enfrentados em Em Pheyna."
    ),
    17440: (
        "Diga, Jack...\nE a Misha?",
        "Aurica demonstra preocupação imediata pelo paradeiro de Misha."
    ),
    17441: (
        "A Misha está... entoando seu canto em Em Pheyna\npara cumprir sua sagrada missão até o fim.",
        "Jack relata o sacrifício ininterrupto de Misha na câmara de canto sagrada."
    ),
    17442: (
        "...Compreendo.\nSerá que posso visitá-la qualquer dia?\nEu queria muito expressar minha gratidão...",
        "Aurica almeja retribuir pessoalmente sua dívida de gratidão a Misha."
    ),
    17443: (
        "Claro. A Misha com certeza vai adorar.",
        "Jack encoraja a visita afetuosa e reconfortante de Aurica."
    ),
    17444: (
        "Que alívio!\nA Misha se tornou a salvadora da minha vida.",
        "Aurica reconhece com comoção profunda o valor inestimável do resgate operado por Misha."
    ),
    17445: (
        "Por isso, queria lhe agradecer pessoalmente algum dia.",
        "Aurica reitera sua gratidão sincera."
    ),
    17446: (
        "Bom, de qualquer forma,\nparece que o caso está encerrado por ora.",
        "Jack sintetiza o alívio momentâneo após a tempestade."
    ),
    17447: (
        "O nosso dever começa agora!\nTodos os Cavaleiros dedicarão força total\nà reconstrução de Platina!",
        "Radolf convoca a ordem dos cavaleiros para a reconstrução cívica da capital."
    ),
    17448: (
        "Sim, senhor!",
        "Cavaleiro responde afirmativamente com disciplina militar."
    ),
    17449: (
        "Sim, senhor!",
        "Segundo cavaleiro responde prontamente em uníssono."
    ),
    17450: (
        "...",
        "Shurelia silencia, demonstrando sinais de exaustão e aflição oculta."
    ),
    17451: (
        "Senhora Shurelia...?",
        "Lyner nota a fragilidade momentânea da Administradora da Torre."
    ),
    17452: (
        "Senhora Shurelia!!",
        "Ayatane aproxima-se alarmado com o estado de Shurelia."
    ),
    17453: (
        "A senhora está bem?!\nEstá se sentindo mal?\nExigiu demais de si mesma!",
        "Ayatane adverte com zelo e extrema lealdade pelo bem-estar de Shurelia."
    ),
    17454: (
        "...Talvez tenha razão.\nDesta vez, admito que esgotei boa parte de minhas forças.",
        "Shurelia confessa o desgaste físico e ressonante gerado pelo embate contra Mir."
    ),
    17455: (
        "...",
        "Ayatane observa compenetrado e apreensivo."
    ),
    17456: (
        "Poderiam... me conceder licença para descansar um instante?",
        "Shurelia pede permissão formal para retirar-se aos seus aposentos."
    ),
    17457: (
        "Com certeza!\nDeixe que nós cuidaremos de todo o restante.",
        "Ayatane tranquiliza a governante de Platina com presteza."
    ),
    17458: (
        "Por favor, vá descansar.",
        "Lyner reforça o pedido com genuína consideração e carinho."
    ),
    17459: (
        "Agradeço a compreensão. Com licença de todos.",
        "Shurelia despede-se com cortesia nobre e etérea."
    ),
    17460: (
        "...",
        "Ayatane guarda silêncio com ar pensativo e enigmático."
    ),
    17461: (
        "Acho que também me sinto um tanto cansado.\nVou me recolher para descansar um pouco.",
        "Ayatane retira-se discretamente seguindo os passos de Shurelia."
    ),
    17462: (
        "Sendo assim, dou esta reunião por encerrada por hoje.",
        "Comandante Leard encerra oficialmente a assembleia dos guardiões."
    ),
    17463: (
        "Jack entrou para o grupo!\nKrusche entrou para o grupo!",
        "Notificação do sistema confirmando o ingresso de Jack e Krusche na equipe ativa."
    ),
    17464: (
        "Ayatane deixou o grupo.",
        "Notificação do sistema registrando a saída de Ayatane do grupo."
    ),
    17465: (
        "Os equipamentos de Ayatane foram removidos.\nAcesse a opção \"Equipamento\" no menu principal para reorganizá-los.",
        "Instrução de tutorial sobre redistribuição de equipamentos da equipe."
    ),

    # =========================================================================
    # CENA 2: Event/262.evd (17466 - 17493, 28 falas)
    # Perseguição no Aeroporto: Lyner, Krusche e Jack perdem a aeronave de
    # Misha, encontram Aurica desolada chamando a si mesma de defeituosa,
    # acolhem-na no grupo e partem juntos rumo à Placa Hexagonal.
    # =========================================================================
    17466: (
        "Droga! Chegamos tarde demais...",
        "Lyner lamenta a perda do horário de embarque da aeronave de Misha."
    ),
    17467: (
        "Com licença! Na aeronave de agora há pouco,\nnão embarcou uma garota baixinha vestindo roupa azul?!",
        "Krusche indaga o atendente do aeroporto buscando pistas de Misha."
    ),
    17468: (
        "Sim! Ela subiu no último instante,\nquase perdeu o embarque.",
        "Funcionário confirma o embarque frenético da passageira."
    ),
    17469: (
        "...!!\nMuito obrigada pela informação...!",
        "Krusche agradece com prontidão feminina."
    ),
    17470: (
        "Não há dúvida.\nEla partiu naquela aeronave agora mesmo.",
        "Krusche conclui que perderam o rastro imediato de Misha."
    ),
    17471: (
        "Que droga... Chegamos um passo atrasados...",
        "Jack lamenta o desencontro frustrante."
    ),
    17472: (
        "Ué? ...Aurica?!",
        "Lyner avista Aurica perambulando pelo terminal."
    ),
    17473: (
        "Hã?",
        "Krusche estranha a surpresa repentina de Lyner."
    ),
    17474: (
        "Aurica, o que você está fazendo por aqui?\nNão devia estar na igreja?",
        "Lyner estranha a presença de Aurica longe de suas obrigações clericais."
    ),
    17475: (
        "...Tudo bem.\nMesmo que eu fique por aqui, ninguém se importa mesmo...",
        "Aurica expressa seu costumeiro complexo de inferioridade e rejeição."
    ),
    17476: (
        "Mas que baita coincidência nos esbarrarmos num lugar desses!",
        "Jack ressalta o acaso improvável do encontro."
    ),
    17477: (
        "Pois é, tem toda razão.\nA propósito, cadê a Misha?",
        "Aurica procura saber o paradeiro da companheira."
    ),
    17478: (
        "Acontece que...",
        "Lyner hesita antes de contar a fuga de Misha."
    ),
    17479: (
        "Entendi...\nEu também vou ajudar a procurá-la.",
        "Aurica prontifica-se solidária a apoiar as buscas."
    ),
    17480: (
        "Sério?!\nMas o Radolf e os outros não vão se preocupar com você?",
        "Lyner preocupa-se com as responsabilidades de Aurica junto aos Cavaleiros."
    ),
    17481: (
        "Não tem problema.\nNinguém se preocupa comigo mesmo...",
        "Aurica reafirma sua melancolia interior com resignação."
    ),
    17482: (
        "Além do mais, eu... sou apenas um produto com defeito...",
        "Aurica desvaloriza-se chamando a si mesma de produto defeituoso (kekkanhin)."
    ),
    17483: (
        "...C-Como assim?\nAgora você está me deixando preocupado...",
        "Lyner sente aflição diante da fragilidade emocional de Aurica."
    ),
    17484: (
        "Não se preocupe.\nEu estou... exatamente como sempre.",
        "Aurica tenta disfarçar a tristeza existencial."
    ),
    17485: (
        "De qualquer jeito,\nvamos atrás dela no próximo voo!",
        "Jack prioriza a perseguição imediata à rota de Misha."
    ),
    17486: (
        "Chegou!\nVamos embarcar depressa!",
        "Krusche avisa a chegada da próxima nau voadora."
    ),
    17487: (
        "...",
        "Aurica hesita antes de tomar a decisão de acompanhar o grupo."
    ),
    17488: (
        "Aurica! Você está bem?!",
        "Lyner estende a mão com preocupação afetuosa."
    ),
    17489: (
        "Sim... tudo bem...\nVamos.",
        "Aurica aceita o acolhimento do grupo e toma coragem."
    ),
    17490: (
        "Aurica entrou para o grupo!",
        "Notificação do sistema registrando o ingresso de Aurica no grupo ativo."
    ),
    17491: (
        "A Misha foi para a Placa Hexagonal, não foi?",
        "Krusche confirma a rota traçada pela fugitiva."
    ),
    17492: (
        "Sim, exatamente.",
        "Lyner valida o destino da perseguição."
    ),
    17493: (
        "Beleza, vamos voando para a Placa Hexagonal!",
        "Jack comanda a partida rumo à colossal estrutura de suspensão."
    ),

    # =========================================================================
    # CENA 3: Event/631.evd (17494 - 17560, 67 falas)
    # Cosmosfera de Misha: O confronto catártico contra o avatar do Pai Teimoso
    # (Ganko Oyaji / Leard), a explosão da mágoa infantil, o desabafo,
    # a reconciliação e o tecer da Magia Vermelha [Pai Teimoso], além do
    # desfecho de falha se Lyner interferir na fúria de Misha.
    # =========================================================================
    17494: (
        "Pai, chegamos em casa.",
        "Persona da irmã acolhedora anuncia o retorno ao lar onírico."
    ),
    17495: (
        "Toma, seu saquê!\nTrouxemos como você pediu.",
        "Misha entrega a bebida ao pai rabugento com rispidez."
    ),
    17496: (
        "Que demora!! O que vocês ficaram fazendo até agora?!\nSe atrasar desse jeito, não serve para nada!!",
        "Avatar de Leard esbraveja com autoritarismo exasperado."
    ),
    17497: (
        "O-O que deu em você?!\nA gente teve o maior trabalho para trazer sua bebida,\npor que precisa falar desse jeito?!",
        "Misha rebela-se contra a ingratidão do pai postiço."
    ),
    17498: (
        "Misha?!\nCalma, se acalma!",
        "Lyner tenta apaziguar a discussão crescente."
    ),
    17499: (
        "Não me acalmo coisa nenhuma!\nHoje eu não perdoo ele de jeito nenhum!",
        "Misha atinge o ápice do descontrole acumulado por anos."
    ),
    17500: (
        "Misha, pai, parem com isso vocês dois!!",
        "Irmã tenta em vão intervir no conflito doméstico."
    ),
    17501: (
        "Fique de fora, mana!\nEu perdi a paciência de vez!\nVou falar tudo o que está engasgado na cara desse velho!",
        "Misha explode decidida a confrontar todas as imposições sofridas."
    ),
    17502: (
        "Sua pirralha insolente!\nDeixei você abrir a boca e já está se achando...\nVenha se tiver coragem!",
        "Avatar paterno desafia a audácia da pupila rebelada."
    ),
    17503: (
        "Escuta aqui, seu velho teimoso: o mundo não gira em torno de você!\nSe eu demorava para memorizar os hinos ou evoluía devagar,\nera tudo baseado no seu padrão absurdo!",
        "Misha expõe a opressão dos rígidos padrões de canto que lhe foram cobrados."
    ),
    17504: (
        "...Hinos?!",
        "Lyner estranha a menção a hinos no contexto de um conflito doméstico."
    ),
    17505: (
        "E ainda vinha com conversa de que a sensibilidade artística nasce no limite do desespero, me trancando no quarto sob pretexto de 'treinamento especial'!\nNum sufoco daqueles, ninguém consegue tecer hino nenhum!",
        "Misha denuncia os métodos draconianos de isolamento para despertar a fônica."
    ),
    17506: (
        "Sua mal-agradecida...\nO que pensa que é o amor de um pai?!",
        "O mestre justifica a severidade como zelo protetor paternal."
    ),
    17507: (
        "Que amor de pai o quê!\nSe tivesse um pingo de consideração paterna,\nteria me comprado pelo menos um lanche infantil quando eu era pequena!",
        "Misha desabafa a dor infantil de nunca ter recebido um mimo afetuoso como um prato infantil."
    ),
    17508: (
        "Vivia repetindo 'vire logo adulta, vire adulta',\nera só isso o tempo todo, e nunca me deixava brincar...",
        "O drama da perda prematura da infância em nome da missão cósmica."
    ),
    17509: (
        "Por sua culpa, as lembranças da minha infância foram despedaçadas!\nDevolva o meu tempo de infância, seu monstro!!",
        "O grito de revolta de Misha cobrando os anos roubados de sua juventude."
    ),
    17510: (
        "Nossa! E-Espera aí, Misha?!",
        "Lyner assusta-se com o poder bélico disparado por Misha."
    ),
    17511: (
        "Maldita! Atrever-se a cuspir fogo contra seu próprio mestre?!\nTome isto!!",
        "Avatar paterno contra-ataca com magia inflamada."
    ),
    17512: (
        "Senhor Lyner, aqui está perigoso demais!\nVamos nos abrigar lá fora por enquanto!",
        "Irmã puxa Lyner para fora da zona de fogo cruzado."
    ),
    17513: (
        "Mas e a Misha...?!",
        "Lyner teme pela integridade física da heroína."
    ),
    17514: (
        "Ela vai ficar bem.\nDepressa, para fora...!",
        "A irmã assegura que Misha aguenta o confronto."
    ),
    17515: (
        "Por que será que a Misha detesta tanto o pai dela...?",
        "Lyner reflete sobre a raiz de tanto rancor acumulado."
    ),
    17516: (
        "Desde criança, ela aprendia tudo com o nosso pai.",
        "Revelação da tutoria precoce de Misha por Leard."
    ),
    17517: (
        "Com aquele velho teimoso?!",
        "Lyner reage chocado com a figura do tutor."
    ),
    17518: (
        "Sim. Ele é teimoso e egoísta, mas é um homem de mente brilhante.",
        "Descrição precisa da personalidade genial e implacável de Leard."
    ),
    17519: (
        "Como a Misha demonstrava enorme talento, nosso pai se entusiasmou e começou a impor treinamentos duríssimos.\nEla suportou tudo calada por muito tempo.",
        "A explicação psicológica da pressão desmedida sobre o talento prodígio."
    ),
    17520: (
        "Acredito que agora toda essa mágoa acumulada finalmente explodiu.",
        "Catarse emocional inevitável na Cosmosfera."
    ),
    17521: (
        "...Não imaginava que fosse assim...",
        "Lyner absorve o impacto da dor oculta de Misha."
    ),
    17522: (
        "Mas acho que, nessas horas, é melhor desabafar tudo de uma vez.\nPor isso, vamos aguardar até que terminem.",
        "Sabedoria terapêutica onírica sobre a necessidade do desabafo."
    ),
    17523: (
        "É... Faz sentido...",
        "Lyner concorda timidamente com a estratégia."
    ),
    17524: (
        "Sim. Depois que extravasam e brigam para valer,\nas coisas costumam se resolver bem mais fácil.",
        "Perspectiva acolhedora de alívio e reconciliação pós-conflito."
    ),
    17525: (
        "Você é bem decidida, moça...",
        "Lyner admira a firmeza tranquila da irmã mais velha."
    ),
    17526: (
        "...",
        "Pausa cênica enquanto a batalha doméstica se desenrola."
    ),
    17527: (
        "...",
        "Tensão silenciosa enquanto o confronto ecoa dentro da cabana."
    ),
    17528: (
        "Arf... arf...",
        "Misha respira ofegante após descarregar toda a sua fúria (sem rubricas teatrais)."
    ),
    17529: (
        "Arf... arf... Sua fedelha insolente...",
        "Pai exausto responde entre arquejos com orgulho ferido mas enternecido."
    ),
    17530: (
        "Por hoje... fica por isso mesmo... Dou-me por satisfeita...\nseu velho ranzinza... arf... arf...",
        "Misha concede trégua entre suspiros de cansaço."
    ),
    17531: (
        "Ai, ai... Que confusão dos diabos...",
        "Lyner entra e constata o cenário de destruição mútua."
    ),
    17532: (
        "Mas admito... Misha...\nVocê ficou... muito forte...\nQuando era pequena, não passava de uma pirralha indefesa...",
        "O mestre reconhece com admiração comovida o crescimento incomensurável de sua aluna."
    ),
    17533: (
        "...Arf... arf...",
        "Misha recupera o fôlego surpresa com o elogio genuíno."
    ),
    17534: (
        "...Estou muito orgulhoso.",
        "O amor paternal e orgulho do mestre enfim manifestados sem máscaras."
    ),
    17535: (
        "Mestre...",
        "Misha emociona-se ao ouvir as palavras que sempre ansiou por escutar de Leard."
    ),
    17536: (
        "...",
        "Momento solene de silêncio e reconciliação filial profunda."
    ),
    17537: (
        "Obrigada...",
        "Misha agradece com sincera ternura filial."
    ),
    17538: (
        "Misha teceu a Magia Vermelha [Pai Teimoso]!",
        "Desbloqueio da Magia Vermelha cômica fruto da superação do trauma infantil."
    ),
    17539: (
        "No fim das contas, o que meu pai era para a Misha?",
        "Lyner indaga o papel real de Leard na formação da garota."
    ),
    17540: (
        "...Você não lembra mesmo, né?\nBem, até eu já tinha me esquecido, então estranho seria se você se lembrasse.",
        "Kanan ironiza a memória esquecida da infância em Platina."
    ),
    17541: (
        "Desculpe aí...",
        "Lyner desculpa-se encabulado."
    ),
    17542: (
        "O Comandante-Geral Leard foi o mestre que a instruiu em Magia da Canção.\nEle a treinou com afinco antes que ela assumisse sua missão, para que fosse capaz de realizá-la.",
        "Explicação canônica do papel de Leard como preceptor supremo de Misha."
    ),
    17543: (
        "Para a Misha, foi um processo doloroso.\nTanto que essa mágoa contra Leard ficou guardada nas profundezas da alma dela...",
        "Revelação da raiz psíquica do bloqueio na Cosmosfera."
    ),
    17544: (
        "Aquele meu pai... Ele já aprontava essas coisas desde aquela época...",
        "Lyner lamenta a rigidez paterna comovido com a luta de Misha."
    ),
    17545: (
        "Mas, depois de gritar até cansar, a Misha parece bem mais aliviada agora.",
        "Diagnóstico do sucesso terapêutico da catarse."
    ),
    17546: (
        "...Hã?",
        "Lyner sente a vibração onírica da transformação do paradigma."
    ),
    17547: (
        "A Mudança de Paradigma...",
        "Lyner reconhece a quebra da barreira psicológica do nível da Cosmosfera."
    ),
    17548: (
        "...Viu só?",
        "Moradora do Mundo Inferior confirma com cumplicidade."
    ),
    17549: (
        "Cala a boca!\nComo você espera que eu fique calma numa hora dessas?!",
        "Linha da rota alternativa/falha quando o jogador tenta conter a fúria de Misha precocemente."
    ),
    17550: (
        "Não, mas...",
        "Lyner tenta intervir sem jeito na discussão."
    ),
    17551: (
        "Quer ficar no meu caminho?!\nSe tentar me atrapalhar, Lyner,\neu não vou ter piedade nem de você!",
        "Misha avisa que não poupará ninguém que se interponha em sua catarse."
    ),
    17552: (
        "Ai!... P-Por que isso sempre acaba sobrando para mim?!",
        "Lyner reage assustado ao se ver como alvo da ira fônica."
    ),
    17553: (
        "Agora não tem quem me segure!\nToda essa raiva e indignação precisam explodir!\nQuem tentar me impedir vai levar porrada!",
        "A força desmedida da cólera reprimida de Misha em ebulição."
    ),
    17554: (
        "Lá vai!\nToma essa!!",
        "Misha ataca Lyner em surto fônico cômico."
    ),
    17555: (
        "Uou! Ei, pare com isso!\nDói, tá doendo pra valer!",
        "Lyner apanha comicamente no mundo dos sonhos."
    ),
    17556: (
        "...Ela te deu uma surra daquelas, hein?\nIsso acontece porque você se mete a tentar pará-la sem pensar.",
        "Kanan zomba da impulsividade tola de Lyner."
    ),
    17557: (
        "Mesmo assim...",
        "Lyner tenta justificar suas boas intenções todo machucado."
    ),
    17558: (
        "Às vezes, dentro do coração, o melhor é colocar tudo para fora até purificar.\nSe tentar conter nessa hora, a energia acaba explodindo...",
        "Lição fundamental sobre o manejo de emoções na Cosmosfera."
    ),
    17559: (
        "Bem, seja como for, se ainda tiver disposição,\ntente outra vez quando estiver pronto.",
        "Dica do jogo para tentar novamente o evento após a falha."
    ),
    17560: (
        "...É... Tá bom...",
        "Lyner consente resignado e dolorido."
    ),

    # =========================================================================
    # CENA 4: Event/24.evd (17561 - 17600, 40 falas)
    # Oficina de Grathmeld em Karff: Conclusão do teste prático de Lyner com
    # Pombad, piada de casamento com a neta Narl, entrega de Pedras Azuis e
    # Vermelhas, preparação do Míssil e revelação cômica do fora que Jack levou.
    # =========================================================================
    17561: (
        "Oh-oh! Você finalmente conseguiu sintetizar!",
        "Pombad celebra com entusiasmo o sucesso prático de Lyner no caldeirão sonoro."
    ),
    17562: (
        "E então? O que achou do resultado?",
        "Lyner apresenta a criação alquímica com expectativa juvenil."
    ),
    17563: (
        "Muito bem! Aprovadíssimo!",
        "Mestre confere o veredito positivo com júbilo rústico."
    ),
    17564: (
        "Com isso, você também se tornou um praticante de Grathmeld!\nToda a síntese de itens nada mais é do que aplicar este princípio.",
        "Pombad outorga formalmente a iniciação na arte de síntese (melk / Grathmeld)."
    ),
    17565: (
        "Tendo paciência, você será capaz de sintetizar até o item mais complexo que existir.",
        "Conselho do mestre sobre a perseverança alquímica."
    ),
    17566: (
        "Diga uma coisa, mestre: e o meu prêmio?",
        "Lyner cobra a recompensa prometida pelo teste."
    ),
    17567: (
        "Ah, quase me esquecia disso!",
        "Pombad finge lapso de memória com graça senil."
    ),
    17568: (
        "Ô, Narl!",
        "Pombad chama a neta pelo nome canônico (ナール)."
    ),
    17569: (
        "Sim, sim, o que manda, vovô?",
        "Narl atende ao chamado com sua entonação cantarolada típica (~)."
    ),
    17570: (
        "Vou lhe dar a minha preciosa neta, a Narl!",
        "Pombad oferece a neta como noiva/prêmio em tom jocoso."
    ),
    17571: (
        "...Hã?!",
        "Lyner fica desconcertado com a oferta estapafúrdia."
    ),
    17572: (
        "O quê?!",
        "Narl é pega de surpresa pelo gracejo do avô."
    ),
    17573: (
        "Como é que éee?!!",
        "Jack berra estarrecido ao ver sua paixão secreta ser oferecida a Lyner."
    ),
    17574: (
        "Vovôôôô!!!!",
        "Narl repreende o avô com escândalo cômico."
    ),
    17575: (
        "É-É brincadeirinha! Francamente, os jovens de hoje em dia não sabem diferenciar uma piadinha esperta de coisa séria...",
        "Pombad tenta contornar o tumulto justificando seu humor excêntrico."
    ),
    17576: (
        "E então?! O que você quer de verdade?!",
        "Narl exige saber o verdadeiro propósito da convocação."
    ),
    17577: (
        "Entregue aquela recompensa a este nobre visitante.",
        "Pombad indica o verdadeiro prêmio guardado no estoque."
    ),
    17578: (
        "Quer dizer que... ele recebeu o título de praticante pleno de Grathmeld!\nMeus sinceros parabéns~!",
        "Narl celebra com alegria a certificação plena de Lyner."
    ),
    17579: (
        "Espere um momentinho, por favor~!",
        "Narl pede paciência enquanto busca o pacote de insumos."
    ),
    17580: (
        "Tchan-tchan-tchan-tchan! Aqui está a sua premiação!\nParabéns~!",
        "Efeito cômico festivo da fanfarra de entrega (panpakapaan)."
    ),
    17581: (
        "Você obteve 10 [Pedras Azuis]!",
        "Mensagem de inventário notificando o ganho de 10 unidades de Pedras Azuis."
    ),
    17582: (
        "Você obteve 10 [Pedras Vermelhas]!",
        "Notificação de inventário registrando o ganho de 10 unidades de Pedras Vermelhas."
    ),
    17583: (
        "P-Pedras?!",
        "Lyner reage decepcionado ao receber minérios brutos em vez de algo valioso."
    ),
    17584: (
        "São matérias-primas fundamentais para o Grathmeld.",
        "Pombad ressalta o valor dos minérios primordiais para a alquimia sonora."
    ),
    17585: (
        "Continue dando o seu melhor na síntese de itens~!",
        "Narl incentiva o herói com doçura juvenil."
    ),
    17586: (
        "Não é que ele aprendeu mesmo as técnicas de Grathmeld?\nFrancamente, esse cara é de tirar o chapéu...",
        "Jack reconhece a proeza e perspicácia do jovem cavaleiro."
    ),
    17587: (
        "'Ele é inteligente'... Era a isso que ela se referia, afinal...",
        "Jack lembra-se de comentários ouvidos de Shurelia/autoridades sobre o potencial de Lyner."
    ),
    17588: (
        "...'Referia'?! Eu sabia!\nAlguém andou falando de mim para você, não foi?!",
        "Lyner confronta Jack desconfiado de segredos ocultos."
    ),
    17589: (
        "N-Não, de jeito nenhum!\nJá falei que não ouvi nada de ninguém!",
        "Jack desconversa apressado para ocultar seus laços com Platina."
    ),
    17590: (
        "O mais importante: se você levar o Míssil com a gente,\nnossas chances de vitória aumentam bastante.",
        "Jack foca no objetivo bélico imediato (メッソー / Míssil sintetizado em Grathmeld)."
    ),
    17591: (
        "...Estou contando com você.",
        "Jack demonstra confiança viril no companheiro de armas."
    ),
    17592: (
        "A propósito, Jack, o seu assunto por aqui já foi resolvido?",
        "Lyner muda de assunto sondando a vida amorosa do parceiro."
    ),
    17593: (
        "...Hã? Do que está falando?",
        "Jack finge desentendimento."
    ),
    17594: (
        "Digo, com aquela garota... Era Narl o nome dela, não era?",
        "Lyner toca no ponto fraco mencionando Narl."
    ),
    17595: (
        "... Esquece esse assunto, por favor.",
        "Jack desvia o olhar amargando a rejeição silenciosa."
    ),
    17596: (
        "...Levou um fora?",
        "Lyner joga a verdade na roda com perspicácia."
    ),
    17597: (
        "Não abre essa boca!",
        "Jack berra desesperado tentando censurar o amigo."
    ),
    17598: (
        "Ora, ora... Meus sentimentos, cara.",
        "Lyner consola o colega com ironia bem-humorada."
    ),
    17599: (
        "Ei! Deixa essa conversa de lado e vamos logo para a Floresta Cello!",
        "Jack apressa o grupo em fuga da vergonha rumo à Floresta Cello."
    ),
    17600: (
        "Jack entrou para o grupo!",
        "Notificação de sistema celebrando o ingresso definitivo de Jack na equipe de combate."
    ),
}

print(f"Total curated lines mapped: {len(CURATED_MAP)}")
assert len(CURATED_MAP) == 194, f"Expected 194, got {len(CURATED_MAP)}"

# Validação linha a linha antes da montagem
hard_gate_errors = 0
lint_warnings = 0
validation_records = []

for item in input_data["dialogues"]:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    assert item_id in CURATED_MAP, f"ID {item_id} missing in CURATED_MAP!"
    curated_text, rationale = CURATED_MAP[item_id]

    # 1. Hard Gate determinístico
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=curated_text,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {item_id}: {e}")

    # 2. Soft Gate editorial
    avisos = validador_editorial.auditar_estilo_editorial(curated_text)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

    # 3. Verificações técnicas adicionais:
    # Sem \r
    if "\r" in curated_text:
        print(f"[TECH ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    # Sem pontuação órfã no início de linha após \n
    parts = curated_text.split("\n")
    for line_part in parts[1:]:
        line_strip = line_part.strip()
        if line_strip.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[PUNCT ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1
        if line_part.startswith("..."):
            print(f"[PUNCT ERROR] ID {item_id}: Line starts with reticências after newline: {line_part!r}")
            hard_gate_errors += 1

    # Sem fratura sintática antes de \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(curated_text)
    if match_frac:
        print(f"[SYNTAX ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

    validation_records.append({
        "id": item_id,
        "valid": valido and len(erros) == 0,
        "errors": erros,
        "warnings": avisos
    })

print(f"\nPre-assembly Validation Summary:")
print(f"Total lines checked: {len(validation_records)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors > 0 or lint_warnings > 0:
    print("\n[ABORT] Curated texts must have ZERO errors and ZERO warnings!")
    sys.exit(1)

# Construir curated_lines e dialogues
curated_lines = []
dialogues = []

for item in input_data["dialogues"]:
    item_id = item["id"]
    curated_text, rationale = CURATED_MAP[item_id]

    curated_lines.append({
        "id": item_id,
        "text": curated_text,
        "ptbr_curated": curated_text,
        "status": "approved",
        "origin": "curadoria_editorial",
        "notes": rationale,
        "rationale": rationale
    })

    dialogue_entry = dict(item)
    dialogue_entry.update({
        "review_status": "approved",
        "text_ptbr": curated_text,
        "curated_ptbr": curated_text,
        "final_ptbr": curated_text,
        "texto_ptbr_curado": curated_text,
        "custom_text": curated_text,
        "ptbr_curated": curated_text,
        "reviewed": True,
        "notes": rationale,
        "curation_notes": rationale,
        "curadoria_notes": rationale
    })
    dialogues.append(dialogue_entry)

# Adições terminológicas canônicas
glossary_additions = {
    "Kyle Clancy": {
        "pt": "Kyle Clancy",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / Lore",
        "note": "カイエル・クランシー (Kyle Clancy). Ex-Magistrado Técnico (技術政官) de Platina dado como morto que se infiltrou na Igreja de El Elemia sob o pseudônimo de Bispo Falss, corrompido pela ambição de controlar o poder ancestral de Mir."
    },
    "Technical Magistrate": {
        "pt": "Magistrado Técnico",
        "gender": "masculino",
        "number": "singular",
        "category": "Título / Cargo",
        "note": "技術政官 (Gijutsu Seikan). Cargo de alto escalão na governança técnica e científica de Platina responsável pela manutenção dos sistemas da Torre."
    },
    "Apostle of Elemia": {
        "pt": "Apóstolo de Elemia",
        "gender": "masculino",
        "number": "singular",
        "category": "Facção / Clero",
        "note": "エレミアの使徒 (Eremia no Shito). Título conspiratório de alta hierarquia ligado à restauração radical da Torre e à manipulação de forças ancestrais."
    },
    "Stubborn Father": {
        "pt": "Pai Teimoso",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia da Canção / Vermelha",
        "note": "赤魔法【頑固親父】 (Akamahō Ganko Oyaji). Magia Vermelha tecida por Misha em sua Cosmosfera após superar o trauma das broncas e cobranças severas do avatar de Leard."
    },
    "Narl": {
        "pt": "Narl",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / NPC",
        "note": "ナール (Nāru / Narl). Neta do excêntrico mestre Pombad na Vila Karulu e atendente da loja de Grathmeld (erroneamente adaptada como 'Noelle' pela NISA)."
    },
    "Blue Stones": {
        "pt": "Pedras Azuis",
        "gender": "feminino",
        "number": "plural",
        "category": "Material / Síntese",
        "note": "青い石 (Aoi Ishi). Mineral básico concedido como recompensa prática por Pombad para uso contínuo em sínteses de Grathmeld."
    },
    "Red Stones": {
        "pt": "Pedras Vermelhas",
        "gender": "feminino",
        "number": "plural",
        "category": "Material / Síntese",
        "note": "赤い石 (Akai Ishi). Mineral básico concedido como recompensa prática por Pombad para uso contínuo em sínteses de Grathmeld."
    }
}

# Scene Handoff profundo
scene_handoff = {
    "last_scene_id": "Event/24.evd",
    "last_line_id": 17600,
    "resumo_dramatico": (
        "O bloco BLK_EVD_077 abrange quatro arcos dramáticos cruciais de revelação política, crise emocional, catarse psicológica e alívio cômico: "
        "(1) Em Event/372.evd, no Alto Comando de Platina, Radolf prostra-se de joelhos diante do Comandante-Geral Leard oferecendo a própria vida em expiação "
        "pelos tumultos e destruição causados pelos cavaleiros corrompidos da Igreja de El Elemia. Leard rejeita a punição, instruindo-o a canalizar seus esforços "
        "na reconstrução de Platina, e desmascara a verdadeira identidade do Bispo Falss como Kyle Clancy (カイエル・クランシー), antigo Magistrado Técnico (技術政官) "
        "de Platina dado como morto que se vendeu à cobiça do poder de Mir. Em seguida, Jack e Krusche retornam com o Esquadrão de Busca trazendo a notícia do "
        "selamento absoluto de Mir graças ao hino entoado por Misha em Em Pheyna. Aurica emociona-se ao saber que sua vida foi salva por Misha e expressa o desejo de "
        "visitá-la para agradecer. Ao final da reunião, a Senhora Shurelia demonstra exaustão extrema pelo confronto e recolhe-se com Ayatane, momento em que Jack e Krusche "
        "reintegram a equipe e Ayatane deixa o grupo. "
        "(2) Em Event/262.evd, no terminal de aeronaves, Lyner, Krusche e Jack perdem por segundos o embarque de Misha e encontram inesperadamente Aurica desolada, "
        "que expressa seu complexo crônico de rejeição chamando a si mesma de 'produto com defeito' (欠陥品). Sensibilizados, Lyner e Jack acolhem-na no grupo e partem "
        "na nau voadora seguinte rumo à Placa Hexagonal (六角板). "
        "(3) Em Event/631.evd, na Cosmosfera de Misha, explode o trauma reprimido de sua infância: ela descarrega anos de fúria e ressentimento acumulados contra o avatar do "
        "Pai Teimoso (頑固親父 / representação onírica do Comandante Leard), denunciando que seus métodos brutais de confinamento e treinamento acelerado roubaram suas melhores memórias "
        "de infância, sem nunca ter recebido nem mesmo um lanche infantil. Após uma batalha inflamada de magia, o mestre reconhece com orgulho filial a imensa força e maturidade "
        "atingidas por Misha, culminando numa comovente reconciliação que gera a Magia Vermelha [Pai Teimoso] e a Mudança de Paradigma. "
        "(4) Em Event/24.evd, na oficina da Vila Karulu, Lyner conclui com sucesso seu treinamento prático de síntese sonoro-alquímica sob a supervisão do excêntrico mestre Pombad. "
        "Este prega uma peça oferecendo sua neta Narl (ナール) como noiva e prêmio, provocando o pânico escandaloso de Jack Hamilton — secretamente apaixonado pela garota. Desfeita a "
        "brincadeira, Narl entrega a Lyner o kit de 10 Pedras Azuis e 10 Pedras Vermelhas certificando-o como praticante pleno de Grathmeld. Ao final, Lyner descobre que Jack levou um fora de "
        "Narl, e os companheiros partem bem-humorados em direção à Floresta Cello com o Míssil (メッソー) pronto para a batalha."
    ),
    "decisoes_terminologicas": {
        "Kyle Clancy": "カイエル・クランシー (Kyle Clancy; nome real do Bispo Falss, ex-Magistrado Técnico de Platina)",
        "Technical Magistrate": "技術政官 (Magistrado Técnico; cargo administrativo e tecnológico de Platina)",
        "Apostle of Elemia": "エレミアの使徒 (Apóstolo de Elemia; título conspiratório dos rebeldes da Igreja)",
        "Song of the Star Singer": "星詠の詩 (Hino da Cantora das Estrelas; Chronicle Key cantado por Misha)",
        "Defective Product": "欠陥品 (produto com defeito / defeituosa; termo autodepreciativo usado por Aurica)",
        "Stubborn Father": "赤魔法【頑固親父】 / [Pai Teimoso] (Magia Vermelha tecida na catarse de Misha contra o avatar de Leard)",
        "Kid's Meal": "お子様ランチ (lanche infantil / prato infantil; símbolo do carinho paternal negado a Misha na infância)",
        "Narl": "ナール (Narl; neta de Pombad, erroneamente chamada de Noelle na versão em inglês da NISA)",
        "Full Grathmeld License": "グラスメルク免許皆伝 (praticante pleno de Grathmeld / mestre com licença completa de síntese)",
        "Blue Stones": "青い石 (Pedras Azuis; material fundamental de Grathmeld)",
        "Red Stones": "赤い石 (Pedras Vermelhas; material fundamental de Grathmeld)",
        "Missile": "メッソー / [Míssil] (projétil bélico de Grathmeld sintetizado para a batalha na Floresta Cello)"
    },
    "alertas_para_proximo_bloco": (
        "Nos blocos subsequentes (BLK_EVD_078 em diante), atentar para as investigações e avanços na Floresta Cello, "
        "a rota para a Placa Hexagonal, os próximos níveis de Cosmosfera de Aurica e Misha, bem como a investigação "
        "dos segredos de Kyle Clancy e a sombra de Mir."
    )
}

output_payload = {
    "block_id": "BLK_EVD_077",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": 194,
    "id_range": [17407, 17600],
    "stats": {
        "total_lines": 194,
        "lines_rewritten": 194,
        "lines_approved_as_is": 0,
        "new_terms_added": len(glossary_additions)
    },
    "curated_lines": curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": dialogues,
    "scene_handoff": scene_handoff
}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_payload, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully wrote {OUTPUT_PATH} with {len(dialogues)} dialogues and {len(curated_lines)} curated lines.")

# Gerar relatório analítico BLK_EVD_077_report.json
report_payload = {
    "block_id": "BLK_EVD_077",
    "status": "APPROVED_PERFECT",
    "scenes_processed": [
        {"scene_id": "Event/372.evd", "line_count": 59, "id_range": [17407, 17465], "focus": "Penitência de Radolf, Revelação de Kyle Clancy, Retorno do Esquadrão e Exaustão de Shurelia"},
        {"scene_id": "Event/262.evd", "line_count": 28, "id_range": [17466, 17493], "focus": "Perseguição no Aeroporto, Acolhimento da Aurica 'Defeituosa' e Rota para a Placa Hexagonal"},
        {"scene_id": "Event/631.evd", "line_count": 67, "id_range": [17494, 17560], "focus": "Cosmosfera de Misha, Catarse contra Pai Teimoso (Leard), Desabafo Infantil e Magia Vermelha"},
        {"scene_id": "Event/24.evd", "line_count": 40, "id_range": [17561, 17600], "focus": "Oficina de Pombad, Pegadinha da Noiva Narl, Pedras Azuis/Vermelhas e Fora de Jack"}
    ],
    "total_lines": 194,
    "hard_gate_errors": 0,
    "lint_warnings": 0,
    "theatrical_rubrics_removed": [
        "17528: '*uf* *uf*' -> 'Arf... arf...'",
        "17533: '*uf* *uf*' -> '...Arf... arf...'",
        "Restauração de interjeições autênticas e remoção de asteriscos cenográficos em todo o bloco"
    ],
    "lore_restorations": [
        "Restauração do título 'Cantora das Estrelas' (星詠) e do Hino ancestral de Misha no relatório militar de Jack (17434)",
        "Correção do nome 'Narl' (ナール) no lugar de 'Noelle' da NISA, alinhado com BLK_EVD_003 e BLK_EVD_015",
        "Restauração do termo 'Magistrado Técnico' (技術政官) para a função original de Kyle Clancy (17422)",
        "Preservação da autodepreciação dolorosa de Aurica como 'produto com defeito' (欠陥品, 17482)",
        "Correção de gênero em fala de Krusche: 'Muito obrigada!' (17469)"
    ],
    "scene_handoff_summary": scene_handoff["resumo_dramatico"]
}

with open(REPORT_PATH, "w", encoding="utf-8") as f:
    json.dump(report_payload, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {REPORT_PATH}.")

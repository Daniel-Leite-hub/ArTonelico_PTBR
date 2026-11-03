# -*- coding: utf-8 -*-
"""Script gerador e validador da curadoria editorial do bloco BLK_EVD_030."""

import json
import sys
from pathlib import Path

# Adiciona o diretório de ferramentas ao sys.path para importar o validador oficial
sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\tools")
from curadoria_validate import validate_line, validate_batch

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_030_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_030_output.json")
REPORT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_030_report.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

raw_dialogues = input_data["dialogues"]
assert len(raw_dialogues) == 282, f"Esperado 282 falas, obtido {len(raw_dialogues)}"

curations = {
    # =========================================================================
    # EVENT: Event/183.evd (IDs 7483 - 7595) [113 falas]
    # O Altar dos Apóstolos: batalha decisiva contra os vírus com o Purger,
    # invasão da mente da heroína (Aurica / Misha) e estado de coma
    # =========================================================================
    7483: (
        "O [Altar dos Apóstolos] fica logo à frente.",
        "validated",
        "Lyner apontando solenemente para o santuário sagrado à frente."
    ),
    7484: (
        "Sem conseguir contato com a Senhora Shurelia e os outros,\nnão temos como saber a situação lá dentro.",
        "rewritten",
        "Lyner ponderando sobre a falta de comunicação e a incerteza do cenário interior."
    ),
    7485: (
        "...Mesmo assim, vocês ainda vêm comigo?",
        "rewritten",
        "Lyner perguntando com lealdade e consideração se os companheiros desejam segui-lo ao perigo."
    ),
    7486: (
        "Mas é claro.",
        "rewritten",
        "Radolf respondendo com serenidade e honra inabalável de cavaleiro."
    ),
    7487: (
        "Pra que você acha que viemos\njuntos até aqui?",
        "rewritten",
        "Jack replicando com seu clássico cinismo pragmático de veterano leal."
    ),
    7488: (
        "Uma bela aposta arriscada!\nNão poderia ser mais interessante.",
        "rewritten",
        "Krusche empolgada com a adrenalina do risco e o desafio que têm pela frente."
    ),
    7489: (
        "É por Platina...\nPor tudo o que amamos.",
        "rewritten",
        "Misha reafirmando seu amor filial pela terra natal e sua determinação."
    ),
    7490: (
        "Eu só quero te ajudar, Lyner...",
        "rewritten",
        "Aurica expressando com meiguice e devoção seu desejo de amparar Lyner."
    ),
    7491: (
        "Obrigado a todos...",
        "rewritten",
        "Lyner agradecendo emocionado pelo apoio incondicional dos companheiros."
    ),
    7492: (
        "Então... vamos nessa!!",
        "rewritten",
        "Lyner partindo resoluto para a batalha com energia heroica."
    ),
    7493: (
        "...Haa... haa...",
        "rewritten",
        "Shurelia ofegante no combate, vocalização natural pura sem rubrica teatral."
    ),
    7494: (
        "Senhora Shurelia!\nA senhora não está chegando ao seu limite?!",
        "rewritten",
        "Ayatane preocupado com o esgotamento extremo de Shurelia."
    ),
    7495: (
        "Estou bem, Ayatane.",
        "rewritten",
        "Shurelia resistindo com nobreza e compostura divina."
    ),
    7496: (
        "Ugh...!!",
        "rewritten",
        "Shurelia suportando o impacto do ataque dos vírus."
    ),
    7497: (
        "Senhora Shurelia!\nIsso já é imprudência demais!",
        "rewritten",
        "Ayatane insistindo aflito para que Shurelia não ultrapasse seus limites vitais."
    ),
    7498: (
        "A nossa missão agora é não deixar\nque os vírus escapem daqui.",
        "rewritten",
        "Shurelia declarando com firmeza a responsabilidade sagrada de conter a ameaça."
    ),
    7499: (
        "Até o momento em que Lyner retornar\ntrazendo o [Purger]...",
        "rewritten",
        "Shurelia sustentando a barreira na esperança do regresso de Lyner com o cristal ancestral."
    ),
    7500: (
        "...",
        "validated",
        "Ayatane em silêncio tenso diante da determinação inabalável de Shurelia."
    ),
    7501: (
        "Lyner...",
        "validated",
        "Shurelia murmurando pelo cavaleiro em quem deposita sua confiança."
    ),
    7502: (
        "Senhora Shurelia!!\nAyataneee!!",
        "rewritten",
        "Lyner irrompendo no altar com grito de socorro e bravura."
    ),
    7503: (
        "Lyner?!",
        "validated",
        "Shurelia surpresa e aliviada com a chegada do jovem cavaleiro."
    ),
    7504: (
        "Yaaahhh!!",
        "rewritten",
        "Lyner desferindo seu golpe com brado de guerra."
    ),
    7505: (
        "Senhora Shurelia!\nTrouxemos o [Purger] de volta!",
        "rewritten",
        "Lyner anunciando com alívio o cumprimento da missão de resgate do Purger."
    ),
    7506: (
        "Deixe o resto conosco!",
        "rewritten",
        "Lyner assumindo a linha de frente para proteger Shurelia e Ayatane."
    ),
    7507: (
        "...Mas onde está o [Purger]?!",
        "rewritten",
        "Shurelia indagando surpresa por não ver o cristal físico em mãos."
    ),
    7508: (
        "Está tudo bem!\nNós baixamos o Purger no coração da Aurica!",
        "rewritten",
        "Lyner explicando a instalação harmônica do Purger na mente de Aurica."
    ),
    7509: (
        "...Compreendo.\nO restante fica em suas mãos.",
        "rewritten",
        "Shurelia confiando a purificação final a Lyner e seu grupo."
    ),
    7510: (
        "Lyner.\nEstamos contando com você.",
        "rewritten",
        "Ayatane transmitindo confiança fraternal ao companheiro de armas."
    ),
    7511: (
        "Pode deixar com a gente!",
        "rewritten",
        "Lyner respondendo com bravura e entusiasmo contagiante."
    ),
    7512: (
        "Aurica, conto com você!\nMostre de novo aquela linda voz cantante de antes!",
        "rewritten",
        "Lyner encorajando Aurica com afeto e entusiasmo para entoar a Canção."
    ),
    7513: (
        "Sim...",
        "rewritten",
        "Aurica assentindo com meiguice e determinação tímida."
    ),
    7514: (
        "Eu... vou cantar com todas as minhas forças...!",
        "rewritten",
        "Aurica concentrando seu canto lírico sagrado para a batalha."
    ),
    7515: (
        "Vamos láaaa!!",
        "rewritten",
        "Lyner partindo para o confronto decisivo contra os vírus."
    ),
    7516: (
        "Pessoal, foi mal...\nVocês terem que me acompanhar até um lugar desses...",
        "rewritten",
        "Lyner agradecendo sem jeito pelo companheirismo irrestrito da equipe."
    ),
    7517: (
        "Desde o início pretendia acompanhar você até o fim.\nPelo contrário, é uma honra estar aqui.",
        "rewritten",
        "Radolf reafirmando sua dignidade e lealdade sagrada a Lyner."
    ),
    7518: (
        "Nós somos os heróis que vão salvar o mundo, sabia?\nIsso não é estiloso pra caramba?",
        "rewritten",
        "Jack zombando espirituoso com seu estilo despojado e confiante."
    ),
    7519: (
        "Serve de referência para meus projetos futuros,\ne até que estou me divertindo bastante.",
        "rewritten",
        "Krusche encarando a missão com sua curiosidade científica e espírito prático."
    ),
    7520: (
        "Obrigado a todos!",
        "rewritten",
        "Lyner grato e revigorado pelo calor da união de todos."
    ),
    7521: (
        "Certo... então vamos arrebentar\ncom eles de alma lavada!!",
        "rewritten",
        "Lyner conclamando o grupo ao ataque definitivo com ardor guerreiro."
    ),
    7522: (
        "Acabou?!",
        "rewritten",
        "Lyner verificando se o monstro viral foi completamente aniquilado."
    ),
    7523: (
        "...Grrr...",
        "rewritten",
        "O vírus moribundo rugindo em espasmo final antes de atacar."
    ),
    7524: (
        "...O quê?!",
        "rewritten",
        "Lyner alarmado com a reação repentina da criatura."
    ),
    7525: (
        "Kyaaaaahhh!!!",
        "rewritten",
        "Aurica gritando ao ser subitamente alvejada pelo salto invasivo do vírus."
    ),
    7526: (
        "Aurica!!",
        "validated",
        "Lyner desesperado ao ver a companheira atingida."
    ),
    7527: (
        "Aurica! Firmeza, aguenta firme!!",
        "rewritten",
        "Lyner acorrendo para amparar Aurica enquanto ela perde a consciência."
    ),
    7528: (
        "Aurica!!",
        "validated",
        "Lyner clamando angustiado pelo nome dela."
    ),
    7529: (
        "Aurica se encontra em um estado\nextremamente crítico.",
        "rewritten",
        "Shurelia diagnosticando a gravidade do colapso psíquico sofrido por Aurica."
    ),
    7530: (
        "...!!",
        "validated",
        "Lyner em choque profundo diante do prognóstico."
    ),
    7531: (
        "O vírus se lançou para dentro da Aurica\ne desapareceu... Não foi isso?",
        "rewritten",
        "Shurelia reconstituindo a dinâmica exata do ataque do parasita mental."
    ),
    7532: (
        "Foi... exatamente isso...",
        "rewritten",
        "Lyner confirmando a tragédia com pesar e desespero."
    ),
    7533: (
        "Por causa do [Purger], o vírus perdeu\na capacidade de se transformar em energia pura.",
        "rewritten",
        "Shurelia detalhando o efeito molecular do Purger sobre a estrutura viral."
    ),
    7534: (
        "Por esse motivo, tudo indica que ele buscou\nrefúgio na Cosmosfera da Aurica.",
        "rewritten",
        "Shurelia deduzindo a fuga do invasor para o mundo interior da Reyvateil."
    ),
    7535: (
        "Pelo choque da invasão,\nela entrou em estado de coma.",
        "rewritten",
        "Shurelia explicando a causa do desmaio profundo e do risco de vida."
    ),
    7536: (
        "Em termos simples... é como se ela tivesse sofrido\no Mergulho mais brutal e forçado de todos.",
        "rewritten",
        "Radolf resumindo a catástrofe com a analogia técnica de um Mergulho violento."
    ),
    7537: (
        "Com o monstro escondido dentro dela,\nnão podemos atacar sem medir forças...",
        "rewritten",
        "Krusche avaliando o dilema tático de não poder disparar contra o vírus hospedeiro."
    ),
    7538: (
        "Afinal, se a gente matar a Aurica,\no vírus morreria junto, mas...",
        "rewritten",
        "Krusche pontuando a fria lógica mecânica da situação."
    ),
    7539: (
        "Krusche!",
        "validated",
        "Lyner repreendendo energicamente a frieza do raciocínio de Krusche."
    ),
    7540: (
        "Foi só uma hipótese, puxa vida!",
        "rewritten",
        "Krusche se defendendo emburrada com seu tom despachado."
    ),
    7541: (
        "...Receio que o vírus estivesse visando exatamente isso.",
        "rewritten",
        "Shurelia concordando que o inimigo usou o corpo da Reyvateil como escudo inviolável."
    ),
    7542: (
        "Senhora Shurelia! Não há alguma forma...\nalguma maneira de combater isso?!",
        "rewritten",
        "Lyner implorando por uma solução para resgatar Aurica do abismo mental."
    ),
    7543: (
        "É perigoso, mas existe um meio.",
        "rewritten",
        "Shurelia revelando a existência de uma saída de alto risco."
    ),
    7544: (
        "No entanto, esse método imporá um fardo\nimparável ao coração de Aurica.",
        "rewritten",
        "Shurelia alertando sobre o perigo severo de trauma irreversível na psique."
    ),
    7545: (
        "...!!",
        "validated",
        "Lyner estremecendo diante da gravidade do alerta."
    ),
    7546: (
        "...Mesmo assim, é infinitamente melhor\ndo que ficar de braços cruzados.",
        "rewritten",
        "Lyner escolhendo agir e enfrentar o perigo sem hesitar."
    ),
    7547: (
        "Se o pior acontecer com ela...\neu mesmo curarei a alma da Aurica!",
        "rewritten",
        "Lyner prometendo com coragem e devoção mergulhar e curar a dor de Aurica."
    ),
    7548: (
        "...Compreendo.",
        "rewritten",
        "Shurelia acatando a firme convicção do cavaleiro."
    ),
    7549: (
        "Sendo assim, iremos para o Centro de Mergulho.",
        "rewritten",
        "Shurelia ordenando o transporte imediato de Aurica à câmara de imersão."
    ),
    7550: (
        "Lyner, assim que terminarem os preparativos,\nencontrem-me lá.",
        "rewritten",
        "Shurelia marcando o ponto de encontro operacional."
    ),
    7551: (
        "Está tudo bem!\nNós baixamos o Purger no coração da Misha!",
        "rewritten",
        "Lyner explicando a instalação harmônica do Purger na mente de Misha (ramo de Misha)."
    ),
    7552: (
        "...Compreendo.\nO restante fica em suas mãos.",
        "rewritten",
        "Shurelia confiando a purificação final a Lyner e seu grupo (ramo de Misha)."
    ),
    7553: (
        "Lyner.\nEstamos contando com você.",
        "rewritten",
        "Ayatane transmitindo confiança fraternal a Lyner (ramo de Misha)."
    ),
    7554: (
        "Pode deixar com a gente!",
        "rewritten",
        "Lyner respondendo com bravura e entusiasmo contagiante (ramo de Misha)."
    ),
    7555: (
        "Misha, conto com você!\nCante com tudo, naquele seu ritmo de sempre!",
        "rewritten",
        "Lyner incentivando Misha a liberar toda a sua energia habitual de canto."
    ),
    7556: (
        "Deixa comigo!",
        "rewritten",
        "Misha respondendo animada e pronta para o combate."
    ),
    7557: (
        "Vou cantar sem parar,\nde corpo e alma!",
        "rewritten",
        "Misha prometendo dedicação absoluta com sua voz sagrada."
    ),
    7558: (
        "Vamos láaaa!!",
        "rewritten",
        "Lyner partindo para o confronto decisivo contra os vírus (ramo de Misha)."
    ),
    7559: (
        "Pessoal, foi mal...\nVocês terem que me acompanhar até um lugar desses...",
        "rewritten",
        "Lyner agradecendo sem jeito pelo apoio da equipe (ramo de Misha)."
    ),
    7560: (
        "Desde o início pretendia acompanhar você até o fim.\nPelo contrário, é uma honra estar aqui.",
        "rewritten",
        "Radolf reafirmando sua honra militar ao lado de Lyner (ramo de Misha)."
    ),
    7561: (
        "Nós somos os heróis que vão salvar o mundo, sabia?\nIsso não é estiloso pra caramba?",
        "rewritten",
        "Jack tirando onda com o heroísmo da missão (ramo de Misha)."
    ),
    7562: (
        "Serve de referência para meus projetos futuros,\ne até que estou me divertindo bastante.",
        "rewritten",
        "Krusche encarando a missão com humor prático (ramo de Misha)."
    ),
    7563: (
        "Obrigado a todos!",
        "rewritten",
        "Lyner agradecendo de coração aberto (ramo de Misha)."
    ),
    7564: (
        "Certo... então vamos arrebentar\ncom eles de alma lavada!!",
        "rewritten",
        "Lyner conclamando o ataque final com bravura (ramo de Misha)."
    ),
    7565: (
        "Acabou?!",
        "rewritten",
        "Lyner conferindo se o monstro tombou (ramo de Misha)."
    ),
    7566: (
        "...Grrr...",
        "rewritten",
        "O vírus agonizante rugindo antes do golpe final (ramo de Misha)."
    ),
    7567: (
        "...O quê?!",
        "rewritten",
        "Lyner assustado com o bote repentino da criatura (ramo de Misha)."
    ),
    7568: (
        "Kyaaaaahhh!!!",
        "rewritten",
        "Misha gritando em choque ao ser alvejada pelo vírus invasor."
    ),
    7569: (
        "Misha!!",
        "validated",
        "Lyner desesperado ao ver a amiga de infância desabar."
    ),
    7570: (
        "Misha! Firmeza, aguenta firme!!",
        "rewritten",
        "Lyner tentando acordar Misha enquanto ela perde os sentidos."
    ),
    7571: (
        "Misha!!",
        "validated",
        "Lyner gritando aflito pelo nome de Misha."
    ),
    7572: (
        "Misha se encontra em um estado\nextremamente crítico.",
        "rewritten",
        "Shurelia atestando a gravidade extrema do colapso de Misha."
    ),
    7573: (
        "...!!",
        "validated",
        "Lyner estarrecido com a constatação médica de Shurelia."
    ),
    7574: (
        "O vírus se lançou para dentro da Misha\ne desapareceu... Não foi isso?",
        "rewritten",
        "Shurelia analisando a entrada invasiva do vírus na mente de Misha."
    ),
    7575: (
        "Foi... exatamente isso...",
        "rewritten",
        "Lyner atestando a cena desoladora que acabou de presenciar."
    ),
    7576: (
        "Por causa do [Purger], o vírus perdeu\na capacidade de se transformar em energia pura.",
        "rewritten",
        "Shurelia explicando a paralisia molecular do vírus causada pelo Purger."
    ),
    7577: (
        "Por esse motivo, tudo indica que ele buscou\nrefúgio na Cosmosfera da Misha.",
        "rewritten",
        "Shurelia deduzindo o refúgio do parasita na mente de Misha."
    ),
    7578: (
        "Pelo choque da invasão,\nela entrou em estado de coma.",
        "rewritten",
        "Shurelia diagnosticando o coma induzido pelo impacto da contaminação."
    ),
    7579: (
        "Em termos simples... é como se ela tivesse sofrido\no Mergulho mais brutal e forçado de todos.",
        "rewritten",
        "Radolf ilustrando a violência da invasão psíquica sofrida por Misha."
    ),
    7580: (
        "Com o monstro escondido dentro dela,\nnão podemos atacar sem medir forças...",
        "rewritten",
        "Krusche destacando o impedimento técnico de alvejar o vírus diretamente."
    ),
    7581: (
        "Afinal, se a gente matar a Misha,\no vírus morreria junto, mas...",
        "rewritten",
        "Krusche raciocinando friamente sobre a conexão biológica entre ambos."
    ),
    7582: (
        "Krusche!",
        "validated",
        "Lyner cortando a indiscrição grosseira de Krusche."
    ),
    7583: (
        "Foi só uma hipótese, puxa vida!",
        "rewritten",
        "Krusche recuando ligeiramente emburrada."
    ),
    7584: (
        "...Receio que o vírus estivesse visando exatamente isso.",
        "rewritten",
        "Shurelia confirmando a estratégia vilã do parasita de usar Misha de escudo."
    ),
    7585: (
        "Senhora Shurelia! Não há alguma forma...\nalguma maneira de combater isso?!",
        "rewritten",
        "Lyner clamando por uma intervenção para salvar a vida de Misha."
    ),
    7586: (
        "É perigoso, mas existe um meio.",
        "rewritten",
        "Shurelia admitindo que há uma rota arriscada de salvação."
    ),
    7587: (
        "No entanto, esse método imporá um fardo\nimparável ao coração de Misha.",
        "rewritten",
        "Shurelia alertando sobre o estresse emocional devastador na mente da garota."
    ),
    7588: (
        "...!!",
        "validated",
        "Lyner sentindo o peso do risco iminente."
    ),
    7589: (
        "...Mesmo assim, é infinitamente melhor\ndo que ficar de braços cruzados.",
        "rewritten",
        "Lyner determinado a arriscar tudo pela sobrevivência de Misha."
    ),
    7590: (
        "Se o pior acontecer com ela...\neu mesmo curarei a alma da Misha!",
        "rewritten",
        "Lyner assumindo o compromisso jurado de proteger e sarar o coração de Misha."
    ),
    7591: (
        "...Compreendo.",
        "rewritten",
        "Shurelia acolhendo a decisão resoluta do rapaz."
    ),
    7592: (
        "Sendo assim, iremos para o Centro de Mergulho.",
        "rewritten",
        "Shurelia liderando o transporte imediato de Misha à câmara técnica."
    ),
    7593: (
        "Lyner, assim que terminarem os preparativos,\nencontrem-me lá.",
        "rewritten",
        "Shurelia instruindo o grupo a se preparar antes do Mergulho salvador."
    ),
    7594: (
        "Aurica saiu do grupo!\nMisha entrou para o grupo!",
        "rewritten",
        "Mensagem de sistema para troca de grupo (entrada de Misha)."
    ),
    7595: (
        "Misha saiu do grupo!\nAurica entrou para o grupo!",
        "rewritten",
        "Mensagem de sistema para troca de grupo (entrada de Aurica)."
    ),

    # =========================================================================
    # EVENT: Event/180.evd (IDs 7596 - 7657) [62 falas]
    # Gabinete de Leard em Platina: relatório de download do Purger,
    # instruções táticas solenes e designação de defesa da cidade flutuante
    # =========================================================================
    7596: (
        "Pai! Baixei o cristal direitinho, como pediu!",
        "rewritten",
        "Lyner reportando com orgulho jovial o sucesso do download ao pai."
    ),
    7597: (
        "Ora... Parece que você aprendeu\nalguma coisa afinal.",
        "rewritten",
        "Leard elogiando o filho com sua costumeira austeridade patriarcal contida."
    ),
    7598: (
        "E em quem realizou o download?",
        "rewritten",
        "Leard indagando qual Reyvateil foi escolhida como receptáculo do Purger."
    ),
    7599: (
        "Na Aurica...",
        "rewritten",
        "Lyner indicando Aurica com cuidado e respeito."
    ),
    7600: (
        "...É-é uma honra conhecê-lo...",
        "rewritten",
        "Aurica cumprimentando o Governador Leard com sua delicada timidez cerimoniosa."
    ),
    7601: (
        "Hum. O destino de Platina...\nNão, o destino de todo este mundo repousa sobre você.",
        "rewritten",
        "Leard transferindo todo o fardo da responsabilidade global para a jovem."
    ),
    7602: (
        "O fracasso é inadmissível.\nCante com toda a gravidade de seu coração.",
        "rewritten",
        "Leard exigindo dedicação marcial irrepreensível."
    ),
    7603: (
        "S-sim, senhor...",
        "rewritten",
        "Aurica engolindo em seco diante da severidade do comandante."
    ),
    7604: (
        "Pai!! Por que tem que intimidar a garota?!",
        "rewritten",
        "Lyner saindo em defesa indignada de Aurica contra a rigidez paterna."
    ),
    7605: (
        "Apenas declarei os fatos.\nE trate de carregar essa mesma seriedade ao entrar na batalha.",
        "rewritten",
        "Leard rebatendo com pragmatismo e cobrando prontidão militar do filho."
    ),
    7606: (
        "Pois bem, senhorita Aurica.",
        "rewritten",
        "Leard retomando o briefing militar formal."
    ),
    7607: (
        "Sua missão é combater os vírus\nao lado de Lyner entoando o seu Hino.",
        "rewritten",
        "Leard esclarecendo o objetivo tático primordial de Aurica no front."
    ),
    7608: (
        "Sustentar o Purger e ao mesmo tempo entoar Canções comuns\né uma tarefa árdua, mas não temos outra escolha.",
        "rewritten",
        "Leard alertando sobre a tremenda carga cognitiva exigida da cantora."
    ),
    7609: (
        "...Entendido.",
        "rewritten",
        "Aurica aceitando o encargo com resignação corajosa."
    ),
    7610: (
        "A Canção que você gravou tem o efeito\nde impedir que o vírus fuja.",
        "rewritten",
        "Leard explicando a mecânica de contenção dimensional exercida pelo Purger."
    ),
    7611: (
        "Participe do combate normalmente\ne, acima de tudo, continue cantando sem cessar.",
        "rewritten",
        "Leard instruindo sobre a prioridade de manter a Canção contínua."
    ),
    7612: (
        "Compreendi. Darei o melhor de mim...",
        "rewritten",
        "Aurica assentindo com modéstia e fibra interior."
    ),
    7613: (
        "Na Misha...",
        "rewritten",
        "Lyner informando ao pai que Misha foi a receptora do Purger."
    ),
    7614: (
        "Fui eu quem recebeu a Canção.",
        "rewritten",
        "Misha se apresentando formal e respeitosamente diante de Leard."
    ),
    7615: (
        "Misha... Sendo você,\ntenho certeza de que cumprirá o dever.",
        "rewritten",
        "Leard demonstrando familiaridade e alta confiança nas capacidades de Misha."
    ),
    7616: (
        "Nesta missão, o fracasso é inadmissível.\nCante com toda a gravidade de seu coração.",
        "rewritten",
        "Leard alertando Misha com a mesma solenidade implacável."
    ),
    7617: (
        "S-sim, senhor!",
        "rewritten",
        "Misha respondendo com postura militar sob a pressão da autoridade."
    ),
    7618: (
        "Pai!! Por que tem que intimidar a garota?!",
        "rewritten",
        "Lyner reclamando da dureza desnecessária do pai contra Misha."
    ),
    7619: (
        "Apenas declarei os fatos.\nE trate de carregar essa mesma seriedade ao entrar na batalha.",
        "rewritten",
        "Leard lembrando que guerra não comporta infantilidade."
    ),
    7620: (
        "Pois bem, Misha.",
        "rewritten",
        "Leard voltando a atenção técnica para as ordens de combate de Misha."
    ),
    7621: (
        "Sua missão é combater os vírus\nao lado de Lyner entoando o seu Hino.",
        "rewritten",
        "Leard definindo o papel de combate na linha de frente."
    ),
    7622: (
        "Sustentar o Purger e ao mesmo tempo entoar Canções comuns\né uma tarefa árdua, mas você é plenamente capaz.",
        "rewritten",
        "Leard reconhecendo a destreza inata de Misha como Reyvateil Origin."
    ),
    7623: (
        "...Sim, senhor.",
        "rewritten",
        "Misha acatando com maturidade e serenidade."
    ),
    7624: (
        "A Canção que você gravou tem o efeito\nde impedir que o vírus fuja.",
        "rewritten",
        "Leard especificando a função anímica de bloqueio do Purger."
    ),
    7625: (
        "Participe do combate normalmente\ne, acima de tudo, continue cantando sem cessar.",
        "rewritten",
        "Leard enfatizando a cadência ininterrupta do canto da Canção."
    ),
    7626: (
        "Entendido! Basta eu cantar sem parar,\nnão é?",
        "rewritten",
        "Misha resumindo a diretriz com sua prontidão perspicaz."
    ),
    7627: (
        "Com isso, os preparativos estão prontos.\nResta apenas confrontar os vírus.",
        "rewritten",
        "Leard encerrando o planejamento tático pré-batalha."
    ),
    7628: (
        "Tudo indica que os vírus continuam\nocupando o [Altar dos Apóstolos].",
        "rewritten",
        "Leard fornecendo a coordenada do bastião inimigo."
    ),
    7629: (
        "Há também a situação da Senhora Shurelia e de Ayatane.\nA situação não tolera nem um segundo de atraso.",
        "rewritten",
        "Leard cobrando urgência máxima em prol do resgate da Administradora."
    ),
    7630: (
        "Partam imediatamente rumo ao [Altar dos Apóstolos].",
        "rewritten",
        "Leard emitindo a ordem de marcha formal aos cavaleiros."
    ),
    7631: (
        "Usem o [Purger] e erradiquem os vírus.",
        "rewritten",
        "Leard estipulando a condição de vitória absoluta."
    ),
    7632: (
        "Certo.\nEstamos a caminho!",
        "rewritten",
        "Lyner respondendo pronto para o dever."
    ),
    7633: (
        "Lyner.",
        "validated",
        "Leard chamando o filho antes da partida, tom grave de despedida."
    ),
    7634: (
        "...",
        "validated",
        "Pausa pesada carregada de afeto paternal contido."
    ),
    7635: (
        "O destino do mundo repousa sobre vocês.\nNão baixe a guarda nem por um instante.",
        "rewritten",
        "Leard aconselhando o filho a manter a vigilância e voltar vivo."
    ),
    7636: (
        "Eu já sei disso!",
        "rewritten",
        "Lyner respondendo com ímpeto confiante."
    ),
    7637: (
        "É só isso o que o senhor tem para me dizer...?",
        "rewritten",
        "Lyner lamentando com doçura velada a falta de palavras mais calorosas do pai."
    ),
    7638: (
        "...",
        "validated",
        "Leard em silêncio estóico, engolindo a preocupação paterna."
    ),
    7639: (
        "Quanto a você, Misha...\nFicará encarregada da defesa de Platina.",
        "rewritten",
        "Leard designando Misha para proteger a cidade flutuante (ramo de Aurica)."
    ),
    7640: (
        "Não pode ser! Eu também quero ir com o Lyner!",
        "rewritten",
        "Misha protestando por querer lutar ao lado de seu amigo de infância."
    ),
    7641: (
        "A erradicação dos vírus só é viável através do Purger.\nAcompanhá-los não mudará nada no campo de batalha.",
        "rewritten",
        "Leard justificando friamente a impossibilidade tática de sua presença."
    ),
    7642: (
        "Acima de tudo, se nada for feito,\na própria Platina correrá o risco de cair nas mãos dos vírus.",
        "rewritten",
        "Leard alertando sobre o risco iminente de colapso de Platina."
    ),
    7643: (
        "...",
        "validated",
        "Misha em silêncio inconformado, mas ciente da realidade."
    ),
    7644: (
        "Fica tranquila, Misha.\nVamos derrotar esses vírus e voltar rapidinho.",
        "rewritten",
        "Lyner confortando a companheira com otimismo fraternal afetuoso."
    ),
    7645: (
        "...",
        "validated",
        "Misha respirando fundo para conter a angústia."
    ),
    7646: (
        "...Tudo bem.\nLyner, você tem que voltar são e salvo... Promete?!",
        "rewritten",
        "Misha arrancando a promessa de sobrevivência com carinho e apreensão."
    ),
    7647: (
        "Misha saiu do grupo.",
        "rewritten",
        "Mensagem de sistema: saída de Misha para guarnição em Platina."
    ),
    7648: (
        "Quanto à senhorita Aurica...\nFicará encarregada da defesa de Platina.",
        "rewritten",
        "Leard designando Aurica para proteger a cidade (ramo de Misha)."
    ),
    7649: (
        "O quê?! Pai, por que isso?!\nA Aurica não pode vir com a gente?!",
        "rewritten",
        "Lyner inconformado por ter que se separar de Aurica."
    ),
    7650: (
        "A erradicação dos vírus só é viável através do Purger.\nAcompanhá-los não mudará nada no campo de batalha.",
        "rewritten",
        "Leard repetindo o princípio militar de neutralização viral exclusiva."
    ),
    7651: (
        "Acima de tudo, se nada for feito,\na própria Platina correrá o risco de cair nas mãos dos vírus.",
        "rewritten",
        "Leard reforçando a ameaça existencial à cidade natal."
    ),
    7652: (
        "...Tsc.",
        "rewritten",
        "Lyner frustrado com a falta de alternativas lógicas perante as ordens."
    ),
    7653: (
        "...Eu compreendo.\nVou ficar aqui... e esperar pelo Lyner.",
        "rewritten",
        "Aurica demonstrando serenidade paciente e confiança devotada em Lyner."
    ),
    7654: (
        "Aurica?!",
        "rewritten",
        "Lyner surpreso com a aceitação dócil e madura da jovem."
    ),
    7655: (
        "...Eu vou estar te esperando.\nPrometa que vai voltar... com vida.",
        "rewritten",
        "Aurica pedindo com meiguice e fervor que Lyner retorne vivo."
    ),
    7656: (
        "Aurica...\nTudo bem, eu prometo.",
        "rewritten",
        "Lyner selando o juramento solene com os olhos fixos nela."
    ),
    7657: (
        "Aurica saiu do grupo.",
        "rewritten",
        "Mensagem de sistema: saída de Aurica para a retaguarda em Platina."
    ),

    # =========================================================================
    # EVENT: Event/811.evd (IDs 7658 - 7764) [107 falas]
    # Clímax Dramático da Cosmosfera de Shurelia (Escola / Leila Togasaki):
    # O sacrifício de Leila, a pureza dos sentimentos (Omoi), o luto de Lyner,
    # o conforto de Aurica, a recusa do pingente de memória e o despertar
    # =========================================================================
    7658: (
        "...N-não pode ser... Até o Demônio foi derrotado...?! Como?!",
        "rewritten",
        "Claire em choque e desespero ao ver seu guardião supremo ser abatido."
    ),
    7659: (
        "Porque dentro de mim existe um sentimento inabalável:\no anseio fervoroso de proteger este mundo!",
        "rewritten",
        "Leila proclamando com nobreza a força transcendental do seu 'Omoi' (sentimento)."
    ),
    7660: (
        "O-o quê?! Uma mera criatura viral ousando falar em \"sentimentos\"...?!\nNo fundo, você não passa de um programa sem coração!",
        "rewritten",
        "Claire desdenhando cruelmente da natureza artificial de Leila."
    ),
    7661: (
        "Posso até ser algo \"criado por mãos alheias\"...\nMas a vontade sincera que trago no peito de proteger este mundo... e de proteger o Lyner... jamais foi mentira!",
        "rewritten",
        "Leila defendendo a verdade irrefutável do amor e devoção que sente por Lyner."
    ),
    7662: (
        "E mesmo que afirmem que até isso é pura programação...\neu não me importo!",
        "rewritten",
        "Leila transcendendo a frieza dos códigos para abraçar a sua alma."
    ),
    7663: (
        "Pois não importa o que digam...\no que sinto aqui dentro é real!",
        "rewritten",
        "Leila afirmando com paixão que a sua dor e seu amor são genuínos."
    ),
    7664: (
        "A força desse sentimento...\na firmeza desta determinação... tudo é verdadeiro...!",
        "rewritten",
        "Leila reunindo sua energia luminosa contra a escuridão do vírus."
    ),
    7665: (
        "Ugh!! Uwaaah...!!\nLarga! Solta de mim!!\nO que... o que você pretende fazer?!",
        "rewritten",
        "Claire apavorada ao ser envolvida pelo abraço de contenção de Leila."
    ),
    7666: (
        "Alguém como você, fruto híbrido entre humano e vírus,\nestá além do que a humanidade pode combater.\nPor isso, eu mesma a farei desaparecer!",
        "rewritten",
        "Leila decidida a sacrificar a própria existência para erradicar o híbrido maligno."
    ),
    7667: (
        "Ficou louca...?! Se fizer uma loucura dessas...\nvocê também não sairá ilesa disso...!",
        "rewritten",
        "Claire alertando em pânico sobre a aniquilação mútua iminente."
    ),
    7668: (
        "Eu vou provar a você a grandeza do que sinto.\nO quão incomensurável é a força do meu anseio de salvar este mundo!",
        "rewritten",
        "Leila elevando a frequência de sua essência ao ponto máximo."
    ),
    7669: (
        "Kyaaaah!!\nUgh... Não... Não pode ser!\nUma mera forma de vida programada jamais teria sentimentos...",
        "rewritten",
        "Claire sendo consumida pela luz da resolução heróica de Leila."
    ),
    7670: (
        "Leila!! Já chega!\nPara com isso! Não use tanto do seu poder!!",
        "rewritten",
        "Lyner clamando desesperado para que Leila não destrua a própria vida."
    ),
    7671: (
        "Você perdeu o juízo, garota?!\nSe continuar com isso, seu próprio fim será questão de tempo!\nNem isso você percebe?!",
        "rewritten",
        "Claire esbravejando diante da autodestruição que consome ambas."
    ),
    7672: (
        "Mesmo se eu não fizesse nada, o meu fim já seria\nquestão de tempo... Não é verdade?",
        "rewritten",
        "Leila encarando a finitude de sua criação com serenidade sublime."
    ),
    7673: (
        "...Ugh...",
        "rewritten",
        "Claire emudecida sem conseguir contra-argumentar."
    ),
    7674: (
        "Claire... o que existe de mais precioso para você?\nÉ você mesma, não é...?",
        "rewritten",
        "Leila confrontando o egoísmo estéril da vilã."
    ),
    7675: (
        "Sendo assim, você jamais seria capaz de entender\no que preenche o meu ser agora.",
        "rewritten",
        "Leila demarcando o abismo entre o egoísmo e o amor desinteressado."
    ),
    7676: (
        "A bênção de ter algo que amamos mais que a nós mesmas...\nalgo que queremos proteger acima da própria vida.",
        "rewritten",
        "Leila sintetizando o significado sagrado de amar e proteger."
    ),
    7677: (
        "Pare com isso!!",
        "rewritten",
        "Lyner berrando em agonia impotente."
    ),
    7678: (
        "Lyner... foi por pouco tempo, mas obrigada.\nNo começo, eu lutava sem nem entender\npor qual razão empunhava a espada...",
        "rewritten",
        "Leila iniciando sua despedida com gratidão lírica e comovente."
    ),
    7679: (
        "Mas... desde o instante em que conheci você...\nesse vazio foi se transformando.",
        "rewritten",
        "Leila confessando o impacto curativo do encontro com Lyner em sua alma."
    ),
    7680: (
        "Eu não conheço quase nada do mundo, não fui capaz de fazer nada por você...\nE agora, nossa despedida chega cedo demais...",
        "rewritten",
        "Leila lamentando a brevidade dolorosa da convivência de ambos."
    ),
    7681: (
        "Por isso, se há algo que posso fazer...\nquero presentear você com este mundo.",
        "rewritten",
        "Leila oferecendo o mundo renascido como seu legado de amor a Lyner."
    ),
    7682: (
        "Este céu límpido e azul, esta terra fértil onde brota o verde...\nTesouros que jamais poderiam ser destruídos...\nA fonte de toda a felicidade sagrada... o mundo que nos gerou...",
        "rewritten",
        "Leila poetizando as belezas da natureza que jurou preservar com a própria vida."
    ),
    7683: (
        "Se o meu destino já é desaparecer de qualquer forma...\nem vez de sumir sem deixar nada para trás,\nquero ao menos fazer algo por você antes do fim.",
        "rewritten",
        "Leila justificando seu sacrifício altruísta com sublime ternura."
    ),
    7684: (
        "Eu nunca quis uma coisa dessas!",
        "rewritten",
        "Lyner rejeitando em prantos a ideia de um mundo salvo ao custo da vida dela."
    ),
    7685: (
        "Mesmo que essa realidade não possa ser mudada,\neu só queria... passar mais um minuto, mais um segundo que fosse\nao lado da Leila... Era só isso o que eu queria!",
        "rewritten",
        "Lyner declarando a verdade despojada do seu coração: o anseio de apenas estar com ela."
    ),
    7686: (
        "...Lyner...\nObrigada... Ouvir isso aquece a minha alma...\nFoi maravilhoso ter encontrado você...",
        "rewritten",
        "Leila comovida pelas palavras puras de amor de Lyner."
    ),
    7687: (
        "Eu também... sinto exatamente a mesma coisa, Lyner...",
        "rewritten",
        "Leila retribuindo a comunhão de sentimentos."
    ),
    7688: (
        "...Por isso...",
        "rewritten",
        "Leila hesitante na transição para o adeus inevitável."
    ),
    7689: (
        "É por isso...\nAdeus...",
        "rewritten",
        "Leila proferindo seu adeus final com doçura e resignação mística."
    ),
    7690: (
        "Kyaaaaaaaaahhh!!",
        "rewritten",
        "Claire berrando enquanto sua essência se desintegra no clarão."
    ),
    7691: (
        "Leilaaaaaaaaahhh!!!",
        "rewritten",
        "Lyner rasgando a voz em um grito dilacerante de perda."
    ),
    7692: (
        "...Lyner... obrigada...",
        "rewritten",
        "O sussurro etéreo de Leila ecoando pela última vez."
    ),
    7693: (
        "...Por ter me presenteado\ncom tantos sentimentos preciosos...",
        "rewritten",
        "Leila agradecendo pelo afeto que deu sentido à sua breve existência."
    ),
    7694: (
        "Quando o clarão avassalador finalmente se dissipou,\ntanto Leila quanto Claire haviam desaparecido.",
        "rewritten",
        "Narração lírica descrevendo o vazio e o silêncio após a grande explosão de luz."
    ),
    7695: (
        "Diante de um desfecho tão abrupto,\neu apenas permaneci ali, emudecido e atônito.",
        "rewritten",
        "Lyner descrevendo o choque paralisante do luto repentino."
    ),
    7696: (
        "Como se a presença dela diante dos meus olhos até instantes atrás\nnão passasse de uma ilusão... uma grande mentira.",
        "rewritten",
        "Lyner sentindo o peso da irrealidade de perder alguém tão vivo."
    ),
    7697: (
        "Por mais que eu procurasse,\nnão conseguia encontrar vestígio algum da existência de Leila.",
        "rewritten",
        "Lyner relatando a busca desesperada por qualquer rastro da amada."
    ),
    7698: (
        "Mesmo assim, continuei vasculhando sem cessar.\nSem comer, sem matar a sede...",
        "rewritten",
        "Lyner negligenciando o próprio corpo na obsessão de reencontrá-la."
    ),
    7699: (
        "Com licença...\nA Leila não apareceu por aqui ultimamente?",
        "rewritten",
        "Lyner perguntando na cidade com voz embargada e ansiosa."
    ),
    7700: (
        "Desde o dia daquele incidente, ela não pisou mais aqui.\nFrancamente... onde será que aquela garota foi parar...?",
        "rewritten",
        "Oficial da Igreja respondendo com indiferença mundana e estranheza."
    ),
    7701: (
        "...",
        "validated",
        "Lyner absorvendo mais uma resposta vazia."
    ),
    7702: (
        "Compreendo...",
        "rewritten",
        "Lyner aceitando com tristeza o desamparo."
    ),
    7703: (
        "Aqui também não...\nNesse caso, terei que perguntar para quem quer que eu cruze pelo caminho...",
        "rewritten",
        "Lyner insistindo na busca cega mesmo sem rumo."
    ),
    7704: (
        "Por favor, com licença!\nUma garota de cabelos azul-claros, mais ou menos dessa altura, passou por aqui...?",
        "rewritten",
        "Lyner abordando pedestres com gestos aflitos de desespero."
    ),
    7705: (
        "Hã? Não me venha com essa, como vou saber?\nGarotas assim têm aos montes por aí, não é?",
        "rewritten",
        "Passante desdenhando da descrição genérica em tom casual."
    ),
    7706: (
        "...É-é verdade...\nDesculpe o incômodo...",
        "rewritten",
        "Lyner recolhendo sua vergonha e pedindo desculpas com voz fraca."
    ),
    7707: (
        "Com tanta gente na rua,\nachar alguém é quase impossível...",
        "rewritten",
        "Lyner tomando consciência da imensidão impessoal da multidão."
    ),
    7708: (
        "...",
        "validated",
        "Lyner paralisado no meio da rua, sentindo a solidão esmagadora."
    ),
    7709: (
        "Droga! Perdido por um, perdido por mil!",
        "rewritten",
        "Lyner abandonando a vergonha num ato de puro desespero."
    ),
    7710: (
        "Leilaaa!!",
        "rewritten",
        "Lyner gritando o nome dela a plenos pulmões na praça."
    ),
    7711: (
        "...Leilaaa!...",
        "rewritten",
        "Lyner chamando novamente com a voz já falhando de exaustão."
    ),
    7712: (
        "O que deu em você, rapaz?\nEstá procurando alguém?",
        "rewritten",
        "Transeunte estranhando a atitude exaltada do jovem."
    ),
    7713: (
        "...!\nAh, n-não... Não é nada.\nDesculpe o alvoroço...",
        "rewritten",
        "Lyner recompondo-se sem jeito diante dos olhares dos curiosos."
    ),
    7714: (
        "...Acabei matando aula hoje de novo...",
        "rewritten",
        "Lyner constatando o abandono total de sua rotina de estudante na simulação."
    ),
    7715: (
        "Lyner!\nAinda bem... você está a salvo! Eu fiquei tão preocupada...",
        "rewritten",
        "Aurica (como jovem colega de Karff) abordando Lyner com alívio carinhoso e aflição."
    ),
    7716: (
        "É mesmo...? Desculpa...",
        "rewritten",
        "Lyner respondendo no piloto automático, com a mente ainda distante."
    ),
    7717: (
        "Você está bem?!\nEstá cambaleando ainda mais do que antes!\nEstá comendo direito? Tem dormido?!",
        "rewritten",
        "Aurica inspecionando o estado deplorável e debilitado de Lyner."
    ),
    7718: (
        "Se eu tivesse tempo para isso,\nestaria procurando a Leila!",
        "rewritten",
        "Lyner reagindo defensivo, fixado unicamente em seu objetivo obsessivo."
    ),
    7719: (
        "Lyner!!\nVolte logo para a realidade!\nA Leila não existe mais neste mundo!",
        "rewritten",
        "Aurica puxando Lyner de volta à razão com firmeza dramática e lágrimas nos olhos."
    ),
    7720: (
        "Pare de viver preso ao passado\ne de se martirizar desse jeito...",
        "rewritten",
        "Aurica suplicando para que ele interrompa aquela espiral de autodestruição."
    ),
    7721: (
        "Eu também... me preocupo tanto com você, fico tão aflita...\nNão cometa mais loucuras... por favor, eu te imploro...",
        "rewritten",
        "Aurica revelando a profundidade do seu amor e a dor de vê-lo definhar."
    ),
    7722: (
        "Aurica...\nPerdão... Não sabia que estava tão aflita por minha causa...",
        "rewritten",
        "Lyner caindo em si e percebendo o sofrimento que estava causando à amiga."
    ),
    7723: (
        "Porque, se você morrer...\neu... o que seria de mim...?!",
        "rewritten",
        "Aurica desabafando com o coração partido o terror de perdê-lo."
    ),
    7724: (
        "Me desculpe... Fiz você sofrer...\nSinto muito mesmo...",
        "rewritten",
        "Lyner reconhecendo com nobreza sua responsabilidade afetiva."
    ),
    7725: (
        "Você tem razão...\nSe eu partisse, haveria quem chorasse por mim\ncom a mesma dor que sinto agora.",
        "rewritten",
        "Lyner atingindo a maturidade de compreender a reciprocidade do luto."
    ),
    7726: (
        "...Por consideração a você, Aurica,\nvou parar de cometer essas loucuras.",
        "rewritten",
        "Lyner prometendo cuidar de si e honrar a vida pelo bem de Aurica."
    ),
    7727: (
        "Lyner...",
        "validated",
        "Aurica aliviada e comovida com a promessa dele."
    ),
    7728: (
        "O tempo fluiu...",
        "rewritten",
        "Transição poética marcando o avanço dos meses e a cicatrização gradual."
    ),
    7729: (
        "No fim, Leila ainda não havia sido encontrada...\nMas a minha mente se acalmou bastante,\ne já não me punha em risco como naquele período.",
        "rewritten",
        "Lyner narrando o apaziguamento de seu coração e a retomada do equilíbrio."
    ),
    7730: (
        "Aos poucos, o meu cotidiano retomava o ritmo sereno\nde antes de eu ter conhecido Leila...",
        "rewritten",
        "Lyner descrevendo a reconciliação com a vida diária na escola cósmica."
    ),
    7731: (
        "Até que...",
        "rewritten",
        "Gancho narrativo anunciando um novo encontro determinante."
    ),
    7732: (
        "...",
        "validated",
        "Silêncio reflexivo diante da aproximação de Misha."
    ),
    7733: (
        "...Misha...",
        "rewritten",
        "Lyner reconhecendo a amiga que surge à sua frente."
    ),
    7734: (
        "Lyner, quanto tempo!\nComo você tem passado?",
        "rewritten",
        "Misha cumprimentando com meiguice e simpatia calorosa."
    ),
    7735: (
        "Graças a Deus, tudo em paz.\nEstou bem mais sereno agora.",
        "rewritten",
        "Lyner respondendo com gentileza e maturidade emocional."
    ),
    7736: (
        "Entendo... Que bom saber.\nNa verdade, eu queria entregar uma coisa para você.\nTome aqui...",
        "rewritten",
        "Misha estendendo a mão para entregar um objeto especial."
    ),
    7737: (
        "...Isso é... um pingente de memória?",
        "rewritten",
        "Lyner fitando o colar de dados com surpresa e curiosidade."
    ),
    7738: (
        "Toda a programação de Leila está armazenada aqui dentro.\nPode ficar com ele.",
        "rewritten",
        "Misha oferecendo o relicário digital contendo o código integral de Leila."
    ),
    7739: (
        "...É um backup dela?",
        "rewritten",
        "Lyner buscando compreender o conteúdo exato do pingente."
    ),
    7740: (
        "Sim.",
        "rewritten",
        "Misha confirmando que se trata de uma cópia integral."
    ),
    7741: (
        "...Compreendo...",
        "rewritten",
        "Lyner contemplando o artefato em silêncio profundo."
    ),
    7742: (
        "Desculpe, mas terei que devolver.",
        "rewritten",
        "Lyner recusando a réplica digital com delicadeza e firmeza."
    ),
    7743: (
        "...Hã?",
        "rewritten",
        "Misha surpresa com a recusa inesperada do presente."
    ),
    7744: (
        "Porque isso aqui...\nnão é a Leila que eu conheci.",
        "rewritten",
        "Lyner enunciando a verdade filosófica sobre a autenticidade humana."
    ),
    7745: (
        "Por mais precisa que seja a cópia, mesmo sem divergir um único bit sequer,\nnão é possível fazer o backup dos sentimentos que ela viveu... Não é?",
        "rewritten",
        "Lyner argumentando com beleza sublime que sentimentos e vivências não cabem em backups."
    ),
    7746: (
        "...",
        "validated",
        "Misha em silêncio absorvendo a sabedoria das palavras dele."
    ),
    7747: (
        "...Tem razão.",
        "rewritten",
        "Misha concordando comovida com a pureza da perspectiva de Lyner."
    ),
    7748: (
        "Não se preocupe.\nAs memórias com a Leila permanecem intactas no meu coração.",
        "rewritten",
        "Lyner assegurando que o verdadeiro templo da memória é a alma."
    ),
    7749: (
        "As horas alegres, as trocas afetuosas,\nos momentos difíceis... absolutamente tudo.",
        "rewritten",
        "Lyner enumerando com carinho toda a gama de experiências compartilhadas."
    ),
    7750: (
        "Desde o instante em que nos conhecemos até o momento da despedida final...\ncada fibra do meu ser se lembra de tudo sobre ela.",
        "rewritten",
        "Lyner afirmando que a lembrança está inscrita na própria carne e no coração."
    ),
    7751: (
        "Por isso... eu não preciso desse pingente.",
        "rewritten",
        "Lyner dispensando o suporte artificial em favor da eternidade do afeto real."
    ),
    7752: (
        "Leila... obrigado.\nFoi por pouco tempo, mas os dias ao seu lado\nserão para sempre as lembranças mais preciosas da minha vida.",
        "rewritten",
        "Lyner dedicando sua gratidão eterna à memória de Leila."
    ),
    7753: (
        "E, onde quer que eu vá, ela estará sempre comigo.",
        "rewritten",
        "Lyner sentindo a presença consoladora e indelével da companheira."
    ),
    7754: (
        "Brilhando sem jamais desbotar,\ncomo uma luz eterna dentro da minha alma...",
        "rewritten",
        "Lyner encerrando seu monólogo lírico com imagem poética de luz eterna."
    ),
    7755: (
        "Lyner!",
        "validated",
        "A voz de Leila ecoando com ternura divina na mente dele."
    ),
    7756: (
        "...",
        "validated",
        "Silêncio do despertar da imersão cósmica."
    ),
    7757: (
        "Chegou ao fim...?",
        "rewritten",
        "Lyner despertando confuso da simulação melodramática ao lado de Shurelia."
    ),
    7758: (
        "Parece que sim.",
        "rewritten",
        "Shurelia confirmando com meiguice e timidez o encerramento do drama escolar."
    ),
    7759: (
        "...É-é um desfecho um tanto desconcertante, não acha...?",
        "rewritten",
        "Lyner coçando a cabeça sem jeito com a carga dramática teatral da história."
    ),
    7760: (
        "É-é verdade...\nMas como foi o episódio final,\nparece que a história não terá continuação...",
        "rewritten",
        "Shurelia justificando com inocência fofa a conclusão definitiva daquela 'série'."
    ),
    7761: (
        "...",
        "validated",
        "Lyner sem saber direito como reagir à sinceridade desajeitada da deusa."
    ),
    7762: (
        "E-então, como a ocasião veio a calhar,\naproveitei para vincular os dados do Demônio Sombra.",
        "rewritten",
        "Shurelia aproveitando o gancho técnico para incorporar a invocação mística."
    ),
    7763: (
        "A partir de agora, você poderá invocá-lo\ncomo uma Magia Vermelha.",
        "rewritten",
        "Shurelia instruindo sobre o uso de Shadow no repertório ofensivo da Canção."
    ),
    7764: (
        "Você criou a Magia Vermelha [Sombra]!",
        "validated",
        "Notificação canônica de sistema da criação da Magia Vermelha [Sombra] (Demônio Shadow)."
    )
}

# =============================================================================
# Validação Técnica Linha a Linha (Hard Gate Determinístico)
# =============================================================================
print("Iniciando validação técnica de integridade das 282 falas...")
total_errors = 0

curated_dialogues = []
translations_list = []
lines_rewritten = 0
lines_approved_as_is = 0

for d in raw_dialogues:
    d_id = d["id"]
    orig_en = d.get("original_en", "")
    orig_jp = d.get("original_jp", "")
    current_pt = d.get("current_ptbr", "")

    if d_id not in curations:
        print(f"ERRO CRÍTICO: Fala ID {d_id} ausente no dicionário de curadoria!")
        total_errors += 1
        continue

    curated_text, verdict, rationale = curations[d_id]

    # Validação com curadoria_validate.validate_line
    errs = validate_line(d_id, orig_en, curated_text)
    if errs:
        print(f"ERRO na fala [{d_id}]: {errs}")
        print(f"  EN: {orig_en}")
        print(f"  PT: {curated_text}")
        total_errors += len(errs)

    if verdict == "rewritten":
        lines_rewritten += 1
    else:
        lines_approved_as_is += 1

    d_entry = dict(d)
    d_entry["curated_ptbr"] = curated_text
    d_entry["text"] = curated_text
    d_entry["verdict"] = verdict
    d_entry["rationale"] = rationale
    curated_dialogues.append(d_entry)

    translations_list.append({
        "id": d_id,
        "text": curated_text
    })

if total_errors > 0:
    print(f"\nFALHA NO HARD GATE: {total_errors} erros detectados. Corrija antes de gerar os arquivos.")
    sys.exit(1)

print(f"SUCESSO ABSOLUTO! 0 erros em 282 falas avaliadas.")

# =============================================================================
# Metadados Editoriais, Destaques, Glossário e Handoff
# =============================================================================
highlights = [
    {
        "id": 7484,
        "speaker": "Lyner",
        "jp": "シュレリア様達の状況がCR掴めない以上、中がどうCRなってるか確認できない。",
        "before": "Não sei como está a Lady Shurelia, então não faço ideia de como é lá dentro.",
        "after": "Sem conseguir contato com a Senhora Shurelia e os outros,\nnão temos como saber a situação lá dentro.",
        "rationale": "Correção canônica do título cerimonioso 'Senhora Shurelia' (シュレリア様), eliminando o decalque inglês 'Lady' e reestruturando a incerteza tática da equipe com naturalidade oral e ritmo."
    },
    {
        "id": 7487,
        "speaker": "Jack",
        "jp": "何のために、ここまで一緒に来たと思ってるんだ。",
        "before": "É um pouco tarde para mudar de ideia.",
        "after": "Pra que você acha que viemos\njuntos até aqui?",
        "rationale": "Resgate absoluto da soberania do original japonês em detrimento da localização americana genérica ('It’s a little late for second thoughts'). Jack demonstra lealdade cínica e camaradagem calejada."
    },
    {
        "id": 7536,
        "speaker": "Radolf",
        "jp": "簡単に言えば、最強に強引なダイブをされた...というCR感じか。",
        "before": "Parece um caso extremo de invasão à força de uma Cosmosfera.",
        "after": "Em termos simples... é como se ela tivesse sofrido\no Mergulho mais brutal e forçado de todos.",
        "rationale": "Radolf sintetiza a tragédia com o termo canônico de sistema 'Mergulho' (ダイブ) com maiúscula, capturando com precisão a agressão psíquica sofrida pela Reyvateil hospedeira."
    },
    {
        "id": 7601,
        "speaker": "Leard",
        "jp": "うむ。君にはプラティナ...CRいや、この世界の命運がCRかかっている。",
        "before": "Hum. O destino de Platina... Não, o destino do mundo está em suas mãos.",
        "after": "Hum. O destino de Platina...\nNão, o destino de todo este mundo repousa sobre você.",
        "rationale": "Austeridade patriarcal e gravidade de Chefe de Estado de Leard Barsett, impondo com dicção sóbria e solene o peso da salvação de Sol Ciel sobre a jovem cantora."
    },
    {
        "id": 7661,
        "speaker": "Estudante da Cosmosfera (Leila)",
        "jp": "確かに「作られたもの」かもしれない。CRでも、私がこの世界を...頼奈を護りたいとCR思う気持ちに嘘はないもの...。",
        "before": "Fui criada por alguém, mas quero mesmo salvar Lyner e o mundo...",
        "after": "Posso até ser algo \"criado por mãos alheias\"...\nMas a vontade sincera que trago no peito de proteger este mundo... e de proteger o Lyner... jamais foi mentira!",
        "rationale": "Clímax lírico da Cosmosfera de Shurelia. Leila contrapõe o insulto mecanicista de Claire com a verdade transcendental do amor e da lealdade ao mundo e a Lyner ('Omoi' - 想い)."
    },
    {
        "id": 7745,
        "speaker": "Lyner",
        "jp": "どんなに精密に、1ビット違わない複製だとしても、「想い」のバックアップまではCRとれないだろ?",
        "before": "Mesmo que seja uma réplica exata, ainda assim não é ela. Não tem os sentimentos dela, tem?",
        "after": "Por mais precisa que seja a cópia, mesmo sem divergir um único bit sequer,\nnão é possível fazer o backup dos sentimentos que ela viveu... Não é?",
        "rationale": "Momento filosófico capital de Lyner: a recusa do pingente de memória prova sua maturidade existencial, reconhecendo que almas e sentimentos vivos jamais podem ser substituídos por meras cópias digitais."
    }
]

new_terms = {
    "Altar of Apostles": {
        "pt": "Altar dos Apóstolos",
        "gender": "masculino",
        "number": "singular",
        "category": "Localização / Lore da Igreja",
        "note": "使徒の祭壇. Santuário sagrado ocupado pelos vírus onde Shurelia e Ayatane lutam exaustivamente para conter a dispersão energética."
    },
    "Purger": {
        "pt": "Purger",
        "gender": "masculino",
        "number": "singular",
        "category": "Hymn Crystal / Lore",
        "note": "パージャ. Cristal Hymmnos sagrado de purificação capaz de impedir a desmaterialização dos vírus em energia e erradicá-los."
    },
    "Demon Shadow": {
        "pt": "Demônio Sombra / Magia Vermelha [Sombra]",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia Vermelha / Invocação",
        "note": "魔神シャドウ / 赤魔法【魔神シャドウ】. Invocação mágica ofensiva tecida na conclusão do drama de Shurelia na Cosmosfera."
    },
    "Memory Pendant": {
        "pt": "Pingente de Memória",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Simulação Cósmica",
        "note": "メモリペンダント. Artefato simbólico que guardava a cópia do programa de Leila Togasaki na simulação escolar."
    }
}

updated_address_matrix = {
    "Lyner": {
        "Leard": "Respeito filial firme, porém contestando vigorosamente a frieza e o tom intimidador do pai diante da vulnerabilidade das Reyvateils ('Pai!! Por que tem que intimidar a garota?!').",
        "Shurelia (Leila)": "Vínculo romântico e transcendente na Cosmosfera ('eu só queria... passar mais um minuto, mais um segundo que fosse ao lado da Leila...'), valorizando os sentimentos vivos e a memória do coração acima de réplicas digitais.",
        "Aurica": "Promessa de sobrevivência e afeto maduro ('Por consideração a você, Aurica, vou parar de cometer essas loucuras').",
        "Misha": "Companheirismo protetor de infância, confortando-a ao ter de se separar em Platina ('Fica tranquila, Misha... vamos voltar rapidinho')."
    },
    "Leard": {
        "Lyner": "Tom austero, exigindo rigor militar supremo sem afrouxar a disciplina paternal ('O destino do mundo repousa sobre vocês. Não baixe a guarda nem por um instante').",
        "Aurica": "Autoridade de líder de estado, transferindo o peso esmagador da sobrevivência de Platina e do mundo ('O fracasso é inadmissível. Cante com toda a gravidade de seu coração').",
        "Misha": "Confiança estrita na Reyvateil Origin de Platina, exigindo prontidão absoluta sem espaço para deslizes ('Misha... Sendo você, tenho certeza de que cumprirá o dever')."
    },
    "Aurica": {
        "Lyner": "Devoção doce e preocupação profunda ('Prometa que vai voltar... com vida'), puxando-o de volta à realidade durante o luto na Cosmosfera com coragem e lágrimas.",
        "Leard": "Respeito cerimonioso e temor reverente ('É-é uma honra conhecê-lo...')."
    },
    "Shurelia (Leila)": {
        "Lyner": "Sacrifício heróico e confissão lírica de que seus sentimentos são reais ('a vontade sincera que trago no peito de proteger este mundo... e de proteger o Lyner... jamais foi mentira!')."
    }
}

scene_handoff = {
    "resumo_dramatico": "A batalha de alta tensão no Altar dos Apóstolos, onde Lyner entrega o Purger para socorrer a Senhora Shurelia e Ayatane, culminando na purificação que encurrala os vírus e força uma invasão violenta na mente da heroína receptora (Aurica ou Misha), mergulhando-a em estado de coma; a reunião estratégica no gabinete de Platina com o Governador Leard Barsett, que cobra rigor implacável e designa uma das heroínas para a defesa da cidade; e a comovente conclusão do drama escolar na Cosmosfera de Shurelia, onde o sacrifício de Leila Togasaki contra Claire imortaliza a pureza do 'Omoi' (sentimento verdadeiro), levando Lyner ao luto profundo e à recusa filosófica do pingente de memória em prol das lembranças vivas do coração, culminando no despertar e na aquisição da Magia Vermelha [Sombra].",
    "decisoes_terminologicas": {
        "Altar dos Apóstolos": "[Altar dos Apóstolos] (使徒の祭壇, local sagrado de contenção dos vírus)",
        "Purger": "[Purger] (パージャ, cristal Hymmnos ancestral de erradicação viral)",
        "Sombra": "Magia Vermelha [Sombra] / Demônio Sombra (魔神シャドウ / 赤魔法【魔神シャドウ】)",
        "Pingente de Memória": "Pingente de Memória (メモリペンダント, suporte de backup de Leila)",
        "Omoi": "Sentimento / Anseio (想い, conceito filosófico de sentimentos vivos irredutíveis a programas)"
    },
    "alertas_para_proximo_bloco": "Atenção máxima ao deslocamento urgente para o Centro de Mergulho (Dive Shop) para adentrar a Cosmosfera da heroína em coma, expurgar o vírus invasor entranhado em seu âmago psíquico e estabilizar as defesas de Platina rumo ao desfecho."
}

output_data = {
    "block_id": "BLK_EVD_030",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "total_lines": len(curated_dialogues),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "highlights": highlights,
    "new_terms": new_terms,
    "updated_address_matrix": updated_address_matrix,
    "scene_handoff": scene_handoff,
    "dialogues": curated_dialogues,
    "entries": curated_dialogues,
    "translations": translations_list
}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Sucesso absoluto! Gravado {OUTPUT_PATH.name} com {len(curated_dialogues)} falas ({lines_rewritten} reescritas, {lines_approved_as_is} aprovadas).")

# Gera relatório consolidado
report_data = {
    "block_id": "BLK_EVD_030",
    "completed_at": "2026-11-01T01:05:00+00:00",
    "total_dialogues": len(curated_dialogues),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "new_terms_added": len(new_terms),
    "scene_handoff": scene_handoff,
    "highlights_count": len(highlights)
}

with open(REPORT_PATH, "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print(f"Gravado {REPORT_PATH.name} com sucesso.")

import json
from pathlib import Path

curated_map = {
    # --- Event/3.evd (11031 - 11118) ---
    11031: {
        "text": "Está tão calmo.",
        "notes": "Lyner comenta a aparente tranquilidade de Platina antes do ataque iminente."
    },
    11032: {
        "text": "Pois é. A própria calmaria.",
        "notes": "Ayatane concorda com tom reflexivo e sereno."
    },
    11033: {
        "text": "Aquilo...",
        "notes": "Shurelia avista uma presença ao longe."
    },
    11034: {
        "text": "Aquilo... é o ELMA...?",
        "notes": "Shurelia hesita ao reconhecer a silhueta do guardião sagrado."
    },
    11035: {
        "text": "ELMA? É o nome daquele vírus?",
        "notes": "Lyner pergunta com curiosidade juvenil."
    },
    11036: {
        "text": "Não. ELMA é um guardião da Torre que eu mesma criei.",
        "notes": "Shurelia esclarece que ELMA é uma de suas criações mecânicas protetoras."
    },
    11037: {
        "text": "Aquele vírus apenas se assemelha de forma idêntica ao ELMA.",
        "notes": "Shurelia constata com sobriedade a mímica visual do vírus."
    },
    11038: {
        "text": "Um guardião? Não pode ser...",
        "notes": "Lyner reage incrédulo à usurpação do guardião divino."
    },
    11039: {
        "text": "Não é algo impossível.",
        "notes": "Ayatane pondera com frieza analítica."
    },
    11040: {
        "text": "Os vírus fazem ninho no Campo Binário de dados da Torre.",
        "notes": "Ayatane explica a natureza dos vírus aninhados na dimensão de dados (バイナリ情報野)."
    },
    11041: {
        "text": "Se eles corromperem os bancos de dados de um guardião, esse é o resultado inevitável.",
        "notes": "Ayatane deduz o processo de assimilação lógica (必然とそうなる)."
    },
    11042: {
        "text": "Mas isso é só na teoria!",
        "notes": "Lyner recusa-se a aceitar a fragilidade da tecnologia sagrada."
    },
    11043: {
        "text": "Como se um guardião da Senhora Shurelia fosse ser tomado assim tão fácil!",
        "notes": "Lyner exalta sua fé inabalável em Shurelia e no guardião (乗っ取られてたまるか)."
    },
    11044: {
        "text": "Chega de conversa.",
        "notes": "Shurelia corta o diálogo com autoridade serena ante a aproximação do perigo."
    },
    11045: {
        "text": "Ele vem aí!",
        "notes": "Shurelia alerta para a ofensiva inimiga."
    },
    11046: {
        "text": "Vou preparar o Cântico!\nAté lá, conto com o apoio de vocês!",
        "notes": "Shurelia solicita cobertura marcial enquanto sintoniza a canção sagrada."
    },
    11047: {
        "text": "Entendido!",
        "notes": "Lyner confirma com prontidão militar."
    },
    11048: {
        "text": "Heh, vou mostrar com tudo o poder de um Cavaleiro de Elemia!",
        "notes": "Lyner empunha sua espada com determinação arrojada (存分に見せてやるぜ)."
    },
    11049: {
        "text": "Não baixem a guarda.\nVocês dois quase não têm experiência em combate real.",
        "notes": "Shurelia adverte os jovens cavaleiros recém-formados com zelo materno."
    },
    11050: {
        "text": "Eu sei, eu sei! Vamos nessa!",
        "notes": "Lyner parte para o confronto com impetuosidade heroica."
    },
    11051: {
        "text": "O quê?!",
        "notes": "Lyner choca-se com a ineficácia dos ataques."
    },
    11052: {
        "text": "O Cântico da Senhora Shurelia...",
        "notes": "Ayatane observa atônito o cancelamento da magia fônica."
    },
    11053: {
        "text": ".........",
        "notes": "Shurelia cala-se momentaneamente sob o impacto do contra-ataque."
    },
    11054: {
        "text": "Guaaargh!!",
        "notes": "Lyner é atingido com violência."
    },
    11055: {
        "text": "Maldito! Ele consegue atacar mesmo desse jeito?!",
        "notes": "Ayatane alarma-se com a capacidade ofensiva anômala do vírus."
    },
    11056: {
        "text": "Maldição...!!",
        "notes": "Lyner pragueja sob dor e fúria juvenil."
    },
    11057: {
        "text": "Não pode ser...",
        "notes": "Lyner sente o peso da impotência física diante do oponente."
    },
    11058: {
        "text": "Desse jeito, não temos como fazer nada...",
        "notes": "Ayatane reconhece a impossibilidade de vitória no confronto direto."
    },
    11059: {
        "text": "Precisamos recuar por agora.",
        "notes": "Shurelia ordena o recuo tático imediato."
    },
    11060: {
        "text": "Recuar?!",
        "notes": "Lyner questiona relutante a ordem de retirada."
    },
    11061: {
        "text": "Parece que aquele vírus consegue transitar livremente entre o Campo Binário e este mundo real.",
        "notes": "Shurelia diagnostica a mobilidade interdimensional do vírus."
    },
    11062: {
        "text": "O Campo Binário é um mundo amorfo, composto apenas por corpos de energia.",
        "notes": "Shurelia explica a ausência de corporeidade tangível no Campo Binário."
    },
    11063: {
        "text": "Por isso, desde que haja linhas de condução fônica conectadas, ele pode ir a qualquer lugar.",
        "notes": "Shurelia aponta a vulnerabilidade das linhas de condução fônica (導力ライン)."
    },
    11064: {
        "text": "Do jeito que estamos, é impossível derrotar este vírus.",
        "notes": "Shurelia conclui categoricamente sobre a inviabilidade do combate convencional."
    },
    11065: {
        "text": "Além disso, para vocês que acabaram de se tornar cavaleiros, é um oponente cruel demais.\nO mais sensato agora é bater em retirada.",
        "notes": "Restauração do original japonês suprimido pela NISA: Shurelia destaca que eles recém se tornaram cavaleiros."
    },
    11066: {
        "text": "Rápido, enquanto ainda dá tempo!",
        "notes": "Ayatane incita a fuga estratégica."
    },
    11067: {
        "text": "Vou fechar temporariamente o Plug Sinfônico!\nFujam depressa!",
        "notes": "Ayatane prepara o isolamento emergencial do Plug Sinfônico (導力プラグ)."
    },
    11068: {
        "text": "Compreendido.\nLyner.",
        "notes": "Shurelia coordena a evacuação chamando Lyner para a formação."
    },
    11069: {
        "text": "Pode deixar! A retaguarda é comigo!",
        "notes": "Lyner assume bravamente a posição de retaguarda protetora (しんがり)."
    },
    11070: {
        "text": "Aqui é o Portão de Antepara A7.\nO operador de autenticação deve dar um passo à frente.",
        "notes": "Comando automatizado da antepara de contenção (A7隔壁ゲート)."
    },
    11071: {
        "text": "Meu nome é Ayatane Michitaka!\nVou selar o Plug Sinfônico!",
        "notes": "Ayatane declara seu nome completo e intenção de selamento do Plug Sinfônico."
    },
    11072: {
        "text": "#0Was i ga exec bansh A7 al noes!",
        "notes": "Comando de execução sagrado na língua Hymmnos preservado rigorosamente sem alterações."
    },
    11073: {
        "text": "Código autenticado.",
        "notes": "Resposta afirmativa do sistema de controle de Platina."
    },
    11074: {
        "text": "Vinte e cinco segundos para o fechamento da antepara.\nSituação: a passagem pelo portão fica proibida a partir de agora.",
        "notes": "Protocolo de contagem regressiva da comporta de segurança."
    },
    11075: {
        "text": "Com isso, devemos conseguir ganhar um pouco de tempo.",
        "notes": "Ayatane avalia o efeito do bloqueio físico emergencial."
    },
    11076: {
        "text": "Tenho minhas dúvidas quanto a isso.",
        "notes": "Shurelia manifesta ceticismo justificado por sua sabedoria milenar."
    },
    11077: {
        "text": "Para um corpo de energia, você acredita que trancar uma porta física tenha alguma serventia?",
        "notes": "Shurelia questiona a eficácia de anteparas sólidas contra formas de vida etéreas."
    },
    11078: {
        "text": "Sendo assim, o que poderíamos fazer...?",
        "notes": "Ayatane indaga buscando uma alternativa tática viável."
    },
    11079: {
        "text": "A única saída é destruí-lo.",
        "notes": "Shurelia dita a imperiosa necessidade de extermínio total da ameaça."
    },
    11080: {
        "text": "Mas se os nossos ataques nem fazem efeito, não tem como derrotar nada!",
        "notes": "Lyner expressa sua frustração pragmática com a invulnerabilidade viral."
    },
    11081: {
        "text": "Não é que não haja um jeito...",
        "notes": "Shurelia revela a existência de um recurso ancestral reservado."
    },
    11082: {
        "text": "E que jeito seria esse?",
        "notes": "Ayatane pede esclarecimentos objetivos."
    },
    11083: {
        "text": "Um Cristal Hymmnos.",
        "notes": "Shurelia menciona a tecnologia fônica sagrada dos Cristais Hymmnos."
    },
    11084: {
        "text": "Exatamente. Para derrotar aquele vírus, temos que impedi-lo de fugir para o Campo Binário.",
        "notes": "Shurelia delineia o princípio de combate: bloquear a fuga para o Campo Binário."
    },
    11085: {
        "text": "O cristal que abriga esse poder é o [Cristal Hymmnos Purger].",
        "notes": "Shurelia nomeia o artefato canônico sagrado com colchetes de paridade."
    },
    11086: {
        "text": "Então, se trouxermos esse cristal para cá...!",
        "notes": "Lyner compreende a missão e antevê a solução."
    },
    11087: {
        "text": "Infelizmente, o [Cristal Hymmnos Purger] não se encontra em Platina nos dias de hoje.",
        "notes": "Shurelia lamenta a perda do artefato no topo da Torre."
    },
    11088: {
        "text": "Ouvi dizer que está consagrado em uma instalação no mundo inferior, nas [Asas de Horus].",
        "notes": "Shurelia aponta a localização mítica do Purger no Mundo Inferior."
    },
    11089: {
        "text": "Nas [Asas de Horus]?!... Aquele continente flutuante onde dizem que existe chão de 'terra'...?",
        "notes": "Lyner relembra com assombro as lendas sobre o continente flutuante coberto de solo natural."
    },
    11090: {
        "text": "Cuidado! Ele está vindo!",
        "notes": "Ayatane detecta o avanço iminente da criatura."
    },
    11091: {
        "text": "Por ora, vamos sair daqui o mais depressa possível!",
        "notes": "Shurelia apressa os companheiros diante do ataque iminente."
    },
    11092: {
        "text": ".........",
        "notes": "Lyner hesita, tomado por uma decisão súbita e audaciosa."
    },
    11093: {
        "text": "Lyner! O que está fazendo?! Depressa...",
        "notes": "Shurelia clama pelo jovem cavaleiro estático."
    },
    11094: {
        "text": "Senhora Shurelia!\nA aeronave lá no hangar de Gather... a senhora me emprestaria?!",
        "notes": "Lyner faz o pedido ousado para pilotar a aeronave ancestral em Gather."
    },
    11095: {
        "text": "Lyner?!",
        "notes": "Ayatane sobressalta-se com a ousadia do amigo."
    },
    11096: {
        "text": "Lyner... você...",
        "notes": "Shurelia comove-se e surpreende-se com a proposta do rapaz."
    },
    11097: {
        "text": "Eu vou até as [Asas de Horus] e encontro o [Cristal Hymmnos Purger]!",
        "notes": "Lyner assume o compromisso solene de resgatar o Cristal Purger no Mundo Inferior."
    },
    11098: {
        "text": "A Senhora Shurelia e os outros... por favor, fiquem esperando em Platina!",
        "notes": "Restauração do japonês soberano: Lyner pede que Shurelia e os demais aguardem em segurança."
    },
    11099: {
        "text": "O... o que você está dizendo...?!",
        "notes": "Shurelia balbucia surpresa pela coragem altruísta do jovem."
    },
    11100: {
        "text": ".........",
        "notes": "Ayatane observa em silêncio o ardor de Lyner."
    },
    11101: {
        "text": "Senhora Shurelia! Eu lhe imploro!",
        "notes": "Lyner reforça seu apelo com fervor sincero."
    },
    11102: {
        "text": "Eu quero... salvar Platina... quero salvar todo mundo!",
        "notes": "Declaração fundamental do caráter protetor e compassivo de Lyner."
    },
    11103: {
        "text": "Senhora Shurelia...\nVamos acolher a determinação do Lyner.",
        "notes": "Ayatane intercede em favor de Lyner (心意気を汲みましょう)."
    },
    11104: {
        "text": "...Compreendo.",
        "notes": "Shurelia anui com dignidade e respeito à coragem do cavaleiro."
    },
    11105: {
        "text": "Lyner Barsett. Eu lhe ordeno a busca pelo [Cristal Hymmnos Purger].",
        "notes": "Shurelia emite a ordem oficial solene com tratamento nominal canônico."
    },
    11106: {
        "text": "A aeronave em Gather fica cedida para o seu uso, Lyner.",
        "notes": "Shurelia concede a autorização especial para utilização da nave sagrada."
    },
    11107: {
        "text": "E mais uma coisa...",
        "notes": "Shurelia interrompe-se para entregar a herança fônica."
    },
    11108: {
        "text": "Fique com este pingente...\nDentro dele estão gravados os diagramas tridimensionais do [Purger].",
        "notes": "Shurelia entrega a joia contendo a planta sagrada do Purger."
    },
    11109: {
        "text": "Senhora Shurelia... Muito obrigado!",
        "notes": "Lyner agradece com genuína emoção filial."
    },
    11110: {
        "text": "Obteve o [Broche Hymmnos]!",
        "notes": "Mensagem de sistema para obtenção do artefato de navegação (ヒュムネブローチ)."
    },
    11111: {
        "text": "Senhora Shurelia! Se não formos rápido... ele vai...!!",
        "notes": "Ayatane alerta para o cerco iminente do vírus."
    },
    11112: {
        "text": "...",
        "notes": "Shurelia despede-se com olhar carregado de preces silenciosas."
    },
    11113: {
        "text": "Senhora Shureliaaa! Ayataneee!",
        "notes": "Lyner acena partindo na aeronave a todo vapor."
    },
    11114: {
        "text": "Podem esperar lembrancinhas na voltaaa!",
        "notes": "Lyner despede-se com sua descontração juvenil carinhosa (おみやげ期待しててくれよー)."
    },
    11115: {
        "text": "...",
        "notes": "Ayatane fita a partida de Lyner com olhar indecifrável."
    },
    11116: {
        "text": "...Ficaremos à sua espera.",
        "notes": "Shurelia murmura votos doces pelo retorno do jovem cavaleiro."
    },
    11117: {
        "text": "Tsc!! Ele me alcançou?!",
        "notes": "Lyner surpreende-se no ar ao ser interceptado por uma criatura viral."
    },
    11118: {
        "text": "Droga! Vai ser aqui mesmo...?!",
        "notes": "Lyner prepara-se para a queda vertiginosa além da barreira de plasma."
    },

    # --- Event/526.evd (11119 - 11162) ---
    11119: {
        "text": "E aí, Lyner.\nJá vamos partir?",
        "notes": "Krusche aborda Lyner em tom casual e descontraído no acampamento."
    },
    11120: {
        "text": "Não, não é isso, não... É que fiquei meio preocupado com você.",
        "notes": "Lyner explica timidamente sua inquietação pelo estado emotivo da piloto."
    },
    11121: {
        "text": "Posso me sentar aqui do lado?",
        "notes": "Lyner pede licença com delicadeza afetuosa."
    },
    11122: {
        "text": "Que sujeito esquisito.\nNem estamos namorando nem nada,\ne fica aí todo preocupado.",
        "notes": "Krusche provoca Lyner com sua ironia defensiva característica."
    },
    11123: {
        "text": "Claro que fico preocupado.\nNão posso me importar com uma companheira?",
        "notes": "Lyner retruca ressaltando o valor dos laços de amizade do grupo."
    },
    11124: {
        "text": "Tipo bancando o meu irmão mais velho, é? Gostei. Até que curto uma parada assim.",
        "notes": "Krusche acolhe a postura protetora fraterna de Lyner (兄貴って感じ)."
    },
    11125: {
        "text": "Se o Luke tivesse se importado comigo metade do que você se importa, quem sabe...",
        "notes": "Krusche desabafa a mágoa do relacionamento frio com o ex-namorado desaparecido."
    },
    11126: {
        "text": "...Ele te deixava de lado?",
        "notes": "Lyner indaga com empatia sincera sobre a frieza de Luke."
    },
    11127: {
        "text": "Aquela caixa de ferramentas de antes...\nFoi um presente que eu dei para ele.",
        "notes": "Krusche revela a história afetiva por trás do jogo de ferramentas devolvido."
    },
    11128: {
        "text": "Quer dizer que... ele devolveu?",
        "notes": "Lyner compreende o peso da rejeição implícita na devolução."
    },
    11129: {
        "text": "Bom, acho que foi o jeito dele\nde colocar um ponto final de vez.",
        "notes": "Krusche analisa a atitude de Luke como demarcação fria de limites (けじめ)."
    },
    11130: {
        "text": "Entendi...\nO tal do Luke era bem desapegado, né?",
        "notes": "Lyner define o desapego emocional do engenheiro rival (淡泊な人)."
    },
    11131: {
        "text": "É, por aí. Mas, independentemente de gostar ou não das pessoas, ele simplesmente era desse jeito.",
        "notes": "Krusche pondera que o distanciamento era parte intrínseca da personalidade dele."
    },
    11132: {
        "text": "Quando ele mergulhava de cabeça nas pesquisas,\nnão conseguia mais enxergar nada além delas.",
        "notes": "Krusche descreve a obsessão técnica cega de Luke pela ciência das aeronaves."
    },
    11133: {
        "text": "Por isso acabei achando\nque precisava entrar no campo de visão dele.",
        "notes": "Krusche confessa a motivação amorosa que a levou ao estudo da mecânica aérea."
    },
    11134: {
        "text": "E foi por isso...\nque você virou engenheira de aeronaves?",
        "notes": "Lyner conecta as peças do passado vocacional da companheira."
    },
    11135: {
        "text": "...Isso mesmo.\nAté então... eu não ligava a mínima para aeronaves.",
        "notes": "Krusche admite seu desinteresse original por dirigíveis antes de se apaixonar."
    },
    11136: {
        "text": "Eu era só uma garota comum,\nque no máximo sintetizava uns mísseis no Grathmeld...",
        "notes": "Krusche descreve com comicidade seu conceito peculiar de 'garota comum' fabricando mísseis."
    },
    11137: {
        "text": "...E criar mísseis no Grathmeld...\né coisa de garota normal...?",
        "notes": "Lyner estranha comicalmente a noção de normalidade bélica de Krusche."
    },
    11138: {
        "text": "Claro que é! E olha que no passado\neu até usava vestidinhos sem problema.\nMeu cabelo também era compridão.",
        "notes": "Krusche defende sua antiga feminilidade com vestidos e longas madeixas."
    },
    11139: {
        "text": "É... é sério...?! Não consigo nem imaginar...",
        "notes": "Lyner engasga ante a ideia surreal de ver Krusche vestida de princesa."
    },
    11140: {
        "text": "...Quer que eu te atire para fora da aeronave?",
        "notes": "Krusche ameaça Lyner com sarcasmo e violência afetuosa de engenheira."
    },
    11141: {
        "text": "Ah, não, que isso, era brincadeira! Que ideia! Ahahaha!",
        "notes": "Lyner recua em pânico cômico ante a truculência da piloto."
    },
    11142: {
        "text": "...",
        "notes": "Krusche fita o vazio com olhar nostálgico e melancólico."
    },
    11143: {
        "text": "Bom... a história com o Luke já são águas passadas dentro de mim, mas...",
        "notes": "Krusche tenta convencer a si mesma de que superou a separação."
    },
    11144: {
        "text": "De vez em quando... quando rola uma coisa dessas, me vêm lembranças tão vívidas.",
        "notes": "Krusche expressa o impacto de encontrar gatilhos da memória do amor perdido."
    },
    11145: {
        "text": "E aí... bate uma solidão daquelas...",
        "notes": "Krusche baixa a guarda demonstrando sua rara vulnerabilidade emotiva."
    },
    11146: {
        "text": "Krusche...\nVai ficar tudo bem! Alguém incrível como você com certeza vai encontrar outra pessoa bacana...",
        "notes": "Lyner tenta consolá-la com o desajeitado otimismo de um companheiro fiel."
    },
    11147: {
        "text": "...",
        "notes": "Krusche encara Lyner fixamente após a frase dele."
    },
    11148: {
        "text": "Q-Que foi...?",
        "notes": "Lyner treme sob o olhar penetrante da amiga."
    },
    11149: {
        "text": "Sendo assim, Lyner...\nnamora comigo.",
        "notes": "Krusche lança a proposta provocativa com ar dissimulado e desafiador."
    },
    11150: {
        "text": "...Hããã?! M-M-Mas isso aí é...",
        "notes": "Lyner entra em curto-circuito total ante o choque romântico súbito."
    },
    11151: {
        "text": "...Relaxa.\nNão tem a menor chance disso acontecer mesmo.",
        "notes": "Krusche desfaz a tensão rindo do desespero do rapaz."
    },
    11152: {
        "text": "Q-Que susto...\nLarga mão desse tipo de piada, pô...",
        "notes": "Lyner respira aliviado e reclama da pegadinha embaraçosa."
    },
    11153: {
        "text": "Você não tem imunidade nenhuma para essas conversas, né, Lyner?\nBem pior do que eu.",
        "notes": "Krusche debocha da inocência virginal e falta de jogo de cintura romântico de Lyner."
    },
    11154: {
        "text": "Me erra.",
        "notes": "Lyner resmunga emburrado rejeitando a provocação (ほっとけ)."
    },
    11155: {
        "text": "Desse jeito, no dia em que eu botar um vestido,\nvocê cai duro de costas na certa.",
        "notes": "Krusche zomba prevendo o desmaio dele diante de seu charme feminino."
    },
    11156: {
        "text": "...Quanta confiança, hein.\nMas confesso que até fiquei curioso para ver...",
        "notes": "Lyner rebate admitindo timidamente uma ponta de curiosidade."
    },
    11157: {
        "text": "...B-Bom, se rolar uma oportunidade qualquer hora dessas, quem sabe.",
        "notes": "Krusche perde o rebolero por um instante e cora de leve ante a réplica dele."
    },
    11158: {
        "text": "...Opa, acabei me enrolando demais aqui. Vamos nessa?",
        "notes": "Krusche recompõe a compostura prática e sugere o retorno à marcha."
    },
    11159: {
        "text": "Lyner.\nObrigada por se preocupar comigo.",
        "notes": "Krusche agradece com carinho e amizade sincera."
    },
    11160: {
        "text": "Magina.\nNão foi nada.",
        "notes": "Lyner responde com generosidade e camaradagem calorosa."
    },
    11161: {
        "text": "Não serviu muito de conselho, mas já me sinto bem mais aliviada.",
        "notes": "Krusche finaliza com seu clássico cutucão afetuoso (気は楽になるよ)."
    },
    11162: {
        "text": "Você sempre tem que soltar uma a mais...",
        "notes": "Lyner suspira conformado com o estilo incorrigível da engenheira."
    },

    # --- Event/362.evd (11163 - 11193) ---
    11163: {
        "text": "Acabamos nos dispersando...",
        "notes": "Cavaleiro relata o caos da emboscada sofrida pelo esquadrão."
    },
    11164: {
        "text": "Fomos pegos de surpresa...\nAinda aguenta entoar?",
        "notes": "Cavaleiro indaga a donzela Reyvateil se ela ainda possui vigor fônico."
    },
    11165: {
        "text": "Arf... arf...\nAcho que vai ser puxado...",
        "notes": "Reyvateil ferida tenta recuperar o fôlego sem rubricas cênicas artificiais."
    },
    11166: {
        "text": "Entendido. A gente vai focar na defesa, então descanse um pouco.",
        "notes": "Cavaleiro protege sua cantora instruindo-a a poupar energia."
    },
    11167: {
        "text": "Tá bom. Me desculpem... numa hora dessas...",
        "notes": "Reyvateil lamenta sua exaustão física em momento crítico."
    },
    11168: {
        "text": "Esquenta não. Faz parte passar por isso.",
        "notes": "Cavaleiro demonstra bravura solidária consolando a parceira."
    },
    11169: {
        "text": "Ainda assim... quem diabos são aqueles sujeitos?!",
        "notes": "Cavaleiro questiona a identidade dos fanáticos armados."
    },
    11170: {
        "text": "Não faço ideia... Lá vêm eles!",
        "notes": "Alerta de nova investida hostil da turba inimiga."
    },
    11171: {
        "text": "Olha só, ainda tinha gente da seita pagã por aqui!",
        "notes": "Fanático acusa os cavaleiros de pertencerem a uma heresia (邪教の徒)."
    },
    11172: {
        "text": "Vamos exterminar até o último de vocês!\nCerto, hora do Cântico! Vai!",
        "notes": "Comandante dos agressores ordena o extermínio e a ativação da Magia da Canção."
    },
    11173: {
        "text": "Eu já não... tenho forças...",
        "notes": "Reyvateil agressores hesita, à beira do esgotamento."
    },
    11174: {
        "text": "O que está dizendo?!\nSe não entoar agora, vai entoar quando?!",
        "notes": "Fanático pressiona impiedosamente a donzela exausta."
    },
    11175: {
        "text": "Creia na bênção do Trio de Elemia e entoe o seu canto!",
        "notes": "Invocação fervorosa do Trio de Elemia (エレミア三謳神) como justificativa de combate."
    },
    11176: {
        "text": "S-Sim... Entendido.",
        "notes": "Reyvateil rende-se coagida à ordem fanática."
    },
    11177: {
        "text": "Droga... É o nosso fim...?!",
        "notes": "Cavaleiro encurralado teme o aniquilamento pela canção adversária."
    },
    11178: {
        "text": "Não desistam! Lutem até o fim!",
        "notes": "Grito de resistência desesperada ante a morte iminente."
    },
    11179: {
        "text": "...Finalmente... eu retornei.",
        "notes": "A aparição espectral e sombria de Kyle Clancy pronuncia seu retorno."
    },
    11180: {
        "text": "O que significa tudo isto...?!\nO que está acontecendo?!",
        "notes": "Governador Leard exige respostas diante da convulsão fônica de Platina."
    },
    11181: {
        "text": "Leard...\nParece que baixamos a guarda em excesso...",
        "notes": "Shurelia constata com pesar a brecha deixada nas defesas da cidadela."
    },
    11182: {
        "text": "Disso eu estou mais do que ciente...",
        "notes": "Leard reconhece amargurado a gravidade da conjuntura."
    },
    11183: {
        "text": "Não, não me refiro a isso...\nÉ Kyle Clancy!",
        "notes": "Shurelia aponta o verdadeiro mentor da crise: o cientista traidor Kyle Clancy."
    },
    11184: {
        "text": "O... O quê?!",
        "notes": "Leard estupefato ante o retorno do arqui-inimigo dado como morto."
    },
    11185: {
        "text": "Quanto tempo...\nSenhora Shurelia... Leard...",
        "notes": "Kyle Clancy saúda seus antigos superiores com ironia macabra."
    },
    11186: {
        "text": "Kyle Clancy acaba de retornar são e salvo.",
        "notes": "Kyle anuncia formalmente sua triunfal ressurreição em Sol Ciel."
    },
    11187: {
        "text": "Junto a um poder grandioso...!",
        "notes": "Kyle proclama o controle das forças virais ancestrais."
    },
    11188: {
        "text": "Ugh...!!",
        "notes": "Shurelia sofre um choque fônico ao sentir a ressonância maligna."
    },
    11189: {
        "text": "Ah...",
        "notes": "Lyner tropeça repentinamente no presente, pressentindo a catástrofe."
    },
    11190: {
        "text": "...O que houve?",
        "notes": "Radolf nota a hesitação repentina de Lyner na marcha."
    },
    11191: {
        "text": "O cadarço da minha bota arrebentou...",
        "notes": "Lyner abaixa-se para consertar o calçado rompido (靴ひもが切れた)."
    },
    11192: {
        "text": "Isso é mau agouro...",
        "notes": "Ayatane comenta a superstição sinistra associada ao rompimento de fios."
    },
    11193: {
        "text": "Desculpem a demora.",
        "notes": "Lyner levanta-se apressado para retomar o trajeto com o pelotão."
    },

    # --- Event/239.evd (11194 - 11256) ---
    11194: {
        "text": "Ué?\nTem uma multidão se aglomerando ali...",
        "notes": "Lyner avista o tumulto perto da abertura da Torre."
    },
    11195: {
        "text": "Não é aqui que diziam ter um buraco que dá para o interior da Torre?",
        "notes": "Jack reconhece a localização da fenda secreta nos alicerces."
    },
    11196: {
        "text": "...!? Mas o que é...",
        "notes": "Lyner aproxima-se e percebe a briga iminente entre civis e guardas."
    },
    11197: {
        "text": "Por favor! Se eu não voltar logo para o Beco Vagalume, vou à falência!",
        "notes": "Comerciante desesperado suplica passagem para salvar suas mercadorias."
    },
    11198: {
        "text": "Deixem a gente passar por dentro da Torre! Eu imploro!",
        "notes": "Mercador apela pelo trânsito seguro pelo interior da estrutura."
    },
    11199: {
        "text": "Isso é impossível.\nA entrada de vocês está terminantemente proibida.",
        "notes": "Guarda Teru barra friamente os refugiados seguindo ordens estritas."
    },
    11200: {
        "text": "Este lugar não é propriedade de vocês!",
        "notes": "Cidadão enfurecido questiona a autoridade territorial dos Teru."
    },
    11201: {
        "text": "Não é nossa propriedade. Mas temos a missão de proteger este lugar.\nNão deixaremos vocês subirem.",
        "notes": "Guarda Teru reitera seu juramento marcial de proteger a passagem."
    },
    11202: {
        "text": "O que foi que disse, seus bostas?!\nVocês vivem ficando no nosso caminho o tempo todo!",
        "notes": "Humano revoltado explode em impropérios contra a etnia Teru."
    },
    11203: {
        "text": "Hoje a paciência acabou!",
        "notes": "Ameaça de confronto violento imediato."
    },
    11204: {
        "text": "Parem com isso!",
        "notes": "Lyner intervém energicamente para evitar o derramamento de sangue."
    },
    11205: {
        "text": "Lyner?!",
        "notes": "Misha sobressalta-se vendo o rapaz pular no meio da contenda."
    },
    11206: {
        "text": "Os dois lados, parem agora mesmo!",
        "notes": "Lyner ergue a voz exigindo o fim das hostilidades mútuas."
    },
    11207: {
        "text": "Quem é você?!",
        "notes": "Civil hostil repele a intromissão do forasteiro."
    },
    11208: {
        "text": "Eu não sei o que está pegando,\nmas parem de brigar agora mesmo!",
        "notes": "Lyner tenta acalmar os ânimos exaltados."
    },
    11209: {
        "text": "Cala a boca!",
        "notes": "O agressor humano empurra ou grita desdenhando do apelo."
    },
    11210: {
        "text": "O que pensa que está fazendo?!",
        "notes": "Misha sai em defesa de Lyner indignada com a agressividade alheia."
    },
    11211: {
        "text": "Se querem briga, serão atendidos.\nNós, da Tribo Teru, não nos acovardamos diante de gente como vocês.",
        "notes": "Guarda Teru desembainha a arma reivindicando o orgulho de seu povo."
    },
    11212: {
        "text": "Gente, parem com isso!",
        "notes": "Lyner insiste no cessar-fogo entre as facções."
    },
    11213: {
        "text": "Não se meta!",
        "notes": "Guarda Teru avisa o cavaleiro para não obstruir o dever de guarda."
    },
    11214: {
        "text": "Se vai entrar no meio,\na gente derruba você primeiro!",
        "notes": "Humano violento ameaça espancar Lyner caso ele não saia da frente."
    },
    11215: {
        "text": "Pode vir! Quero ver tentar!",
        "notes": "Lyner desafia a intimidação inicial firmando os pés."
    },
    11216: {
        "text": "...",
        "notes": "Lyner silencia, lembrando-se das lições de paz aprendidas com Misha e Claire."
    },
    11217: {
        "text": "...Lyner?",
        "notes": "Misha percebe a súbita mudança na expressão do amigo."
    },
    11218: {
        "text": "O quê?!\nQual é a dele?!",
        "notes": "Agressor estupefato ao ver o rapaz baixar a guarda deliberadamente."
    },
    11219: {
        "text": "Este não é um problema\nque se resolve na violência.",
        "notes": "Lyner inicia seu discurso pacifista e humanitário."
    },
    11220: {
        "text": "A violência só atrai mais violência.\nMesmo que um dos lados vença aqui,\nvão acabar brigando de novo em outro lugar.",
        "notes": "Lyner expõe o ciclo destrutivo do ódio étnico e fratricida."
    },
    11221: {
        "text": "...O que você está falando?!",
        "notes": "Humano confuso diante da filosofia desarmante do cavaleiro."
    },
    11222: {
        "text": "Gente, vamos parar de brigar, por favor.",
        "notes": "Lyner roga pela cessação voluntária das armas."
    },
    11223: {
        "text": "Se conversarem direito,\ntenho certeza de que poderão se entender.",
        "notes": "Lyner defende o diálogo construtivo entre humanos e Teru."
    },
    11224: {
        "text": "Larga de ser ingênuo!\nA gente comeu o pão que o diabo amassou\nnas mãos deles por anos a fio!",
        "notes": "Humano expressa o ressentimento histórico acumulado das privações (苦汁をなめさせられてきた)."
    },
    11225: {
        "text": "Exatamente. É tarde demais para resolver qualquer coisa na conversa.",
        "notes": "Segundo humano apoia o pessimismo belicista."
    },
    11226: {
        "text": "Se continuar no caminho, vai levar porrada também!",
        "notes": "Agressor ameaça punir fisicamente o intermediador de paz."
    },
    11227: {
        "text": "Se isso aliviar a sua raiva,\npode me bater.",
        "notes": "Lyner oferece o próprio corpo em sacrifício para absorver a fúria dos homens (気が済むなら)."
    },
    11228: {
        "text": "!!",
        "notes": "Choque geral dos presentes diante da renúncia total à violência."
    },
    11229: {
        "text": "...",
        "notes": "Jack Hamilton observa com respeito e gravidade o amadurecimento moral do rapaz."
    },
    11230: {
        "text": "Eu não vou reagir!",
        "notes": "Lyner proclama seu voto de resistência pacífica intransigente."
    },
    11231: {
        "text": "Ficou louco?! Saia daí!",
        "notes": "Guarda Teru tenta dissuadi-lo de se deixar martirizar."
    },
    11232: {
        "text": "Se vocês querem tanto assim brigar, me batam!\nMas não encostem a mão em mais ninguém!",
        "notes": "Lyner protege a multidão e os guardas transformando-se em escudo vivo."
    },
    11233: {
        "text": "Lyner!\nPara com isso agora!",
        "notes": "Misha implora em desespero ao ver o amigo de infância sendo agredido."
    },
    11234: {
        "text": "Eu tô bem.\nVamos, bate mais!\nNão era derrubar quem entrasse no meio que vocês queriam?!",
        "notes": "Lyner desafia a consciência moral dos agressores suportando os golpes."
    },
    11235: {
        "text": "Esse cara...\né completamente maluco...",
        "notes": "Humano agressor recua perturbado e constrangido pela falta de ódio de Lyner."
    },
    11236: {
        "text": "Ficar aí levando socos sem nem tentar reagir...\nPor que faria isso?!",
        "notes": "Guarda Teru questiona atônito a lógica de compaixão daquele humano."
    },
    11237: {
        "text": "Pessoas brigando umas com as outras é um absurdo... Eu não luto sem um motivo justo.",
        "notes": "Lyner sintetiza sua moral de cavaleiro: a força existe para defender, nunca para agredir."
    },
    11238: {
        "text": "Que droga, perdi até a vontade...\nEu tô indo embora.\nVou esperar a tempestade passar.",
        "notes": "Agressor perde a sanha assassina, envergonhado por sua própria covardia."
    },
    11239: {
        "text": "Ficou um clima esquisito aqui...\nAcho melhor eu voltar outra hora...",
        "notes": "O grupo de insurgentes dispersa-se desarmado pela postura de Lyner."
    },
    11240: {
        "text": "Lyner! Por que você...",
        "notes": "Misha corre até Lyner com os olhos cheios de lágrimas."
    },
    11241: {
        "text": "Hehe... Viu só?\nDesta vez eu não espanquei ninguém.",
        "notes": "Lyner sorri machucado, orgulhoso de ter honrado a promessa de não ferir ninguém."
    },
    11242: {
        "text": "É tudo culpa minha...\nEu falei aquelas coisas no parque e aí...",
        "notes": "Misha chora culpando-se pelo sofrimento físico imposto a Lyner."
    },
    11243: {
        "text": "Lyner.\nPara você, varrer todo mundo na porrada não teria custado nada.",
        "notes": "Jack atesta a superioridade bélica de Lyner que optou conscientemente pelo perdão."
    },
    11244: {
        "text": "Pois é.\nMas o que a gente ganharia fazendo isso?",
        "notes": "Lyner reflete com maturidade serena sobre a futilidade da violência."
    },
    11245: {
        "text": "A Misha e a Senhorita Claire me ensinaram:\na violência não gera nada de bom.",
        "notes": "Lyner reverencia os valores transmitidos pelas mulheres que o guiaram."
    },
    11246: {
        "text": "Mas resolver desse jeito é loucura!!",
        "notes": "Misha briga com ele em meio ao choro protetor (そんなやり方は)."
    },
    11247: {
        "text": "É, tem razão, foi mal.\nPrometo que só fiz isso desta vez.",
        "notes": "Lyner desculpa-se carinhosamente acalmando a amiga de infância."
    },
    11248: {
        "text": "Ainda deixei todo mundo preocupado...",
        "notes": "Lyner reconhece o peso de sua imprudência emocional sobre os parceiros."
    },
    11249: {
        "text": "Desculpe por ter batido em você antes...",
        "notes": "Guarda Teru aproxima-se comovido para prestar sinceras desculpas."
    },
    11250: {
        "text": "Ah, você é aquele de antes...\nNão esquenta, não.\nO importante é que ninguém se matou.",
        "notes": "Lyner acolhe as desculpas sem ressentimento, comemorando a preservação da vida."
    },
    11251: {
        "text": "No fundo... tenho certeza de que ninguém quer brigar.",
        "notes": "Lyner expressa sua fé na bondade intrínseca de todos os seres conscientes."
    },
    11252: {
        "text": "Seja humano ou Teru,\nisso não faz a menor diferença.",
        "notes": "Lyner desmantela o preconceito racial unificando os povos de Sol Ciel."
    },
    11253: {
        "text": "Você é um humano bem peculiar.",
        "notes": "Guarda Teru elogia o caráter ímpar do cavaleiro de Platina."
    },
    11254: {
        "text": "A propósito, está rolando um boato de que há uma passagem secreta para a Torre por aqui... Procede?",
        "notes": "Krusche retoma o foco pragmático da investigação da rota de escalada."
    },
    11255: {
        "text": "Olha, nunca ouvi falar de nada parecido...",
        "notes": "Guarda Teru responde com sinceridade descartando o rumor local."
    },
    11256: {
        "text": "Talvez seja melhor subirmos um pouco mais a pé para procurar.",
        "notes": "Jack sugere a exploração vertical das encostas superiores."
    },

    # --- Event/374.evd (11257 - 11283) ---
    11257: {
        "text": "Mas olha, com essa confusão toda,\nPlatina levou um baque dos grandes.",
        "notes": "Jack comenta os estragos severos causados à infraestrutura de Platina."
    },
    11258: {
        "text": "Nem me fale.\nEu tô caindo de cansaço já...",
        "notes": "Lyner expressa sua exaustão física e mental após os combates."
    },
    11259: {
        "text": "Mas quem diria que até a Senhora Shurelia se cansa às vezes, né?",
        "notes": "Aurica surpreende-se com a vulnerabilidade física da Deusa da Torre."
    },
    11260: {
        "text": "Mas é claro.\nEla é um ser vivo afinal.",
        "notes": "Lyner pontua com naturalidade a humanidade biológica de Shurelia."
    },
    11261: {
        "text": "Então ela é viva mesmo?\nEu achava de verdade que ela era um robô.",
        "notes": "Aurica confessa sua crença cândida e inocente de que Shurelia era um autômato mecânico."
    },
    11262: {
        "text": "...Um robô?!\nBom, agora que você tocou no assunto,\naté que dá essa impressão...",
        "notes": "Lyner diverte-se admitindo que a aura etérea e rígida da Deusa lembrava uma máquina."
    },
    11263: {
        "text": "O que será que ela é de verdade, hein...?",
        "notes": "Lyner questiona a verdadeira natureza ontológica das Reyvateils Origin."
    },
    11264: {
        "text": "...",
        "notes": "Shurelia isola-se em um recanto contemplativo, recuperando suas forças."
    },
    11265: {
        "text": "Senhora Shurelia.\nFicar sozinha em um lugar como este é perigoso, sabia?",
        "notes": "Ayatane surge das sombras interpelando a guardiã com falsa solicitude."
    },
    11266: {
        "text": "Ayatane?!\nNão deveria haver meio algum de chegar até aqui. Como você...?!",
        "notes": "Shurelia alarma-se com a presença inexplicável de Ayatane naquela área restrita."
    },
    11267: {
        "text": "Se agora mesmo os vírus... ou a Mir\natacassem a senhora,\no que faria?",
        "notes": "Ayatane insinua a fraqueza momentânea da divindade invocando a ameaça de Mir."
    },
    11268: {
        "text": "Do jeito que a senhora está agora,\nnão teria a menor condição de enfrentá-los.",
        "notes": "Ayatane aponta impiedosamente o esgotamento do poder fônico de Shurelia."
    },
    11269: {
        "text": "!! Como é que você sabe disso...?!",
        "notes": "Shurelia sobressalta-se ao perceber que seu segredo biológico foi desvendado."
    },
    11270: {
        "text": "Ora, porque eu velo pela Senhora Shurelia o tempo todo.\nÉ natural que eu perceba pelo menos isso.",
        "notes": "Ayatane disfarça suas intenções sob o pretexto de devoção protetora perpétua."
    },
    11271: {
        "text": "Você não é um simples ser humano!\nQuem é você afinal?!",
        "notes": "Shurelia confronta a anomalia existencial do cavaleiro."
    },
    11272: {
        "text": "Que deselegância...\nEu não fiz nada que mereça tantas suspeitas, fiz?",
        "notes": "Ayatane adota postura de fingida ofensa e ironia cortês."
    },
    11273: {
        "text": "Sou apenas um guerreiro tímido e puro de coração,\nque não queria se afastar da senhora nem por um único instante.",
        "notes": "Fidelidade absoluta ao original japonês: Ayatane ironiza chamando-se de guerreiro puro e tímido."
    },
    11274: {
        "text": "Basta de brincadeiras!\nSe não disser a verdade agora mesmo...\neu vou atacar!",
        "notes": "Shurelia assume postura de combate exigindo a revelação da identidade dele."
    },
    11275: {
        "text": "Que crueldade...\nE olhe que gostei tanto da senhora por todo esse tempo.",
        "notes": "Ayatane lamenta com cinismo venenoso o carinho que fingiu nutrir por ela."
    },
    11276: {
        "text": "Mas, se esse é o seu desejo...\nnão me resta escolha.\nEu sou... ISTO AQUI!!",
        "notes": "Ayatane revela sua verdadeira forma como vírus supremo criado por Mir."
    },
    11277: {
        "text": "Nããão!!",
        "notes": "Grito de pavor e desespero dilacerante de Shurelia ante a abominação."
    },
    11278: {
        "text": "Senhor Lyner, é uma calamidade!\nUma horda gigantesca de vírus está brotando do Altar dos Apóstolos!",
        "notes": "Cavaleiro mensageiro corre em pânico relatando a erupção viral no santuário sagrado."
    },
    11279: {
        "text": "O Comandante-Geral Leard e a Ordem dos Cavaleiros marcharam para o Altar dos Apóstolos há pouco, mas perdemos todo o contato...",
        "notes": "O mensageiro informa o isolamento trágico das forças armadas de Platina."
    },
    11280: {
        "text": "Como é que é?!...\nMeu pai?!",
        "notes": "Lyner desespera-se ao saber que seu pai está na linha de frente do desastre."
    },
    11281: {
        "text": "É grave, Lyner!\nO lado de fora da cidade está infestado de guardiões!",
        "notes": "Comandante Radolf chega trazendo o relatório do cerco externo por autômatos corrompidos."
    },
    11282: {
        "text": "Droga, lá fora também...?! De qualquer forma, vamos voando para o Altar dos Apóstolos!",
        "notes": "Lyner conclama o grupo para marchar em socorro de Platina e de seu pai."
    },
    11283: {
        "text": "Radolf uniu-se ao grupo!",
        "notes": "Notificação canônica de sistema para o recrutamento do Comandante Radolf."
    }
}

with open("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_047_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

dialogues_out = []
curated_lines_out = []

for d in input_data["dialogues"]:
    d_id = d["id"]
    if d_id not in curated_map:
        raise ValueError(f"ID {d_id} ausente no mapeamento!")
    
    cur_info = curated_map[d_id]
    cur_text = cur_info["text"]
    notes = cur_info["notes"]
    
    entry = {
        "id": d_id,
        "event_file": d.get("event_file", ""),
        "speaker": d.get("speaker", ""),
        "speaker_id": d.get("speaker_id", 0),
        "original_jp": d.get("original_jp", ""),
        "original_en": d.get("original_en", ""),
        "curated_ptbr": cur_text,
        "final_ptbr": cur_text,
        "texto_ptbr_curado": cur_text,
        "custom_text": cur_text,
        "review_status": "approved",
        "reviewed": True,
        "notes": notes,
        "curation_notes": notes
    }
    dialogues_out.append(entry)
    curated_lines_out.append(entry)

# Monta estrutura completa do output
output_data = {
    "block_id": "BLK_EVD_047",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(dialogues_out),
    "dialogues": dialogues_out,
    "curated_lines": curated_lines_out,
    "glossary_updates": [
        {
            "term_en": "Kyle Clancy",
            "term_jp": "カイエル・クランシー",
            "term_ptbr": "Kyle Clancy",
            "category": "Personagem / Lore"
        },
        {
            "term_en": "ELMA",
            "term_jp": "エルマ",
            "term_ptbr": "ELMA",
            "category": "Guardião / Lore"
        },
        {
            "term_en": "Symphonic Plug",
            "term_jp": "導力プラグ",
            "term_ptbr": "Plug Sinfônico",
            "category": "Tecnologia / Lore"
        },
        {
            "term_en": "A7 Dividing Gate",
            "term_jp": "A7隔壁ゲート",
            "term_ptbr": "Portão de Antepara A7",
            "category": "Localização / Estrutura"
        }
    ],
    "new_terms": {
        "Kyle Clancy": {
            "pt": "Kyle Clancy",
            "category": "Personagem / Lore",
            "note": "カイエル・クランシー. Cientista de Platina corrompido que se tornou o Bispo Falss e aliou-se secretamente a Bourd e à Tenba."
        },
        "ELMA": {
            "pt": "ELMA",
            "category": "Guardião / Lore",
            "note": "エルマ. Guardião ancestral de base branca esculpido por Shurelia para defesa de Platina e dos santuários da Torre."
        },
        "Symphonic Plug": {
            "pt": "Plug Sinfônico",
            "category": "Tecnologia / Lore",
            "note": "導力プラグ. Conectores e reatores de alta densidade fônica que alimentam os santuários e anteparas de Platina."
        },
        "A7 Dividing Gate": {
            "pt": "Portão de Antepara A7",
            "category": "Localização / Estrutura",
            "note": "A7隔壁ゲート. Comporta de segurança blindada para isolamento de setores superiores da Torre Ar tonelico."
        }
    },
    "scene_handoff_final": {
        "resumo_dramatico": "O bloco BLK_EVD_047 articula cinco momentos narrativos de imensa tensão dramática, comédia de costumes e revelações cruciais da trama: (1) O prólogo/flashback canônico da partida de Platina, no qual Shurelia, Lyner e Ayatane confrontam um vírus que mimetizou o guardião ancestral ELMA através da invasão do Campo Binário. Ayatane isola o Plug Sinfônico com o comando Hymmnos '#0Was i ga exec bansh A7 al noes!', e Lyner voluntaria-se heroicmente para voar na aeronave sagrada de Gather rumo às Asas de Horus em busca do Cristal Hymmnos Purger, recebendo de Shurelia o Broche Hymmnos antes de ser abatido na barreira de plasma. (2) Uma intimista e bem-humorada conversa noturna de acampamento entre Krusche e Lyner, onde a engenheira abre o coração sobre seu antigo relacionamento com Luke, explicando que aprendeu mecânica apenas para entrar no campo de visão dele e que costumava usar vestidos e cabelos longos; Krusche prega uma peça em Lyner pedindo para namorarem, deixando-o em choque até rir da total falta de imunidade romântica do cavaleiro. (3) A retrospectiva trágica de uma batalha herética em Platina sob as bênçãos do Trio de Elemia, culminando na sinistra ressurreição e retorno anunciado de Kyle Clancy, acompanhada de um presságio sinistro no presente quando o cadarço da bota de Lyner se arrebenta. (4) Diante da fenda de acesso à Torre no Mundo Inferior, uma turba humana furiosa e guardas da Tribo Teru entram em confronto violento; Lyner atua como escudo humano, recusando-se a revidar os socos e proclamando que a violência só atrai violência, desarmando moralmente os insurgentes e conquistando o respeito dos Teru. (5) Por fim, no rescaldo dos combates em Platina, enquanto Lyner e Aurica brincam sobre Shurelia parecer um robô, a Deusa é encurralada sozinha por Ayatane; o jovem cavaleiro desfaz sua máscara de pureza e revela-se cinicamente como uma forma de vida viral suprema gerada por Mir, desencadeando um grito de pavor em Shurelia enquanto o Altar dos Apóstolos é tomado por vírus e Radolf une-se a Lyner em marcha desesperada.",
        "decisoes_terminologicas": {
            "ELMA": "エルマ (guardião original criado por Shurelia)",
            "Plug Sinfônico": "導力プラグ (reator/conector fônico isolado emergencialmente)",
            "Portão de Antepara A7": "A7隔壁ゲート (comporta de contenção blindada)",
            "Cristal Hymmnos Purger": "ヒュムネクリスタル・パージャ (cristal sagrado purificador)",
            "Asas de Horus": "ホルスの翼 (região do Mundo Inferior onde o Purger foi consagrado)",
            "Broche Hymmnos": "ヒュムネブローチ (pingente concedido a Lyner com os dados do Purger)",
            "Kyle Clancy": "カイエル・クランシー (identidade original do cientista de Platina / Falss)",
            "Altar dos Apóstolos": "使徒の祭壇 (santuário invadido pelas hordas virais)"
        },
        "alertas_para_proximo_bloco": "A revelação chocante da verdadeira identidade viral de Ayatane como criatura de Mir deixa Shurelia em perigo extremo, enquanto Leard e os Cavaleiros enfrentam o cerco viral no Altar dos Apóstolos com Radolf e Lyner acorrendo em socorro."
    },
    "highlights": [
        "Prólogo canônico de Platina: confronto contra o mímico do guardião ELMA, selamento fônico por Ayatane via Hymmnos (#0Was i ga exec bansh A7 al noes!) e juramento heroico de Lyner rumo às Asas de Horus portando o [Broche Hymmnos].",
        "Confissões de Krusche no acampamento: passado doloroso com Luke, a motivação amorosa para se tornar engenheira, a defesa cômica de sua feminilidade (vestidos e cabelos compridos) e o falso pedido de namoro que deixa Lyner desconcertado.",
        "Retrospectiva de Kyle Clancy e mau agouro: aparição sombria de Kyle Clancy diante de Shurelia e Leard, conectada ao rompimento premonitório do cadarço da bota de Lyner.",
        "Resistência pacifista heroica nos portões da Torre: Lyner oferece o próprio corpo aos golpes dos revoltosos humanos para proteger os guardas Teru, provando que a coragem reside em não revidar a violência.",
        "Clímax dramático de Platina: desmascaramento aterrador de Ayatane diante de Shurelia como forma de vida viral leal a Mir, seguido pelo alerta de emergência e recrutamento do Comandante Radolf rumo ao Altar dos Apóstolos."
    ]
}

output_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_047_output.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Gerado com sucesso: {output_path} ({len(dialogues_out)} falas).")

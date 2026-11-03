# -*- coding: utf-8 -*-
"""
build_and_validate_088.py - Constrói e valida BLK_EVD_088_output.json
"""
import sys
import json
import re
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Mapeamento completo das 185 falas com curadoria profunda
CURATED_DATA = {
    # === Event/888.evd (19808 - 19859) ===
    19808: {
        "curated_ptbr": "Quem vai querer a famosa Bala de Gato do Beco Vagalume?",
        "notes": "Spica promovendo a Bala de Gato (Kitty Candy) no Beco Vagalume (Firefly Alley)."
    },
    19809: {
        "curated_ptbr": "Spica!",
        "notes": "Misha cumprimentando a amiga comerciante."
    },
    19810: {
        "curated_ptbr": "Ora, se não é a Misha!\nComo vai você~?",
        "notes": "Spica reconhecendo Misha em tom caloroso e dengoso."
    },
    19811: {
        "curated_ptbr": "Spica, quanto tempo!",
        "notes": "Cumprimento afetuoso e casual de Lyner."
    },
    19812: {
        "curated_ptbr": "Você também parece ótimo, Lyner.\nUltimamente você quase não vem me ver...\nFiquei com saudades, sabia?",
        "notes": "Spica demonstrando afeto manhoso por Lyner."
    },
    19813: {
        "curated_ptbr": "Desculpe...\nAndei bem ocupada ultimamente...",
        "notes": "Misha pedindo desculpas; correção crítica de gênero (ocupada, feminino)."
    },
    19814: {
        "curated_ptbr": "Ora, só de vocês aparecerem por aqui de vez em quando\neu já fico muito feliz.",
        "notes": "Spica acolhendo os amigos."
    },
    19815: {
        "curated_ptbr": "O que traz vocês por aqui hoje?",
        "notes": "Spica perguntando o motivo da visita."
    },
    19816: {
        "curated_ptbr": "Nada de especial.\nEstávamos passando por perto e resolvemos dar um oi.",
        "notes": "Misha explicando que foi apenas uma visita casual."
    },
    19817: {
        "curated_ptbr": "É mesmo?... Ué?\nLyner, você está carregando algo bem curioso aí...",
        "notes": "Spica notando o item peculiar que Lyner carrega."
    },
    19818: {
        "curated_ptbr": "Ah... isto aqui?\nÉ uma bomba chamada Pipocabomba.",
        "notes": "Lyner apresentando a Pipocabomba (Popcorn Bomb), termo canônico de Grathmeld."
    },
    19819: {
        "curated_ptbr": "Embora eu ache que chamar isso só de «bomba»\nnão faça jus ao estrago...",
        "notes": "Misha ironizando o poder destrutivo da Pipocabomba."
    },
    19820: {
        "curated_ptbr": "Quer dizer que é uma bomba poderosa?",
        "notes": "Spica interessada no poder do artefato."
    },
    19821: {
        "curated_ptbr": "Além de dano físico, ela também causa dano elemental.\nÉ superpotente!",
        "notes": "Misha detalhando as propriedades ofensivas da Pipocabomba."
    },
    19822: {
        "curated_ptbr": "Nossa, que maravilha!\nVocê não passaria isso para mim?",
        "notes": "Spica cobiçando a bomba."
    },
    19823: {
        "curated_ptbr": "Por que você iria querer uma coisa dessas?\nÉ uma bomba, sabia?",
        "notes": "Lyner perplexo com o pedido de Spica."
    },
    19824: {
        "curated_ptbr": "Ela é potente de verdade!\nSe detonar, vai ser um perigo sem tamanho!",
        "notes": "Misha alertando sobre o risco de explosão."
    },
    19825: {
        "curated_ptbr": "É exatamente por isso que eu quero...\nCom ela, meu grande sonho pode se realizar um pouco mais rápido...",
        "notes": "Spica revelando suas ambições misteriosas ligadas a explosivos."
    },
    19826: {
        "curated_ptbr": "E-eu não sei o que você está tramando,\nmas é perigoso demais, então nada feito!",
        "notes": "Misha barrando a entrega da bomba."
    },
    19827: {
        "curated_ptbr": "Poxa, que pena...\nE eu aqui querendo de verdade...",
        "notes": "Spica fazendo bico desapontada."
    },
    19828: {
        "curated_ptbr": "Sabe, a Spica é uma pessoa bem misteriosa...\nEla tem Grathnodes incríveis e vive cobiçando coisas estranhas.",
        "notes": "Lyner ponderando sobre a natureza enigmática de Spica."
    },
    19829: {
        "curated_ptbr": "Em condições normais, só para juntar Cristais Grathnode\ncomo aqueles já daria um trabalho danado, não é?",
        "notes": "Lyner questionando a raridade dos cristais que Spica comercializa."
    },
    19830: {
        "curated_ptbr": "Hmm... Bem, já que são vocês,\ntalvez eu possa revelar um pedacinho do meu segredo.",
        "notes": "Spica decidindo compartilhar parte de sua rede de contatos."
    },
    19831: {
        "curated_ptbr": "A verdade é que fiz amizade com uma garota\nque tem um monte de Grathnodes. Ela que me repassa.",
        "notes": "Spica aludindo a Claire, a garota colecionadora de itens e cristais."
    },
    19832: {
        "curated_ptbr": "...Uma garota que tem\num monte de Grathnodes?",
        "notes": "Misha intrigada com a menção da fornecedora misteriosa."
    },
    19833: {
        "curated_ptbr": "Não são só Grathnodes...\nEla também junta uma quantidade absurda de itens!",
        "notes": "Spica descrevendo os estoques de Claire."
    },
    19834: {
        "curated_ptbr": "Aí, quando sobram itens repetidos,\nela me repassa tudo.",
        "notes": "Spica explicando o fluxo de mercadorias excedentes."
    },
    19835: {
        "curated_ptbr": "Mas o que você vende não é o tipo de mercadoria\nque se consegue tão fácil assim, não acha?",
        "notes": "Lyner apontando o alto valor dos itens de Spica."
    },
    19836: {
        "curated_ptbr": "É claro que ela não me passa nada de graça.\nMas vale cada centavo.",
        "notes": "Spica explicando que paga pelos itens (roha = gratuito); corrige o achatamento da NISA."
    },
    19837: {
        "curated_ptbr": "Pelo visto você investe um bom capital nisso.",
        "notes": "Misha comentando sobre o investimento financeiro necessário."
    },
    19838: {
        "curated_ptbr": "Os detalhes são segredo do negócio!\nMas digamos que é uma parceria vantajosa para ambas.",
        "notes": "Spica guardando seus trunfos comerciais."
    },
    19839: {
        "curated_ptbr": "Hum... Mas você disse que faz tudo pelo seu sonho...\nSerá que é um sonho assim tão arriscado?",
        "notes": "Misha desconfiada sobre as intenções de Spica."
    },
    19840: {
        "curated_ptbr": "Hmm... Se for parar para pensar,\nacho que pode ser arriscado, sim...",
        "notes": "Spica alimentando o suspense."
    },
    19841: {
        "curated_ptbr": "Por exemplo... se for com o Lyner,\neu até que não acharia nada mau fazer «aquilo»...",
        "notes": "Spica provocando Lyner com segundas intenções cômicas."
    },
    19842: {
        "curated_ptbr": "Hããã?!",
        "notes": "Lyner em choque com o flerte repentino."
    },
    19843: {
        "curated_ptbr": "E-ei, Spica!\nO que você está pensando?!",
        "notes": "Misha ciumenta reagindo à provocação."
    },
    19844: {
        "curated_ptbr": "Ufufu, não se preocupe...\nEu não faria nada arriscado a ponto de virar inimiga da Misha.",
        "notes": "Spica rindo da reação de Misha."
    },
    19845: {
        "curated_ptbr": "Opa, alto lá!",
        "notes": "Jack se intrometendo espalhafatoso."
    },
    19846: {
        "curated_ptbr": "Se for para ser assim, eu não sou uma opção\nmuito melhor que o Lyner?!",
        "notes": "Jack oferecendo-se galanteador."
    },
    19847: {
        "curated_ptbr": "Lá vem esse sujeito de novo...",
        "notes": "Krusche bufando com o comportamento de Jack."
    },
    19848: {
        "curated_ptbr": "Sinto muito, mas perdeu a viagem.\nNão tenho o menor interesse em homens mais velhos.",
        "notes": "Spica cortando as asas de Jack sem piedade."
    },
    19849: {
        "curated_ptbr": "Garoto bom tem que ser novinho!",
        "notes": "Spica expondo sua preferência explícita por rapazes mais novos."
    },
    19850: {
        "curated_ptbr": "Vinte e poucos anos\nnão serve para você?!",
        "notes": "Jack indignado com a rejeição etária."
    },
    19851: {
        "curated_ptbr": "Hã? Vinte e poucos anos?!",
        "notes": "Lyner surpreso com a idade revelada de Jack."
    },
    19852: {
        "curated_ptbr": "Mentira?!",
        "notes": "Misha chocada por Jack ser tão jovem."
    },
    19853: {
        "curated_ptbr": "Eu jurava que você já estava beirando os trinta!",
        "notes": "Krusche tirando sarro da cara de acabado de Jack."
    },
    19854: {
        "curated_ptbr": "Suas ingratas... Quer dizer, até você, Misha?!",
        "notes": "Jack magoado com a humilhação coletiva."
    },
    19855: {
        "curated_ptbr": "...Até me surpreendeu um pouco, mas passo.\nNão basta ser mais jovem, tem que ter encanto.",
        "notes": "Spica mantendo a recusa impassível."
    },
    19856: {
        "curated_ptbr": "Gaaah!",
        "notes": "Jack atingido em cheio no orgulho."
    },
    19857: {
        "curated_ptbr": "Chega, chega de palhaçada!\nAté mais, Spica, a gente se vê.",
        "notes": "Misha encerrando o bate-papo cômico."
    },
    19858: {
        "curated_ptbr": "Da próxima vez comprem alguma guloseima, tá bem~?",
        "notes": "Spica se despedindo com seu apelo comercial fofo."
    },
    19859: {
        "curated_ptbr": "...Descobrimos coisas até demais em tão pouco tempo...",
        "notes": "Lyner atordoado com o turbilhão de revelações cômicas."
    },

    # === Event/130.evd (19860 - 19921) ===
    19860: {
        "curated_ptbr": "Nossa... Este lugar desabou feio...",
        "notes": "Lyner contemplando a devastação das ruínas."
    },
    19861: {
        "curated_ptbr": "...!!",
        "notes": "Krusche avistando algo em meio aos escombros."
    },
    19862: {
        "curated_ptbr": "Lyner! Olha lá!",
        "notes": "Krusche apontando com urgência."
    },
    19863: {
        "curated_ptbr": "Hã?!",
        "notes": "Lyner reagindo ao aviso de Krusche."
    },
    19864: {
        "curated_ptbr": "Não tem dúvida...\nÉ o Cristal Hymmnos!",
        "notes": "Lyner identificando o Cristal Hymmnos (termo canônico: Cristal Hymmnos)."
    },
    19865: {
        "curated_ptbr": "Senhora Shurelia!\nFinalmente... até que enfim nós o encontramos!",
        "notes": "Lyner comemorando em júbilo filial para Shurelia."
    },
    19866: {
        "curated_ptbr": "...! Tem algo vindo aí!",
        "notes": "Radolf percebendo uma ameaça iminente."
    },
    19867: {
        "curated_ptbr": "Lyner!\nCuidado!",
        "notes": "Aurica gritando em pânico para alertar seu parceiro."
    },
    19868: {
        "curated_ptbr": "O quê?!",
        "notes": "Lyner pego de surpresa pelo ataque."
    },
    19869: {
        "curated_ptbr": "Urgh... Droga!",
        "notes": "Lyner sentindo o golpe do inimigo."
    },
    19870: {
        "curated_ptbr": "O que foi?!",
        "notes": "Aurica alarmada com o tremor violento."
    },
    19871: {
        "curated_ptbr": "Que droga...\nO impacto do combate está fazendo a sala desabar!",
        "notes": "Radolf avaliando a integridade estrutural em ruína rápida."
    },
    19872: {
        "curated_ptbr": "Aqui é perigoso demais!\nVamos evacuar já!",
        "notes": "Ordem de retirada militar de Radolf."
    },
    19873: {
        "curated_ptbr": "! Cadê o cristal?!",
        "notes": "Lyner descobrindo que o cristal desapareceu no caos."
    },
    19874: {
        "curated_ptbr": "Lyner!",
        "notes": "Radolf chamando Lyner para recuar."
    },
    19875: {
        "curated_ptbr": "O cristal sumiu!",
        "notes": "Lyner desesperado com a perda do artefato."
    },
    19876: {
        "curated_ptbr": "Se perdermos aquilo...\ntudo o que fiz para chegar até aqui terá sido em vão!",
        "notes": "Lyner verbalizando o peso de sua jornada e seu propósito heróico."
    },
    19877: {
        "curated_ptbr": "Achei!\nBem ali...",
        "notes": "Lyner avistando o cristal dependurado na fenda."
    },
    19878: {
        "curated_ptbr": "Lyner! Cuidado!",
        "notes": "Radolf vendo um desmoronamento cair sobre Lyner."
    },
    19879: {
        "curated_ptbr": "Aaaah!",
        "notes": "Vocalização genuína de susto feminino de Aurica."
    },
    19880: {
        "curated_ptbr": "O cristal...!",
        "notes": "Lyner vendo o cristal despencar para o abismo."
    },
    19881: {
        "curated_ptbr": "Lyner!\nDepressa!",
        "notes": "Radolf exigindo agilidade diante do colapso iminente."
    },
    19882: {
        "curated_ptbr": "Se continuarmos aqui,\nisso não aguenta nem mais dez segundos!",
        "notes": "Krusche calculando pragmaticamente o tempo de vida da estrutura."
    },
    19883: {
        "curated_ptbr": "Drogaaaa!",
        "notes": "Grito visceral de frustração de Lyner sendo forçado a fugir."
    },
    19884: {
        "curated_ptbr": "A câmara de antes... veio abaixo por completo...",
        "notes": "Radolf lamentando o desmoronamento total da câmara anterior."
    },
    19885: {
        "curated_ptbr": "De todo modo, aqui também não é seguro.\nTemos que sair logo destas ruínas.",
        "notes": "Radolf insistindo em deixar o local inóspito."
    },
    19886: {
        "curated_ptbr": "Pessoal!",
        "notes": "Lyner parando os companheiros antes da saída."
    },
    19887: {
        "curated_ptbr": "Desculpem, mas vão na frente.\nEu vou voltar para resgatar o Cristal Hymmnos.",
        "notes": "Lyner anunciando sua decisão temerária e heróica de voltar."
    },
    19888: {
        "curated_ptbr": "O quê?! Lyner!\nVocê tem noção do que está dizendo?!",
        "notes": "Radolf revoltado com a impulsividade perigosa do jovem cavaleiro."
    },
    19889: {
        "curated_ptbr": "Ele ainda pode ter ficado preso\nem algum ponto lá embaixo...",
        "notes": "Lyner buscando esperança na física da queda."
    },
    19890: {
        "curated_ptbr": "Lyner!\nNão jogue a sua vida fora dessa maneira!",
        "notes": "Radolf repreendendo o menosprezo à própria sobrevivência."
    },
    19891: {
        "curated_ptbr": "O que você sabe sobre isso?!",
        "notes": "Lyner explodindo sob a pressão do fardo que carrega."
    },
    19892: {
        "curated_ptbr": "Lyner?!",
        "notes": "Radolf chocado com a exasperação do rapaz."
    },
    19893: {
        "curated_ptbr": "!!",
        "notes": "Aurica assustada com a tensão entre os dois guerreiros."
    },
    19894: {
        "curated_ptbr": "...",
        "notes": "Krusche em silêncio grave observando a discussão."
    },
    19895: {
        "curated_ptbr": "Eu... arrisquei a própria vida\ne desci até aqui só por esse único cristal...",
        "notes": "Lyner desabafando sobre o preço cobrado pela jornada."
    },
    19896: {
        "curated_ptbr": "Carregando a esperança de tanta gente...\neu finalmente cheguei tão perto dele...",
        "notes": "Lyner expressando a responsabilidade sobre os ombros."
    },
    19897: {
        "curated_ptbr": "Eu não estou atrás dele\ncomo se fosse um simples «tesouro»!",
        "notes": "Lyner repudiando a ideia de que o cristal é mera pilhagem."
    },
    19898: {
        "curated_ptbr": "Todo mundo em Platina\nestá dependendo desse cristal...",
        "notes": "Lyner lembrando de sua terra natal na Torre."
    },
    19899: {
        "curated_ptbr": "Radolf... você também arriscaria a vida\nse fosse por uma missão da Igreja, não arriscaria?",
        "notes": "Lyner apelando para o código de honra cavalheiresco de Radolf."
    },
    19900: {
        "curated_ptbr": "...Sem dúvida.",
        "notes": "Radolf respondendo com a solenidade estoica de sua vocação militar."
    },
    19901: {
        "curated_ptbr": "Então para mim é a mesma coisa.",
        "notes": "Lyner traçando o paralelo irrefutável com seu dever sagrado."
    },
    19902: {
        "curated_ptbr": "...",
        "notes": "Radolf absorvendo as palavras do jovem cavaleiro."
    },
    19903: {
        "curated_ptbr": "...Desculpe por ter gritado.\nAté logo.",
        "notes": "Lyner se recompondo e pedindo desculpas antes de partir sozinho."
    },
    19904: {
        "curated_ptbr": "Ei, espere!",
        "notes": "Radolf interrompendo a despedida de Lyner."
    },
    19905: {
        "curated_ptbr": "Quem disse que vamos embora sem você?\nSe você vai ficar, eu fico também.",
        "notes": "Radolf declarando sua lealdade inabalável de companheiro de armas."
    },
    19906: {
        "curated_ptbr": "Nem pensar! Eu não posso me responsabilizar\npela sua vida, Radolf!",
        "notes": "Lyner recusando arrastar Radolf para a morte."
    },
    19907: {
        "curated_ptbr": "Do que você está falando?...\nEu também estou no meio de uma missão da Igreja, sabia?",
        "notes": "Radolf sorrindo com astúcia cavalheiresca."
    },
    19908: {
        "curated_ptbr": "A missão de «proteger o Lyner».",
        "notes": "Radolf definindo o juramento de proteção que o liga a Lyner."
    },
    19909: {
        "curated_ptbr": "E eu jamais abandonaria meu dever pelo caminho.",
        "notes": "Radolf reafirmando seu compromisso de guerreiro honrado."
    },
    19910: {
        "curated_ptbr": "Eu também vou com vocês até o fim.",
        "notes": "Krusche unindo-se à causa com determinação leal."
    },
    19911: {
        "curated_ptbr": "Quando estou com você, a própria palavra «morte»\nparece perder todo o sentido.",
        "notes": "Krusche confessando a energia inspiradora transmitida por Lyner."
    },
    19912: {
        "curated_ptbr": "A vontade de viver fala muito mais alto, com certeza.\nPor isso consigo manter a calma mesmo numa hora dessas.",
        "notes": "Krusche explicando a força que mantém o grupo sereno na crise."
    },
    19913: {
        "curated_ptbr": "...Com licença...",
        "notes": "Aurica dando um passo à frente com timidez resoluta."
    },
    19914: {
        "curated_ptbr": "...Aurica...",
        "notes": "Lyner fitando sua parceira com carinho."
    },
    19915: {
        "curated_ptbr": "Eu também... vou proteger você, Lyner.",
        "notes": "Aurica fazendo seu juramento protetor e afetuoso."
    },
    19916: {
        "curated_ptbr": "Afinal de contas, eu sou a sua parceira.",
        "notes": "Aurica afirmando seu vínculo sagrado de Reyvateil parceira."
    },
    19917: {
        "curated_ptbr": "Eu sou... alguém de quem você precisa, não sou?",
        "notes": "Aurica buscando confirmação afetiva para suas inseguranças."
    },
    19918: {
        "curated_ptbr": "Sim, é claro que é.",
        "notes": "Lyner assegurando Aurica com firmeza e ternura imediata."
    },
    19919: {
        "curated_ptbr": "...",
        "notes": "Aurica reconfortada e radiante em silêncio."
    },
    19920: {
        "curated_ptbr": "Muito bem! Antes que tudo venha abaixo,\nvamos achar esse cristal e dar o fora!",
        "notes": "Radolf dando a ordem de ação em ritmo entusiasmado."
    },
    19921: {
        "curated_ptbr": "Gente... muito obrigado!",
        "notes": "Lyner transbordando gratidão sincera aos companheiros."
    },

    # === Event/470.evd (19922 - 19942) ===
    19922: {
        "curated_ptbr": "Pronto, conseguimos recuperar o cristal.",
        "notes": "Lyner aliviado com a posse segura do artefato resgatado."
    },
    19923: {
        "curated_ptbr": "Contudo, ainda temos muito trabalho pela frente...",
        "notes": "Radolf mantendo os pés no chão quanto aos desafios futuros."
    },
    19924: {
        "curated_ptbr": "Que tal irmos para a estalagem comer alguma coisa\nenquanto decidimos os próximos passos?",
        "notes": "Radolf propondo um descanso revigorante para planejar a rota."
    },
    19925: {
        "curated_ptbr": "...Só que primeiro precisamos fazer o download.",
        "notes": "Lyner lembrando do processo técnico-litúrgico de instalação do Cântico."
    },
    19926: {
        "curated_ptbr": "Eu canto... Essa canção...",
        "notes": "Aurica se prontificando voluntariamente para entoar o cântico sagrado."
    },
    19927: {
        "curated_ptbr": "É a única coisa que posso fazer agora...\nE além do mais, eu quero cantar.",
        "notes": "Aurica manifestando seu desejo íntimo de servir através do canto."
    },
    19928: {
        "curated_ptbr": "Combinado. Conto com você.\nEntão... vamos fazer o download na Grande Catedral de Platina.",
        "notes": "Lyner aceitando a oferta e definindo o local de instalação na cidade flutuante."
    },
    19929: {
        "curated_ptbr": "Lyner!!",
        "notes": "Misha chamando afobada ao avistar o grupo."
    },
    19930: {
        "curated_ptbr": "Misha!\nE o Jack também...?!",
        "notes": "Lyner surpreso com o retorno repentino dos dois companheiros."
    },
    19931: {
        "curated_ptbr": "...E aí.",
        "notes": "Jack um pouco sem jeito pelo sumiço repentino anterior."
    },
    19932: {
        "curated_ptbr": "...Lyner. Desculpe por aquele dia.\nEu recusei de repente e dei no pé...",
        "notes": "Jack pedindo desculpas honestas pelo abandono do grupo."
    },
    19933: {
        "curated_ptbr": "Lyner... você ainda pretende\nmesmo reviver a Senhora Shurelia?",
        "notes": "Jack sondando a determinação de Lyner com solenidade velada."
    },
    19934: {
        "curated_ptbr": "S-sim... com certeza.",
        "notes": "Lyner reafirmando sua fidelidade à Senhora Shurelia."
    },
    19935: {
        "curated_ptbr": "Nesse caso, antes de ir revivê-la,\npasse em Em Pheyna.",
        "notes": "Jack pedindo um desvio crucial até sua cidade natal (Em Pheyna)."
    },
    19936: {
        "curated_ptbr": "Tem uma coisa muito importante que você precisa ouvir.\nSó peço que escute e depois reconsidere a sua decisão.",
        "notes": "Jack apelando para que Lyner pondere sobre o destino do mundo."
    },
    19937: {
        "curated_ptbr": "...O que foi? Por que todo esse mistério?",
        "notes": "Lyner estranhando o suspense de Jack."
    },
    19938: {
        "curated_ptbr": "Isso não é o tipo de coisa que deva sair da minha boca.",
        "notes": "Jack explicando que a revelação deve vir dos anciãos Teru; corrige erro da NISA."
    },
    19939: {
        "curated_ptbr": "Além do mais... se eu contar, vou acabar misturando sentimentos pessoais de novo, que nem da outra vez...",
        "notes": "Jack admitindo sua fraqueza emocional diante do passado; conserta a aberração de gênero da NISA/PT prévio ('toda emocionada')."
    },
    19940: {
        "curated_ptbr": "Tudo bem.\nVamos até Em Pheyna.",
        "notes": "Lyner concordando em atender ao pedido de Jack."
    },
    19941: {
        "curated_ptbr": "Valeu.\nEu também vou junto com vocês.",
        "notes": "Jack agradecendo e se reintegrando ao grupo."
    },
    19942: {
        "curated_ptbr": "Jack entrou no grupo!\nMisha entrou no grupo!",
        "notes": "Notificação de sistema da reintegração dos membros à equipe."
    },

    # === Event/19.evd (19943 - 19992) ===
    19943: {
        "curated_ptbr": "Mas que encrenca...\nQuem diria que espadas não fariam nem cócegas neles...",
        "notes": "Jack desconcertado com a imunidade a lâminas dos monstros."
    },
    19944: {
        "curated_ptbr": "Pelo que deu para notar,\naquele monstro não sofre dano com ataques físicos normais.",
        "notes": "Jack deduzindo a resistência física do oponente."
    },
    19945: {
        "curated_ptbr": "Mas como a minha arma surtiu algum efeito,\ntalvez ele seja vulnerável a «ataques ígneos».",
        "notes": "Jack identificando a fraqueza elemental ao calor/fogo (炎打撃 = ataques ígneos)."
    },
    19946: {
        "curated_ptbr": "...Ataques ígneos?",
        "notes": "Lyner repetindo o termo tático."
    },
    19947: {
        "curated_ptbr": "Bolas de fogo, os tiros da minha arma,\nbombas... qualquer investida que gere calor.",
        "notes": "Jack exemplificando os tipos de dano ígneo."
    },
    19948: {
        "curated_ptbr": "Mas, só de olhar para você,\ndá para ver que não carrega nada desse tipo.",
        "notes": "Jack avaliando o arsenal limitado de Lyner."
    },
    19949: {
        "curated_ptbr": "É verdade...\nNão tenho nenhuma arma assim comigo.",
        "notes": "Lyner confirmando a falta de opções elementais."
    },
    19950: {
        "curated_ptbr": "Mas se eu atacar com toda a minha força e determinação,\nserá que não consigo derrotar o bicho?",
        "notes": "Lyner apelando ingenuamente para a força de vontade e raça juvenil."
    },
    19951: {
        "curated_ptbr": "Ai, meus sais... Você é idiota?!\nJá não falei? Não adianta insistir!",
        "notes": "Jack estupefato com a teimosia descabida de Lyner."
    },
    19952: {
        "curated_ptbr": "Mas a gente nunca vai ter certeza se não tentar!",
        "notes": "Lyner defendendo sua abordagem empírica teimosa."
    },
    19953: {
        "curated_ptbr": "Você acabou de tentar, seu tapado!",
        "notes": "Jack apontando o óbvio recente com indignação cômica."
    },
    19954: {
        "curated_ptbr": "Se você não serve para a luta,\né o mesmo que eu ir caçar aquela coisa sozinho!",
        "notes": "Jack reclamando da falta de utilidade do companheiro."
    },
    19955: {
        "curated_ptbr": "Você só vai me atrapalhar,\nentão vê se tira essa ideia da cabeça.",
        "notes": "Jack avisando sem rodeios que Lyner só vai empatar."
    },
    19956: {
        "curated_ptbr": "Não, mas calma...\nSe eu colocar mais garra ainda...!",
        "notes": "Lyner insistindo na garra shonen inconsequente."
    },
    19957: {
        "curated_ptbr": "Ah... quanta besteira.\nFoi mal, mas perdi a vontade de andar com você.",
        "notes": "Jack desistindo da parceria diante de tanta cabeça-dura."
    },
    19958: {
        "curated_ptbr": "E-ei!\nEspera um pouco!",
        "notes": "Lyner pedindo para Jack não ir embora."
    },
    19959: {
        "curated_ptbr": "...Pelo que andaram me dizendo,\nera para você ser bem mais esperto que isso...",
        "notes": "Jack resmungando consigo mesmo sobre a fama prévia de Lyner."
    },
    19960: {
        "curated_ptbr": "...Hã? Pelo que andaram te dizendo?!\nQuer dizer que alguém falou de mim para você?",
        "notes": "Lyner pescando o deslize revelador de Jack."
    },
    19961: {
        "curated_ptbr": "...! N-não, ouvi nada!\nNão ouvi absolutamente nada!",
        "notes": "Jack disfarçando o segredo com afobação culposa."
    },
    19962: {
        "curated_ptbr": "...?",
        "notes": "Lyner desconfiado e perplexo."
    },
    19963: {
        "curated_ptbr": "Seja como for, estou encrencado se não recuperar\na minha aeronave.",
        "notes": "Lyner retomando a urgência pragmática de sua missão."
    },
    19964: {
        "curated_ptbr": "Se na base da força bruta não dá,\nme ensine algum jeito em que eu possa ser útil!",
        "notes": "Lyner pedindo uma alternativa tática madura."
    },
    19965: {
        "curated_ptbr": "Já ouviu falar numa técnica\nchamada Grathmeld?",
        "notes": "Jack introduzindo o conceito central de síntese de Sol Ciel."
    },
    19966: {
        "curated_ptbr": "Se dominar essa arte,\nvai poder criar de tudo, de bombas a remédios.",
        "notes": "Jack resumindo a versatilidade alquímica do Grathmeld."
    },
    19967: {
        "curated_ptbr": "Beleza! É isso aí!",
        "notes": "Lyner abraçando a solução sem nem pensar duas vezes."
    },
    19968: {
        "curated_ptbr": "Ué, seu paspalho!\nPor acaso você sabe o que é Grathmeld?!",
        "notes": "Jack desconfiado da empolgação vazia de Lyner."
    },
    19969: {
        "curated_ptbr": "Não faço a menor ideia!",
        "notes": "Lyner admitindo com orgulho ingênuo que não sabe nada."
    },
    19970: {
        "curated_ptbr": "...Quê?! Olha aqui, garoto...\nIsso não é algo que se aprenda estalando os dedos!",
        "notes": "Jack dando bronca na ingenuidade de Lyner."
    },
    19971: {
        "curated_ptbr": "Mas eu preciso aprender de qualquer jeito!",
        "notes": "Lyner resoluto em sua determinação inabalável."
    },
    19972: {
        "curated_ptbr": "...",
        "notes": "Jack avaliando a insistência do rapaz."
    },
    19973: {
        "curated_ptbr": "Mas mesmo que queira...\neu não entendo o bastante para te ensinar nada...",
        "notes": "Jack admitindo suas próprias limitações pedagógicas."
    },
    19974: {
        "curated_ptbr": "Ah... Falando em Grathmeld,\no mestre Pochoma está na vila hoje, sabiam?",
        "notes": "Moradora local dando a dica providencial sobre a presença do mestre."
    },
    19975: {
        "curated_ptbr": "C-como é que é?!!!",
        "notes": "Jack atônito com a revelação da ilustre presença."
    },
    19976: {
        "curated_ptbr": "...Mestre Pochoma?",
        "notes": "Lyner estranhando o nome singular do renomado sábio."
    },
    19977: {
        "curated_ptbr": "Você não conhece nem o mestre Pochoma?!\nEle é um Grathmelder lendário!",
        "notes": "Jack exaltando o prestígio mundial do mestre artesão."
    },
    19978: {
        "curated_ptbr": "Dizem que qualquer um instruído por ele\nse tornou um renomado mestre da síntese!",
        "notes": "Jack narrando a lenda de eficácia docente de Pochoma."
    },
    19979: {
        "curated_ptbr": "É mesmo?!\nVamos lá falar com ele agora! Onde ele está?",
        "notes": "Lyner empolgado para iniciar o aprendizado imediatamente."
    },
    19980: {
        "curated_ptbr": "Pois então... Ele está no café\nconstruído no alto do pilar.",
        "notes": "Moradora local indicando a localização excêntrica da loja."
    },
    19981: {
        "curated_ptbr": "No alto do pilar?!\nTsc... Que trabalheira...\nLyner, vai lá você sozinho.",
        "notes": "Jack caindo na preguiça costumeira de mercenário."
    },
    19982: {
        "curated_ptbr": "Parece que ele se mudou para lá\ncom a neta recentemente.",
        "notes": "Moradora local acrescentando o detalhe familiar."
    },
    19983: {
        "curated_ptbr": "Ele insistiu que queria um lugar com boa vista\ne acabou abrindo a loja bem no topo do pilar...",
        "notes": "Moradora local explicando o capricho estético do estabelecimento."
    },
    19984: {
        "curated_ptbr": "Fico pensando se aquele negócio vai dar certo...\nNunca vou entender a cabeça dessas garotas da cidade.",
        "notes": "Moradora local com o ceticismo interiorano típico sobre jovens citadinas."
    },
    19985: {
        "curated_ptbr": "Opa, alto lá!\nEssa neta que você falou...",
        "notes": "Jack apurando os ouvidos ao sinal de mulher bonita."
    },
    19986: {
        "curated_ptbr": "Uma mocinha, sim. Em plena flor da idade.",
        "notes": "Moradora local confirmando a idade jovem e casadoira da moça."
    },
    19987: {
        "curated_ptbr": "Muito bem, Lyner!\nVamos para lá agora mesmo!",
        "notes": "Jack mudando radicalmente de postura em um piscar de olhos."
    },
    19988: {
        "curated_ptbr": "...Hã?\nVocê acabou de falar para eu ir sozinho...",
        "notes": "Lyner pasmo diante da hipocrisia cômica instantânea de Jack."
    },
    19989: {
        "curated_ptbr": "A neta você deixa por minha conta!\nVocê vai lá e aprende Grathmeld de cabo a rabo com o velho!",
        "notes": "Jack distribuindo as funções com descaramento canastrão impagável."
    },
    19990: {
        "curated_ptbr": "É-é mesmo?...",
        "notes": "Lyner aceitando a situação com resignação cómica."
    },
    19991: {
        "curated_ptbr": "O Mercado ao Ar Livre «Tower Guardian»\nagora está acessível!",
        "notes": "Notificação de sistema desbloqueando a área de comércio."
    },
    19992: {
        "curated_ptbr": "Você pode se deslocar para cada local\nutilizando o Mapa da Cidade.",
        "notes": "Instrução de navegação da interface de mapa."
    }
}

# Carrega input JSON original
input_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_088_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

dialogues_input = input_data["dialogues"]
print(f"Total lines in input: {len(dialogues_input)}")
assert len(dialogues_input) == len(CURATED_DATA), f"Mismatch: input has {len(dialogues_input)}, curated has {len(CURATED_DATA)}"

# Monta curated_lines com todos os sinônimos exigidos
curated_lines = []
for d in dialogues_input:
    item_id = d["id"]
    cur_info = CURATED_DATA[item_id]
    cur_text = cur_info["curated_ptbr"]
    note_text = cur_info["notes"]
    
    entry = {
        "id": item_id,
        "event_file": d["event_file"],
        "speaker_id": d["speaker_id"],
        "speaker": d["speaker"],
        "original_jp": d["original_jp"],
        "original_en": d["original_en"],
        "current_ptbr": d["current_ptbr"],
        "review_status": "approved",
        "ptbr_text": cur_text,
        "text_ptbr": cur_text,
        "curated_ptbr": cur_text,
        "final_ptbr": cur_text,
        "texto_ptbr_curado": cur_text,
        "custom_text": cur_text,
        "reviewed": True,
        "notes": note_text,
        "curation_notes": note_text,
        "curadoria_notes": note_text
    }
    curated_lines.append(entry)

# Monta o Scene Handoff
scene_handoff = {
    "last_scene_id": "Event/19.evd",
    "last_line_id": 19992,
    "resumo_dramatico": "O bloco BLK_EVD_088 abrange quatro sequências cruciais do enredo e do cotidiano de Sol Ciel: (1) Em Event/888.evd, Lyner e Misha visitam Spica em sua barraca no Beco Vagalume. Spica nota que Lyner carrega uma potente Pipocabomba (Popcorn Bomb) e tenta comprá-la para acelerar seu sonho misterioso. Misha veta a venda pelo perigo explosivo. Em seguida, Spica revela como consegue tantos Cristais Grathnode e itens raros: sua fornecedora é uma garota colecionadora compulsiva (Claire). Spica passa a flertar com Lyner, provocando o ciúme de Misha. Jack tenta se oferecer no lugar de Lyner, mas Spica o rejeita sumariamente afirmando só ter interesse em garotos jovens. Ao Jack protestar que está na faixa dos vinte e poucos anos, o grupo inteiro fica chocado por achar que ele já beirava os trinta, destruindo o ego do pistoleiro. (2) Em Event/130.evd, Lyner, Aurica, Radolf e Krusche localizam o Cristal Hymmnos nas ruínas antigas de Elemia no Silvaplate. Quando Lyner comemora para a Senhora Shurelia, a câmara é atacada e o impacto do combate faz a estrutura desabar. O cristal despenca no abismo. Radolf ordena a evacuação imediata, mas Lyner se recusa a fugir e decide voltar sozinho para resgatar o cristal, afirmando que sua vida nada vale se falhar em sua missão e que todo o povo de Platina depende dele, comparando sua determinação ao dever sagrado de Radolf com a Igreja. Tocado pela bravura moral do jovem, Radolf decide ficar ao lado dele, declarando que sua missão é «proteger Lyner». Krusche e Aurica juntam-se imediatamente, com Aurica selando seu vínculo como parceira indispensável de Lyner. (3) Em Event/470.evd, após recuperarem o cristal, o grupo planeja o download litúrgico. Aurica prontifica-se a entoar a canção na Grande Catedral de Platina. Misha e Jack reaparecem; Jack pede desculpas por tê-los abandonado e pede solenemente que, antes de reviverem a Senhora Shurelia, passem por Em Pheyna para ouvir uma verdade fundamental dos anciãos Teru. Lyner aceita e Jack e Misha reintegram-se ao grupo. (4) Em Event/19.evd, logo após o início da jornada em Karff, Lyner e Jack enfrentam monstros imunes a lâminas. Jack deduz que eles sofrem dano por «ataques ígneos» (calor/fogo) e conclui que Lyner não tem armas adequadas. Quando Lyner sugere vencer na base da pura força de vontade e raça, Jack perde a paciência e ameaça romper a parceria. Lyner pede uma alternativa e Jack menciona a arte do Grathmeld. Uma moradora local avisa que o lendário Mestre Pochoma está na aldeia, num café no alto do pilar. Jack desdenha da subida até saber que a neta do mestre é uma bela jovem; instantaneamente, Jack muda de ideia e arrasta Lyner, desbloqueando o Mercado ao Ar Livre «Tower Guardian».",
    "decisoes_terminologicas": {
        "Bala de Gato": "猫飴 (Kitty Candy - doce tradicional de Spica no Beco Vagalume)",
        "Beco Vagalume": "ほたる横丁 (Firefly Alley - distrito comercial de Karff)",
        "Pipocabomba": "ポプコーンボム (Popcorn Bomb - bomba de síntese com dano físico e elemental)",
        "Cristal Hymmnos": "ヒュムネクリスタル (Hymn Crystal - artefato musical que guarda os Cânticos ancestrais)",
        "Senhora Shurelia": "シュレリア様 (Lady Shurelia - tratamento reverente e afetuoso de Lyner)",
        "Em Pheyna": "イム・フェーナ (Em Pheyna - cidade sagrada da Tribo Teru no Silvaplate)",
        "Ataques Ígneos / Dano Ígneo": "炎打撃 (Honoo Dageki / Fire Attacks - dano térmico/fogo de armas de fogo, bombas e magias)",
        "Grathmeld": "グラスメルク (Grathmeld - arte de síntese alquímica sonora de Sol Ciel)",
        "Grathmelder": "メルク (Melder / Grathmelder - artesão praticante de Grathmeld)",
        "Mestre Pochoma": "ポチョマー先生 (Mr. Pochoma - venerável e renomado mestre artesão de Grathmeld)",
        "Tower Guardian": "タワーガーディアン (Tower Guardian - Mercado ao Ar Livre no pilar de Karff)"
    },
    "alertas_para_proximo_bloco": "Para os blocos seguintes (BLK_EVD_089 em diante), acompanhar a chegada a Em Pheyna, as revelações dramáticas da Tribo Teru sobre a história de Sol Ciel e o papel de Shurelia, bem como a confecção dos primeiros itens via Grathmeld com o Mestre Pochoma e sua neta."
}

# Monta as adições ao glossário
glossary_additions = {
    "Ataques Ígneos": {
        "pt": "Ataques Ígneos",
        "gender": "masculino",
        "number": "plural",
        "category": "Sistema de Batalha / Dano Elemental",
        "note": "炎打撃 (Honoo Dageki / Fire Attacks). Categoria de dano térmico gerado por armas de fogo, bombas de Grathmeld e magias de fogo, capaz de ferir monstros imunes a lâminas."
    },
    "Mestre Pochoma": {
        "pt": "Mestre Pochoma",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / NPC Lendário",
        "note": "ポチョマー先生 (Mr. Pochoma). Grathmelder lendário de renome mundial estabelecido no topo do pilar em Karff; mentor de grandes artesãos de Sol Ciel."
    },
    "Tower Guardian": {
        "pt": "Mercado ao Ar Livre «Tower Guardian»",
        "gender": "masculino",
        "number": "singular",
        "category": "Localização / Ponto de Interesse",
        "note": "青空市場『タワーガーディアン』 (Tower Guardian Outdoor Market). Feira e praça comercial localizada nos pilares de Karff."
    }
}

output_data = {
    "block_id": "BLK_EVD_088",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(curated_lines),
    "id_range": [19808, 19992],
    "stats": {
        "total_lines": len(curated_lines),
        "lines_rewritten": len(curated_lines),
        "lines_approved_as_is": 0,
        "new_terms_added": len(glossary_additions)
    },
    "curated_lines": curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": curated_lines,
    "scene_handoff": scene_handoff,
    "entries": curated_lines,
    "block_entries": curated_lines
}

# Valida deterministicamente cada linha
hard_gate_errors = 0
lint_warnings = 0

print("\n--- INICIANDO AUDITORIA DETERMINÍSTICA LINHA A LINHA ---")
for item in curated_lines:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    trad = item["curated_ptbr"]

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

    # Check for \r
    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contém retorno de carro \\r!")
        hard_gate_errors += 1

    # Check orphan line start with punctuation after \n
    parts = trad.split("\n")
    for line_part in parts[1:]:
        line_strip = line_part.strip()
        if line_strip.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Linha inicia com pontuação órfã após quebra: {line_part!r}")
            hard_gate_errors += 1
        if line_part.startswith("..."):
            print(f"[ERROR] ID {item_id}: Linha inicia com reticências após quebra: {line_part!r}")
            hard_gate_errors += 1

    # Check syntactic fracture before \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Fratura sintática antes de \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

print(f"\nResumo da Auditoria:")
print(f"Total de falas auditadas: {len(curated_lines)}")
print(f"Erros de Hard Gate: {hard_gate_errors}")
print(f"Avisos de Lint: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("\n[PERFEIÇÃO] 100% das 185 falas passaram em todas as travas sem nenhum erro ou aviso!")
    out_file = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_088_output.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"Arquivo gerado com sucesso: {out_file}")
else:
    print(f"\n[FALHA] Detectados {hard_gate_errors} erros e {lint_warnings} avisos. Corrija antes de gerar.")
    sys.exit(1)

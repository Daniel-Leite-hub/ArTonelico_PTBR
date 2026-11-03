# -*- coding: utf-8 -*-
import json
import sys
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_072_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_072_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    inp = json.load(f)

# Dicionário de traduções e notas
curated_data = {
    # Event/446.evd (16362 - 16404)
    16362: (
        "É a Krusche!\nSerá que ela tá encrencada com o pessoal da Tenba?!",
        "Lyner avista Krusche cercada por guardas e teme que ela esteja sofrendo represálias da corporação."
    ),
    16363: (
        "Temos que ir lá ajudar!",
        "Aurica reage prontamente com senso de urgência para socorrer a amiga mecânica."
    ),
    16364: (
        "Ei! Vocês aí!!",
        "Lyner brada para intimidar os guardas da Tenba, corrigindo o erro da NISA que traduziu 'お前ら' no singular."
    ),
    16365: (
        "Ué?! Lyner!\nHá quanto tempo!",
        "Krusche surpreende-se com a aparição súbita dos amigos em meio à sede da corporação."
    ),
    16366: (
        "Krusche! Você tá bem?!",
        "Lyner indaga com preocupação transparente pelo bem-estar da mecânica."
    ),
    16367: (
        "...Hã? Como assim?\nPor mim tá tudo ótimo... mas e você, Lyner, tá bem?",
        "Krusche estranha o alvoroço de Lyner, reagindo com sua habitual nonchalance."
    ),
    16368: (
        "Ué?... Mas é que...\nCom os guardas da Tenba cercando você...",
        "Lyner hesita desconcertado ao perceber que não se tratava de um ataque violento."
    ),
    16369: (
        "Ah, isso. Ninguém tava me atacando não.\nEu só tava numa reunião de alinhamento com eles.",
        "Krusche esclarece que se tratava de uma reunião com a equipe da Tenba (打ち合わせ)."
    ),
    16370: (
        "...Uma reunião?",
        "Lyner reage atônito à incompatibilidade entre a rebelde mecânica do Beco e a burocracia corporativa."
    ),
    16371: (
        "Na verdade, assim que voltei para o Beco Vagalume,\nfui recrutada pessoalmente pela Presidente Ayano.",
        "Krusche revela sua contratação executiva de prestígio pela própria chefe do Conglomerado Tenba."
    ),
    16372: (
        "Agora eu também sou engenheira da Tenba.\nHehehe.",
        "Krusche ostenta com orgulho travesso seu novo crachá corporativo, resgatando o risinho 'えへへ' suprimido na NISA."
    ),
    16373: (
        "...Tá falando sério?!",
        "Lyner fica de queixo caído diante da reviravolta profissional da amiga."
    ),
    16374: (
        "Mas que bom rever vocês!\nPor que não aproveitam e dão uma passada na sede?",
        "Krusche convida calorosamente a dupla para conhecer as instalações centrais da Tenba."
    ),
    16375: (
        "Caramba...\nÉ num lugar desses que você trabalha agora?",
        "Lyner fica impressionado com a magnitude e imponência tecnológica dos laboratórios corporativos."
    ),
    16376: (
        "Pois é. Mudou da água para o vinho\nse comparar com a minha velha oficina caindo aos pedaços.",
        "Krusche ironiza com nostalgia pragmática sua antiga oficina modesta (ボロ工房)."
    ),
    16377: (
        "Mas o que eu faço não mudou em nada:\ncontinuo pesquisando e projetando aeronaves.",
        "Krusche frisa que sua verdadeira paixão vocacional pela aviação permanece intocada."
    ),
    16378: (
        "Antes de cruzarmos a Blastline, foi sob o meu comando\nque aquela aeronave foi construída, lembra?",
        "Krusche recorda seu feito de liderança na travessia pioneira do plasma atmosférico da Blastline."
    ),
    16379: (
        "Parece que viram potencial em mim naquela época.",
        "Krusche constata que o sucesso de seu projeto experimental atraiu o radar dos caça-talentos da Tenba."
    ),
    16380: (
        "Construir uma nave que consiga voar até os confins deste mundo:\nesse é o meu trabalho agora.",
        "Krusche expõe a visão ambiciosa de seu projeto de aviação no Projeto Shoga."
    ),
    16381: (
        "E verba para pesquisa é o que não falta!",
        "Krusche comemora o financiamento corporativo abundante que a diretoria disponibilizou (資金も潤沢にあるしね)."
    ),
    16382: (
        "Entendi...\nVocê subiu mesmo na vida, Krusche. Meus parabéns.",
        "Lyner parabeniza a amiga com orgulho e afeto fraterno (ずいぶん出世したんだな)."
    ),
    16383: (
        "Valeu!",
        "Krusche agradece em tom descontraído e fraternal."
    ),
    16384: (
        "Lyner, temos que falar sobre aquele assunto!",
        "Aurica lembra Lyner do objetivo urgente que os levou até ali."
    ),
    16385: (
        "O quê? Que assunto?...\nNão me digam que vocês vão se casar?",
        "Krusche provoca o casal com seu sarcasmo bem-humorado habitual."
    ),
    16386: (
        "N-não é nada disso!!",
        "Aurica entra em pânico corada diante da insinuação embaraçosa (ち、違います!!)."
    ),
    16387: (
        "Na verdade...\né sobre a Senhora Shurelia...",
        "Lyner retoma a seriedade e revela o motivo da visita."
    ),
    16388: (
        "...A Senhora Shurelia?",
        "Krusche indaga surpresa com a menção à deusa guardiã."
    ),
    16389: (
        "Entendi... Então foi isso que aconteceu.",
        "Krusche processa com seriedade o relato sobre o colapso dos sistemas da Primeira Torre."
    ),
    16390: (
        "Mas fico bem mais aliviada\nem saber que ela não morreu de verdade.",
        "Krusche expressa alívio por saber que Shurelia está preservada em hibernação criogênica."
    ),
    16391: (
        "Eu também tava muito preocupada com ela...",
        "Krusche confessa sua aflição constante pelo destino da deusa."
    ),
    16392: (
        "Por isso... você não podia nos dar uma força, Krusche...?\nA procurar o [RE Nation].",
        "Lyner pede o auxílio técnico da engenheira para localizar o Cristal Hymmnos primordial."
    ),
    16393: (
        "...",
        "Krusche hesita em silêncio dividida entre o dever profissional e o apelo dos amigos."
    ),
    16394: (
        "...Vontade não me falta, mas no momento é impossível.",
        "Krusche lamenta não poder aceitar (そうしたいのは山々だけど)."
    ),
    16395: (
        "...Como?!\nÉ sério isso...?",
        "Lyner reage chocado com a recusa inesperada de Krusche."
    ),
    16396: (
        "O meu cargo atual é de suma importância aqui dentro.",
        "Krusche contextualiza a gravidade e o peso de suas responsabilidades na Tenba."
    ),
    16397: (
        "Este projeto é de escala monumental até para a Tenba...\nSe eu sair agora, vai desandar tudo.",
        "Krusche explica que o projeto aeronáutico depende inteiramente de sua liderança técnica."
    ),
    16398: (
        "Eu não posso...\nnão posso abandonar o meu posto.",
        "Krusche admite com pesar a impossibilidade de acompanhar a comitiva."
    ),
    16399: (
        "...Me perdoem.",
        "Krusche pede sinceras desculpas aos dois companheiros."
    ),
    16400: (
        "Não se preocupe. Tudo bem.",
        "Lyner compreende e acolhe com maturidade a posição profissional da amiga."
    ),
    16401: (
        "A gente chegou de repente jogando tudo em cima de você...\nDesculpe por colocar você nessa saia justa.",
        "Lyner assume a responsabilidade pelo pedido abrupto (困らせて済まなかったな)."
    ),
    16402: (
        "Imagina...\nEu que peço desculpas por não poder fazer nada...",
        "Krusche agradece a nobreza e a empatia fraterna de Lyner."
    ),
    16403: (
        "O acesso à [Sede da Tenba] foi liberado!",
        "Mensagem de sistema notificando desbloqueio de localização no mapa mundial."
    ),
    16404: (
        "É possível se deslocar até a Sede da Tenba pelo mapa da cidade.",
        "Instrução de navegação para acessar a sede corporativa pelo mapa urbano."
    ),

    # Event/178.evd (16405 - 16476)
    16405: (
        "Você é o jovem Lyner, certo?\nO Comandante Leard já me avisou da sua chegada.",
        "O operador da plataforma de Platina acolhe Lyner sob orientações prévias do Comandante Leard."
    ),
    16406: (
        "Disseram que você vai fazer o download de um Cristal Hymmnos!\nImpressionante, meu jovem!",
        "O operador entusiasma-se com a instalação de um Cristal Hymmnos ancestral na Torre."
    ),
    16407: (
        "...Download?",
        "Lyner estranha o jargão técnico da engenharia sonora da Primeira Torre."
    ),
    16408: (
        "Isso mesmo! É o termo que usamos quando\numa Reyvateil se sintoniza e se une a um cristal.",
        "O operador elucida o significado de download na cosmologia de Sol Ciel."
    ),
    16409: (
        "E então, em quem faremos o download do Cristal Hymmnos?",
        "O operador indaga qual das donzelas receberá a infusão do cântico ancestral."
    ),
    16410: (
        "Escolha uma Reyvateil que já conheça seu [Código Hymmnos].",
        "O operador instrui a seleção de uma parceira com seu Código Hymmnos desperto."
    ),
    16411: (
        "Aurica... posso confiar isso a você?",
        "Lyner propõe a tarefa com delicadeza e respeito à sensibilidade de Aurica."
    ),
    16412: (
        "Hã!?... Tem certeza de que quer...\nalguém como eu?",
        "Aurica expressa sua constante dúvida e modéstia dolorosa (あたし...なんかでいいの?)."
    ),
    16413: (
        "Sim. É exatamente por ser você, Aurica, que quero te pedir.\nVocê aceita...?",
        "Lyner valoriza a identidade de Aurica para fortalecê-la emocionalmente."
    ),
    16414: (
        "...Sim!",
        "Aurica aceita a honra com entusiasmo contido e gratidão."
    ),
    16415: (
        "Muito bem! Como temos um ritual a cumprir,\nvamos nos deslocar até o local apropriado.",
        "O operador convida a dupla a avançar para o átrio sagrado de Platina."
    ),
    16416: (
        "Nossa, quer dizer que esta praça\nfoi feita justamente para a Cerimônia de Download?",
        "Lyner admira a função sacra da arquitetura da plataforma."
    ),
    16417: (
        "Bem, é mais por tradição formal mesmo.",
        "O operador pontua que o espaço é sobretudo cerimonial (形式だけだけどね)."
    ),
    16418: (
        "Agora, façam exatamente o que eu instruir.",
        "O operador assume o protocolo do rito de inicialização."
    ),
    16419: (
        "Primeiro, fiquem um de frente para o outro.",
        "Posicionamento ritualístico exigido para alinhamento ressonante entre os parceiros."
    ),
    16420: (
        "Jovem Lyner, empunhe o cristal\ne erga-o diante da jovem Aurica.",
        "Instrução para a elevação do Cristal Hymmnos diante da cantora."
    ),
    16421: (
        "Muito bem, vamos começar.",
        "O operador dá o sinal para a deflagração da prece em Hymmnos."
    ),
    16422: (
        "#0Fou paks ra exec hymnos PAJA!",
        "Verso procedural sagrado em Hymmnos entoado pelo operador para inicializar a execução de Purger."
    ),
    16423: (
        "...!!\nI-isto é...!!",
        "Lyner é tomado de assombro com a emanação de luz e dados holográficos do cristal."
    ),
    16424: (
        "Jovem Lyner! Leia o texto que apareceu! Rápido!",
        "O operador comanda a leitura imediata dos versos de acesso projetados no ar."
    ),
    16425: (
        "C-certo!",
        "Lyner prontifica-se a vocalizar o texto ancestral."
    ),
    16426: (
        "#0Was yea ra chs hymnos yor...",
        "Verso procedural sagrado em Hymmnos entoado por Lyner estabelecendo a intenção de união lírica."
    ),
    16427: (
        "#0n chsee fwal fwal yor...",
        "Verso procedural sagrado em Hymmnos entoado por Lyner abrindo o fluxo melódico."
    ),
    16428: (
        "#0exec drone hymnos PAJA ",
        "Comando procedural sagrado em Hymmnos ativando o processo drone de Purger."
    ),
    16429: (
        "#0enter MULE TEIWAZ ARTONELICO.",
        "Invocação do Código Hymmnos sagrado de linhagem ancestral de Aurica."
    ),
    16430: (
        "...",
        "Aurica em silêncio de absorção mística e sintonização profunda com a melodia."
    ),
    16431: (
        "E-e então?! Como você tá?!",
        "Lyner indaga aflito pela integridade psíquica de Aurica."
    ),
    16432: (
        "...A melodia... Um cântico tá brotando lá do fundo da minha alma...",
        "Aurica sente a melodia de Purger florescer no núcleo de seu espírito."
    ),
    16433: (
        "Incrível...! Eu tô tecendo uma Canção...\nNunca senti algo assim na minha vida...",
        "Aurica se maravilha ao tecer sua primeira grande Magia da Canção de alta tecnologia."
    ),
    16434: (
        "Não é todo dia que se vivencia uma sensação dessas.\nAproveite cada segundo!",
        "O operador valida o êxtase lírico da jovem Reyvateil."
    ),
    16435: (
        "Pois bem, meu papel termina por aqui.\nAfinal, não tenho como saber que tipo de Canção nasceu aí dentro.",
        "O operador informa que sua atuação técnica se esgota com a conclusão do rito."
    ),
    16436: (
        "Para maiores detalhes, consultem o Comandante-Geral.",
        "O operador orienta o grupo a buscar Leard para orientações táticas sobre a canção."
    ),
    16437: (
        "Muito obrigado. Você nos ajudou bastante.",
        "Lyner agradece com civilidade o trabalho do operador."
    ),
    16438: (
        "Certo! Vamos voltar para a catedral.",
        "Lyner reúne o grupo para regressar ao templo de Platina."
    ),
    16439: (
        "Misha... posso confiar isso a você?",
        "Lyner consulta carinhosamente Misha na ramificação alternativa do evento."
    ),
    16440: (
        "Lyner...\nVocê quer mesmo confiar isso a mim...?",
        "Misha reage tocada e surpresa com a honra concedida pelo amigo."
    ),
    16441: (
        "Sim. É justamente por ser você que eu quero.\nPosso contar com você?",
        "Lyner reafirma sua lealdade incondicional a Misha."
    ),
    16442: (
        "Mas é claro!...\nEu tava esperando você me dizer isso há tanto tempo!",
        "Misha comemora com entusiasmo contagiante a escolha de Lyner."
    ),
    16443: (
        "Muito bem! Como temos um ritual a cumprir,\nvamos nos deslocar até o local apropriado.",
        "O operador conduz a comitiva para o centro cerimonial."
    ),
    16444: (
        "Nossa, quer dizer que esta praça\nfoi feita justamente para a Cerimônia de Download?",
        "Lyner observa a solenidade arquitetônica do local."
    ),
    16445: (
        "Bem, é mais por tradição formal mesmo.",
        "O operador reforça a natureza simbólica e tradicional do espaço."
    ),
    16446: (
        "Agora, façam exatamente o que eu instruir.",
        "O operador dita as instruções preliminares da sintonização."
    ),
    16447: (
        "Primeiro, fiquem um de frente para o outro.",
        "Posicionamento inicial dos parceiros."
    ),
    16448: (
        "Jovem Lyner, empunhe o cristal\ne erga-o diante da jovem Misha.",
        "Comando para expor o cristal à visão de Misha."
    ),
    16449: (
        "Muito bem, vamos começar.",
        "O operador deflagra a abertura do ritual."
    ),
    16450: (
        "#0Fou paks ra exec hymnos PAJA!",
        "Verso procedural sagrado em Hymmnos entoado pelo operador invocando a canção PAJA."
    ),
    16451: (
        "...!!\nI-isto é...!!",
        "Lyner sobressalta-se diante da projeção etérea do texto sagrado."
    ),
    16452: (
        "Jovem Lyner! Leia o texto que apareceu! Rápido!",
        "O operador exige a leitura instantânea dos versos de ativação."
    ),
    16453: (
        "C-certo!",
        "Lyner acata a ordem prontamente."
    ),
    16454: (
        "#0Was yea ra chs hymnos yor...",
        "Verso procedural sagrado em Hymmnos abrindo a conexão lírica entre Lyner e Misha."
    ),
    16455: (
        "#0En chsee fwal fwal yor...",
        "Verso procedural sagrado em Hymmnos expandindo as asas espirituais da canção."
    ),
    16456: (
        "#0exec drone hymnos PAJA ",
        "Comando procedural sagrado em Hymmnos ativando o fluxo drone de Purger."
    ),
    16457: (
        "#0enter MISYA FEHU EORIA ARTONELICO!",
        "Invocação do Código Hymmnos sagrado de linhagem Origin de Misha."
    ),
    16458: (
        "...",
        "Misha em silêncio sagrado absorvendo os dados acústicos de Purger."
    ),
    16459: (
        "E-e então?! Como você tá?!",
        "Lyner pergunta com afeto e preocupação pelo estado da parceira."
    ),
    16460: (
        "Mas o que é isso... Não pode ser...",
        "Misha reage desconcertada pelas lembranças remotas despertadas pelo cristal."
    ),
    16461: (
        "Uma sensação tão nostálgica...\nPor que será que as minhas lágrimas tão caindo...?",
        "Misha chora involuntariamente diante do eco emocional de tempos imemoriais."
    ),
    16462: (
        "Lyner... Isso é incrível!...\nMas por que será que me dá um aperto tão doce no peito...?",
        "Misha descreve a sensação agridoce e enternecedora provocada pela melodia ancestral (切ない)."
    ),
    16463: (
        "Não é todo dia que se vivencia uma sensação dessas.\nAproveite cada segundo!",
        "O operador valida o sentimento lírico singular vivido por Misha."
    ),
    16464: (
        "Pois bem, meu papel termina por aqui.\nAfinal, não tenho como saber que tipo de Canção nasceu aí dentro.",
        "O operador encerra sua contribuição no procedimento litúrgico."
    ),
    16465: (
        "Para maiores detalhes, consultem o Comandante-Geral.",
        "O operador encaminha o grupo de volta a Leard."
    ),
    16466: (
        "Muito obrigado. Você nos ajudou bastante.",
        "Lyner agradece cordialmente o auxílio prestado."
    ),
    16467: (
        "Certo! Vamos voltar para a catedral.",
        "Lyner conclama o retorno à Catedral de Platina."
    ),
    16468: (
        "Que nada, às ordens!\nApareçam por aqui sempre que precisarem.",
        "O operador despede-se demonstrando prontidão para novos rituais."
    ),
    16469: (
        "...Código Hymmnos!?...\nO que significa isso afinal?",
        "Lyner indaga com ingenuidade sobre o termo técnico na ramificação explicativa."
    ),
    16470: (
        "Você não sabe de nada mesmo, né, jovem Lyner?\nExatamente como o Comandante Leard comentou...",
        "O operador diverte-se com o desconhecimento de Lyner, confirmando os relatos de Leard."
    ),
    16471: (
        "...Aquele velho... Tinha que ficar falando demais de mim pelas costas...",
        "Lyner resmunga aborrecido com os comentários depreciativos do pai (親父のヤツ)."
    ),
    16472: (
        "O [Código Hymmnos] é como se fosse uma senha de identificação de uma Reyvateil.",
        "O operador esclarece que o Código Hymmnos funciona como credencial cifrada."
    ),
    16473: (
        "Para usar uma metáfora poética e lendária,\né o seu \"verdadeiro nome\", guardado a sete chaves.",
        "O operador recorre à tradição mística que define o código como o nome oculto da Reyvateil (真の名前)."
    ),
    16474: (
        "Mas pelo visto, você ainda não conhece o [Código Hymmnos] dela, né?",
        "O operador percebe que Lyner ainda não conquistou essa confidência."
    ),
    16475: (
        "Você precisa mergulhar e consultar o guardião da Cosmosfera dela.",
        "O operador prescreve o Mergulho mental como único meio de obter a chave."
    ),
    16476: (
        "Se ela tiver aberto o coração para você,\ncom certeza vai te revelar o [Código Hymmnos].",
        "O operador pontua que o desvelamento do código decorre do aprofundamento do afeto mútuo."
    ),

    # Event/743.evd (16477 - 16557)
    16477: (
        "Vejamos... Onde será que a Aurica foi parar...?",
        "Lyner procura Aurica ao adentrar o cenário da Cosmosfera."
    ),
    16478: (
        "Lyner!",
        "Aurica surge chamando por seu parceiro com entusiasmo."
    ),
    16479: (
        "Ah, aí tá você!\nE aí? As suas notas melhoraram nem que seja um pouquinho?",
        "Lyner indaga em tom descontraído sobre o boletim de notas de Aurica."
    ),
    16480: (
        "Hehehe, deixa esse assunto para lá!",
        "Aurica desconversa com risinho travesso (もうその話しはいいの)."
    ),
    16481: (
        "...Como?",
        "Lyner é surpreendido pela esquiva da garota."
    ),
    16482: (
        "Toma essa!",
        "Aurica dispara seu encanto paralisante com um grito enérgico (えいっ!)."
    ),
    16483: (
        "Uouuu!!",
        "Lyner é subjugado pela força do golpe psíquico."
    ),
    16484: (
        "M-mas o que é isso...? Onde...",
        "Lyner desperta desorientado em um novo cômodo."
    ),
    16485: (
        "...Onde é que eu tô?\nÉ melhor dar uma olhada em volta...",
        "Lyner tenta se mover para examinar o local."
    ),
    16486: (
        "Ai!!\nM-mas que correntes são essas?! Por que diabos eu tô...\namarrado na cama enrolado em tantas correntes?!",
        "Lyner percebe apavorado que está preso e imobilizado por grossos grilhões."
    ),
    16487: (
        "...Lyner.",
        "Aurica aproxima-se com voz mansa e olhar fixo."
    ),
    16488: (
        "Uou!\nAurica!?... Mas que roupas são essas afinal...?!",
        "Lyner espanta-se com o visual ousado e atípico assumido por Aurica na Cosmosfera."
    ),
    16489: (
        "Diga, Lyner...\nEu tô... bonita...?",
        "Aurica busca a aprovação do cavaleiro com insegurança disfarçada de charme."
    ),
    16490: (
        "D-do que você tá falando?!\nTira essas correntes de mim, por favor!",
        "Lyner ignora o flerte e implora pela soltura imediata."
    ),
    16491: (
        "Ué? Não me diga que...\nficou tão fascinado olhando para mim que não tá aguentando?\nMas ainda não pode...",
        "Aurica provoca Lyner insinuando que ele não resiste aos seus encantos."
    ),
    16492: (
        "A-aguentando o quê?! Não tem nada a ver com isso!\nPor que me amarrou desse jeito...?",
        "Lyner contesta a presunção embaraçosa com indignação gaga."
    ),
    16493: (
        "É que... você é mulherengo demais, Lyner.\nSe eu não fizer isso, você logo corre para o lado de outra garota, né?",
        "Aurica expressa seu ciúme possessivo e pavor inconsciente do abandono (気が多い)."
    ),
    16494: (
        "Eu nunca faria uma coisa dessas!!",
        "Lyner rechaça com veemência o rótulo de inconstante."
    ),
    16495: (
        "Faria ou não faria, tanto faz!\nPorque agora... você é todinho meu e de mais ninguém...",
        "Aurica manifesta sua obsessão em mantê-lo cativo como objeto exclusivo de seu afeto."
    ),
    16496: (
        "Né, Lyner...?",
        "Aurica busca a cumplicidade do rapaz em tom suave."
    ),
    16497: (
        "...S-sim...?",
        "Lyner responde hesitante e na defensiva."
    ),
    16498: (
        "Sabe...",
        "Aurica prepara sua confissão íntima com doçura enganosa."
    ),
    16499: (
        "Eu quero... me unir a você de corpo e alma, Lyner...\nVocê deixa...?",
        "Aurica pede a fusão afetiva total na Cosmosfera (ひとつになりたいの)."
    ),
    16500: (
        "C... como assim, o quêêêê?!",
        "Lyner empalidece em choque absoluto com a audácia do pedido."
    ),
    16501: (
        "Se você concordar,\neu solto as correntes agora mesmo.",
        "Aurica oferece a liberdade como moeda de troca para a anuência de Lyner."
    ),
    16502: (
        "E se eu disser que não...?",
        "Lyner tenta sondar as repercussões de uma negativa."
    ),
    16503: (
        "Aí eu não solto as correntes...\ne vou aprontar mil e uma travessuras com você... Quem sabe...?",
        "Aurica faz ameaças veladas e cômicas com ar misterioso (あーんな事やこーんな事)."
    ),
    16504: (
        "...",
        "Lyner calcula rapidamente suas chances diante da chantagem."
    ),
    16505: (
        "...Tá, eu aceito!",
        "Lyner finge capitulação para conseguir a desamarração."
    ),
    16506: (
        "É sério?!\nAh, Lyner... Eu com você...",
        "Aurica comove-se acreditando na aceitação genuína do cavaleiro."
    ),
    16507: (
        "(As correntes caíram! É a minha chance...!!)",
        "Pensamento de fuga de Lyner aproveitando o descuido da garota."
    ),
    16508: (
        "Uaaah!!",
        "Lyner salta em debandada pela sala."
    ),
    16509: (
        "Você tava tentando fugir agora, não tava?",
        "Aurica bloqueia a saída interceptando a manobra evasiva."
    ),
    16510: (
        "E-eu? Imagina!",
        "Lyner desconversa com fingimento canhestro."
    ),
    16511: (
        "Mentira...\nTava na cara que você ia fugir de mim.",
        "Aurica reprova a traição da palavra com decepção gélida."
    ),
    16512: (
        "Olha só...\nSe você tentar escapar outra vez...\ncorrentes vão ser o menor dos seus problemas...",
        "Aurica avisa friamente que a próxima punição será muito mais severa."
    ),
    16513: (
        "Por exemplo... que tal uma coisinha assim?",
        "Aurica materializa uma faísca elétrica como demonstração de força."
    ),
    16514: (
        "Uwaaaah! T-tô tomando um choque...!!",
        "Lyner contorce-se sob a descarga elétrica entorpecente (しびれる)."
    ),
    16515: (
        "Gostou tanto assim da sensação...?\nQuer que eu mande mais um choque?",
        "Aurica ironiza o sofrimento físico de Lyner com sadismo infantil."
    ),
    16516: (
        "Não, já chega, pelo amor dos deuses!\nEu me rendo! Não tento mais fugir!!",
        "Lyner capitula de vez implorando pelo cessar-fogo elétrico."
    ),
    16517: (
        "Mas... Aurica, desde quando você ficou...\ntão ousada desse jeito?",
        "Lyner questiona o contraste radical com a personalidade recatada da donzela no mundo real (大胆なんだ)."
    ),
    16518: (
        "É que eu quero ficar com você para todo o sempre...\nNão importa a idade que a gente tenha... envelhecendo juntos... até na morte...",
        "Aurica expõe o núcleo de sua angústia: o medo dilacerante da brevidade e do esquecimento."
    ),
    16519: (
        "Por isso, aconteça o que acontecer,\neu nunca, jamais vou soltar você...",
        "Aurica reafirma seu voto possessivo de retenção absoluta."
    ),
    16520: (
        "Sim, mas veja bem... eu tenho as minhas obrigações no mundo real.\nE se eu não voltar, a Aurica da realidade não vai conseguir acordar...",
        "Lyner apela para o senso de autopreservação da jovem para justificar o retorno."
    ),
    16521: (
        "Você não precisa voltar para a realidade...\nE eu... também não faço questão de acordar nunca mais.",
        "Aurica rejeita a vida desperta em prol da fantasia psíquica protetora."
    ),
    16522: (
        "Se eu acordar, a gente não vai poder ficar junto o tempo todo de novo.\nAlém disso, a realidade só traz sofrimento...",
        "Aurica desabafa sobre a crueldade e a solidão da vida real (現実は辛いことばかり)."
    ),
    16523: (
        "Se eu puder ficar com você para sempre aqui dentro...\neu prefiro nunca mais abrir os olhos até o fim da vida...",
        "Aurica escolhe o sono eterno desde que compartilhada com Lyner."
    ),
    16524: (
        "V-você tá falando sério mesmo...?",
        "Lyner assusta-se com a seriedade sombria do voto da donzela."
    ),
    16525: (
        "Lyner...\nVem ficar comigo...",
        "Aurica reitera seu apelo de aproximação íntima."
    ),
    16526: (
        "Não, eu não posso fazer isso com você, Aurica...!\nNão desse jeito...",
        "Lyner recusa o envolvimento por ética e zelo fraternal."
    ),
    16527: (
        "Ué? Que coisa seria essa?",
        "Aurica finge desentendimento para embaraçar o rapaz."
    ),
    16528: (
        "Hã?! Ah, quer dizer... Quando um rapaz e uma garota...\nsabe... se unem assim... aquela intimidade toda...",
        "Lyner balbucia corado ao tentar explicar sua leitura do que ouviu."
    ),
    16529: (
        "Nossa... Era nisso que você tava pensando?!\nQue indecente, Lyner...\nQuem diria que você era tão atirado...",
        "Aurica zomba chamando Lyner de atrevido e pervertido (ライナーのエッチ)."
    ),
    16530: (
        "Ai! N-não era isso?! Então retiro o que eu disse agora mesmo!!",
        "Lyner entra em combustão de vergonha e cancela a fala anterior."
    ),
    16531: (
        "...Não retiro nada não.",
        "Aurica desmente com cumplicidade maliciosa (違わないよ)."
    ),
    16532: (
        "Se for você, Lyner...\neu aceitaria de coração aberto tudo o que quisesse fazer comigo...",
        "Aurica confessa sua total vulnerabilidade e entrega emocional a ele."
    ),
    16533: (
        "Só de imaginar o que a gente poderia fazer...\neu já sinto até um arrepio pelo corpo todo...",
        "Aurica devaneia com o toque do cavaleiro eletrizando seus sentidos (シビレちゃいそう)."
    ),
    16534: (
        "Uwaaaah! T-tô tomando outro choque...!!",
        "A empolgação de Aurica descarrega outra rajada involuntária em Lyner."
    ),
    16535: (
        "Você tá arrepiado igualzinho a mim, né... Que alegria...",
        "Aurica interpreta o choque como sintonia afetiva correspondida."
    ),
    16536: (
        "Olha, Lyner...\nEu me decidi.",
        "Aurica bate o martelo sobre a resolução de confinamento."
    ),
    16537: (
        "D-decidiu o quê...?",
        "Lyner teme pelo pior ao ouvir a solenidade na voz dela."
    ),
    16538: (
        "Vou deixar você amarrado aqui para sempre.\nAssim, você vai olhar unicamente para mim a toda hora.",
        "Aurica sela o cativeiro perpétuo para garantir a atenção exclusiva de Lyner."
    ),
    16539: (
        "E vai pensar apenas em mim, a cada segundo...",
        "O desejo de monopolizar as lembranças e afetos de seu salvador."
    ),
    16540: (
        "M-mas que loucura é essa...?!",
        "Lyner protesta em choque contra a decisão delirante."
    ),
    16541: (
        "Se você me prender aqui,\ncomo é que eu vou conseguir voltar para o mundo real...?!",
        "Lyner cobra a coerência funcional entre a mente e a realidade desperta."
    ),
    16542: (
        "Você não precisa voltar para a realidade...\nE eu... também não faço questão de acordar nunca mais.",
        "Aurica reafirma sua recusa em despertar para o mundo exterior."
    ),
    16543: (
        "Se eu acordar, a gente não vai poder ficar junto o tempo todo de novo.\nAlém disso, a realidade só traz sofrimento...",
        "Aurica lamenta as agruras e desilusões da vida fora da mente."
    ),
    16544: (
        "Se eu puder ficar com você para sempre aqui dentro...\neu prefiro nunca mais abrir os olhos até o fim da vida...",
        "Aurica defende o confinamento como única salvação para o amor de ambos."
    ),
    16545: (
        "V-você tá falando sério mesmo...?",
        "Lyner estarrece-se diante da fixação psíquica da donzela."
    ),
    16546: (
        "Lyner...\nVem ficar comigo...",
        "Aurica acolhe o momento de união eterna."
    ),
    16547: (
        "Onde eu tô...\nAh, é verdade, eu fui capturado pela Aurica... Quando será que vou conseguir sair daqui...?",
        "Lyner desperta no aposento de cativeiro ponderando uma rota de fuga."
    ),
    16548: (
        "...Entendi tudo.\nO \"verdadeiro risco de vida\" de que o Don Leon falou... era exatamente sobre isso...",
        "Lyner correlaciona a loucura da cena com os avisos ancestrais de Don Leon."
    ),
    16549: (
        "Tô amarrado em correntes de novo...\nQue fome que tá me dando... Como é que eu vou comer aqui dentro...?",
        "Lyner manifesta seu apego às necessidades materiais mesmo preso na mente dela."
    ),
    16550: (
        "Ora, ora... Que situação complicada em que você se meteu, hein?",
        "Uma voz misteriosa surge debochando do aperto do cavaleiro."
    ),
    16551: (
        "Aurica!?...\nEspera, essas roupas... eu tenho a impressão de já ter visto antes...",
        "Lyner reconhece os trajes de uma faceta mais profunda de Aurica."
    ),
    16552: (
        "Isso mesmo. Eu sou a Aurica, mas não a Aurica deste nível de mundo.",
        "A projeção do inconsciente profundo esclarece sua identidade desdobrada."
    ),
    16553: (
        "Eu vim de um estrato que você ainda não alcançou na sua jornada.",
        "A Aurica guardiã explica sua procedência de uma camada mental mais avançada."
    ),
    16554: (
        "...Mas não importa nada disso agora!\nDepressa, fuja daqui o quanto antes!",
        "A guardiã exige urgência máxima na evacuação de Lyner."
    ),
    16555: (
        "As correntes caíram!\nMuito obrigado, você me salvou!\nMas fugir como, se não tem saída...?!",
        "Lyner comemora a libertação e questiona o caminho de fuga."
    ),
    16556: (
        "Não importa, vamos sair logo daqui!",
        "A guardiã lidera a rota de escape rompendo o casulo da sala."
    ),
    16557: (
        "Você teceu a Magia Verde [Tiro Trovejante]!",
        "Conclusão do evento com a criação da Magia Verde elemental na Cosmosfera."
    )
}

print(f"Total curated lines defined: {len(curated_data)}")

# Validação linha a linha
hard_gate_errors = 0
lint_warnings = 0

for item in inp["dialogues"]:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    if item_id not in curated_data:
        print(f"[ERROR] Missing translation for ID {item_id}")
        hard_gate_errors += 1
        continue

    trad, rat = curated_data[item_id]

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
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    # Check orphan line start with punctuation after \n
    parts = trad.split("\n")
    for line_part in parts[1:]:
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1

    # Check syntactic fracture before \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

print(f"\nValidation Result:")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("[SUCCESS] All checks passed with 0 errors and 0 warnings!")
else:
    print("[FAILURE] Fix the issues above before proceeding.")
    sys.exit(1)

# Montagem do output JSON
output_dialogues = []
output_curated_lines = []

for item in inp["dialogues"]:
    item_id = item["id"]
    trad, rat = curated_data[item_id]

    output_curated_lines.append({
        "id": item_id,
        "ptbr_curated": trad,
        "rationale": rat
    })

    d_out = {
        "id": item_id,
        "event_file": item.get("event_file"),
        "speaker_id": item.get("speaker_id"),
        "speaker": item.get("speaker"),
        "original_jp": item.get("original_jp"),
        "original_en": item.get("original_en"),
        "current_ptbr": item.get("current_ptbr"),
        "review_status": "approved",
        "text_ptbr": trad,
        "curated_ptbr": trad,
        "final_ptbr": trad,
        "texto_ptbr_curado": trad,
        "custom_text": trad,
        "ptbr_curated": trad,
        "reviewed": True,
        "notes": rat,
        "curation_notes": rat,
        "curadoria_notes": rat
    }
    output_dialogues.append(d_out)

glossary_additions = {
    "Tiro Trovejante": {
        "pt": "Tiro Trovejante",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia Verde / Cosmosphere",
        "note": "緑魔法【雷弾】. Magia Verde elemental tecida por Aurica na Cosmosfera (Nível 3) sob a forma de esfera elétrica para energizar circuitos e ativar interruptores paralisados na Torre."
    },
    "Cerimônia de Download": {
        "pt": "Cerimônia de Download",
        "gender": "feminino",
        "number": "singular",
        "category": "Lore / Sistema",
        "note": "ダウンロードの儀式. Rito sagrado e técnico oficiado em Platina no qual um Cristal Hymmnos (ex.: Purger) é sintonizado e transferido para a memória de uma Reyvateil."
    },
    "Verdadeiro Nome": {
        "pt": "Verdadeiro Nome",
        "gender": "masculino",
        "number": "singular",
        "category": "Lore / Identidade",
        "note": "真の名前. Metáfora mística e lendária para o Código Hymmnos pessoal e secreto de cada Reyvateil, obtido ao mergulhar na Cosmosfera e obter a confidência de seu guardião."
    }
}

scene_handoff = {
    "last_scene_id": "Event/743.evd",
    "last_line_id": 16557,
    "resumo_dramatico": "O bloco BLK_EVD_072 aprofunda três momentos dramáticos e sistêmicos cruciais: (1) Em Event/446.evd (variante da rota de Aurica), Lyner e Aurica encontram Krusche cercada pela segurança corporativa da Tenba; esclarecido que ela fora contratada pela Presidente Ayano como engenheira-chefe do Projeto Shoga para criar uma aeronave de alcance global, Lyner pede sua ajuda para localizar o Cristal Hymmnos \"RE Nation\" e salvar Shurelia, mas Krusche precisa recusar diante da responsabilidade intransferível de seu cargo corporativo. O acesso à Sede da Tenba é liberado no mapa urbano. (2) Em Event/178.evd, na plataforma de Platina, Lyner e o operador realizam a Cerimônia de Download do lendário Cristal Hymmnos Purger (PAJA). O jogador pode escolher entre Aurica ou Misha para receber o download através de seus respectivos Códigos Hymmnos primordiais (\"MULE TEIWAZ ARTONELICO\" ou \"MISYA FEHU EORIA ARTONELICO\"); ao sintonizarem a canção, ambas vivenciam um despertar nostálgico e comovente. Caso o jogador ainda não saiba o Código Hymmnos, o operador elucida que o código é o \"verdadeiro nome\" secreto da Reyvateil, que exige mergulhar em sua Cosmosfera e conquistar a confiança do guardião. (3) Em Event/743.evd, no Nível 3 da Cosmosfera de Aurica, Lyner depara-se com uma faceta hiperpossessiva e sensual de Aurica, que o prende em grossas correntes na cama pelo pavor desesperado de perdê-lo para outras garotas ou de ser abandonada. Ao tentar escapar, Lyner é castigado com faíscas elétricas e descobre que Aurica deseja hibernar eternamente naquele mundo onírico ao lado dele para nunca mais sofrer na dura realidade desperta. Uma projeção de Aurica de um nível mais profundo surge, liberta Lyner dos grilhões e o guia para a fuga, culminando na tecitura da Magia Verde [Tiro Trovejante] (雷弾).",
    "decisoes_terminologicas": {
        "RE Nation": "リ・ネイション (RE Nation / Cristal Hymmnos primordial para despertar a Senhora Shurelia)",
        "Tenba Headquarters": "天覇本社 (Sede da Tenba / complexo industrial-corporativo)",
        "President Ayano": "亜耶乃社長 (Presidente Ayano / líder executiva da Tenba)",
        "Purger": "パージャ (Purger / Cristal Hymmnos e Magia da Canção de purificação viral)",
        "Download Ceremony": "ダウンロードの儀式 (Cerimônia de Download / rito sagrado de sintonização na praça de Platina)",
        "Hymn Code": "ヒュムネコード (Código Hymmnos / chave alfanumérica e senha de identificação da Reyvateil)",
        "True Name": "真の名前 (Verdadeiro Nome / metáfora mística do Código Hymmnos)",
        "MULE TEIWAZ ARTONELICO": "Código Hymmnos ancestral primordial de Aurica",
        "MISYA FEHU EORIA ARTONELICO": "Código Hymmnos de linhagem Origin de Misha",
        "Thunder Shot": "緑魔法【雷弾】 (Magia Verde [Tiro Trovejante] / projétil de descarga elétrica para energizar circuitos)"
    },
    "alertas_para_proximo_bloco": "Nos blocos subsequentes (BLK_EVD_073 em diante), acompanhar as repercussões da posse da Magia Verde [Tiro Trovejante] na exploração dos labirintos da Torre e setores industriais, a progressão das camadas mais profundas da Cosmosfera de Aurica e Misha, bem como o avanço na busca pelas chaves para despertar a Senhora Shurelia."
}

final_output = {
    "block_id": inp["block_id"],
    "axis_id": inp["axis_id"],
    "axis_name": inp["axis_name"],
    "category": inp["category"],
    "line_count": len(output_dialogues),
    "id_range": inp["id_range"],
    "curated_lines": output_curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": output_dialogues,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {output_path} with {len(output_dialogues)} lines.")

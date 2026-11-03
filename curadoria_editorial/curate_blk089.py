# -*- coding: utf-8 -*-
"""
curate_blk089.py - Curadoria Editorial Canônica de BLK_EVD_089
"""
import sys
import json
import re
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Definindo as falas curadas por ID com notas
curated_data = {
    # =========================================================================
    # Event/864.evd (IDs 19993-20032): Tutorial de Aprimoramento com Cristais Grathnode
    # =========================================================================
    19993: (
        "Mas me diga uma coisa, Lyner...\nUm Cavaleiro de Elemia luta só com uma espada dessas?",
        "Jack questionando casualmente o estilo de combate de Lyner apenas com espada."
    ),
    19994: (
        "Hã? Sim, é isso mesmo.\nMas por que a pergunta?",
        "Lyner respondendo com naturalidade e estranheza à indagação de Jack."
    ),
    19995: (
        "É que, vendo você lutar com tanta garra\nportando uma lâmina comum, achei impressionante.",
        "Jack elogiando o talento marcial bruto de Lyner com uma espada sem modificações."
    ),
    19996: (
        "De onde veio esse elogio repentino?...\nMas bem, não posso negar que sou bom de briga.",
        "Lyner demonstrando seu orgulho juvenil bem-humorado."
    ),
    19997: (
        "Mesmo assim... Você nunca fez um Aprimoramento?\nDessa vez você me deixou de queixo caído...",
        "Jack chocado com a inocência técnica de Lyner sobre aprimoramento de armas (パワード)."
    ),
    19998: (
        "Aprimoramento?...\nQue história é essa de Aprimoramento?",
        "Lyner intrigado ao ouvir falar de Aprimoramento pela primeira vez."
    ),
    19999: (
        "O quê!? Você nem sequer sabe\no que é um Aprimoramento?",
        "Jack incrédulo diante da falta de instrução armamentista do cavaleiro."
    ),
    20000: (
        "...Francamente, você não tem jeito.\nVou te ensinar ali na loja de armas. Me acompanhe.",
        "Jack guiando Lyner até a loja de armas local."
    ),
    20001: (
        "E-ei! Espere aí!\nO que está pegando afinal?",
        "Lyner sendo arrastado por Jack sem entender a urgência."
    ),
    20002: (
        "Olá, senhorita.\nQueremos aprimorar nossos equipamentos.\nTem algum bom Grathnode em estoque?",
        "Jack flertando/conversando amigavelmente com a atendente da loja de armas."
    ),
    20003: (
        "Ah, os senhores chegaram na hora perfeita!\nAcabamos de receber um Ataque Duplo~",
        "Atendente jovem da loja de armas anunciando a chegada de Cristal Grathnode raro."
    ),
    20004: (
        "Ora, que maravilha! Você tem ótimos contatos.\nQuanto vai custar?",
        "Jack elogiando o estoque da vendedora e perguntando o preço."
    ),
    20005: (
        "Como é uma peça raríssima, seriam 2.000 Leaves!...\nOu pelo menos era o que eu cobraria, mas...",
        "Vendedora preparando a surpresa generosa para os heróis."
    ),
    20006: (
        "Vocês são os heróis que derrotaram aquele Guardião, não são?\nEntão considerem isto um presente meu!",
        "Vendedora presenteando o grupo em gratidão pela derrota do Guardião."
    ),
    20007: (
        "Cristal Grathnode: «Ataque Duplo» obtido!",
        "Mensagem de sistema: recebimento do Cristal Grathnode «Ataque Duplo»."
    ),
    20008: (
        "Tem certeza disso?\nNão é uma peça valiosa demais para dar de graça?",
        "Lyner hesitante diante da generosidade do presente."
    ),
    20009: (
        "Não se preocupem! Perto de salvarem a nossa cidade,\nisso não é nada. Agradeço de coração!",
        "Vendedora expressando profunda gratidão sincera."
    ),
    20010: (
        "...Bom, se ela está oferecendo de bom grado,\nvamos aceitar sem cerimônia.",
        "Jack pragmático aceitando a oferta gentil."
    ),
    20011: (
        "E então? Como funciona esse tal de Aprimoramento?",
        "Lyner retomando a dúvida sobre o funcionamento técnico."
    ),
    20012: (
        "Seguinte: o Aprimoramento serve para transferir\no poder oculto nos Cristais Grathnode aos seus equipamentos.",
        "Jack explicando a mecânica de infusão dos Cristais Grathnode em armas."
    ),
    20013: (
        "Dá para usá-los dessa forma também?...",
        "Lyner surpreso ao descobrir a versatilidade bélica dos cristais."
    ),
    20014: (
        "Quanto maior for o nível do cristal,\nmais devastador será o poder guardado nele.",
        "Jack detalhando a relação entre o nível do cristal e sua potência."
    ),
    20015: (
        "Mas lembre-se: para suportar um cristal poderoso,\nvocê precisará de um equipamento à altura.",
        "Jack alertando sobre os requisitos de compatibilidade dos equipamentos."
    ),
    20016: (
        "Bem, ver para crer. Experimente instalar esse «Ataque Duplo»\nque acabamos de ganhar para você entender na prática.",
        "Jack incentivando Lyner a testar imediatamente o cristal recebido."
    ),
    20017: (
        "O tópico de ajuda «Aprimoramento» foi adicionado.",
        "Notificação de sistema sobre inclusão do tutorial de Aprimoramento no menu."
    ),
    20018: (
        "Deseja visualizar as explicações detalhadas deste tópico?",
        "Caixa de confirmação do tutorial interativo do sistema."
    ),
    20019: (
        "Os Cristais Grathnode podem ser obtidos\nem lojas ou após batalhas por todo o mundo.",
        "Tutorial explicando as fontes de obtenção dos Cristais Grathnode."
    ),
    20020: (
        "Você pode utilizar esses cristais para potencializar\nos atributos dos equipamentos dos personagens.",
        "Tutorial explicando a função básica do Aprimoramento."
    ),
    20021: (
        "Primeiro, escolha qual Cristal Grathnode\ndeseja utilizar no Aprimoramento.",
        "Passo 1 do tutorial: seleção do cristal desejado."
    ),
    20022: (
        "Cada Cristal Grathnode possui um nível que varia de 1 a 4.",
        "Classificação em 4 níveis dos Cristais Grathnode."
    ),
    20023: (
        "Em cada espaço, você pode equipar Cristais Grathnode\nde nível equivalente ou inferior ao indicado no compartimento.",
        "Regra de encaixe por nível de slot sem fratura sintática."
    ),
    20024: (
        "Quanto maior for o nível do cristal,\nmais restritos serão os espaços disponíveis para aprimoramento.",
        "Explicação sobre a escassez de slots para cristais de alto nível."
    ),
    20025: (
        "Além disso, entre cristais que concedem o mesmo efeito,\napenas o bônus de maior valor será aplicado.",
        "Regra de não-acumulação de efeitos idênticos em armas."
    ),
    20026: (
        "Com o Aprimoramento, a capacidade combativa\ndo grupo de Lyner se elevará expressivamente.",
        "Impacto estratégico do aprimoramento no rendimento da equipe."
    ),
    20027: (
        "Os benefícios incluem adicionar dano elemental aos golpes,\nprovocar anomalias de estado no adversário ou...",
        "Exemplos de efeitos adicionais concedidos por cristais."
    ),
    20028: (
        "...até mesmo elevar diretamente os atributos base dos equipamentos.",
        "Efeito de melhoria de status diretos nos equipamentos."
    ),
    20029: (
        "Ao explorar as fraquezas elementais dos inimigos,\nvocê causará um impacto devastador em batalha.",
        "Dica tática de exploração de fraquezas elementais."
    ),
    20030: (
        "Os aprimoramentos instalados permanecerão intactos\nmesmo se você trocar a arma equipada.",
        "Garantia de persistência do aprimoramento ao alternar armas."
    ),
    20031: (
        "Aproveite para personalizar seus guerreiros à vontade!",
        "Estímulo do tutorial para livre experimentação de personalização."
    ),
    20032: (
        "Um resumo destas orientações pode ser consultado\na qualquer momento no tópico «Ajuda» do menu principal.",
        "Indicação de consulta futura do tutorial no menu Ajuda."
    ),

    # =========================================================================
    # Event/809.evd (IDs 20033-20099): Minigame/Simulação Paródica de Shurelia
    # =========================================================================
    20033: (
        "Raina.",
        "Misha interpretando na simulação colegial e chamando Lyner pelo nome fictício Raina."
    ),
    20034: (
        "Misha!\nVocê caprichou na produção hoje, hein...",
        "Lyner admirando a fantasia vestida por Misha na simulação."
    ),
    20035: (
        "O que achou? Ficou bom em mim, não ficou?",
        "Misha pedindo a opinião de Lyner sobre seu figurino com charme."
    ),
    20036: (
        "Sim, caiu muito bem em você.",
        "Lyner elogiando com sinceridade o visual de Misha."
    ),
    20037: (
        "Obrigada.\nDepois trate de dizer a mesma coisa para a Leila, ouviu?",
        "Misha lembrando Lyner de elogiar a noiva Leila (Shurelia)."
    ),
    20038: (
        "Raina!",
        "Convidado do casamento saudando Lyner na simulação."
    ),
    20039: (
        "Nossa! O Raina não chegou atrasado?...\nNem estou acreditando!",
        "Convidada zombando da pontualidade rara de Lyner."
    ),
    20040: (
        "Mas que diabos... O que deu nessa sua roupa?!",
        "Lyner espantado com a extravagância da vestimenta do colega."
    ),
    20041: (
        "Ué? São os meus trajes de gala, sabia?",
        "Convidado justificando sua roupa formal inusitada."
    ),
    20042: (
        "Você não entendeu nada do figurino.",
        "Lyner comentando com ironia e incredulidade."
    ),
    20043: (
        "Como assim?!\nA Misha está vestida num estilo bem parecido!",
        "Convidado apontando que Misha também está fantasiada."
    ),
    20044: (
        "Não tem nada a ver uma coisa com a outra...",
        "Lyner defendendo que Misha está elegante, ao contrário do colega."
    ),
    20045: (
        "Mas mudando de assunto...\nMesmo sendo de mentirinha, tudo parece tão autêntico.",
        "Misha comentando sobre o realismo impressionante da cerimônia na capela."
    ),
    20046: (
        "Mas é claro!\nEu tive que implorar de joelhos ao padre desta capela\npara ele aceitar realizar a cerimônia.",
        "Lyner explicando seu esforço para convencer o sacerdote do local."
    ),
    20047: (
        "Afinal de contas... é uma ocasião única na vida, não é?\nNão existe essa de «de mentira» ou «de verdade».",
        "Lyner demonstrando sua solenidade e carinho genuínos pela ocasião."
    ),
    20048: (
        "...\nPerdão... Eu não devia...",
        "Misha ficando constrangida e pedindo desculpas pela indiscrição."
    ),
    20049: (
        "Tudo bem, não precisa se desculpar...\nNão havia outra saída mesmo.\nHoje é dia de festejar com tudo!",
        "Lyner confortando Misha e convidando todos a comemorar alegremente."
    ),
    20050: (
        "Neste dia tão auspicioso, manifesto minha mais sincera alegria\npor testemunhar o início desta nova jornada a dois.",
        "Padre (interpretado por Tastiella/Falss) abrindo a cerimônia matrimonial."
    ),
    20051: (
        "E agora, com vocês... a entrada da noiva.",
        "Padre anunciando solene a entrada triunfal da noiva."
    ),
    20052: (
        "...Leila...",
        "Lyner emocionado ao vislumbrar Leila Togasaki (Shurelia) vestida de noiva."
    ),
    20053: (
        "O que achou?... Ficou bem em mim?...",
        "Leila tímida e deslumbrante perguntando sobre seu vestido."
    ),
    20054: (
        "Sim... Você está deslumbrante.",
        "Lyner encantado com a beleza radiante de Leila."
    ),
    20055: (
        "...Muito obrigada...",
        "Leila agradecendo com doçura e afeto."
    ),
    20056: (
        "Demos prosseguimento ao rito sagrado.",
        "Padre conduzindo os votos matrimoniais solenes."
    ),
    20057: (
        "Raina Harase.\nPrometeis amar Leila Togasaki em todas as circunstâncias\ne apoiar-vos mutuamente na alegria e na adversidade?",
        "Voto matrimonial sagrado dirigido a Raina Harase."
    ),
    20058: (
        "...Sim, prometo.",
        "Lyner proferindo seu compromisso solene de amor eterno."
    ),
    20059: (
        "Leila Togasaki.\nPrometeis amar Raina Harase em todas as circunstâncias\ne apoiar-vos mutuamente na alegria e na adversidade?",
        "Voto matrimonial sagrado dirigido a Leila Togasaki."
    ),
    20060: (
        "Sim, prometo.",
        "Leila confirmando seu voto sagrado diante do altar."
    ),
    20061: (
        "Muito bem.\nPermiti-me agora proferir uma breve exortação\npara guiar os passos de vossa vida conjunta.",
        "Padre preparando a virada dramática e sombria da cena."
    ),
    20062: (
        "Jamais vos esqueçais de que a vingança não é mero impulso passageiro,\nmas uma maldição indelével que assombra por incontáveis gerações.",
        "Padre destilando rancor e revelando sua faceta perturbadora."
    ),
    20063: (
        "E nunca vos esqueçais de que o ódio ataca implacavelmente,\nsem piedade, a qualquer momento.",
        "Padre profetizando o ataque cruel do ódio sobre os amantes."
    ),
    20064: (
        "...",
        "Lyner pasmo e estupefato diante do discurso bizarro do padre."
    ),
    20065: (
        "Ele surge dos lugares mais inesperados.\nDespoja, humilha e consome tudo até consumar o seu desígnio.",
        "Padre ameaçando abertamente o casal no altar."
    ),
    20066: (
        "Você... não é um padre de verdade!...",
        "Leila percebendo a impostura sinistra do clérigo."
    ),
    20067: (
        "Sou um sacerdote, sim.\nContudo, não sou humano...\nAssim como você, Shurelia!",
        "Padre revelando sua natureza não-humana e chamando Leila pelo verdadeiro nome."
    ),
    20068: (
        "Você... é um vírus?!",
        "Leila reconhecendo o inimigo viral disfarçado."
    ),
    20069: (
        "Como é que é?!\nLogo numa hora dessas!...",
        "Lyner enfurecido com a interrupção vil em pleno casamento."
    ),
    20070: (
        "Jamais vos esqueçais de que a vingança não é mero impulso passageiro,\nmas uma maldição que assombra por gerações.",
        "Convidados da capela entoando o cântico macabro em uníssono."
    ),
    20071: (
        "E nunca vos esqueçais de que o ódio ataca implacavelmente,\na qualquer instante.",
        "Claire completando a sentença sinistra ao fazer sua entrada apoteótica."
    ),
    20072: (
        "Olá, Leila... Raina...\nPerdoem-me por arruinar a festinha de vocês.",
        "Claire tripudiando com deboche e malícia diabólica."
    ),
    20073: (
        "Claire!!\nTinha que aparecer logo agora, sua desgraçada?...\nEu nunca vou te perdoar por isso!",
        "Lyner reagindo com fúria contra a invasão de Claire."
    ),
    20074: (
        "Essa é a minha fala!\nVocês destruíram o meu esconderijo, sequestraram a Shurelia...\ne arruinaram todos os meus planos!",
        "Claire justificando sua vendeta pela sabotagem de seus projetos."
    ),
    20075: (
        "Eu jamais perdoarei vocês...\nPor isso escolhi justamente este momento:\no instante mais cruel possível para a vida de vocês!",
        "Claire revelando seu sadismo ao escolher o dia do casamento para atacar."
    ),
    20076: (
        "Leila... Seus dias estão contados.",
        "Claire sentenciando a morte iminente de Leila."
    ),
    20077: (
        "...!!",
        "Leila em choque ao ter sua finitude esfregada na face."
    ),
    20078: (
        "Claire! Como você se atreve...",
        "Lyner tentando intervir e proteger Leila."
    ),
    20079: (
        "E a culpa é de vocês dois!\nOuviu bem, Raina?! Misha?!",
        "Claire culpando as escolhas de Raina e Misha pela tragédia."
    ),
    20080: (
        "Eu já sei muito bem disso...",
        "Leila confessando resignada a consciência de seu fardo."
    ),
    20081: (
        "Compreendo... Só que antes do seu fim,\nfaço questão absoluta de esmagar você com as minhas próprias mãos.",
        "Claire expressando sua sede assassina de combate direto."
    ),
    20082: (
        "O sentimento é recíproco...\nRaina... empresta-me a tua força...",
        "Leila aceitando o duelo e pedindo a ressonância de Lyner."
    ),
    20083: (
        "Leila!\nNão faça isso! Não gaste mais as suas forças!",
        "Lyner desesperado tentando impedir o desgaste vital de Leila."
    ),
    20084: (
        "Raina... Não se preocupe.\nAo me transformar, eu não consumirei a minha própria energia:\nserei movida pelo poder dos seus Harmonics!",
        "Leila explicando que sua forma mágica se nutre dos Harmonics de Lyner."
    ),
    20085: (
        "...É verdade mesmo?!",
        "Lyner hesitando e buscando confirmação."
    ),
    20086: (
        "Apenas confie em mim...",
        "Leila pedindo fé e cumplicidade ao companheiro."
    ),
    20087: (
        "Está bem...",
        "Lyner concordando em sincronizar seu poder."
    ),
    20088: (
        "Enquanto o mal macular a terra,\na verdadeira felicidade jamais florescerá!",
        "Início da proclamação dramática de heroína tokusatsu/mágica."
    ),
    20089: (
        "Portanto, dissiparei as trevas deste mundo...\ne cairei com elegância quando minha hora chegar!\nEis que surge a Singer Angel Shurelia!",
        "Clímax da transformação de Shurelia em Singer Angel com lema heroico."
    ),
    20090: (
        "(Leila... Eu já devia imaginar...)",
        "Lyner resignado e perplexo com os exageros dramáticos de Shurelia."
    ),
    20091: (
        "Então vamos lá!...\nFalss, liberte o seu selo agora mesmo!\nTorne-se o vírus mais poderoso da história!",
        "Claire ordenando a libertação da entidade viral suprema."
    ),
    20092: (
        "Como desejar!...\nUoooohhhhhh!!!",
        "Falss respondendo com submissão e rugindo em monstruosa mutação."
    ),
    20093: (
        "M-mas o que é essa aberração?!",
        "Lyner chocado diante da silhueta monstruosa do vírus."
    ),
    20094: (
        "Que vírus hediondo...\nRaina... está preparado?",
        "Singer Angel Shurelia convocando Raina para a investida final."
    ),
    20095: (
        "Urrghh-gwaaah!...\nChacina total... Exterminar todos...",
        "Falss berrando palavras de aniquilação inarticuladas."
    ),
    20096: (
        "...Ué? Onde é que eu estou?...",
        "Lyner despertando da simulação de volta à realidade."
    ),
    20097: (
        "Bem-vindo de volta.\nPelo visto, deu Game Over para você.",
        "Shurelia recebendo Lyner com sua costumeira placidez após a derrota no jogo."
    ),
    20098: (
        "Ah, que droga...",
        "Lyner lamentando a derrota no minigame de Shurelia."
    ),
    20099: (
        "Da próxima vez, dá para continuar de onde paramos.\nTalvez valha a pena tentar de novo em outro momento.",
        "Shurelia encorajando Lyner com otimismo sereno a rejogar o minigame."
    ),

    # =========================================================================
    # Event/375.evd (IDs 20100-20122): Posseção Viral de Shurelia e Rapto de Leard
    # =========================================================================
    20100: (
        "Senhora Shurelia!\nPai!",
        "Lyner adentrando a Catedral em desespero ao encontrar o pai e Shurelia em confronto."
    ),
    20101: (
        "M-mas o que é isso?!\nPor que a Senhora Shurelia e o meu pai estão...?!",
        "Lyner atônito sem compreender a hostilidade súbita da deusa da Torre."
    ),
    20102: (
        "Lyner! Fique longe!\nHá algo muito errado com a Senhora Shurelia!",
        "Leard alertando o filho com autoridade paternal e marcial sobre a anomalia."
    ),
    20103: (
        "A partir deste instante,\neste mundo passará por uma radical transformação de rumo.",
        "Shurelia possuída por Mir declarando a reviravolta apocalíptica da ordem global."
    ),
    20104: (
        "O extermínio completo da escória humana\ne a criação de uma utopia governada pela raça superior: as Reyvateils.",
        "Discurso chauvinista viral de supremacia das Reyvateils e purga da humanidade."
    ),
    20105: (
        "...Senhora Shurelia!\nMas o que a senhora está dizendo?!\nEssa brincadeira já passou de todos os limites!",
        "Lyner em choque, recusando-se a crer nas palavras cruéis de Shurelia."
    ),
    20106: (
        "...Humanos tolos.\nSerá que ainda não foram capazes de compreender?",
        "Shurelia corrompida demonstrando desdém gélido pela fragilidade humana."
    ),
    20107: (
        "Este mundo já me pertence.\nVermes humanos não possuem o menor direito de continuar habitando nele.",
        "Mir/Shurelia reafirmando a posse despótica de Sol Ciel."
    ),
    20108: (
        "Como é que é?...",
        "Jack atônito diante da hostilidade declarada da guardiã de Platina."
    ),
    20109: (
        "Comandante-Geral Leard.\nO senhor virá comigo até os níveis superiores.",
        "Shurelia ordenando o sequestro formal de Leard."
    ),
    20110: (
        "Ugh-aaaaahhh!!",
        "Leard urrando ao ser atingido e imobilizado pelo pulso energético."
    ),
    20111: (
        "Pai!!",
        "Lyner gritando em pânico diante da captura violenta do progenitor."
    ),
    20112: (
        "Pretende ficar no meu caminho,\nLyner?",
        "Shurelia desafiando friamente o protagonista com olhar glacial."
    ),
    20113: (
        "Pois muito bem.\nSerei a sua oponente.",
        "Shurelia aceitando o confronto contra Lyner sem vacilar."
    ),
    20114: (
        "Senhora Shurelia!!\nO que pretende fazer com o meu pai?!",
        "Lyner exigindo saber o destino do comandante capturado."
    ),
    20115: (
        "Como detentor de segredos de Nível Especial A,\nele será confinado no Jardim de Prisma e,\ncaso necessário, eliminado.",
        "Shurelia revelando a prisão de Leard no Jardim de Prisma com frieza técnica militar."
    ),
    20116: (
        "O quê?!",
        "Lyner aterrorizado com a perspectiva de execução do pai."
    ),
    20117: (
        "#0Wee i ga flip 0x1011001101 enter ARTONELICO",
        "Código canônico intocado de ativação e teletransporte em Hymmnos executado por Shurelia."
    ),
    20118: (
        "Senhora Shurelia...\nPai...",
        "Lyner desolado após o desaparecimento repentino de ambos."
    ),
    20119: (
        "Mas por que cargas d'água os vírus voltaram\na se alastrar com tamanha violência de repente?",
        "Radolf indagando com apreensão tática o ressurgimento da ameaça viral."
    ),
    20120: (
        "Ei, Lyner!\nSerá que... aconteceu alguma coisa com a Misha?!",
        "Krusche alertando Lyner sobre a vulnerabilidade crítica de Misha."
    ),
    20121: (
        "Não pode ser...",
        "Lyner temendo pelo pior destino para a amiga de infância."
    ),
    20122: (
        "É melhor não pagar para ver.\nVamos depressa até o Crescent Chronicle conferir.",
        "Jack ordenando marcha urgente até o altar sagrado de contenção Crescent Chronicle."
    ),

    # =========================================================================
    # Event/959.evd (IDs 20123-20158): Descoberta na Tenba e Alternância de Misha
    # =========================================================================
    20123: (
        "Mas o que é isso aqui?...",
        "Lyner vasculhando a instalação clandestina abandonada da Tenba."
    ),
    20124: (
        "Q-quem são vocês?!",
        "Pesquisador desonesto sobressaltado com a invasão súbita."
    ),
    20125: (
        "A pergunta é o que vocês estão fazendo aqui!\nEste setor não tinha sido totalmente interditado?",
        "Krusche confrontando os funcionários clandestinos com autoridade técnica."
    ),
    20126: (
        "S-sujou!\nCorram!!",
        "Pesquisador ordenando fuga desesperada ao ser flagrado."
    ),
    20127: (
        "Alto lá! Não vão fugir!",
        "Lyner bloqueando a rota de escape dos rebeldes da Tenba."
    ),
    20128: (
        "Aaaaiii!...\nS-socorro, tenham piedade!",
        "Pesquisador covarde implorando por clemência ao ser encurralado."
    ),
    20129: (
        "Agora desembuchem:\no que vocês estavam aprontando aqui?",
        "Lyner interrogando os cientistas com dureza."
    ),
    20130: (
        "Entendi tudo.\nVocês continuavam os experimentos do Bourd às escondidas,\nnas costas da diretoria da Tenba.",
        "Lyner desvendando a operação ilegal de réplica dos planos de Bourd."
    ),
    20131: (
        "P-por favor!\nNão contem nada para a Presidente Ayano!",
        "Pesquisador suplicando sigilo para não enfrentar a fúria da presidente da corporação."
    ),
    20132: (
        "Ora, ora... vai depender do nosso humor.",
        "Krusche debochando do desespero dos cientistas com ironia afiada."
    ),
    20133: (
        "...",
        "Misha observando o maquinário com olhar pensativo e distante."
    ),
    20134: (
        "Tenham compaixão...\nSe isso vazar, ser demitido vai ser o menor dos nossos problemas...",
        "Cientista temendo punições severas da corporação Tenba."
    ),
    20135: (
        "O-olhem só: se vocês guardarem segredo,\ndeixamos vocês usarem estas instalações sempre que quiserem!...",
        "Cientista tentando subornar o grupo oferecendo acesso irrestrito ao laboratório."
    ),
    20136: (
        "Vocês acham que estão falando com quem?!",
        "Lyner indignado com a tentativa descarada de suborno."
    ),
    20137: (
        "Hiiiiieee!!",
        "Cientista apavorado com a imponência enfurecida de Lyner."
    ),
    20138: (
        "A Misha passou por um verdadeiro pesadelo\npor culpa desse maquinário nefando!\nNão foi, Misha?",
        "Lyner lembrando os traumas provocados pelos experimentos de manipulação corporal em Misha."
    ),
    20139: (
        "...",
        "Misha absorta examinando os painéis do dispositivo."
    ),
    20140: (
        "Misha?",
        "Lyner notando a distração curiosa da garota."
    ),
    20141: (
        "Diga uma coisa...",
        "Misha quebrando o silêncio com uma indagação inesperada."
    ),
    20142: (
        "S-sim?...",
        "Pesquisador assustado respondendo com timidez servil."
    ),
    20143: (
        "Esse equipamento conseguiria me deixar pequena de novo?",
        "Misha revelando seu desejo secreto de regressar à forma infantil."
    ),
    20144: (
        "...Hã?...",
        "Pesquisador embasbacado com o pedido improvável da Reyvateil."
    ),
    20145: (
        "Se não me falha a memória...\nesta máquina consegue separar uma Reyvateil de um Cristal Hymmnos, não consegue?",
        "Misha lembrando a mecânica sonora de separação de cristais que alterou sua maturação."
    ),
    20146: (
        "S-sim... Dá para fazer isso, mas...",
        "Cientista confirmando a funcionalidade teórica do maquinário."
    ),
    20147: (
        "É sério?!\nEntão deixe-me usar essa máquina agora mesmo!",
        "Misha entusiasmada exigindo operar o transformador corporal."
    ),
    20148: (
        "M-Misha?!",
        "Lyner boquiaberto diante da iniciativa repentina da amiga."
    ),
    20149: (
        "Você gosta mais de mim quando eu sou pequenininha,\nnão é, Lyner?",
        "Misha provocando Lyner com afeto dengoso sobre suas preferências visuais."
    ),
    20150: (
        "...O-o quê?! N-não viaja...",
        "Lyner completamente desconsertado gaguejando na resposta."
    ),
    20151: (
        "Por mim tudo bem voltar a ser pequenininha.\nJá não tenho mais onde entoar meu canto mesmo...\nVocê escolhe o que preferir, Lyner.",
        "Misha entregando o controle de sua aparência estética a Lyner sem pudor."
    ),
    20152: (
        "E-escolher o que eu preferir?...\nNão é essa a questão!...",
        "Lyner tentando em vão impor limites lógicos à conversa."
    ),
    20153: (
        "Vai ficar tudo bem.\nA Krusche está de olho neles.\nEles não teriam coragem de aprontar nada.",
        "Misha assegurando que Krusche manterá os cientistas na linha."
    ),
    20154: (
        "S-se for apenas isso,\né moleza, um serviço facílimo!",
        "Cientista aliviado por não ser denunciado à diretoria."
    ),
    20155: (
        "Com certeza!\nP-podem passar por aqui quando quiserem! Hahaha...",
        "Cientista oferecendo a máquina com bajulação e risadas nervosas."
    ),
    20156: (
        "Combinado, conto com vocês.",
        "Misha selando o trato com os pesquisadores da Tenba."
    ),
    20157: (
        "Francamente... Ninguém merece...",
        "Lyner soltando os ombros derrotado pela teimosia charmosa de Misha."
    ),
    20158: (
        "Agora é possível alternar a aparência de Misha.",
        "Notificação do sistema desbloqueando o recurso cosmético de alternância de Misha."
    ),

    # =========================================================================
    # Event/890.evd (IDs 20159-20209): Desaparecimento de Shurelia e Anúncio de Mei Mei
    # =========================================================================
    20159: (
        "...Aí, Lyner, para tudo!\nDeu ruim!!",
        "Krusche alertando aos berros a interrupção da caminhada."
    ),
    20160: (
        "O que houve?!",
        "Lyner reagindo com susto imediato."
    ),
    20161: (
        "A Senhora Shurelia sumiu!",
        "Krusche dando a notícia do sumiço da deusa da Torre."
    ),
    20162: (
        "D-de novo?!",
        "Lyner exasperado com a reincidência de Shurelia em se perder."
    ),
    20163: (
        "Como assim?!\nEla estava colada atrás de mim até agorinha mesmo!",
        "Misha inconformada por tê-la perdido de vista em segundos."
    ),
    20164: (
        "E ela estava andando bem na minha frente há um segundo...",
        "Aurica atestando que Shurelia caminhava logo à sua frente."
    ),
    20165: (
        "Como é que alguém consegue se perder\nestando ensanduichada no meio de vocês duas?!",
        "Jack apontando a impossibilidade física de sumir entre duas pessoas."
    ),
    20166: (
        "Tem razão, mas não seria prudente\nsairmos à procura dela imediatamente?",
        "Radolf propondo busca tática com senso prático e urgência."
    ),
    20167: (
        "Por estas redondezas, existe até o risco\nde ela topar com monstros de alta periculosidade...",
        "Radolf ponderando os perigos de feras agressivas nas imediações."
    ),
    20168: (
        "É, tem razão... Mas se a gente se separar de qualquer jeito,\nnós é que vamos correr perigo...",
        "Lyner avaliando com prudência o perigo de dispersar a equipe."
    ),
    20169: (
        "M-mas que barulho é esse?!",
        "Lyner sobressaltado com a ativação súbita do sistema de som."
    ),
    20170: (
        "Atenção a todos os presentes! Chamada especial da administração!",
        "Mei Mei transmitindo no alto-falante da Torre com tom formal cômico."
    ),
    20171: (
        "Essa voz... não é a da Mei Mei?",
        "Misha reconhecendo o timbre peculiar da atendente da Torre."
    ),
    20172: (
        "Solicita-se a presença do senhor Lyner Barsett,\nresidente de Platina.",
        "Anúncio de som da Torre convocando Lyner pelo nome completo com civilidade."
    ),
    20173: (
        "A ilustríssima Senhora Shurelia o aguarda com urgência.",
        "Mei Mei avisando que Shurelia está esperando no balcão."
    ),
    20174: (
        "A Senhora Shurelia?!",
        "Lyner pasmo ao ouvir o nome da deusa no interfone público."
    ),
    20175: (
        "Favor comparecer com máxima urgência ao balcão da Mei Mei!",
        "Mei Mei finalizando o recado de convocação no sistema da Torre."
    ),
    20176: (
        "Uau~ Quem diria que o observatório\ntinha um sistema de som tão moderno!",
        "Aurica maravilhada com a acústica das instalações tecnológicas do observatório."
    ),
    20177: (
        "...Ninguém merece uma coisa dessas,\nSenhora Shurelia...",
        "Lyner suspirando derrotado pela vergonha pública."
    ),
    20178: (
        "...E agora, o que vai fazer?",
        "Krusche perguntando qual a decisão do líder."
    ),
    20179: (
        "...Não me resta outra escolha, né?",
        "Lyner conformando-se em ir atender ao chamado da deusa desorientada."
    ),
    20180: (
        "Lyner!",
        "Shurelia acenando aliviada ao ver Lyner no balcão."
    ),
    20181: (
        "Senhora Shurelia!\nPor onde a senhora andou zanzando?!",
        "Lyner cobrando explicações da governante da Torre."
    ),
    20182: (
        "Que bom que ele apareceu, Senhora Shurelia!",
        "Mei Mei comemorando o reencontro feliz."
    ),
    20183: (
        "...S-sim.\nMuito obrigada, Mei Mei.",
        "Shurelia agradecendo com timidez sem graça pelo resgate."
    ),
    20184: (
        "...Mudando de assunto...",
        "Mei Mei mudando a entonação para iniciar o sermão."
    ),
    20185: (
        "...A senhora tem ideia de quantas vezes\njá me tirou do sono só porque acabou se perdendo?",
        "Mei Mei reclamando das noites interrompidas pelas desorientações de Shurelia."
    ),
    20186: (
        "Mei Mei! Com sono ou sem sono,\nessa é a sua obrigação aqui, não é?...",
        "Shurelia tentando se defender puxando autoridade hierárquica."
    ),
    20187: (
        "V-você quer dizer que... isso já aconteceu outras vezes?!",
        "Misha chocada ao descobrir o histórico de perdição crônica de Shurelia."
    ),
    20188: (
        "Acontece direto!\nE para piorar, é sempre no momento em que a Mei Mei está morrendo de sono.",
        "Mei Mei expondo a frequência hilária dos incidentes de Shurelia."
    ),
    20189: (
        "...Eu sabia!\nJá tinha achado aquela história mal contada lá no Beco Vagalume.",
        "Krusche conectando os pontos da fuga anterior no distrito comercial."
    ),
    20190: (
        "Eu já me acostumei com a rotina.\nSó que... Senhora Shurelia.",
        "Mei Mei apelando para o bom senso da mestra ancestral."
    ),
    20191: (
        "...Diga.",
        "Shurelia encolhida aguardando o julgamento da funcionária."
    ),
    20192: (
        "Eu já venho repetindo isso há centenas de anos:\njá passou da hora de a senhora aprender a andar pela Torre!",
        "Mei Mei dando bronca milenar sobre o senso de orientação nulo da deusa."
    ),
    20193: (
        "C-centenas de anos?!...\nEla já faz isso há tanto tempo assim?!",
        "Lyner estarrecido com a escala secular das trapalhadas de Shurelia."
    ),
    20194: (
        "Compreenda que mapear com exatidão uma Torre\nque muda de configuração a cada instante é uma tarefa hercúlea, sabia?",
        "Shurelia justificando suas perambulações pela natureza mutável dos pilares da Torre."
    ),
    20195: (
        "...Bom, a Senhora Shurelia tem razão em parte:\nresgatá-la também faz parte do meu expediente.",
        "Mei Mei cedendo com complacência ao argumento."
    ),
    20196: (
        "É... obrigado pelo empenho.\nVocê quebrou um galho enorme para nós, Mei Mei.",
        "Lyner agradecendo a paciência e eficiência da guardiã do anteparo."
    ),
    20197: (
        "De nada, de nada!\nComo foi a primeira vez que usei o interfone da Torre,\na Mei Mei até que se divertiu bastante.",
        "Mei Mei contente por experimentar o microfone geral da Torre."
    ),
    20198: (
        "Ahaha! A Senhora Shurelia é uma perdida de primeira linha!\nNão tem a menor noção de direção!",
        "Aurica gargalhando da fofura desastrada da protetora sagrada."
    ),
    20199: (
        "E-ei, Aurica...\nNão precisava jogar na cara desse jeito...",
        "Lyner pedindo moderação para não ferir o orgulho divino da Senhora Shurelia."
    ),
    20200: (
        "Pois é, parece que sim...\nAurica, conto com o seu apoio de agora em diante.",
        "Shurelia aceitando sua deficiência de orientação e pedindo a escolta de Aurica."
    ),
    20201: (
        "Pode deixar comigo!\nVamos, Lyner, hora de partir!",
        "Aurica assumindo o papel de guia oficial com entusiasmo contagiante."
    ),
    20202: (
        "É, vamos lá...\nFrancamente, esses sustos ainda acabam com o meu coração.",
        "Lyner recuperando o fôlego após o estresse do sumiço da divindade."
    ),
    20203: (
        "Mas tenho que admitir:\nelas estão formando uma duplinha até que bem afinada...",
        "Misha observando com carinho a cumplicidade nascente entre Aurica e Shurelia."
    ),
    20204: (
        "Senhora Shurelia, essa desculpa aí não colou nada, viu?~",
        "Mei Mei cutucando Shurelia em tom zombeteiro."
    ),
    20205: (
        "......",
        "Shurelia emudecida fingindo não ouvir a alfinetada de Mei Mei."
    ),
    20206: (
        "Eu preferia não ter que admitir isso, mas...",
        "Jack preparando o diagnóstico impiedoso."
    ),
    20207: (
        "Falando com toda a seriedade...\nEla deve ser uma desligada nata...",
        "Radolf decretando com solenidade e estoicismo que Shurelia é uma avoada de nascença."
    ),
    20208: (
        "......",
        "Shurelia sustentando o olhar com pose de estátua sem piscar."
    ),
    20209: (
        "Sim. Eu estava apenas fazendo uma pequena...\nmanutenção nos aparelhos do observatório...",
        "Shurelia tentando resgatar sua dignidade divina com desculpa esfarrapada e deadpan sublime."
    )
}

print(f"Total curated lines defined: {len(curated_data)}")

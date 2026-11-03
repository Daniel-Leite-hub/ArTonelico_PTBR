# -*- coding: utf-8 -*-
"""
build_and_validate_073.py - Gera e valida estritamente o bloco BLK_EVD_073_output.json
"""
import sys
import os
import json
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_073_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_073_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Dicionário de traduções curadas e notas por ID
CURATED_DATA = {
    # Event/232.evd (16558 a 16590)
    16558: {
        "text": "Ei, Lyner.\nQue tal a gente dar um pulo no parque?",
        "notes": "Misha convida Lyner casualmente para espairecer no parque urbano de Karff durante a tempestade."
    },
    16559: {
        "text": "Que vento gostoso, né?\nSerá porque a tempestade tá soprando\nmais forte do que o costume?",
        "notes": "Misha comenta com leveza a intensidade agradável da ventania trazida pela tempestade."
    },
    16560: {
        "text": "Eu preciso dar um jeito de chegar logo\nao Beco Vagalume...",
        "notes": "Lyner demonstra inquietação e afobação para resgatar Claire no Beco Vagalume."
    },
    16561: {
        "text": "Lyner...\nVocê não tá afobado demais, não?",
        "notes": "Misha repreende carinhosamente a afobação evidente de Lyner (焦り過ぎ)."
    },
    16562: {
        "text": "Hã?...\nVocê acha?",
        "notes": "Lyner reage surpreso ao perceber que sua afobação está visível."
    },
    16563: {
        "text": "Acho, sim. Quando você se afoba, Lyner,\nisso transparece na hora no que fala e faz.",
        "notes": "Misha aponta que o nervosismo de Lyner transparece de imediato em suas palavras e atitudes."
    },
    16564: {
        "text": "Foi a mesma coisa quando estávamos\nvoltando a Platina para combater os vírus.",
        "notes": "Misha recorda o mesmo comportamento afobado na jornada anterior a Platina."
    },
    16565: {
        "text": "......",
        "notes": "Lyner silencia reflexivo e sem argumentos diante da constatação de Misha."
    },
    16566: {
        "text": "Tem horas em que não adianta nada se afobar.\nNum momento desses,\no melhor que você faz é se divertir e pronto!",
        "notes": "Misha defende que em momentos de impasse a melhor saída é descontrair e descansar a mente."
    },
    16567: {
        "text": "Eu não posso fazer isso agora!",
        "notes": "Lyner recusa impulsivamente a ideia de relaxar em meio à crise."
    },
    16568: {
        "text": "Lyner...\nSempre puro e obstinado... Sempre com esse mesmo\ncoração sincero de menino.",
        "notes": "Misha descreve com ternura a pureza obstinada e juvenil de Lyner (純心で一途な)."
    },
    16569: {
        "text": "Eu gosto demais desse seu jeito, sabia?",
        "notes": "Misha expressa carinho pelo idealismo de Lyner, removendo a rubrica teatral indevida da NISA (*giggle*)."
    },
    16570: {
        "text": "Mas escuta: quando for hora de descansar, descanse.\nSenão... você vai acabar perdendo o controle de si.",
        "notes": "Misha adverte que a privação de descanso leva à perda de autocontrole físico e emocional."
    },
    16571: {
        "text": "...É...",
        "notes": "Lyner concorda timidamente e reconhece a sabedoria do conselho."
    },
    16572: {
        "text": "Eu... fico tão preocupada com você...\nCom tanto medo...",
        "notes": "Misha confessa a dor e o medo constante de ver Lyner se desgastar até o colapso."
    },
    16573: {
        "text": "Vendo você daquele jeito agora há pouco...\neu fiquei apavorada, quase chorei... Por isso...",
        "notes": "Misha revela que quase chorou de pavor ao ver Lyner à beira do descontrole emocional."
    },
    16574: {
        "text": "Me desculpa...\nEu só estava tentando ajudar a Claire...",
        "notes": "Lyner pede desculpas cabisbaixo, explicando que sua intenção era apenas socorrer Claire."
    },
    16575: {
        "text": "Eu sei. Mas, no fim das contas,\na Claire acabou sofrendo com isso.",
        "notes": "Misha pontua a consequência amarga das ações precipitadas de Lyner, sem afetação."
    },
    16576: {
        "text": "Talvez houvesse outro caminho,\nnão acha?",
        "notes": "Misha sugere com delicadeza que existiam alternativas menos destrutivas."
    },
    16577: {
        "text": "......",
        "notes": "Lyner acusa o golpe e permanece em silêncio culpado."
    },
    16578: {
        "text": "Pronto!\nChega de papo difícil!",
        "notes": "Misha corta a conversa pesada com energia extrovertida (よし! 難しい話はおしまい!)."
    },
    16579: {
        "text": "Ei, vamos às compras!\nJá que sobrou um tempinho livre!",
        "notes": "Misha convida Lyner para fazer compras aproveitando a pausa forçada da tempestade."
    },
    16580: {
        "text": "O quê?! M-mas isso é...",
        "notes": "Lyner gagueja perplexo diante da mudança brusca de assunto."
    },
    16581: {
        "text": "E você prefere fazer o quê?!\nFicar enfurnado no quarto remoendo a afobação\nenquanto espera a tempestade passar?",
        "notes": "Misha questiona a inércia de ficar remoendo ansiedade dentro do quarto."
    },
    16582: {
        "text": "Lyner, você precisa arejar a cabeça...\nDe vez em quando a gente tem que brincar\ne descontrair a valer!",
        "notes": "Misha defende a necessidade de mudar de ares (気分転換) e brincar sem culpas."
    },
    16583: {
        "text": "Tudo bem que eu também quero me divertir\num pouquinho, mas...",
        "notes": "Misha admite com charme tsundere que ela própria também deseja espairecer."
    },
    16584: {
        "text": "Hã?!",
        "notes": "Lyner reage atônito à confissão travessa da amiga."
    },
    16585: {
        "text": "Bora logo!",
        "notes": "Misha puxa Lyner animadamente em direção ao centro comercial."
    },
    16586: {
        "text": "Vamos lá!\nEu vou comprar de tudo até cansar!",
        "notes": "Misha celebra com entusiasmo gastador (じゃんじゃん買うわよ!)."
    },
    16587: {
        "text": "Ei, ei, não temos tempo\npara brincadeiras agora, sabiam?",
        "notes": "Jack intervém com pragmatismo de mercenário calejado para conter a euforia infantil."
    },
    16588: {
        "text": "Poxa, até você falando isso, Harm-da!\nSe a gente não se divertir numa hora dessas,\nquando é que vai se divertir?!",
        "notes": "Misha reclama em bico usando o diminutivo afetuoso de infância 'Harm-da' (アル兄ぃ)."
    },
    16589: {
        "text": "Quanta despreocupação...\nEu vou é colher algumas informações por aí.",
        "notes": "Jack ironiza a leviandade da dupla e parte para investigar o terreno por conta própria."
    },
    16590: {
        "text": "Jack deixou o grupo.",
        "notes": "Mensagem de sistema notificando a saída temporária de Jack da equipe ativa."
    },

    # Event/730.evd (16591 a 16650)
    16591: {
        "text": "É nesta mansão que dizem estar o livro para ficar inteligente?...\nN-nossa, parece bem mais assustadora do que eu imaginava...",
        "notes": "Aurica expressa espanto tímido diante do casarão sombrio na Cosmosfera."
    },
    16592: {
        "text": "Eu não te avisei para desistir?\nVamos dar meia-volta, vai?",
        "notes": "Lyner tenta dissuadir Aurica de explorar o local lúgubre."
    },
    16593: {
        "text": "Não, de jeito nenhum!\nConseguir esse livro é a minha única saída\npara sobreviver neste mundo!",
        "notes": "Aurica insiste desesperada em sua busca pelo compêndio de inteligência para não ser descartada."
    },
    16594: {
        "text": "Vamos, vem!",
        "notes": "Aurica toma coragem e avança para dentro da biblioteca."
    },
    16595: {
        "text": "E-ei, Aurica!\nAi, ai... Não tem jeito mesmo, né...",
        "notes": "Lyner suspira conformado e segue os passos da donzela."
    },
    16596: {
        "text": "Ei, aqui parece uma biblioteca, não acha?\nVamos procurar aquele livro!",
        "notes": "Aurica identifica a sala de arquivos (書庫) e incita a busca pelo volume."
    },
    16597: {
        "text": "Será que um livro desses existe de verdade...?",
        "notes": "Lyner duvida com razão da existência de uma fórmula mágica para a sabedoria."
    },
    16598: {
        "text": "Existe com certeza...\nAchei!! É este aqui!",
        "notes": "Aurica localiza triunfante a obra misteriosa nas estantes."
    },
    16599: {
        "text": "Olha só!\n[Método de Desenvolvimento do Potencial Oculto:\nA Arte Secreta Dominada em 3 Minutos]!",
        "notes": "Aurica lê com júbilo o título bizarro do compêndio de autoajuda mágica."
    },
    16600: {
        "text": "Nossa, que troço mais suspeito...",
        "notes": "Lyner reage com estranhamento e ceticismo ao título apelativo."
    },
    16601: {
        "text": "Lê comigo, Lyner?\nÉ que... tá difícil demais, não consigo entender nada...",
        "notes": "Aurica confessa com vergonha sua incapacidade de decifrar o texto técnico do livro."
    },
    16602: {
        "text": "Hã?... É sério isso?\nFazer o quê, deixa eu ver...",
        "notes": "Lyner atende resignado ao pedido de leitura de Aurica."
    },
    16603: {
        "text": "Vejamos...\n\"O potencial oculto é um mundo desconhecido\nque reside em você, ignorado por si mesmo.\"",
        "notes": "Lyner começa a ler em voz alta a introdução pseudocientífica da obra."
    },
    16604: {
        "text": "\"Diz-se que tal potencial é capaz de despertar\nmais de dez vezes a força que você possui atualmente.\"",
        "notes": "O livro promete uma multiplicação decuplicada de capacidades físicas e mágicas."
    },
    16605: {
        "text": "\"Ao desenvolver o potencial oculto, você tirará nota cem\nnas provas, terá reflexos atléticos impecáveis\ne nunca mais se atrasará três dias seguidos...\"",
        "notes": "A lista cômica de benefícios mundanos reflete as neuroses escolares infantis de Aurica."
    },
    16606: {
        "text": "Que exemplos estranhamente específicos...",
        "notes": "Aurica nota desconcertada a especificidade prosaica das promessas do livro."
    },
    16607: {
        "text": "Bem... até dá para imaginar o porquê.\nMas vamos continuar lendo.",
        "notes": "Lyner compreende intuitivamente que o livro foi moldado pelo subconsciente dela e prossegue."
    },
    16608: {
        "text": "\"Para fazer desabrochar seu potencial,\né necessário absorver energia diretamente da torre\nno centro do mundo.\"",
        "notes": "A tese do livro prescreve a extração crua de energia da Torre Ar tonelico."
    },
    16609: {
        "text": "\"A torre no centro do mundo funciona como um duto\npara canalizar energia do potencial oculto\naté o seu cotidiano.\"",
        "notes": "O livro descreve a Torre como um gasoduto/duto que conecta o potencial ao consciente."
    },
    16610: {
        "text": "\"Contudo, essa força acaba represada no meio do caminho\npor fatores diversos.\"",
        "notes": "A obra explica que o fluxo de energia sofre bloqueios ao longo da transmissão."
    },
    16611: {
        "text": "\"Sendo assim, a ideia é puxar a força direto da torre\nantes que seja represada! Em suma:\né passar a mão na energia alheia.\"",
        "notes": "O texto resume a teoria de forma descarada com o termo popular 'energia desviada / passar a mão' (ネコババ)."
    },
    16612: {
        "text": "...Que livro mais absurdo...",
        "notes": "Lyner embasbaca-se com o cinismo do autor daquele manual."
    },
    16613: {
        "text": "Mas pelo menos deu para entender\nque a gente precisa ir até a \"Torre\", né?",
        "notes": "Aurica extrai a instrução prática de dirigir-se à Torre mental da Cosmosfera."
    },
    16614: {
        "text": "É verdade. Quer ir até lá agora?",
        "notes": "Lyner aceita prontamente acompanhar a moça até a estrutura central."
    },
    16615: {
        "text": "Hã? Você vai comigo até a Torre?",
        "notes": "Aurica surpreende-se com a solicitude protetora de Lyner."
    },
    16616: {
        "text": "Ué, claro que vou.\nNão posso deixar você ir sozinha,\nnunca se sabe o que pode acontecer lá...",
        "notes": "Lyner reforça seu zelo leal de guardião, recusando deixá-la desprotegida."
    },
    16617: {
        "text": "...Obrigada.\nVocê é tão gentil, Lyner...",
        "notes": "Aurica comove-se com a generosidade afetuosa do rapaz."
    },
    16618: {
        "text": "Ah, se você lesse livros para mim assim sempre,\ntenho certeza de que meus estudos renderiam tanto...",
        "notes": "Aurica expressa o anseio romântico de ter a presença constante de Lyner em seus estudos."
    },
    16619: {
        "text": "Será?\nLer por conta própria costuma fixar bem melhor.",
        "notes": "Lyner responde com ingenuidade prática sobre métodos de aprendizado."
    },
    16620: {
        "text": "Não é isso que eu quis dizer...\nÉ que... se eu pudesse estudar com você...",
        "notes": "Aurica tenta explicar sem jeito seu desejo íntimo de cumplicidade amorosa."
    },
    16621: {
        "text": "Perdoem a intromissão repentina, jovem dama e nobre rapaz.\nPermitem-me uma palavrinha?",
        "notes": "A figura encapuzada e misteriosa surge educadamente nos corredores do casarão."
    },
    16622: {
        "text": "Quem tá aí?!",
        "notes": "Aurica sobressalta-se com a voz desconhecida que ecoa na biblioteca."
    },
    16623: {
        "text": "Veio do corredor!",
        "notes": "Lyner localiza a origem fônica do chamado nos corredores escuros."
    },
    16624: {
        "text": "Ora, ora, minhas sinceras desculpas pelo susto.\nChamam-me de ???, ao vosso inteiro dispor.",
        "notes": "O indivíduo misterioso desculpa-se formalmente mantendo o anonimato de sua identidade."
    },
    16625: {
        "text": "Por acaso você é o dono desta mansão?!",
        "notes": "Lyner interroga o interlocutor supondo tratar-se do proprietário da edificação."
    },
    16626: {
        "text": "Não, longe de mim tamanha presunção.\nSou o Guia do Fluxo, o condutor da jovem senhorita.",
        "notes": "O homem revela seu título canônico de 'Guia do Fluxo' (ナガレの水先案内人), suprimido pela NISA."
    },
    16627: {
        "text": "M-meu condutor...?",
        "notes": "Aurica gagueja intrigada ao descobrir que possui um mentor naquele nível mental."
    },
    16628: {
        "text": "Exatamente. Vim transmitir-lhe um recado de suma importância:\nnão há nada de bom a colher roubando o poder da Torre.",
        "notes": "O Guia adverte com sobriedade que saquear energia da Torre mental só trará desgraça."
    },
    16629: {
        "text": "Existe um caminho muito mais seguro:\nderrotar o gato que espreita diante da Torre.",
        "notes": "O mentor orienta a eliminar o gato sentinela que bloqueia o acesso à Torre."
    },
    16630: {
        "text": "Um gato...?! Tem um gato na frente da Torre...?",
        "notes": "Aurica estranha a existência de um felino montando guarda perante a Torre."
    },
    16631: {
        "text": "...Precisamente. Um felino bastante peculiar.\nÉ ele quem vive drenando o poder mágico da senhorita.",
        "notes": "O Guia elucida que o animal estranho funciona como um parasita que suga o poder de Aurica."
    },
    16632: {
        "text": "Eis a razão pela qual seus estudos não avançam,\nimpossibilitando-a de manifestar uma magia poderosa.",
        "notes": "Correção crítica do erro de inversão da NISA, explicitando a incapacidade de conjurar magias fortes."
    },
    16633: {
        "text": "Como assim...?! Quem foi que fez uma maldade dessas?!",
        "notes": "Aurica revolta-se estarrecida contra o responsável por sua limitação mágica crônica."
    },
    16634: {
        "text": "Foi a senhorita mesma.\nUm \"limite\" imposto por sua própria mente.",
        "notes": "O Guia profere a revelação psicológica capital: o gato é um constructo onírico de autoimposição (制限)."
    },
    16635: {
        "text": "Sendo assim, peço vossa licença para me retirar.\nPassai muito bem...",
        "notes": "O Guia despede-se com cortesia cerimoniosa e desvanece no ar."
    },
    16636: {
        "text": "Um felino...? Um \"limite\" que eu mesma impus...?",
        "notes": "Aurica balbucia perturbada com a constatação de que seu próprio medo a acorrentava."
    },
    16637: {
        "text": "Seja como for, vamos até a Torre ver isso.",
        "notes": "Lyner toma a dianteira pragmática e propõe investigar o local imediatamente."
    },
    16638: {
        "text": "Aquele sujeito mascarado não me sai da cabeça...\nEi, Donsuke, você por acaso conhece um cara\ncom manto cheio de olhos desenhados?",
        "notes": "Lyner consulta Don Leon sobre a identidade da aparição mascarada com túnica de olhos."
    },
    16639: {
        "text": "Ora, quem saberá? Eu cá não estava espiando,\nnão há como este servo adivinhar só por isso.",
        "notes": "Don Leon responde em sua afetação samurai tradicional, corrigindo o deboche inventado pela NISA."
    },
    16640: {
        "text": "Mas uma coisa é certa: foi algo tecido pela mente da Senhorita Aurica.\nMais cedo ou mais tarde você compreenderá a razão.",
        "notes": "O guardião samurai atesta a gênese psíquica da figura e recomenda paciência investigativa."
    },
    16641: {
        "text": "...Ué?\nEste livro... não consigo entender nada do que tá escrito.",
        "notes": "Lyner tenta reabrir o livro e depara-se com caracteres indecifráveis."
    },
    16642: {
        "text": "Como assim?! Nem você consegue ler, Lyner?!",
        "notes": "Aurica assusta-se com o súbito analfabetismo funcional do companheiro."
    },
    16643: {
        "text": "Não dá...\nNão é bem não conseguir ler... é como se não me deixassem ler...\nQue sensação mais esquisita é essa...?",
        "notes": "Lyner descreve a barreira perceptiva imposta pela psique de Aurica que bloqueia sua leitura."
    },
    16644: {
        "text": "Chega! Pára de dar desculpas!\nVocê simplesmente não sabe ler, não é?!\nFui uma boba de ter contado com a sua ajuda!",
        "notes": "Aurica interpreta a falha como pretexto desdenhoso, tem um acesso de fúria e ataca Lyner verbalmente."
    },
    16645: {
        "text": "Deixa que agora eu me viro sozinha!\nPassar bem...!",
        "notes": "Consumida pela vergonha e pela desconfiança, Aurica bate em retirada abandonando Lyner."
    },
    16646: {
        "text": "E-ei! Espera aí, Aurica!\nFicou tudo num breu total, não enxergo nada...",
        "notes": "Com a saída abrupta de Aurica, o mundo onírico mergulha em trevas completas em torno de Lyner."
    },
    16647: {
        "text": "Ei!!\nTem alguém aí?! Alguém me tira daqui...!",
        "notes": "Lyner clama desesperado por socorro no vácuo escuro do subconsciente."
    },
    16648: {
        "text": "Tem alguém ouvindo...?",
        "notes": "A voz de Lyner esvanece em eco solitário e desamparado."
    },
    16649: {
        "text": "Pelo visto a Senhorita Aurica pegou ranço de vós.\nNão conseguir ler o livro é fruto da rejeição inconsciente dela:\nprova cabal de que ainda não confia em vós.",
        "notes": "Don Leon diagnostica a mecânica da Cosmosfera: a ilegibilidade é sintoma da desconfiança latente de Aurica."
    },
    16650: {
        "text": "Pois bem, trate de se esforçar mais da próxima vez.",
        "notes": "Don Leon conclui com conselho estoico para que Lyner reconstrua a ponte afetiva com a mestra."
    },

    # Event/145.evd (16651 a 16766)
    16651: {
        "text": "...Ué? É a Aurica...",
        "notes": "Lyner avista Aurica cantando ao entardecer à beira do precipício de Karff."
    },
    16652: {
        "text": "Entoem~ os cantos de Gaia~...\nRessoando pelos céus da criação~...",
        "notes": "Aurica entoa versos sacros e melancólicos da liturgia de Elemia dedicados a Gaia."
    },
    16653: {
        "text": "Que voz mais linda...",
        "notes": "Lyner aproxima-se comovido com a pureza e a beleza da interpretação vocal da Reyvateil."
    },
    16654: {
        "text": "Lyner!?",
        "notes": "Aurica interrompe o cântico envergonhada ao ser flagrada pelo cavaleiro."
    },
    16655: {
        "text": "Você sempre costuma cantar por aqui?",
        "notes": "Lyner indaga com carinho sobre os hábitos de treino musical de Aurica."
    },
    16656: {
        "text": "...É que eu canto muito mal.\nPreciso treinar bastante...",
        "notes": "Aurica desvia o olhar com modéstia dolorosa e autodepreciação crônica."
    },
    16657: {
        "text": "Que nada, não é verdade...\nA canção de agora há pouco foi muito bonita.",
        "notes": "Lyner refuta a insegurança da donzela elogiando com franqueza seu desempenho."
    },
    16658: {
        "text": "Não... não precisa me consolar.\nNinguém no mundo precisa das minhas canções...",
        "notes": "Aurica lamenta com amargura a sensação de inutilidade e rejeição que carrega desde a infância."
    },
    16659: {
        "text": "Eu não sou como a mana Claire...\nNinguém precisa de mim como precisam dela...",
        "notes": "Aurica compara-se com sofrimento à sua irmã de criação Claire (クレアお姉ちゃん)."
    },
    16660: {
        "text": "Além do mais, vivo atrapalhando todo mundo...\nSó sei causar transtornos...",
        "notes": "Aurica martiriza-se lembrando dos erros e tropeços cometidos nas missões."
    },
    16661: {
        "text": "......",
        "notes": "Lyner ouve em silêncio compassivo, sentindo o peso da dor oculta no peito da parceira."
    },
    16662: {
        "text": "Você e a Claire são amigas de infância, não é?",
        "notes": "Lyner busca compreender as raízes do vínculo afetivo entre Aurica e Claire."
    },
    16663: {
        "text": "...Sim. Ao contrário de mim,\na mana Claire é capaz de fazer qualquer coisa.",
        "notes": "Aurica descreve a admiração e o complexo de inferioridade perante os talentos múltiplos de Claire."
    },
    16664: {
        "text": "Assim como na apresentação de hoje...\ntodo mundo admira ela, todo mundo precisa dela.",
        "notes": "Aurica rememora a aclamação calorosa que Claire recebeu no concerto de Karff."
    },
    16665: {
        "text": "Eu até entrei para a Igreja e dei o meu melhor\npara ser candidata a Donzela Sagrada, mas...",
        "notes": "Aurica recorda seu esforço desmedido nos templos clericais de Elemia para ser reconhecida."
    },
    16666: {
        "text": "Por ter baixa aptidão e ser apenas Classe D,\nnenhum cavaleiro quis ser meu parceiro.",
        "notes": "Aurica revela a humilhação de ter sido preterida por todos os guerreiros por sua classificação biológica."
    },
    16667: {
        "text": "Por isso, quando o Bispo me deu ordens\npara participar da missão na Colina do Canto...\neu fiquei tão feliz...",
        "notes": "Aurica relembra a convocação do Bispo Falss para a missão sagrada na Colina do Canto (謳う丘)."
    },
    16668: {
        "text": "Porque senti que finalmente\nalguém precisava de mim...",
        "notes": "Aurica confessa o alívio que sentiu ao acreditar que finalmente tinha algum valor no mundo."
    },
    16669: {
        "text": "Mas é claro.\nVocê é indispensável para mim, Aurica.",
        "notes": "Lyner intervém com convicção e firmeza heroica, afirmando o valor insubstituível dela."
    },
    16670: {
        "text": "Na Colina do Canto, quando a ponte ia desabar\ne eu quase caí... você me salvou com sua Magia da Canção.",
        "notes": "Lyner recorda o salvamento milagroso operado por Aurica quando ele quase despencou no abismo."
    },
    16671: {
        "text": "...Aquela magia esquisita...\nAi, que vergonha...",
        "notes": "Aurica cora envergonhada ao lembrar da forma cômica de sua primeira Magia da Canção."
    },
    16672: {
        "text": "Mas é que eu só consigo conjurar\nmagias esquisitas assim...",
        "notes": "Aurica lamenta com biquinho fofo sua incapacidade de conjurar magias visualmente gloriosas."
    },
    16673: {
        "text": "Que nada, aquilo me salvou a vida.\nGraças àquela magia, a minha base não caiu.",
        "notes": "Lyner ressalta que a utilidade e a proteção da magia foram vitais para sua sobrevivência."
    },
    16674: {
        "text": "Mentira!!",
        "notes": "Aurica reage incrédula achando que Lyner está zombando dela carinhosamente."
    },
    16675: {
        "text": "É sério! Ela continua firme lá até agora.\nSe não fosse por você, eu estaria morto.",
        "notes": "Lyner jura com sinceridade que sem a intervenção oportuna dela teria perecido nas ruínas."
    },
    16676: {
        "text": "Não fica mais deprimida, vai.\nEu nunca achei que você fosse um fardo...",
        "notes": "Lyner conforta a parceira, desmantelando sua culpa e seu pavor crônico de atrapalhar o grupo."
    },
    16677: {
        "text": "Lyner...\nPor que você é tão gentil comigo?",
        "notes": "Aurica pergunta com olhar vulnerável e voz trêmula, desarmada pela bondade dele."
    },
    16678: {
        "text": "...Hã?\nIsso é o normal... qualquer um faria o mesmo.",
        "notes": "Lyner desconversa com modéstia honesta, considerando seu afeto a coisa mais natural do mundo."
    },
    16679: {
        "text": "Não é, não...\nVocê, Lyner...",
        "notes": "Aurica insiste que a nobreza de espírito de Lyner transcende qualquer gentileza comum."
    },
    16680: {
        "text": "......",
        "notes": "Lyner fita os olhos marejados de Aurica sob a brisa noturna."
    },
    16681: {
        "text": "......Você é gentil de verdade.",
        "notes": "Aurica sela seu reconhecimento de gratidão e carinho profundo por Lyner."
    },
    16682: {
        "text": "Haa... haa...\nNão adianta, não importa quantos a gente derrote,\neles não param de vir...!",
        "notes": "Transição para Platina: a donzela de guarda arfa exausta sob o cerco implacável dos vírus."
    },
    16683: {
        "text": "Você tá bem?!\nJá cantou demais por hoje... Recue e descanse!",
        "notes": "O comandante dos Cavaleiros ordena que a Reyvateil esgotada recue para preservar a vida."
    },
    16684: {
        "text": "...Obrigada, mas eu ainda aguento!\nMais importante agora é defender Platina!",
        "notes": "A guerreira clerical recusa o descanso e mantém sua canção defensiva para salvar a cidade flutuante."
    },
    16685: {
        "text": "Malditos vírus...\nEstão controlando os Guardiões a bel-prazer!",
        "notes": "O cavaleiro amaldiçoa a corrupção cibernética dos autômatos de defesa de Platina."
    },
    16686: {
        "text": "Alerta de emergência!\nA rede de defesa da passagem para Platina foi rompida...!",
        "notes": "A sentinela anuncia o colapso catastrófico da barreira de contenção do corredor urbano."
    },
    16687: {
        "text": "C-como é que é?!",
        "notes": "O oficial reage atônito à queda das defesas primárias da metrópole divina."
    },
    16688: {
        "text": "Capitão! Más notícias!\nOs vírus no Altar dos Apóstolos estão agindo de forma anômala!",
        "notes": "O sentinela relata perturbações energéticas inéditas no recinto sagrado do Altar dos Apóstolos."
    },
    16689: {
        "text": "...O quê?!",
        "notes": "O comandante teme o pior diante da movimentação suspeita dos vírus ancestrais."
    },
    16690: {
        "text": "Qual é a situação dos vírus?",
        "notes": "Senhora Shurelia entra em cena com compostura solene para assumir o comando da crise."
    },
    16691: {
        "text": "Eles ergueram uma barreira de força colossal!",
        "notes": "O soldado reporta a formação de um campo de força opaco em torno do Altar."
    },
    16692: {
        "text": "...Uma barreira?",
        "notes": "Shurelia estranha a natureza defensiva adotada pelos vírus invasores."
    },
    16693: {
        "text": "Só de chegar perto já dá náuseas...\nSem dúvida é uma emanação de energia avassaladora!",
        "notes": "A Reyvateil alerta para a toxicidade e a magnitude fônica avassaladora da barreira."
    },
    16694: {
        "text": "...Isso é preocupante.\nDepressa, ao Altar dos Apóstolos!",
        "notes": "Shurelia pressente o perigo iminente e lidera a marcha imediata ao santuário."
    },
    16695: {
        "text": "Sim, Senhora!",
        "notes": "A guarda clerical responde em prontidão marcial à ordem da deusa tutelar."
    },
    16696: {
        "text": "...Não pode ser!",
        "notes": "Shurelia estaca perplexa diante do que testemunha no coração do Altar."
    },
    16697: {
        "text": "Quanto tempo, Shurelia......",
        "notes": "A voz espectral e sedutora de Mir ressoa dos vórtices da barreira após séculos de confinamento."
    },
    16698: {
        "text": "Essa voz...",
        "notes": "Shurelia reconhece o timbre inconfundível de sua irmã primordial de criação."
    },
    16699: {
        "text": "Depois de tanto tempo...\neu finalmente consegui sair para o exterior...\nEmbora ainda seja apenas a minha \"voz\"...",
        "notes": "Mir comemora com ironia mordaz sua libertação fônica parcial através do campo de força."
    },
    16700: {
        "text": "Senhora Shurelia!?...\nO que significa isto...?!",
        "notes": "O capitão apavora-se com a emanação hostil que abala o santuário de Platina."
    },
    16701: {
        "text": "Você finalmente adquiriu poder para se manifestar...\nMir...",
        "notes": "Shurelia constata com pesar e gravidade o avanço na corporificação do vírus primordial."
    },
    16702: {
        "text": "Sim... Muito grata por perguntar...",
        "notes": "Mir responde com deboche cortês e veneno afável (お陰様で)."
    },
    16703: {
        "text": "Não sei quanto tempo se passou desde então...\nmas vejo que você continua a mesma de sempre.",
        "notes": "Mir zomba da imutabilidade moral e da ingenuidade preservada por Shurelia através dos séculos."
    },
    16704: {
        "text": "...Por que você insiste em ficar do lado dos humanos?",
        "notes": "Mir questiona com desprezo visceral a aliança protetora de Shurelia com a raça humana."
    },
    16705: {
        "text": "Seres covardes, débeis e efêmeros que, por isso mesmo,\ntornam-se selvagens e devoram o mundo...\nO verdadeiro vírus... a humanidade.",
        "notes": "Mir expõe seu manifesto de ódio ontológico contra a humanidade predatória."
    },
    16706: {
        "text": "Está errada!\nOs humanos não são assim!",
        "notes": "Shurelia ergue a voz divina com indignação para defender a dignidade e o valor humanos."
    },
    16707: {
        "text": "Fufu...\nExatamente como naquele tempo...\nVocê sempre foi ingênua desse jeito.",
        "notes": "Mir ri desdenhosa da fidelidade inabalável de Shurelia à sua fé na coexistência pacífica."
    },
    16708: {
        "text": "......",
        "notes": "Shurelia mantém-se em guarda silenciosa perante o escárnio da irmã corrompida."
    },
    16709: {
        "text": "Sabe... eu decidi que já é hora\nde realizar o meu sonho.",
        "notes": "Mir anuncia a deflagração da fase executiva de seu plano milenar."
    },
    16710: {
        "text": "E para que isso aconteça,\na sobrevivência dos humanos só atrapalha...",
        "notes": "Mir decreta com frieza homicida a necessidade de aniquilar a espécie humana."
    },
    16711: {
        "text": "Uaaagh!!",
        "notes": "O comandante é fulminado por uma descarga de plasma desferida pela barreira."
    },
    16712: {
        "text": "O que está fazendo?!",
        "notes": "Shurelia clama enfurecida contra o ataque traiçoeiro perpetrado contra seu cavaleiro."
    },
    16713: {
        "text": "Aaaah! Capitão!!",
        "notes": "A jovem Reyvateil grita em desespero ao ver o oficial tombar gravemente ferido."
    },
    16714: {
        "text": "Que crueldade!...\nPor que fazer uma atrocidade dessas...?!",
        "notes": "A sentinela acusa Mir entre lágrimas pela violência desmedida contra um homem indefeso."
    },
    16715: {
        "text": "Minha doce filhinha, não fique tão zangada...\nTudo o que faço é pelo bem de vocês...",
        "notes": "Mir assume tom maternal perverso com a Reyvateil clerical, proclamando agir em prol de sua linhagem."
    },
    16716: {
        "text": "...O que você tá dizendo...?",
        "notes": "A donzela recua horrorizada diante da manipulação afetiva do vírus ancestral."
    },
    16717: {
        "text": "Vou erradicar a humanidade inteira\ne conceber uma utopia exclusiva para as Reyvateils...",
        "notes": "Mir explicita o cerne de sua ideologia: genocídio humano para fundar um paraíso lírico puro."
    },
    16718: {
        "text": "Não pode ser...\nEu não quero um mundo desses de jeito nenhum!!",
        "notes": "A Reyvateil de Platina rejeita com veemência e asco o paraíso sanguinário oferecido por Mir."
    },
    16719: {
        "text": "...Não permitirei que profane a Torre nem mais um segundo!",
        "notes": "Shurelia desembainha sua autoridade suprema para repelir a profanação do sistema de Sol Ciel."
    },
    16720: {
        "text": "Fufufu. Não vai permitir? E o que pretende fazer?\nEu sou muito mais \"rápida\" do que você.",
        "notes": "Mir tripudia da lentidão dos protocolos da deusa, gabando-se de sua velocidade de propagação."
    },
    16721: {
        "text": "...!!",
        "notes": "Shurelia sobressalta-se ao perceber o disparo de um comando de script prioritário."
    },
    16722: {
        "text": "Isto não passa do prelúdio...\nAgora mesmo vou lhes brindar com algo grandioso.",
        "notes": "Mir avisa que a queda daquele posto era apenas uma demonstração preliminar de seu poder."
    },
    16723: {
        "text": "Uma cerimônia magnífica e digna...\nde saudar o alvorecer deste novo mundo...",
        "notes": "Mir evoca a destruição em massa como se fosse uma liturgia solene de fundação."
    },
    16724: {
        "text": "Não! O Corredor Musical...\nestá sendo purgado!!",
        "notes": "Shurelia descobre horrorizada o expurgo iminente do Corredor Musical (彩音回廊がパージされる)."
    },
    16725: {
        "text": "...!!",
        "notes": "O sistema central da Torre emite sinais de sobrecarga sísmica extrema."
    },
    16726: {
        "text": "Kyaaaah!!",
        "notes": "Shurelia é arremessada pela onda de choque da ejeção atmosférica do bloco."
    },
    16727: {
        "text": "Aaaai!!",
        "notes": "No Mundo Inferior, Aurica perde o equilíbrio com o violento tremor de terra."
    },
    16728: {
        "text": "O que foi isso?!",
        "notes": "Lyner firma os pés no chão e reage em sobressalto ao abalo sísmico descomunal."
    },
    16729: {
        "text": "O que tá acontecendo...?!",
        "notes": "Aurica contempla o horizonte aterrorizada com o estrondo vindo das alturas da Torre."
    },
    16730: {
        "text": "Não me diga que... os vírus de novo...?!",
        "notes": "Lyner associa de imediato a catástrofe fônica a uma nova ofensiva do enxame viral."
    },
    16731: {
        "text": "...Hã?",
        "notes": "Aurica não compreende a que vírus Lyner está se referindo naquele instante."
    },
    16732: {
        "text": "Não, não é nada...\nVamos voltar logo para a pousada,\no pessoal vai ficar preocupado.",
        "notes": "Lyner disfarça sua inquietação para poupar Aurica e decide retornar à estalagem com urgência."
    },
    16733: {
        "text": "Tá bem.",
        "notes": "Aurica anui dócil e acompanha o cavaleiro de volta ao abrigo da cidade."
    },
    16734: {
        "text": "O Corredor Musical era o sistema que regulava\no clima de todo este mundo...\nDerrubá-lo dessa maneira...",
        "notes": "De volta a Platina, Shurelia contempla em desespero o abismo deixado pela queda do setor regulador."
    },
    16735: {
        "text": "O mundo se tornará inabitável para todos!\nNão apenas para os humanos, mas até para as Reyvateils...!",
        "notes": "Shurelia denuncia a loucura ecológica do plano de Mir, que condena todas as formas biológicas à extinção."
    },
    16736: {
        "text": "Fufu. Fique tranquila.\nEu não sou tola a esse ponto: calculei cada detalhe...",
        "notes": "Mir rebate com frieza calculista, assegurando ter previsto os desdobramentos climáticos da queda."
    },
    16737: {
        "text": "O que você pretende afinal,\nMir...?!",
        "notes": "Shurelia exige respostas perante a desfaçatez da entidade inimiga."
    },
    16738: {
        "text": "Eu já lhe disse:\nvou erradicar os humanos e forjar\na utopia eterna das Reyvateils.",
        "notes": "Mir reitera seu dogma imutável de purificação e redenção da linhagem cantora."
    },
    16739: {
        "text": "Para isso, inúmeras armadilhas\njá foram tecidas por toda parte...",
        "notes": "Mir revela a existência de uma teia conspiratória operando clandestinamente no mundo."
    },
    16740: {
        "text": "Sim...\ninclusive bem ao seu lado...",
        "notes": "Mir deixa no ar a insinuação aterrorizante de que possui um agente infiltrado no círculo íntimo da deusa."
    },
    16741: {
        "text": "...!!",
        "notes": "Shurelia estremece ao pressentir a sombra da traição antes de perder a consciência."
    },
    16742: {
        "text": "...Senhora Shurelia.",
        "notes": "Ayatane aproxima-se com passos silenciosos da deusa caída no chão do templo."
    },
    16743: {
        "text": "......",
        "notes": "Shurelia permanece inerte e desacordada aos pés do altar sagrado."
    },
    16744: {
        "text": "Senhora Shurelia...?\nEla perdeu os sentidos...",
        "notes": "Ayatane constata o desmaio da guardiã divina sem esboçar alarme ou pressa."
    },
    16745: {
        "text": "...Ainda assim, como é bela.\nBasta contemplar o seu semblante adormecido\npara que a minha alma encontre paz.",
        "notes": "Ayatane murmura com obsessão perturbadora e fascínio solene enquanto fita a administradora inconsciente."
    },
    16746: {
        "text": "Senhora Shurelia...\nEu hei de proteger tudo o que lhe pertence.\nDe agora em diante... para todo o sempre...",
        "notes": "Ayatane faz um juramento ambíguo e possessivo de proteção perpétua à deusa de Elemia."
    },
    16747: {
        "text": "Como Cavaleiro de Elemia...\ne também pela minha \"Mãe\"...",
        "notes": "Revelação sombria de lealdade filial a Mir ('Mãe'), expondo sua verdadeira natureza de vírus infiltrado."
    },
    16748: {
        "text": "Cadê a Krusche?",
        "notes": "De volta à estalagem de Karff, Lyner indaga pelo paradeiro da engenheira mecânica."
    },
    16749: {
        "text": "Disse que precisava checar uma coisa\ne deu no pé.",
        "notes": "Jack informa em tom informal e despojado que Krusche saiu a negócios particulares."
    },
    16750: {
        "text": "Gente, eu descobri uma coisa gravíssima!\nParece que um pedaço da Torre desabou em cima\nde uma das instalações da Tenba!",
        "notes": "Krusche irrompe na taverna anunciando que os destroços da Torre esmagaram um complexo da corporação."
    },
    16751: {
        "text": "C-como é que é?!",
        "notes": "Lyner empalidece diante da magnitude do desastre urbano provocado pela queda."
    },
    16752: {
        "text": "E tem mais: por puro azar,\nparece que o alto escalão da Tenba estava todo reunido lá...",
        "notes": "Krusche complementa que a cúpula diretiva da Tenba realizava uma conferência secreta no local."
    },
    16753: {
        "text": "Aquele grandalhão brutamontes, a presidente...",
        "notes": "Krusche identifica os presentes na reunião: Bourd e a Presidente Ayano."
    },
    16754: {
        "text": "Um homem gigantesco...\nSerá que é o Bourd?!",
        "notes": "Lyner associa de imediato a descrição ao cruel comandante corporativo Bourd."
    },
    16755: {
        "text": "Não há dúvida.\nNa Tenba não existe outro homem com aquele porte.",
        "notes": "Radolf corrobora com precisão tática a identidade física do oficial inimigo."
    },
    16756: {
        "text": "Se for isso... quer dizer que a Misha\ntambém pode estar lá?!",
        "notes": "Lyner conecta as peças e entra em pânico pelo risco mortal que ronda sua amiga de infância mantida cativa."
    },
    16757: {
        "text": "O-o quê?! A Misha?!!",
        "notes": "Ao ouvir o nome de Misha, Jack perde instantaneamente a pose fria e reage em desespero total."
    },
    16758: {
        "text": "...Jack?\nVocê conhece a Misha?",
        "notes": "Lyner estranha o sobressalto desmedido do mercenário veterano."
    },
    16759: {
        "text": "Se conheço?! É claro que conheço...\nAliás, o único motivo de eu ter saído em viagem\nfoi para encontrar a Misha!",
        "notes": "Jack escancara a verdade sobre sua missão pessoal: encontrar e resgatar a jovem Reyvateil."
    },
    16760: {
        "text": "C-caramba, é sério?!\nQuer dizer que se você já sabia quem eu era,\nfoi a Misha que te contou...?",
        "notes": "Lyner compreende que as referências que Jack tinha sobre ele provinham dos relatos de Misha."
    },
    16761: {
        "text": "É... bem...\nMais ou menos por aí.",
        "notes": "Jack desconversa desconcertado para não expor prematuramente os laços de sangue e o passado Teru."
    },
    16762: {
        "text": "Mas esquece isso agora, Lyner!\nTemos que ir resgatá-la agora mesmo!\nSem perder um segundo!",
        "notes": "Jack corta as explicações e exige ação militar imediata para salvar a vida de Misha nos escombros."
    },
    16763: {
        "text": "S-sim, vamos...!",
        "notes": "Lyner concorda impetuosamente, unindo forças ao mercenário para a missão de salvamento."
    },
    16764: {
        "text": "...Aguenta firme, Misha!",
        "notes": "Jack profere um voto silencioso e angustiado pela sobrevivência da jovem amiga."
    },
    16765: {
        "text": "Acesso à [Placa Hexagonal] liberado no Mapa-Múndi!",
        "notes": "Notificação do sistema desbloqueando a rota de navegação para a Placa Hexagonal (六角板)."
    },
    16766: {
        "text": "......",
        "notes": "Aurica observa o tumulto em silêncio contido, sentindo a sombra da urgência pairar sobre o grupo."
    }
}

# Montagem dos dados
curated_lines = []
dialogues = []

assert len(CURATED_DATA) == 209, f"Expected 209 entries in CURATED_DATA, got {len(CURATED_DATA)}"

for d in input_data["dialogues"]:
    item_id = d["id"]
    assert item_id in CURATED_DATA, f"Missing ID {item_id} in CURATED_DATA"
    info = CURATED_DATA[item_id]
    txt = info["text"]
    nts = info["notes"]

    curated_lines.append({
        "id": item_id,
        "ptbr_curated": txt,
        "rationale": nts
    })

    dialogues.append({
        "id": item_id,
        "event_file": d["event_file"],
        "speaker_id": d["speaker_id"],
        "speaker": d["speaker"],
        "original_jp": d["original_jp"],
        "original_en": d["original_en"],
        "current_ptbr": d["current_ptbr"],
        "review_status": "approved",
        "text_ptbr": txt,
        "curated_ptbr": txt,
        "final_ptbr": txt,
        "texto_ptbr_curado": txt,
        "custom_text": txt,
        "ptbr_curated": txt,
        "reviewed": True,
        "notes": nts,
        "curation_notes": nts,
        "curadoria_notes": nts
    })

glossary_additions = {
    "Corredor Musical": {
        "pt": "Corredor Musical",
        "gender": "masculino",
        "number": "singular",
        "category": "Cenário / Setor da Torre",
        "note": "彩音回廊 (Sai'on Kairou / Musical Corridor). Setor atmosférico da Torre Ar tonelico responsável pelo equilíbrio climático e pela circulação fônica do mundo, purgado e ejetado por Mir."
    },
    "Placa Hexagonal": {
        "pt": "Placa Hexagonal",
        "gender": "feminino",
        "number": "singular",
        "category": "Toponímia / Estrutura",
        "note": "六角板 (Rokkaku-ban / Hexagonal Plate). Plataforma colossal suspensa na atmosfera da Torre que caiu sobre as instalações industriais da Tenba após a sabotagem viral."
    },
    "Altar dos Apóstolos": {
        "pt": "Altar dos Apóstolos",
        "gender": "masculino",
        "number": "singular",
        "category": "Localização / Lore de Platina",
        "note": "使徒の祭壇 (Shito no Saidan / Altar of Apostles). Santuário sagrado no topo de Platina invadido e corrompido pelos vírus de Mir para transmissão de sua voz espectral."
    },
    "Guia do Fluxo": {
        "pt": "Guia do Fluxo",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / Cosmosphere",
        "note": "ナガレの水先案内人 (Nagare no Mizusaki Annai-nin). Figura mascarada misteriosa vestindo túnica ornada de olhos que atua como guia mental na Cosmosfera de Aurica."
    },
    "Método de Desenvolvimento do Potencial Oculto": {
        "pt": "Método de Desenvolvimento do Potencial Oculto",
        "gender": "masculino",
        "number": "singular",
        "category": "Lore / Cosmosphere",
        "note": "「潜在能力開発法~3分で修得できる秘術~」. Livro satírico encontrado na mansão da Cosmosfera de Aurica prometendo sabedoria e notas máximas mediante roubo de energia da Torre."
    },
    "Colina do Canto": {
        "pt": "Colina do Canto",
        "gender": "feminino",
        "number": "singular",
        "category": "Toponímia / Lore",
        "note": "謳う丘 (Utau Oka / Singing Hill). Colina sagrada onde ficavam guardados os Cristais Hymmnos e onde Aurica salvou Lyner de despencar com sua primeira Magia da Canção."
    }
}

scene_handoff = {
    "last_scene_id": "Event/145.evd",
    "last_line_id": 16766,
    "resumo_dramatico": "O bloco BLK_EVD_073 articula três passagens dramáticas de altíssimo impacto narrativo e revelações canônicas capitais: (1) Em Event/232.evd, no parque urbano de Karff durante um intervalo da tempestade, Misha percebe o estresse e a afobação de Lyner em querer resgatar Claire e chegar ao Beco Vagalume. Com carinho e cumplicidade de infância, Misha o convence a arejar a cabeça e ir às compras para relaxar, antes que o esgotamento o faça perder o controle; Jack intervém ironizando a despreocupação dos dois ('Harm-da!') e parte sozinho para colher informações. (2) Em Event/730.evd, na mansão onírica da Cosmosfera de Aurica, a garota busca desesperadamente o livro 'Método de Desenvolvimento do Potencial Oculto' para ficar inteligente e não ser descartada. O misterioso 'Guia do Fluxo' surge e adverte que sugar energia da Torre é prejudicial, orientando-a a derrotar o gato parasita diante da Torre — um constructo mental imposto por ela mesma. Ao tentar reler o livro, Lyner é impedido pela rejeição inconsciente de Aurica, que tem um colapso de raiva, o acusa de falso e o abandona na escuridão sob o olhar cínico de Don Leon. (3) Em Event/145.evd, Aurica e Lyner conversam ao entardecer; tomada por complexo de inferioridade perante Claire e estigmatizada como Reyvateil Classe D, Aurica revela que sua única alegria fora ser convocada pelo Bispo Falss para a missão na Colina do Canto, momento em que Lyner a reafirma como indispensável e relembra como ela salvou sua vida no desabamento. Subitamente, a cena corta para o santuário do Altar dos Apóstolos em Platina: o enxame viral rompe as defesas e a voz espectral de Mir manifesta-se através de uma barreira tóxica. Mir proclama seu ódio à humanidade ('o verdadeiro vírus') e purga violentamente o Corredor Musical (彩音回廊), provocando abalos sísmicos que ecoam até o Mundo Inferior e deixam o clima global em colapso. Nos escombros sagrados, Ayatane contempla a Senhora Shurelia desacordada e faz um juramento ambíguo de proteção como Cavaleiro de Elemia... e por sua 'Mãe' (Mir), revelando sua condição de vírus infiltrado. Na taverna de Karff, Krusche noticia que destroços da Torre caíram sobre um complexo da Tenba onde estavam reunidos Bourd e Ayano; temendo pela vida de Misha mantida cativa, Lyner mobiliza o grupo, momento em que Jack perde o controle e revela que Misha é a única razão de sua viagem. O acesso à Placa Hexagonal é desbloqueado no Mapa-Múndi.",
    "decisoes_terminologicas": {
        "Musical Corridor": "彩音回廊 (Corredor Musical / complexo de regulação climática purgado por Mir)",
        "Hexagonal Plate": "六角板 (Placa Hexagonal / setor suspenso da Torre derrubado sobre as instalações da Tenba)",
        "Altar of Apostles": "使徒の祭壇 (Altar dos Apóstolos / santuário sagrado de Platina corrompido por Mir)",
        "Guide of the Flow": "ナガレの水先案内人 (Guia do Fluxo / entidade tutelar onírica da Cosmosfera de Aurica)",
        "Singing Hill": "謳う丘 (Colina do Canto / sítio ancestral onde repousavam os cristais)",
        "Potential Development Method": "「潜在能力開発法~3分で修得できる秘術~」 (Método de Desenvolvimento do Potencial Oculto / livro onírico)",
        "Mother": "『母さん』 (Mãe / título filial com que Ayatane se refere a Mir)",
        "Harm-da": "アル兄ぃ (Harm-da / diminutivo carinhoso infantil de Misha para Jack)"
    },
    "alertas_para_proximo_bloco": "Nos blocos subsequentes (BLK_EVD_074 em diante), acompanhar o avanço urgente do grupo rumo à Placa Hexagonal para resgatar Misha dos escombros da Tenba, a tensão crescente sobre o passado Teru de Jack e os desdobramentos da sabotagem de Mir e da infiltração de Ayatane após o colapso climático do Corredor Musical."
}

output_obj = {
    "block_id": "BLK_EVD_073",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(dialogues),
    "id_range": [16558, 16766],
    "curated_lines": curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": dialogues,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_obj, f, ensure_ascii=False, indent=2)

print(f"Sucesso: gerado {output_path} com {len(dialogues)} linhas.")

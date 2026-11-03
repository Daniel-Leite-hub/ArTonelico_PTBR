# -*- coding: utf-8 -*-
"""
build_blk057.py - Construtor e validador integral para BLK_EVD_057_output.json
"""
import json
import sys
import os

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_057_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_057_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Dicionário de curadoria: ID -> (curated_ptbr, notes)
curated = {}

# =========================================================================
# CENÁRIO 1: Event/297.evd (13304 - 13334) - A Cozinha de Claire em Nemo
# =========================================================================
curated[13304] = (
    "Mana Claire, queria te pedir um favor...\nSerá que você me empresta a sua cozinha?",
    "Aurica pede a cozinha emprestada a Claire com afeto fraternal carinhoso."
)
curated[13305] = (
    "Ora, o que houve?\nVai cozinhar alguma coisa?",
    "Claire estranha a petição inusitada com curiosidade fraternal."
)
curated[13306] = (
    "Sim!\nQuero preparar algo pro Lyner comer.",
    "Aurica revela radiante sua intenção de cozinhar para Lyner."
)
curated[13307] = (
    "...Vejamos,\nprimeiro eu pico isto aqui... e pronto.",
    "Aurica inicia o preparo cortando os ingredientes com técnica desastrada."
)
curated[13308] = (
    "E-espera aí!\nSe cortar desse jeito, vai decepar os dedos!",
    "Claire entra em pânico cômico ao ver a falta de jeito perigosa de Aurica com a faca."
)
curated[13309] = (
    "Não se preocupe!\nFaz dez anos que cozinho desse jeito.",
    "Aurica defende suas habilidades culinárias caóticas com confiança desconcertante."
)
curated[13310] = (
    "......",
    "Silêncio atônito de contemplação do desastre gastronômico iminente."
)
curated[13311] = (
    "Mas que raios...\nela está cozinhando ali?...",
    "Radolf observa aterrorizado e atônito a alquimia bizarra da panela."
)
curated[13312] = (
    "Q-que pavor...!",
    "Lyner estremece apavorado antevendo o veneno potencial que terá de engolir."
)
curated[13313] = (
    "Aurica...",
    "Claire suspira em choque conformada com a fatalidade culinária."
)
curated[13314] = (
    "Ficou pronto...",
    "Aurica anuncia a conclusão orgulhosa de sua obra gastronômica duvidosa."
)
curated[13315] = (
    "O prato de hoje é um agradecimento a você,\nLyner, por todo o esforço de cada dia!",
    "Aurica dedica solenemente o prato ao cavaleiro com carinho ingênuo."
)
curated[13316] = (
    "Aqui está... Pode comer, por favor!",
    "Aurica serve a iguaria suspeita com entusiasmo radiante."
)
curated[13317] = (
    "......",
    "Hesitação mortal de Lyner diante da comida fumegante."
)
curated[13318] = (
    "...Muito bem, Lyner!\nManda ver com tudo!",
    "Radolf empurra o jovem parceiro para o perigo com sadismo militar bem-humorado."
)
curated[13319] = (
    "Come você primeiro, Radolf!",
    "Lyner devolve o desafio apavorado tentando salvar o próprio estômago."
)
curated[13320] = (
    "...Não quer comer?\nE eu que fiz com tanto carinho só pra você...",
    "Aurica expressa mágoa enternecedora e bico de decepção desarmante."
)
curated[13321] = (
    "Ah, que seja! Agora vai no desespero!\nBom apetite!!",
    "Lyner rende-se ao destino fatal em ato heroico de puro desespero."
)
curated[13322] = (
    "Está uma delícia!!",
    "Reação estupefata e espontânea de Lyner diante do sabor inesperado."
)
curated[13323] = (
    "C-como é que é?!",
    "Radolf reage em choque absoluto à sobrevida milagrosa de Lyner."
)
curated[13324] = (
    "Está uma delícia, mas... que estranho!\nNunca provei um sabor tão bizarro na vida!",
    "Lyner descreve a perplexidade de um paladar contraditório e excêntrico."
)
curated[13325] = (
    "A suavidade e a picância marcante se harmonizam tão bem...\nque fica estranhamente viciante!",
    "Lyner detalha a alquimia sensorial viciante da mistura caótica de Aurica."
)
curated[13326] = (
    "...N-não é possível!\nIsso não faz o menor sentido...",
    "Radolf recusa-se a acreditar na física gastronômica impossível daquele prato."
)
curated[13327] = (
    "Que alívio!\nFico feliz que você tenha gostado.",
    "Aurica comemora aliviada a aprovação do cavaleiro."
)
curated[13328] = (
    "Mas me diz uma coisa, Aurica...\nonde foi que você aprendeu uma receita dessas?",
    "Lyner questiona a procedência mística de tal iguaria exótica."
)
curated[13329] = (
    "Hã? Ninguém me ensinou, não.\nSó fui misturando o que vi pela frente agora mesmo.",
    "Aurica revela descarada que jogou ingredientes a esmo sem qualquer critério."
)
curated[13330] = (
    "Fala sério...",
    "Choque estupefato de Lyner diante da sorte cega de não ter sido envenenado."
)
curated[13331] = (
    "Pelo visto a sua sorte é de outro mundo, Lyner.\nVocê vai viver um bocado, com certeza.",
    "Radolf ironiza o corpo fechado e a sobrevida miraculosa do companheiro."
)
curated[13332] = (
    "Bem, agora preciso arrumar a bagunça,\nentão a sessão acabou por hoje!",
    "Claire encerra com praticidade doméstica o expediente da cozinha."
)
curated[13333] = (
    "Muito obrigada por hoje, mana Claire!",
    "Aurica agradece afetuosamente à acolhida fraternal de Claire."
)
curated[13334] = (
    "Certo, vamos para a igreja agora.",
    "Radolf retoma a postura sóbria e direciona a comitiva para o próximo objetivo."
)

# =========================================================================
# CENÁRIO 2: Event/542.evd (13335 - 13362) - O Conflito Ideológico com Hama / Tastiella
# =========================================================================
curated[13335] = (
    "...E então?\nEncontrou a resposta?",
    "Hama interroga Lyner sobre o dilema filosófico imposto à comitiva."
)
curated[13336] = (
    "Qual é a causa mais simples e, ao mesmo tempo,\nmais crucial para o surgimento de um conflito?",
    "Hama formula o enigma existencial sobre a raiz primal de todas as guerras."
)
curated[13337] = (
    "...Entendo.\nPretende abrir passagem à força?",
    "Hama percebe a postura resoluta e combativa do cavaleiro."
)
curated[13338] = (
    "A própria sobrevivência deste mundo está em jogo...",
    "Lyner justifica a urgência heroica diante do colapso iminente da Torre."
)
curated[13339] = (
    "Se você continuar agindo assim e nos bloqueando sem motivo,\nacho que não teremos outra escolha.",
    "Lyner lamenta a necessidade do embate contra a guardiã misteriosa."
)
curated[13340] = (
    "Compreendo.\nMas eu também estou agindo pelo bem deste mundo.",
    "Hama contrapõe o nobre propósito de sua provação moral e guardiã."
)
curated[13341] = (
    "Se faz tanta questão de passar,\nterá que me derrotar para seguir em frente.",
    "Hama impõe o duelo inescapável como único teste de resolução."
)
curated[13342] = (
    "...O-o quê?! Ficou louca?!",
    "Lyner recua espantado com a exigência extrema da guardiã."
)
curated[13343] = (
    "Se essa é a sua forma de resolver as coisas...\nvocê é capaz, não é?",
    "Hama desafia a hipocrisia de justificar violência em nome da justiça."
)
curated[13344] = (
    "Está bem. Eu amo este mundo!\nE por isso farei o que for preciso para salvá-lo.",
    "Lyner assume a dor do confronto em defesa do futuro de Sol Ciel."
)
curated[13345] = (
    "Eu sinto o mesmo que você.\nÉ justamente por isso que não vou te deixar passar.",
    "Hama espelha a convicção do jovem sem recuar um milímetro de seu dever."
)
curated[13346] = (
    "Lyner...\nSe este é o caminho em que acredita, siga-o com firmeza até o fim.",
    "Hama reconhece a têmpera do cavaleiro ao ser subjugada no combate."
)
curated[13347] = (
    "Este é... o meu último con... se... lho... para você...",
    "Hama desvanece espiritualmente pronunciando suas palavras finais fragmentadas."
)
curated[13348] = (
    "Tastiella!!",
    "Grito dilacerado de Shurelia ao reconhecer a mentora ancestral sacrificada."
)
curated[13349] = (
    "......",
    "Luto e solenidade silenciosa de Shurelia diante do espírito consumado."
)
curated[13350] = (
    "Senhora Shurelia... me perdoe.\nMas eu...",
    "Lyner expressa pesar angustiado pela dureza da escolha necessária."
)
curated[13351] = (
    "...Eu compreendo.\nNão se preocupe, estou bem.",
    "Shurelia recolhe suas lágrimas e conforta com nobreza o peso no coração de Lyner."
)
curated[13352] = (
    "Vamos depressa...\naté onde Mir está...",
    "Shurelia conclama o avanço irrevogável rumo ao confronto com a Rainha Viral."
)
curated[13353] = (
    "Eu... não posso fazer isso...",
    "Lyner hesita no ramo alternativo, recusando-se a erguer a espada contra a guardiã."
)
curated[13354] = (
    "Entendo.\nNesse caso, não posso deixar você passar.",
    "Hama barra o avanço diante da falta de determinação do cavaleiro."
)
curated[13355] = (
    "Lyner...\nvou lhe dizer uma dura verdade.",
    "Hama prepara uma repreensão severa para quebrar a ingenuidade do rapaz."
)
curated[13356] = (
    "A sua escolha de agora não nasceu da bondade.\nÉ mero fruto de uma resolução fraca e indecisa.",
    "Hama desmascara a falsa compaixão como incapacidade de assumir responsabilidade."
)
curated[13357] = (
    "Se pretendia de verdade romper o meu bloqueio,\ndeveria ter atacado sem vacilar!",
    "Hama exige postura convicta e condena a covardia de meias medidas."
)
curated[13358] = (
    "Hesitar assim... é pura covardia...",
    "Sentença desdenhosa da guardiã confrontando o recuo hesitante de Lyner."
)
curated[13359] = (
    "......",
    "Silêncio cabisbaixo de Lyner sentindo o peso da crítica impiedosa."
)
curated[13360] = (
    "Tudo bem. Eu ainda estou bem por aqui,\nentão pense com muita calma.",
    "Hama abranda o tom concedendo ao jovem o tempo necessário para amadurecer."
)
curated[13361] = (
    "...É, você tem razão. Desculpe.",
    "Lyner aceita com humildade o ensinamento severo da mentora."
)
curated[13362] = (
    "Não se preocupe...\nEstou contando com você.",
    "Hama renova sua esperança velada no potencial do jovem herói."
)

# =========================================================================
# CENÁRIO 3: Event/739.evd (13363 - 13421) - O Drama de Donsuke / Don Leon na Cosmosfera
# =========================================================================
curated[13363] = (
    "Nossa, Srta. Claire?!\nDesculpe entrar assim de repente!",
    "Lyner surpreende-se ao adentrar os aposentos de Claire no mundo onírico."
)
curated[13364] = (
    "Ah, não se preocupe, tudo bem.\nNa verdade, você chegou na hora certa. Eu queria falar com você sobre o Don Leon e a Aurica...",
    "Claire acolhe Lyner e aproveita para expor sua aflição com a dinâmica psíquica da amiga."
)
curated[13365] = (
    "Pelo que andei vendo, as coisas estão bem caóticas.\nO que é aquilo, afinal?... O que é esse tal de Don Leon?",
    "Lyner indaga confuso sobre a natureza da persona samurai e da pelúcia protetora."
)
curated[13366] = (
    "O Don Leon é um bichinho de pelúcia que dei de presente para a Aurica quando deixei o nosso vilarejo.",
    "Claire revela a origem real do guardião como um objeto de transição afetiva."
)
curated[13367] = (
    "Um bicho de pelúcia?! Então era isso...\nMas... por que ela deu um nome como Don Leon pra ele?",
    "Lyner espanta-se com o contraste entre o brinquedo infantil e o nome pomposo."
)
curated[13368] = (
    "A-aquele nome... foi a própria Aurica quem inventou.",
    "Claire confessa com sorriso tímido o senso peculiar de batismo da amiga."
)
curated[13369] = (
    "...Eu já devia imaginar... O senso dela pra dar nomes é tão peculiar que eu já desconfiava...",
    "Lyner resigna-se diante da excentricidade inconfundível de Aurica."
)
curated[13370] = (
    "Quando saí do vilarejo, eu entreguei a pelúcia dizendo: 'Cuide dele com carinho, pensando que sou eu'...",
    "Claire compartilha a memória afetuosa da despedida da infância em Skuwat."
)
curated[13371] = (
    "E parece que ela cuidou com um carinho enorme mesmo.\nA ponto de torná-lo o protagonista num recanto tão profundo do coração dela.",
    "Claire emociona-se ao perceber a magnitude que seu presente adquiriu no inconsciente de Aurica."
)
curated[13372] = (
    "Por isso, fico feliz, mas...\nsinto que tem algo meio fora do lugar...",
    "Claire expressa inquietude com a distorção dependente que essa devoção causou."
)
curated[13373] = (
    "Mana Claire!",
    "A projeção infantil de Aurica surge chamando pela irmã mais velha com doçura."
)
curated[13374] = (
    "Aurica! O que houve?",
    "Claire reage à aproximação da pequena Aurica com solicitude."
)
curated[13375] = (
    "Sabe o que é? Eu queria te agradecer hoje.\nMuito obrigada por ter me dado o Don Leon!",
    "A Aurica criança expressa gratidão genuína pelo companheiro inseparável."
)
curated[13376] = (
    "Imagina, não há de quê.",
    "Claire responde com ternura contida à pequena."
)
curated[13377] = (
    "O Don Leon é incrível!\nEle dá uma surra em todo mundo que tenta me fazer mal!",
    "A criança exalta entusiasmada a função bélica e defensiva de seu ursinho justiceiro."
)
curated[13378] = (
    "Escuta, Aurica...\nEu não te dei o Don Leon de presente para ele tomar o seu lugar nas coisas, sabe?",
    "Claire tenta alertar suavemente sobre a fuga de responsabilidade emocional."
)
curated[13379] = (
    "...Hã?",
    "Incompreensão inocente da pequena Aurica diante da advertência."
)
curated[13380] = (
    "Eu te dei o Don Leon para que você não ficasse sozinha...",
    "Claire relembra o verdadeiro propósito afetivo da lembrança: afastar a solidão."
)
curated[13381] = (
    "Além do mais, se você ficar sempre dependendo dele desse jeito,\nquando é que vai crescer e virar adulta?!",
    "Claire repreende amorosamente a estagnação infantil da amiga."
)
curated[13382] = (
    "...Como assim?... Até você, mana Claire?...\nDon Leon!! Me ajuda! A mana Claire tá implicando comigo...!",
    "A criança entra em pânico e clama socorro ao guardião contra a própria Claire."
)
curated[13383] = (
    "C-como é que é?! E-espera aí, Aurica!",
    "Claire assusta-se com a reação defensiva desmedida da garotinha."
)
curated[13384] = (
    "...O quê?!",
    "Lyner pasma-se com a virada repentina e violenta do delírio onírico."
)
curated[13385] = (
    "A mana Claire tá implicando com você?\nCerto, deixa comigo! Deixa que o Don Leon resolve!",
    "A persona combativa de Aurica assume o comando para proteger sua faceta infantil."
)
curated[13386] = (
    "Aurica, espera um pouco!\nA Srta. Claire só estava preocupada e te deu uma bronca. Você acha mesmo que isso é implicar com você?!",
    "Lyner intervém racionalmente para desarmar a histeria agressiva da parceira."
)
curated[13387] = (
    "......",
    "Choque e conflito interno de Aurica ao ser confrontada pela razão de Lyner."
)
curated[13388] = (
    "O Don Leon tem que obedecer ao que a Aurica diz, não importa o que aconteça...",
    "Aurica recita dogmaticamente a diretriz cega gravada em sua mente."
)
curated[13389] = (
    "Como assim?!",
    "Lyner recusa-se a aceitar essa lógica destrutiva e aprisionadora."
)
curated[13390] = (
    "Desculpem, mana Claire, Lyner.\nLá vou eu...!",
    "Aurica pede perdão sofrida antes de disparar a agressão do guardião."
)
curated[13391] = (
    "Yaaah!!",
    "Grito de ataque impetuoso desferido pela defensora mágica."
)
curated[13392] = (
    "Pare com isso!!!",
    "Lyner interpõe-se heroicamente bloqueando o golpe devastador."
)
curated[13393] = (
    "...Lyner.\nPor que está me impedindo? Se você ficar no meu caminho... eu vou acabar hesitando...",
    "Resgate crucial sobre o erro da NISA: Aurica confessa com vulnerabilidade que a presença de Lyner abala sua convicção cega."
)
curated[13394] = (
    "Quem foi que inventou que o Don Leon tem que obedecer a tudo o que você manda?",
    "Lyner questiona a raiz arbitrária da subserviência do guardião."
)
curated[13395] = (
    "E mesmo que fosse assim, não quer dizer que você possa fazer o que bem entender! Por que tudo virou essa loucura?!",
    "Lyner expõe o absurdo moral da violência desencadeada por capricho."
)
curated[13396] = (
    "......",
    "Aurica desmorona emocionalmente ao encarar sua carência desnuda."
)
curated[13397] = (
    "É que... se o Don Leon sumir, eu não vou aguentar...",
    "Aurica confessa o pavor paralisante de perder seu esteio protetor."
)
curated[13398] = (
    "...Hã?",
    "Lyner percebe a fragilidade dilacerante por trás da agressividade dela."
)
curated[13399] = (
    "Se eu parar de pedir ajuda ao Don Leon...\nele vai embora pra sempre...",
    "A faceta infantil verbaliza a crença trágica de que só mantém o amigo se for eternamente frágil."
)
curated[13400] = (
    "Eu não quero isso! Eu quero ficar com o Don Leon pra sempre!",
    "Grito angustiado de carência afetiva da jovem Reyvateil."
)
curated[13401] = (
    "O Don Leon é o meu cavaleiro particular,\nque protege uma garota fraca como eu...",
    "A criança apoia sua identidade no papel de donzela indefesa protegida pela pelúcia."
)
curated[13402] = (
    "Mas se eu ficar bem sem precisar da proteção dele...\no Don Leon vai desaparecer...",
    "O núcleo do trauma revelado: a cura e o amadurecimento significariam a aniquilação do amigo."
)
curated[13403] = (
    "Se for pro Don Leon sumir,\neu não quero crescer coisa nenhuma!",
    "Recusa infantil visceral do amadurecimento em troca da preservação do afeto."
)
curated[13404] = (
    "Quero continuar assim para sempre...\nnum mundo onde o Don Leon fique me vigiando e cuidando de mim...",
    "O desejo regressivo supremo de permanecer em um eterno casulo seguro."
)
curated[13405] = (
    "Espereeeeeeem aí!!!!",
    "Entrada retumbante e teatral de Don Leon interrompendo o ciclo de vitimização."
)
curated[13406] = (
    "Quem é?!",
    "Aurica assusta-se com o brado imponente que ecoa na sala."
)
curated[13407] = (
    "Don Leon?!",
    "Aurica reconhece estupefata o guardião samurai em pessoa."
)
curated[13408] = (
    "Esse tal de Don Leon... em nada se parece com este humilde guerreiro!!",
    "Restauração do vocabulário samurai e da solenidade de Don Leon distorcida pela NISA."
)
curated[13409] = (
    "É verdade que este servo reside aqui juramentado a proteger a senhorita Aurica.",
    "Don Leon reafirma seu juramento de honra e fidelidade cavalheiresca."
)
curated[13410] = (
    "No entanto! Esse papel de Don Leon que vossas mercês encenam neste mundo... é, porventura, um ato de verdadeira 'proteção' à senhorita Aurica...?",
    "Don Leon questiona filosoficamente se perpetuar a fraqueza constitui verdadeira proteção."
)
curated[13411] = (
    "Se for este o caso... então este humilde servidor já não vos pode acompanhar...",
    "O guardião declara a impossibilidade moral de respaldar a autoflagelação de sua mestra."
)
curated[13412] = (
    "Passai bem...!",
    "Despedida nobre e cortês do guardião samurai retirando-se em protesto ético."
)
curated[13413] = (
    "Don Leon!!",
    "Desespero de Aurica ao ver o pilar de sua alma partir por vontade própria."
)
curated[13414] = (
    "...O que a gente faz?...\nPor nossa culpa, o Don Leon...",
    "A Aurica criança desaba em remorso pelo abandono imprevisto."
)
curated[13415] = (
    "Não adianta lamentar aqui parados. Vamos atrás do Don Leon!",
    "Lyner toma a iniciativa prática e convoca a busca imediata pelo companheiro."
)
curated[13416] = (
    "Don Leon... para onde você foi...?!",
    "Lyner perscruta o horizonte onírico em busca do rastro da pelúcia."
)
curated[13417] = (
    "Eu o derrotei, Aurica.",
    "Aurica conclui a batalha do sub-evento purificando o obstáculo interior."
)
curated[13418] = (
    "Obrigada, Don Leon!\nContinue cuidando de mim de agora em diante...",
    "A menina agradece enternecida reafirmando os laços com o leal defensor."
)
curated[13419] = (
    "Parece que fomos subjugados...",
    "Don Leon constata com serenidade estóica a resolução da disputa mental."
)
curated[13420] = (
    "Bem... significa que o afeto que a senhorita Aurica nutre por este humilde servo superou até mesmo o que ela sente por vós, Lyner...",
    "Don Leon alfineta Lyner com cortesia marcial ao notar a precedência de seu valor afetivo."
)
curated[13421] = (
    "Resta saber se este servo deve celebrar de bom grado...\nUma situação deveras espinhosa, sem dúvida...",
    "O samurai pondera com comicidade aristocrática a ambiguidade de tal vitória sentimental."
)

# =========================================================================
# CENÁRIO 4: Event/444.evd (13422 - 13497) - A Revelação dos Três Sábios e a Queda de Kyle
# =========================================================================
curated[13422] = (
    "Puxa vida!\nTinha que ser logo num lugar mofado e úmido como este?!",
    "Lyner reclama da atmosfera sombria e claustrofóbica das profundezas tecnológicas."
)
curated[13423] = (
    "Por acaso você preferia estar num parque ensolarado mastigando sanduíches?",
    "Leard dispara seu sarcasmo austero e patriarcal para enquadrar as lamúrias do filho."
)
curated[13424] = (
    "...Q-que ideia mais idiota! Quem disse isso?!",
    "Lyner reage indignado e na defensiva diante do deboche paterno."
)
curated[13425] = (
    "Ahaha! Que engraçado!",
    "Aurica cai na gargalhada com a troca de farpas cômica entre pai e filho."
)
curated[13426] = (
    "Bem, um piquenique até que não soa mal, mas hoje eu tinha um motivo para vir aqui.",
    "Leard encerra a provocação e introduz com gravidade a missão histórica do dia."
)
curated[13427] = (
    "Diga-me, Lyner.\nVocê se lembra do homem chamado Kyle Clancy?",
    "Leard traz à tona o nome original do antigo amigo e algoz de Platina."
)
curated[13428] = (
    "...Kyle? Acho que já ouvi esse nome em algum lugar... ou talvez não...",
    "Lyner vasculha a memória tentando associar o nome às lendas de infância."
)
curated[13429] = (
    "Ele desceu para as Asas de Hórus\ne, pelo visto, passou a atender pelo nome de 'Bispo Falss'.",
    "Leard desmascara formalmente a identidade clandestina assumida pelo traidor."
)
curated[13430] = (
    "Bispo Falss!... É verdade!",
    "Lyner conecta as peças do xadrez político e religioso de Sol Ciel."
)
curated[13431] = (
    "Bispo Falss...",
    "Aurica estremece ao recordar os abusos e perseguições sofridos nas mãos do clérigo."
)
curated[13432] = (
    "Pois esse Kyle Clancy guardava a chave para o despertar da Senhora Shurelia.",
    "Leard revela que o destino da deusa administradora estava atado às maquinações de Kyle."
)
curated[13433] = (
    "O quê?! ...O Bispo Falss?!",
    "Lyner choca-se com a amplitude da influência nefasta do farsante."
)
curated[13434] = (
    "Originalmente, ele era um dos altos dignitários da Catedral, no coração de Platina.",
    "Leard rememora o prestigioso status de Kyle no topo do governo de Sol Ciel."
)
curated[13435] = (
    "A Senhora Shurelia, Kyle e eu\néramos chamados, outrora, de os 'Três Sábios'.",
    "Revelação histórica canônica dos Três Sábios que governavam e mantinham a Primeira Torre."
)
curated[13436] = (
    "O nosso vínculo e trabalho conjunto eram verdadeiramente incomparáveis.",
    "Leard evoca com melancolia e orgulho a lendária coesão do antigo triunvirato."
)
curated[13437] = (
    "A própria Senhora Shurelia costumava afirmar que a nossa sintonia estava entre as maiores de toda a história dos Três Sábios.",
    "O testemunho de Shurelia atesta a excelência do colegiado antes da cisão ideológica."
)
curated[13438] = (
    "E com toda a razão... Afinal, Kyle e eu éramos grandes amigos desde pequenos...",
    "A dor pessoal de Leard: a traição do homem que fora seu irmão de criação e confidências."
)
curated[13439] = (
    "...Eu não fazia ideia!",
    "Lyner surpreende-se ao descobrir o passado oculto e as raízes afetivas de seu pai."
)
curated[13440] = (
    "Os Três Sábios carregavam nos ombros a responsabilidade de proteger a Torre, que representa tudo neste mundo.",
    "Leard define o peso existencial da soberania de Platina sobre a infraestrutura vital."
)
curated[13441] = (
    "Por esse motivo,\nnós administrávamos em conjunto um Cristal Hymmnos.",
    "A salvaguarda compartilhada dos códigos operacionais supremos da civilização."
)
curated[13442] = (
    "Um deles era o \"Suspend\", sob minha guarda:\no Cântico capaz de silenciar a Torre.",
    "Leard detalha a função terminal do Cântico Suspend como trava de segurança criogênica."
)
curated[13443] = (
    "O outro era o chamado \"RE Nation\":\no cristal capaz de reativar a Torre.",
    "Apresentação da relíquia sagrada de renascimento de sistema: o Cristal Hymmnos RE Nation."
)
curated[13444] = (
    "RE Nation...",
    "Lyner assimila o nome do artefato mítico indispensável para salvar o mundo."
)
curated[13445] = (
    "O \"RE Nation\" é o nosso último recurso em caso de pane catastrófica na Torre.",
    "Leard adverte sobre a natureza emergencial e definitiva do protocolo RE Nation."
)
curated[13446] = (
    "A confiança da Senhora Shurelia em nós era tão plena que ela nos confiou algo desse porte sem hesitar.",
    "A reverência comovida à fé incondicional que a Guardiã depositava em seus cientistas."
)
curated[13447] = (
    "No entanto, Kyle traiu essa confiança... Ele cometeu um tabu imperdoável.",
    "O ponto de ruptura moral: a apostasia científica de Kyle em busca de poder desenfreado."
)
curated[13448] = (
    "Refiro-me à conspiração da 'ressurreição de Mir', cujos desdobramentos nos assombraram até pouco tempo atrás.",
    "A conexão entre os experimentos proibidos de Kyle e o surto viral que abalou a civilização."
)
curated[13449] = (
    "Kyle... Por acaso tem consciência do que está fazendo...?",
    "Flashback histórico: a voz trêmula de Shurelia interpelando o cientista rebelde."
)
curated[13450] = (
    "Mas é claro, Senhora Shurelia.",
    "Kyle responde com insolência polida e arrogância acadêmica inabalável."
)
curated[13451] = (
    "Dedico-me dia e noite a pesquisas incansáveis para que este mundo se torne ainda mais próspero e confortável...",
    "Kyle escuda sua heresia na bandeira sedutora do bem-estar e da evolução técnica."
)
curated[13452] = (
    "Mexer com Mir é o tabu supremo no Juramento de Elemia!!",
    "Leard brada com fúria legalista e religiosa em defesa das cláusulas ancestrais sagradas."
)
curated[13453] = (
    "Violar esse preceito sagrado...\né algo que jamais será tolerado, não importa a justificativa!",
    "A intolerância intransigente do líder de Platina contra a quebra do pacto civilizatório."
)
curated[13454] = (
    "Kyle...\nVocê é um homem brilhante, dotado de grande poder e sabedoria.",
    "Shurelia elogia a genialidade do colaborador antes de pronunciar a sentença irrecorrível."
)
curated[13455] = (
    "No entanto, não posso permitir que continue habitando Platina nem mais um instante.",
    "A condenação ao banimento irrevogável imposta pela autoridade máxima da Torre."
)
curated[13456] = (
    "Peço-lhe que se retire de Platina...\nimediatamente.",
    "O decreto sumário de expulsão desferido com solenidade e pesar pela administradora."
)
curated[13457] = (
    "......",
    "Silêncio desdenhoso de Kyle assimilando o veredito sem demonstrar remorso."
)
curated[13458] = (
    "Lamento profundamente...\nVer que a minha pesquisa é incapaz de ser compreendida por vós.",
    "Kyle externa seu desprezo condescendente pela 'estreiteza mental' de seus pares."
)
curated[13459] = (
    "O mundo atual começou a apodrecer.\nTudo graças a essa lei nefasta chamada 'Juramento de Elemia'.",
    "Kyle ataca as bases fundacionais da ordem cósmica, rotulando o tratado sagrado de aberração."
)
curated[13460] = (
    "Renunciar ao progresso é o fim.\nNo instante em que uma civilização estagna, seu mundo caminha para a ruína.",
    "O credo transumanista e radical de Kyle: o medo patológico do declínio tecnológico."
)
curated[13461] = (
    "Tanta tecnologia avançada do passado...\nTanto poder imenso e recursos incalculáveis adormecidos aqui...",
    "O fascínio cobiçoso pelos segredos perdidos da era primordial de Ar tonelico."
)
curated[13462] = (
    "Optar por descartar tudo isso para levar uma vida primitiva... Francamente, acho ridículo.",
    "A virulência sarcástica do cientista cuspindo sobre a moderação ética da sociedade."
)
curated[13463] = (
    "Kyle! Aonde pensa que vai...?",
    "Leard tenta conter o velho companheiro que dá as costas à liderança."
)
curated[13464] = (
    "A Senhora Shurelia ordenou que eu partisse.\nVou aprontar os preparativos para o meu exílio.",
    "Kyle retruca com ironia ácida acatando formalmente a ordem de deportação."
)
curated[13465] = (
    "...Até o dia em que nos reencontrarmos. Passar bem...",
    "A despedida zombeteira de quem já arquitetava nas sombras sua vingança e infiltração."
)
curated[13466] = (
    "Depois disso, Kyle fingiu que ia embora, mas retornou às escondidas para o Altar dos Apóstolos.",
    "Leard narra o estratagema sorrateiro do traidor violando o santuário proibido."
)
curated[13467] = (
    "E quando tentava se apossar do poder de Mir, acabou flagrado pelos cavaleiros...",
    "A emboscada dos cavaleiros no instante em que Kyle tentava absorver o código viral."
)
curated[13468] = (
    "Dizem que ele se atirou daqui de cima para dar fim à própria vida.",
    "O falso suicídio cinematográfico nas bordas abissais de Platina."
)
curated[13469] = (
    "No entanto, até mesmo aquilo era pura encenação, uma manobra diversionista. Ele não morreu aqui de verdade.",
    "Leard desvenda o ardil genial de Kyle para simular a própria morte e operar impune."
)
curated[13470] = (
    "Graças à estratégia dele, o tal 'Bispo Falss' agindo no Mundo Inferior passou totalmente despercebido sob o nosso radar.",
    "O reconhecimento amargo do sucesso da camuflagem clerical adotada pelo fugitivo."
)
curated[13471] = (
    "E o desfecho foi essa calamidade que testemunhamos agora.",
    "A constatação sombria do preço trágico pago pela desatenção de Platina."
)
curated[13472] = (
    "Pensar que...\ntudo isso já vinha acontecendo desde o passado...",
    "Lyner dimensiona assombrado a escala temporal da conspiração que desmoronou o mundo."
)
curated[13473] = (
    "Peço desculpas à senhorita Aurica.\nNossa negligência acabou por lhe impor um fardo pesado demais.",
    "Leard curva-se dignamente pedindo perdão à Reyvateil pelas dores infligidas pela Igreja de Falss."
)
curated[13474] = (
    "Não...\nPor favor, não se preocupe comigo.",
    "Aurica acolhe o pedido de desculpas com serenidade e generosidade comovente."
)
curated[13475] = (
    "Afinal, se não tivesse sido assim... eu não estaria aqui agora...",
    "A maturidade lírica de Aurica: encontrar significado salvador nas próprias cicatrizes."
)
curated[13476] = (
    "E além do mais... talvez eu nunca tivesse conhecido o Lyner...",
    "A confissão romântica sussurrada e terna do valor transcendente do encontro dos dois."
)
curated[13477] = (
    "......",
    "Leard observa em silêncio comovido a cumplicidade que amadureceu entre os jovens."
)
curated[13478] = (
    "Se obtivermos o \"RE Nation\", a Senhora Shurelia certamente despertará mais uma vez.",
    "Leard crava o objetivo operacional indispensável para reviver a alma da Torre."
)
curated[13479] = (
    "Contudo, o \"RE Nation\" foi ocultado por Kyle.",
    "O grande entrave: a localização secreta do Cristal Hymmnos levado pelo falso bispo."
)
curated[13480] = (
    "Muito provavelmente no Mundo Inferior...\nÉ como se ele já previsse que as coisas chegariam a este ponto...",
    "Leard projeta a dedução lógica do paradeiro da relíquia na teia montada por Kyle."
)
curated[13481] = (
    "Onde será que está... esse Cristal Hymmnos chamado \"RE Nation\"?...",
    "Aurica pondera sobre o enigma geográfico da busca que os aguarda."
)
curated[13482] = (
    "...Boa pergunta. Talvez tenhamos que seguir os rastros deixados pelo Bispo Falss até agora.",
    "Lyner traça a linha investigativa para recuperar o rastro deixado pelo clérigo usurpador."
)
curated[13483] = (
    "Diga, Aurica... o que será que os outros pensam sobre despertar a Senhora Shurelia?",
    "Lyner consulta a sensibilidade da parceira sobre a reação e apoio dos antigos companheiros."
)
curated[13484] = (
    "Bem... imagino que todos queiram vê-la de volta, mas...",
    "Aurica pondera os riscos e as incertezas que cercam o grupo após a batalha da Torre."
)
curated[13485] = (
    "Se nós explicarmos toda a situação... será que eles aceitam nos ajudar de novo?",
    "Lyner manifesta sua fé inabalável na lealdade dos laços forjados na jornada."
)
curated[13486] = (
    "...É verdade. Eles podem até saber de alguma pista...",
    "Aurica apoia com entusiasmo prático a reunião da caravana de aliados."
)
curated[13487] = (
    "Radolf, Krusche, Jack, Misha...\nonde será que eles estão?",
    "Lyner enumera saudoso e decidido o quarteto de companheiros fundamentais."
)
curated[13488] = (
    "O Comandante-Geral Radolf com certeza está em Nemo.\nJá a Krusche deve estar no Beco Vagalume.",
    "Aurica mapeia com precisão os redutos habituais de seus leais amigos."
)
curated[13489] = (
    "O senhor Jack e a Misha disseram que iam sair em uma aventura, então não sei ao certo...",
    "Aurica ressalva a incerteza quanto à dupla andarilha de Teru e Reyvateil."
)
curated[13490] = (
    "Se formos até Em Pheyna, alguém por lá deve saber de alguma coisa.",
    "Lyner identifica o santuário da Tribo Teru como o ponto focal mais provável para obter notícias."
)
curated[13491] = (
    "Certo!\nEntão vamos nos pôr a caminho agora mesmo!",
    "O chamado ardente de Lyner à nova e grandiosa expedição de libertação mundial."
)
curated[13492] = (
    "O que houve, Aurica...?",
    "Lyner nota a hesitação súbita e o semblante apreensivo da amiga."
)
curated[13493] = (
    "Lyner... A força da Magia da Canção...\nquase não consigo mais usá-la... Eu...",
    "Aurica confessa sua impotência e vulnerabilidade decorrentes da suspensão da Torre."
)
curated[13494] = (
    "...Do que você está falando?",
    "Lyner rejeita com carinho protetor a ideia de que ela precise ser uma arma para ter valor."
)
curated[13495] = (
    "Eu estou com você, não estou?",
    "A declaração de coragem, companheirismo absoluto e amor protetor do herói."
)
curated[13496] = (
    "...Sim.",
    "Aurica desarma-se com um sorriso comovido, encontrando abrigo seguro no coração de Lyner."
)
curated[13497] = (
    "Agora você pode sair\npara o Mapa-Múndi!",
    "Notificação canônica de sistema liberando o trânsito da expedição pelo mundo."
)

print(f"Total lines curated: {len(curated)}")
assert len(curated) == 194, f"Expected 194, got {len(curated)}"

# Run validation against all 194 items
hard_gate_errors = 0
lint_warnings = 0

for item in input_data["dialogues"]:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    if item_id not in curated:
        print(f"[MISSING] ID {item_id}")
        hard_gate_errors += 1
        continue
    
    trad, note = curated[item_id]
    
    # Check \r
    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1
        
    # Check orphan line start with punctuation after \n
    parts = trad.split("\n")
    for i, line_part in enumerate(parts[1:], 1):
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line {i} starts with orphan punctuation after \\n: {line_part!r}")
            hard_gate_errors += 1
            
    # Check syntactic fracture before \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1
        
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

print(f"\n--- Pre-validation Results ---")
print(f"Total Curated: {len(curated)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("[SUCCESS] All 194 lines passed with 0 errors and 0 warnings!")
else:
    print("[FAIL] Please fix the issues before proceeding.")
    sys.exit(1)

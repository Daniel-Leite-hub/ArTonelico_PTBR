import json
from pathlib import Path

INPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_048_input.json")
OUTPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_048_output.json")

# Dicionário de traduções curadas (ID -> (Texto Curado, Nota Editorial))
CURATIONS = {
    # Event/144.evd (11284 - 11330)
    11284: ("Consegui!", "Lyner celebra a síntese bem-sucedida da Corda Yuteria via Grathmeld."),
    11285: ("Vou levar para a Srta. Claire agora mesmo!", "Lyner parte animado para entregar a corda à dona da taverna."),
    11286: ("Srta. Claire, as cordas ficaram prontas!", "Lyner entrega a encomenda fônica concluída."),
    11287: ("Entregou a [Corda Yuteria].", "Notificação de entrega de item-chave com paridade exata de colchetes."),
    11288: ("Sério mesmo?! Muito obrigada!", "Claire agradece calorosamente a Lyner."),
    11289: ("...Espere só um instantinho.", "Claire pede um momento para afinar o instrumento com a nova corda."),
    11290: ("Pronto, acho que ficou afinado.", "Ajuste e afinação da corda no instrumento."),
    11291: ("Faz tanto tempo... Será que ainda consigo tocar direitinho?", "Claire hesita com modéstia antes de tocar após anos afastada."),
    11292: ("Incrível...", "Lyner fica maravilhado com a canção acústica."),
    11293: ("Fiquei emocionada de verdade...", "Krusche expressa comoção genuína e rara diante da música."),
    11294: ("Isso foi nível de mestre, não acha?", "Jack elogia o talento instrumental de Claire em tom calejado."),
    11295: ("......", "Aurica ouve em silêncio compenetrado e reflexivo."),
    11296: ("Fazia tempo que eu não ouvia a canção da Srta. Claire. É sempre maravilhoso escutá-la.", "Cliente habitual da taverna elogia a apresentação."),
    11297: ("Em vez de tocar uma vez a cada tantos meses, você bem que podia tocar todo dia pra gente!", "Cliente pede apresentações diárias."),
    11298: ("Isso mesmo! Se fizesse isso, eu vinha aqui todo santo dia.", "Freguês reforça o apreço pela atmosfera calorosa."),
    11299: ("Digo o mesmo! Hahaha!", "Gargalhada coletiva na taverna."),
    11300: ("Gente...", "Claire comove-se com o carinho do público."),
    11301: ("Muito obrigada...", "Agradecimento emocionado de Claire."),
    11302: ("Obrigada, de verdade. Não só por fazer as cordas, mas até por me ajudar com a arrumação.", "Correção canônica: 片付け significa arrumação/limpeza, e não 'trazer o fragmento' como NISA errou."),
    11303: ("Não precisa agradecer! É o mínimo depois da música maravilhosa que você tocou para nós.", "Lyner retribui a gentileza de Claire com humildade e gratidão."),
    11304: ("Hehehe, obrigada.", "Risinho carinhoso de Claire."),
    11305: ("Não é algo avassalador como uma Magia da Canção...", "Lyner contrasta o impacto bélico das Reyvateils com a música acústica."),
    11306: ("Mas... me trouxe um calor tão gostoso no peito.", "Lyner descreve a sensação reconfortante e acolhedora da canção."),
    11307: ("...Obrigada. Para mim, esse é o maior elogio de todos.", "Claire recebe comovida a impressão de Lyner."),
    11308: ("Eu sou uma Reyvateil, mas sou do tipo que abandonou a Magia da Canção...", "Claire revela sua recusa em usar o canto como arma bélica."),
    11309: ("...Não costumo falar disso para quase ninguém, mas... antigamente, eu fazia parte da Tenba.", "Claire confidencia seu passado secreto ligada à corporação Tenba."),
    11310: ("Hã?! Sério mesmo?!", "Espanto absoluto de Lyner com o vínculo corporativo pretérito."),
    11311: ("...Sim. Mas, ao ver uma realidade tão distante daquilo que eu buscava... acabei saindo.", "Claire explica sua desilusão ética com os objetivos bélicos da Tenba."),
    11312: ("Diga... Você já parou para pensar no que é o poder de uma canção?", "Claire propõe a questão filosófica central da obra."),
    11313: ("Hã?... Tipo, sem ser como poder mágico ou coisa do tipo...?", "Lyner tenta compreender a distinção entre magia e sentimento."),
    11314: ("Não desse jeito.", "Claire esclarece que não se refere a atributos mágicos."),
    11315: ("Hehe. Uma canção, mais do que qualquer outra coisa, tem o poder de transmitir o coração.", "Definição poética canônica da função primordial da música em Sol Ciel."),
    11316: ("Não é algo visível nem palpável... Então, sempre que falo sobre isso, caçoam de mim, mas...", "Claire reflete sobre a incompreensão do mundo utilitarista."),
    11317: ("Veja só: bastou tocar uma única canção hoje para fazer tanta gente feliz.", "A prova viva da harmonia transmitida pela música desarmada."),
    11318: ("Ah...", "Compreensão de Lyner atingindo o coração."),
    11319: ("Foi por isso que decidi: vou continuar cantando as canções tecidas pelo meu próprio coração... em prol das pessoas comuns.", "O juramento de vida de Claire como cantora popular."),
    11320: ("Uma cantora que é Reyvateil, mas que não recorre aos poderes de uma Reyvateil...", "A singularidade pacífica de sua existência."),
    11321: ("...Hehehe, estranho, não é?", "Humor autodepreciativo afetuoso de Claire."),
    11322: ("Não tem nada de estranho. Acho isso incrível de verdade.", "Lyner valida com entusiasmo caloroso o propósito de Claire."),
    11323: ("Obrigada. Se quiser, venha me ouvir tocar outra vez.", "Convite cordial para visitas futuras."),
    11324: ("Está quase na hora de voltar para Platina...", "Lyner reflete sozinho antes da grande travessia de retorno."),
    11325: ("Mas ainda bem que pude ouvir a canção da Srta. Claire antes da partida...", "Gratidão pelo momento de paz antes do perigo iminente."),
    11326: ("......", "Pausa reflexiva à noite."),
    11327: ("Será que a Senhora Shurelia e o Ayatane estão bem...?", "Preocupação de Lyner com a Deusa e seu companheiro cavaleiro."),
    11328: ("...E o meu pai também...", "Pensamento no Comandante-Geral Leard Barsett."),
    11329: ("Fiquei matutando tanta coisa que nem consigo pegar no sono...", "Insônia provocada pela gravidade dos acontecimentos vindouros."),
    11330: ("Vou dar uma caminhada para arejar a cabeça...", "Lyner sai pela madrugada de Karff para clarear os pensamentos."),

    # Event/152.evd (11331 - 11368)
    11331: ("Isso é...", "O grupo depara-se com o gigantesco obstáculo no Silvaplate."),
    11332: ("...O Portão Pheyna. Foi construído pela Tribo Teru para impedir que os humanos subam além daqui.", "Jack explica a função defensiva do portão ancestral dos Teru."),
    11333: ("Que enorme...", "Krusche impressiona-se com a escala da fortificação."),
    11334: ("Ai, ai... Acabamos vindo parar aqui no fim das contas...", "Jack lamenta o inevitável retorno à sua terra natal Teru."),
    11335: ("De qualquer forma, precisamos que abram este portão. Vamos negociar com a Tribo Teru.", "Lyner assume a iniciativa diplomática."),
    11336: ("...É sério isso?! Nem percam tempo! Não tem a menor chance de abrirem pra gente!", "Jack tenta desesperadamente dissuadir o grupo de abordar os guardas."),
    11337: ("...Não precisa ser tão pessimista. Por acaso você tem algum histórico com eles?", "Lyner nota o nervosismo suspeito de Jack."),
    11338: ("Não tenho nada!", "Jack nega veementemente para esconder suas raízes."),
    11339: ("O-olha só, a Misha e eu vamos esperar aqui. Vão vocês lá pedir para abrirem.", "Jack tenta se esconder na retaguarda junto a Misha."),
    11340: ("...?", "Lyner estranha o comportamento esquivo."),
    11341: ("Humanos... Que negócios vieram tratar aqui?", "Resos interpela o grupo com rispidez na sentinela."),
    11342: ("...!!", "Tensão imediata com a guarda Teru."),
    11343: ("Vocês são... da Tribo Teru?!", "Lyner identifica a raça ancestral dos guardas."),
    11344: ("Exatamente.", "Confirmação marcial de Resos."),
    11345: ("Nós estamos a caminho de Platina! Por favor, abram o portão!!", "Lyner suplica passagem urgente rumo ao cume da Torre."),
    11346: ("Platina, é?", "Resos reage surpreso com o destino mencionado."),
    11347: ("Nós, da Tribo Teru, vivemos aqui justamente para impedir que os humanos subam a Torre.", "Resos reafirma o dever sagrado de isolamento dos Teru."),
    11348: ("Não há conversa sobre isso. É impossível.", "Recusa taxativa da guarda."),
    11349: ("...Não pode ser!", "Consternação de Lyner diante da barreira."),
    11350: ("Se entenderam, tratem de voltar para o Mundo Inferior.", "Resos ordena o recuo imediato dos humanos."),
    11351: ("Espere! O lugar para onde preciso voltar... fica lá em cima!", "Lyner esclarece que sua terra natal é a própria Platina."),
    11352: ("Eu sou um Cavaleiro de Elemia e moro em Platina.", "Lyner declara sua identidade militar de Platina."),
    11353: ("Mesmo assim não vão nos deixar passar por aqui?", "Lyner apela para a justiça de seu regresso."),
    11354: ("......", "Hesitação momentânea de Resos."),
    11355: ("Resos... Traga essas pessoas até mim.", "O Ancião Flute intervém com serenidade de líder."),
    11356: ("Ancião!! ...Entendido.", "Resos acata prontamente a ordem de seu chefe supremo."),
    11357: ("Vocês aí, o Ancião está chamando. Entrem.", "Resos autoriza a entrada protocolar do grupo."),
    11358: ("...Vamos.", "Lyner avança com cautela."),
    11359: ("Harm-da...", "Misha deixa escapar o apelido afetuoso e secreto de infância de Jack."),
    11360: ("S-sua tonta! Não me chama por esse nome!", "Jack entra em pânico cômico ao ter seu nome Teru vocalizado."),
    11361: ("...Harmonica?! É você mesmo, Harmonica?!", "Resos reconhece de imediato o lendário guerreiro Teru fujão."),
    11362: ("Ai, que droga... Tá vendo só?! Já descobriram quem eu sou...", "Jack lamenta a perda do disfarce humano diante dos compatriotas."),
    11363: ("Desculpa... Mas eu não sabia como mais te chamar...", "Misha justifica-se ingenuamente com carinho infantil."),
    11364: ("Há uma bifurcação. Para que lado fica a cidade da Tribo Teru?", "Lyner pede orientação diante do caminho dividido."),
    11365: ("...Escuta aqui, vocês vão mesmo lá?", "Jack ainda tenta evitar o embaraço de reencontrar sua aldeia."),
    11366: ("É claro que vamos! Já viemos até aqui!", "Lyner corta as hesitações de Jack com determinação."),
    11367: ("...Ai, ai, que sufoco. Fica logo adiante: Em Pheyna.", "Jack cede e indica a direção da cidade oculta de Em Pheyna."),
    11368: ("Certo, vamos nessa!", "O grupo parte em direção à morada dos Teru."),

    # Event/301.evd (11369 - 11404)
    11369: ("Ora, perdoem-me. Os meus afazeres sacerdotais acabaram se prolongando um pouco.", "Bispo Falss desculpa-se formalmente pelo atraso no templo."),
    11370: ("Senhor Bispo, gostaria de lhe fazer uma pergunta.", "Radolf aborda o líder religioso com deferência e seriedade."),
    11371: ("Diante desta tempestade devastadora, a Igreja está prestando algum tipo de auxílio ao povo?", "Radolf questiona a inércia institucional frente à catástrofe."),
    11372: ("A tempestade é um fenômeno de ordem natural. Não é algo em que a Igreja possa intervir.", "O Bispo esquiva-se dogmaticamente da responsabilidade social."),
    11373: ("Mesmo que não possamos conter a tempestade, há muito o que fazer pelos aflitos.", "Radolf defende a caridade ativa e o dever de socorro."),
    11374: ("Podemos conter os tumultos, abrigar aqueles que ficaram desamparados...", "Radolf elenca ações emergenciais concretas."),
    11375: ("Não é esse o verdadeiro dever e propósito da Igreja?", "Radolf confronta a essência moral da fé de Elemia."),
    11376: ("......", "Silêncio austero do Bispo."),
    11377: ("Radolf. Creio já ter deixado bem claro: o objetivo supremo desta Igreja é o Advento Divino.", "O Bispo reafirma a obsessão dogmática com o despertar das Deusas."),
    11378: ("No momento, todos os nossos cavaleiros e donzelas sagradas estão totalmente absorvidos por essa missão sagrada.", "Justificativa burocrática para a mobilização total de recursos."),
    11379: ("Não dispomos de tempo para nos preocupar com o populacho.", "Desdém elitista do prelado pelas agruras do povo comum."),
    11380: ("Droga...", "Radolf range os dentes indignado com a frieza de seu superior."),
    11381: ("Sendo assim, eu, Lyner e Aurica nos encarregaremos de socorrer o povo.", "Radolf voluntaria seu destacamento para a assistência popular."),
    11382: ("O que está dizendo?! Lyner e Aurica devem se dedicar a partir de hoje exclusivamente ao Advento Divino.", "O Bispo veta autoritariamente a missão humanitária."),
    11383: ("...O quê?!", "Radolf choca-se com a recusa intransigente."),
    11384: ("Além do mais... uma vez que o Trio de Elemia desperte, os distúrbios populares serão contidos num piscar de olhos.", "Promessa messiânica vazia para justificar a inação presente."),
    11385: ("É preciso ter paciência até lá.", "Apelo hipócrita à resignação dos fiéis."),
    11386: ("Senhor Bispo... vossa concepção está profundamente equivocada. Lyner virá comigo.", "Ruptura dramática de Radolf com a autoridade dogmática corrupta."),
    11387: ("O que pensa que está dizendo?!", "Indignação do Bispo diante da insubordinação aberta."),
    11388: ("Nós faremos todo o possível em prol dos cidadãos castigados pela tempestade. Com sua licença!", "Radolf bate em retirada para cumprir seu dever moral."),
    11389: ("Radolf! Espere!", "O Bispo tenta em vão frear a partida do comandante."),
    11390: ("......", "Tensão silenciosa após a ruptura."),
    11391: ("Tinha certeza disso? Falar daquele jeito com ele...", "Lyner questiona se não foram longe demais na confrontação."),
    11392: ("Se eu não falasse com essa firmeza, ele jamais entenderia.", "Radolf reafirma a necessidade ética de seu posicionamento."),
    11393: ("Mas... o que faremos a partir de agora?", "Lyner pede diretrizes táticas para contornar o bloqueio."),
    11394: ("Tenho um plano. Quando eu explorava a Torre junto à divisão da Igreja, descobri algo.", "Radolf revela uma rota secreta identificada em patrulhas."),
    11395: ("Em Silvaplate, havia uma porta que levava ao interior da Torre.", "Ponto de infiltração alternativo na grande placa estrutural."),
    11396: ("Se conseguirmos abrir aquela porta, talvez seja possível atravessar a Torre por dentro até o Beco Vagalume.", "A rota de passagem interna até o distrito comercial."),
    11397: ("O quê?! Isso é verdade mesmo?!", "Transeunte/espião ouve a conversa com espanto."),
    11398: ("E-esperem um instante. Ainda não é certeza que a porta abrirá.", "Radolf pede cautela para conter boatos prematuros."),
    11399: ("Mas, se abrir, quer dizer que podemos descer até lá embaixo, não é?", "Outro popular vislumbra uma rota de fuga da tormenta."),
    11400: ("É apenas uma possibilidade teórica. Peço que não criem falsas expectativas.", "Radolf enfatiza o caráter incerto da empreitada."),
    11401: ("De qualquer forma, vamos averiguar aquela porta pessoalmente.", "Radolf e Lyner decidem inspecionar o local."),
    11402: ("......", "Murmúrios conspiratórios entre os populares."),
    11403: ("Ei, você ouviu isso?!", "Espanto excitado com a revelação da passagem."),
    11404: ("Sim... É um senhor furo de reportagem!", "Concluem que a descoberta renderá uma grande matéria."),

    # Event/314.evd (11405 - 11449)
    11405: ("Aurica, fique descansando na pousada até melhorar, tá?", "Lyner zela carinhosamente pela recuperação física de Aurica."),
    11406: ("Você deve ter chegado ao seu limite de exaustão. Aproveite para repousar com calma.", "Radolf aconselha repouso disciplinado à jovem Reyvateil."),
    11407: ("Tá bom...", "Aurica anui com voz fraca e desanimada."),
    11408: ("...Entendo. A Aurica...", "Claire escuta a situação com preocupação fraternal."),
    11409: ("Parando para pensar, ela mudou tanto desde pequena.", "Claire relembra o contraste comportamental de Aurica."),
    11410: ("Na época do Vilarejo de Skuwat, ela era bem mais animada, alegre... Uma menina que nunca se dava por vencida.", "O retrato da infância luminosa de Aurica antes do massacre."),
    11411: ("É verdade, você e a Aurica nasceram no mesmo vilarejo, não é?", "Lyner recorda a origem compartilhada em Skuwat."),
    11412: ("Sim, éramos de lá. Quando crianças, eu brincava todo dia com ela. Brincávamos de [Brincar de Deus], por exemplo.", "Revelação da brincadeira canônica de infância com paridade exata de colchetes."),
    11413: ("[Brincar de Deus]...?", "Radolf estranha o conceito sacrílego da brincadeira infantil."),
    11414: ("Ela sempre foi apaixonada pela Lenda de Elemia desde bem pequenininha...", "A fascinação precoce de Aurica pelo mito das Deusas."),
    11415: ("Eu fazia o papel de Deus, e a Aurica o de aldeã. Ela me fazia preces e eu realizava os desejos dela, coisas assim.", "A dinâmica psicológica de dependência projetada desde a infância."),
    11416: ("Esperava tudo cair do céu, hein...", "Lyner comenta a passividade dependente da amiga."),
    11417: ("Pois é. Nisso ela não mudou nada. Desde pequena, vivia dizendo que era incapaz de fazer qualquer coisa sozinha.", "Claire pontua o complexo de inferioridade crônico de Aurica."),
    11418: ("Se ela tivesse mais confiança e lutasse com garra, seria capaz de realizar qualquer coisa...", "Claire expressa seu anseio de ver a irmã postiça florescer."),
    11419: ("Isso é... porque você é a mana Claire... Por isso você consegue...", "Aurica surge febril e fragilizada, confrontando o discurso alheio."),
    11420: ("Aurica! Você está bem?!", "Sobressalto de Lyner ao vê-la fora da cama."),
    11421: ("Não estou nada bem! Fiquei chamando e ninguém veio me acudir... Então vim me arrastando até aqui sozinha!", "Aurica desabafa seu sentimento de abandono e carência."),
    11422: ("Nossa, você estava me chamando?! Desculpa, Aurica...", "Lyner pede perdão encabulado por não ter escutado."),
    11423: ("E além do mais... mana Claire, não fique contando essas historinhas ridículas do meu passado pro Lyner e pros outros!", "Humilhação ferida diante da exposição de suas fraquezas de infância."),
    11424: ("Eu fico morrendo de vergonha... Como é que vou encarar o Lyner de novo depois disso...?!", "Angústia de ver sua imagem arruinada perante o cavaleiro que ama."),
    11425: ("Ora, bobagem! Ninguém liga para historinhas de infância depois que a gente cresce.", "Claire tenta amenizar com naturalidade fraternal."),
    11426: ("É fácil falar para quem teve uma infância brilhante como a sua! Mas a minha não foi assim!", "Rancor e amargura contra a figura perfeita da irmã adotiva."),
    11427: ("Você também me desprezou depois de ouvir essa história, não foi, Lyner?!", "Aurica projeta sua autodepreciação em Lyner."),
    11428: ("É por isso que... quando eu te chamei, você nem se deu ao trabalho de vir!", "Acusação dolorosa fruto da febre e da rejeição imaginada."),
    11429: ("N-não é nada disso! É que por acaso eu...", "Lyner tenta se defender da acusação injusta."),
    11430: ("Mentiroso!", "Grito dilacerante corrigindo o erro de gênero do texto anterior ('Sua mentirosa')."),
    11431: ("Aurica?!", "Choque de Lyner com a agressividade do desabafo."),
    11432: ("O Lyner é um mentiroso! Você não vivia dizendo que sempre ia me proteger?!", "Aurica cobra desesperada a promessa protetora de Lyner."),
    11433: ("Mas nem outro dia, nem hoje... você não me protegeu em nada!", "Dor acumulada dos traumas e ataques virais recentes."),
    11434: ("Aurica!", "Claire tenta intervir para conter a crise."),
    11435: ("Chega, não quero mais saber... Nem do Lyner, nem da mana Claire...", "Rejeição defensiva cortando os laços mais caros."),
    11436: ("Vocês já estão fartos de mim porque sou uma Reyvateil defeituosa, não é?!", "O trauma nuclear de sua identidade estilhaçada vem à tona."),
    11437: ("...O que você está dizendo?! Quando é que vai parar com essa dependência infantil e se manter nos seus próprios pés?!", "Claire perde a paciência e aplica um choque de realidade severo."),
    11438: ("E o que você entende, mana?! Uma aluna exemplar nunca vai saber como se sente uma fracassada como eu!", "A dor do estigma da Reyvateil de Terceira Geração fracassada."),
    11439: ("Aurica!", "Apelo impotente de Claire."),
    11440: ("Chega! Eu odeio você, mana! O Lyner também! Eu odeio todos vocês!!", "Clímax da crise emocional antes da fuga desesperada."),
    11441: ("Aurica!!", "Grito de socorro de Lyner enquanto ela foge."),
    11442: ("Srta. Claire, eu vou atrás dela! A Aurica está ardendo em febre!", "Lyner dispara em perseguição para salvá-la da tempestade."),
    11443: ("O quê?!", "Claire espanta-se com a gravidade da condição de saúde."),
    11444: ("Nós também vamos!", "Radolf mobiliza o apoio imediato na busca."),
    11445: ("Sim.", "Ayatane junta-se à busca na cidade."),
    11446: ("Aurica...", "Culpa e apreensão de Claire deixada para trás."),
    11447: ("Aurica... Onde foi que você se meteu?!", "Desespero de Lyner buscando rastros na chuva torrencial."),
    11448: ("O jeito é revirar a cidade inteira de ponta a ponta até encontrá-la.", "Radolf traça o plano de busca sistemática."),
    11449: ("Aurica deixou o grupo.", "Notificação sistêmica canônica da saída temporária de Aurica da equipe."),

    # Event/653.evd (11450 - 11497)
    11450: ("Lyner, vamos interceptar o Ceifador aqui.", "Misha prepara a emboscada mental contra a manifestação viral."),
    11451: ("Aqui nós temos chance...?", "Lyner avalia as condições do terreno cósmico."),
    11452: ("Sim. Se eu disse lá na Mansão da Lua que não dava para derrotá-lo, foi só porque a Misha de Armadura estava presente.", "Misha revela o estratagema psicológico de isolamento na Cosmosfera."),
    11453: ("Este é o meu mundo. Um mundo onde os meus sentimentos são a força motriz de tudo.", "A regra de ouro da arquitetura ontológica da Cosmosfera."),
    11454: ("Se a Misha de Armadura, que é de um nível superior ao meu, achar que ele é invencível, o Ceifador se tornará invencível de fato. Porque aqui, isso se torna realidade.", "Explicação do perigo do dogma internalizado no estrato psíquico superior."),
    11455: ("Por isso precisávamos ficar a sós, só você e eu.", "A cumplicidade única necessária para quebrar o bloqueio mental."),
    11456: ("Precisávamos ser apenas nós dois, compartilhando a certeza absoluta de que podemos vencê-lo...", "A sinergia inabalável do Dive como arma psíquica."),
    11457: ("Era isso então...! Beleza... agora sim estou confiante! Nós vamos acabar com ele, com certeza!", "Lyner absorve a lógica cósmica e renova seu ardor combativo."),
    11458: ("Humanos... Já escolheram a vossa sepultura? Pois muito bem, vou enterrá-los ali mesmo.", "O Ceifador profere sua sentença sombria na arena da alma."),
    11459: ("Misha, por favor! Mentalize com toda a sua força que eu vou vencer!", "Lyner pede o suporte fônico e volitivo máximo de Misha."),
    11460: ("Entendido!", "Misha projeta sua fé incondicional no parceiro."),
    11461: ("Lá vou eu!! Iaaaaaahhh!!!", "Grito de investida heroica de Lyner."),
    11462: ("Guwaaaaaahhh...!", "Urro de agonia do Ceifador atingido pelo golpe de convicção."),
    11463: ("...Conseguimos?!", "Lyner recupera o fôlego checando o resultado."),
    11464: ("...Derrotamos! Derrotamos o Ceifador! Os nossos sentimentos... revolucionaram o meu destino!", "Misha comemora a aparente quebra da condenação eterna."),
    11465: ("Sim! Agora você finalmente... está livre, Misha...", "Lyner celebra a redenção e emancipação da amiga de infância."),
    11466: ("Sim! Eu não estou mais presa à roda do destino... Agora eu sou verdadeiramente livre...!!", "Misha vislumbra a libertação de seu fardo existencial."),
    11467: ("O... o quê?!", "Súbita convulsão no tecido da mente interrompe o júbilo."),
    11468: ("Kyaah!!", "Grito de pânico diante do choque anômalo."),
    11469: ("O que houve?! O que está acontecendo?!", "Alarme imediato de Lyner diante da desestabilização."),
    11470: ("Tolos insensatos... Como tiveram a audácia de destruir o Ceifador...?!", "A voz severa da Misha de Armadura repreende a ilusão criada."),
    11471: ("O que significa isso?! O que está havendo aqui?!", "Lyner exige respostas da entidade guardiã."),
    11472: ("Por terem destruído o Ceifador, uma discrepância colossal se instaurou entre a realidade e a Misha deste mundo interior.", "Diagnóstico da fratura ontológica entre a psique e a realidade biológica."),
    11473: ("O Ceifador nada mais é do que o reflexo do vírus no mundo real. Eliminar uma mera projeção não mudará em nada a situação dela na realidade.", "A verdade implacável sobre a permanência do vírus físico em Sol Ciel."),
    11474: ("Jamais haverá liberdade genuína por meio de uma ilusão!", "Condenação da fuga psicológica que mascara a servidão real."),
    11475: ("Contudo, nesta mente, uma Misha que reivindica uma liberdade vazia e ilusória tomou posse de parte de seu coração.", "A usurpação mental provocada pelo falso triunfo."),
    11476: ("Disso nasceu um paradoxo irreconciliável dentro de uma única psique...", "O conflito de camadas que ameaça destruir a Reyvateil."),
    11477: ("Não pode ser... Eu estou livre, sim! Ao derrotar o Ceifador, eu me libertei dos grilhões do destino!", "Misha apega-se desesperadamente à fantasia de libertação."),
    11478: ("Uou!", "Tremor violento abala as fundações da Cosmosfera."),
    11479: ("Kyaaaah!!", "Grito de dor com a ruptura do espaço mental."),
    11480: ("É terrível... Nesse ritmo, a própria psique de Misha sofrerá um colapso mental irreversível...!", "Aviso crítico de perigo iminente de colapso cognitivo."),
    11481: ("Você criou a Magia Vermelha [Corte do Vazio]!", "Notificação canônica de síntese da magia ofensiva com paridade estrita de colchetes."),
    11482: ("É a Mudança de Paradigma!!", "Desencadeamento da transição de nível na mente de Misha."),
    11483: ("Lyner, olhe com atenção... Tem algo errado. Os feixes de luz estão completamente instáveis...", "A guia da Cosmosfera alerta para anomalias na torrente de energia."),
    11484: ("...Parando para olhar direito...", "Lyner percebe as distorções sinistras na luz ascendente."),
    11485: ("Essa Mudança de Paradigma ainda está incompleta. Algum fator está bloqueando o amadurecimento de Misha.", "A revelação de que o conflito interno sabotou a evolução harmônica."),
    11486: ("Se ela atravessar esse portal, não fazemos ideia do que acontecerá com a Misha do próximo nível...", "Alerta sobre os riscos sombrios de adentrar um estrato corrompido."),
    11487: ("Uma Mudança de Paradigma deturpada às vezes gera um crescimento totalmente distorcido...", "Teorema fundamental sobre as patologias da Cosmosfera."),
    11488: ("Lá vou eu!! Iaaaaaahhh!!!", "Rota alternativa: Lyner desfere o golpe físico no Ceifador."),
    11489: ("...Droga!... Não deu certo...", "O ataque falha miseravelmente diante da dúvida no coração."),
    11490: ("Lyner...?! O que houve?! Por acaso você não acreditava do fundo do coração que nós venceríamos?!", "Misha sente a hesitação oculta e cobra a quebra de confiança."),
    11491: ("Que isso, Misha...! Eu acreditava com todas as forças! E você, acreditava?!", "Lyner tenta se justificar rebatendo a dúvida para a donzela."),
    11492: ("...Eu estava acreditando com todo o meu ser! É você que não confia em mim, Lyner...", "Racha emocional e perda de sintonia do casal cósmico."),
    11493: ("Não, não foi isso o que eu quis dizer...!", "Lyner tenta em vão remendar o descompasso sentimental."),
    11494: ("O vosso tempo esgotou-se... Chegou a hora de ceifar as vossas vidas.", "O Ceifador ergue sua lâmina fatal diante do fracasso volitivo dos humanos."),
    11495: ("......", "Lyner paralisa sem forças diante do destino adverso."),
    11496: ("Rapaz... parece que você não tem a menor moral com ela, hein.", "Comentário sardônico da guia da Cosmosfera sobre a carência de sintonia."),
    11497: ("Bem, mesmo que o Ceifador fosse derrotado aqui... meus sentimentos quanto a isso seriam bem contraditórios...", "Reflexão cética final sobre a impossibilidade de resolver a vida real por atalhos cósmicos.")
}

def main():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    dialogues = input_data["dialogues"]
    assert len(dialogues) == 214, f"Esperado 214 diálogos, obtido {len(dialogues)}"

    curated_dialogues = []
    curated_lines = []

    for d in dialogues:
        d_id = d["id"]
        assert d_id in CURATIONS, f"Faltando curadoria para ID {d_id}"
        final_text, note = CURATIONS[d_id]

        entry = {
            "id": d_id,
            "event_file": d.get("event_file"),
            "speaker": d.get("speaker"),
            "speaker_id": d.get("speaker_id"),
            "original_jp": d.get("original_jp"),
            "original_en": d.get("original_en"),
            "curated_ptbr": final_text,
            "final_ptbr": final_text,
            "texto_ptbr_curado": final_text,
            "custom_text": final_text,
            "review_status": "approved",
            "reviewed": True,
            "notes": note,
            "curation_notes": note
        }
        curated_dialogues.append(entry)
        curated_lines.append(entry)

    glossary_updates = [
        {
            "term_en": "Yuteria String",
            "term_jp": "ユーテリア弦",
            "term_ptbr": "Corda Yuteria",
            "category": "Item / Síntese Grathmeld",
            "rationale": "Fio condutor de extrema finura e tenacidade sintetizado via Grathmeld para instrumentos musicais e amarrações."
        },
        {
            "term_en": "Pheyna Gate",
            "term_jp": "フェーナ門",
            "term_ptbr": "Portão Pheyna",
            "category": "Cenário / Estrutura",
            "rationale": "Grande fortificação de acesso que isola o Silvaplate e impede a subida de humanos rumo a Platina."
        },
        {
            "term_en": "Em Pheyna",
            "term_jp": "イム・フェーナ",
            "term_ptbr": "Em Pheyna",
            "category": "Localização / Lore",
            "rationale": "Cidade oculta e sagrada da Tribo Teru no Silvaplate, terra natal ancestral de Jack Hamilton."
        },
        {
            "term_en": "Playing God",
            "term_jp": "神様ごっこ",
            "term_ptbr": "[Brincar de Deus]",
            "category": "Lore / Costumes",
            "rationale": "Brincadeira de infância de Claire e Aurica no Vilarejo de Skuwat inspirada na Lenda de Elemia."
        },
        {
            "term_en": "Aura Slicer",
            "term_jp": "虚空破斬",
            "term_ptbr": "Corte do Vazio",
            "category": "Magia da Canção / Vermelha",
            "rationale": "Magia Vermelha ofensiva de Misha tecida na Cosmosfera (赤魔法【虚空破斬】), traduzida em paridade com as habilidades do menu."
        },
        {
            "term_en": "Armor Misha",
            "term_jp": "甲冑のミシャ",
            "term_ptbr": "Misha de Armadura",
            "category": "Cosmosfera / Projeção Mental",
            "rationale": "Manifestação psíquica austera de nível superior na Mansão da Lua que impõe limites dogmáticos à mente de Misha."
        },
        {
            "term_en": "Resos",
            "term_jp": "レッソス",
            "term_ptbr": "Resos",
            "category": "Personagem / Tribo Teru",
            "rationale": "Sentinela leal da Tribo Teru que guarda o Portão Pheyna sob as ordens do Ancião Flute."
        }
    ]

    new_terms = {
        "Yuteria String": {
            "pt": "Corda Yuteria",
            "category": "Item / Síntese Grathmeld",
            "note": "ユーテリア弦. Fio condutor de extrema finura e tenacidade sintetizado via Grathmeld para instrumentos musicais e amarrações."
        },
        "Pheyna Gate": {
            "pt": "Portão Pheyna",
            "category": "Cenário / Estrutura",
            "note": "フェーナ門. Grande fortificação de acesso erguida pela Tribo Teru que isola o Silvaplate e impede a subida de humanos rumo a Platina."
        },
        "Em Pheyna": {
            "pt": "Em Pheyna",
            "category": "Localização / Lore",
            "note": "イム・フェーナ. Cidade oculta e sagrada da Tribo Teru no Silvaplate, terra natal ancestral de Jack Hamilton (Harmonica)."
        },
        "Playing God": {
            "pt": "[Brincar de Deus]",
            "category": "Lore / Costumes",
            "note": "神様ごっこ. Brincadeira de infância de Claire e Aurica no Vilarejo de Skuwat inspirada na Lenda de Elemia, onde Claire fazia o papel de divindade e Aurica o de devota pedinte."
        },
        "Aura Slicer": {
            "pt": "Corte do Vazio",
            "category": "Magia da Canção / Vermelha",
            "note": "虚空破斬 (Kokuuhazan). Magia Vermelha ofensiva tecida na Cosmosfera de Misha (赤魔法【虚空破斬】), harmonizada com o registro do menu 'Corte do Vazio'."
        },
        "Armor Misha": {
            "pt": "Misha de Armadura",
            "category": "Cosmosfera / Projeção Mental",
            "note": "甲冑のミシャ. Manifestação psíquica austera e encouraçada de nível superior na Mansão da Lua que personifica a aceitação do destino trágico."
        },
        "Resos": {
            "pt": "Resos",
            "category": "Personagem / Tribo Teru",
            "note": "レッソス. Sentinela valoroso da Tribo Teru que vigia o Portão Pheyna e reconhece de pronto a fuga do renegado Harmonica."
        }
    }

    scene_handoff_final = {
        "resumo_dramatico": (
            "O bloco BLK_EVD_048 articula cinco momentos narrativos de excepcional carga dramática, caracterização íntima e viradas canônicas: "
            "(1) Em Karff, após Lyner sintetizar a Corda Yuteria via Grathmeld, Claire afina seu instrumento e presenteia a taverna com uma canção acústica comovente; em conversa confissional com Lyner, ela revela seu passado como Reyvateil que abandonou a Tenba e a Magia da Canção bélica para abraçar o verdadeiro poder da música de transmitir o calor do coração às pessoas comuns. "
            "(2) Na ascensão da Torre pelo Silvaplate, o grupo é barrado pelo imponente Portão Pheyna guardado pelo guerreiro Teru Resos; diante do pânico de Jack em ser reconhecido, Misha ingenuamente chama-o de 'Harm-da', expondo seu verdadeiro nome ancestral 'Harmonica' antes de o Ancião Flute franquear a entrada do grupo rumo à cidade oculta de Em Pheyna. "
            "(3) Na Igreja de Elemia do Mundo Inferior, Radolf rebela-se com coragem militar contra a frieza dogmática do Bispo Falss, que recusa socorrer as vítimas da tormenta de plasma em nome do culto cego ao Advento Divino; Radolf rompe ordens e parte com Lyner para inspecionar a passagem interna secreta da Torre em Silvaplate, sendo ouvidos por populares intrigados. "
            "(4) Na estalagem, Aurica, consumida pela febre e pelo complexo de inferioridade crônico de Skuwat, flagra Claire e Lyner conversando sobre sua antiga brincadeira de infância '[Brincar de Deus]'; tomada por um dilacerante sentimento de rejeição e desespero, Aurica tem um colapso emocional, acusa Lyner de ser um mentiroso e foge desabalada pela tempestade, abandonando o grupo. "
            "(5) Na Cosmosfera de Misha (Nível 3 / Mansão da Lua), desenrolam-se duas ramificações cruciais contra o Ceifador: na rota do falso triunfo, a vitória ilusória gera um paradoxo psíquico letal e um quase colapso mental diante dos avisos da Misha de Armadura, culminando na síntese da Magia Vermelha [Corte do Vazio] e em uma Mudança de Paradigma instável; na rota da quebra de confiança, a hesitação de Lyner faz o ataque falhar, deixando evidente a fragilidade dos laços que ainda precisam amadurecer."
        ),
        "decisoes_terminologicas": {
            "Corda Yuteria": "ユーテリア弦 (item alquímico fônico de alta precisão sintetizado por Lyner)",
            "Portão Pheyna": "フェーナ門 (fortificação colossal erguida pela Tribo Teru no Silvaplate)",
            "Em Pheyna": "イム・フェーナ (morada sagrada e isolada da Tribo Teru)",
            "Harmonica": "アルモニカ (nome nativo e ancestral de Jack Hamilton entre os Teru)",
            "Harm-da": "アル兄ぃ (diminutivo carinhoso e infantil usado exclusivamente por Misha)",
            "[Brincar de Deus]": "神様ごっこ / [Playing God] (brincadeira infantil de Skuwat entre Claire e Aurica)",
            "[Corte do Vazio]": "赤魔法【虚空破斬】 / [Aura Slicer] (Magia Vermelha tecida na Cosmosfera de Misha)",
            "Misha de Armadura": "甲冑のミシャ (projeção psíquica encouraçada de nível superior na Mansão da Lua)",
            "Ceifador": "死神 (manifestação mental personificada do vírus na Cosmosfera)",
            "Resos": "レッソス (sentinela militar Teru do Portão Pheyna)",
            "Advento Divino": "神光臨 (dogma do despertar das Deusas priorizado fanaticamente pelo Bispo Falss)"
        },
        "alertas_para_proximo_bloco": (
            "A fuga desesperada de Aurica em meio à febre deixa a donzela desprotegida e o grupo em alerta máximo de busca pela cidade; "
            "ao mesmo tempo, a chegada a Em Pheyna colocará Jack face a face com o Ancião Flute e as feridas abertas de seu povo Teru, "
            "enquanto a instabilidade ontológica da Mudança de Paradigma de Misha projeta sombras sobre o próximo estrato mental."
        )
    }

    highlights = [
        "Confissões éticas de Claire: a distinção ontológica entre a Magia da Canção bélica da Tenba e a música desarmada tecida pelo coração para confortar pessoas comuns, corrigindo o erro da NISA sobre a arrumação da taverna.",
        "A revelação cômica e tensa no Portão Pheyna: o desespero de Jack Hamilton tentando esconder sua origem Teru, traído pelo doce 'Harm-da' de Misha que o expõe perante o sentinela Resos.",
        "O motim virtuoso de Radolf: o rompimento heroico do cavaleiro com a inércia burocrática e dogmática do Bispo Falss para salvar o povo flagelado pela tormenta de plasma.",
        "O dilacerante colapso emocional de Aurica: a ferida exposta de sua infância em Skuwat, o trauma de ser uma Reyvateil considerada defeituosa e o grito de 'Mentiroso!' contra Lyner antes de fugir na tormenta.",
        "O paradoxo psíquico da Cosmosfera de Misha: a destruição do Ceifador como armadilha mental, o risco de colapso cognitivo sob o olhar severo da Misha de Armadura e o despertar da Magia Vermelha [Corte do Vazio]."
    ]

    output_data = {
        "block_id": "BLK_EVD_048",
        "axis_id": "AXIS_3",
        "axis_name": "3_HISTORIA_E_EVENTOS",
        "category": "Event Dialogue",
        "line_count": len(curated_lines),
        "dialogues": curated_dialogues,
        "curated_lines": curated_lines,
        "glossary_updates": glossary_updates,
        "new_terms": new_terms,
        "scene_handoff_final": scene_handoff_final,
        "highlights": highlights
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Sucesso! Gerado {OUTPUT_PATH} com {len(curated_lines)} falas curadas.")

if __name__ == "__main__":
    main()

import json
from pathlib import Path

INPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_052_input.json")
OUTPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_052_output.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

curated_translations = {
    # Event/12.evd
    12232: ("Sua inútil!", "Repreensão brutal do comandante da Tenba à Reyvateil."),
    12233: ("Ai!", "Grito de dor da Reyvateil ao ser agredida fisicamente (correção do errôneo 'Nossa!')."),
    12234: ("Foi por causa da sua lerdeza que a tropa principal nos deixou para trás!", "Justificativa abusiva do oficial da Tenba pela perda de contato com o contingente."),
    12235: ("Senhor comandante, por favor, não brigue com ela desse jeito!", "Apelo desesperado do aldeão em defesa da jovem."),
    12236: ("Essa menina estava apenas protegendo a minha filha de um monstro...", "Esclarecimento comovido da bravura e sacrifício da Reyvateil."),
    12237: ("...Ah, é?", "Reação cínica e indiferente do oficial."),
    12238: ("S-sim...", "Confirmação tímida e amedrontada da Reyvateil."),
    12239: ("Sua idiota! Eu já não cansei de avisar pra você nunca agir por conta própria?!", "Fúria do comandante contra a insubordinação altruísta da cantora."),
    12240: ("Pra começo de conversa, esse vilarejo mal paga um tostão pra gente!", "Pragmatismo mercenário e ganancioso da corporação Tenba."),
    12241: ("Não fique fazendo mais serviço do que o estritamente necessário!", "Ordem rígida de não prestar auxílio além do contrato."),
    12242: ("D-desculpe...", "Pedido de desculpas gaguejado sob coação."),
    12243: ("Acha que um \"desculpe\" resolve alguma coisa?!", "Agressividade implacável do superior rejeitando o pedido de perdão."),
    12244: ("Ugh!", "Gemido de dor sob novo golpe físico."),
    12245: ("Aquele desgraçado...!!", "Indignação moral explosiva de Lyner presenciando a covardia."),
    12246: ("Miserável! O que pensa que está fazendo?!", "Intervenção solene e severa de Radolf impondo autoridade militar."),
    12247: ("E quem diabos é você?!", "Arrogância do comandante Tenba confrontado."),
    12248: ("Sou Radolf, Comandante-Geral da Igreja de Elemia.", "Apresentação oficial com a patente canônica correta (総司 / Comandante-Geral)."),
    12249: ("Comandante-Geral da Igreja...?", "Hesitação atônita do oficial Tenba ao reconhecer a alta patente da Igreja."),
    12250: ("Um engomadinho da Igreja querendo se meter nos assuntos da Tenba?! Tá se achando importante demais!", "Rebeldia desdenhosa contra a jurisdição eclesiástica."),
    12251: ("Isso é uma questão interna da Tenba! Não temos obrigação de ouvir sermão da corja da Igreja!", "Rejeição veemente da interferência moral externa."),
    12252: ("Tenba ou Igreja, nada disso importa!", "Radolf coloca a dignidade humana e o combate à injustiça acima de políticas faccionais."),
    12253: ("Q-que palhaçada é essa de vocês...?", "Recuo intimidado diante da firmeza inabalável de Radolf."),
    12254: ("Cesse essa violência agora mesmo, ou será punido aqui e agora!", "Ultimato marcial severo de Radolf."),
    12255: ("M-malditos... Nunca mais ajudo este vilarejo na minha vida!", "Retirada covarde praguejando contra a população."),
    12256: ("Anda! Você vem comigo! Pare de enrolar!", "Comandante arrasta a Reyvateil à força."),
    12257: ("Ai!", "Exclamação de dor ao ser puxada pelo braço."),
    12258: ("Francamente... É por essas e outras que nunca vou conseguir tolerar essa tal de Tenba.", "Desabafo ético de Radolf repudiando a corporação."),
    12259: ("Ultimamente, as atitudes da Tenba têm passado de todos os limites.", "Cavaleiro subordinado concorda com a escalada abusiva da rival."),
    12260: ("Sim. Sobretudo na forma desumana como tratam as Reyvateils.", "Crítica frontal de Radolf à mercantilização e abuso das donzelas."),
    12261: (".........", "Silêncio constrangido e doloroso de Aurica revivendo traumas."),
    12262: ("...Ficou assustada?", "Sensibilidade paternal e protetora de Radolf."),
    12263: ("Não... Não foi nada...", "Aurica minimiza seu choque para não demonstrar fragilidade."),
    12264: ("Enquanto alguém estiver subordinado à Tenba, esse tipo de covardia é inevitável.", "Diagnóstico sóbrio de Radolf sobre a crueldade corporativa."),
    12265: ("Mas, aqui na Igreja, você estará segura. Ao menos enquanto eu estiver vivo para impedir.", "Promessa solene de Radolf (restauração do provérbio JP 俺の目が黒いうちはな)."),
    12266: ("...", "Olhar tímido e reservado de Aurica."),
    12267: ("Aquela garota...", "Lyner repara nos traços de Aurica."),
    12268: ("Não tenho dúvida. É ela mesma!", "Reconhecimento certo da jovem que ele viu anteriormente."),
    12269: ("Ei, você!", "Lyner chama a atenção de Aurica com informalidade juvenil."),
    12270: ("!", "Susto contido de Aurica."),
    12271: ("Isso aqui não é seu?", "Lyner tenta devolver o pertence perdido."),
    12272: ("Aurica, é seu mesmo?", "Radolf indaga sua protegida."),
    12273: ("Então seu nome é Aurica! Eu sou o Lyner. Muito prazer!", "Simpatia aberta e calorosa de Lyner."),
    12274: ("...", "Hesitação desconfiada de Aurica."),
    12275: ("Não. Isso não é meu...", "Aurica nega a posse com frieza defensiva."),
    12276: ("E afinal de contas... quem é você?", "Barreira interpessoal erguida por Aurica contra estranhos."),
    12277: ("Ué? Vocês não se conheciam?", "Estranhamento de Radolf diante do mal-entendido."),
    12278: ("...Não conheço ele.", "Rejeição categórica de Aurica."),
    12279: ("Hã?! E-espera aí...", "Lyner perplexo com o corte repentino."),
    12280: ("O que deu nela? Eu podia jurar que era aquela garota...", "Monólogo interior de Lyner coçando a cabeça."),
    12281: ("Deixa pra lá. Mais importante agora é dar um jeito no dirigível e no cristal...", "Lyner reorienta o foco para sua missão primária no Mundo Inferior."),
    12282: ("Parece bem movimentado por aqui. Quem sabe eu não acho alguma pista? Vou dar uma olhada.", "Decisão de explorar a área comercial de Karulu."),
    12283: ("Você liberou o acesso à [Loja de Descontos] e à [Pousada da Torre]!", "Notificação de sistema com os nomes padronizados do mapa urbano."),
    12284: ("Você pode se deslocar para esses locais através do mapa da cidade.", "Instrução de tutorial de navegação rápida."),

    # Event/135.evd
    12285: ("Ela tá logo embaixo! Vamos pular!", "Lyner avista Aurica em perigo e decide saltar sem hesitar."),
    12286: ("...É sério isso?!", "Jack estarrecido com a impulsividade suicida de Lyner."),
    12287: ("Não...!", "Grito de pânico de Aurica encurralada pela máquina."),
    12288: ("Aurica!", "Grito de socorro e apoio de Lyner."),
    12289: ("...! L-Lyner?!", "Aurica surpresa com o resgate milagroso."),
    12290: ("Guh...!", "Impacto da aterrissagem pesada de Jack."),
    12291: ("Vamos nessa!", "Lyner parte para a ofensiva contra o robô."),
    12292: ("Aurica, você tá bem?", "Lyner checa a integridade física de Aurica após o combate."),
    12293: ("...Lyner, você tá são e salvo!", "Alívio emocionado de Aurica ao ver Lyner ileso."),
    12294: ("Sim. Desculpa ter te deixado preocupada...", "Lyner demonstra consideração e carinho sincero."),
    12295: ("...", "Aurica abaixa a cabeça consumida pela culpa."),
    12296: ("Aurica? ...Você ficou brava comigo?", "Lyner estranha o silêncio pesaroso dela."),
    12297: ("...", "Permanência em silêncio hesitante."),
    12298: ("Desculpa, Aurica...", "Lyner assume a culpa sem entender o real motivo."),
    12299: ("Não, não é isso...", "Aurica desfaz o mal-entendido com voz sumida."),
    12300: ("...Lyner, eu... só fui um estorvo para você de novo...", "Complexo de inferioridade e trauma de inutilidade de Aurica (足手まとい)."),
    12301: ("...Hã?", "Lyner pego de surpresa pelo autoflagelo dela."),
    12302: ("Você teve que vir me salvar do ataque daquele robô...", "Aurica lamenta sua incapacidade de se defender sozinha."),
    12303: ("Eu só causei mais problemas para você... Me perdoa...", "Humildade dolorosa e pedido de desculpas emocionado."),
    12304: ("Aurica!", "Radolf chega correndo ao local do resgate."),
    12305: ("...Lyner!!", "Radolf aliviado ao encontrar ambos inteiros."),
    12306: ("Ah, continuam vivos.", "Sarcasmo e alívio seco de Krusche."),
    12307: ("Vocês dois estão sãos e salvos! Que alívio!... E o cristal?", "Radolf celebra o bem-estar dos jovens e cobra o objetivo da missão."),
    12308: ("Claro que conseguimos!", "Orgulho jovem e confiante de Lyner."),
    12309: ("Conseguiram?! Que maravilha, que alívio!!", "Entusiasmo efusivo e risonho do Comandante Radolf."),
    12310: ("Bom... mas foi graças ao Jack que a gente conseguiu.", "Modéstia e reconhecimento leal de Lyner ao veterano."),
    12311: ("...J-Jack?!", "Krusche reconhece a voz e o nome do devedor."),
    12312: ("Ora, ora! Então quer dizer que o Jack salvou a sua vida, Lyner? Hahaha!", "Radolf admira a proeza militar do mercenário."),
    12313: ("Que isso, não foi nada demais... Hmpf...", "Pose canastrona e modéstia fingida de Jack."),
    12314: ("...", "Krusche medindo o alvo com olhar predador."),
    12315: ("Ora, ora, Jack~ Mas que imeeeeensa alegria revê-lo!", "Entonação teatral e afetação de falsa dama da sociedade."),
    12316: ("...Nossa, até fico sem jeito com tanto carinho. E de onde seria essa distinta senhorita?", "Jack galanteador até notar a identidade da mecânica."),
    12317: ("Guh!!!! ...V-v-você...?!", "Choque apavorado de Jack ao encarar sua credora implacável."),
    12318: ("??", "Lyner sem entender nada da dinâmica prévia entre os dois."),
    12319: ("Mas que coincidência fantástica nos encontrarmos justamente aqui!", "Krusche fechando o cerco com ironia cortante."),
    12320: ("Agora, indo direto ao ponto... que tal quitar todinho aquele calote da manutenção passada de uma vez por todas?!", "Cobrança direta da fatura atrasada com firmeza hilária."),
    12321: ("E-espera aí, foi tudo tão de repente que eu tô sem um tostão furado aqui comigo...", "Gagueira e desculpas esfarrapadas de Jack encurralado."),
    12322: ("Ah, é? Então que tal eu reverter esse seu braço pro estado que tava antes da manutenção agora mesmo?!", "Ameaça cirúrgica e desastrosa de desmontar a prótese gatling."),
    12323: ("Piedade, mulher, dá uma folga aí...", "Jack implorando por clemência diante do desmonte iminente."),
    12324: ("Ué, vocês dois se conhecem?", "Lyner ligando os pontos com humor."),
    12325: ("Sou eu que faço a manutenção da metralhadora giratória no braço dele.", "Krusche explica a relação profissional de longa data."),
    12326: ("Se bem que ele quase nunca me pagou um único centavo!", "Indignação comercial de Krusche com o caloteiro crônico."),
    12327: ("Por favor! Deixa passar só por hoje! Por favorzinho, vai?!", "Jack humilhando-se em súplica cómica."),
    12328: ("Hahaha! Você tá numa enrascada das grandes, Jack...", "Riso franco de Lyner diante da derrocada da pose durona de Jack."),
    12329: ("Ei, parem de discutir negócios num lugar desses. O que tínhamos que fazer já foi feito, vamos sair logo daqui.", "Intervenção disciplinar e prática de Radolf recompondo a marcha."),
    12330: ("...Aurica?", "Lyner percebe que Aurica voltou a se recolher."),
    12331: ("...", "Hesitação silenciosa de Aurica."),
    12332: ("Tudo bem com você?", "Lyner checa a estabilidade emocional da amiga."),
    12333: ("...Sim, tô ótima, de verdade.", "Sorriso amarelo de Aurica forçando normalidade para não preocupar."),
    12334: ("...", "Lyner pressente que há algo mais profundo não dito."),

    # Event/797.evd
    12335: ("Ei, Misha! Antes de irmos, tem uma coisa que eu queria te perguntar.", "Lyner puxa assunto sério com Misha na Cosmosfera de Shurelia."),
    12336: ("...O quê?", "Misha receptiva mas atenta à indagação."),
    12337: ("O que a Claire quis dizer quando falou de \"personalidade original\"? A personalidade de agora da senhorita Togasaki é diferente de antes?", "Dúvida existencial sobre o passado e natureza de Leila Togasaki."),
    12338: ("...E por que você quer saber disso?", "Misha avalia as reais motivações de Lyner antes de abrir a verdade."),
    12339: ("É que...", "Hesitação sincera de Lyner."),
    12340: ("Se a minha resposta for a pior coisa possível, muito além de tudo o que você imagina... o que você vai fazer?", "Teste moral de Misha sobre a resiliência emocional do mergulhador."),
    12341: ("Vai abandonar a Leila e sair correndo?", "Provocação incisiva sobre o medo de desilusão romântica."),
    12342: ("...De jeito nenhum!", "Determinação inflexível de Lyner."),
    12343: ("Tem certeza? Porque vou logo avisando que a verdade vai ser um tremendo choque para você.", "Aviso prévio da gravidade do segredo cósmico."),
    12344: ("...Não importa o que seja. Seja lá qual for a verdade, o que eu sinto pela senhorita Togasaki jamais vai mudar.", "Declaração de lealdade incondicional ao coração de Leila."),
    12345: ("Está bem. Então prepare o seu coração.", "Restauração da firmeza solene de Misha (restaurando o JP 心して聞いて)."),
    12346: ("...", "Lyner aguarda com respiração suspensa."),
    12347: ("Leila Togasaki é... uma forma de vida viral.", "Revelação ontológica: Togasaki é um vírus (ウイルス生命体)."),
    12348: ("...!! Um vírus...?! Como assim um vírus... Não pode ser...", "Choque dilacerante e negação imediata de Lyner."),
    12349: ("Isso mesmo. Igual ao professor A.B.R. e àquela fera chamada ELMA de antes. Ela foi criada como a arma suprema da Facção Mir...", "Conexão com os vírus hostis e o projeto militar da Facção Mir (ミュール団)."),
    12350: ("Não pode ser... A senhorita Togasaki... ser um vírus...", "Dissonância cognitiva entre o amor doce de Leila e uma entidade viral destruidora."),
    12351: ("Eu a tirei de lá. Reescrevi o programa dela, apaguei os dados do passado e programei uma nova missão.", "Origem da persona Shurelia: ato redentor de reprogramação realizado por Misha."),
    12352: ("Essa é a Shurelia... Ou seja, a verdadeira identidade de Leila Togasaki.", "A síntese entre o vírus bélico e a santa de Platina."),
    12353: ("Tirou de lá...? Espera aí, Misha... quem é você...?", "Lyner atônito deduzindo as credenciais ocultas de sua guia."),
    12354: ("...Ex-oficial de alto escalão da Facção Mir. Programadora de vírus sob as ordens diretas de Claire: Misha Arsellec Lune...", "Confissão de culpa e identidade ancestral na paródia cósmica."),
    12355: ("Você também fazia parte da Facção Mir?!", "Espanto colossal ao descobrir o passado inimigo de sua amiga de infância."),
    12356: ("Vai me derrotar? Então derrote. Não vou revidar contra você. Pode me atacar o quanto quiser.", "Vulnerabilidade corajosa de Misha entregando-se ao julgamento dele."),
    12357: ("Mas depois não venha reclamar. Você vai ter que resgatar a Leila sozinho.", "Alerta pragmático de que o ódio cego isolará Lyner da vitória."),
    12358: ("...", "Silêncio reflexivo de Lyner processando o preconceito."),
    12359: ("Se você sente ódio de mim agora... isso só prova que você julga as pessoas por \"rótulos\", e não pelos sentimentos delas.", "Lição filosófica sobre julgar a essência (想い) em vez do título (肩書き)."),
    12360: ("......", "Internalização madura da crítica."),
    12361: ("Acho que peguei um pouco pesado demais com você.", "Misha suaviza a postura ao ver a dor do rapaz."),
    12362: ("Mas, se o seu coração não amadurecer a ponto de compreender isso, mesmo que traga a Leila de volta, você vai fraquejar de novo.", "Necessidade de maturidade psíquica para acolher a totalidade do ser amado."),
    12363: ("...E, se isso acontecer... acabará repetindo o mesmo erro.", "Alerta contra a armadilha da ilusão idealizada."),
    12364: ("...Obrigado, Misha. Eu tô bem.", "Lyner reconquista o equilíbrio e a gratidão."),
    12365: ("Obrigado por me contar tudo com sinceridade. Eu acredito em você, Misha.", "Aceitação incondicional: laço de confiança mútua reforçado."),
    12366: ("...Bom, não temos tempo a perder. Vamos depressa...", "Misha comovida retoma o comando da operação de resgate."),
    12367: ("M-mas o que é tudo isso...?!", "Lyner impressionado com a magnitude da câmara tecnológica."),
    12368: ("É o Repositório de Programas Virais. Dentre todos os sistemas que já projetei, é a minha maior obra-prima... e a pior criação de todas.", "Apresentação solene do Virus Program Storage (ウイルスプログラムストレージ)."),
    12369: ("O quê...? Foi você quem construiu toda essa máquina, Misha?!", "Assombro diante do gênio científico aterrador de Misha."),
    12370: ("...Sim. É aqui dentro que ficam armazenados os mais diversos vírus desenvolvidos até hoje.", "Confirmação do acervo bélico concentrado no local."),
    12371: ("...Quer dizer que a senhorita Togasaki também...?", "Compreensão de que o berço de Leila foi aquela fábrica de armas."),
    12372: ("Sim. Foi aqui que ela nasceu.", "Misha confirma a criação do vírus Leila naquele núcleo."),
    12373: ("...", "Aperto no coração diante da frieza do maquinário."),
    12374: ("...", "Leila em transe catatônico de contenção."),
    12375: ("Leila!!", "Grito angustiado de Misha tentando alcançá-la."),
    12376: ("Senhorita Togasaki...", "Lyner comovido ao reencontrar a jovem sob custódia."),
    12377: ("Ora, ora, que demora. Já peguei a minha querida Shurelia de volta!", "Entrada triunfal e zombeteira da vilã Claire."),
    12378: ("...Chegamos tarde demais?!", "Desespero de Misha vendo a reversão do programa."),
    12379: ("Fufufu. Você per-deu! Fim de jogo para vocês.", "Deboche clássico de Claire decretando derrota."),
    12380: ("...", "Tensão máxima na câmara."),
    12381: ("Aproveitando a ocasião, que tal a Shureliazinha dar um fim em vocês agora mesmo? Acabe com esses traidores!", "Claire comanda o vírus rearmado para exterminar os intrusos."),
    12382: ("O quê?!", "Lyner em choque ao ser apontado como alvo."),
    12383: ("...Droga...!!", "Frustração combativa de Misha."),
    12384: ("...Iniciando ataque.", "Leila operando sob protocolo mecanicista desprovido de afeto."),
    12385: ("...Olhe aquilo! Lyner, a lavagem cerebral da Leila ainda não está completa!", "Misha identifica a brecha de segurança no processo de controle."),
    12386: ("É sério?!", "Esperança renascida no cavaleiro."),
    12387: ("Sim! Aquelas três esferas diante da Leila estão apenas mantendo a lavagem cerebral externamente!", "Análise tática dos emissores externos de controle mental."),
    12388: ("Então, se destruirmos apenas essas três esferas...!", "Lyner traça o plano de ataque focado nos emissores."),
    12389: ("Isso... a Leila será libertada dessa prisão mental!", "Misha confirma a condição de vitória e libertação."),
    12390: ("...Ué? Onde é que eu tô...?", "Lyner acorda no mundo real após derrota/expulsão temporária."),
    12391: ("Seja bem-vindo de volta! Parece que você tomou um Fim de Jogo.", "Shurelia acolhe Lyner no mundo de vigília com doçura cômica."),
    12392: ("Ai, ai, ai... de novo não...", "Lamento descontraído de Lyner por ter falhado."),
    12393: ("Parece que você pode tentar quantas vezes quiser, então talvez seja uma boa ideia tentar de novo quando puder.", "Estímulo paciente de Shurelia para tentar novas abordagens."),

    # Event/440.evd
    12394: ("Ah, Lyner! Bom dia!", "Saudação matinal afetuosa e reconfortante de Aurica."),
    12395: ("A-ah... Bom dia.", "Lyner responde ainda atordoado e abatido pelo pesadelo."),
    12396: ("O que aconteceu? Você parece tão desanimado...", "Empatia aguçada de Aurica percebendo o semblante pesado dele."),
    12397: ("Hã? Ah... é...", "Lyner desconversa hesitante."),
    12398: ("...Está tudo bem?", "Carinho sincero de Aurica oferecendo ombro amigo."),
    12399: ("Não precisa me olhar com essa cara de preocupada.", "Lyner tenta poupar a amiga de seu sofrimento interno."),
    12400: ("...Ei, Aurica. Desculpa te incomodar com isso, mas posso desabafar uma coisa com você?", "Lyner cede à necessidade de partilhar a angústia com quem confia."),
    12401: ("O que é isso?! Claro que pode!", "Acolhimento imediato, generoso e sem hesitação de Aurica."),
    12402: ("...Entendi. Então você sonhou com a Senhora Shurelia...", "Aurica compreende a ferida aberta da perda da deusa."),
    12403: ("...Foi.", "Confirmação dolorosa de Lyner."),
    12404: ("Quando eu olho em volta, todo mundo parece tão feliz...", "Contraste agridoce entre a paz geral e o vazio individual."),
    12405: ("A Mir desapareceu, os vírus sumiram... não restou mais nada para apavorar ninguém.", "A vitória oficial contra a calamidade viral."),
    12406: ("...Mas...", "A inquietação moral que corrói o herói."),
    12407: ("Eu simplesmente não consigo acreditar que aquele tenha sido o melhor desfecho...", "Recusa em aceitar que o sacrifício de Shurelia tenha sido o único caminho."),
    12408: ("Não... Isso é loucura...! Se você entoar essa Canção, vai sumir junto comigo!", "Flashback: o clamor estarrecido de Mir diante do Suspend de Shurelia."),
    12409: ("...Senhora Shurelia! Não faça isso!!", "Flashback: o grito de desespero impotente de Lyner."),
    12410: ("Eu já estou preparada. Mesmo assim, eu... este mundo...", "Flashback: a nobreza trágica e resolução altruísta da deusa."),
    12411: ("Eu quero... salvar este mundo!!", "Flashback: o amor sublime e absoluto de Shurelia pela humanidade."),
    12412: ("Eu quero... salvar este mundo...", "Flashback: o eco etéreo do sacrifício ecoando na mente de Lyner."),
    12413: ("Naquele momento, nós tínhamos ido lá para resgatar a Senhora Shurelia.", "O sentimento de fracasso pessoal na missão de cavaleiro."),
    12414: ("Só que... nós não fomos capazes de salvá-la.", "A amargura do herói que não conseguiu salvar quem mais amava e admirava."),
    12415: ("...Lyner.", "Aurica enternecida pela vulnerabilidade e nobreza de Lyner."),
    12416: ("Pode ser verdade que a Senhora Shurelia tenha confiado este mundo a nós.", "Reconhecimento do legado sagrado deixado pela administradora."),
    12417: ("Quando aquela batalha terminou, nós descemos, vimos o mundo em paz e comemoramos...", "A lembrança da euforia efêmera do retorno."),
    12418: ("Tive a ilusão de que tudo tinha acabado bem... mas não foi nada disso.", "A revelação de que uma paz comprada com uma vida inocente não é vitória."),
    12419: ("...Eu entendo perfeitamente o que você sente. Isso também não saía da minha cabeça...", "Sintonia empática profunda de Aurica compartilhando a mesma culpa."),
    12420: ("Só que... depois de tudo o que já aconteceu...", "O peso do fatalismo que parece impedir qualquer ação posterior."),
    12421: ("Ainda pode haver um jeito de salvá-la!", "A centelha de esperança inabalável que redefine o protagonista."),
    12422: ("Lyner?!", "Aurica surpresa com o lampejo de audácia."),
    12423: ("A Senhora Shurelia... morreu de verdade? Aquilo foi mesmo o que nós chamamos de \"morte\"?", "Questionamento ontológico brilhante sobre a natureza biomecânica e cósmica de uma Origin."),
    12424: ("Eu não sei explicar direito... mas sinto que ainda tem alguma coisa que nós não tentamos.", "Intuição heroica de que a busca não se esgotou."),
    12425: ("...", "Aurica contemplando a fé contagiante de Lyner."),
    12426: ("É verdade. Talvez ainda seja cedo demais para desistir.", "Aurica decide apoiar a cruzada com renovada determinação."),
    12427: ("Lyner... por que não conversamos com o seu pai... digo, com o Comandante?", "Sugestão tática de Aurica recorrendo aos arquivos e autoridade de Platina."),
    12428: ("Aurica entrou para o grupo!", "Mensagem canônica de sistema confirmando a união formal da dupla para a Fase 3."),

    # Event/572.evd
    12429: ("...E aí.", "Saudação despojada e contida de Jack quebrando anos de distanciamento."),
    12430: ("O que houve para vir assim tão de repente?", "Flute surpreso com o reaparecimento inesperado do renegado."),
    12431: ("Nada... Só queria te pedir um favor.", "Jack mantém sua pose durona para disfarçar o afeto filial/fraterno."),
    12432: ("Você me pedindo um favor... Há quantos anos isso não acontecia...?", "Nostalgia solene do líder Teru rememorando os laços do passado."),
    12433: ("O meu \"desejo mais profundo\", é...?", "Flute medita sobre o conceito místico de cristalização do sentimento (想い)."),
    12434: ("Seria... que as pessoas pudessem viver em paz neste mundo sem precisar de um único mandamento sequer.", "A aspiração utópica máxima do patriarca: uma harmonia tão pura que dispense leis rígidas."),
    12435: ("V-você...? Jamais imaginei ouvir da sua boca palavras que renegassem os mandamentos...", "Choque genuíno de Jack ouvindo o guardião dogmático relativizar a regra suprema."),
    12436: ("Nem eu tenho apreço por mandamentos. Eles são um mal necessário.", "Restauração magistral do conceito ontológico Teru (掟は必要悪である)."),
    12437: ("Apenas compreendo que, enquanto eles existirem, nós temos o dever de cumpri-los.", "A ética estóica da responsabilidade coletiva para evitar o caos."),
    12438: ("Afinal de contas... os mandamentos são a síntese de todas as provações e sacrifícios acumulados pelos nossos ancestrais.", "Valorização da memória histórica e das feridas acumuladas pela tribo."),
    12439: ("Por essa mesma razão, eles servem para guiar o nosso povo com firmeza rumo ao bem maior.", "A função protetora e teleológica dos preceitos arcaicos."),
    12440: ("Contudo... ultimamente comecei a pensar que até esses \"mandamentos\" precisam se adaptar com flexibilidade às mudanças dos tempos.", "Abertura filosófica à evolução moral e flexibilidade perante novas gerações."),
    12441: ("...Flute!", "Jack comovido ao ver o antigo mestre e líder reconhecer seus motivos."),
    12442: ("O que você me dizia... no fim das contas, tinha mesmo razão.", "A consagração moral tardia da rebeldia de Jack em nome da compaixão viva."),
    12443: ("Olha só... Você ficou bem mais compreensivo do que era antes.", "Jack disfarça a emoção com leve ironia afetuosa."),
    12444: ("É verdade. Todos esses acontecimentos recentes me deram muito o que refletir. Além do mais...", "Amadurecimento doloroso do Ancião diante dos traumas da guerra."),
    12445: ("No fim das contas... nós ainda precisamos muito de você ao nosso lado, Harmonica.", "Apelo de reconciliação chamando o veterano por seu nome de batismo sagrado."),
    12446: ("...Hehe. Então é isso? Bom... não seria nada mau voltar aos velhos tempos.", "Aceitação calorosa de Jack vislumbrando o retorno ao seu lar ancestral."),
    12447: ("Bom, mas agora eu tenho que ir andando. Ainda tenho outros lugares para visitar.", "Compromisso inabalável com a missão antes de gozar de seu merecido repouso."),
    12448: ("Harmonica!", "Clamor final de Flute transbordando respeito e culpa acumulada."),
    12449: ("Por tudo até hoje... me perdoe...", "O pedido formal de perdão histórico pelas incompreensões e rigidez do passado."),
    12450: ("...Eu que te peço perdão.", "Reciprocidade e redenção mútua entre mestre e aprendiz."),
    12451: ("Só que... eu ainda tenho algumas coisas inacabadas para resolver.", "A honra do mercenário que jamais abandona companheiros de batalha."),
    12452: ("Não sei quanto tempo ainda vai levar... mas você esperaria até eu terminar tudo?", "Pacto de espera e esperança entre a tribo e o guerreiro."),
    12453: ("Sim... com toda certeza.", "Consentimento paternal caloroso selando o destino pacífico de Em Pheyna."),
    12454: ("Hehe... Fico te devendo essa.", "Sorriso cúmplice e agradecimento sincero de Jack."),
    12455: ("Vai ser mais uma despedida um pouco longa, mas se cuida.", "Despedida comovente restaurada com base na ternura do original japonês."),
    12456: ("...Você também.", "Votos de vida longa e proteção mútua."),
    12457: ("...", "Jack parte em silêncio com o coração finalmente pacificado."),
}

dialogues_out = []
curated_lines_out = []

for item in input_data["dialogues"]:
    d_id = item["id"]
    if d_id not in curated_translations:
        raise ValueError(f"Falta tradução para ID {d_id}")
    
    text, note = curated_translations[d_id]
    
    entry = {
        "id": d_id,
        "event_file": item.get("event_file", ""),
        "speaker_id": item.get("speaker_id", 0),
        "speaker": item.get("speaker", ""),
        "original_jp": item.get("original_jp", ""),
        "original_en": item.get("original_en", ""),
        "curated_ptbr": text,
        "final_ptbr": text,
        "texto_ptbr_curado": text,
        "custom_text": text,
        "review_status": "approved",
        "reviewed": True,
        "notes": note,
        "curation_notes": note
    }
    dialogues_out.append(entry)
    curated_lines_out.append(entry)

new_terms = {
    "Virus Lifeform": {
        "pt": "Forma de Vida Viral",
        "gender": "feminino",
        "number": "singular",
        "category": "Lore / Cosmosphere",
        "note": "ウイルス生命体. Entidade bioviral consciente e programável sintetizada na simulação cósmica, revelando a verdadeira identidade de Leila Togasaki (Shurelia)."
    },
    "Virus Program Storage": {
        "pt": "Repositório de Programas Virais",
        "gender": "masculino",
        "number": "singular",
        "category": "Localização / Cosmosphere",
        "note": "ウイルスプログラムストレージ. Sistema colossal projetado por Misha na paródia colegial onde todas as matrizes e cepas virais da Facção Mir eram compiladas e guardadas."
    },
    "Teru Commandments": {
        "pt": "Mandamentos dos Teru",
        "gender": "masculino",
        "number": "plural",
        "category": "Lore / Tribo Teru",
        "note": "掟 (okite). Dogmas ancestrais rígidos concebidos como mal necessário (必要悪) pela Tribo Teru para preservar sua linhagem, cuja flexibilização permitiu a reconciliação entre Flute e Harmonica (Jack)."
    },
    "General Discount Shop": {
        "pt": "Loja de Descontos",
        "gender": "feminino",
        "number": "singular",
        "category": "Comércio / Localização",
        "note": "雑貨屋・爆安一番. Estabelecimento comercial popular de Karulu desbloqueado no início da aventura, padronizado com o rótulo do mapa urbano (BLK_SYS_031 ID 30213)."
    },
    "Tower Inn": {
        "pt": "Pousada da Torre",
        "gender": "feminino",
        "number": "singular",
        "category": "Hospedaria / Localização",
        "note": "宿屋・塔の下亭. Hospedaria acolhedora aos pés de Sol Ciel em Karulu, padronizada em harmonia com a sigla abreviada de menu 'Pous. Torre' (BLK_SYS_031 ID 29180/30212)."
    }
}

glossary_updates = [
    {
        "term_en": "Virus Lifeform",
        "term_jp": "ウイルス生命体",
        "term_ptbr": "Forma de Vida Viral",
        "category": "Lore / Cosmosphere",
        "rationale": "Revelação existencial em Shurelia Nível 8 sobre a matriz ontológica de Leila Togasaki."
    },
    {
        "term_en": "Virus Program Storage",
        "term_jp": "ウイルスプログラムストレージ",
        "term_ptbr": "Repositório de Programas Virais",
        "category": "Localização / Cosmosphere",
        "rationale": "Câmara-núcleo criada por Misha para armazenar matrizes de vírus bélicos na Facção Mir."
    },
    {
        "term_en": "Teru Commandments",
        "term_jp": "掟",
        "term_ptbr": "Mandamentos dos Teru",
        "category": "Lore / Tribo Teru",
        "rationale": "Preceitos arcaicos da Tribo Teru explicados por Flute como 'mal necessário' acumulado por provações ancestrais."
    },
    {
        "term_en": "General Discount Shop",
        "term_jp": "雑貨屋・爆安一番",
        "term_ptbr": "Loja de Descontos",
        "category": "Comércio / Localização",
        "rationale": "Padronização canônica com o mapa urbano de Karulu (ID 30213)."
    },
    {
        "term_en": "Tower Inn",
        "term_jp": "宿屋・塔の下亭",
        "term_ptbr": "Pousada da Torre",
        "category": "Hospedaria / Localização",
        "rationale": "Padronização canônica com o mapa e hospedarias de Karulu (ID 29180/30212)."
    }
]

scene_handoff_final = {
    "resumo_dramatico": "O bloco BLK_EVD_052 consolida cinco momentos axiais de lore, comédia de relacionamentos e superação emocional da narrativa: (1) Em Karulu (Event/12.evd), um oficial tirânico da Tenba espanca e humilha uma jovem Reyvateil por ter protegido a filha de um aldeão fora do contrato; o Comandante-Geral Radolf intervém com autoridade marcial inflexível, põe os agressores em fuga e promete a Aurica segurança na Igreja 'enquanto eu estiver vivo'; Lyner reconhece Aurica e tenta devolver seu pingente, mas ela o repele com desconfiança e frieza protetora. (2) Na emboscada robótica (Event/135.evd), Lyner e Jack saltam para salvar Aurica; Aurica desmorona em culpa julgando-se um fardo inútil, enquanto Krusche reencontra Jack e o encurrala com humor impiedoso exigindo a quitação imediata do calote histórico na manutenção de seu braço-gatling sob ameaça de reversão mecânica forçada. (3) Na Cosmosfera de Shurelia (Event/797.evd), Misha testa os sentimentos de Lyner e revela o segredo mais aterrador da simulação escolar: Leila Togasaki é na verdade uma forma de vida viral desenvolvida como arma suprema da Facção Mir, reprogramada secretamente pela própria Misha; Lyner supera o choque e reafirma sua fé incondicional no coração de Leila e na lealdade de Misha; eles invadem o Repositório de Programas Virais onde Claire tenta usar Shurelia contra eles, mas Misha instrui Lyner a destruir os emissores externos antes de sofrerem uma expulsão temporária acolhida com doçura pela deusa em vigília. (4) No amanhecer pós-Mir (Event/440.evd), Lyner desabafa com Aurica sua recusa em aceitar a perda trágica de Shurelia na Canção do Sacrifício Supremo, questionando se a deusa realmente 'morreu' no sentido humano; contagiada pela esperança do jovem, Aurica decide ingressar no grupo para buscar a sabedoria do Comandante de Platina. (5) No Portão Pheyna (Event/572.evd), Jack visita o líder Teru Flute em busca de seu 'desejo mais profundo'; Flute surpreende ao admitir que os mandamentos ancestrais são um mal necessário que deve se dobrar aos novos tempos, pedindo perdão a Jack por sua rigidez do passado e celebrando com lágrimas a promessa de retorno definitivo de Harmonica à sua terra natal.",
    "decisoes_terminologicas": {
        "Comandante-Geral": "Radolf como líder dos Cavaleiros da Igreja (エル・エレミア教会総司)",
        "Comandante de Platina": "General Leard Barsett, pai de Lyner (プラティナの総帥)",
        "Forma de Vida Viral": "Natureza ontológica de Leila Togasaki na simulação (ウイルス生命体)",
        "Repositório de Programas Virais": "Câmara-cofre de vírus da Facção Mir (ウイルスプログラムストレージ)",
        "Facção Mir": "ミュール団 (organização da simulação liderada por Claire)",
        "Mandamentos dos Teru": "掟 (preceitos dogmáticos da Tribo Teru definidos por Flute como 必要悪 / mal necessário)",
        "Harmonica": "Nome de batismo ancestral de Jack Hamilton entre os Teru (アルモニカ)",
        "Loja de Descontos": "雑貨屋・爆安一番 (padronizado com ID 30213 do mapa urbano)",
        "Pousada da Torre": "宿屋・塔の下亭 (padronizado com ID 29180/30212 do mapa urbano)"
    },
    "alertas_para_proximo_bloco": "A narrativa avança para o desdobramento da audiência solene na Igreja de Elemia em Platina e o avanço da jornada de redenção em direção à Fase 3, mantendo a vigilância sobre a vulnerabilidade de Aurica, a cumplicidade de Misha na Cosmosfera e os laços reconciliados de Harmonica com Em Pheyna."
}

highlights = [
    {
        "id": 12248,
        "scene": "Confronto com a Tenba em Karulu",
        "original_jp": "エル・エレミア教会総司、CRラードルフだ。",
        "original_en": "I am Cardinal Radolf of the Elemia Church.",
        "curated_ptbr": "Sou Radolf, Comandante-Geral da Igreja de Elemia.",
        "rationale": "Correção de alta fidelidade: Radolf é o Comandante-Geral militar dos Cavaleiros (総司 / Soushi), restaurando sua dignidade marcial frente à NISA que o chamou incorretamente de 'padre' e 'cardeal'."
    },
    {
        "id": 12265,
        "scene": "Promessa solene de Radolf a Aurica",
        "original_jp": "だが教会にいれば大丈夫だ。少なくとも、俺の目がCR黒いうちはな。",
        "original_en": "But, as long as I’m in charge of the Church, you won’t have to worry about a thing.",
        "curated_ptbr": "Mas, aqui na Igreja, você estará segura. Ao menos enquanto eu estiver vivo para impedir.",
        "rationale": "Restauração magistral da expressão idiomática '俺の目が黒いうちはな' ('enquanto eu viver / respirar'), deturpada pela NISA como se Radolf fosse o líder da Igreja (cargo que pertence ao Bispo Falss)."
    },
    {
        "id": 12322,
        "scene": "Ameaça hilária de Krusche a Jack",
        "original_jp": "それじゃその腕、いますぐCRメンテ前の状態に戻してCRあげようか?",
        "original_en": "Do you want me to fix your arm so it’s just like it was before I fixed it?",
        "curated_ptbr": "Ah, é? Então que tal eu reverter esse seu braço pro estado que tava antes da manutenção agora mesmo?!",
        "rationale": "Polimento cômico com ritmo impecável e mordacidade típica da jovem mecânica, preservando o timing de chantagem cômica."
    },
    {
        "id": 12347,
        "scene": "A Revelação de Misha sobre Shurelia",
        "original_jp": "塔ヶ崎澪羅は...ウイルス生命体よ。",
        "original_en": "Leila Togasaki is a virus.",
        "curated_ptbr": "Leila Togasaki é... uma forma de vida viral.",
        "rationale": "Precisão de ficção científica e lore: Shurelia/Leila é uma 'forma de vida viral' (ウイルス生命体), e não um mero software infeccioso ordinário."
    },
    {
        "id": 12436,
        "scene": "A Filosofia dos Teru por Lorde Flute",
        "original_jp": "私とて掟が好きというわけではない。掟は必要悪である。",
        "original_en": "I never said that I liked them...just that they’re necessary.",
        "curated_ptbr": "Nem eu tenho apreço por mandamentos. Eles são um mal necessário.",
        "rationale": "Resgate crucial da tese ética dos Teru omitida pela NISA: os mandamentos ancestrais são um 'mal necessário' (必要悪 / hitsuyou-aku)."
    },
    {
        "id": 12445,
        "scene": "Reconciliação no Portão Pheyna",
        "original_jp": "やはり...CRお前にいてもらわないと困る、アルモニカ。",
        "original_en": "I realize that we need you....Harmonica.",
        "curated_ptbr": "No fim das contas... nós ainda precisamos muito de você ao nosso lado, Harmonica.",
        "rationale": "Carga dramática profunda e reconexão filial/fraterna entre o Ancião Teru e o mercenário renegado, honrando seu nome sagrado de batismo."
    }
]

output_data = {
    "block_id": "BLK_EVD_052",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(dialogues_out),
    "id_range": [12232, 12457],
    "dialogues": dialogues_out,
    "curated_lines": curated_lines_out,
    "new_terms": new_terms,
    "glossary_updates": glossary_updates,
    "scene_handoff_final": scene_handoff_final,
    "highlights": highlights
}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"[SUCESSO] Bloco BLK_EVD_052 gerado com {len(dialogues_out)} falas em {OUTPUT_PATH}")

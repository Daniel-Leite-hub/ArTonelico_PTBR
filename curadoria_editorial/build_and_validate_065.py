# -*- coding: utf-8 -*-
"""
build_and_validate_065.py - Constrói e valida rigorosamente o catálogo do BLK_EVD_065
"""
import sys
import json
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

curated_dict = {
    14914: {
        "pt": "BANPRESTO & GUST APRESENTAM",
        "rationale": "Abertura cinematográfica oficial das desenvolvedoras Banpresto e Gust."
    },
    14915: {
        "pt": "A TORRE DE AR TONELICO",
        "rationale": "Cartão de título de abertura apresentando a Primeira Torre de Sol Ciel."
    },
    14916: {
        "pt": "Num passado remoto. Uma era tão distante que até as engrenagens do tempo esqueceram as marcas que talharam—",
        "rationale": "Restauração da prosa poética japonesa original sobre as engrenagens do tempo e suas marcas esquecidas, achatada pela NISA."
    },
    14917: {
        "pt": "Este mundo pereceu por duas vezes.",
        "rationale": "Registro narrativo solene e épico da cosmologia de Sol Ciel."
    },
    14918: {
        "pt": "A primeira, pelas mãos da humanidade...",
        "rationale": "Primeira Grande Catástrofe (Grathnode Infernal) provocada pela ambição humana."
    },
    14919: {
        "pt": "A segunda, pelas mãos de seres criados pelo homem...",
        "rationale": "Segunda Grande Catástrofe causada pela revolta das Reyvateils e Mir."
    },
    14920: {
        "pt": "E essa segunda grande catástrofe deixou sequelas profundas no destino do mundo.",
        "rationale": "Consequências cósmicas e estruturais da Guerra das Reyvateils na Torre."
    },
    14921: {
        "pt": 'Pois ela deu origem a uma nova e intrusa existência: uma "vida indesejada".',
        "rationale": "Gênese das entidades biovirais na rede da Torre."
    },
    14922: {
        "pt": "As formas de vida virais.",
        "rationale": "Termo técnico canônico da cosmologia (ウイルス生命体 - Virus Lifeform)."
    },
    14923: {
        "pt": 'Programadas pela própria Torre, essas "vidas" permaneciam ocultas em seu interior como pacotes de dados—',
        "rationale": "Mecânica computacional e energética dos vírus na arquitetura de Ar tonelico."
    },
    14924: {
        "pt": "E então se materializavam no mundo físico para atacar a humanidade repetidas vezes.",
        "rationale": "Processo de materialização física a partir de dados digitais."
    },
    14925: {
        "pt": "Eram dias de constante pavor, sob o temor perpétuo dos ataques virais.",
        "rationale": "Retrato dramático da vida cotidiana sob a ameaça dos vírus."
    },
    14926: {
        "pt": "Porém, em meio a essa escuridão, um raio de luz desceu sobre a humanidade.",
        "rationale": "Virada de esperança épica no prólogo."
    },
    14927: {
        "pt": 'O surgimento das "Reyvateils", as Donzelas do Canto, e dos lendários orbes sagrados: os [Cristais Hymmnos].',
        "rationale": "Fixação dos termos canônicos Reyvateil (Donzelas do Canto) e Cristal Hymmnos (ヒュムネクリスタル)."
    },
    14928: {
        "pt": "Canalizando o poder dos cristais, as santas donzelas enfraqueceram a força dos vírus.",
        "rationale": "Ação mística e técnica do uso dos cristais no combate viral."
    },
    14929: {
        "pt": 'Até que, por fim, conseguiram selar com êxito a temível entidade conhecida como "Vírus-Mãe".',
        "rationale": "Conclusão da lendária batalha contra o Vírus-Mãe (Mir)."
    },
    14930: {
        "pt": "Após o triunfo, o mundo recuperou uma paz fugaz.",
        "rationale": "Elegância literária para o intervalo de aparente tranquilidade."
    },
    14931: {
        "pt": "A santa donzela que selou o vírus e seus fiéis companheiros permaneceram na Torre para impedir o retorno da praga.",
        "rationale": "Missão de Shurelia e dos cavaleiros em vigília eterna."
    },
    14932: {
        "pt": 'Eles passaram a ser chamados de "Apóstolos de Elemia", venerados com fervor por todos os povos.',
        "rationale": "Título sagrado dos Apóstolos de Elemia."
    },
    14933: {
        "pt": "E aquela cidadela de vigília, com o tempo, floresceu e se transformou numa cidade...",
        "rationale": "Origem da fundação de Platina."
    },
    14934: {
        "pt": "A Cidade Celestial de Platina—",
        "rationale": "Epíteto solene de Platina no topo da Torre (天空都市プラティナ)."
    },
    14935: {
        "pt": "Protegido por Platina e pelos Apóstolos de Elemia, este mundo pôde respirar e pulsar com vida outra vez.",
        "rationale": "Restauração da biosfera e civilização sob os cuidados dos Apóstolos."
    },
    14936: {
        "pt": "Contudo, neste exato instante, uma terceira grande catástrofe está prestes a assolar o mundo—",
        "rationale": "Gancho dramático para o início da campanha do jogo."
    },
    14937: {
        "pt": "Ano 3770 d.C. — [Altar dos Apóstolos]",
        "rationale": "Restauração do nome completo do santuário ([Altar dos Apóstolos]) truncado no texto anterior."
    },
    14938: {
        "pt": "...Mas o que significa isso...?! O que está acontecendo?!",
        "rationale": "Autoridade e apreensão de Leard ao sentir o tremor e o alarme militar."
    },
    14939: {
        "pt": "Trago o relatório, senhor!\nVírus estão se proliferando no [Altar dos Apóstolos]!",
        "rationale": "Comunicação militar em pânico do soldado subordinado a Leard."
    },
    14940: {
        "pt": "Espécie desconhecida, classe desconhecida!\nTodos os dados são uma incógnita, senhor!",
        "rationale": "Alarme operacional diante de uma cepa viral sem precedentes."
    },
    14941: {
        "pt": "...Uma nova cepa de vírus...?! Seja como for, esses tremores não são normais!",
        "rationale": "Leard percebe que o abalo estrutural transcende um ataque viral comum."
    },
    14942: {
        "pt": "Pai!!",
        "rationale": "Entrada impulsiva e informal de Lyner no quartel-general."
    },
    14943: {
        "pt": "Pai!\nÉ verdade que apareceu uma nova espécie de vírus?!",
        "rationale": "Ansiedade juvenil de Lyner querendo detalhes do combate."
    },
    14944: {
        "pt": "Idiota!\nEm público, dirija-se a mim como Comandante!",
        "rationale": "Rigor militar de Leard repreendendo a falta de postura do filho."
    },
    14945: {
        "pt": "A gente não tem tempo para ficar discutindo formalidades!\nE aí, que tipo de monstro apareceu?!",
        "rationale": "Insolência e impaciência características de Lyner no início da jornada."
    },
    14946: {
        "pt": "Sem espécie, sem classe... Não temos dado algum.\nÉ um vírus completamente desconhecido.",
        "rationale": "Gravidade solene na voz do comandante."
    },
    14947: {
        "pt": "...Entendi. Quanto mais difícil for,\nmaior vai ser o gosto de derrubar!",
        "rationale": "Bravata juvenil de Lyner buscando autoafirmação marcial."
    },
    14948: {
        "pt": "Muito bem!\nHora de fazer um estrago com esses desgraçados!",
        "rationale": "Entusiasmo de combate desinibido."
    },
    14949: {
        "pt": "Espere, Lyner!",
        "rationale": "Interrupção ríspida de Leard contendo o filho."
    },
    14950: {
        "pt": "Quem lhe deu permissão?",
        "rationale": "Tom gélido e disciplinar da cadeia de comando."
    },
    14951: {
        "pt": "...Hã?",
        "rationale": "Surpresa desconcertada de Lyner."
    },
    14952: {
        "pt": "Quem foi que ordenou que você fosse combatê-los?!\nNão tome atitudes por conta própria!",
        "rationale": "Bronca veemente contra a insubordinação."
    },
    14953: {
        "pt": "Se a gente ficar parado esperando ordens,\na cidade de Platina vai ser engolida pelos vírus!",
        "rationale": "Justificativa rebelde e pragmática de Lyner."
    },
    14954: {
        "pt": "A quem você deve lealdade como cavaleiro?!\nResponda, Lyner!",
        "rationale": "Leard cobra o juramento de lealdade sagrado à Deusa/Administradora."
    },
    14955: {
        "pt": "...À Senhora Shurelia.",
        "rationale": "Lyner baixa a bola e pronuncia o nome sagrado de Shurelia com respeito."
    },
    14956: {
        "pt": "Sendo assim, receber as instruções da Senhora Shurelia\ne cumpri-las é a sua única missão.",
        "rationale": "Lição de dever militar de Leard."
    },
    14957: {
        "pt": "Ou acaso esqueceu a razão de ser um Cavaleiro de Elemia?!",
        "rationale": "Orgulho e peso da ordem sagrada dos Cavaleiros de Elemia."
    },
    14958: {
        "pt": "...",
        "rationale": "Silêncio contrariado de Lyner."
    },
    14959: {
        "pt": "Leard.\nQual é a situação no [Altar dos Apóstolos]?",
        "rationale": "Entrada serena e majestosa de Shurelia no posto de comando."
    },
    14960: {
        "pt": "Senhora Shurelia!",
        "rationale": "Saudação reverente de Lyner à sua protetora divina."
    },
    14961: {
        "pt": "O [Altar dos Apóstolos] encontra-se, neste momento,\ntotalmente ocupado pelas forças virais.",
        "rationale": "Relatório militar formal de Leard à deusa."
    },
    14962: {
        "pt": "Espécie, capacidade de combate...\nNão dispomos de nenhuma informação confirmada.",
        "rationale": "Conclusão técnica do relatório de Leard."
    },
    14963: {
        "pt": "Compreendo. Partirei pessoalmente para averiguar.\nLyner, acompanhe-me, por favor.",
        "rationale": "Shurelia assume a liderança e convoca Lyner como sua escolta."
    },
    14964: {
        "pt": "Sim! Com certeza!",
        "rationale": "Prontidão vibrante de Lyner ao ser escolhido."
    },
    14965: {
        "pt": "Viu só, pai?!\nA Senhora Shurelia confia no meu taco!\nEngole essa!",
        "rationale": "Provocação infantil típica de Lyner contra Leard."
    },
    14966: {
        "pt": "...",
        "rationale": "Desdém e paciência esgotada de Leard."
    },
    14967: {
        "pt": "Sendo assim, nós partiremos agora.\nLeard, confio a você a proteção da cidade.",
        "rationale": "Shurelia delega o governo e a defesa civil de Platina a Leard."
    },
    14968: {
        "pt": "Sim! Deixe sob meus cuidados.\nSenhora Shurelia, queira tomar extremo cuidado.",
        "rationale": "Lealdade incondicional e prece devota de Leard."
    },
    14969: {
        "pt": "Lyner...",
        "rationale": "Advertência paterna final antes da partida."
    },
    14970: {
        "pt": "Não espero que você vá ser de grande ajuda lá fora...\nmas trate de não virar um fardo para ela.",
        "rationale": "Dureza paterna ocultando apreensão pela vida do filho."
    },
    14971: {
        "pt": "...É óbvio que não vou!\nEu mesmo vou varrer esses vírus do mapa, vai ver só!",
        "rationale": "Promessa impetuosa de Lyner."
    },
    14972: {
        "pt": "Hmph... Até quando você pretende brandir a espada\ncom essa ilusão de moleque, Lyner...?",
        "rationale": "Desabafo solitário de Leard sobre a imaturidade do filho."
    },
    14973: {
        "pt": "M-mas o que diabos são essas coisas?!",
        "rationale": "Espanto no primeiro contato visual com as anomalias virais no Altar."
    },
    14974: {
        "pt": "...De fato. Nunca vi vírus com uma natureza dessas.",
        "rationale": "Análise perspicaz de Ayatane."
    },
    14975: {
        "pt": "...Estão brotando sem parar do [Altar dos Apóstolos]!\nMas o que este lugar significa, afinal?!",
        "rationale": "Estranhamento de Lyner com a fonte de emanação viral."
    },
    14976: {
        "pt": "Chega de conversa!\nTodos em prontidão de combate!",
        "rationale": "Comando tático austero de Shurelia."
    },
    14977: {
        "pt": "Beleza!\nVamos liquidar logo com a raça deles!",
        "rationale": "Ardor agressivo de combate."
    },
    14978: {
        "pt": "Espere, Lyner!\nPrimeiro farei a análise dos dados.",
        "rationale": "Shurelia intervém com cautela científica e administrativa."
    },
    14979: {
        "pt": "#0Was I ga enter px058-359-6002 flip mea.",
        "rationale": "Linha de execução de comando Hymmnos preservada estritamente com integridade intacta."
    },
    14980: {
        "pt": "...Confirmado.\nNenhum dos registros bate com amostras catalogadas anteriormente.",
        "rationale": "Diagnóstico do escaneamento de Shurelia."
    },
    14981: {
        "pt": "Padrões de conduta, propriedades elementares... Tudo é uma incógnita.\nNão temos como prever o desfecho deste confronto.",
        "rationale": "Alerta solene sobre a imprevisibilidade do perigo."
    },
    14982: {
        "pt": "Não importa o que sejam, continuam sendo vírus, né?!\nQuem ataca primeiro leva a melhor!",
        "rationale": "Convicção obstinada e inconsequente de Lyner."
    },
    14983: {
        "pt": "Lyner! Não avance sozinho!\nObedeça às instruções da Senhora Shurelia.",
        "rationale": "Moderação leal de Ayatane contendo o amigo."
    },
    14984: {
        "pt": "Senhora Shurelia!",
        "rationale": "Apelo ansioso de Lyner para receber a ordem de ataque."
    },
    14985: {
        "pt": "...Embora seja um risco imenso,\nnão podemos simplesmente ficar de braços cruzados.",
        "rationale": "Decisão ponderada de engajamento da deusa."
    },
    14986: {
        "pt": "Como de costume, vou tecer a Canção enquanto avalio a reação deles.\nVocês dois, deem-me cobertura!",
        "rationale": "Uso do verbo canônico 'tecer a Canção' (詩で戦う) e coordenação de combate."
    },
    14987: {
        "pt": "Mas o que é isso...?! Estão ficando transparentes?!\nO que está acontecendo...?",
        "rationale": "Espanto com o fenômeno de desmaterialização dos vírus."
    },
    14988: {
        "pt": "Não dou a mínima para o que sejam!\nToma essa!!",
        "rationale": "Ataque impetuoso desferido por Lyner."
    },
    14989: {
        "pt": "A espada atravessou o corpo deles?!\nOs meus golpes não surtem efeito nenhum!",
        "rationale": "Choque ao constatar que a lâmina atravessa energia pura."
    },
    14990: {
        "pt": "Essa técnica... Não me diga que...!!",
        "rationale": "Shurelia reconhece o método de transfiguração energética característico de Mir."
    },
    14991: {
        "pt": "Gwaaagh!!",
        "rationale": "Grito de dor ao receber contra-ataque maciço."
    },
    14992: {
        "pt": "Kgh...",
        "rationale": "Gemido contido ao ser atingida pelo impacto."
    },
    14993: {
        "pt": "Desse jeito, nós só vamos servir de alvo indefeso!",
        "rationale": "Ayatane constata a assimetria letal do confronto."
    },
    14994: {
        "pt": "...Lyner, Ayatane!\nVamos recuar temporariamente!",
        "rationale": "Ordem de retirada tática antes do aniquilamento."
    },
    14995: {
        "pt": "Como é que é?!",
        "rationale": "Indignação instintiva de Lyner perante a fuga."
    },
    14996: {
        "pt": "Creio ser a decisão mais sensata.\nVamos nos retirar.",
        "rationale": "Concordância madura e disciplinada de Ayatane."
    },
    14997: {
        "pt": "Espera aí!\nNós somos Cavaleiros de Elemia, não somos?!\nNosso dever é erradicar os vírus!",
        "rationale": "Senso de honra ferido de Lyner apelando para o voto dos cavaleiros."
    },
    14998: {
        "pt": "E mesmo assim a senhora quer que a gente fuja\ne abandone tudo numa situação crítica dessas?!",
        "rationale": "Revolta de Lyner contra a retirada."
    },
    14999: {
        "pt": "Lyner! Como tem coragem de falar nesse tom com a Senhora Shurelia?!",
        "rationale": "Repreensão austera de Ayatane contra o desrespeito de Lyner."
    },
    15000: {
        "pt": "Não tem importância.\nMais importante do que isso, Lyner...",
        "rationale": "Generosidade divina de Shurelia relevando a audácia do rapaz."
    },
    15001: {
        "pt": "Se todos nós tombarmos aqui...\nquem protegerá este solo sagrado?",
        "rationale": "Consciência do peso da responsabilidade cósmica de Shurelia."
    },
    15002: {
        "pt": "Mas...!!",
        "rationale": "Hesitação angustiada de Lyner."
    },
    15003: {
        "pt": "Eu compreendo perfeitamente o seu ardor.\nPorém, saber avaliar a situação com frieza\ntambém é um dever vital para um cavaleiro.",
        "rationale": "Conselho magistral de Shurelia moldando o jovem guerreiro."
    },
    15004: {
        "pt": "Vamos bater em retirada imediatamente.\nIsto é uma ordem!",
        "rationale": "Imposição firme da autoridade de líder suprema."
    },
    15005: {
        "pt": "Entendido...",
        "rationale": "Submissão resignada de Lyner."
    },
    15006: {
        "pt": "Uoooh!!",
        "rationale": "Grito de desequilíbrio perante o terremoto violento."
    },
    15007: {
        "pt": "Ugh...!!",
        "rationale": "Reação de impacto físico do abalo."
    },
    15008: {
        "pt": "Kyaaah!!",
        "rationale": "Emissão vocal feminina genuína do impacto."
    },
    15009: {
        "pt": "O céu...",
        "rationale": "Flash-cut para o Mundo Inferior onde Aurica pressente a anomalia celestial."
    },
    15010: {
        "pt": "Está rugindo...",
        "rationale": "Misha percebe as reverberações sonoras e fônicas da catástrofe na Torre."
    },
    15011: {
        "pt": "Senhora Shurelia! O que é isso?!",
        "rationale": "Pânico de Lyner diante da destruição em massa."
    },
    15012: {
        "pt": "Parece que as linhas de condução de doryoku de toda esta área foram severamente danificadas.",
        "rationale": "Diagnóstico técnico da ruptura do fluxo condutor de doryoku na Torre."
    },
    15013: {
        "pt": "As funções vitais de Platina devem estar completamente paralisadas...\nSerá impossível conter o avanço dos vírus nestas condições.",
        "rationale": "Constatação desesperadora da queda das defesas da capital."
    },
    15014: {
        "pt": "Não pode ser!\nIsso nunca tinha acontecido antes em toda a história...!!",
        "rationale": "Quebra da ilusão de invulnerabilidade de Platina na mente de Lyner."
    },
    15015: {
        "pt": "Esta tragédia... só encontra paralelo\nnas Duas Grandes Catástrofes dos tempos remotos...",
        "rationale": "Shurelia reconhece a escala apocalíptica da crise."
    },
    15016: {
        "pt": "Devemos regressar a Platina com urgência máxima\ne convocar um conselho extraordinário de crise.",
        "rationale": "Ação emergencial de comando de Shurelia."
    },
    15017: {
        "pt": "Eles nos alcançaram...",
        "rationale": "Ayatane nota a aproximação veloz da vanguarda viral."
    },
    15018: {
        "pt": "Droga!!",
        "rationale": "Sobressalto ao ver a emboscada."
    },
    15019: {
        "pt": "Ayatane!!",
        "rationale": "Lyner grita ao ver o amigo avançar para a frente."
    },
    15020: {
        "pt": "Essa passou raspando!\nVamos, depressa! Aproveitem enquanto é tempo!",
        "rationale": "Ayatane bloqueia a investida letal e abre a brecha de fuga."
    },
    15021: {
        "pt": "Mas e você, Ayatane...?!",
        "rationale": "Desespero de Lyner ao ver o companheiro para trás."
    },
    15022: {
        "pt": "Eu vou ficar aqui mais um pouco para conter o avanço deles.",
        "rationale": "Heroísmo sereno e sacrifício premeditado de Ayatane."
    },
    15023: {
        "pt": "Mas... se fizer isso, você...!",
        "rationale": "Shurelia teme pela vida de Ayatane perante a horda viral."
    },
    15024: {
        "pt": "Não há tempo a perder!",
        "rationale": "Urgência absoluta cortando as objeções."
    },
    15025: {
        "pt": "Senhora Shurelia, Lyner...\nMe perdoem!",
        "rationale": "Pedido comovente de desculpas antes de selar o próprio destino."
    },
    15026: {
        "pt": "Ayatane!!",
        "rationale": "Clamor angustiado de Lyner."
    },
    15027: {
        "pt": "AYATANEEEE!!!",
        "rationale": "Grito dilacerante ao ver o amigo ser cercado."
    },
    15028: {
        "pt": "...Lyner.\nEsta área cairá a qualquer segundo.\nPrecisamos nos apressar até Platina...",
        "rationale": "Shurelia engole as lágrimas para salvar a vida de Lyner."
    },
    15029: {
        "pt": "A senhora está me mandando abandonar o Ayatane para trás?!\nNão pode ser...",
        "rationale": "Inconformismo moral de Lyner em abandonar um irmão de armas."
    },
    15030: {
        "pt": "Eu sei perfeitamente o quanto dói seguir em frente\ne deixar o Ayatane para trás...",
        "rationale": "Empatia e sofrimento compartilhado por Shurelia."
    },
    15031: {
        "pt": "Porém, ficarmos paralisados aqui\nnão trará salvação a ninguém.",
        "rationale": "Firmeza trágica da deusa perante o sacrifício inevitável."
    },
    15032: {
        "pt": "Retornar a Platina e encontrar uma resposta contra os vírus\né a única alternativa que, no fim, nos permitirá salvar o Ayatane.",
        "rationale": "Argumento decisivo para dar a Lyner um propósito de esperança."
    },
    15033: {
        "pt": "...",
        "rationale": "Conflito interno de Lyner aceitando a dura realidade."
    },
    15034: {
        "pt": "Lyner...",
        "rationale": "Chamado suave para recolocá-lo em movimento."
    },
    15035: {
        "pt": "Ayatane...\nAguenta firme, eu vou voltar por você!",
        "rationale": "Promessa jurada no coração ao partir."
    },
    15036: {
        "pt": "!!",
        "rationale": "Alerta repentino diante de nova ameaça."
    },
    15037: {
        "pt": "O-o quê?!",
        "rationale": "Pega de surpresa no corredor."
    },
    15038: {
        "pt": "Droga! De novo não!",
        "rationale": "Frustração ao ser encurralado outra vez."
    },
    15039: {
        "pt": "Seus desgraçados!!",
        "rationale": "Ódio contra as aberrações virais."
    },
    15040: {
        "pt": "Lyner, seus golpes físicos não surtirão efeito contra esse vírus!",
        "rationale": "Advertência desesperada para evitar gasto inútil de energia."
    },
    15041: {
        "pt": "Lyner!\nRecue agora mesmo!!",
        "rationale": "Grito enfático ordenando a fuga imediata."
    },
    15042: {
        "pt": "Malditos...\nE o Ayatane...",
        "rationale": "Remorso lancinante de Lyner enquanto corre."
    },
    15043: {
        "pt": "Nós também estamos correndo sério risco...\nSe bloquearem aquela passagem,\nnão conseguiremos regressar a Platina...",
        "rationale": "Perigo iminente de isolamento no anel externo da Torre."
    },
    15044: {
        "pt": "A Senhora Shurelia não sente nada pelo Ayatane?!\nComo a senhora consegue manter essa frieza toda?!",
        "rationale": "Explosão emocional desmedida de Lyner contra a aparente compostura de Shurelia."
    },
    15045: {
        "pt": "Eu sou a Administradora da Torre...\nNão me é permitido agir movida por emoções pessoais.",
        "rationale": "Restauração canônica do título Administradora da Torre (管理者) e da dor do autodomínio divino."
    },
    15046: {
        "pt": "...",
        "rationale": "Lyner se cala ao perceber o fardo esmagador que Shurelia carrega."
    },
    15047: {
        "pt": "Lyner...\nAcalme-se e escute com atenção o que vou dizer.",
        "rationale": "Transição de Shurelia para o tom confidencial e instrutivo."
    },
    15048: {
        "pt": "Aquele vírus não pode ser erradicado por meios convencionais.",
        "rationale": "Revelação da barreira técnica instransponível."
    },
    15049: {
        "pt": "Por serem capazes de se converter em pura energia e viajar instantaneamente pela Torre, paredes e golpes físicos não têm efeito algum sobre eles.",
        "rationale": "Explicação da física e do estado energético dos vírus de Mir."
    },
    15050: {
        "pt": "...Quer dizer então que a gente é completamente indefeso contra eles...?",
        "rationale": "Desalento amargo diante da constatação de impotência física."
    },
    15051: {
        "pt": "...Resta apenas uma única esperança.",
        "rationale": "Shurelia introduz a solução sagrada da mitologia."
    },
    15052: {
        "pt": "O quê?!\nE que esperança seria essa...?!",
        "rationale": "Reacendimento súbito de esperança em Lyner."
    },
    15053: {
        "pt": "Devemos recorrer àquele cristal lendário...",
        "rationale": "Suspense místico e reverente."
    },
    15054: {
        "pt": "Precisamos usar o [Cristal Hymmnos].",
        "rationale": "Termo mestre [Cristal Hymmnos] devidamente padronizado com colchetes canônicos."
    },
    15055: {
        "pt": "O Cristal Hymmnos...!\nAquele que as lendárias donzelas usaram para salvar o mundo...",
        "rationale": "Reconhecimento do mito primordial por Lyner."
    },
    15056: {
        "pt": 'Sim. E, mais especificamente,\ndeve ser o cristal da linhagem sagrada "Purger".',
        "rationale": "Especificação do tipo de cristal purificador (Purger)."
    },
    15057: {
        "pt": "O Cristal Hymmnos Purger...",
        "rationale": "Lyner memoriza o nome do artefato supremo."
    },
    15058: {
        "pt": "No entanto, esse cristal não se encontra\nem lugar algum da cidade de Platina.",
        "rationale": "O obstáculo logístico que impulsiona a jornada ao Mundo Inferior."
    },
    15059: {
        "pt": "Dizem que ele repousa no continente flutuante [Asas de Hórus],\nlocalizado milhares de stons abaixo de nós.",
        "rationale": "Padronização canônica de [Asas de Hórus] e da unidade de distância [stons]."
    },
    15060: {
        "pt": "No Mundo Inferior...!\nMas... aquele não é o lugar proibido, onde ninguém jamais deve descer?!",
        "rationale": "Tabu cultural de Platina em relação ao Mundo Inferior (下の世界)."
    },
    15061: {
        "pt": "Lyner.\nSei perfeitamente que estou lhe pedindo o impossível,\nmas há algo que preciso lhe confiar.",
        "rationale": "Sinceridade e gravidade com que Shurelia faz o pedido a Lyner."
    },
    15062: {
        "pt": 'Desça até as [Asas de Hórus]\ne encontre o cristal "Purger"...',
        "rationale": "A missão fundamental do jogo outorgada a Lyner."
    },
    15063: {
        "pt": "Traspasse esta porta, embarque na aeronave selada\ne parta em direção às Asas de Hórus.",
        "rationale": "Revelação do veículo que cruzará a Blastline."
    },
    15064: {
        "pt": "O quê?!\nMas a aeronave é...",
        "rationale": "Lyner lembra do tabu milenar que proíbe o voo para o Mundo Inferior."
    },
    15065: {
        "pt": "Estamos sob estado de emergência absoluta...\nConcedo autorização para a decolagem como medida de exceção.",
        "rationale": "Prerrogativa executiva de Shurelia quebrando a lei da Torre."
    },
    15066: {
        "pt": "M-mas isso é uma loucura!\nA senhora não pode simplesmente me jogar isso de repente!",
        "rationale": "Aturdimento e vertigem de Lyner diante da súbita responsabilidade."
    },
    15067: {
        "pt": "O mundo inteiro está à beira do colapso!\nSe não agirmos agora, a catástrofe se repetirá pela terceira vez...!",
        "rationale": "Momento raro e arrebatador onde Shurelia perde a impassibilidade e grita em desespero."
    },
    15068: {
        "pt": "Senhora... Shurelia...",
        "rationale": "Lyner estremece ao presenciar a aflição e humanidade da deusa."
    },
    15069: {
        "pt": "...M-me perdoe.\nEu não deveria ter gritado com você desse jeito...",
        "rationale": "Shurelia envergonha-se da perda de compostura e pede desculpas com doçura tímida."
    },
    15070: {
        "pt": "É que... esta missão não é algo que qualquer pessoa seja capaz de suportar.",
        "rationale": "Confiança exclusiva depositada no coração puro e na bravura de Lyner."
    },
    15071: {
        "pt": "É exatamente por ser você, Lyner,\nque eu peço isso do fundo da minha alma...",
        "rationale": "Conexão íntima e transcendente entre Shurelia e Lyner."
    },
    15072: {
        "pt": "...Sim.\nEu compreendi.",
        "rationale": "Lyner amadurece instantaneamente e assume o destino do mundo nos ombros."
    },
    15073: {
        "pt": "Mas... e a Senhora Shurelia?",
        "rationale": "Preocupação genuína com a segurança de Shurelia na Torre infestada."
    },
    15074: {
        "pt": "Eu sou... a Administradora.",
        "rationale": "Afirmação categórica do dever sacrificial da Administradora da Torre."
    },
    15075: {
        "pt": "Enquanto esses vírus estiverem à solta pela Torre,\neu jamais poderei abandonar o meu posto.",
        "rationale": "Shurelia se coloca como o último escudo vivo de Platina."
    },
    15076: {
        "pt": "Não pode ser!\nEu não posso deixar a senhora aqui para trás!",
        "rationale": "Dor da separação imposta pelas circunstâncias."
    },
    15077: {
        "pt": "Eu ficarei... bem.",
        "rationale": "Sorriso corajoso e reconfortante para dar serenidade ao cavaleiro."
    },
    15078: {
        "pt": "Vamos, depressa!\nNão temos mais nem um segundo a perder!",
        "rationale": "Despedida urgente empurrando Lyner para o hangar."
    },
    15079: {
        "pt": "Esta é... a lendária aeronave selada...!",
        "rationale": "Deslumbramento diante da relíquia alada que descerá pelo abismo da Torre."
    },
    15080: {
        "pt": "Lyner...\nFique com isto...",
        "rationale": "Shurelia entrega o artefato chave."
    },
    15081: {
        "pt": "O que é isso...?",
        "rationale": "Curiosidade diante da joia misteriosa."
    },
    15082: {
        "pt": 'Nele estão registrados os diagramas holográficos tridimensionais do "Purger".',
        "rationale": "Revelação do conteúdo tecnológico do broche."
    },
    15083: {
        "pt": "Tenho certeza de que ele será de grande valia em sua jornada.",
        "rationale": "Bênção e votos de segurança de Shurelia."
    },
    15084: {
        "pt": "Você obteve o item [Broche Hymmnos]!",
        "rationale": "Mensagem de obtenção de item com o nome canônico do broche."
    },
    15085: {
        "pt": "...Lyner.",
        "rationale": "Pausa delicada antes da última prece."
    },
    15086: {
        "pt": "Sim...?",
        "rationale": "Lyner se vira na soleira da porta da aeronave."
    },
    15087: {
        "pt": "Por favor... traga o cristal...",
        "rationale": "Apelo emocionado com a respiração suspensa."
    },
    15088: {
        "pt": "Salve este mundo...",
        "rationale": "O destino de toda a vida dependendo dele."
    },
    15089: {
        "pt": "...Você é a minha única esperança!",
        "rationale": "Declaração despojada de títulos onde a deusa confessa sua vulnerabilidade e fé em Lyner."
    },
    15090: {
        "pt": "...",
        "rationale": "O peso sagrado das palavras ecoando na alma do herói."
    },
    15091: {
        "pt": 'Senhora Shurelia...\nEu juro que trarei o "Purger" de volta para cá!',
        "rationale": "Voto inquebrantável do cavaleiro à sua deusa."
    },
    15092: {
        "pt": "Até lá...\npor favor, aguente firme!",
        "rationale": "Prece filial de Lyner pela sobrevivência de Shurelia."
    },
    15093: {
        "pt": "...",
        "rationale": "Olhar eterno de despedida enquanto a nave decola e a porta se fecha."
    },
    15094: {
        "pt": "Primeiro, projetar o Campo de Ambiência sobre o alvo.",
        "rationale": "Instrução de combate e ativação do Campo de Ambiência (アンビエンスフィールド)."
    },
    15095: {
        "pt": "Assim que atingir o ponto crítico, desencadearei a Canção.\nMuito bem... posições de combate!",
        "rationale": "Conclusão do tutorial de canto e entrada em postura de batalha contra a horda viral."
    }
}

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_065_input.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

dialogues = input_data['dialogues']
assert len(dialogues) == 182, f"Expected 182 dialogues, got {len(dialogues)}"
assert len(curated_dict) == 182, f"Expected 182 curated lines, got {len(curated_dict)}"

hard_gate_errors = 0
lint_warnings = 0

for item in dialogues:
    item_id = item['id']
    orig_jp = item['original_jp']
    assert item_id in curated_dict, f"Missing ID {item_id} in curated_dict"
    trad = curated_dict[item_id]['pt']

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

    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    parts = trad.split("\n")
    for line_part in parts[1:]:
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1

    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

print(f"\nPre-validation Summary for BLK_EVD_065:")
print(f"Total lines evaluated: {len(dialogues)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("[SUCCESS] All 182 lines validated with ZERO errors and ZERO warnings!")
else:
    print("[ATTENTION] Some issues require fixing.")

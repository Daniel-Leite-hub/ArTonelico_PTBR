# -*- coding: utf-8 -*-
"""
generate_blk061.py - Curadoria Editorial Canônica e Validação Rigorosa de BLK_EVD_061
"""
import json
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Carrega input original
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_061_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Dicionário de traduções curadas e rationales por ID
curations = {
    # --- EVENT/657.EVD (IDs 14158 - 14216, 59 falas) ---
    14158: (
        "Misha... Onde você está...?",
        "Lyner chama por Misha em tom angustiado ao procurar por ela na Mansão da Lua."
    ),
    14159: (
        "Acalme-se, procuremos sem pressa.\nA propósito... conhece a origem do nome\n'Mansão da Lua'?",
        "Anjo Shura acolhe a aflição de Lyner com serenidade e indaga sobre a etimologia da Mansão da Lua."
    ),
    14160: (
        "Hã...? Não faço ideia...",
        "Lyner reage surpreso com a pergunta inesperada."
    ),
    14161: (
        "Pois bem, permita-me explicar.",
        "Shura se prontifica a revelar a natureza ontológica daquele local."
    ),
    14162: (
        "Quando a minha mestra, Misha, nasceu,\nesta mansão também veio ao mundo.\nE este lugar é a própria fonte de sua vida.",
        "Shura revela a gênese simultânea da mansão e de sua mestra Misha."
    ),
    14163: (
        "Inúmeras engrenagens, correntes e eixos\nprovêm a força motriz que a impulsiona\ne a mantém em funcionamento.",
        "Shura descreve a mecânica de engrenagens e eixos que pulsam como fonte motriz da mente de Misha."
    ),
    14164: (
        "Como assim...? Engrenagens e correntes...?\nA Misha não é nenhuma máquina...",
        "Lyner se recusa a aceitar que a amiga seja reduzida a um mecanismo."
    ),
    14165: (
        "Engana-se. Na raiz de sua existência,\nreside um programa que opera segundo processos fixos.\nEm suma: ela é praticamente uma máquina.",
        "Shura expõe a base programática e artificial da psicologia de uma Reyvateil Origin."
    ),
    14166: (
        "A camada mais profunda de sua psique\né este castelo que dita o compasso exato de sua vida...\na Mansão da Lua.",
        "Revelação de que a Mansão da Lua personifica o mecanismo central da psique profunda de Misha."
    ),
    14167: (
        "O que você está dizendo...?\nQuer dizer que todos os sentimentos e emoções\nda Misha são uma farsa?!",
        "Lyner expressa choque ante a possibilidade de os sentimentos de Misha serem artificiais."
    ),
    14168: (
        "Não, não se trata disso.\nOs sentimentos e as emoções de minha mestra\nsão inteiramente reais.",
        "Shura tranquiliza Lyner afirmando a legitimidade inequívoca dos sentimentos de Misha."
    ),
    14169: (
        "O que estou lhe explicando aqui é apenas\no que jaz no alicerce mais primitivo de sua mente.",
        "Distinção entre o alicerce mecânico basal e a consciência viva e senciente."
    ),
    14170: (
        "De qualquer forma, aceite esta verdade:\nminha mestra, Misha, é uma forma de vida criada.\nEla não é um ser humano de carne e osso.",
        "Declaração solene sobre a natureza artificial de Misha como Reyvateil Origin."
    ),
    14171: (
        "Contudo, os sentimentos e as emoções que ali brotam\nem nada diferem daqueles de um ser humano.",
        "Shura reafirma que a humanidade do afeto não depende da biologia."
    ),
    14172: (
        "E é exatamente isso o que engendra desfechos\ntão desastrosos como este de agora... não é?",
        "Anjo Rishi intervém das sombras apontando as consequências trágicas da emotividade."
    ),
    14173: (
        "...!?\nQuem é você?!",
        "Lyner reage à voz desconhecida em sobressalto."
    ),
    14174: (
        "Muito prazer. Eu sou o Anjo Rishi,\nregente da preservação e da razão.",
        "Apresentação formal de Anjo Rishi (利支天) estabelecendo sua esfera conceitual de preservação e racionalidade."
    ),
    14175: (
        "Jamais imaginei que você daria as caras por aqui.",
        "Shura expressa surpresa com a manifestação direta de sua contraparte racional."
    ),
    14176: (
        "Eu digo o mesmo. No entanto, lamento informar:\nsua mestra está prestes a ser apagada.",
        "Rishi decreta com frieza calculista a exclusão iminente de Shinobi Misha."
    ),
    14177: (
        "Afinal, a causa deste Grande Colapso decorre\ndo paradoxo gerado pelo descontrole emocional dela.",
        "Diagnóstico técnico do colapso psicológico gerado pelo conflito afetivo."
    ),
    14178: (
        "Em outras palavras: a psique fundamental de Misha\ndeliberou por expurgar tudo o que há de emotivo nela.",
        "Explicação da diretriz de autoexclusão emocional tomada pelo núcleo psíquico."
    ),
    14179: (
        "...Uma atitude e tanto, devo admitir.",
        "Ironia amarga de Shura diante da decisão drástica da psique lógica."
    ),
    14180: (
        "O-o que está acontecendo aqui?!\nO que vai ser da Misha?!",
        "Lyner em pânico ao perceber a ameaça existencial sobre Misha."
    ),
    14181: (
        "Trata-se da exclusão de minha mestra,\na Shinobi Misha, regente da inovação.\nCom isso, ela perderá quase todo vestígio de emoção.",
        "Shura explica o apagamento da persona afetiva Shinobi Misha."
    ),
    14182: (
        "Exato. Ela passará a operar com eficiência máxima,\ncapaz de tecer canções com precisão matemática\na qualquer momento.",
        "Visão pragmática de Rishi sobre transformar Misha em instrumento sem falhas."
    ),
    14183: (
        "Em contrapartida, toda a sua gama de sentimentos,\nseja alegria, raiva, tristeza ou prazer,\nserá extirpada para sempre.",
        "Shura enfatiza a perda trágica da alma e das emoções humanas de Misha."
    ),
    14184: (
        "Em conclusão: eu jamais consentirei\ncom semelhante deliberação.",
        "Shura firma sua lealdade inabalável a Shinobi Misha."
    ),
    14185: (
        "Eu também não vou permitir uma barbaridade dessas!\nA Misha é um ser vivo!",
        "Lyner se rebela contra o descarte da essência viva da amiga."
    ),
    14186: (
        "Sendo assim, estamos em oposição.",
        "Rishi constata a cisão ideológica entre conservação e emoção."
    ),
    14187: (
        "Não que isso seja alguma novidade.",
        "Shura retruca com elegância que a rivalidade de ambos é ancestral."
    ),
    14188: (
        "Vejo que estão todos reunidos...",
        "Entrada imponente e gélida da Misha da Disciplina e da Razão."
    ),
    14189: (
        "Seja bem-vinda, Mestra.",
        "Saudação reverente de Rishi à sua soberana lógica."
    ),
    14190: (
        "Você é... aquela da outra vez?!",
        "Lyner reconhece a persona austera encontrada anteriormente na Cosmosfera."
    ),
    14191: (
        "Sim. Sou a Misha regente da disciplina e da razão.\nAquela destinada a salvar este mundo.",
        "Apresentação dogmática da persona austera de Misha."
    ),
    14192: (
        "A Shinobi Misha está aqui?!\nO que você fez com ela?!",
        "Lyner exige saber o paradeiro de sua querida amiga de infância."
    ),
    14193: (
        "Ela está aprisionada nos aposentos do fundo.\nMas antes disso, tenho uma tarefa indispensável a cumprir.",
        "Misha da Razão desvia o foco para sua missão executiva."
    ),
    14194: (
        "Uma tarefa a cumprir...?",
        "Lyner indaga apreensivo sobre a intenção da persona."
    ),
    14195: (
        "Sim... A sua completa eliminação.",
        "Veredito fatal da persona lógica contra a existência de Lyner."
    ),
    14196: (
        "O-o quê?!",
        "Choque fulminante de Lyner."
    ),
    14197: (
        "Guh!!",
        "Gemido de dor física sob o ataque cinético de Misha."
    ),
    14198: (
        "Você acumulou erros demais.\nNa verdade, ter cruzado meu caminho foi o erro primordial.",
        "Condenação filosófica da relação entre os dois como fonte do desvio funcional."
    ),
    14199: (
        "Isso é um completo absurdo...!",
        "Lyner contesta a frieza insana da declaração."
    ),
    14200: (
        "Nosso propósito supremo é entoar a canção\ne selar os vírus que ameaçam este mundo.\nAté então, tudo transcorria em perfeita ordem.",
        "Evocação da missão cósmica da Star Singer contra os vírus."
    ),
    14201: (
        "Porém, bastou você reaparecer para tudo ruir!\nOs apegos mundanos em seu peito se avolumaram\ne ela passou a rejeitar a canção...!",
        "A paixão e o apego humano por Lyner desestabilizaram o dever sacrificial de Misha."
    ),
    14202: (
        "Ghaaaah!!",
        "Grito dilacerante de Lyner sob a tortura mágica."
    ),
    14203: (
        "Por sua culpa...\neste mundo corre o risco de sucumbir à ruína!",
        "Acusação de perigo cósmico iminente atribuído aos laços com Lyner."
    ),
    14204: (
        "Se ao menos você não existisse...\na Misha... eu...!!",
        "Conflito interior trágico que transparece na voz da persona disciplinada."
    ),
    14205: (
        "...P-pa... re...",
        "A voz sufocada de Shinobi Misha tentando conter a execução."
    ),
    14206: (
        "Ugh...",
        "Hesitação involuntária da Misha austera ao ser confrontada de dentro."
    ),
    14207: (
        "Não machuque... o Lyner...",
        "Clamor protetor e infantilmente terno de Shinobi Misha."
    ),
    14208: (
        "V-você... Como?!\nComo conseguiu escapar 'daquele quarto'?! Impossível!",
        "Desconcerto da persona disciplinada ante a quebra do confinamento psíquico."
    ),
    14209: (
        "Você nem percebeu, não é...?\nO ato que tentou cometer agora há pouco\ntambém gerou um novo paradoxo.",
        "Shinobi Misha revela o erro de cálculo inerente à tentativa de destruir o amor por Lyner."
    ),
    14210: (
        "...O quê?!",
        "Choque de autopercepção da Misha lógica."
    ),
    14211: (
        "Você tentou destruir um sentimento que repousa\ntão fundo quanto o 'propósito supremo' que você vigia...\nos sentimentos dedicados ao Lyner.",
        "Revelação canônica de que o amor por Lyner é tão fundacional na alma de Misha quanto sua diretriz original."
    ),
    14212: (
        "Venha, Lyner... vamos fugir...\nVenha comigo...",
        "Shinobi Misha resgata Lyner para tirá-lo do alcance da persona implacável."
    ),
    14213: (
        "Essa foi por muito pouco...",
        "Alívio pós-fuga em segurança."
    ),
    14214: (
        "Misha...!\nVocê está bem...?",
        "Preocupação genuína de Lyner com o estado frágil da amiga."
    ),
    14215: (
        "Estou bem...\nO importante agora é irmos ao 'Bosque do Sono'.\nHá uma fonte curativa por lá.",
        "Indicação do próximo destino na Cosmosfera para recuperar as forças."
    ),
    14216: (
        "Você teceu a Magia Azul [Anjo Rishi]!",
        "Síntese da Magia Azul correspondente à entidade de conservação."
    ),

    # --- EVENT/176.EVD (IDs 14217 - 14282, 66 falas) ---
    14217: (
        "Os vírus invadiram também\na rede sinfônica do Segundo Distrito!",
        "Alerta emergencial sobre o avanço viral na infraestrutura da cidade."
    ),
    14218: (
        "...Não há escolha!\nCortem imediatamente toda a energia sinfônica\ndo Segundo Distrito!",
        "Ordem austera e pragmática do governador Leard para conter a proliferação viral."
    ),
    14219: (
        "Sim, senhor!",
        "Pronta confirmação militar da ordem recebida."
    ),
    14220: (
        "Neste ritmo, Platina cairá...\nAinda não temos nenhuma notícia\nda Senhora Shurelia ou de Ayatane?!",
        "Angústia contida de Leard com o cerco e o silêncio da Deusa."
    ),
    14221: (
        "Ainda nenhuma novidade, senhor...\nJá se passaram dias desde que partiram\nrumo ao Altar dos Apóstolos...",
        "Confirmação do desaparecimento tático da comitiva no santuário sagrado."
    ),
    14222: (
        "Que situação lamentável...\nSenhora Shurelia... rogo para que esteja sã e salva.",
        "Devoção e temor patriarcal de Leard pelo bem-estar de Shurelia."
    ),
    14223: (
        "...Certamente ela está em segurança, senhor.\nAfinal, o Senhor Ayatane a está escoltando.",
        "Confiança devotada do oficialado na competência marcial de Ayatane."
    ),
    14224: (
        "E por qual razão a presença de Ayatane\nseria garantia de segurança...?",
        "Ceticismo analítico de Leard questionando certezas infundadas."
    ),
    14225: (
        "É que o Senhor Ayatane abriga um poder misterioso.",
        "Testemunho sobre as habilidades anômalas de Ayatane."
    ),
    14226: (
        "Mesmo quando os vírus surgiram pela primeira vez\nno Altar dos Apóstolos...",
        "Rememoração da primeira incursão perigosa."
    ),
    14227: (
        "Embora tenham sido encurralados lá dentro,\nele retornou sem um único arranhão, não se lembra?",
        "Argumento empírico sobre a sobrevivência sobrenatural de Ayatane."
    ),
    14228: (
        "Droga!!",
        "Grito urgente de Lyner no calor da emboscada no Altar dos Apóstolos."
    ),
    14229: (
        "Ayatane!!",
        "Lyner chama pelo amigo encurralado pelos vírus."
    ),
    14230: (
        "Essa foi por um triz.\nRápido, Lyner! Aproveite a brecha!",
        "Ayatane afasta Lyner e Shurelia mantendo a compostura cortês."
    ),
    14231: (
        "Senhora Shurelia, Lyner... perdoem-me!",
        "Falso pedido de desculpas encenado para os companheiros antes de revelar sua verdadeira face."
    ),
    14232: (
        "...",
        "Pausa dramática calculista na transição para sua persona viral secreta."
    ),
    14233: (
        "Meros vírus de assalto básico ousando\nlevantar as garras contra mim... Que atrevimento.",
        "Revelação sinistra e desdenhosa da superioridade de Ayatane perante os vírus da espécie dele."
    ),
    14234: (
        "Tratem de sossegar e ficar bem quietinhos por ora.",
        "Restauração da autoridade de Ayatane comandando os vírus subordinados, corrigindo a omissão crassa da NISA."
    ),
    14235: (
        "...Eu tenho os meus próprios métodos.",
        "Monólogo sombrio prenunciando a agenda oculta de Ayatane e Mir."
    ),
    14236: (
        "Por isso, tenho certeza de que, com o Senhor Ayatane\nao lado dela, nada de mal acontecerá.",
        "A ironia dramática do oficial ignorando o perigo que Ayatane representa."
    ),
    14237: (
        "Hum... Quem dera fosse assim tão simples.",
        "O pressentimento incômodo de Leard."
    ),
    14238: (
        "Relatório urgente!\nUm Guardião acabou de invadir o Segundo Distrito!",
        "Notificação da ruptura catastrófica da linha de defesa."
    ),
    14239: (
        "O quê...?! Será este o nosso fim...?",
        "Leard à beira do desespero perante a queda iminente de Platina."
    ),
    14240: (
        "...Lyner!\nÉ você mesmo?!",
        "Leard avista o filho que acaba de retornar da jornada no Mundo Inferior."
    ),
    14241: (
        "...Oi... pai.",
        "Saudação contida e tensa de Lyner perante a figura austera do pai."
    ),
    14242: (
        "Humpf. De que serve regressar a estas horas tardias,\nLyner?",
        "Rispidez cortante do patriarca reprovando a demora."
    ),
    14243: (
        "...C-como é que é?!",
        "Indignação imediata de Lyner."
    ),
    14244: (
        "Eu quase morri correndo de um lado para o outro\npara trazer o Cristal Hymmnos até aqui...",
        "Desabafo apaixonado sobre as provações e perigos que enfrentou."
    ),
    14245: (
        "E essa é a primeira coisa que você me diz?!\nNão tem uma mísera palavra de consideração?!",
        "Lyner cobra a empatia e o reconhecimento que o pai lhe nega sistematicamente."
    ),
    14246: (
        "...Diz que trouxe o Cristal Hymmnos?\nOra, isso não passa da sua mais estrita obrigação.",
        "Rigor implacável de Leard desdenhando a autoglorificação do filho."
    ),
    14247: (
        "O que se julga de fato é o tempo gasto na conclusão.\nE sob esse prisma, seu desempenho não merece elogio algum.",
        "Cobrança burocrática e militarista de eficiência operacional."
    ),
    14248: (
        "Jamais compreenderei por qual razão a Senhora Shurelia\nconfiou tamanha missão a alguém como você.",
        "Desdém patriarcal questionando a confiança da Deusa em Lyner."
    ),
    14249: (
        "Ghk... Seu velho imprestável!!",
        "Revolta filial explosiva de Lyner perante a humilhação."
    ),
    14250: (
        "Chega, Lyner! Não numa hora dessas!\nE o senhor também passou de todos os limites, Leard!!",
        "Misha intervém energicamente repreendendo tanto o amigo quanto o governador."
    ),
    14251: (
        "...Por acaso você seria... a Misha?!\nMas o que diabos aconteceu com o seu corpo...?",
        "Leard estupefato ao ver a amiga de infância de Lyner transformada no corpo adulto de Origin."
    ),
    14252: (
        "No meu estado atual,\nsou incapaz de entoar a Chronicle Key.",
        "Confissão direta sobre o impedimento de cantar o hino de selamento."
    ),
    14253: (
        "Mas explicarei isso com calma depois!\nAgora, nossa prioridade máxima é conter os vírus.",
        "Senso prático de urgência de Misha diante da catástrofe de Platina."
    ),
    14254: (
        "O Lyner encarou a morte de perto incontáveis vezes\npara conseguir recuperar este cristal!",
        "Misha defende o sacrifício de Lyner perante o pai insensível."
    ),
    14255: (
        "Foi uma jornada em que ele arriscou a própria vida!\nReconheça ao menos o valor desse feito!",
        "Clamor comovente por justiça e validação afetiva."
    ),
    14256: (
        "Misha... Quem não é capaz de cumprir uma missão\ncom desenvoltura simplesmente carece de competência.",
        "Filosofia implacável de Leard desqualificando o sofrimento como sintoma de fraqueza."
    ),
    14257: (
        "Pouco importa quantas vezes ele esteve à beira da morte;\nnada disso é digno de qualquer mérito.",
        "Negação absoluta de mérito ao esforço desprovido de perfeição."
    ),
    14258: (
        "Sei muito bem que sou um forasteiro,\nmas peço vênia para intervir, honrado pai de Sir Lyner!",
        "Intervenção solene, nobre e militar de Radolf em defesa do companheiro de armas."
    ),
    14259: (
        "Eu, Radolf, acompanhei Sir Lyner a cada passo,\ne seus feitos foram de uma bravura admirável!",
        "Testemunho cavalheiresco de honra e coragem presenciadas em batalha."
    ),
    14260: (
        "Jamais em minha vida vi alguém tão devotado\nao cumprimento do dever quanto ele!",
        "Elogio máximo de cavaleiro militar à determinação de Lyner."
    ),
    14261: (
        "Chama-se Radolf, se não me engano.\nNão queira nivelar os nossos padrões\naos daqueles que vivem lá embaixo.",
        "Arrogância elitista platinesa de Leard desqualificando o olhar dos habitantes de baixo."
    ),
    14262: (
        "Repito mais uma vez: ser fiel ao cumprimento da missão\né a premissa mais elementar da conduta.",
        "Reiteração dogmática do dever absoluto."
    ),
    14263: (
        "Não admito ser comparado àqueles que mal conseguem\nconcluir uma tarefa com a devida competência.",
        "Leard rejeita comparações com os povos da superfície inferior, corrigindo a inversão grosseira da NISA."
    ),
    14264: (
        "...Ghk.",
        "Frustração de Radolf ao engolir o orgulho ferido em prol da diplomacia."
    ),
    14265: (
        "Radolf. Não precisa mais... Obrigado.",
        "Gratidão fraterna de Lyner acolhendo o gesto honrado do amigo."
    ),
    14266: (
        "E então, pai!\nO que devemos fazer afinal com este cristal?",
        "Lyner retoma o pragmatismo da crise."
    ),
    14267: (
        "Esse cristal só manifesta o seu poder\nao se fundir e se integrar a uma Reyvateil.",
        "Explicação do processo de união simbiótica entre cristal e cantora."
    ),
    14268: (
        "Em circunstâncias normais, caberia à Senhora Shurelia\nintegrar-se a esse cristal, contudo...",
        "Menção ao plano mestre original interrompido pelo sumiço de Shurelia."
    ),
    14269: (
        "...",
        "Pausa sombria de Leard avaliando a perda de opções."
    ),
    14270: (
        "No momento, a Senhora Shurelia partiu\npara o Altar dos Apóstolos ao lado de Ayatane...",
        "Reiteração da localização do contingente desaparecido."
    ),
    14271: (
        "...e desde então não tivemos notícia alguma de ambos.",
        "Constatação do vácuo de liderança sagrada em Platina."
    ),
    14272: (
        "O quê?!",
        "Choque de Lyner ao saber do desaparecimento de Shurelia e Ayatane."
    ),
    14273: (
        "Chegados a este ponto extremo,\ntemos de agir considerando o pior cenário possível.",
        "Decisão de emergência governamental perante o colapso iminente."
    ),
    14274: (
        "Lyner. Confie o cristal à Reyvateil\nem quem você deposita sua maior confiança.",
        "Ordem crucial que delega a Lyner a escolha entre Aurica e Misha."
    ),
    14275: (
        "Faça com que ela e o cristal se integrem,\nliberando assim todo o seu poder.",
        "Instrução para a realização do rito de instalação/integração."
    ),
    14276: (
        "E como diabos se faz essa tal 'integração'...?",
        "Ignorância juvenil de Lyner sobre os procedimentos técnicos de instalação de cristais."
    ),
    14277: (
        "...Você não sabe?\nLogo agora, quando cada segundo é precioso...",
        "Impaciência de Leard com o desconhecimento técnico do filho."
    ),
    14278: (
        "Nesse caso, procure Horai,\no dono do Centro de Mergulho de Platina,\npara que ele realize o procedimento.",
        "Encaminhamento de Lyner ao especialista em Mergulho e integração de Platina."
    ),
    14279: (
        "No tocante a Reyvateils e cristais,\nele é um especialista consumado.",
        "Aval da autoridade de Horai no manuseio de dados psíquicos e cristais."
    ),
    14280: (
        "Tenho uma infinidade de providências a tomar.\nRetorne a este posto assim que concluir o rito de integração.",
        "Despedida funcional de Leard focando na defesa de Platina."
    ),
    14281: (
        "O acesso ao [Centro de Mergulho de Platina]\nfoi liberado!",
        "Notificação de desbloqueio de novo local no mapa."
    ),
    14282: (
        "Você pode se deslocar até o Centro de Mergulho\nselecionando-o no Mapa da Cidade.",
        "Instrução de navegação para a interface de mapa urbano."
    ),

    # --- EVENT/714.EVD (IDs 14283 - 14342, 60 falas) ---
    14283: (
        "...Este lugar tem toda a pinta\nde onde um dragão se esconderia.",
        "Avaliação de Lyner sobre a atmosfera sombria do covil onírico."
    ),
    14284: (
        "Pensou isso mesmo? Acertou em cheio!\nKukuku...",
        "Riso zombeteiro do dragão assumindo a malícia de Bourd."
    ),
    14285: (
        "Bourd... Não, o dragão?!\nEntão era aqui que você estava se escondendo?!",
        "Reconhecimento alarmado da forma antropomórfica do monstro."
    ),
    14286: (
        "Aurica! Use a Guarda do Vento!",
        "Comando tático de Lyner invocando a Magia Azul de suporte de Aurica."
    ),
    14287: (
        "...Entendido.\nLá vou eu...",
        "Aurica assentindo com nervosismo para invocar o feitiço."
    ),
    14288: (
        "Haa!!",
        "Vocalização de invocação mágica."
    ),
    14289: (
        "Por favor! Apareça!!",
        "Súplica angustiada para a materialização da magia protetora."
    ),
    14290: (
        "▼○$#!...&#@!",
        "Preservação estrita da sequência procedural de caracteres de distorção mágica."
    ),
    14291: (
        "...Tsc, de novo esse truque?\nOlha aqui, Aurica... Acha mesmo que a mesma tática\nvai funcionar duas vezes contra mim?",
        "Falss/Dragão desdenha da tentativa de defesa de Aurica."
    ),
    14292: (
        "!!\nM-mas...",
        "Aurica recua hesitante e abalada pela intimidação psicológica."
    ),
    14293: (
        "Aurica! Não caia nas provocações dele!\nVocê consegue, Aurica! Eu tenho certeza!!",
        "Lyner injeta ânimo e confiança na parceira hesitante."
    ),
    14294: (
        "Eu...",
        "Hesitação vulnerável de Aurica processando a fé de Lyner."
    ),
    14295: (
        "Eu jamais serei derrotado!!\nKukuku...",
        "Arrogância vilanesca do dragão traumatizante."
    ),
    14296: (
        "Acredite em mim!!",
        "Apelo heroico de Lyner para fortalecer a determinação de Aurica."
    ),
    14297: (
        "Eu vou te derrotar, custe o que custar!\nAfinal, sou a heroína que trará a paz a este mundo!",
        "Aurica assume o arquétipo da heroína de sua Cosmosfera para enfrentar o monstro."
    ),
    14298: (
        "Ghk!! Insolente...\nVou fazer você se arrepender amargamente dessas palavras!!",
        "Reação enraivecida do dragão à ousadia de Aurica."
    ),
    14299: (
        "Você também não passa de uma criatura\nde um truque só!",
        "Retruque afiado de Aurica desmascarando a limitação do adversário."
    ),
    14300: (
        "Como é que é...?!",
        "Espanto do monstro ao ser desafiado frontalmente."
    ),
    14301: (
        "Eu não tenho mais medo das suas rajadas de fogo!\nÉ verdade que naquela época não pude proteger minha família...\nmas agora sou capaz de proteger quem amo!",
        "Superação catártica do trauma do massacre familiar no Vilarejo Skuwat."
    ),
    14302: (
        "Maldita!!",
        "Ira impotente do dragão perante a coragem renovada da donzela."
    ),
    14303: (
        "Tome isto!!\nHaa!!",
        "Grito de ataque decisivo de Aurica desferindo a magia liberadora."
    ),
    14304: (
        "Ughwaaaah!!\nNão... Não pode ser...!!",
        "Rugido de aniquilação do dragão sendo esmagado pela magia."
    ),
    14305: (
        "Eu não vou deixar você fazer o que bem entender\ncom este mundo para sempre!",
        "Tomada de controle de Aurica sobre a própria mente onírica."
    ),
    14306: (
        "Gyaaaaaah...!!",
        "Último berro agonizante do monstro."
    ),
    14307: (
        "...Lyner, eu...",
        "Aurica estupefata e ainda sem fôlego após a façanha."
    ),
    14308: (
        "Não foi incrível?!\nAurica, você derrotou o dragão completamente sozinha!!",
        "Celebração eufórica de Lyner diante da vitória da parceira."
    ),
    14309: (
        "Eu... salvei este mundo...?\nQuase não consigo acreditar...",
        "Deslumbramento hesitante da jovem heroína perante o triunfo."
    ),
    14310: (
        "Lyner... obrigada.\nSinto... como se um peso enorme tivesse saído do meu peito...",
        "Expressão genuína de alívio e gratidão pelo amparo afetivo."
    ),
    14311: (
        "Você teceu a Magia Vermelha \"Dragonferno\"!",
        "Síntese da Magia Vermelha de dano gerada pela vitória sobre o dragão."
    ),
    14312: (
        "Aquilo é... a Mudança de Paradigma!!\nNão me digais... que ela superou o dragão?!",
        "Don Leon em assombro épico com a quebra do bloqueio psicológico de Aurica."
    ),
    14313: (
        "Pode apostar que sim!\nE o melhor: a Aurica derrotou o dragão por conta própria!",
        "Orgulho radiante de Lyner ao relatar a proeza."
    ),
    14314: (
        "...Que feito assombroso.\nAquele dragão medonho... Custa-me a crer...",
        "Donsuke emocionado com a façanha improvável de sua protegida."
    ),
    14315: (
        "Pensando bem... por qual razão\no dragão assumiu a aparência do Bourd?",
        "Lyner investiga a simbologia por trás da manifestação onírica."
    ),
    14316: (
        "Isso se deve ao fato... de que o vilarejo da Senhorita Aurica\nfoi devastado por culpa exclusiva de Bourd.",
        "Don Leon começa a desvendar a raiz do trauma existencial de Aurica."
    ),
    14317: (
        "Bourd roubou o 'Tesouro' da Tribo Teru e, na fuga,\npassou pelo Vilarejo Skuwat. Os Teru o perseguiram,\ne a aldeia inteira se converteu em campo de batalha.",
        "Reconstituição histórica do massacre de Skuwat desencadeado pela cobiça de Bourd."
    ),
    14318: (
        "Bourd usou os aldeões como escudo humano\ne fugiu sozinho, carregando o 'Tesouro'.",
        "A covardia atroz de Bourd sacrificando vidas civis."
    ),
    14319: (
        "...Não pode ser!!",
        "Repulsa e horror de Lyner diante da atrocidade."
    ),
    14320: (
        "Os pais da Senhorita Aurica foram coagidos pelas tropas\nda Tenba a lutar... e pereceram com a onda de choque\nda magia disparada pela Tribo Teru.",
        "Donsuke narra o destino fúnebre dos pais de Aurica como dano colateral da guerra."
    ),
    14321: (
        "...Então era essa a verdade.",
        "Lyner finalmente compreende a raiz da fobia e da culpa corrosiva de Aurica."
    ),
    14322: (
        "...",
        "Pausa comovida em respeito à tragédia do passado."
    ),
    14323: (
        "Opa! Acabei me alongando além da conta.\nVamos, depressa rumo a Stonehenge!",
        "Don Leon retoma o senso de urgência para selar a Mudança de Paradigma."
    ),
    14324: (
        "...Não... é impossível!\nComo poderia, se estamos falando de um dragão capaz\nde aniquilar a minha aldeia inteira num piscar de olhos?!",
        "Recaída traumática imediata de Aurica ao reviver mentalmente o massacre."
    ),
    14325: (
        "Aurica!!",
        "Lyner clama assustado com a regressão súbita da amiga."
    ),
    14326: (
        "Exatamente! Eu varro uma aldeia inteira num piscar de olhos.\nMesmo que fossem uma centena de vocês,\neu os esmagaria num instante ainda mais breve!",
        "A projeção do medo renasce alimentada pela insegurança de Aurica."
    ),
    14327: (
        "E então... já fizeram suas preces...?",
        "Ameaça iminente de massacre."
    ),
    14328: (
        "Uwaaaahhh!!!",
        "Grito ao ser atingido pela explosão avassaladora do monstro."
    ),
    14329: (
        "...Ora, ora... Estivemos tão perto.\nNo fim das contas, para a Senhorita Aurica, aquele passado\nainda é uma ferida indelével no coração.",
        "Análise melancólica de Don Leon sobre a profundidade da cicatriz psicológica."
    ),
    14330: (
        "...Não é possível...\nNão haverá meio algum de superar isso de vez?!",
        "Angústia de Lyner diante da persistência do bloqueio."
    ),
    14331: (
        "Bem... tudo dependerá de você, meu caro.",
        "Donsuke transfere a responsabilidade da cura afetiva para Lyner."
    ),
    14332: (
        "Você aí!!",
        "Lyner se volta para encarar o dragão redivivo."
    ),
    14333: (
        "Arrastar-se até este antro sem pestanejar...\nVeio aqui para morrer?!",
        "Zombaria do monstro diante do avanço solitário de Lyner."
    ),
    14334: (
        "Vim aqui para acabar com você!",
        "Resolução heroica de Lyner mesmo desprovido de apoio."
    ),
    14335: (
        "...Acabar comigo?\nKukuku... Que disparate patético.\nVocês jamais serão capazes de me derrotar!",
        "O dragão reforça a impossibilidade de vitória enquanto o medo reinar."
    ),
    14336: (
        "Ele tem razão, Lyner!\nUm dragão desses... jamais poderemos derrotá-lo!\nVamos fugir daqui, por favor...!",
        "Aurica em pânico absoluto cedendo ao impulso de fuga."
    ),
    14337: (
        "Aurica!!",
        "Lyner tenta conter a fuga desesperada da parceira."
    ),
    14338: (
        "Kukuku... Ela abandonou você.\nPois muito bem... tome isto para aprender!!",
        "O monstro se aproveita do isolamento de Lyner para disparar o golpe letal."
    ),
    14339: (
        "Uwaaaahhh!!!",
        "Grito ao ser atingido em cheio pelo ataque avassalador."
    ),
    14340: (
        "...Que sujeito imprudente.\nLançar-se de peito aberto contra um dragão desses...",
        "Don Leon censura a temeridade cega de Lyner."
    ),
    14341: (
        "Mesmo que diga isso, o que mais eu poderia fazer...?",
        "Desabafo frustrado de Lyner buscando uma saída tática."
    ),
    14342: (
        "Enquanto a Senhorita Aurica carecer de confiança em si,\njamais podereis abater esse dragão.\nNa próxima tentativa, investigai ao redor em busca de pistas.",
        "Conselho final de Donsuke apontando a autoconfiança de Aurica como a verdadeira chave mágica da vitória."
    ),
}

# Verificação se todos os 185 IDs estão cobertos
assert len(curations) == 185, f"Esperado 185, obtido {len(curations)}"

# Validação linha a linha contra validador_editorial
hard_gate_errors = 0
lint_warnings = 0

dialogues_output = []
curated_lines_output = []

for item in input_data["dialogues"]:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    orig_en = item["original_en"]
    speaker = item.get("speaker", "")
    speaker_id = item.get("speaker_id", 0)
    event_file = item.get("event_file", "")

    if item_id not in curations:
        print(f"[FATAL] ID {item_id} não encontrado nas curadorias!")
        sys.exit(1)

    ptbr_curated, rationale = curations[item_id]

    # Validação Hard Gate
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=ptbr_curated,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {item_id}: {e}")

    # Lint editorial
    avisos = validador_editorial.auditar_estilo_editorial(ptbr_curated)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

    # Checa \r
    if "\r" in ptbr_curated:
        print(f"[ERROR] ID {item_id}: Contém \\r carriage return!")
        hard_gate_errors += 1

    # Checa pontuação órfã após \n
    parts = ptbr_curated.split("\n")
    for line_part in parts[1:]:
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Linha inicia com pontuação órfã após newline: {line_part!r}")
            hard_gate_errors += 1

    # Checa fratura sintática antes de \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(ptbr_curated)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Fratura sintática antes de \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

    curated_lines_output.append({
        "id": item_id,
        "ptbr_curated": ptbr_curated,
        "rationale": rationale
    })

    dialogues_output.append({
        "id": item_id,
        "event_file": event_file,
        "speaker_id": speaker_id,
        "speaker": speaker,
        "original_jp": orig_jp,
        "original_en": orig_en,
        "curated_ptbr": ptbr_curated,
        "final_ptbr": ptbr_curated,
        "texto_ptbr_curado": ptbr_curated,
        "custom_text": ptbr_curated,
        "ptbr_curated": ptbr_curated,
        "review_status": "approved",
        "reviewed": True,
        "notes": rationale,
        "curation_notes": rationale
    })

print(f"Resultado da validação prévia:")
print(f"Total avaliado: {len(dialogues_output)}")
print(f"Erros Hard Gate: {hard_gate_errors}")
print(f"Avisos Lint: {lint_warnings}")

if hard_gate_errors > 0 or lint_warnings > 0:
    print("Corrija os problemas antes de salvar!")
    sys.exit(1)

# Monta JSON final
glossary_additions = {
    "Angel Rishi": {
        "pt": "Anjo Rishi",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Magia Azul",
        "note": "Entidade onírica que governa a preservação e a razão na Cosmosfera de Misha, convertida na Magia Azul Anjo Rishi (JP 利支天)."
    },
    "Dragonferno": {
        "pt": "Dragonferno",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Magia Vermelha",
        "note": "Magia Vermelha de ataque de fogo gerada na Cosmosfera de Aurica após o enfrentamento contra a projeção do dragão (JP ドラゴンフェルノ)."
    }
}

output_dict = {
    "block_id": "BLK_EVD_061",
    "axis_id": input_data.get("axis_id", "AXIS_3"),
    "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
    "category": input_data.get("category", "Event Dialogue"),
    "line_count": len(dialogues_output),
    "id_range": [dialogues_output[0]["id"], dialogues_output[-1]["id"]],
    "curated_lines": curated_lines_output,
    "glossary_additions": glossary_additions,
    "dialogues": dialogues_output
}

out_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_061_output.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output_dict, f, ensure_ascii=False, indent=2)

print(f"\n[SUCESSO] Arquivo gerado com perfeição em: {out_path}")

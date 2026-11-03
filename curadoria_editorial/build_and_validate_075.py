# -*- coding: utf-8 -*-
"""
build_and_validate_075.py - Constrói e valida BLK_EVD_075_output.json
"""
import json
import sys
import os

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

INPUT_FILE = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_075_input.json"
OUTPUT_FILE = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_075_output.json"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    input_data = json.load(f)

dialogues = input_data["dialogues"]

curated_map = {
    # Event/378.evd (IDs 17017 - 17076)
    17017: ("...O que eu devo fazer agora...?", "Lyner sente-se desorientado e sobrecarregado pelas perdas repentinas de seus mentores."),
    17018: ("A Senhora Shurelia, meu pai...\nAté o Ayatane desapareceu...", "Lyner enumera a ausência dos pilares de sua vida em Platina."),
    17019: ("Por falar nisso... Esse tal Jardim de Prisma\npra onde levaram o seu pai... Onde fica afinal?", "Jack indaga sobre o destino para onde Leard foi levado."),
    17020: ("Se não me engano,\nouvi dizer que fica acima da Blastline.", "Misha recorda a localização geográfica do Jardim de Prisma."),
    17021: ("Então não tem jeito...\nVou ter que atravessar a Blastline...", "Lyner conclui que a travessia da tempestade de plasma é inevitável."),
    17022: ("Lyner...\nO que você realmente quer fazer no fundo do coração?", "Radolf incita o jovem cavaleiro a buscar seu desejo verdadeiro."),
    17023: ("...Eu...\nEu...", "Lyner hesita diante da imensidão da tarefa."),
    17024: ("Por que não tira um tempo\npra pensar com calma?", "Radolf sugere uma pausa necessária para reflexão estratégica."),
    17025: ("É, desculpe...\nVou fazer isso... Me deem um momento, por favor...", "Lyner agradece e afasta-se momentaneamente."),
    17026: ("......", "Lyner em silêncio absorto."),
    17027: ("Hum...", "Lyner suspira em reflexão interior sem rubrica."),
    17028: ("......", "Radolf contempla a estátua em silêncio paciente."),
    17029: ("Comandante-Geral Radolf...?", "Aurica aproxima-se com deferência cerimonial ao líder clerical."),
    17030: ("É exatamente idêntica à estátua da nossa igreja.\nA imagem da [Cantora e o Guardião].", "Radolf reconhece o monumento clássico da fé de Elemia."),
    17031: ("Aurica, você conhece o significado por trás desta estátua?", "Radolf sonda a familiaridade da donzela com os textos sagrados."),
    17032: ("...Sim, eu conheço.", "Aurica responde com modéstia e convicção."),
    17033: ("Desde eras imemoriais, onde ecoar a voz da cantora,\nali estará o seu guardião.", "Aurica entoa a primeira estrofe do poema canônico de Elemia."),
    17034: ("Se o vento soprar a oeste, para o oeste irá;\nse a chuva cair a leste, ao leste marchará.\nMesmo que seu corpo pereça, a donzela há de proteger.", "Aurica recita a estrofe do juramento de proteção incondicional."),
    17035: ("E quando a cantora a ele se entregar pelo laço da confiança,\num sopro de cura e bênção para o mundo... há de florescer.", "Aurica conclui o verso sacro sobre o poder curativo da harmonia."),
    17036: ("...Estou impressionado.\nComo conhecia um clássico tão arcaico e complexo?", "Radolf elogia o notável saber mitológico da jovem."),
    17037: ("É que... desde pequena eu sempre amei as lendas de El Elemia.\nVivia lendo livros de mitologia.", "Aurica compartilha com doçura sua paixão precoce pelas lendas."),
    17038: ("Por isso acabei decorando tudo.", "Aurica justifica sua memória com naturalidade."),
    17039: ("É o laço e a confiança mútua entre a cantora e o guardião\nque tecem sentimentos tão puros e inabaláveis.\nÉ disso que nasce a Magia da Canção de hoje, não é?", "Aurica decifra o elo simbiótico que gera a Magia da Canção."),
    17040: ("Exato.\nO laço de confiança mútua entre a Reyvateil e o humano\né o que gera a magia mais poderosa.", "Radolf confirma o princípio metafísico fundamental."),
    17041: ("Mas essa verdade não se limita apenas à Magia da Canção.", "Radolf eleva a lição para o campo dos relacionamentos humanos."),
    17042: ("Ter companheiros em quem se possa confiar de olhos fechados...\nIsso, por si só, já nos torna mais fortes.", "Radolf ensina o valor transcendental da união."),
    17043: ("Ah...", "Aurica assimila a profundidade do ensinamento."),
    17044: ("O Lyner costuma carregar o peso do mundo nas próprias costas,\nmas acho que ele deveria se apoiar mais nos companheiros.", "Radolf expressa preocupação com o isolamento emocional de Lyner."),
    17045: ("Mesmo aquilo que é impossível para um homem sozinho\npode ser superado quando todos lutam juntos.", "Radolf reitera o poder da superação coletiva."),
    17046: ("É verdade...\nEu também... quero muito conseguir apoiar o Lyner...", "Aurica expressa seu anseio íntimo de sustentar o protagonista."),
    17047: ("E então, Lyner? Já se decidiu?", "Radolf traz o jovem de volta ao conselho de guerra."),
    17048: ("Sim. Tomei minha decisão.", "Lyner manifesta firmeza inabalável."),
    17049: ("Eu vou cruzar a Blastline e subir até Platina.", "Lyner traça a rota audaciosa de resgate."),
    17050: ("Quero resgatar a Senhora Shurelia, o Ayatane e o meu pai.", "Lyner reafirma sua lealdade inegociável à família e mentores."),
    17051: ("E não é só isso...\nEu quero restaurar a paz e o equilíbrio deste mundo!", "Lyner ergue sua vocação heroica pela salvação de Sol Ciel."),
    17052: ("Mas escuta: como você pretende atravessar a Blastline?", "Jack confronta a viabilidade prática da empreitada."),
    17053: ("Tentar cruzar de aeronave é suicídio puro!", "Jack enfatiza a letalidade das tormentas de plasma da barreira."),
    17054: ("...Eu sei muito bem.", "Lyner reconhece a seriedade do alerta."),
    17055: ("É pedir pra morrer! Não dá pra subir por dentro da Torre?", "Jack sugere a rota fechada pelo interior da Torre."),
    17056: ("Subir pelo interior da Torre seria uma opção, claro,\nmas acho quase impossível dar certo agora.", "Lyner avalia os perigos do trajeto interno."),
    17057: ("A Senhora Shurelia monitora os corredores o tempo todo,\ne pode paralisar ou acionar as defesas como quiser.\nSeria perigoso demais.", "Lyner pondera o controle onisciente da Administradora sobre a Torre."),
    17058: ("Pra começo de conversa... eu nunca subi até lá pelo interior da Torre.", "Lyner admite a falta de conhecimento dos acessos internos superiores."),
    17059: ("......", "Jack fica pensativo diante das limitações táticas."),
    17060: ("Então... sobre a aeronave...", "Lyner redireciona o foco para sua alternativa tecnológica."),
    17061: ("A aeronave em que eu vim...\nTalvez ela seja capaz de atravessar a Blastline.", "Lyner cogita a capacidade singular de sua nave de Platina."),
    17062: ("...!!", "Krusche surpreende-se com o potencial mecânico do projeto."),
    17063: ("Fiquei repensando em todas as coisas que ouvi até hoje.", "Lyner articula o raciocínio fundamentado em evidências."),
    17064: ("As aeronaves do Mundo Inferior não conseguem subir até Platina\npor causa das correntes de plasma da Blastline.", "Lyner resume o bloqueio histórico imposto à tecnologia inferior."),
    17065: ("Mas a nave em que eu voava partiu de Platina e desceu até aqui.", "Lyner argumenta a robustez de uma nave originária do Mundo Superior."),
    17066: ("Será que a gente não consegue dar um jeito na nave\nque caiu lá na Floresta de Viola?", "Lyner propõe o plano de restauração da nave acidentada."),
    17067: ("...Gostei da ideia.\nEu topo ajudar. Cruzar a barreira sempre foi meu grande sonho!", "Krusche abraça com fervor a oportunidade de superar o limite dos céus."),
    17068: ("Eu não vou me opor à sua decisão, Lyner.\nVá em frente e dê tudo de si.", "Radolf dá seu aval cavalheiresco e espiritual."),
    17069: ("Beleza, estou dentro.\nNo fim das contas, a gente dá um jeito.", "Jack fecha fileiras com pragmatismo e camaradagem."),
    17070: ("Muito obrigado, pessoal!", "Lyner celebra comovido o apoio unânime do grupo."),
    17071: ("A Krusche já deu uma olhada nela antes\ne disse que consertar era impossível, mas...", "Lyner recorda o veredito prévio pessimista."),
    17072: ("Podemos examinar a carcaça com mais calma dessa vez?", "Lyner solicita uma revisão detalhada do maquinário."),
    17073: ("Quem sabe a gente não encontra uma solução pro conserto?", "Lyner deposita esperança na genialidade da parceira."),
    17074: ("Por mim, tudo bem. Quantas vezes precisar.\nDa última vez foi só uma olhada por cima mesmo.", "Krusche compromete-se a uma perícia minuciosa sem preguiça."),
    17075: ("Conto com você, parceira.", "Lyner sela a aliança de engenharia."),
    17076: ("Plano traçado, rumo à floresta imediatamente!", "Jack comanda a mobilização rápida da equipe."),

    # Event/713.evd (IDs 17077 - 17133)
    17077: ("Lyner!? Você ainda está neste mundo?!\nÉ perigoso demais aqui, era melhor não ter vindo...", "Aurica angustia-se com a vulnerabilidade de Lyner em sua mente dilacerada."),
    17078: ("Escuta, Aurica.\nVamos derrotar o dragão juntos.", "Lyner desafia o carrasco onírico ao lado da donzela."),
    17079: ("O quê...?\nLyner... você perdeu o juízo?!", "Aurica espanta-se com a temeridade do rapaz."),
    17080: ("Falo muito sério. Eu finalmente entendi:\neste lugar é o seu mundo mental, não é?\nSe você acreditar que pode vencer o monstro, você vence!", "Lyner evoca o axioma de que a vontade consciente molda a Cosmosfera."),
    17081: ("Não fala... esse tipo de bobagem...\nAchar que tudo no mundo vai acontecer como a gente quer\né a maior ilusão de todas!", "Aurica expressa a amargura da impotência que marcou sua vida."),
    17082: ("Se fosse assim tão simples...\no meu vilarejo... o meu pai e a minha mãe...\neu teria conseguido salvar os dois...!", "Aurica expõe o luto não cicatrizado pelo massacre familiar."),
    17083: ("Isso é... sobre quando o seu vilarejo foi incendiado?", "Lyner reconhece a raiz do trauma projetado no cenário."),
    17084: ("......", "Aurica silencia diante da memória dolorosa."),
    17085: ("...O Vilarejo de Skuwat, onde eu morava,\nfoi completamente aniquilado num ataque inimigo repentino.", "Aurica relembra a queda trágica de sua aldeia natal."),
    17086: ("Eu era uma Reyvateil, mas meu poder era tão fraco\nque não pude fazer nada... Se eu tivesse mais força,\nmeu pai e minha mãe estariam...", "Aurica flagela-se pela incapacidade de cantar para salvar quem amava."),
    17087: ("Mesmo que não tenha conseguido naquela época, agora pode ser diferente!\nVamos lutar juntos, confia em mim!", "Lyner conclama a donzela a reescrever o desfecho ao seu lado."),
    17088: ("...Não adianta.", "Aurica sucumbe ao desânimo crônico."),
    17089: ("Socorro!! O dragão está atacando outra vez!!", "Guarda anuncia o novo assalto da fera titânica."),
    17090: ("Vocês dois!\nO dragão voltou ao ataque!\nFujam imediatamente daqui!!", "Radolf projeta a advertência desesperada de retirada."),
    17091: ("Radolf!?", "Lyner estranha a presença da persona do companheiro no pesadelo."),
    17092: ("Se ficarem enrolando nesse lugar,\nvão ser varridos pelo turbilhão da tempestade!", "Radolf avisa sobre o vendaval devastador que tudo destrói."),
    17093: ("Socorro...!\nVamos fugir! O vendaval vai jogar a gente longe!", "Aurica entra em pânico temendo a repetição da catástrofe."),
    17094: ("Eu não vou fugir.\nJá te disse, não disse? Eu vou derrotar esse dragão!", "Lyner planta os pés recusando-se a abandonar o posto."),
    17095: ("Não faz isso!\nVocê vai acabar morto, Lyner!", "Aurica desespera-se diante do perigo iminente ao aliado."),
    17096: ("Você realmente acha que eu vou perder...?", "Lyner encara os medos dela com confiança calorosa."),
    17097: ("...Hã?", "Aurica estremece ao confrontar a convicção do cavaleiro."),
    17098: ("Ora, ora, que belo casal!\nNão achei que ainda haveria idiotas perambulando pelas ruas desta vila!", "Bispo Falss, personificando o Dragão no mundo mental, surge debochado."),
    17099: ("Bourd?! O que você está fazendo aqui...?!", "Lyner confunde a figura da cúpula com o oficial da Tenba."),
    17100: ("Do que está falando?!\nEle é o dragão!", "Aurica esclarece o papel simbólico da aberração no sonho."),
    17101: ("...Quê?", "Lyner espanta-se com a lógica delirante da mente."),
    17102: ("Bourd? Quem é esse verme?!\nEu sou o dragão! E vou reduzir este vilarejo a cinzas,\ncomo sempre faço!", "O Dragão reafirma sua sina tirânica e destrutiva sobre a psique."),
    17103: ("Mas antes... vou cuidar de vocês dois!\nCom um bater destas asas, vou arremessar os dois pombinhos\npara os confins do nada!", "O monstro alça voo ameaçando expulsá-los com rajadas cortantes."),
    17104: ("Exatamente como fiz com a sua casa... naquela guerra maldita!", "A manifestação da fera tortura Aurica com lembranças da perda do lar."),
    17105: ("...Aah!!", "Aurica grita diante do choque psicológico."),
    17106: ("Uoooh!!\nO vento tá me arrastando!!", "Lyner tenta se segurar na tormenta gerada pelas asas."),
    17107: ("Voem pelos ares, sumam da minha frente!\nAssim como naquele massacre!\nAssim como a sua patética família!!", "O monstro celebra com sadismo a dor ancestral de Skuwat."),
    17108: ("Não...! Chega... chega disso!\nLyner!!", "Aurica explode em desespero protetor pelo amigo em apuros."),
    17109: ("...V-você...?!", "Aurica vislumbra uma presença misteriosa em socorro."),
    17110: ("▼○$#!...&#@!", "A entidade incompreensível ergue-se barrando o fluxo hostil."),
    17111: ("Mas o que foi isso...?! O vendaval parou... Eu não fui jogado longe...?", "Lyner percebe o escudo erguido em torno de seu corpo."),
    17112: ("C-como é que é...?!\nMaldita... Vou varrer você e esse protetor de uma vez só!!", "O Dragão enfurece-se com a intervenção inesperada."),
    17113: ("...Eu... consegui proteger o Lyner...?!", "Aurica assombra-se ao perceber o próprio escudo operando."),
    17114: ("Aurica! Isso foi incrível!\nViu só?! Eu não te disse?!\nA gente pode vencer! Com certeza a gente vence!!", "Lyner enaltece com entusiasmo a proeza protetora da garota."),
    17115: ("É... é verdade... Quem sabe se a gente...", "Aurica começa a enxergar uma fagulha de esperança na vitória."),
    17116: ("Tsc!... Vou deixar passar só por hoje!\nMas da próxima vez, vou arremessar vocês dois pros confins do mundo!", "O Dragão bate em retirada sob a barreira recém-erguida."),
    17117: ("...Ele foi embora.\nEu não consigo nem acreditar...", "Aurica respira aliviada com a fuga da assombração."),
    17118: ("Droga...\nO desgraçado fugiu...", "Lyner lamenta a fuga do algoz."),
    17119: ("Escuta, Lyner...\nEu comecei a sentir que posso derrotar esse dragão.", "Aurica compartilha seu despertar de força interior."),
    17120: ("Sozinha eu nunca conseguiria, mas... ao seu lado, quem sabe...", "Aurica reconhece que a presença dele é o gatilho de sua coragem."),
    17121: ("É sério mesmo?!", "Lyner alegra-se com a transformação no ânimo dela."),
    17122: ("Sim... Vamos encontrar o dragão, derrotá-lo de vez...\ne devolver a paz a este mundo!", "Aurica assume a determinação heroica de libertar seu subconsciente."),
    17123: ("Você teceu a Magia Azul [Guarda do Vento]!", "Mensagem formal de sistema premiando a conquista mágica."),
    17124: ("...A Senhorita Aurica...\nteceu uma Magia Azul... em seu favor.", "Don Leon observa a tecitura de proteção com olhar crítico."),
    17125: ("Sim. Ela teceu com o coração.", "Lyner reconhece a pureza do ato protetor."),
    17126: ("...Não me agrada nem um pouco,\nmas é a prova incontestável de que ela está abrindo o coração pra você.", "Don Leon admite o desarmamento emocional de sua protegida."),
    17127: ("A Magia Azul é assim...\nEla só floresce quando a Reyvateil deseja proteger alguém com a própria alma,\ne só é tecida em favor daquele a quem ela quer resguardar.", "Don Leon discorre sobre a natureza afetiva e sacra da Magia Azul."),
    17128: ("A Guarda de Fogo anterior, a Senhorita Aurica teceu para resguardar a si mesma...\nMas desta vez, foi descaradamente por sua causa!", "O guardião contrasta a postura defensiva anterior com a devoção atual."),
    17129: ("Entendi...\nAurica... da próxima vez, a gente vai derrubar esse dragão de vez!", "Lyner renova o pacto de vitória contra o monstro interior."),
    17130: ("......", "Don Leon observa calado a cumplicidade que se fortalece."),
    17131: ("O-onde é que a gente veio parar...?!", "Lyner assusta-se com a ejeção para o limbo cósmico."),
    17132: ("...Pelo visto, fomos arremessados até os confins do mundo.", "Don Leon constata com sarcasmo o desfecho turbulento do mergulho."),
    17133: ("Conquistar a confiança plena da Senhorita Aurica\nainda vai exigir uma longa caminhada...\nBem, faça o melhor que puder, pivete.", "Don Leon despede o parceiro com ironia e cobrança de maturidade."),

    # Event/255.evd (IDs 17134 - 17161)
    17134: ("Este lugar é...", "Lyner estranha o ambiente fúnebre do corredor da Torre."),
    17135: ("Vocês não tão ouvindo um zunido agudo no ar? Tipo um 'tzzzz'?", "Krusche capta uma frequência acústica anormal no ambiente."),
    17136: ("...N-não...", "Misha balbucia sentindo os primeiros efeitos da dissonância."),
    17137: ("Misha?", "Lyner nota a aflição repentina da donzela."),
    17138: ("D-desculpa... Eu...", "Misha sente o corpo desfalecer sem motivo aparente."),
    17139: ("Misha! O que você tem?! Firmeza!", "Lyner socorre a amiga com firmeza e carinho."),
    17140: ("Eu tô com medo... Lyner, tô com muito medo!", "Misha entra em pânico puro sem conseguir raciocinar."),
    17141: ("Quando eu olho pra essa porta,\num calafrio repulsivo sobe por todo o meu corpo...", "Misha descreve a rejeição celular provocada pela frequência."),
    17142: ("Não sei explicar o que é, mas não consigo dar mais nenhum passo...\nEu sinto... que vou enlouquecer...!", "Misha implora por socorro diante do colapso sensorial iminente."),
    17143: ("A coisa tá feia!\nVamos tirar ela daqui agora!", "Jack comanda a retirada tática emergencial."),
    17144: ("Como a Misha tá?", "Krusche inquire sobre o quadro clínico da companheira."),
    17145: ("Ela tá bem, só adormeceu.\nO cansaço e o estresse devem ter pesado.", "Lyner acomoda Misha para repousar com segurança."),
    17146: ("Mas me digam uma coisa:\nque diabos de sala era aquela...?", "Jack cobra uma explicação sobre o fenômeno aberrante."),
    17147: ("Ei, Jack. Pode me emprestar aquele mapa um segundo?", "Krusche busca os esquemas da Torre para perícia técnica."),
    17148: ("Eu sabia...\nEssa sala tem alguma tramóia oculta.", "Krusche constata anomalias estruturais na planta."),
    17149: ("Como é que é?!", "Jack reage intrigado."),
    17150: ("Não existe instalação nenhuma ali dentro,\nmas tem uma linha condutora de doryoku gigantesca puxada direto pra lá.", "Krusche revela a alimentação desproporcional para uma sala vazia."),
    17151: ("Provavelmente... aquela câmara tá saturada de energia sinfônica\nnum comprimento de onda repulsivo e insuportável pras Reyvateils.", "Krusche decodifica a natureza anti-Reyvateil da emissão."),
    17152: ("Se uma Reyvateil for forçada a atravessar ali,\na mente ou o corpo dela provavelmente vão entrar em colapso.", "Krusche alerta sobre os danos cerebrais ou físicos irreparáveis."),
    17153: ("...Que roubada.", "Jack lamenta o impasse gerado pela armadilha sonora."),
    17154: ("Devem estar escondendo algo crucial que não querem de jeito nenhum que as Reyvateils vejam.\nOu então...", "Krusche teoriza sobre a censura institucional contra a espécie."),
    17155: ("Escutem... E se nós três fôssemos investigar atrás daquela porta sozinhos?", "Lyner propõe avançar com a vanguarda desprovida de sensibilidade acústica."),
    17156: ("Hã?", "Krusche hesita com a sugestão arriscada."),
    17157: ("Mas a Misha implorou com todas as forças pra gente não deixar ela pra trás, lembra...?", "Krusche teme reativar o trauma de abandono de Misha."),
    17158: ("Eu sei, mas desta vez não tem outro jeito.\nNão é uma questão de mero medo infantil... O perigo ali é real.", "Lyner separa o afeto protetor da imprudência mortal."),
    17159: ("Bom, se o Lyner garante, vamos voltar até aquela porta.", "Jack valida a liderança e decisão de Lyner."),
    17160: ("......", "Krusche concorda com a lógica dos fatos."),
    17161: ("Misha deixou o grupo.", "Aviso de sistema da saída temporária da cantora do grupo ativo."),

    # Event/117.evd (IDs 17162 - 17205)
    17162: ("Certo! Vamos nessa!", "Lyner toma a dianteira partindo para o confronto."),
    17163: ("Caramba!... São gigantescos!!", "Lyner surpreende-se com a estatura colossal das sentinelas."),
    17164: ("...São guardiões da Classe Fortaleza!\nEles vão chamar reforços!", "Misha adverte sobre o perfil de convocação em cadeia dos autômatos."),
    17165: ("Então o único jeito é derrubar tudo antes que o chamado chegue!", "Lyner impõe velocidade para neutralizar a ameaça."),
    17166: ("Pra cima deles!", "Lyner lança o grito de guerra da vanguarda."),
    17167: ("Meus agradecimentos.\nA intervenção de vocês nos salvou de um aperto e tanto.", "Radolf expressa alívio e gratidão pelo auxílio prestado em combate."),
    17168: ("Mas me diga, Lyner: o que faz num lugar como este...?", "Radolf indaga sobre os motivos da presença improvável de Lyner no cais."),
    17169: ("Bem, na verdade...", "Lyner inicia o relato das atribulações recentes."),
    17170: ("Entendo. Por causa da Tenba.", "Radolf deduz a perseguição corporativa com rapidez."),
    17171: ("O aeroporto estava interditado,\nentão o único jeito foi vir a pé.", "Lyner justifica a exaustiva caminhada pelas bordas externas."),
    17172: ("Deve ter sido uma travessia exaustiva.", "Radolf reconhece a penúria da marcha terrestre."),
    17173: ("Fiquei surpreso outro dia quando meu mensageiro voltou de mãos vazias.", "Radolf lamenta o contato que não se concretizou na igreja."),
    17174: ("Mas diante de tais circunstâncias, não havia o que fazer.", "Radolf desculpa a ausência compreensivelmente."),
    17175: ("O que acha de vir conosco?\nEstamos de partida para retornar a Nemo agora mesmo.", "Radolf estende o convite para a viagem rápida na embarcação militar."),
    17176: ("Podemos mesmo?!", "Lyner alegra-se com a hospitalidade inesperada."),
    17177: ("Certamente. Não foi possível da última vez,\nmas ainda desejo muito lhe apresentar o nosso Bispo Falss.", "Radolf reforça seu desejo de promover a reunião com a liderança episcopal."),
    17178: ("Se pudermos pegar carona, com certeza é a opção mais sensata.\nVai nos poupar um tempo precioso.", "Misha aprova o transporte aéreo em prol da economia de tempo."),
    17179: ("Decidido, então.\nSejam muito bem-vindos à nossa embarcação.", "Radolf acolhe formalmente os convidados a bordo."),
    17180: ("Bom, então eu vou nessa.", "Krusche apronta sua partida autônoma."),
    17181: ("Ah, é mesmo.\nVocê tinha vindo recolher a carga aqui no Cais Flutuante, não é?", "Lyner recorda o objetivo comercial original de Krusche."),
    17182: ("Isso aí. Foi pouco tempo,\nmas valeu pela força no caminho. Muito obrigada!", "Krusche agradece com cordialidade despojada a escolta dos cavaleiros."),
    17183: ("Como você vai voltar pra cidade?\nQuer que a gente peça pro pessoal da nave esperar você pegar a carga?", "Lyner oferece a espera da nau para transporte da parceira."),
    17184: ("Não esquenta, tá tudo certo.\nEu tenho a minha própria aeronave pra voltar.", "Krusche dispensa a carona com orgulho de sua autonomia."),
    17185: ("Sua própria aeronave?!", "Lyner pasma diante do fato extraordinário para uma jovem mecânica."),
    17186: ("Ué, não te contei?\nEu sou uma artesã de síntese especializada em aeronaves.", "Krusche define sua maestria alquímica focada em veículos aéreos."),
    17187: ("Especializada bem entre aspas, né...\nSó construí três naves até hoje, ainda tô engatinhando no ramo.", "Krusche ironiza com modéstia suas realizações aeronáuticas impressionantes."),
    17188: ("Construiu três aeronaves inteiras?!", "Lyner abisma-se com o talento prodígio da garota."),
    17189: ("E isso... é o que você chama de estar engatinhando...?", "Misha reage estarrecida com o padrão elevado de exigência da amiga."),
    17190: ("Escuta, Krusche...\nSerá que você não conseguiria consertar a nave em que eu vim?", "Lyner vislumbra a oportunidade de reparar sua embarcação de Platina."),
    17191: ("Hã? A sua aeronave?!", "Krusche espanta-se com a menção da relíquia aérea."),
    17192: ("É. Na verdade... quando eu estava descendo, fui atacado por um monstro.\nA fuselagem quebrou toda e eu tive que fazer um pouso de emergência.", "Lyner recapitula o pouso forçado de sua chegada ao Mundo Inferior."),
    17193: ("Hum... Parece interessante.\nConfesso que bateu uma baita curiosidade de dar uma olhada nela.", "Krusche sente o fascínio profissional pelo maquinário desconhecido."),
    17194: ("É sério?! Sensacional!\nVocê me salvou a vida! Salvou mesmo! Valeu demais!", "Lyner celebra com exuberância a abertura de esperança."),
    17195: ("E-ei, calma lá! Eu só disse que ia dar uma olhada...\nSe for pra consertar de verdade, vai sair uma nota preta!", "Krusche impõe prudência profissional e financeira com seu jeitão pragmático."),
    17196: ("É-é mesmo...?", "Lyner vacila diante da perspectiva dos custos exorbitantes."),
    17197: ("Depende do nível dos danos e das peças.\nNão dá pra adivinhar sem ver antes, então primeiro me leva até lá.", "Krusche estabelece o protocolo de diagnóstico presencial."),
    17198: ("Vocês vão pro Aeroporto de Nemo agora, não vão?", "Krusche alinha o cronograma de deslocamento até a metrópole."),
    17199: ("Eu também vou voar pra Nemo na minha aeronave, então a gente se encontra lá no aeroporto.", "Krusche combina o ponto de reencontro estratégico em Nemo."),
    17200: ("Maravilha!\nConto com você!", "Lyner fecha a parceria de reparo animado."),
    17201: ("Combinado.\nAté mais tarde, então!", "Krusche despede-se com brevidade e espírito dinâmico."),
    17202: ("Krusche deixou o grupo.", "Aviso de sistema registrando a partida de Krusche."),
    17203: ("Muito bem. Vamos aprontar tudo para a nossa partida.", "Radolf inicia a mobilização dos marinheiros sagrados."),
    17204: ("Assim que estiver pronto, é só me avisar.", "Radolf aguarda as ordens de embarque de Lyner."),
    17205: ("Radolf deixou o grupo.", "Aviso de sistema da saída temporária de Radolf.")
}

print(f"Total curated entries mapped: {len(curated_map)}")
assert len(curated_map) == 189, f"Expected 189 lines, mapped {len(curated_map)}"

# Monta estruturas completas
curated_lines = []
dialogues_out = []
lines_rewritten = 0
lines_approved_as_is = 0

for d in dialogues:
    item_id = d["id"]
    orig_jp = d["original_jp"]
    orig_en = d["original_en"]
    curr_pt = d["current_ptbr"]

    if item_id in curated_map:
        text, note = curated_map[item_id]
    else:
        raise ValueError(f"Missing ID {item_id}")

    if text != curr_pt:
        lines_rewritten += 1
    else:
        lines_approved_as_is += 1

    curated_lines.append({
        "id": item_id,
        "text": text,
        "ptbr_curated": text,
        "status": "approved",
        "origin": "curadoria_editorial",
        "notes": note,
        "rationale": note
    })

    dialogue_entry = dict(d)
    dialogue_entry.update({
        "review_status": "approved",
        "text_ptbr": text,
        "curated_ptbr": text,
        "final_ptbr": text,
        "texto_ptbr_curado": text,
        "custom_text": text,
        "ptbr_curated": text,
        "reviewed": True,
        "notes": note,
        "curation_notes": note,
        "curadoria_notes": note
    })
    dialogues_out.append(dialogue_entry)

scene_handoff = {
    "last_scene_id": "Event/117.evd",
    "last_line_id": 17205,
    "resumo_dramatico": (
        "O bloco BLK_EVD_075 reúne quatro arcos dramáticos e fundamentais da saga de Sol Ciel: "
        "(1) Em Event/378.evd, logo após o sequestro e o sumiço simultâneo de Shurelia, Ayatane e do Comandante Supremo Leard, "
        "Lyner é tomado por um vazio existencial e desnorteante. Radolf intervém com sabedoria paternal e conduz o jovem diante da "
        "estátua de 'A Cantora e o Guardião' (謳姫と守護者), onde Aurica recita de cor a milenar lenda de Elemia sobre a proteção incondicional "
        "e o vento curador gerado pela mútua confiança. Inspirado pela camaradagem, Lyner decide romper a Blastline para salvar seus entes "
        "queridos, idealizando recuperar e consertar sua aeronave de Platina caída na Floresta de Viola com o suporte técnico de Krusche. "
        "(2) Em Event/713.evd, no mergulho da Cosmosfera de Aurica, revive-se o trauma primal da destruição do Vilarejo de Skuwat pelo Dragão "
        "(personificado na figura odiosa de Bourd e Falss). Lyner finca os pés contra o vendaval e recusa-se a fugir, despertando em Aurica o ímpeto "
        "sagrado de salvá-lo, o que materializa a tecitura da Magia Azul [Guarda do Vento] (青魔法【ウインドガード】). Don Leon explica que a Magia Azul "
        "só floresce pelo desejo altruísta de proteger outrem, e mesmo com a fuga temporária do Dragão e o arremesso de Lyner ao fim do mundo, "
        "Aurica descobre que ao lado dele poderá vencer seus traumas. "
        "(3) Em Event/255.evd, nos meandros internos da Torre Ar tonelico, Misha entra em pânico e quase sucumbe à loucura ao se deparar com uma "
        "antepara selada. Krusche analisa os esquemas e descobre uma colossal linha de doryoku alimentando o local com uma frequência sônica "
        "destrutiva exclusiva para Reyvateils; Lyner e Jack decidem avançar a vanguarda e investigar o mistério a portas fechadas, poupando Misha em repouso. "
        "(4) Em Event/117.evd, nas imediações do Cais Flutuante (滞空岸壁), Lyner e Misha socorrem Radolf em combate contra guardiões da Classe Fortaleza. "
        "Radolf oferece carona na nau eclesiástica de regresso a Nemo, enquanto Krusche revela ser uma talentosa Grathmelder especializada em aeronaves "
        "com três veículos já construídos. Impressionado, Lyner propõe a reforma de sua nave de Platina acidentada; Krusche aceita o desafio "
        "com pragmatismo comercial, marcando reencontro no Aeroporto de Nemo."
    ),
    "decisoes_terminologicas": {
        "Songstress and Guardian": "謳姫と守護者 (A Cantora e o Guardião / Donzela da Canção e Guardião; estátua e poema sagrado)",
        "Wind Guard": "青魔法【ウインドガード】 / [Guarda do Vento] (Magia Azul tecida por Aurica)",
        "Fire Guard": "青魔法【ファイアーガード】 / Guarda de Fogo (Magia Azul defensiva prévia)",
        "Prism Garden": "プリズムガーデン (Jardim de Prisma / setor superior onde Leard é mantido)",
        "Fortress-Class Guardians": "要塞クラスのガーディアン (Guardiões da Classe Fortaleza)",
        "Symphonic Power Line": "導力ライン (Linha condutora de doryoku / linha de condução de energia sinfônica)",
        "Melder": "メルク (Grathmelder / artesã de síntese especializada em aeronaves)",
        "Viola Forest": "ヴィオラの森 (Floresta de Viola / local da queda da aeronave de Platina)"
    },
    "alertas_para_proximo_bloco": (
        "Nos blocos seguintes (BLK_EVD_076 em diante), manter a simetria terminológica quanto à engenharia de aeronaves de Krusche, "
        "as etapas do conserto na Floresta de Viola, a audiência com o Bispo Falss na Catedral de Nemo e a exploração de setores profundos da Torre."
    )
}

output_payload = {
    "block_id": "BLK_EVD_075",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(dialogues_out),
    "id_range": [dialogues_out[0]["id"], dialogues_out[-1]["id"]],
    "stats": {
        "total_lines": len(dialogues_out),
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "new_terms_added": 4
    },
    "curated_lines": curated_lines,
    "glossary_additions": [
        {
            "term": "Songstress and Guardian",
            "pt": "A Cantora e o Guardião",
            "category": "Lore / Religião de Elemia",
            "note": "謳姫と守護者. Estátua milenar e poema lendário que simboliza a aliança sacrificial do cavaleiro guardião e a Reyvateil cantora."
        },
        {
            "term": "Wind Guard",
            "pt": "Guarda do Vento",
            "category": "Combate / Magia Azul",
            "note": "青魔法【ウインドガード】. Magia Azul protetora tecida por Aurica em sua Cosmosfera para resguardar Lyner do vendaval do Dragão."
        },
        {
            "term": "Fortress-Class Guardians",
            "pt": "Guardiões da Classe Fortaleza",
            "category": "Inimigo / Autômatos",
            "note": "要塞クラスのガーディアン. Sentinelas mecânicas de grande porte da Torre que convocam reforços continuamente."
        },
        {
            "term": "Prism Garden",
            "pt": "Jardim de Prisma",
            "category": "Toponímia / Mundo Superior",
            "note": "プリズムガーデン. Setor de alta tecnologia localizado acima da Blastline para onde o Comandante Leard foi levado cativo."
        }
    ],
    "dialogues": dialogues_out,
    "scene_handoff": scene_handoff
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(output_payload, f, indent=2, ensure_ascii=False)

print(f"Saved {len(dialogues_out)} lines to {OUTPUT_FILE}.")

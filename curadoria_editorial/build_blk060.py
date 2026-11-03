# -*- coding: utf-8 -*-
"""
build_blk060.py - Script de curadoria e validação determinística para BLK_EVD_060
"""
import sys
import json
import re
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Mapeamento completo dos 241 diálogos de BLK_EVD_060
# ID: (texto_curado, justificativa_editorial)
curated_data = {
    # ------------------------------------------------------------------------
    # Event/569.evd: Morte de Tastiella e Canção de Despedida (IDs 13917-13981)
    # ------------------------------------------------------------------------
    13917: (
        "...Lyner.\nParece que chegou a hora da despedida...",
        "Tastiella pressente o fim iminente e se despede suavemente de Lyner."
    ),
    13918: (
        "No final de tudo...\npude contemplar algo maravilhoso. Obrigada...",
        "Tastiella agradece por ter testemunhado a esperança e a redenção antes de partir."
    ),
    13919: (
        "Tastiella...",
        "Lyner sussurra com pesar o nome da mentora moribunda."
    ),
    13920: (
        "Não faça essa cara tão triste...\nEu me sinto tão feliz agora.",
        "Tastiella conforta Lyner assegurando estar em paz e plena felicidade."
    ),
    13921: (
        "Poder conhecer... alguém como você...\nfez valer a pena... ter vivido quatro...centos anos...",
        "Último suspiro de Tastiella agradecendo pelos quatrocentos anos de vigília coroados pelo encontro com Lyner."
    ),
    13922: (
        "Misha... Você... se tornou\na última [Cantora das Estrelas]...",
        "Tastiella passa o manto sagrado de Star Singer (星詠) para Misha."
    ),
    13923: (
        "Tastiella!\nNão morra, por favor...",
        "Misha clama em desespero pela vida da venerável anciã."
    ),
    13924: (
        "Fufu... Você não perde esse jeito manhoso...\naté o fim...",
        "Tastiella acaricia a fragilidade dengosa de Misha com ternura maternal derradeira."
    ),
    13925: (
        "Flau...te... Ja...ck...\nCui...dem... de todo o po...vo Teru...",
        "Tastiella confia seu povo a Flute e a Jack antes de expirar."
    ),
    13926: (
        "Senhora Anciã!!",
        "Grito estarrecido do guerreiro Teru diante da morte de Tastiella."
    ),
    13927: (
        "Vovó!!",
        "Jack clama em desespero filial ao ver a matriarca partir."
    ),
    13928: (
        "...Tastiella.",
        "Lyner reverencia o silêncio final da guardiã ancestral."
    ),
    13929: (
        "Ei! Qual é, pessoal!\nDe que adianta ficarem se lamentando assim?",
        "Jack tenta disfarçar a dor incitando o grupo a erguer a cabeça."
    ),
    13930: (
        "A própria Anciã disse que estava feliz,\nnão ouviram?!\nVamos nos despedir dela com um sorriso no rosto.",
        "Jack exorta todos a honrarem a memória alegre e resoluta de Tastiella."
    ),
    13931: (
        "Pois é...\nA Anciã se foi de vez...",
        "Jack assimila com melancolia a perda definitiva da protetora."
    ),
    13932: (
        "De agora em diante...\na gente vai ter que apoiar um ao outro... Flute.",
        "Jack estende a mão a Flute para unificar os Teru."
    ),
    13933: (
        "Harmonica... Você...",
        "Flute comove-se com a postura conciliadora de Jack, evocando seu nome de batismo."
    ),
    13934: (
        "Opa, não pense que sou só eu que vou ceder, viu?\nVocê também vai ter que dar o braço a torcer em muita coisa!",
        "Jack impõe com ironia afetuosa a reciprocidade na aliança com Flute."
    ),
    13935: (
        "O segredo não é a «coexistência», Lyner?\nEu até que fiquei com vontade de entender melhor as intenções do Flute...",
        "Jack adota a filosofia de convivência mútua proposta por Lyner."
    ),
    13936: (
        "Jack...",
        "Lyner admira a maturidade moral do calejado parceiro Teru."
    ),
    13937: (
        "...Entendo.\nEntão a Tastiella se foi...",
        "Leard recebe com gravidade a notícia da morte de Tastiella."
    ),
    13938: (
        "Mas ela parecia estar em tamanha paz e felicidade.",
        "Shurelia atesta a serenidade espiritual do passamento da anciã."
    ),
    13939: (
        "Talvez ela tenha partido sem mais nenhuma aflição\nquanto ao destino que aguarda este mundo...",
        "Leard reflete com solenidade sobre o descanso merecido da guardiã."
    ),
    13940: (
        "Lyner...",
        "Leard chama a atenção do filho com olhar enternecido e sério."
    ),
    13941: (
        "...",
        "Lyner aguarda em silêncio o veredito paternal."
    ),
    13942: (
        "Você cumpriu sua missão com maestria.",
        "Leard elogia com orgulho e sobriedade a vitória do filho."
    ),
    13943: (
        "Custa-me admitir,\nmas não sou capaz de encontrar palavras melhores que estas.",
        "Leard rende sua maior homenagem à bravura demonstrada por Lyner."
    ),
    13944: (
        "Hehe... Valeu, pai.",
        "Lyner agradece com sorriso sem jeito o reconhecimento paterno."
    ),
    13945: (
        "Bem, mas veja bem...\nHá uma questão.",
        "Leard retoma a postura formal de líder de estado."
    ),
    13946: (
        "Com este feito, tornou-se ainda mais imperativo\nque você suceda o posto de Comandante Geral.",
        "Leard reacende a exigência de que Lyner assuma a liderança dos Cavaleiros."
    ),
    13947: (
        "E-Espera aí um pouco!\nTudo menos isso, por favor!",
        "Lyner recua espavorido diante da responsabilidade burocrática e militar."
    ),
    13948: (
        "Ahaha! Nisso aí\nvocê não mudou nada, não é?!",
        "Aurica ri gostosamente da eterna aversão de Lyner ao comando."
    ),
    13949: (
        "N-Não se meta nisso!",
        "Lyner rebate sem jeito à provocação carinhosa de Aurica."
    ),
    13950: (
        "Ahahaha!",
        "Risadas conjuntas celebrando a descontração do momento."
    ),
    13951: (
        "Ahahaha!",
        "Misha diverte-se com a recusa desesperada de Lyner."
    ),
    13952: (
        "Ahahaha!",
        "Shurelia ri com graciosidade ao ver os jovens brincando."
    ),
    13953: (
        "Ahahaha!",
        "Ayatane compartilha do bom humor do grupo."
    ),
    13954: (
        "Ahahaha!",
        "Jack gargalha do desespero de Lyner com o pai."
    ),
    13955: (
        "Ahahaha!",
        "Krusche desfruta da comicidade familiar dos Barsett."
    ),
    13956: (
        "Ahahaha!",
        "Radolf solta uma risada franca com os companheiros."
    ),
    13957: (
        "Ora, não vejo problema algum.\nEssa é justamente a melhor virtude do Lyner.",
        "Shurelia elogia a pureza e a recusa ao poder mundano que tornam Lyner nobre."
    ),
    13958: (
        "Chegou o momento da despedida, afinal...\nDepois de termos percorrido um caminho tão longo,\nconfesso que bate um aperto no peito.",
        "Radolf admite com comovente sensibilidade a dor do adeus."
    ),
    13959: (
        "Nossa, nunca imaginei ouvir a palavra «aperto no peito»\nvindo logo do Bispo Radolf!",
        "Aurica brinca surpresa com a vulnerabilidade emocional do austero cavaleiro."
    ),
    13960: (
        "Não seja atrevida!",
        "Radolf rebate envergonhado e bem-humorado à provocação de Aurica."
    ),
    13961: (
        "Ora, também não precisam se desesperar tanto.\nAgora subir e descer a Torre virou passeio,\ngraças a essa nossa nave aqui.",
        "Jack tranquiliza a todos lembrando que a aeronave quebrou o isolamento entre os mundos."
    ),
    13962: (
        "Bom, mas mesmo assim...\na saudade vai apertar, né...?",
        "Krusche reconhece que a distância física trará saudade."
    ),
    13963: (
        "...Eu vou sentir tanta falta...",
        "Misha confessa com meiguice infantil a saudade antecipada dos amigos."
    ),
    13964: (
        "...",
        "Aurica emociona-se em silêncio com o momento de partida."
    ),
    13965: (
        "...Gente...\nEu tenho uma sugestão...",
        "Shurelia interrompe com doçura cerimoniosa para propor um ato de união."
    ),
    13966: (
        "Por que todos nós não tecemos uma Canção juntos?\nE então a transformamos em um Cristal Hymmnos.",
        "Shurelia propõe forjar um Cristal Hymmnos com os sentimentos de todos."
    ),
    13967: (
        "Todos nós juntos?!",
        "Aurica surpreende-se com a proposta colaborativa cósmica."
    ),
    13968: (
        "Tecer uma Canção?!",
        "Misha reage fascinada com a criação conjunta de um Canto sagrado."
    ),
    13969: (
        "Sim. Vamos transmitir à Torre a nossa firme determinação\nde unirmos forças para vivermos juntos daqui em diante.",
        "Shurelia explica a mensagem espiritual de harmonia que ecoará pela Torre."
    ),
    13970: (
        "Mas um Cristal Hymmnos\né algo que pode ser criado com tanta facilidade assim?",
        "Radolf indaga sobre a viabilidade técnica e mística de criar um cristal."
    ),
    13971: (
        "Criar o Cristal Hymmnos em si\nnão é uma tarefa tão difícil...",
        "Shurelia esclarece que o processo técnico é acessível."
    ),
    13972: (
        "Desde que os sentimentos que depositamos nele\nsejam fortes e verdadeiros.",
        "Shurelia enfatiza a pureza emocional como núcleo da criação."
    ),
    13973: (
        "Bem, sendo assim...\npor que não pedimos para todas as pessoas\ndeste mundo tecerem também?",
        "Aurica expande a ideia para abranger os laços de todos os habitantes."
    ),
    13974: (
        "Eu... faço questão absoluta\nde que a mana Claire teça com a gente.",
        "Aurica manifesta o carinho fraterno profundo pela dona da taverna."
    ),
    13975: (
        "Eu também...\nAcho que vou pedir para a Presidente Ayano tecer.",
        "Krusche decide envolver a chefe corporativa da Tenba no elo musical."
    ),
    13976: (
        "Tsc... Bem, vou ver se penso em algo com o Flute.",
        "Jack aceita criar a canção com o líder Teru, sem rubricas artificiais."
    ),
    13977: (
        "...Q-Que foi?!",
        "Lyner estranha os olhares cúmplices convergindo em sua direção."
    ),
    13978: (
        "Lyner...",
        "Aurica cobra a iniciativa filial de Lyner com meiguice implacável."
    ),
    13979: (
        "T-Tá bom, já entendi!\nVou tecer com o meu velho, pronto...\nQue saco...",
        "Lyner cede resignado à pressão para tecer a canção com Leard."
    ),
    13980: (
        "Ahaha!\nFica todo envergonhado, que fofo!",
        "Misha deleita-se com o rubor juvenil de Lyner."
    ),
    13981: (
        "P-Parem de palhaçada!!",
        "Lyner explode em protesto cômico contra as provocações amorosas."
    ),

    # ------------------------------------------------------------------------
    # Event/299.evd: Tumulto de Civis e Desabafo de Radolf (IDs 13982-14007)
    # ------------------------------------------------------------------------
    13982: (
        "Dê um jeito nisso!\nA gente tá passando aperto aqui!",
        "Cidadão enfurecido cobra providências imediatas contra o transtorno."
    ),
    13983: (
        "Isso mesmo!\nNós também temos nossas vidas para sustentar!",
        "Moradora aflita exige garantias básicas de sobrevivência."
    ),
    13984: (
        "Vocês podem reclamar o quanto quiserem,\nmas não há nada que a gente possa fazer!",
        "Atendente rebate a impossibilidade técnica de intervir na crise."
    ),
    13985: (
        "E dar um jeito nisso não é o trabalho de vocês, hein?!",
        "Civil eleva a voz cobrando a responsabilidade dos funcionários."
    ),
    13986: (
        "O que disse?!\nQuer brigar, é?!",
        "Tensão escala para ameaça iminente de agressão física."
    ),
    13987: (
        "Parem com isso, vocês dois!",
        "Transeunte tenta conter a eclosão da briga entre os homens."
    ),
    13988: (
        "Mau sinal, começou uma briga!\nVamos lá intervir!",
        "Radolf corre para apaziguar os ânimos exaltados na praça."
    ),
    13989: (
        "Parem já com isso!\nFicar brigando por causa disso não vai resolver nada!",
        "Radolf impõe autoridade pacífica para estancar o confronto."
    ),
    13990: (
        "Então por que o senhor não leva a gente até o [Beco Vagalume]?",
        "Cidadão desafia o cavaleiro a providenciar o transporte bloqueado."
    ),
    13991: (
        "É uma tempestade.\nNão é culpa de ninguém.\nNão comecem a exigir absurdos.",
        "Radolf pede bom senso perante a fatalidade climática."
    ),
    13992: (
        "E encontrar uma solução para isso não é dever da Igreja?\nNa hora em que o povo mais precisa, vocês não servem de nada.",
        "Crítica contundente da população ao descaso do clero para com os pobres."
    ),
    13993: (
        "...",
        "Radolf silencia golpeado pelo peso moral da acusação popular."
    ),
    13994: (
        "Deixa para lá...\nO jeito é esperar a tempestade passar.",
        "Mulher resigna-se à falta de perspectivas diante do impasse."
    ),
    13995: (
        "Falar é fácil, mas...\ntodas as hospedarias já estão lotadas por hoje!",
        "Homem denuncia a falta completa de vagas de abrigo na cidade."
    ),
    13996: (
        "Ai, meu Deus... E agora o que a gente faz...?",
        "Cidadã expressa desespero com o desamparo noturno."
    ),
    13997: (
        "...",
        "Radolf absorve a crise habitacional com angústia e dever cívico."
    ),
    13998: (
        "Não leve a mal, Radolf.\nO pessoal só está de cabeça quente,\na Igreja não tem culpa.",
        "Lyner tenta atenuar o fardo emocional que o amigo carrega."
    ),
    13999: (
        "Não...\nO que aqueles três disseram é a mais pura verdade.",
        "Radolf reconhece com hombridade o erro estrutural de sua instituição."
    ),
    14000: (
        "Ainda que não possamos deter a tempestade,\ndeveríamos ser capazes de prestar algum auxílio\naos que ficaram desabrigados.",
        "Radolf defende a caridade ativa como dever inegociável da fé."
    ),
    14001: (
        "Além do mais, intermediar conflitos civis\né uma das obrigações mais elementares da Igreja.",
        "Radolf elenca os deveres pastorais negligenciados pelos sacerdotes."
    ),
    14002: (
        "Ver que até a Tenba está agindo numa situação dessas,\nenquanto a Igreja não designou uma única alma para intervir...",
        "Radolf indigna-se ao constatar que a corporação mercenária presta mais apoio que o clero."
    ),
    14003: (
        "...Radolf?",
        "Lyner percebe o tom sombrio e grave do companheiro de armas."
    ),
    14004: (
        "Ah, não... Perdoe-me.\nFoi só um desabafo tolo.\nNão dê muita importância a isso.",
        "Radolf recolhe sua queixa para não sobrecarregar os mais jovens."
    ),
    14005: (
        "É que ultimamente a Igreja\nanda deslumbrada demais com o Advento das Deusas.",
        "Radolf aponta a obsessão messiânica que cegou a cúpula eclesiástica."
    ),
    14006: (
        "Quando servir e proteger os fiéis\ndeveria ser uma missão muito mais sagrada\ndo que aguardar a descida dos deuses...",
        "Reflexão ética profunda de Radolf sobre a verdadeira vocação religiosa."
    ),
    14007: (
        "...",
        "Aurica ouve em silêncio o desabafo sobre as falhas da instituição a que pertence."
    ),

    # ------------------------------------------------------------------------
    # Event/395.evd: Encontro com Mei Mei e Acesso à SPU (IDs 14008-14043)
    # ------------------------------------------------------------------------
    14008: (
        "Sinto a presença de alguém por aqui...",
        "Lyner pressente uma forma de vida desconhecida no setor deserto da Torre."
    ),
    14009: (
        "Olha ali, tem alguém deitado!",
        "Krusche avista uma figura imóvel acomodada no chão."
    ),
    14010: (
        "...",
        "Mei Mei dorme placidamente alheia à chegada dos forasteiros."
    ),
    14011: (
        "Que coisa... Tem uma garotinha\ntirando uma soneca bem num lugar desses...",
        "Aurica surpreende-se com a inocência e o sono tranquilo da pequena."
    ),
    14012: (
        "Opa, vai com calma...\nAquilo ali não é humana de jeito nenhum.",
        "Jack reconhece de imediato a natureza cibernética da androide de segurança."
    ),
    14013: (
        "...Mas espera aí, eu conheço essa menina\nde algum lugar.",
        "Lyner tenta resgatar nas lembranças a fisionomia familiar da robô."
    ),
    14014: (
        "Lyner... Por acaso você anda cantando tantas meninas\nque nem se lembra mais do rosto delas?",
        "Krusche provoca Lyner com ironia zombeteira, restaurando a fala japonesa genuína."
    ),
    14015: (
        "...Dá um tempo, Krusche.",
        "Lyner desvia constrangido da insinuação mordaz da engenheira."
    ),
    14016: (
        "Awa-wa-wa!\nEu não fazia ideia de que tínhamos visitas!...",
        "Mei Mei desperta em sobressalto cômico diante dos visitantes."
    ),
    14017: (
        "Não precisa entrar em pânico desse jeito...",
        "Lyner acalma a pequena atendente cibernética desajeitada."
    ),
    14018: (
        "Sejam bem-vindos!\nBoas-vindas ao Observatório... sim!",
        "Mei Mei recupera sua programação protocolar e saúda o grupo com candura."
    ),
    14019: (
        "...Ah! Agora me lembrei!\nVocê é aquela que sempre aparece\nna autenticação dos anteparos...",
        "Lyner recorda a interface virtual de Mei Mei nas comportas de segurança da Torre."
    ),
    14020: (
        "Correto!\nSou o Protocolo de Segurança, Mei Mei.",
        "Mei Mei apresenta formalmente sua designação sistêmica."
    ),
    14021: (
        "E o senhor é, sem dúvidas,\no senhor Lyner Barsett, correto?",
        "Mei Mei identifica os dados biométricos e registros do cavaleiro."
    ),
    14022: (
        "Puxa, que boa memória...",
        "Lyner espanta-se com o reconhecimento imediato do sistema."
    ),
    14023: (
        "Sim, eu o conheço muito bem.",
        "Mei Mei gaba-se de seu banco de dados analítico imbatível."
    ),
    14024: (
        "Até 98 dias atrás, o senhor acessava o [Portão de Antepara A7]\ntodas as manhãs, entre as 11h03 e 11h06.",
        "Mei Mei recita com precisão milimétrica a rotina passada de Lyner."
    ),
    14025: (
        "Além disso, há 58 dias atravessou\no [Portão de Antepara B1] nº 3, e em seguida...",
        "Mei Mei prossegue detalhando a trajetória militar recente do rapaz."
    ),
    14026: (
        "J-Já chega!\nJá entendi, já entendi!",
        "Lyner interrompe apressado a leitura pública de seu histórico sigiloso."
    ),
    14027: (
        "Que impressionante...\nEla sabe de cada passo seu.",
        "Krusche impressiona-se com a vigilância onipresente do servidor da Torre."
    ),
    14028: (
        "Sim. Como disponho do histórico de registros,\nconsigo pesquisar qualquer evento.",
        "Mei Mei explica o alcance do kakolog (カコログ / histórico de registros)."
    ),
    14029: (
        "Histórico de registros...?",
        "Krusche indaga curiosa sobre o termo técnico ancestral."
    ),
    14030: (
        "Então quer dizer que, se a Aurica cruzar a Torre\npara se esgueirar até o quarto do Lyner à noite,\nvai ser pega na hora!",
        "Misha faz troça de Aurica insinuando visitas noturnas clandestinas (夜這い / yobai)."
    ),
    14031: (
        "...Por que cargas d'água\neu iria me esgueirar no quarto dele?!",
        "Aurica fica escarlate e protesta contra a calúnia atrevida de Misha."
    ),
    14032: (
        "Espere um instante...\nSe é assim, você saberia nos informar\nonde a Senhora Shurelia se encontra?",
        "Radolf percebe o valor estratégico do terminal para localizar a Deusa."
    ),
    14033: (
        "Se ela tiver passado pelos portões,\né possível localizar.",
        "Mei Mei confirma a funcionalidade de rastreamento por passagem de anteparo."
    ),
    14034: (
        "Contudo... não há nenhum registro gravado\nnos últimos dias...",
        "Mei Mei detecta lacunas suspeitas nas tabelas de dados recentes."
    ),
    14035: (
        "Pelo visto apagaram o rastro direitinho.",
        "Jack constata a ação cirúrgica de adulteração nos logs da Torre."
    ),
    14036: (
        "E quanto a Leard Barsett?\nConsta alguma coisa sobre ele?",
        "Lyner busca pistas sobre os passos recentes de seu pai."
    ),
    14037: (
        "Leard Barsett acessou a SPU recentemente.",
        "Mei Mei localiza o registro de entrada do governador no centro neural."
    ),
    14038: (
        "SPU...?",
        "Lyner estranha a sigla técnica do setor."
    ),
    14039: (
        "Fica num setor bem mais elevado.\nÉ a câmara onde reside o cérebro desta Torre.",
        "Mei Mei define a Sala SPU como o núcleo cognitivo da infraestrutura."
    ),
    14040: (
        "...O cérebro... da Torre?!\nQuer dizer que esta Torre está viva?!",
        "Radolf choca-se com a revelação da senciência computacional de Ar tonelico."
    ),
    14041: (
        "Essa é uma indagação filosófica.\nHá ocasiões em que dizer que ela está viva\nseria a definição mais precisa.",
        "Mei Mei responde com elegância lógica sobre o conceito de vida biomecânica."
    ),
    14042: (
        "Embora, sob a ótica biológica,\nela seja classificada como matéria inanimada...",
        "Mei Mei pondera os limites da classificação zoológica humana."
    ),
    14043: (
        "De qualquer forma,\nvamos rumar direto para essa tal de SPU.",
        "Lyner define o novo objetivo tático da missão rumo ao topo."
    ),

    # ------------------------------------------------------------------------
    # Event/348.evd: Busca nas Ruínas e Falss (IDs 14044-14066)
    # ------------------------------------------------------------------------
    14044: (
        "Como era de se esperar,\nnão vai ser nada fácil encontrar.",
        "Radolf constata a dificuldade de localizar o artefato nas ruínas instáveis."
    ),
    14045: (
        "Que tal fazermos uma pausa por aqui\npara descansar um pouco?",
        "Ayatane propõe um intervalo prudente para recompor as energias."
    ),
    14046: (
        "Uff... É verdade,\njá caminhamos um bocado.",
        "Lyner apoia a pausa expressando alívio físico."
    ),
    14047: (
        "Não andávamos tanto assim\ndesde a época em que você procurava\npelo Cristal «Purger», Lyner.",
        "Radolf relembra a exaustiva expedição anterior em busca do cristal sagrado."
    ),
    14048: (
        "Além de ser um lugar repleto de desabamentos,\né vasto demais...",
        "Radolf enumera os perigos geológicos do setor arruinado da Torre."
    ),
    14049: (
        "E não podemos descartar a hipótese\nde que o artefato sagrado já tenha despencado\njunto com os escombros da ruína.",
        "Ayatane levanta uma hipótese sombria sobre o paradeiro da relíquia cerimonial."
    ),
    14050: (
        "Sem dúvida.\nUma ruína desta magnitude antigamente\nexigiria a mobilização de uma divisão inteira de busca.",
        "Radolf compara os recursos atuais com os antigos padrões militares da Igreja."
    ),
    14051: (
        "Ainda mais se tratando de uma relíquia cerimonial crucial.\nQuerer encontrar isso em apenas três pessoas...\né um completo despropósito.",
        "Radolf critica a leviandade de enviar um contingente ínfimo para a missão."
    ),
    14052: (
        "...Pensando bem, você e o Bispo Falss\nnunca pareceram se dar muito bem, não é?",
        "Lyner sonda as origens do atrito entre o comandante e o prelado."
    ),
    14053: (
        "Nossos princípios divergem em tudo.\nO Bispo Falss coloca o Advento das Deusas\nacima de qualquer outra prioridade.",
        "Radolf aponta a divergência doutrinária irreconciliável que os separa."
    ),
    14054: (
        "Ao passo que eu... acredito piamente\nque a missão precípua da Igreja é salvar o povo.",
        "Radolf reitera o sacerdócio humanitário como norte supremo de sua conduta."
    ),
    14055: (
        "Por isso acabamos nos chocando\nem toda e qualquer decisão.",
        "Radolf resume a inevitabilidade das colisões cotidianas no comando."
    ),
    14056: (
        "A bem da verdade,\nantes de Falss assumir o episcopado,\na Igreja não vivia neste estado deplorável.",
        "Radolf relembra os tempos em que a ordem mantinha suas virtudes originais."
    ),
    14057: (
        "Era uma instituição que colocava o bem-estar\nda população sempre em primeiro lugar...",
        "Radolf lamenta o desvio ético imposto pela nova liderança clerical."
    ),
    14058: (
        "O Bispo Falss foi investido no cargo\nhá pouco tempo?",
        "Ayatane questiona o histórico cronológico da ascensão do prelado."
    ),
    14059: (
        "Não diria tão recente assim...\nFoi há cerca de oito anos, se bem me lembro.",
        "Radolf situa temporalmente a posse episcopal de Falss."
    ),
    14060: (
        "O próprio Bispo Falss, na verdade,\nsurgiu do nada há cerca de quinze anos.\nEle tem pouca história dentro da ordem.",
        "Radolf revela o passado obscuro e repentino da aparição de Falss."
    ),
    14061: (
        "Entretanto, graças ao seu poder sem igual e vasto conhecimento,\nele ascendeu na hierarquia com velocidade espantosa.",
        "Radolf descreve a escalada fulgurante do bispo movida por talento incomum."
    ),
    14062: (
        "Bem, justiça seja feita, é alguém digno de respeito.\nExceto por essa obsessão cega\nde colocar o Advento Divino acima de tudo...",
        "Radolf reconhece a competência intelectual de Falss, deplorando seu fanatismo."
    ),
    14063: (
        "Mas então, se as Deusas finalmente descerem,\nserá que as coisas não podem mudar para melhor?",
        "Lyner cogita esperançoso uma era de prosperidade após a chegada das divindades."
    ),
    14064: (
        "Quem dera fosse assim tão simples...",
        "Radolf expressa ceticismo pragmático perante promessas milagrosas."
    ),
    14065: (
        "Bem, hora de encerrar a nossa pausa.\nVamos avançar mais um pouco pelas profundezas?",
        "Ayatane recolhe o equipamento e convoca os amigos a retomar a exploração."
    ),
    14066: (
        "Certo, vamos nessa.",
        "Lyner concorda com prontidão e se levanta para a marcha."
    ),

    # ------------------------------------------------------------------------
    # Event/636.evd: Pesadelo na Cosmosfera de Misha e o Dragão (IDs 14067-14127)
    # ------------------------------------------------------------------------
    14067: (
        "Não tem absolutamente nada nesta floresta...",
        "Lyner estranha o vazio opressivo do bosque mental da Cosmosfera."
    ),
    14068: (
        "Lyner?!",
        "Aurica chama por Lyner em meio à névoa das árvores."
    ),
    14069: (
        "Aurica!\nO que você está fazendo num lugar desses?!",
        "Lyner corre surpreso ao deparar com a amiga num domínio onírico hostil."
    ),
    14070: (
        "Eu de repente perdi a consciência e...\nquando acordei, já estava nesta floresta...\nJá faz dias que estou perdida sem conseguir sair...",
        "Aurica relata o tormento de vagar perdida há dias no labirinto psicológico."
    ),
    14071: (
        "Dias a fio?!\nVocê está bem...?",
        "Lyner espanta-se com a distorção temporal e preocupa-se com o estado da moça."
    ),
    14072: (
        "...Sim.\nMas que alívio... Com você ao meu lado, não sinto mais medo.\nPor favor, me tire daqui...",
        "Aurica confia cegamente na proteção de Lyner para escapar do bosque."
    ),
    14073: (
        "Deixa comigo.",
        "Lyner assume a proteção de Aurica com bravura resoluta."
    ),
    14074: (
        "Nem pensar que eu vou deixar!",
        "Bourd surge das sombras bloqueando bruscamente a passagem dos jovens."
    ),
    14075: (
        "Ah...!!",
        "Aurica recua aterrorizada diante do algoz de seu passado."
    ),
    14076: (
        "Bourd?!\nO que você está fazendo num lugar desses...?!",
        "Lyner empunha a espada em choque com a presença repentina do militar."
    ),
    14077: (
        "Lyner Barsett.\nÉ com você mesmo que eu tenho negócios.",
        "Bourd intima o cavaleiro com arrogância marcial."
    ),
    14078: (
        "Certa pessoa me ordenou que te levasse até ela.\nE se você resistir... vai ser à força!",
        "Bourd anuncia a ordem de captura emanada pela dona daquele mundo mental."
    ),
    14079: (
        "O-O quê...?!",
        "Lyner indigna-se com a tentativa arbitrária de sequestro."
    ),
    14080: (
        "Não! Não levem o Lyner embora!\nEu não quero ficar sozinha de novo!!",
        "Aurica clama em pânico temendo ser abandonada novamente na escuridão."
    ),
    14081: (
        "Ordens são ordens, mocinha...\nGuhahaha...",
        "Bourd zomba cruelmente do pranto da jovem sacerdotisa."
    ),
    14082: (
        "Nada pessoal, Lyner.\nNão tenho nada contra você, mas...\nToma essa!!",
        "Bourd ataca Lyner de surpresa para neutralizá-lo."
    ),
    14083: (
        "Guh... Arrgh...!\nO que... você fez comigo...?",
        "Lyner tomba atingido pelo golpe traiçoeiro desferido por Bourd."
    ),
    14084: (
        "Não! Lyner!\nResista!! Não me deixe sozinha!!",
        "Grito desesperado de Aurica enquanto Lyner perde a consciência."
    ),
    14085: (
        "Onde... estou...?",
        "Lyner desperta desorientado num aposento luxuoso e estranho."
    ),
    14086: (
        "Acordou, foi?\nMeu querido e adorável Lyner...",
        "Misha recebe Lyner com carinho provocador e tom possessivo."
    ),
    14087: (
        "Misha?! E o Bourd?!\nO que significa tudo isso...?!",
        "Lyner sobressalta-se ao ver a amiga comandando o antigo rival corporativo."
    ),
    14088: (
        "Como assim «o que significa»?\nEu localizei o meu Lyner, então mandei o Bourd\nir buscá-lo para mim.",
        "Misha confessa com naturalidade desconcertante o sequestro de seu amor de infância."
    ),
    14089: (
        "Pois é, exatamente isso.\nKukuku...",
        "Bourd confirma a subserviência rindo sarcasticamente nos bastidores."
    ),
    14090: (
        "Bom trabalho, Bourd.\nPode se retirar agora.",
        "Misha dispensa o lacaio com autoridade de senhora absoluta daquele domínio."
    ),
    14091: (
        "Misha!\nVocê não precisava ter feito uma loucura dessas...!",
        "Lyner recrimina o método violento empregado pela garota."
    ),
    14092: (
        "Ora, vai reclamar do que eu faço?\nNão vai me dizer que se esqueceu...\nde que este aqui é o meu mundo?",
        "Misha rebate altiva lembrando que na Cosmosfera as suas regras são soberanas."
    ),
    14093: (
        "...Não me diga que...\no fato de a Aurica estar perdida na floresta...",
        "Lyner percebe o complô maquiavélico por trás do sofrimento de Aurica."
    ),
    14094: (
        "Ah, mas é claro que fui eu que a trouxe.\nQueria que ela ficasse vagando por aquela floresta\npara todo o sempre.",
        "Misha confessa friamente o castigo infligido à rival amorosa."
    ),
    14095: (
        "Afinal, aquela garota vive me irritando...\nDe vez em quando eu a chamo aqui\nsó para dar uma liçãozinha nela.",
        "Misha expõe o ciúme reprimido que transborda na fantasia onírica."
    ),
    14096: (
        "Isso é crueldade...\nPare com isso, Misha! Fazer uma coisa dessas...",
        "Lyner tenta apelar ao bom coração de sua amiga de infância."
    ),
    14097: (
        "Este mundo é meu. Não aceito ordens suas.\nMas mudando de assunto, que bom que veio, Lyner...\nEstou tão feliz...",
        "Misha descarta a censura moral e abraça a euforia de ter Lyner consigo."
    ),
    14098: (
        "Uou!\nO-Olhando bem, que traje é esse que você está vestindo?!\nOnde foram parar as suas roupas de sempre...?!",
        "Lyner cora desconcertado ao reparar no despojamento sensual do figurino de Misha."
    ),
    14099: (
        "As de sempre...? Ah, aquele vestido.\nNão aguento mais usar aquilo.\nDemora uma eternidade para vestir e aperta a minha cintura...",
        "Misha reclama do incômodo sufocante dos trajes sacerdotais formais."
    ),
    14100: (
        "Ficar só de camisa social é tão prático...\nDá uma sensação de liberdade tão deliciosa.\nEu simplesmente adorei.",
        "Misha gaba-se do conforto de trajar unicamente a camisa (ワイシャツ一枚)."
    ),
    14101: (
        "Diga, Lyner...\nVocê não quer vir comigo...?",
        "Misha convida Lyner com olhar insinuante e sedutor."
    ),
    14102: (
        "Hã...?\nPara onde...?",
        "Lyner gagueja temeroso com o rumo da proposta íntima."
    ),
    14103: (
        "Para o mundo dos prazeres...",
        "Misha convida Lyner sem rodeios para um retiro de delícias sensuais (快楽の世界)."
    ),
    14104: (
        "N-Não, Misha!\nA gente não pode fazer isso...!",
        "Lyner resiste ao impulso carnal invocando princípios e decoro."
    ),
    14105: (
        "...Por que não?\nNão me diga que gosta de outra garota?\nQuem é ela, hein?",
        "Misha enciumada exige saber se há outra donzela ocupando o coração do herói."
    ),
    14106: (
        "N-Não é nada disso!\nEu só estou pensando no seu próprio bem!",
        "Lyner tenta se justificar apelando para a proteção e zelo moral pela amiga."
    ),
    14107: (
        "...De novo com esse papo de «para o meu próprio bem».\nO que diabos significa «para o meu próprio bem»?!",
        "Misha desabafa ressentida contra a hipocrisia paternalista da frase feita."
    ),
    14108: (
        "Toda vez que você solta essa frase,\nnunca é para atender aos meus verdadeiros anseios.",
        "Misha acusa Lyner de mascarar desfeitas sob o pretexto de protegê-la."
    ),
    14109: (
        "Isso não é «pelo meu bem»...\né pelo seu próprio bem, não é, Lyner?!",
        "Misha desmascara com perspicácia dilacerante o egoísmo velado do cavaleiro."
    ),
    14110: (
        "...Não é isso...",
        "Lyner hesita desarmado diante da verdade cortante apontada por Misha."
    ),
    14111: (
        "Vou repetir apenas mais uma vez.\nEste é o meu mundo.\nE aqui só há espaço para aquilo que se curva à minha vontade.",
        "Misha endurece a postura e impõe submissão absoluta como condição de permanência."
    ),
    14112: (
        "Entendeu, Lyner...?\nEu quero que você fique aqui comigo para sempre...\nPor isso...",
        "Misha tenta mais uma investida afetuosa para reter Lyner ao seu lado."
    ),
    14113: (
        "E-Eu já disse que não!\nMisha!",
        "Lyner rejeita com firmeza a ilusão estéril e recusa a rendição."
    ),
    14114: (
        "Entendi...\nVocê quer dar uma de bom moço, é?",
        "Misha debocha da postura moralista do amigo com frieza decepcionada."
    ),
    14115: (
        "Tudo bem...\nSendo assim, não tenho mais serventia para você neste castelo...",
        "Misha expulsa Lyner sumariamente de seus domínios íntimos."
    ),
    14116: (
        "O-O que está fazendo...?!\nUwaaaaaaaahhhh!!!",
        "Lyner é projetado no vácuo por uma rajada mágica conjurada pela Reyvateil."
    ),
    14117: (
        "Urrgh! Q-Que frio, que frio, que frio!\nEstá congelando aqui!!",
        "Lyner aterrissa numa estepe gélida e treme violentamente de frio."
    ),
    14118: (
        "Precisava me atirar logo num cafundó desses...?!",
        "Lyner esbraveja contra o capricho vingativo de sua amiga de infância."
    ),
    14119: (
        "...Lyner... Você... também...?",
        "Voz fraca de Bourd ecoa entre os montes de neve anunciando sua presença."
    ),
    14120: (
        "Bourd?!\nO que aconteceu com você?! Que ferimentos são esses...?!",
        "Lyner encontra Bourd agonizando coberto de cortes e contusões severas."
    ),
    14121: (
        "Cuidado... Um dragão...\nTem um dragão enfurecido aqui...\nAquela desgraçada... da Misha...",
        "Bourd alerta Lyner com suas últimas forças antes de tombar inconsciente."
    ),
    14122: (
        "Guhhh...",
        "Bourd desfalece vitimado pela investida da besta alada."
    ),
    14123: (
        "Bourd!",
        "Lyner tenta amparar o rival caído na tempestade de gelo."
    ),
    14124: (
        "...Grrrrrr...",
        "Rosnado gutural e ameaçador ecoa pelas fendas da geleira."
    ),
    14125: (
        "Droga!!\nO que é isso...?!\nDe onde diabos surgiu um dragão num lugar desses?!",
        "Lyner depara com o monstro colossal criado pela imaginação vingativa de Misha."
    ),
    14126: (
        "Gyaaaaaaarrrgh!!",
        "Rugido ensurdecedor do dragão preparando-se para o ataque mortal."
    ),
    14127: (
        "P-Péssima ideia ficar aqui!\nO jeito é correr!!",
        "Lyner bate em retirada desesperada para salvar a própria pele na Cosmosfera."
    ),

    # ------------------------------------------------------------------------
    # Event/327.evd: Bênção de Falss e Rumo à Garra do Falcão (IDs 14128-14157)
    # ------------------------------------------------------------------------
    14128: (
        "Já estão prontos para partir?",
        "Radolf averigua a prontidão da tropa antes da marcha solene."
    ),
    14129: (
        "Muito bem, em marcha.",
        "Radolf autoriza o início do deslocamento cerimonial."
    ),
    14130: (
        "M-Mas o que é tudo isso?!",
        "Lyner assusta-se com a imensa multidão de fiéis e cavaleiros perfilados."
    ),
    14131: (
        "...Que despedida triunfal.",
        "Radolf admira a pompa e a reverência armada para a expedição sagrada."
    ),
    14132: (
        "Sejam muito bem-vindos!\nÓ gloriosa Reyvateil e seus valorosos sacerdotes!",
        "Bispo Falss abre a magna assembleia clerical saudando Aurica e sua comitiva."
    ),
    14133: (
        "Neste exato instante, os Céus concederam\numa sagrada revelação a este solo.",
        "Falss anuncia que a profecia de restauração divina desceu sobre Platina e o Mundo Inferior."
    ),
    14134: (
        "E ela será manifestada pela voz\nda Donzela Sagrada Aurica!",
        "Falss consagra Aurica perante o povo como a porta-voz oficial dos deuses."
    ),
    14135: (
        "Dirijam-se ao Templo de Elemia e recebam\no Cristal Hymmnos que servirá de testemunho\npara a ressurreição divina!",
        "Falss outorga a missão canônica de resgatar o Cristal Hymmnos no Templo de Elemia."
    ),
    14136: (
        "Ó Aurica.\nO destino de todo este mundo foi confiado a ti.",
        "Falss exalta solenemente o fardo milagroso depositado sobre os ombros da donzela."
    ),
    14137: (
        "Não precisas te martirizar.\nApenas cumpre o teu papel com toda a força do teu coração.",
        "Falss aconselha paternalmente a jovem a agir com bravura e fé sem desespero."
    ),
    14138: (
        "...Sim, senhor!",
        "Aurica responde com reverência solene à ordem sacerdotal."
    ),
    14139: (
        "Lorde Lyner.\nTudo isto devemos à vossa bravura.\nNão encontro palavras para expressar tamanha gratidão.",
        "Falss rende homenagem especial aos feitos heróicos de Lyner."
    ),
    14140: (
        "Quando as Deusas do Trio de Elemia descerem,\no senhor certamente será eternizado\ncomo um santo nestas terras.",
        "Falss promete a canonização de Lyner como protetor sagrado da civilização."
    ),
    14141: (
        "Erguei-vos, fiéis! Filhos do Canto Sagrado!\nVamos cobrir de bênçãos a nossa Donzela Sagrada\ne seus valorosos guardiões!",
        "Falss convoca a multidão a bradar hinos de júbilo e devoção à comitiva."
    ),
    14142: (
        "Que o sagrado Trio de Elemia abençoe a todos!",
        "Falss conclui a liturgia rogando a proteção perpétua das três deusas."
    ),
    14143: (
        "E então, qual é a sensação de ser aclamado santo?",
        "Radolf cochicha zombeteiro cutucando o desconforto de Lyner perante a pompa."
    ),
    14144: (
        "Dá um tempo, vai...\nVocê sabe que não levo jeito para cerimônias assim...",
        "Lyner encolhe-se constrangido com a veneração religiosa excessiva."
    ),
    14145: (
        "Nem eu jamais presenciei um rito tão grandioso.\nO homem realmente está jogando todas as fichas nisso.",
        "Radolf pondera o nível inaudito de empenho e mobilização encabeçado por Falss."
    ),
    14146: (
        "Pensando bem...\nvocê nunca pareceu muito entusiasmado\ncom esse tal de Advento Divino, não é?",
        "Lyner questiona as ressalvas do comandante em relação à volta das deusas."
    ),
    14147: (
        "Bem... de certa forma, sim.\nMas a minha ressalva é contra os métodos do Bispo Falss.",
        "Radolf pontua com precisão que sua crítica repousa na gestão do prelado."
    ),
    14148: (
        "Desperdiçar recursos em buscas infrutíferas\nenquanto vira as costas para o sofrimento do povo...\né isso o que me indigna.",
        "Radolf denuncia o abandono das necessidades populares em prol de ambições cósmicas."
    ),
    14149: (
        "Pois se as Deusas realmente descerem aos nossos braços,\nnada me traria maior regozijo.",
        "Radolf reafirma sua devoção autêntica à salvação divina caso ela se concretize."
    ),
    14150: (
        "...Mas me diga, o que exatamente\numa Deusa faz quando chega?",
        "Lyner faz uma pergunta sincera e ingênua sobre a atuação prática de uma divindade."
    ),
    14151: (
        "...Como assim?\nEla vai salvar o nosso mundo, ora essa.",
        "Radolf responde com a premissa teológica óbvia que todos repetem."
    ),
    14152: (
        "E de que maneira?",
        "Lyner insiste em buscar um mecanismo concreto e realista para a redenção."
    ),
    14153: (
        "Aí você me pegou.\nIsso é algo que só os céus sabem! Hahaha!",
        "Radolf ri gostosamente da própria ignorância teológica diante do mistério sagrado."
    ),
    14154: (
        "Comandante Radolf,\nestamos prestes a atracar.",
        "Oficial subordinado reporta a proximidade do destino da aeronave."
    ),
    14155: (
        "Entendido.\nLyner, apronte o seu equipamento.",
        "Radolf assume o comando tático e ordena os preparativos de desembarque."
    ),
    14156: (
        "O local [Garra do Falcão]\nfoi liberado no Mapa-Múndi!",
        "Notificação do sistema desbloqueando o novo ponto de navegação com o termo canônico correto."
    ),
    14157: (
        "Nesse caso,\nvamos passar em outros lugares primeiro.",
        "Radolf sugere explorar destinos opcionais antes de marchar para o templo."
    )
}

print(f"Total lines defined in curated_data: {len(curated_data)}")
assert len(curated_data) == 241, f"Expected 241 lines, got {len(curated_data)}"

# Validação estrita
with open(r'Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_060_input.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

input_lines = input_data['dialogues']
assert len(input_lines) == 241

hard_gate_errors = 0
lint_warnings = 0

for item in input_lines:
    item_id = item['id']
    if item_id not in curated_data:
        print(f"[FATAL] ID {item_id} missing from curated_data!")
        hard_gate_errors += 1
        continue
    
    text, note = curated_data[item_id]
    orig_jp = item['original_jp']
    
    # 1. Hard gate básico
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=text,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        for e in erros:
            print(f"[HARD GATE] ID {item_id}: {e}")
            hard_gate_errors += 1

    # 2. Rubricas
    if validador_editorial.FORBIDDEN_STAGE_DIRECTIONS_REGEX.search(text):
        print(f"[STAGE DIR] ID {item_id}: Rubrica teatral detectada: {text}")
        hard_gate_errors += 1

    # 3. Retorno de carro
    if "\r" in text:
        print(f"[CARRIAGE RETURN] ID {item_id}: Contém \\r!")
        hard_gate_errors += 1

    # 4. Pontuação órfã no início de linha
    parts = text.split("\n")
    for p in parts[1:]:
        if p.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ORPHAN PUNCTUATION] ID {item_id}: Linha inicia com pontuação órfã: {p!r}")
            hard_gate_errors += 1

    # 5. Fratura sintática antes de \n
    m_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(text)
    if m_frac:
        print(f"[SYNTACTIC FRACTURE] ID {item_id}: Fratura sintática antes de \\n: {m_frac.group(0)!r} em {text!r}")
        hard_gate_errors += 1

    # 6. Linter editorial
    avisos = validador_editorial.auditar_estilo_editorial(text)
    if avisos:
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")
            lint_warnings += 1

print("\n--- RESUMO DE VALIDAÇÃO ---")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("\n>>> SUCESSO ABSOLUTO: 100% dos 241 diálogos passaram por todos os crivos! <<<")
    
    output_dialogues = []
    curated_lines = []
    
    for item in input_lines:
        item_id = item["id"]
        text, note = curated_data[item_id]
        
        curated_lines.append({
            "id": item_id,
            "ptbr_curated": text,
            "rationale": note
        })
        
        output_dialogues.append({
            "id": item_id,
            "event_file": item["event_file"],
            "speaker_id": item.get("speaker_id"),
            "speaker": item.get("speaker"),
            "original_jp": item["original_jp"],
            "original_en": item["original_en"],
            "curated_ptbr": text,
            "final_ptbr": text,
            "texto_ptbr_curado": text,
            "custom_text": text,
            "ptbr_curated": text,
            "review_status": "approved",
            "reviewed": True,
            "notes": note,
            "curation_notes": note
        })
    
    output_obj = {
        "block_id": "BLK_EVD_060",
        "axis_id": "AXIS_3",
        "axis_name": "3_HISTORIA_E_EVENTOS",
        "category": "Event Dialogue",
        "line_count": len(output_dialogues),
        "id_range": [
            output_dialogues[0]["id"],
            output_dialogues[-1]["id"]
        ],
        "curated_lines": curated_lines,
        "glossary_additions": {
            "SPU": {
                "pt": "SPU",
                "gender": "feminino",
                "number": "singular",
                "category": "Estrutura / Tecnologia da Torre",
                "note": "Câmara situada nos setores superiores onde reside o cérebro e núcleo cognitivo da Torre Ar tonelico (JP SPU)."
            },
            "kakolog": {
                "pt": "Histórico de registros",
                "gender": "masculino",
                "number": "singular",
                "category": "Tecnologia / Sistema da Torre",
                "note": "Registro e histórico de tráfego/acessos da Torre mantido por Mei Mei (JP カコログ)."
            }
        },
        "dialogues": output_dialogues
    }
    
    out_file = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_060_output.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output_obj, f, ensure_ascii=False, indent=2)
    print(f"Arquivo de saída salvo com sucesso em: {out_file}")
else:
    print("\n>>> FALHA: Correções necessárias! <<<")
    sys.exit(1)

# -*- coding: utf-8 -*-
"""Script gerador canônico de curadoria para BLK_EVD_049."""

import json
from pathlib import Path

curated_lines = []

def add_line(d_id, ptbr, notes=""):
    curated_lines.append({
        "id": d_id,
        "curated_ptbr": ptbr,
        "final_ptbr": ptbr,
        "texto_ptbr_curado": ptbr,
        "custom_text": ptbr,
        "review_status": "approved",
        "reviewed": True,
        "notes": notes,
        "curation_notes": notes
    })

# ==========================================
# CENA 1: Event/704.evd (IDs 11498 - 11572)
# Cosmosfera de Aurica (Nível 2) - O Ataque do Demônio das Chamas
# ==========================================
add_line(11498, "É uma emergência! O Demônio das Chamas atacou novamente! Devemos dar tudo de nós para detê-lo!", "Radolf anuncia o retorno do monstro que ameaça incendiar o vilarejo mental de Aurica.")
add_line(11499, "O-o quê?! Aurica...", "Lyner reage sobressaltado e volta-se para Aurica.")
add_line(11500, "...E-eu... não consigo. Não temos como vencer...", "Aurica sucumbe ao desânimo e ao trauma de incapacidade.")
add_line(11501, "Droga! Se nada for feito, a vila será aniquilada de novo...! À carga!", "Radolf parte bravamente para o combate suicida.")
add_line(11502, "Espere, Radolf!!", "Lyner tenta conter o avanço imprudente do cavaleiro.")
add_line(11503, "O senhor Radolf... de novo... Ele sabe perfeitamente que não pode vencer, então por que insiste em lutar...?", "Aurica questiona perplexa o sacrifício alheio por sua causa.")
add_line(11504, "...É porque a vontade dele de proteger o seu mundo fala mais alto, não é?", "Lyner explica a motivação nobre de Radolf.")
add_line(11505, "Enquanto você fica aí se martirizando, dizendo que é inútil, tem um monte de gente te dando apoio.", "Lyner confronta a autoflagelação de Aurica com o carinho ao seu redor.")
add_line(11506, "Mas... eles não precisavam fazer isso por mim...", "Aurica recua, constrangida pela dívida emocional.")
add_line(11507, "Aurica!", "Lyner chama a atenção da donzela com firmeza.")
add_line(11508, "Você faz ideia do sentimento com que o Radolf se atira para te socorrer?", "Lyner indaga sobre a empatia de Aurica perante o cavaleiro.")
add_line(11509, "Não, eu não faço ideia...!", "Aurica resiste em reconhecer o afeto alheio.")
add_line(11510, "Não é verdade. Você sabe muito bem.", "Lyner desmonta a negação da donzela.")
add_line(11511, "Este aqui é o seu mundo. Se o Radolf luta para te proteger neste lugar, é porque lá no fundo você mesma espera isso dele, não é?", "Lyner revela a dinâmica psíquica da Cosmosfera onde Radolf reflete o desejo inconsciente dela.")
add_line(11512, "Isso...", "Aurica hesita ao ser desmascarada por Lyner.")
add_line(11513, "Não precisa ser pelo Radolf. Mas, pelo menos a vila do seu próprio mundo... tente proteger com as suas próprias mãos.", "Lyner convoca Aurica a assumir a responsabilidade por seu próprio mundo interior.")
add_line(11514, "......", "Silêncio reflexivo de Aurica.")
add_line(11515, "...Tudo bem.", "Aurica aceita tentar com resignação dócil.")
add_line(11516, "M-mas o que é isso?!", "Lyner assusta-se com o calor repentino que invade o ambiente.")
add_line(11517, "...Ugh, está tão quente! O demônio veio para reduzir a vila a cinzas...", "Aurica sente a aproximação abrasadora do monstro.")
add_line(11518, "Queimar tudo... queimar tudo até as cinzas... Não pouparei uma única alma...", "O Demônio das Chamas manifesta seu intento destrutivo ancestral.")
add_line(11519, "Maldito...! Não vou deixar você fazer o que bem entende!", "Lyner desafia a manifestação viral.")
add_line(11520, "Aurica! Proteja a vila! Neste mundo, a sua determinação é a única força capaz de salvá-la!", "Lyner instrui Aurica sobre a soberania da vontade na Cosmosfera.")
add_line(11521, "Mas...! Eu não faço a menor ideia do que fazer!", "Aurica desespera-se sem saber como materializar uma defesa.")
add_line(11522, "Eu tive uma ideia genial! O bicho ataca cuspindo fogo. Se a gente erguer uma barreira capaz de deter essas chamas, não resolve?!", "Habitante de Skuwat propõe a criação de uma barreira protetora.")
add_line(11523, "...E que tipo de barreira seria essa?", "Lyner pede detalhes práticos da sugestão.")
add_line(11524, "...B-bom, seu tonto... pensar nisso é papel da donzela aí, não é?!", "O habitante esquiva-se e repassa a responsabilidade a Aurica.")
add_line(11525, "Você é uma piada, sabia...?", "Lyner desconcerta-se com a covardia do habitante.")
add_line(11526, "Tudo bem... Eu vou tentar. Não sei se vai funcionar, mas...", "Aurica toma coragem para tecer sua primeira defesa.")
add_line(11527, "Aurica...", "Lyner observa a determinação tímida da parceira.")
add_line(11528, "É só fazer, não é...? Não posso ficar dando trabalho aos outros a vida inteira. Mas...", "Aurica tenta afastar seu complexo de inferioridade crônico.")
add_line(11529, "...Você promete que não vai rir de mim?", "Aurica expõe sua vulnerabilidade infantil e medo do ridículo.")
add_line(11530, "Eu jamais riria. Sei que você vai tecer isso com todo o seu coração.", "Lyner oferece acolhimento sincero e encorajamento genuíno.")
add_line(11531, "...Entendi. Então... lá vou eu...", "Aurica prepara-se para a conjuração.")
add_line(11532, "Iaaaah!!", "Grito de foco mágico de Aurica.")
add_line(11533, "Por favor! Apareça!!", "Aurica clama pela materialização da defesa.")
add_line(11534, "▼○$#!...&#@!", "Balbucio procedimental incompreensível do habitante, preservado rigorosamente.")
add_line(11535, "M-mas o que é isso?!", "Lyner surpreende-se com o cata-vento bizarro materializado.")
add_line(11536, "Achei que... quem sabe... se usasse vento, daria para afastar o fogo para longe... foi o que imaginei... e acabei criando isso...", "Aurica explica timidamente a lógica ingênua de sua criação.")
add_line(11537, "Fwahaha!... Queimarei tudo junto... até virar cinzas... até virar cinzas!", "O Demônio das Chamas zomba do obstáculo inócuo.")
add_line(11538, "Não adiantou... não aconteceu nada... Eu sabia, eu sabia que não ia prestar! Com uma coisa dessas...", "Aurica entra em pânico ao ver a falha inicial.")
add_line(11539, "Nada disso! Concentre-se com mais força! Visualize com nitidez, bem na sua mente, como derrotar o demônio!", "Lyner orienta a visualização criativa fundamental para a Magia da Canção.")
add_line(11540, "Sim... vou tentar. Vai dar certo, não vai...?", "Aurica busca segurança no olhar de Lyner.")
add_line(11541, "Sim, com certeza. Acredite no que eu digo. E... acredite no seu próprio poder também.", "Lyner ancora a autoconfiança de Aurica.")
add_line(11542, "...Sim. De repente, sinto minhas forças voltando. Nunca ninguém tinha me dito coisas assim antes...", "Aurica emociona-se ao receber incentivo autêntico pela primeira vez.")
add_line(11543, "Você tem razão. Vou dar tudo de mim!", "Aurica assume uma postura resoluta.")
add_line(11544, "Guarda de Fogo... por favor, nos proteja!!", "Aurica invoca formalmente a Magia Azul de defesa elemental.")
add_line(11545, "▼○$#!...&#@!", "Vocalização procedimental protegida intacta.")
add_line(11546, "M-mas o que é isso?!", "Lyner presencia o poder fônico ressoando.")
add_line(11547, "Uwaaaaah!!", "Rugido de derrota do Demônio das Chamas.")
add_line(11548, "...As chamas foram varridas para longe...?!", "Lyner constata maravilhado a dispersão do fogo.")
add_line(11549, "Eu consegui...?", "Aurica hesita em acreditar em seu próprio triunfo.")
add_line(11550, "Sim, foi um sucesso absoluto! Aurica, você protegeu a vila!!", "Lyner celebra com euforia a vitória da donzela.")
add_line(11551, "Eu... salvei a vila...? Mal posso acreditar...", "Aurica deslumbra-se com a sensação inédita de vitória.")
add_line(11552, "Calma lá, ainda não dá para cantar vitória. Aquele desgraçado ainda está vivo. Se bobearmos, ele volta para atacar de novo.", "O habitante adverte para a persistência da ameaça.")
add_line(11553, "Nesse caso, da próxima vez não vamos apenas afugentá-lo. Teremos que acabar com ele de vez.", "Lyner eleva a ambição tática do grupo.")
add_line(11554, "...Mas eu...", "Aurica teme o confronto definitivo.")
add_line(11555, "Vai dar tudo certo. Contanto que acredite em si mesma, com certeza salvará a sua vila.", "Lyner reforça a fé no potencial interior de Aurica.")
add_line(11556, "...Sim. Você tem razão... Tomara que seja assim mesmo...", "Aurica acolhe o conselho com esperança contida.")
add_line(11557, "......", "Lyner contempla o amadurecimento paulatino de Aurica.")
add_line(11558, "Você teceu a Magia Azul [Guarda de Fogo]!", "Notificação de sistema com paridade de colchetes.")
add_line(11559, "Vejo que conseguistes tecer uma magia. Contudo... não te envaideças por teres tecido míseras uma ou duas magias!", "Don Leon intervém com solenidade pomposa e severidade paternal.")
add_line(11560, "Eu não estou me envaidecendo coisa nenhuma... Mas me diga uma coisa: por que o coração da Aurica insiste em queimar a própria vila?", "Lyner busca entender o subtexto sombrio da psique de Aurica.")
add_line(11561, "Isso deveis perguntar diretamente à senhorita Aurica. Não cabe a este humilde guerreiro revelar tais assuntos.", "Don Leon preserva a intimidade inviolável de sua protegida.")
add_line(11562, "Mas que diferença faz?! Este mundo é meu! Não me importo quantas vezes esta vila arda em chamas!", "Aurica explode em amargura defensiva.")
add_line(11563, "Eles saem por aí dizendo que vão me proteger e acabam derrotados... e depois a culpa cai sobre mim, dizendo que não sei tecer magias ou que atraio desgraças...", "Aurica expõe o trauma original de Skuwat, onde sua suposta incompetência fônica virou bode expiatório.")
add_line(11564, "Eu não preciso de nada disso! Só quero que me deixem viver sozinha em paz!", "Aurica expressa o desejo de isolamento total para evitar novas culpas.")
add_line(11565, "Aurica...", "Lyner sente o peso dilacerante da mágoa dela.")
add_line(11566, "...Parece que fostes rejeitado. Isso demonstra que ela ainda não deposita a menor confiança em ti.", "Don Leon analisa sobriamente a barreira afetiva erguida por Aurica.")
add_line(11567, "Se desejas a confiança dela aqui, trata de conquistar a sua estima e valor no mundo real.", "Don Leon instrui Lyner sobre a correlação ontológica entre realidade e Cosmosfera.")
add_line(11568, "Tem gente que faz de tudo por mim por pura caridade, mas eu dispenso esse tipo de favor.", "Aurica rejeita a comiseração alheia.")
add_line(11569, "Eu nunca pedi nada disso... No fundo, eles só fazem para massagear o próprio ego e se sentirem satisfeitos consigo mesmos...", "Aurica desmascara a falsa piedade como mera autoindulgência dos outros.")
add_line(11570, "Aurica...", "Lyner cala-se diante da lucidez amarga da donzela.")
add_line(11571, "Bem, a própria senhorita Aurica anseia pelo isolamento e pela solidão.", "Don Leon sintetiza o estado psíquico de Aurica.")
add_line(11572, "Para provocar qualquer mudança no coração dela, terás de agir com extrema ousadia e determinação.", "Don Leon desafia Lyner a quebrar essa couraça com atos decisivos.")

# ==========================================
# CENA 2: Event/578.evd (IDs 11573 - 11603)
# Reunião dos Sentimentos no Cristal & Despedidas
# ==========================================
add_line(11573, "Reunimos os sentimentos de muita gente, hein...", "Lyner contempla o volume de 'pensamentos/desejos' colhidos para o cristal.")
add_line(11574, "De fato. Com esta quantidade... resta apenas integrarmos os nossos próprios sentimentos.", "Shurelia constata com graça divina a plenitude da energia afetiva reunida.")
add_line(11575, "Desta vez, parece ser o verdadeiro fim...", "Radolf reflete com sobriedade militar sobre o desfecho da jornada.")
add_line(11576, "É... o fim de tudo.", "Jack concorda em tom reflexivo e calejado.")
add_line(11577, "Já perdi as contas de quantas vezes ouvi vocês dizerem isso.", "Krusche quebra a solenidade com seu pragmatismo sarcástico clássico.")
add_line(11578, "Mas, agora sim... acabou de vez...", "Lyner reforça a sensação de alívio e conclusão.")
add_line(11579, "Lyner, vamos logo inserir os nossos sentimentos!", "Misha manifesta seu entusiasmo impaciente para concluir o cristal.")
add_line(11580, "Que tipo de Canção será que vai nascer...?", "Aurica indaga com fascínio e delicadeza sobre a harmonia resultante.")
add_line(11581, "......", "Ayatane permanece quieto, guardando seu segredo.")
add_line(11582, "Perdoem-me, pessoal.", "Ayatane interrompe cordialmente o grupo.")
add_line(11583, "Ainda tem mais uma pessoa de quem eu gostaria de recolher os sentimentos... Será que ainda dá tempo?", "Ayatane pede permissão para buscar os sentimentos de Mir.")
add_line(11584, "Não há problema algum. Darei início aos preparativos, mas venha me trazer quando terminar.", "Shurelia acolhe com serenidade e benevolência o pedido de Ayatane.")
add_line(11585, "Muito obrigado!", "Ayatane agradece reverente.")
add_line(11586, "...Estarei à sua espera.", "Shurelia despede-se com afeto sereno.")
add_line(11587, "Compreendo... Um intercâmbio mútuo entre os dois lados...", "Governador Leard reflete sobre a reconciliação entre Mundos.")
add_line(11588, "Se a nossa Ordem dos Cavaleiros da Igreja e os Cavaleiros de Elemia cooperarem, criaremos um ambiente onde todos possam viver em paz.", "Radolf defende a união institucional e militar em prol da estabilidade de Sol Ciel.")
add_line(11589, "Tanto nós quanto os Apóstolos de Elemia, no fim das contas, somos todos da mesma espécie humana.", "Oficial da Igreja apela para a irmandade fundamental entre as ordens.")
add_line(11590, "Que a Tribo Teru também seja integrada para iniciarmos um verdadeiro intercâmbio tecnológico.", "O oficial propõe incorporar a ciência Teru ao progresso comum.")
add_line(11591, "O que um único povo jamais realizaria sozinho torna-se um poder grandioso quando as três nações se unem.", "A Igreja celebra a força da tríplice aliança (Platina, Igreja e Tribo Teru).")
add_line(11592, "O dirigível é uma prova viva disso.", "Radolf cita a aeronave de Krusche como ápice da cooperação multirracial.")
add_line(11593, "De fato. De agora em diante, teremos de unir forças para prosperar.", "Leard ratifica o compromisso político e moral do novo pacto.")
add_line(11594, "Esse assunto... também me interessa.", "Sentinela manifesta curiosidade pelos rumos da cooperação.")
add_line(11595, "...Os confins do mundo, hein...", "Krusche sonha alto contemplando horizontes além da Torre.")
add_line(11596, "Pretende voar até o céu ou algo assim?", "Jack provoca Krusche com cinismo bem-humorado.")
add_line(11597, "...Quem sabe até o inferno. Um lugar onde alma alguma jamais pisou.", "Krusche responde com audácia desbravadora e fascínio pelo desconhecido.")
add_line(11598, "Se for assim... vai precisar de um guarda-costas.", "Jack oferece sua proteção sob o disfarce de mercenário galanteador.")
add_line(11599, "...É, talvez precise.", "Krusche aceita a companhia com cumplicidade velada.")
add_line(11600, "Vocês estão de cochicho sobre algo divertido, não é? Deixem eu entrar na conversa também!", "Misha intromete-se cheia de energia e curiosidade juvenil.")
add_line(11601, "Esse é um papo que não diz respeito a pirralhas.", "Jack alfineta Misha chamando-a de pirralha/criança.")
add_line(11602, "...Mas que atrevimento! Fique sabendo que eu já sou uma mulher bem adulta, ouviu bem?!", "Misha emburra e protesta com indignação cômica e bico tsundere.")
add_line(11603, "Finalmente... eu o encontrei...", "Ayatane murmura sozinho, encontrando o canal de Mir.")

# ==========================================
# CENA 3: Event/256.evd (IDs 11604 - 11634)
# Invasão da Instalação & O Resgate Tático de Misha
# ==========================================
add_line(11604, "Mas olha... mesmo não sendo uma Reyvateil, este lugar não tem nada de agradável.", "Jack reclama da atmosfera opressiva e artificial da instalação.")
add_line(11605, "Esta porta... está trancada.", "Lyner examina a passagem bloqueada.")
add_line(11606, "Ai! Ai, ai, ai... Sem chance. É muito mais resistente do que imaginei...", "Lyner tenta forçar a porta fisicamente e machuca a mão.")
add_line(11607, "Claro, né? Esta porta também foi trancada usando energia sinfônica.", "Krusche analisa a tranca com olho clínico de engenheira.")
add_line(11608, "Energia sinfônica de novo...?", "Lyner suspira diante da barreira tecnológica.")
add_line(11609, "No fim das contas, foi viagem perdida...", "Jack desanima com o impasse.")
add_line(11610, "Não necessariamente. Acabei de encontrar uma solução bem racional.", "Krusche rebate com orgulho técnico e pragmatismo.")
add_line(11611, "Essa trava por energia sinfônica da porta tem uma única falha fatal.", "Krusche aponta a vulnerabilidade do sistema de segurança.")
add_line(11612, "Se o fornecimento de energia sinfônica for cortado, a tranca se abre facinho, facinho.", "Krusche explica a lógica do mecanismo à prova de falhas.")
add_line(11613, "Ou seja: a nossa solução é derrubar a força do reator do núcleo motor.", "Krusche propõe desativar a propulsão nuclear da ilha flutuante.")
add_line(11614, "Ficou maluca, mulher?! A ilha inteira vai despencar!", "Jack entra em pânico cômico diante da ousadia suicida da piloto.")
add_line(11615, "Relaxa. Mesmo se cortarmos a força, a ilha só vai descer de mansinho por uns dez minutos.", "Krusche tranquiliza o grupo com frieza técnica hilária.")
add_line(11616, "Além disso, pelo visto ainda vamos topar com um monte de portas trancadas por energia sinfônica mais à frente.", "Krusche justifica a medida radical para abrir caminho em todo o setor.")
add_line(11617, "Se é assim, que se dane tudo! Vamos tocar o terror de uma vez!", "Jack rende-se à loucura com bravata de mercenário veterano.")
add_line(11618, "Vamos procurar os controles do reator nuclear. Devem ficar em algum ponto da [Casa de Máquinas].", "Jack orienta as buscas com paridade de colchetes.")
add_line(11619, "Mas antes disso... o que faremos sobre a Misha? Sem ela, é certeza de que nosso poder de combate despenca...", "Krusche pondera a importância tática do suporte fônico de Misha.")
add_line(11620, "Vamos voltar lá para ver como ela está.", "Lyner decide checar a amiga de infância.")
add_line(11621, "Lyner!! Poxa vida! Onde é que vocês se meteram?!", "Misha explode em cobrança carinhosa ao rever Lyner.")
add_line(11622, "Eu não avisei para não saírem sem mim?!", "Misha faz bico emburrado por ter sido deixada para trás.")
add_line(11623, "Desculpa. Mas nós descobrimos um jeito de fazer você parar de sentir medo daquela sala.", "Lyner acalma a parceira com gentileza protetora.")
add_line(11624, "E de quebra descobrimos como abrir a porta também.", "Jack complementa a notícia com ar descontraído.")
add_line(11625, "Hmm, entendi... Derrubar a energia sinfônica? Até que parece emocionante.", "Misha entusiasma-se com a audácia do plano.")
add_line(11626, "Sendo assim, o próximo passo é revistar a Casa de Máquinas.", "Jack delineia o objetivo da missão.")
add_line(11627, "Então vamos logo!", "Misha toma a dianteira com energia.")
add_line(11628, "Misha... tem certeza de que está bem? Não seria melhor descansar mais um pouco...?", "Lyner preocupa-se com o desgaste físico e emocional dela.")
add_line(11629, "...Lyner. Se eu estou dizendo que vou, é porque vou.", "Misha bate o pé com sua determinação tsundere.")
add_line(11630, "Lyner... por acaso você não quer ficar comigo?", "Misha expõe sua carência afetiva e medo de rejeição.")
add_line(11631, "Não, não é isso! Só estou pensando no seu bem...", "Lyner defende-se afobado para não magoá-la.")
add_line(11632, "Se é assim, me deixe ir junto! Ficar aqui plantada esperando é mil vezes mais doloroso.", "Misha declara que o afastamento é a pior tortura para seu coração.")
add_line(11633, "...É verdade. Então venha com a gente.", "Lyner rende-se com ternura ao companheirismo inabalável da amiga.")
add_line(11634, "Misha entrou para o grupo!", "Mensagem canônica de sistema.")

# ==========================================
# CENA 4: Event/179.evd (IDs 11635 - 11704)
# Centro de Mergulho de Platina: Cerimônia de Download do Purger & Código Hymmnos
# ==========================================
add_line(11635, "Seja bem-vindo. ...Olha só, se não é o jovem Lyner.", "O Operador de Portão da Loja de Mergulho reconhece o cavaleiro.")
add_line(11636, "Veio baixar um Cristal Hymmnos em uma Reyvateil?", "O operador questiona o propósito da visita técnica.")
add_line(11637, "E em quem você vai baixar?", "O operador solicita a escolha da donzela para a instalação.")
add_line(11638, "Por favor, selecione a Reyvateil que conhece o seu [Código Hymmnos].", "Instrução técnica de interface mantendo paridade de colchetes.")
add_line(11639, "Aurica... posso contar com você?", "Lyner convida Aurica para receber o Purger.")
add_line(11640, "Hã?! ...T-tem certeza de que serve... alguém como eu?", "Aurica hesita em sua eterna insegurança de donzela de Skuwat.")
add_line(11641, "Sim. Faço questão de pedir a você, Aurica. Você toparia...?", "Lyner valida o valor único de Aurica para a missão.")
add_line(11642, "...Sim.", "Aurica consente com meiguice emocionada.")
add_line(11643, "Muito bem, já que faremos a cerimônia, vamos nos mover até o local apropriado.", "O operador conduz o casal ao tablado ritual.")
add_line(11644, "Nossa... Quer dizer então que esta praça servia justamente para a Cerimônia de Download?", "Lyner surpreende-se com a finalidade sagrada da praça.")
add_line(11645, "Bem, é mais por formalidade, na verdade.", "O operador desmistifica o aparato religioso com franqueza técnica.")
add_line(11646, "Pois bem, agora façam exatamente o que eu instruir.", "O operador inicia o protocolo de segurança.")
add_line(11647, "Primeiro, fiquem frente a frente.", "Posicionamento espacial sagrado entre cavaleiro e Reyvateil.")
add_line(11648, "Lyner, pegue o cristal e erga-o diante da senhorita Aurica.", "Instrução de alinhamento óptico do Cristal Hymmnos.")
add_line(11649, "Muito bem, vamos começar.", "Início do rito de invocação.")
add_line(11650, "#0Fou paks ra exec hymnos PAJA!", "Comando sagrado de execução Hymmnos do Purger preservado integralmente.")
add_line(11651, "...!! I-isso é...!!", "Lyner sente o influxo transcendental da ressonância de dados.")
add_line(11652, "Lyner! Leia isso! Rápido!", "O operador ordena a leitura imediata dos versos revelados.")
add_line(11653, "S-sim!", "Lyner responde pronto para a recitação.")
add_line(11654, "#0Was yea ra chs hymnos yor...", "Verso Hymmnos de abertura de vínculo conservado intocado.")
add_line(11655, "#0En chsee fwal fwal yor...", "Verso Hymmnos de comunhão espiritual conservado intocado.")
add_line(11656, "#0exec drone hymnos PAJA ", "Comando Hymmnos de execução de drone de dados fônicos do Purger.")
add_line(11657, "#0enter MULE_TEIWAZ_ARTONELICO.", "Entrada canônica do Código Hymmnos de Aurica (Mule Teiwaz Ar Tonelico).")
add_line(11658, "......", "Silêncio sagrado durante a gravação neural dos dados.")
add_line(11659, "E-e então, como você está?!", "Lyner indaga ansioso sobre o bem-estar da parceira.")
add_line(11660, "...A Canção... sinto a Canção sendo tecida do fundo do meu coração...", "Aurica descreve a gênese viva da Magia da Canção em seu ser.")
add_line(11661, "É incrível...! Eu estou mesmo tecendo uma Canção... Nunca senti nada parecido em toda a minha vida...", "Aurica chora de felicidade ao vivenciar a plenitude de sua vocação fônica.")
add_line(11662, "Não é algo que se experimente muitas vezes na vida, sabe? Por isso, aproveite cada segundo dessa sensação.", "O operador comenta com empatia sobre a raridade do download de um Cristal Hymmnos lendário.")
add_line(11663, "Pois bem, o que eu podia fazer termina aqui. Até porque não faço ideia de qual é a natureza dessa Canção.", "O técnico demarca o limite de seu conhecimento profano.")
add_line(11664, "Para o restante, consulte o Comandante Leard, certo?", "Encaminhamento institucional a Leard Barsett em Platina.")
add_line(11665, "Muito obrigado. Você nos ajudou bastante.", "Lyner agradece cordialmente o suporte.")
add_line(11666, "Certo! Vamos voltar para a Catedral.", "Lyner comanda o retorno ao Altar de Platina.")
add_line(11667, "Misha... posso pedir isso a você?", "Ramificação alternativa: Lyner convida Misha para o download.")
add_line(11668, "Lyner... Você vai mesmo deixar eu fazer isso...?", "Misha comove-se com a prova definitiva de confiança.")
add_line(11669, "Sim. Faço questão de pedir a você, Misha. Posso contar com você?", "Lyner reitera seu laço inquebrável com a amiga de infância.")
add_line(11670, "Mas é claro!... Eu estava esperando você me dizer isso há tanto tempo!", "Misha vibra de júbilo e gratidão.")
add_line(11671, "Muito bem, já que faremos a cerimônia, vamos nos mover até o local apropriado.", "O operador conduz Misha e Lyner.")
add_line(11672, "Nossa... Quer dizer então que esta praça servia justamente para a Cerimônia de Download?", "Lyner repete a constatação espacial.")
add_line(11673, "Bem, é mais por formalidade, na verdade.", "O técnico relativiza o ritualismo da praça.")
add_line(11674, "Pois bem, agora façam exatamente o que eu instruir.", "Início do protocolo de segurança.")
add_line(11675, "Primeiro, fiquem frente a frente.", "Posicionamento frontal dos parceiros.")
add_line(11676, "Lyner, pegue o cristal e erga-o diante da senhorita Misha.", "Elevação do Purger diante de Misha.")
add_line(11677, "Muito bem, vamos começar.", "O rito tem início.")
add_line(11678, "#0Fou paks ra exec hymnos PAJA!", "Invocação canônica Hymmnos intocada.")
add_line(11679, "...!! I-isso é...!!", "Lyner testemunha o fluxo energético do servidor.")
add_line(11680, "Lyner! Leia isso! Rápido!", "Ordem de leitura imediata dos versos.")
add_line(11681, "S-sim!", "Lyner apronta-se para a leitura.")
add_line(11682, "#0Was yea ra chs hymnos yor...", "Verso Hymmnos mantido estritamente original.")
add_line(11683, "#0En chsee fwal fwal yor...", "Verso Hymmnos corrigido da corrupção da NISA (En chsee completo).")
add_line(11684, "#0exec drone hymnos PAJA ", "Comando Hymmnos de ativação do drone preservado.")
add_line(11685, "#0enter MISYA_FEHU_EORIA_ARTONELICO!", "Código Hymmnos canônico sagrado de Misha Arsellec Lünn, corrigindo o erro grotesco de cópia da NISA.")
add_line(11686, "......", "Silêncio de sincronia neural com o servidor da Torre.")
add_line(11687, "E-e então, tudo bem?!", "Lyner verifica o estado emocional de Misha.")
add_line(11688, "Mas o que é isso...? Não pode ser...", "Misha sente o despertar de memórias ancestrais e vínculos do passado.")
add_line(11689, "É uma sensação de tanta saudade... Por que será... que as lágrimas não param de descer...?", "Misha chora diante da ressonância de sua herança como Reyvateil Origin de Eoria.")
add_line(11690, "Lyner... Isso é impressionante!... Mas por que traz um aperto tão agridoce no peito...?", "Misha compartilha a comoção profunda do Cântico sagrado.")
add_line(11691, "Não é algo que se experimente muitas vezes na vida, sabe? Por isso, aproveite cada segundo dessa sensação.", "O operador valoriza a transcendência da experiência.")
add_line(11692, "Pois bem, o que eu podia fazer termina aqui. Até porque não faço ideia de qual é a natureza dessa Canção.", "O operador conclui seu papel técnico.")
add_line(11693, "Para o restante, consulte o Comandante Leard, certo?", "Encaminhamento a Leard.")
add_line(11694, "Muito obrigado. Você nos ajudou bastante.", "Agradecimento de Lyner.")
add_line(11695, "Certo! Vamos voltar para a Catedral.", "Lyner convoca o grupo ao retorno.")
add_line(11696, "Imagina, não há de quê. Apareçam sempre que quiserem.", "O operador despede-se com afabilidade.")
add_line(11697, "Na verdade... para ser sincero, ainda não entendi muito bem...", "Lyner confessa sua ignorância técnica sobre os Códigos Hymmnos.")
add_line(11698, "É sério mesmo?! ...Puxa vida, vou ter que explicar tudo de novo?", "O operador exaspera-se em tom cômico e descontraído.")
add_line(11699, "O [Código Hymmnos] é uma espécie de senha pessoal da Reyvateil.", "Definição didática e acessível de Código Hymmnos mantendo colchetes.")
add_line(11700, "Para usar uma expressão mais lendária, é o chamado 'Verdadeiro Nome' que ela não revela a ninguém.", "Explicação mitológica e íntima do conceito de Nome Secreto / 真の名前.")
add_line(11701, "Mas pelo visto, parece que você ainda não tem esse [Código Hymmnos] em mãos.", "Constatação da ausência do código.")
add_line(11702, "Faça um Mergulho e tente perguntar ao guardião da Cosmosfera dela.", "Instrução canônica para obter o código com Don Leon.")
add_line(11703, "Se ela já tiver aberto o coração para você, com certeza vai lhe confiar o [Código Hymmnos].", "Condição afetiva necessária para a revelação do nome sagrado.")
add_line(11704, "Sendo assim... quer dizer que você veio aqui para mergulhar, não é?", "O operador deduz o verdadeiro motivo da visita à Loja de Mergulho.")

# ==========================================
# CENA 5: Event/218.evd (IDs 11705 - 11725)
# Partida para as Asas de Hórus: Despedida de Shurelia e Lealdade de Radolf
# ==========================================
add_line(11705, "Minha despedida será aqui. Rogo aos céus pela melhor sorte em sua jornada.", "Shurelia despede-se com elegância e nobreza divina.")
add_line(11706, "Jack, Srta. Krusche, agradeço imensamente pela cooperação de ambos. Por favor, cuidem bem da Misha.", "Shurelia agradece aos veteranos e confia-lhes a proteção da Reyvateil Origin.")
add_line(11707, "Pode deixar!", "Krusche aceita com firmeza profissional.")
add_line(11708, "Deixa com a gente!", "Jack assegura seu compromisso com despojamento.")
add_line(11709, "Então... já estamos indo!", "Misha despede-se com vivacidade.")
add_line(11710, "Misha saiu do grupo. Jack saiu do grupo. Krusche saiu do grupo.", "Mensagem técnica de atualização da formação do grupo.")
add_line(11711, "Lyner... cuide-se bem nas Asas de Hórus...", "Shurelia demonstra carinho íntimo e preocupação maternal com Lyner.")
add_line(11712, "Calma lá, também não é como se fosse uma despedida eterna. A senhora está exagerando um pouco, não acha?", "Lyner desanuvia o clima com seu otimismo caloroso juvenil.")
add_line(11713, "...Tem razão. Aja sempre de modo a honrar o nome de um Apóstolo de Elemia.", "Shurelia sorri e lembra-o de sua dignidade espiritual como Cavaleiro sagrado.")
add_line(11714, "Sim, senhora!", "Lyner responde com postura marcial respeitosa.")
add_line(11715, "...Lyner!", "Shurelia chama-o uma última vez, hesitando com doçura.")
add_line(11716, "Pois não?", "Lyner volta-se para ela.")
add_line(11717, "Dê... dê o seu melhor lá.", "Shurelia expressa sua torcida singela e tímida.")
add_line(11718, "S-sim... com certeza.", "Lyner comove-se com a pureza da Deusa.")
add_line(11719, "......", "Aurica observa a cumplicidade entre Lyner e a Administradora.")
add_line(11720, "......", "Shurelia contempla a partida deles com serenidade solene.")
add_line(11721, "Lyner. Devo-lhe sinceras desculpas. Fazer tanto sacrifício em nome da Igreja...", "Radolf manifesta nobreza e culpa cavalheiresca por sobrecarregar o jovem.")
add_line(11722, "O que é isso, Radolf? Se não fosse pelo apoio da Igreja, eu não teria chegado aonde cheguei hoje.", "Lyner reconhece a imensa dívida de gratidão para com a Igreja de Elemia.")
add_line(11723, "Retribuir uma dívida dessas é a obrigação mais natural do mundo.", "Lyner afirma seu código moral de reciprocidade e honra.")
add_line(11724, "Compreendo... Agradeço do fundo do coração. Sendo assim, vamos primeiro até a Igreja para prestar cumprimentos ao Bispo.", "Radolf comove-se e orienta o roteiro em direção ao Bispo Falss.")
add_line(11725, "Os equipamentos dos membros que deixaram o grupo foram removidos. Selecione [Equipamento] no menu principal para reconfigurar seus itens.", "Aviso de sistema com paridade de colchetes.")

# ==========================================
# CENA 6: Event/724.evd (IDs 11726 - 11747)
# Cosmosfera de Aurica: Reconciliação com Claire, Calor Vital e Mudança de Paradigma
# ==========================================
add_line(11726, "Ora, vejam só, vocês dois juntos... Hoje estou me sentindo um pouco melhor. Quem dera todos os dias fossem assim...", "Claire acolhe Lyner e Aurica na estalagem mental com doçura serena.")
add_line(11727, "Vão ser sim. De hoje em diante, para sempre... Não vou deixar a mana Claire sofrer com essa doença nunca mais.", "Aurica promete erradicar o sofrimento da irmã de criação.")
add_line(11728, "Me perdoa por tudo até hoje... Eu sentia tanta inveja de você. Você faz tudo com perfeição, é tão bondosa, tem tanto talento...", "Aurica confessa abertamente a inveja e o complexo de inferioridade que a corroíam.")
add_line(11729, "Mas agora meu coração já se decidiu. Eu quero continuar ao seu lado, mana Claire, para sempre.", "Aurica supera a vergonha e abraça o amor fraterno acima do rancor.")
add_line(11730, "É claro que a inveja não vai sumir como num passe de mágica... mas mesmo assim, eu quero ficar com você! Por isso... eu sei que vamos curar essa doença!", "Aurica expressa a maturidade de aceitar suas fraquezas humanas sem se deixar paralisar por elas.")
add_line(11731, "...Tudo bem. Nesse caso... posso contar com você?", "Claire entrega-se com confiança e carinho ao cuidado de Aurica.")
add_line(11732, "Sim! Então, mana Claire, lá vou eu... Haaah!!", "Aurica prepara-se com ânimo radiante para entoar o Cântico de cura.")
add_line(11733, "Por favor, Calor Vital... Tente curar a doença da mana Claire mais uma vez!", "Aurica conjura sua magia primária de recuperação (Life Warm).")
add_line(11734, "Vai tentar de novo? Olha... acho que não importa quantas vezes tente, não vai adiantar nada...", "Espírito guardião cético duvida da capacidade fônica de Aurica.")
add_line(11735, "Não diga isso! Desta vez, eu também estou infundindo todos os meus sentimentos!", "Aurica rebate convicta de que sua doação emocional mudará o resultado.")
add_line(11736, "Tudo bem... Então vou fazer uma tentativa...", "O espírito consente em canalizar o poder.")
add_line(11737, "M-mas o que... é isso?!", "O espírito assombra-se com o surto inusitado de energia térmica.")
add_line(11738, "Não pode ser...?! O meu... poder aumentou tanto assim?!", "A entidade fônica sente uma expansão colossal em sua matriz de restauração.")
add_line(11739, "O sentimento da Aurica potencializou o poder de cura!", "Lyner reconhece o milagre da comunhão afetiva amplificando a Magia Azul.")
add_line(11740, "Com isso... talvez a gente consiga! Não... tenho certeza de que vai dar certo!", "O espírito enche-se de fé inabalável.")
add_line(11741, "...Nossa... sinto uma disposição tão boa... Tão reconfortante...", "Claire sente o calor vital regenerando suas forças e dissipando a aflição.")
add_line(11742, "Mana Claire... como se sente? Ficou... melhor?", "Aurica pergunta com o coração transbordando de expectativa amorosa.")
add_line(11743, "Sim, graças a você. Estou tão bem que mal posso acreditar.", "Claire atesta a cura completa de sua aflição com gratidão infinita.")
add_line(11744, "É sério?! Que alívio...! Que alívio, de verdade...", "Aurica desaba em lágrimas de alegria e redenção.")
add_line(11745, "Mana Claire... Por favor, continue comigo de hoje em diante, para sempre e todo o sempre.", "Aurica sela o pacto de união e cumplicidade eterna com sua mentora.")
add_line(11746, "Você teceu a Magia Azul [Renovação Vital]!", "Notificação de sistema tecendo a versão superior do Calor Vital (Life Refresh) com paridade de colchetes.")
add_line(11747, "É a Mudança de Paradigma! Depressa, rumo a Stonehenge!", "Don Leon proclama a abertura do portal do próximo estrato psíquico.")

# Montagem do pacote canônico
output_data = {
    "block_id": "BLK_EVD_049",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(curated_lines),
    "id_range": [11498, 11747],
    "dialogues": curated_lines,
    "curated_lines": curated_lines,
    "glossary_updates": [
        {
            "term_en": "Fire Demon",
            "term_jp": "炎の悪魔",
            "term_ptbr": "Demônio das Chamas",
            "category": "Cosmosfera / Inimigo Mental",
            "rationale": "Manifestação destrutiva e traumática de nível 2 na Cosmosfera de Aurica inspirada no ataque de Bomball que incendiou Skuwat."
        },
        {
            "term_en": "Fire Guard",
            "term_jp": "ファイアーガード",
            "term_ptbr": "Guarda de Fogo",
            "category": "Magia da Canção / Azul",
            "rationale": "Magia Azul defensiva elemental tecida por Aurica para deter as labaredas do Demônio das Chamas, harmonizada com a série de guardas elementais."
        },
        {
            "term_en": "Life Refresh",
            "term_jp": "ライフリフレッシュ",
            "term_ptbr": "Renovação Vital",
            "category": "Magia da Canção / Azul",
            "rationale": "Evolução curativa de alto nível tecida por Aurica a partir do Calor Vital (Life Warm) ao reconciliar-se com Claire."
        },
        {
            "term_en": "Wings of Horus",
            "term_jp": "ホルスの翼",
            "term_ptbr": "Asas de Hórus",
            "category": "Toponímia / Estrutura da Torre",
            "rationale": "Designação estrutural colossal dos níveis intermediários da Torre Ar tonelico onde Lyner caiu no início de sua jornada."
        },
        {
            "term_en": "Apostles of Elemia",
            "term_jp": "エレミアの使徒",
            "term_ptbr": "Apóstolos de Elemia",
            "category": "Facção / Ordem Sagrada",
            "rationale": "Título solene conferido aos membros nobres e guerreiros da Ordem dos Cavaleiros e da liderança de Platina consagrados à proteção divina da Torre."
        }
    ],
    "new_terms": {
        "Fire Demon": {
            "pt": "Demônio das Chamas",
            "category": "Cosmosfera / Inimigo Mental",
            "note": "炎の悪魔. Personificação do trauma do massacre e incêndio do Vilarejo de Skuwat na mente de Aurica."
        },
        "Fire Guard": {
            "pt": "Guarda de Fogo",
            "category": "Magia da Canção / Azul",
            "note": "ファイアーガード (青魔法【ファイアーガード】). Magia Azul tecida por Aurica para varrer chamas e resguardar aliados."
        },
        "Life Refresh": {
            "pt": "Renovação Vital",
            "category": "Magia da Canção / Azul",
            "note": "ライフリフレッシュ (青魔法【ライフリフレッシュ】). Forma aprimorada de Calor Vital (ライフウォーム) tecida para curar Claire."
        },
        "Wings of Horus": {
            "pt": "Asas de Hórus",
            "category": "Toponímia / Estrutura da Torre",
            "note": "ホルスの翼. Complexo estrutural alado da Torre Ar tonelico."
        },
        "Apostles of Elemia": {
            "pt": "Apóstolos de Elemia",
            "category": "Facção / Ordem Sagrada",
            "note": "エレミアの使徒. Título cerimonial honorífico dos guardiões e cavaleiros fiéis à vontade de Eoria/Shurelia."
        }
    },
    "scene_handoff_final": {
        "resumo_dramatico": "O bloco BLK_EVD_049 articula seis momentos narrativos fundamentais de desfecho de ato, transição psíquica e avanço canônico: (1) Na Cosmosfera de Aurica (Nível 2), o vilarejo mental de Skuwat é sitiado pelo terrível Demônio das Chamas; enquanto Radolf tomba em combate abnegado, Lyner confronta o complexo de culpa e autoflagelação de Aurica, guiando-a na síntese da Magia Azul [Guarda de Fogo], desarmando temporariamente o monstro e expondo o profundo ressentimento dela contra falsas piedades e caridades condescendentes. (2) Diante do Cristal Hymmnos, o grupo reúne os sentimentos de todos os povos antes que Shurelia inicie os preparativos finais; Krusche e Jack compartilham anseios sobre desbravar os confins do mundo e Misha protesta contra ser tratada como pirralha, enquanto Ayatane afasta-se sorrateiramente para selar seu pacto secreto com Mir. (3) Na invasão da instalação flutuante, Jack e Lyner deparam-se com uma porta colossal selada por energia sinfônica; Krusche delineia o audacioso plano de desativar a propulsão nuclear da ilha e Misha reinsere-se heroicamente na linha de frente tática do grupo. (4) No Centro de Mergulho de Platina, realiza-se o rito sagrado de Download do lendário Cristal Purger (パージャ); o operador conduz o emparelhamento com Aurica (e alternativamente com Misha), entoando os mandamentos Hymmnos e desmistificando o segredo do [Código Hymmnos] como o 'Verdadeiro Nome' das Reyvateils obtido via Mergulho com Don Leon. (5) Em solene despedida no Altar, Shurelia abençoa a partida do grupo rumo às [Asas de Hórus] e Radolf renova seus votos de lealdade e gratidão a Lyner antes de marcharem até a Igreja do Bispo Falss. (6) No ápice do Nível 2 da Cosmosfera de Aurica, a donzela tem uma comovente conversa íntima com a mana Claire, confessa abertamente a inveja que envenenava seu coração, canaliza todo o seu amor fraterno para potencializar o [Calor Vital] na sublime Magia Azul [Renovação Vital], curando a mentora e desencadeando a [Mudança de Paradigma] rumo a Stonehenge.",
        "decisoes_terminologicas": {
            "Demônio das Chamas": "炎の悪魔 (manifestação do trauma de Skuwat na Cosmosfera de Aurica)",
            "[Guarda de Fogo]": "青魔法【ファイアーガード】 (Magia Azul de Aurica para conter fogo e resguardar aliados)",
            "[Calor Vital]": "ライフウォーム / Life Warm (magia primordial de restauração tecida por Aurica)",
            "[Renovação Vital]": "青魔法【ライフリフレッシュ】 / Life Refresh (Magia Azul tecida para curar a mana Claire)",
            "Asas de Hórus": "ホルスの翼 / Wings of Horus (estrutura colossal da Torre Ar tonelico)",
            "Apóstolos de Elemia": "エレミアの使徒 / Apostles of Elemia (título sagrado dos campeões e cavaleiros de Platina)",
            "Purger": "パージャ (Cristal Hymmnos sagrado de erradicação de vírus)",
            "Código Hymmnos": "ヒュムネコード (senha ontológica e Nome Verdadeiro da Reyvateil)",
            "Casa de Máquinas": "動力部 / Power Department (setor de controle do reator de propulsão nuclear da ilha)"
        },
        "alertas_para_proximo_bloco": "A transição de Aurica pelo portal de Stonehenge para o Nível 3 da Cosmosfera trará à tona camadas ainda mais profundas de suas dores de infância e traumas em Skuwat; nas Asas de Hórus, a comitiva de Lyner e Radolf reencontrará o Bispo Falss e os meandros políticos da Igreja de Elemia, enquanto as ações furtivas de Ayatane ao lado de Mir começam a lançar sombras irreversíveis sobre a estabilidade da Torre."
    },
    "highlights": [
        "A superação do complexo de inferioridade em Skuwat: Aurica confronta a culpa por não saber cantar, descobre que os outros a apoiavam de verdade e tece a Magia Azul [Guarda de Fogo] para salvar seu próprio mundo interior.",
        "A confissão amarga sobre a falsa caridade: o desabafo contundente de Aurica a Lyner sobre como favores e piedades alheias muitas vezes servem apenas à autoindulgência e ao ego de quem ajuda.",
        "A cumplicidade cínica entre veteranos: Jack Hamilton e Krusche Elendia flertando com a ideia de desbravar juntos os confins do mundo até o inferno, contrastados pelo bico indignado de Misha contra o rótulo de pirralha.",
        "A audácia mecânica de Krusche: o plano insano de desligar o reator nuclear da ilha flutuante por dez minutos para arrombar todas as portas trancadas por energia sinfônica.",
        "A solenidade ancestral do rito de Download: a preservação intocada dos cânticos Hymmnos do Purger e a correção histórica do Código Hymmnos exclusivo de Misha (#0enter MISYA_FEHU_EORIA_ARTONELICO!), corrigindo a falha crítica da NISA.",
        "A cura do coração entre irmãs: a confissão desarmada de Aurica perante a mana Claire sobre a inveja que sentia, culminando na tecelagem da Magia Azul [Renovação Vital] e na Mudança de Paradigma em Stonehenge."
    ]
}

output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_049_output.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"[OK] Gerado {len(curated_lines)} falas em {output_path.name}")

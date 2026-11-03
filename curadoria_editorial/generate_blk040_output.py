import json
import re

# Dicionário de diálogos curados para BLK_EVD_040 (IDs 9529 a 9712)
curated_data = {
    # SEÇÃO 1: Event/85.evd (9529 a 9584)
    9529: (
        "Olha lá...",
        "Espanto e atenção de Lyner ao avistar alguém correndo perigo próximo à usina."
    ),
    9530: (
        "Ei, o que aquele garoto está fazendo?!",
        "Correção do erro crasso de gênero da NISA ('she'); Misha se refere ao jovem que avista na instalação."
    ),
    9531: (
        "Será que não conseguiu fugir?!\nVamos lá!!",
        "Lyner preocupado com a segurança do rapaz encurralado, tomando a iniciativa do resgate."
    ),
    9532: (
        "Você está bem?!",
        "Abordagem direta e protetora de Lyner ao alcançar o jovem."
    ),
    9533: (
        "Quem são vocês...?",
        "Reação assustada e atônita do rapaz ao ser abordado."
    ),
    9534: (
        "Viemos te salvar!",
        "Misha tranquilizando o jovem com energia e prontidão."
    ),
    9535: (
        "Comigo está tudo bem!\nMas a gente precisa parar aquela máquina agora mesmo!",
        "Correção do decalque da NISA ('wing nut'); o jovem alerta sobre o robô/vírus descontrolado."
    ),
    9536: (
        "Se ele continuar enfurecido e arrebentar o núcleo de força,\nesta ilha vai despencar sem dúvida nenhuma!",
        "Correção do trocadilho grosseiro da NISA ('Nukular'); fidelidade ao termo 'núcleo de força/propulsão' (核動力部)."
    ),
    9537: (
        "...Uma ilha?!\nEla vai despencar?!",
        "Choque genuíno de Lyner, que cresceu em Platina e desconhece a engenharia das ilhas flutuantes do Mundo Inferior."
    ),
    9538: (
        "É verdade, você não faz ideia\nde como as coisas funcionam por aqui, né?",
        "Misha compreendendo o espanto de Lyner com a realidade do Mundo Inferior."
    ),
    9539: (
        "Esta ilha inteira é artificial.\nEla só se mantém no ar graças a este núcleo de força.",
        "Explicação técnica de Misha sobre a sustentação gravitacional da ilha flutuante."
    ),
    9540: (
        "Então, se destruírem isso,\né o fim de tudo aqui!",
        "Misha ressaltando a iminência de uma catástrofe total."
    ),
    9541: (
        "O quê?!\nIsso é perigoso demais!\nVamos dar um jeito de detê-lo!",
        "Prontidão heroica e impulsiva de Lyner para conter o perigo imediatamente."
    ),
    9542: (
        "Uff...\nFoi por um triz!",
        "Suspiro aliviado de naturalidade expressiva do jovem após neutralizarem a fera mecânica."
    ),
    9543: (
        "E você, quem...",
        "Lyner tentando entender a identidade do jovem quando é interrompido."
    ),
    9544: (
        "E-essa não!\nA guarda da Tenba está vindo!\nPreciso dar o fora daqui...",
        "Pavor do rapaz ao avistar as forças armadas da corporação Tenba."
    ),
    9545: (
        "Ei, espera aí!",
        "Misha tentando chamar de volta o garoto que sai correndo."
    ),
    9546: (
        "Ora, ora... Como esperado\ndo magnífico Apóstolo de Elemia.",
        "Bourd entrando em cena com seu costumeiro sarcasmo arrogante e intimidador."
    ),
    9547: (
        "Bourd!!",
        "Lyner reconhecendo imediatamente seu arqui-inimigo da Tenba com hostilidade."
    ),
    9548: (
        "Vou repetir mais uma vez:\nvenha trabalhar para mim.\nConsagre essa sua força à glória da Tenba!",
        "Proposta impositiva e tirânica de recrutamento forçado de Bourd."
    ),
    9549: (
        "Você nunca vai ter\no que quer, seu desgraçado!",
        "Misha desafiando Bourd sem hesitar, rechaçando qualquer submissão."
    ),
    9550: (
        "Então foi você, Misha... Foi você que ajudou\no Lyner a escapar daquela vez.\nTinha que enfiar o bico onde não foi chamada...",
        "Bourd repreendendo Misha com desprezo e ressentimento pela fuga anterior."
    ),
    9551: (
        "Uma Reyvateil devia abaixar a cabeça\ne apenas obedecer às ordens de seus senhores humanos!",
        "Declaração desumanizadora canônica de Bourd evidenciando a exploração e opressão contra as Reyvateils."
    ),
    9552: (
        "Acha mesmo que eu obedeceria\nàs ordens de um crápula feito você?!",
        "Indignação visceral e orgulhosa de Misha perante a prepotência de Bourd."
    ),
    9553: (
        "Olha como abre essa sua bocarra insolente...\nNão passa de uma reles Reyvateil!",
        "Correção do insulto inventado da NISA; fidelidade à expressão 'レーヴァテイルの分際が' (reles Reyvateil que não sabe o seu lugar)."
    ),
    9554: (
        "...Gh!",
        "Reação engasgada de Misha contendo a fúria e o choque pelo insulto."
    ),
    9555: (
        "É, pelo visto não existe a menor chance\nde eu servir a você, Bourd.",
        "Firmeza inabalável de Lyner rejeitando a tirania de Bourd e defendendo Misha."
    ),
    9556: (
        "Ora... Então não há conversa mesmo.\nAdmito que cometi um grande erro de cálculo...",
        "Bourd constatando a intransigência de Lyner com frieza ameaçadora."
    ),
    9557: (
        "Deveria ter me certificado\nde te matar daquela vez!",
        "Ameaça de morte direta e cruel de Bourd."
    ),
    9558: (
        "Essa não! Ele tá falando muito sério!",
        "Pavor iminente de Misha percebendo a intenção assassina de Bourd."
    ),
    9559: (
        "Lyner, vamos dar o fora!",
        "Chamado tático e urgente de Misha para retirada imediata."
    ),
    9560: (
        "Qual a situação lá fora?",
        "Comando seco e militar de Bourd aos seus subordinados."
    ),
    9561: (
        "Continuam cruzando os céus em disparada, senhor!",
        "Relato militar do soldado sobre as aeronaves/ameaças em patrulha."
    ),
    9562: (
        "Entendo.",
        "Resposta concisa de Bourd."
    ),
    9563: (
        "Humpf. Deixem-nos correr.\nNão têm como escapar de qualquer forma.",
        "Arrogância estratégica de Bourd encurralando a presa."
    ),
    9564: (
        "Fechem o aeroporto e cancelem todas as linhas de dirigíveis civis!\nE ordenem que todas as naves no Cais Flutuante retornem a Nemo!",
        "Ordens militares canônicas: 'Cais Flutuante' (滞空岸壁) e cidade flutuante de Nemo."
    ),
    9565: (
        "Às ordens, senhor!",
        "Confirmação militar padrão do subordinado."
    ),
    9566: (
        "Vocês não me escapam...",
        "Promessa sombria e predatória de Bourd."
    ),
    9567: (
        "Hehehe...\nHahaha... Hahahaha!",
        "Gargalhada vil e triunfante sem rubrica artificial."
    ),
    9568: (
        "Eles não estão nos seguindo.",
        "Misha estranhando a ausência de perseguição imediata."
    ),
    9569: (
        "Pois é.\nE duvido muito que tenham desistido...",
        "Desconfiança intuitiva de Lyner."
    ),
    9570: (
        "Que sinistro...",
        "Calafrio de inquietação de Misha."
    ),
    9571: (
        "Mas mudando de assunto...\nSobre aquele autômato com cara de lobo\nde agora há pouco...",
        "Misha trazendo à tona o autômato canino que enfrentaram."
    ),
    9572: (
        "Você parecia conhecer aquela criatura.\nAcho que mereço, no mínimo, uma explicação.",
        "Misha exigindo clareza de Lyner sobre a ameaça que o abalou."
    ),
    9573: (
        "Aquilo ali...\né o vírus que atacou Platina.",
        "Revelação grave de Lyner sobre a natureza do vírus invasor."
    ),
    9574: (
        "O quê?!",
        "Choque genuíno de Misha."
    ),
    9575: (
        "Aquela criatura surgiu no «Altar dos Apóstolos»...\ne então Platina...",
        "Lyner relembrando o trauma da invasão no santuário sagrado (使徒の祭壇)."
    ),
    9576: (
        "...Entendo...",
        "Tom compassivo e pesaroso de Misha ao perceber o peso que Lyner carrega."
    ),
    9577: (
        "...",
        "Pausa reflexiva e silenciosa."
    ),
    9578: (
        "...Seja como for,\nficar remoendo isso aqui não vai adiantar nada.",
        "Lyner sacudindo a tristeza para focar na sobrevivência."
    ),
    9579: (
        "O que faremos agora?",
        "Consulta tática à parceira."
    ),
    9580: (
        "Antes de mais nada,\nprecisamos dar o fora daqui.",
        "Pragmatismo resoluto de Misha."
    ),
    9581: (
        "O caminho comum seria pegar\num dirigível no cais do porto, mas...",
        "Avaliação das rotas de fuga disponíveis."
    ),
    9582: (
        "Aqueles desgraçados não estariam\nnos esperando de emboscada por lá?",
        "Suspeita prudente de Lyner sobre a armadilha de Bourd."
    ),
    9583: (
        "Hum... É bem provável...",
        "Misha pesando o perigo da rota óbvia."
    ),
    9584: (
        "De qualquer forma, vamos dar uma olhada no porto.",
        "Resolução pragmática de Lyner para verificar o terreno."
    ),

    # SEÇÃO 2: Event/406.evd (9585 a 9630)
    9585: (
        "Pai!!",
        "Grito aflito de Lyner ao encontrar o pai ferido na SPU."
    ),
    9586: (
        "Senhor Leard!\nO senhor está bem?!",
        "Respeito afetuoso de Misha ao patriarca de Platina."
    ),
    9587: (
        "Sim... Por um triz,\nainda me mantenho respirando.",
        "Fala entrecortada e resistente do Comandante Leard."
    ),
    9588: (
        "Vamos sair logo daqui!\nTemos que descer para um lugar seguro!",
        "Desejo urgente de Lyner de retirar o pai da zona de perigo."
    ),
    9589: (
        "Acalme-se... Antes disso,\nhá algo de extrema gravidade que preciso lhes revelar...",
        "Firmeza serena de Leard priorizando a missão sobre sua própria saúde."
    ),
    9590: (
        "O que o senhor está dizendo num estado desses?!",
        "Desespero filial de Lyner diante da teimosia do pai."
    ),
    9591: (
        "Vamos levá-lo até o Observatório.\nLá é mais seguro e ele poderá se recompor.",
        "Conselho sensato do cavaleiro Radolf."
    ),
    9592: (
        "Primeiro, sobre a Senhora Shurelia...\nNão resta dúvida de que ela foi subjugada por Mir.",
        "Confirmação solene da tragédia que acometeu Shurelia."
    ),
    9593: (
        "Contudo, as causas para isso continuam uma incógnita.",
        "Pesar e perplexidade técnica de Leard."
    ),
    9594: (
        "E a razão pela qual a Senhora Shurelia...\nou melhor, Mir, me arrastou como prisioneiro...",
        "Leard corrigindo-se com dor ao distinguir Shurelia de sua possessora."
    ),
    9595: (
        "...é muito provavelmente porque sei exatamente como separar\naquele ser malévolo da Senhora Shurelia.",
        "Revelação crucial do segredo guardado por Leard."
    ),
    9596: (
        "O quê?!",
        "Espanto e esperança súbita de Lyner."
    ),
    9597: (
        "Lyner. Ouça com extrema atenção.",
        "Tom paterno austero exigindo concentração total."
    ),
    9598: (
        "A chave para separar a Senhora Shurelia de Mir\nrepousa no coração desta própria SPU.",
        "Indicação do local do artefato de purificação."
    ),
    9599: (
        "Na SPU?\nO senhor quer dizer o lugar onde estava trancafiado?",
        "Lyner conectando os pontos da geografia da Torre."
    ),
    9600: (
        "Exato. Logo antes da câmara onde eu estava cativo,\nhá um vasto salão que abriga o núcleo da SPU.",
        "Instrução espacial precisa de Leard."
    ),
    9601: (
        "Lá repousa um dispositivo resguardado\npor uma barreira impenetrável de luz.",
        "Descrição do artefato e do sistema de proteção de alta energia."
    ),
    9602: (
        "É conhecido como [Divisor FFT].",
        "Menção formal ao artefato canônico 'Divisor FFT' (FFTディバイダ)."
    ),
    9603: (
        "Sua função é purificar e expelir fatores externos\nque tenham invadido o sistema de uma Reyvateil.",
        "Explicação técnica da função de filtragem e purificação do dispositivo."
    ),
    9604: (
        "Em termos simples:\nele é capaz de extirpar Mir\nde dentro da Senhora Shurelia.",
        "Conclusão direta e esperançosa de Leard."
    ),
    9605: (
        "Então, se resgatarmos esse [Divisor FFT]...",
        "Lyner vislumbrando a salvação de Shurelia."
    ),
    9606: (
        "A Senhora Shurelia retornará\nao seu estado primordial.",
        "Confirmação da cura espiritual e física da Administradora."
    ),
    9607: (
        "Contudo, o grande perigo é a barreira protetora.",
        "Mudança de tom para alertar sobre o risco fatal."
    ),
    9608: (
        "O escudo de luz que guarda o [Divisor FFT] é tão devastador\nque um corpo humano não suportaria entrar nele por mais de alguns segundos.",
        "Alerta sobre o campo energético letal aos mortais."
    ),
    9609: (
        "E, no presente momento,\nnão disponho de qualquer meio para desativá-lo.",
        "Reconhecimento amargo da limitação atual."
    ),
    9610: (
        "...Não esquenta com isso.\nSaber de tudo isso já é mais do que suficiente.\nO resto a gente resolve por conta própria.",
        "Lyner tranquilizando o pai com bravura e otimismo."
    ),
    9611: (
        "Obrigado, pai.\nPor ter nos contado tudo isso.",
        "Gratidão calorosa e afetuosa de Lyner."
    ),
    9612: (
        "...",
        "Silêncio comovido de Leard."
    ),
    9613: (
        "Bom, nós estamos indo nessa!",
        "Despedida animada e corajosa de Lyner."
    ),
    9614: (
        "Sim...\nEu também continuarei pesquisando o que puder, mas...",
        "Leard ainda tentando ser útil apesar de seus ferimentos graves."
    ),
    9615: (
        "Pai...",
        "Repreensão doce de Lyner ao ver o pai insistir no trabalho."
    ),
    9616: (
        "Ao menos numa hora dessas,\nvê se descansa um pouco, tá?",
        "Cuidado protetor e sincero do filho com a fragilidade do pai."
    ),
    9617: (
        "O senhor só sabe enfiar a cara no trabalho.",
        "Crítica carinhosa ao excesso de austeridade de Leard."
    ),
    9618: (
        "...Até logo, então!",
        "Despedida jovial e resoluta."
    ),
    9619: (
        "Lyner...",
        "Leard chamando o filho antes que cruze a porta."
    ),
    9620: (
        "Ter alguém da família que se preocupe com a gente...\né um sentimento surpreendentemente bom.",
        "Momento de sublime vulnerabilidade de Leard amolecendo a postura rígida."
    ),
    9621: (
        "...Pai?!",
        "Lyner atônito diante da declaração afetuosa e inédita do pai."
    ),
    9622: (
        "...",
        "Reticência cúmplice e respeitosa."
    ),
    9623: (
        "Desta vez, tenho de admitir:\nfui salvo inteiramente por você.",
        "Reconhecimento nobre da dívida de vida e da força do filho."
    ),
    9624: (
        "A lâmina de uma espada talvez não seja\nalgo tão descartável quanto eu julgava.",
        "Quebra de preconceito de Leard, que antes desdenhava das armas em prol da ciência e do dogma."
    ),
    9625: (
        "...A Senhora Shurelia também...\nEu a confio aos seus cuidados.",
        "Leard legando solenemente a proteção da Administradora a Lyner."
    ),
    9626: (
        "...Pode deixar!\nÉ uma promessa!",
        "Resposta leal e vigorosa de Lyner selando o pacto com o pai."
    ),
    9627: (
        "Heh...\nSem que eu percebesse,\nvocê se tornou um homem tão formidável.",
        "Solilóquio emocionado de orgulho paterno incontido."
    ),
    9628: (
        "...",
        "Silêncio contemplativo de Leard."
    ),
    9629: (
        "Pensar que eu nunca tive a serenidade necessária\npara enxergar isso antes...",
        "Reflexão melancólica sobre o tempo perdido em rigidez."
    ),
    9630: (
        "Certo! Rumo à SPU!",
        "Comando firme e animado de Lyner aos companheiros."
    ),

    # SEÇÃO 3: Event/547.evd (9631 a 9670)
    9631: (
        "O que acham de uma pequena pausa por aqui?\nTem uma coisa que eu gostaria de conversar com vocês.",
        "Lyner convidando o grupo a uma parada para diálogo sincero."
    ),
    9632: (
        "Sabe, gente...\nEu andei pensando muito...",
        "Abertura reflexiva e honesta de Lyner."
    ),
    9633: (
        "Será que... não existiria um jeito\nda gente salvar a Mir...?",
        "A proposta inesperada e comovente de redimir e resgatar a antagonista."
    ),
    9634: (
        "O quêêê?!",
        "Reação histérica e incrédula de Misha."
    ),
    9635: (
        "...Lyner?",
        "Tom surpreso e perspicaz de Shurelia."
    ),
    9636: (
        "Como é que é?!\nVocê por acaso endoidou de vez?!",
        "Choque pragmático e ríspido do veterano Teru Jack."
    ),
    9637: (
        "Eu pensava que a Mir fosse apenas um monstro terrível,\nque só queria ver este mundo reduzido a cinzas.",
        "Lyner desconstruindo sua visão infantil inicial da inimiga."
    ),
    9638: (
        "Mas, depois de percorrer tantos lugares\ne ouvir tantas histórias pelo caminho, eu compreendi.",
        "Fruto da jornada e do contato com os diferentes povos da Torre e do Mundo Inferior."
    ),
    9639: (
        "A Mir não quer destruir o mundo em si.",
        "Conclusão profunda sobre as motivações de Mir."
    ),
    9640: (
        "O que ela carrega é um ódio dilacerante pela humanidade.\nE é exatamente por isso...",
        "Empatia de Lyner reconhecendo as feridas e o ressentimento da antagonista."
    ),
    9641: (
        "Lyner!\nEstamos no meio de uma batalha da qual depende\na própria sobrevivência do mundo!",
        "Apelo severo de Radolf à urgência militar da crise cósmica."
    ),
    9642: (
        "...Eu sei perfeitamente disso.",
        "Resposta calma e consciente de Lyner."
    ),
    9643: (
        "Mas... mesmo assim, não consigo aceitar\nque esmagar o inimigo seja a única resposta possível.",
        "Rejeição da lógica destrutiva do olho por olho."
    ),
    9644: (
        "Eliminar simplesmente todo mundo que nos cause problemas...\nSe fizermos isso, nada nunca vai mudar neste mundo.",
        "Lição madura sobre o ciclo perpétuo da violência e do ódio."
    ),
    9645: (
        "Até hoje, eu lutei sem conhecer absolutamente nada\nsobre quem estava do outro lado. O Falss, o Bourd... e até o Ayatane.",
        "Arrependimento de Lyner por ter lutado às cegas contra seus rivais."
    ),
    9646: (
        "Sei que alguns deles cometeram atrocidades imperdoáveis,\nmas eu sequer tentei entender as razões por trás de seus atos.",
        "Lucidez sobre os atos cruéis de Falss e Bourd sem ignorar suas motivações humanas/traumáticas."
    ),
    9647: (
        "O que se passava no peito de cada um enquanto cruzavam armas comigo...\nQue dores e circunstâncias eles carregavam...",
        "Sensibilidade profunda de Lyner perante a dor dos adversários."
    ),
    9648: (
        "Se eu tivesse compreendido aquilo antes,\ntalvez existisse um caminho onde não precisássemos ter lutado...",
        "Pesar pela perda de vidas e confrontos evitáveis."
    ),
    9649: (
        "...",
        "Shurelia absorvendo as palavras de Lyner em silêncio emocionado."
    ),
    9650: (
        "A pergunta que a Tastiella me fez...\nEu finalmente descobri a resposta.",
        "Conexão direta com os ensinamentos da Guardiã da Torre Tastiella."
    ),
    9651: (
        "O que é que realmente dá origem a todas as guerras...",
        "O grande tema filosófico de Ar tonelico: a falta de diálogo e sintonização mútua dos corações."
    ),
    9652: (
        "E eu pretendo dar essa resposta\natravés das minhas próprias ações!",
        "Resolução de corporificar a resposta na prática e não apenas em discurso."
    ),
    9653: (
        "Vou lutar por um mundo onde a Mir, o Ayatane...\ne todos nós possamos viver juntos!",
        "O ideal de coexistência universal entre humanos, Reyvateils e vírus."
    ),
    9654: (
        "...E qual a probabilidade que você estima\npara tornar esse sonho realidade?",
        "Pergunta calma e perspicaz de Shurelia sondando a solidez da fé de Lyner."
    ),
    9655: (
        "Hã?... É... pra ser sincero, não faço a menor ideia!\nHahaha!",
        "Descontração espontânea e franca de Lyner sem rubrica teatral."
    ),
    9656: (
        "Você não tem jeito mesmo...\nSempre tão impulsivo e cabeça-dura...",
        "Tom de doce reprovação carinhosa de Shurelia."
    ),
    9657: (
        "A Senhora Shurelia tem toda razão.\nTrate de esquecer essa loucura.",
        "Radolf assumindo precipitadamente que Shurelia desaprovou o plano."
    ),
    9658: (
        "Não... Não pretendo impedi-lo.",
        "Firmeza surpreendente de Shurelia contrariando Radolf."
    ),
    9659: (
        "...Hã?",
        "Espanto cômico de Krusche."
    ),
    9660: (
        "Eu disse que ele é imprudente, mas...\neu tenho fé absoluta no Lyner.",
        "Declaração solene e comovente da Deusa depositando seu coração em Lyner."
    ),
    9661: (
        "Eu também.\nUm mundo onde todo mundo possa ser feliz...\né tudo o que eu sempre sonhei.",
        "Aurica expressando seu anseio de bondade e harmonia."
    ),
    9662: (
        "Aurica?!",
        "Misha surpresa com o entusiasmo imediato da rival/amiga."
    ),
    9663: (
        "Ai, não tem jeito mesmo com vocês dois, né?...\nEstá bem! Eu também vou ficar ao seu lado até o fim!",
        "Misha cedendo com ternura tsundere indisfarçável."
    ),
    9664: (
        "Olha, não me parece nada mal.\nTem cara de que vai abrir caminho para um mundo bem diferente,\ne isso soa divertidíssimo.",
        "Espírito aventureiro, inventor e desinibido de Krusche."
    ),
    9665: (
        "...Faça como quiser.\nMas fique avisado: se eu farejar o menor sinal de perigo,\nte puxo de volta na mesma hora!",
        "Pose durona do veterano Jack disfarçando sua lealdade protetora."
    ),
    9666: (
        "Bem, é isso aí.\nEm bom português: estaremos sempre cobrindo a sua retaguarda.",
        "Radolf abraçando a causa com lealdade inabalável de cavaleiro."
    ),
    9667: (
        "Portanto, fique tranquilo...\ne vá em frente, contanto que tente não morrer no caminho.",
        "Bom humor camarada de Radolf."
    ),
    9668: (
        "Gente... Muito obrigado a todos.",
        "Gratidão profunda e humilde de Lyner fortalecido pela união dos companheiros."
    ),
    9669: (
        "Pois bem, decidida a rota,\nprecisamos nos apressar.",
        "Radolf chamando o grupo à ação prática."
    ),
    9670: (
        "Antes que o Ayatane cometa\numa tragédia sem volta.",
        "Alerta sombrio sobre o perigo de Ayatane consumar seu sacrifício destrutivo."
    ),

    # SEÇÃO 4: Event/721.evd (9671 a 9712)
    9671: (
        "Hum... Olhando assim,\nnão parece haver a menor pista por aqui...",
        "Lyner investigando o platô montanhoso da Cosmosfera."
    ),
    9672: (
        "Espera! As montanhas são cheias de ervas medicinais.\nQuem sabe a gente não encontra alguma capaz de curar a doença dela?",
        "Aurica propondo a busca para salvar sua amiga/irmã Claire."
    ),
    9673: (
        "Então vamos dar uma boa olhada por aqui.",
        "Lyner concordando e apoiando a busca."
    ),
    9674: (
        "...Nada feito.\nAliás, a altitude aqui não está alta demais para brotar alguma coisa?",
        "Raciocínio prático de Lyner após procurar em vão."
    ),
    9675: (
        "Achei!",
        "Exclamação vitoriosa e ingênua de Aurica."
    ),
    9676: (
        "Sério?!",
        "Surpresa e alívio de Lyner."
    ),
    9677: (
        "Impressionante. Você tem um gosto bem fascinante...\nEssa planta aí é puro veneno.",
        "A Sombra de Aurica surgindo com voz sibilante e sarcástica."
    ),
    9678: (
        "Hã?",
        "Desconforto e susto de Aurica."
    ),
    9679: (
        "Quem é você?!",
        "Reação imediata de defesa de Lyner contra a intrusa."
    ),
    9680: (
        "Muito prazer. Eu sou a faceta da sua querida «euzinha»\nque você ainda não conhecia... Acho que posso me apresentar assim, não?",
        "Ironia gélida da Sombra revelando ser a personificação reprimida dos desejos de Aurica."
    ),
    9681: (
        "E agora... é um demônio?!",
        "Lyner reagindo à aparência sinistra da manifestação psíquica."
    ),
    9682: (
        "Você ter colhido logo uma erva venenosa\nsó prova que se conhece muito bem no fundo da alma, não acha?",
        "Provocação psicológica da Sombra expondo a intenção inconsciente de Aurica."
    ),
    9683: (
        "...C-como assim...?",
        "Hesitação trêmula de Aurica pressentindo o pesadelo."
    ),
    9684: (
        "Ué? Quer mesmo que eu diga com todas as letras?\nPelo visto a gente tem uma veia masoquista bem mais afiada do que parecia.",
        "Correção do erro da NISA ('sadistic'); no original 'マゾっ気' refere-se ao prazer de se martirizar."
    ),
    9685: (
        "Tudo bem, eu falo sem rodeios:\nvocê odeia a Claire, não odeia?!\nEntão aproveita e mata ela de uma vez por todas!",
        "Incitação direta e brutal ao assassinato de Claire."
    ),
    9686: (
        "O-o que você está dizendo?!\nIsso é verdade, Aurica...?",
        "Pavor e incredulidade de Lyner ao ouvir tamanha maldade."
    ),
    9687: (
        "N-não é nada disso!\nA mana Claire é... ela é quem eu mais amo...",
        "Aurica tentando desesperadamente manter a fachada de amor fraternal pela 'mana Claire' (クレアお姉ちゃん)."
    ),
    9688: (
        "«Quem eu mais amo»...\nSerá meeesmo?",
        "Desdém zombeteiro e sarcástico da Sombra destruindo a ilusão."
    ),
    9689: (
        "...Hã?",
        "Fraquejada psíquica de Aurica."
    ),
    9690: (
        "Puxe bem pela memória.\nLembra de todas as humilhações pelas quais tivemos que passar\npor causa da Claire?",
        "Início da evocação dos traumas reprimidos de infância."
    ),
    9691: (
        "Notas impecáveis, um poder descomunal de Reyvateil e dona de uma beleza radiante: essa era a Claire.\nE nós duas ali largadas na sombra dela, sem que vivaldino nenhum olhasse na nossa cara!",
        "O contraste doloroso entre a perfeição de Claire e a invisibilidade de Aurica."
    ),
    9692: (
        "Desde pequenas, a gente vivia encolhida atrás da Claire, tão radiante e cheia de vida...\nMas, mesmo ali escondidas, o que a gente queria de verdade era brilhar lá na frente!",
        "O grito sufocado de vaidade e anseio de reconhecimento de Aurica."
    ),
    9693: (
        "Se não fosse pela Claire, nós teríamos sido a grande estrela tantas e tantas vezes!\nLembra do concurso da donzela mais bela no festival do vilarejo? Pois é.",
        "Evocação da mágoa por ter perdido o posto de heroína e o concurso de beleza para Claire."
    ),
    9694: (
        "E tem mais: quando a Tenba veio recrutar a Claire,\nnem sequer olharam na nossa direção!",
        "A dor da rejeição institucional da Tenba, selando seu complexo de inferioridade."
    ),
    9695: (
        "...Para, por favor...",
        "Súplica sufocada de Aurica perante a verdade que rasga sua alma."
    ),
    9696: (
        "A Claire sempre foi uma pedra pontuda cravada no nosso sapato!\nChegou a hora de dar um basta definitivo nesse tormento...",
        "Adaptação expressiva do provérbio japonês '目の上のタンコブ' (pedra no sapato / espinho na garganta)."
    ),
    9697: (
        "Não!!...\nA mana Claire é...",
        "Conflito desesperado entre o carinho fraterno e o ódio reprimido."
    ),
    9698: (
        "Minha doce e querida Aurica...\nCrie coragem e dê esse passo adiante...\nVocê vai ver como um mundo novo em folha se abrirá para nós...",
        "Sedução mefistofélica da Sombra convencendo Aurica a cometer o crime."
    ),
    9699: (
        "E-espera um minuto aí!\nAcho que dar esse tipo de passo é cruzar completamente os limites...",
        "Lyner tentando intervir e conter o delírio assassino incitado pela Sombra."
    ),
    9700: (
        "Não meta esse seu bedelho onde não foi chamado!\nO que um forasteiro como você sabe sobre mim?!\nVocê tem a menor capacidade de sentir na pele as humilhações que engolimos à sombra da Claire?!",
        "Fúria defensiva da Sombra rejeitando a interferência de Lyner."
    ),
    9701: (
        "Aurica...\nNós engolimos tanta amargura até hoje, não foi?\nChegou a hora de romper de vez com essa versão fraca de si mesma.",
        "A Sombra apelando ao ego ferido de Aurica para fazê-la quebrar seus laços morais."
    ),
    9702: (
        "Basta dar uma infusão desta erva venenosa para a Claire...\ne todas as lembranças amargas do passado vão virar fumaça!\nE uma nova versão de nós duas nascerá!",
        "O ápice da tentação envenenada prometendo falsamente renascimento através da morte de Claire."
    ),
    9703: (
        "...É verdade. Se eu der isso para ela beber...\nfinalmente vou me libertar de todas as amarras\nque me prendiam à mana Claire...",
        "Aurica entrando em transe, sucumbindo à loucura sombria de sua mente dividida."
    ),
    9704: (
        "Aurica!",
        "Grito aterrado de Lyner tentando despertá-la da hipnose do ódio."
    ),
    9705: (
        "Você não faz a menor ideia, Lyner!\nPor causa da mana Claire...\neu sempre fui humilhada e jogada de lado por todo mundo!",
        "O veneno jorrando da boca de Aurica contra Lyner, culpando Claire por sua dor."
    ),
    9706: (
        "Nos estudos, nos exercícios físicos... e até nas habilidades de Reyvateil!\nVivia todo mundo me comparando com ela e me chamando de «inútil»!!",
        "Fidelidade exata ao estigma de infância '出来ない子' («inútil» / incapaz)."
    ),
    9707: (
        "Eu cansei... Vou dar um basta\nnessa garota imprestável de uma vez por todas!",
        "Decisão cega de ruptura radical de Aurica, fugindo em disparada."
    ),
    9708: (
        "Aurica!!\nDroga... Preciso ir atrás dela agora mesmo!",
        "Pavor e urgência de Lyner para impedir que ela execute o crime."
    ),
    9709: (
        "É inútil.\nAquela menina finalmente despertou\npara a sua verdadeira natureza.",
        "Crueldade triunfante da Sombra cantando vitória."
    ),
    9710: (
        "Foi você que envenenou a cabeça dela!",
        "Fúria justificada de Lyner contra a criatura."
    ),
    9711: (
        "Eu não envenenei cabeça nenhuma.\nAfinal de contas, eu também sou a verdadeira Aurica.\nMas e aí... não ia sair correndo atrás dela?",
        "Cinismo cortante da Sombra lembrando que ela é parte legítima do inconsciente de Aurica."
    ),
    9712: (
        "Maldição!\nTenho que correr...!!",
        "Lyner arrancando em desespero para salvar Claire e a alma de Aurica."
    ),
}

# Verificações de integridade
expected_count = 184
start_id = 9529
end_id = 9712

dialogues_list = []
errors = []

for i in range(start_id, end_id + 1):
    if i not in curated_data:
        errors.append(f"Missing dialogue ID {i}")
        continue
    pt, notes = curated_data[i]
    
    # Validação 1: Nenhuma linha após \n começando com pontuação órfã
    lines = pt.split('\n')
    for l_idx, line in enumerate(lines):
        if l_idx > 0 and line:
            if line[0] in '.,!?:;)]}':
                errors.append(f"ID {i}: Line starts with orphan punctuation '{line[0]}': {repr(line)}")
            if line.startswith('...'):
                errors.append(f"ID {i}: Line starts with orphan ellipsis: {repr(line)}")
                
    # Validação 2: Nenhuma rubrica cênica (*suspiro*, etc.)
    if re.search(r'\*[^*]+\*', pt):
        errors.append(f"ID {i}: Scenic rubric found: {repr(pt)}")
        
    # Validação 3: Balanceamento de aspas e parênteses
    quotes_count = pt.count('"')
    if quotes_count % 2 != 0:
        errors.append(f"ID {i}: Unbalanced double quotes: {repr(pt)}")
    if pt.count('(') != pt.count(')'):
        errors.append(f"ID {i}: Unbalanced parentheses: {repr(pt)}")
    if pt.count('«') != pt.count('»'):
        errors.append(f"ID {i}: Unbalanced guillemets: {repr(pt)}")
    if pt.count('[') != pt.count(']'):
        errors.append(f"ID {i}: Unbalanced brackets: {repr(pt)}")

    dialogues_list.append({
        "id": i,
        "pt_curated": pt,
        "curation_notes": notes
    })

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print("  -", e)
else:
    print(f"Validation SUCCEEDED! All {len(dialogues_list)} dialogues are valid.")
    output_obj = {
        "block_id": "BLK_EVD_040",
        "dialogues": dialogues_list
    }
    with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_040_output.json', 'w', encoding='utf-8') as f_out:
        json.dump(output_obj, f_out, ensure_ascii=False, indent=2)
    print("Saved output to Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_040_output.json")

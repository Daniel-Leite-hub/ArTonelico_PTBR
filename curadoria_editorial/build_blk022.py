# -*- coding: utf-8 -*-
"""
Script de construção e curadoria integral de BLK_EVD_022.
Garante paridade canônica, eufonia literária, ausência de rubricas e obediência estrita ao validador técnico.
"""

import json
from pathlib import Path

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_022_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_022_output.json")

# Dicionário de curadoria id -> (curated_ptbr, verdict, rationale)
CURATIONS = {}

# ==========================================
# EVENT 568: IDs 5573..5589 (Kanade / Retrogaming Mini-game)
# ==========================================
CURATIONS[5573] = (
    "...Pensando bem, a gente não\nacabou de vencer cinco vezes seguidas?",
    "rewritten",
    "Oralidade natural de Lyner constatando a quinta vitória consecutiva contra Kanade no minigame retro."
)
CURATIONS[5574] = (
    "...Uééé? É, é verdade!\nMeus parabéns!",
    "rewritten",
    "Expressão fofa de espanto de Kanade (...ひぇ?) seguida de sua comemoração animada."
)
CURATIONS[5575] = (
    "É, obrigado... Mas e aí,\no que você vai me dar de prêmio?",
    "rewritten",
    "Tom descontraído e curioso de Lyner cobrando a recompensa prometida."
)
CURATIONS[5576] = (
    "O prêmio...",
    "rewritten",
    "Hesitação tímida de Kanade criando suspense antes da revelação cômica."
)
CURATIONS[5577] = (
    "...Sou... eu mesma.\nPor favor, fique com a Kanade!",
    "rewritten",
    "Fala em terceira pessoa fofa e de duplo sentido ingênuo de Kanade (カナデをもらってください) oferecendo a si mesma."
)
CURATIONS[5578] = (
    "Cof, cof...?!",
    "rewritten",
    "Interjeição eufônica de engasgo/espanto de Lyner (ぶっ...!) diante da proposta de Kanade, sem rubricas."
)
CURATIONS[5579] = (
    "Sendo assim, vou passar a minha\nChave de Análise para a Senhora Shurelia.",
    "rewritten",
    "Kanade explicando tecnicamente a concessão da Chave de Análise (解析キー) à Deusa Shurelia."
)
CURATIONS[5580] = (
    "Com ela, a senhora poderá me convocar\na qualquer momento de agora em diante.",
    "rewritten",
    "Explicação do sistema de invocação da Criança da Luz em batalha."
)
CURATIONS[5581] = (
    "Tenho certeza de que serei útil nas batalhas\nde vocês, então conto com a sua cooperação!",
    "rewritten",
    "Entusiasmo prestativo e polidez formal de Kanade prometendo apoio nos combates."
)
CURATIONS[5582] = (
    "Ah, compreendo...\nSendo assim, aceito sua gentil oferta\ne vou convocá-la quando necessário.",
    "rewritten",
    "Polidez digna e serena de Shurelia aceitando a invocação (お言葉に甘えて召喚させてもらいますね)."
)
CURATIONS[5583] = (
    "...A-Ahaha...\nÉ-É claro, era isso que ela queria dizer!",
    "rewritten",
    "Lyner rindo sem jeito ao perceber a inocência da proposta técnica."
)
CURATIONS[5584] = (
    "Lyner... por acaso você não estava\nimaginando alguma bobagem indecente?",
    "rewritten",
    "Shurelia repreendendo os pensamentos maliciosos de Lyner com olhar inquisidor."
)
CURATIONS[5585] = (
    "Hãã?! Q-Que bobagem!\nComo se eu fosse pensar numa coisa dessas!",
    "rewritten",
    "Lyner em pânico e negação afobada (そんなわけ無いじゃないですか!)."
)
CURATIONS[5586] = (
    "Hahaha!",
    "approved_as_is",
    "Riso nervoso e aliviado de Lyner preservado."
)
CURATIONS[5587] = (
    "......",
    "approved_as_is",
    "Silêncio desconfiado e severo de Shurelia."
)
CURATIONS[5588] = (
    "...?",
    "approved_as_is",
    "Ponto de interrogação de incompreensão inocente de Kanade."
)
CURATIONS[5589] = (
    "Shurelia teceu a Magia Vermelha\n[Criança da Luz]!",
    "rewritten",
    "Notificação canônica de síntese: verbo sagrado 'tecer' (紡ぎ出した) e título místico [Criança da Luz] (光の御子)."
)

# ==========================================
# EVENT 733: IDs 5590..5599 (Cosmosphere Level 4 End / Aurica & Don Leon)
# ==========================================
CURATIONS[5590] = (
    "Lyner... Muito obrigada por tudo mais uma vez.\nSinto que você vive me salvando...",
    "rewritten",
    "Correção de gênero obrigatória (muito obrigada feminino) e gratidão sincera de Aurica."
)
CURATIONS[5591] = (
    "Que nada! Pra ser bem sincero, eu\nquase não tive o que fazer neste nível.",
    "rewritten",
    "Modéstia calorosa e reconfortante de Lyner desvalorizando o próprio esforço para exaltar Aurica."
)
CURATIONS[5592] = (
    "Será...? Mas acho que só consegui superar tudo\nporque você me disse que “eu já sou mais que suficiente”...",
    "rewritten",
    "Aurica recordando a frase de validação de Lyner que a fez romper o bloqueio interior."
)
CURATIONS[5593] = (
    "Mas quem superou isso foi você, Aurica.\nDevia se orgulhar de si mesma!",
    "rewritten",
    "Lyner reforçando o mérito e a autoestima de Aurica com convicção."
)
CURATIONS[5594] = (
    "...Tem razão.\nÉ... vou fazer isso!",
    "rewritten",
    "Aurica assentindo com um sorriso confiante e renovado."
)
CURATIONS[5595] = (
    "Então, eu... já vou indo.",
    "rewritten",
    "Despedida afetuosa e tímida de Aurica ao deixar a Cosmosfera."
)
CURATIONS[5596] = (
    "O próximo é o Nível 5...\nQue tipo de mundo será desta vez...?",
    "rewritten",
    "Monólogo reflexivo de Lyner antecipando os desafios do Nível 5 da Cosmosfera."
)
CURATIONS[5597] = (
    "Já tá começando a ficar com medinho?",
    "rewritten",
    "Provocação ríspida e debochada de Don Leon surgindo das sombras."
)
CURATIONS[5598] = (
    "Tá de brincadeira comigo?",
    "rewritten",
    "Resposta desafiadora e confiante de Lyner a Don Leon."
)
CURATIONS[5599] = (
    "Bom, se for voltar aqui,\né bom vir com a corda toda.",
    "rewritten",
    "Advertência marcial de Don Leon exigindo foco e espírito de luta (しっかり気合いを入れてくるんだな)."
)

# ==========================================
# EVENT 849: IDs 5600..5605 (Dividing Gate A8 / FFT Spectrum)
# ==========================================
CURATIONS[5600] = (
    "Aqui é o [Anteparo A8]. O usuário\nautorizado deve dar um passo à frente.",
    "rewritten",
    "Fixação da toponímia canônica [Anteparo A8] (A8隔壁) e protocolo militar da guarnição."
)
CURATIONS[5601] = (
    "Autenticação por [Espectro FFT].\nLyner Barsett. Suas ordens, por favor.",
    "rewritten",
    "Protocolo acústico e biométrico [Espectro FFT] (FFTスペクトラム認証) reconhecendo o cavaleiro."
)
CURATIONS[5602] = (
    "Liberar o [Anteparo A8].",
    "rewritten",
    "Ordem de comando direta de Lyner abrindo a comporta."
)
CURATIONS[5603] = (
    "#0Ma paks ga exec guol A8 al noes.",
    "rewritten",
    "Restauração do código executável ancestral em Hymmnos (#0), que constava completamente vazio no banco."
)
CURATIONS[5604] = (
    "Código autenticado com sucesso.",
    "rewritten",
    "Resposta de confirmação de segurança do sistema da Torre."
)
CURATIONS[5605] = (
    "Dois segundos para a abertura do anteparo.\nStatus: permissão de passagem confirmada.",
    "rewritten",
    "Contagem regressiva e liberação de tráfego do Anteparo A8."
)

# ==========================================
# EVENT 10: IDs 5606..5609 (Arrival at Lower World Village)
# ==========================================
CURATIONS[5606] = (
    "Então este é um vilarejo do [Mundo Inferior]...\nÉ totalmente diferente de [Platina].",
    "rewritten",
    "Lyner observando o contraste marcante entre o Mundo Inferior e sua cidade natal flutuante Platina."
)
CURATIONS[5607] = (
    "Parece tão cheio de vida...",
    "rewritten",
    "Sensação de vivacidade e dinamismo que impressiona o jovem cavaleiro."
)
CURATIONS[5608] = (
    ".........",
    "approved_as_is",
    "Pausa contemplativa de Lyner absorvendo o novo ambiente."
)
CURATIONS[5609] = (
    "De qualquer forma, vou dar uma boa olhada\npor todos os cantos.",
    "rewritten",
    "Determinação exploratória de Lyner para conhecer o vilarejo."
)

# ==========================================
# EVENT 288: IDs 5610..5611 (Running with Misha)
# ==========================================
CURATIONS[5610] = (
    "Lyner!",
    "approved_as_is",
    "Grito de chamado urgente de Misha mantido perfeitamente."
)
CURATIONS[5611] = (
    "Vamos correr com tudo o que temos!!",
    "rewritten",
    "Comando urgente de corrida a toda velocidade (全力で走るぞ!!)."
)

# ==========================================
# EVENT 819: IDs 5612..5615 (Looking for Don Leon)
# ==========================================
CURATIONS[5612] = (
    "Ah, é mesmo! Preciso contar ao Don Leon\nsobre o mundo virtual da Senhora Shurelia...",
    "rewritten",
    "Lembrança de Lyner querendo relatar a experiência da realidade virtual retro a Don Leon."
)
CURATIONS[5613] = (
    "Ei, Don Leon! Don Leon!",
    "approved_as_is",
    "Lyner chamando pelo companheiro guardião da Cosmosfera."
)
CURATIONS[5614] = (
    "......",
    "approved_as_is",
    "Silêncio indicando a ausência do guardião."
)
CURATIONS[5615] = (
    "Ah, é verdade... O Don Leon desapareceu\nnaquele dia, né... Desse jeito, não tem como\neu falar com ele.",
    "rewritten",
    "Melancolia de Lyner ao recordar o sumiço temporário de Don Leon após os traumas da mente de Aurica."
)

# ==========================================
# EVENT 244: IDs 5616..5626 (Shuttle Gondola / Bets with Krusche & Misha)
# ==========================================
CURATIONS[5616] = (
    "Eu já vi isso em algum lugar...\nOu será que não...?",
    "rewritten",
    "Déjà-vu de Lyner observando os controles da gôndola de traslado."
)
CURATIONS[5617] = (
    "Não pode ser...!",
    "rewritten",
    "Exclamação de espanto empolgado de Misha reconhecendo a máquina."
)
CURATIONS[5618] = (
    "Que saudaaade!!",
    "rewritten",
    "Explosão nostálgica eufórica e expressiva de Krusche (懐かしいー!!)."
)
CURATIONS[5619] = (
    "...Hã?",
    "rewritten",
    "Confusão cômica de Lyner sem entender a reação das duas garotas."
)
CURATIONS[5620] = (
    "Lyner! É o sistema de controle para mover\na Gôndola de Traslado!",
    "rewritten",
    "Misha explicando que se trata do comando do bondinho/gôndola (シャトルゴンドラ)."
)
CURATIONS[5621] = (
    "Aquele onde apostamos os [Combos Dokkoi]\ne caímos na pancadaria... aquele mesmo!",
    "rewritten",
    "Krusche recordando com bom humor as brigas de infância apostando o prato tradicional Combo Dokkoi."
)
CURATIONS[5622] = (
    "Isso! Aquele lá!",
    "rewritten",
    "Misha confirmando com energia a memória compartilhada."
)
CURATIONS[5623] = (
    "Falando nisso, você ainda me deve 84 [Combos Dokkoi],\n57 taças de [Gelo Ralado], 7 peixes secos ao mirin\ne 1 garrafa de [Megaleite] pendurados na conta!",
    "rewritten",
    "Krusche cobrando a hilária lista de dívidas culinárias com os termos canônicos precisos."
)
CURATIONS[5624] = (
    "E você me deve 56 [Combos Dokkoi],\n116 [Balas de Gato] e 20 garrafas de [Megaleite]!\nVê se não se faz de desentendida!",
    "rewritten",
    "Misha retrucando com sua própria conta detalhada de doces e leite em cobrança acalorada."
)
CURATIONS[5625] = (
    "Vocês ainda lembram dessa dívida...?",
    "rewritten",
    "Lyner perplexo com a memória inacreditável de ambas para cobranças de guloseimas."
)
CURATIONS[5626] = (
    "Lyner! Se você disparar uma [Bomba de Raio]\nde novo, tenho certeza de que a gôndola volta a andar!",
    "rewritten",
    "Sugestão prática de Misha para reativar o maquinário com a [Bomba de Raio] (雷弾)."
)

# ==========================================
# EVENT 540: IDs 5627..5652 (Platina Council / Mir's revival & Em Pheyna)
# ==========================================
CURATIONS[5627] = (
    "Pai, o Ayatane não passou por aqui?",
    "rewritten",
    "Lyner indagando Leard sobre o paradeiro de Ayatane."
)
CURATIONS[5628] = (
    "...Acha mesmo que ele viria até aqui?\nOu será que aconteceu alguma coisa?",
    "rewritten",
    "Tom pragmático e inquiridor do comandante Leard sobre Ayatane."
)
CURATIONS[5629] = (
    "Não, não é nada disso...\nSó perguntei por via das dúvidas.",
    "rewritten",
    "Lyner desconversando para não alarmar o pai."
)
CURATIONS[5630] = (
    "Mudando de assunto... em que pé está\na situação da Mir?",
    "rewritten",
    "Leard voltando a atenção para a crise existencial da ressurreição de Mir."
)
CURATIONS[5631] = (
    "Pois é, as coisas na [Crônica Crescente]\nestavam um verdadeiro caos.",
    "rewritten",
    "Lyner descrevendo o altar corrompido da Crônica Crescente."
)
CURATIONS[5632] = (
    "Surgiu uma esfera de luz, e a voz de Mir\necoava de lá de dentro...",
    "rewritten",
    "Descrição do fenômeno sobrenatural da manifestação de Mir."
)
CURATIONS[5633] = (
    "...O quê?!",
    "rewritten",
    "Alarme e gravidade de Leard diante da manifestação fônica de Mir."
)
CURATIONS[5634] = (
    "Mir já concluiu cerca de cinquenta por cento\nde sua ressurreição.",
    "rewritten",
    "Relatório fônico preciso e austero de Shurelia sobre o avanço viral de Mir."
)
CURATIONS[5635] = (
    "Que calamidade... Eu não imaginava que a situação\ntivesse se agravado a esse ponto...",
    "rewritten",
    "Angústia de Leard percebendo o abismo iminente que ameaça Platina."
)
CURATIONS[5636] = (
    "Senhora Shurelia...",
    "rewritten",
    "Vocativo reverente de Leard buscando orientação da administradora da Torre."
)
CURATIONS[5637] = (
    "Depois de termos chegado até aqui...\nnão podemos mais recuar.",
    "rewritten",
    "Determinação solene e inabalável de Shurelia (もう後には退けません)."
)
CURATIONS[5638] = (
    "Creio que não nos resta outra saída a não ser\ndestruir o verdadeiro corpo de Mir.",
    "rewritten",
    "Veredito terminal de Shurelia sobre a necessidade de destruir o corpo original de Mir."
)
CURATIONS[5639] = (
    "...Compreendo.",
    "rewritten",
    "Assentimento pesado e resignado de Leard."
)
CURATIONS[5640] = (
    "Toda essa consequência nos atinge agora porque me\nfaltou força no passado, e recorri a um “selamento” provisório.",
    "rewritten",
    "Confissão dolorosa de Shurelia assumindo o peso histórico de ter selado Mir."
)
CURATIONS[5641] = (
    "Eu assumirei a responsabilidade e lidarei com isso.",
    "rewritten",
    "Compromisso heroico e maternal de Shurelia com o destino de Sol Ciel."
)
CURATIONS[5642] = (
    "Senhora Shurelia... No entanto...",
    "rewritten",
    "Leard hesitante diante do perigo a que a divindade se expõe."
)
CURATIONS[5643] = (
    "Não se preocupe, pai. Eu estou aqui para apoiá-la!",
    "rewritten",
    "Lyner se oferecendo com bravura juvenil como guardião protetor de Shurelia."
)
CURATIONS[5644] = (
    "É justamente por você estar ao lado dela\nque a minha preocupação aumenta...",
    "rewritten",
    "Ironia paterna e afetuosa de Leard quebrando a tensão dramática."
)
CURATIONS[5645] = (
    "Como é que é?!",
    "rewritten",
    "Reação indignada e cômica de Lyner ao descrédito do pai."
)
CURATIONS[5646] = (
    "Não, Leard... O Lyner é o esteio do meu coração.",
    "rewritten",
    "Declaração comovente e profunda de Shurelia validando o papel afetivo de Lyner (心の支え)."
)
CURATIONS[5647] = (
    "Senhora Shurelia...",
    "rewritten",
    "Lyner profundamente tocado pelas palavras da Deusa."
)
CURATIONS[5648] = (
    "C-Compreendo... Se a senhora diz,\nentão não há problema algum, mas...",
    "rewritten",
    "Leard desconcertado e surpreso com o laço íntimo entre a Deusa e seu filho."
)
CURATIONS[5649] = (
    "De qualquer forma, será melhor nos apressarmos\nquanto a Mir.",
    "rewritten",
    "Retorno imediato ao senso de urgência militar."
)
CURATIONS[5650] = (
    "Contudo... se for para derrotá-la,\nterão que ir até Em Pheyna...",
    "rewritten",
    "Leard traçando a rota geográfica obrigatória até a cidade Teru de Em Pheyna."
)
CURATIONS[5651] = (
    "...e convencer Tastiella a desfazer o selo de Mir.",
    "rewritten",
    "Menção à guardiã milenar Tastiella e ao rito de quebra do selo."
)
CURATIONS[5652] = (
    "...Tem razão.",
    "rewritten",
    "Concordância serena de Shurelia com o plano de ação."
)

# ==========================================
# EVENT 694: IDs 5653..5654 (Flower Spirit)
# ==========================================
CURATIONS[5653] = (
    "Olá, Lyner. Boa noite.",
    "rewritten",
    "Cumprimento delicado do Espírito da Flor na colina mental."
)
CURATIONS[5654] = (
    "Não sobrou nenhuma florzinha para regar.\nFica um vazio estranho, não é?",
    "rewritten",
    "Tom melancólico e poético do Espírito da Flor refletindo sobre o término do florescimento."
)

# ==========================================
# EVENT 381: IDs 5655..5658 (Soleil Stones / Tail of Reminiscence & Skuwat)
# ==========================================
CURATIONS[5655] = (
    "A matéria-prima, a [Pedra Soleil], fica num lugar\nchamado [Asa da Reminiscência].",
    "rewritten",
    "Misha indicando o ingrediente [Pedra Soleil] e a toponímia canônica [Asa da Reminiscência] (追憶の尾翼)."
)
CURATIONS[5656] = (
    "É um pouquinho longe daqui, mas vamos nos esforçar!",
    "rewritten",
    "Encorajamento caloroso e afetuoso de Misha."
)
CURATIONS[5657] = (
    "Agora é possível viajar\npara a [Asa da Reminiscência] no Mapa-Múndi!",
    "rewritten",
    "Mensagem de sistema canônica desbloqueando a [Asa da Reminiscência]."
)
CURATIONS[5658] = (
    "Agora é possível viajar\npara as [Ruínas de Skuwat] no Mapa-Múndi!",
    "rewritten",
    "Mensagem de sistema canônica desbloqueando as [Ruínas de Skuwat] (スクワート廃墟), corrigindo erro crasso da NISA."
)

# ==========================================
# EVENT 460: IDs 5659..5688 (Kyle's Diary Vol 2 / Falss & Bourd Conspiracy)
# ==========================================
CURATIONS[5659] = (
    "“Nova Autobiografia de Kyle, Volume 2”.\nO diário do Bispo Falss...",
    "rewritten",
    "Lyner examinando o volume confidencial do diário com a identidade original de Falss."
)
CURATIONS[5660] = (
    "Havia um homem ambicioso na Tenba. Chamava-se Bourd.\nEu o encontrei em certas ruínas chamadas Colina do Canto.",
    "rewritten",
    "Início do relato de Kyle revelando seu primeiro contato com Bourd na sagrada Colina do Canto (謳う丘)."
)
CURATIONS[5661] = (
    "Dizer que o “encontrei” é um certo exagero, admito.\nTratava-se do costumeiro confronto armado entre a Tenba e a Igreja.",
    "rewritten",
    "Cinismo de Kyle contextualizando os conflitos armados no Mundo Inferior."
)
CURATIONS[5662] = (
    "Disputavam a hegemonia sobre aquelas ruínas.\nUma futilidade patética.",
    "rewritten",
    "Desprezo intelectual de Kyle pelas disputas mesquinhas de facções terrenas."
)
CURATIONS[5663] = (
    "Ruínas tão remotas como aquelas... Bastaria um punhado\nde homens se infiltrar para que qualquer posse perdesse o sentido.",
    "rewritten",
    "Raciocínio tático pragmático sobre a vulnerabilidade de ruínas distantes."
)
CURATIONS[5664] = (
    "Resolvi propor um acordo de paz recorrendo\naos meus costumeiros ardis.",
    "rewritten",
    "Elegância maquiavélica de Kyle descrevendo sua intervenção diplomática calculada."
)
CURATIONS[5665] = (
    "Cederia a jurisdição das ruínas à Tenba. Em contrapartida,\neles cooperariam em uma certa missão da Igreja.",
    "rewritten",
    "Os termos da barganha política entre Kyle e as ambições industriais da Tenba."
)
CURATIONS[5666] = (
    "Bourd, a princípio reticente, mudou de postura\nno mesmo instante em que ouviu uma única palavra.",
    "rewritten",
    "A virada psicológica instantânea na negociação com Bourd."
)
CURATIONS[5667] = (
    "O Cristal Hymmnos. Compreensível... Por estas bandas,\neles o veneram como um tesouro sagrado.",
    "rewritten",
    "Fixação terminológica de [Cristal Hymmnos] e o espanto com a idolatria no Mundo Inferior."
)
CURATIONS[5668] = (
    "Quando lhe revelei o verdadeiro poder do cristal,\nele aceitou a proposta de pronto, sem qualquer hesitação.",
    "rewritten",
    "A ganância de Bourd selando o pacto nefasto."
)
CURATIONS[5669] = (
    "Um comandante tão simplório que nem sequer ofereceu desafio;\npara mim, não teve graça alguma.",
    "rewritten",
    "Tédio aristocrático de Kyle ao manipular alguém desprovido de intelecto."
)
CURATIONS[5670] = (
    "Bolar estratagemas sem precisar sujar as próprias mãos\né um prazer refinado.",
    "rewritten",
    "A essência pérfida da mente manipuladora de Kyle/Falss."
)
CURATIONS[5671] = (
    "Orgulho-me do plano de hoje como o ápice dessa filosofia.",
    "rewritten",
    "Empáfia de Kyle vangloriando-se de sua maquinação mais audaciosa."
)
CURATIONS[5672] = (
    "O cerne da operação: assassinar Misha, a [Cantora das Estrelas].",
    "rewritten",
    "A frieza chocante do plano: execução da sagrada [Cantora das Estrelas] (星詠)."
)
CURATIONS[5673] = (
    "Segundo minhas averiguações, a Tenba vive em constante conflito com a Tribo Teru.",
    "rewritten",
    "Mapeamento da hostilidade ancestral entre Tenba e a linhagem Teru."
)
CURATIONS[5674] = (
    "Facções que vivem colecionando inimigos podem agir com truculência sem despertar a menor suspeita.",
    "rewritten",
    "Cálculo sociopolítico cínico sobre reputações violentas."
)
CURATIONS[5675] = (
    "Infiltrarei nas instalações da Tenba um pelotão disfarçado como membros da Tribo Teru para cometer atos de sabotagem.",
    "rewritten",
    "Operação de falsa bandeira orquestrada pela Igreja para acirrar a guerra."
)
CURATIONS[5676] = (
    "Bourd certamente virá correndo buscar o meu conselho.",
    "rewritten",
    "Previsão certeira do desespero de Bourd."
)
CURATIONS[5677] = (
    "Quando isso acontecer, bastará sugerir que ele execute a [Cantora das Estrelas], a fonte do poder mágico dos Teru.",
    "rewritten",
    "O veneno sussurrado aos ouvidos de Bourd visando a morte de Misha."
)
CURATIONS[5678] = (
    "Aquele fantoche simplório engolirá a isca num piscar de olhos e partirá para matá-la.",
    "rewritten",
    "Kyle tratando Bourd como mero títere descartável (あのデクの棒)."
)
CURATIONS[5679] = (
    "Com isso, a morte dela parecerá mero fruto da contenda bélica, e jamais uma eliminação estratégica para a ressurreição de Mir.",
    "rewritten",
    "A verdadeira motivação da trama desmascarada: abrir caminho para Mir sem levantar suspeitas."
)
CURATIONS[5680] = (
    "Muito embora as chances de um incompetente feito ele ser bem-sucedido não sejam lá muito altas...",
    "rewritten",
    "Ceticismo de Kyle quanto à competência militar de Bourd."
)
CURATIONS[5681] = (
    "Tratarei de conceber uma estratégia alternativa para remediar tal eventualidade.",
    "rewritten",
    "Prudência meticulosa do mentor da conspiração."
)
CURATIONS[5682] = (
    "Justo quando julgava não ter mais notícias de Bourd, recebi seu contato.",
    "rewritten",
    "Reviravolta na narrativa do diário com a mensagem de Bourd."
)
CURATIONS[5683] = (
    "Parece que fora atacado pela Tribo Teru no Vilarejo de Skuwat, onde estava aquartelado, e acabou ferido.",
    "rewritten",
    "Relato do massacre no Vilarejo de Skuwat onde a guarnição foi cercada."
)
CURATIONS[5684] = (
    "Segundo seu relato, ele concluiu o assassinato da Cantora das Estrelas, sendo emboscado durante a retirada.",
    "rewritten",
    "A farsa de Bourd alegando ter executado a Cantora das Estrelas antes de fugir."
)
CURATIONS[5685] = (
    "Para os padrões medíocres de Bourd, foi um feito impressionante.",
    "rewritten",
    "Sarcasmo de Kyle avaliando o resultado."
)
CURATIONS[5686] = (
    "Contudo, o vilarejo atacado e a guarnição lá aquartelada foram completamente dizimados.",
    "rewritten",
    "A dimensão trágica do genocídio em Skuwat registrada com frieza."
)
CURATIONS[5687] = (
    "A Tribo Teru é de fato implacável.",
    "rewritten",
    "Reconhecimento da fúria retaliatória da Tribo Teru."
)
CURATIONS[5688] = (
    "Não obstante, a aniquilação do vilarejo em nada interfere no meu plano; para mim, não faz a menor diferença.",
    "rewritten",
    "A crueldade aterradora de Falss desdenhando o massacre de inocentes."
)

# ==========================================
# EVENT 964: IDs 5689..5696 (Tutorial: Talk Topics / Matérias)
# ==========================================
CURATIONS[5689] = (
    "Os [Tópicos de Conversa] surgem em locais que chamam a atenção da heroína que acompanha você.",
    "rewritten",
    "Explicação clara e fluida sobre a mecânica de pontos de interesse das Reyvateils."
)
CURATIONS[5690] = (
    "Ao obtê-los, você poderá conversar sobre o assunto com ela em pousadas ou acampamentos mais tarde.",
    "rewritten",
    "Instrução funcional sobre as conversas íntimas durante o descanso."
)
CURATIONS[5691] = (
    "Por exemplo: se a heroína reparar em uma “estatueta de gato diante de uma loja”, um tópico surgirá ali.",
    "rewritten",
    "Exemplo prático de gatilho de tópico usando aspas tipográficas limpas."
)
CURATIONS[5692] = (
    "Ao reunir os tópicos e conversar, você poderá descobrir facetas surpreendentes da heroína.",
    "rewritten",
    "Aprofundamento psicológico e intimidade possibilitados pelas conversas."
)
CURATIONS[5693] = (
    "Com isso, os laços entre vocês se estreitarão passo a passo.",
    "rewritten",
    "Efeito mecânico e emocional do sistema de afinidade."
)
CURATIONS[5694] = (
    "Sempre que encontrar um tópico,\nnão hesite em pegá-lo!",
    "rewritten",
    "Recomendação prática enfática para o jogador."
)
CURATIONS[5695] = (
    "O tutorial [Sobre os Tópicos de Conversa] foi adicionado ao menu de Ajuda.",
    "rewritten",
    "Notificação do sistema sobre a nova entrada nos manuais do jogo."
)
CURATIONS[5696] = (
    "Esta instrução pode ser consultada\na qualquer momento pelo menu.",
    "rewritten",
    "Confirmação de acesso permanente via menu de ajuda."
)

# ==========================================
# EVENT 364: ID 5697 (Urgent Lyner)
# ==========================================
CURATIONS[5697] = (
    "Agora não temos tempo a perder com isso!",
    "rewritten",
    "Determinação assertiva de Lyner recusando distrações no momento crítico."
)

# ==========================================
# EVENT 27: IDs 5698..5705 (Combat with Jack / Fire Attack & Missile)
# ==========================================
CURATIONS[5698] = (
    "Muito bem, tudo pronto?!",
    "rewritten",
    "Jack conferindo a prontidão para o confronto bélico."
)
CURATIONS[5699] = (
    "Sim, quando quiser!",
    "rewritten",
    "Prontidão entusiasmada e corajosa de Lyner."
)
CURATIONS[5700] = (
    "Vou repetir mais uma vez: essa criatura\nsó sofre dano com [Ataque de Fogo]!",
    "rewritten",
    "Instrução tática vital de Jack com a propriedade elemental [Ataque de Fogo] (炎打撃)."
)
CURATIONS[5701] = (
    "Minha arma tem a propriedade de [Ataque de Fogo],\nentão funciona, mas a sua espada não serve pra nada.",
    "rewritten",
    "Jack diferenciando o efeito de seus disparos flamejantes das lâminas comuns."
)
CURATIONS[5702] = (
    "Use os [Mísseis] o máximo que puder durante a luta.",
    "rewritten",
    "Recomendação tática de Jack para o uso dos itens sintetizados [Mísseis] (メッソー)."
)
CURATIONS[5703] = (
    "Conseguimos!",
    "rewritten",
    "Celebração direta e vibrante de vitória de Jack."
)
CURATIONS[5704] = (
    "Sim... Agora vou ter a aeronave de volta!",
    "rewritten",
    "Alívio de Lyner por reconquistar a aeronave indispensável à jornada."
)
CURATIONS[5705] = (
    "Vamos, de volta para a [Floresta de Viola]!",
    "rewritten",
    "Toponímia canônica [Floresta de Viola] (ヴィオラ森) fixada no comando de partida."
)

# ==========================================
# EVENT 768: IDs 5706..5722 (Stonehenge Virtual World in Cosmosphere)
# ==========================================
CURATIONS[5706] = (
    "Pois é, rapaz! Deixe-me contar algo bem interessante.",
    "rewritten",
    "Tom fanfarrão e solene da entidade da Cosmosfera abordando Lyner."
)
CURATIONS[5707] = (
    "Agora que o coração da Aurica finalmente se conectou à Torre, tornou-se possível usar o poder dela para criar mundos que desafiam a realidade.",
    "rewritten",
    "Explicação mitológica sobre a ressonância da mente com os servidores da Torre."
)
CURATIONS[5708] = (
    "...Mundos que desafiam a realidade?\nDo que você está falando?",
    "rewritten",
    "Ceticismo curioso de Lyner ante a revelação inusitada."
)
CURATIONS[5709] = (
    "Um mundo desconectado do coração da Aurica...\nBem, por assim dizer, um mundo para pura diversão!",
    "rewritten",
    "Caracterização do mundo lúdico/virtual concebido pela mente de Aurica."
)
CURATIONS[5710] = (
    "Entendi...",
    "rewritten",
    "Compreensão cautelosa de Lyner."
)
CURATIONS[5711] = (
    "Sendo assim, pensei em abrir um portal para esse mundo bem aqui neste Stonehenge, que já cumpriu o seu propósito... O que me diz da ideia?",
    "rewritten",
    "Proposta arquitetônica no megalítico sagrado Stonehenge, alinhada com diálogos canônicos correlatos."
)
CURATIONS[5712] = (
    "Parece divertido.",
    "rewritten",
    "Adesão descomplicada e confiante de Lyner ao desafio."
)
CURATIONS[5713] = (
    "Ah, eu já sabia que diria isso! Esse é o meu rapaz!",
    "rewritten",
    "Aprovação entusiasmada da entidade mental ao espírito aventureiro de Lyner."
)
CURATIONS[5714] = (
    "Pois bem, como seria sem graça só abrir a passagem, vamos transformar isso em um jogo!",
    "rewritten",
    "Estabelecimento das regras da prova mental."
)
CURATIONS[5715] = (
    "Eu estabelecerei as condições de vitória neste mundo virtual. Se você as descobrir e triunfar com perfeição...",
    "rewritten",
    "Condições de vitória estipuladas no rito de desafio da Cosmosfera."
)
CURATIONS[5716] = (
    "...eu mesmo me submeterei à Aurica, tornando-me uma de suas magias!",
    "rewritten",
    "A recompensa mística: consagração da entidade como Song Magic a serviço de Aurica."
)
CURATIONS[5717] = (
    "Você era uma magia?!",
    "rewritten",
    "Espanto genuíno de Lyner com a verdadeira natureza daquela criatura."
)
CURATIONS[5718] = (
    "Chamar-me de “magia”... é uma definição um tanto imprecisa. Rigorosamente falando, sou quem rege o “mistério” no coração da Aurica... por assim dizer.",
    "rewritten",
    "Refinamento ontológico sobre o guardião do mistério interior na psique de Aurica."
)
CURATIONS[5719] = (
    "Mas detalhes teóricos pouco importam agora!\nVamos logo abrir esse portal!",
    "rewritten",
    "Impaciência cômica dispensando explicações filosóficas longas."
)
CURATIONS[5720] = (
    "E lá vai!!",
    "rewritten",
    "Grito festivo de conjuração abrindo o vórtice dimensional."
)
CURATIONS[5721] = (
    "Pronto! Basta mergulhar aqui para visitar o mundo virtual quando quiser. E, naturalmente, você poderá regressar a este lado a qualquer instante.",
    "rewritten",
    "Instrução funcional de trânsito entre o Stonehenge e a realidade alternativa."
)
CURATIONS[5722] = (
    "Sinta-se à vontade para vir quando bem entender!",
    "rewritten",
    "Despedida calorosa da entidade abrindo as portas do novo conteúdo lúdico."
)

# ==========================================
# EVENT 478: IDs 5723..5739 (Hangar / Airship ready & Krusche climbing)
# ==========================================
CURATIONS[5723] = (
    "Uau... A aeronave ficou pronta de verdade!",
    "rewritten",
    "Admiração sincera de Lyner ao contemplar a aeronave totalmente concluída no hangar."
)
CURATIONS[5724] = (
    "Sim, está em perfeitas condições de voo a qualquer hora.",
    "rewritten",
    "Relatório profissional e orgulhoso do mecânico da oficina."
)
CURATIONS[5725] = (
    "Maravilha! Então vamos partir agora mes...\nEspera aí, quem vai pilotar?",
    "rewritten",
    "Empolgação de Lyner subitamente freada pela constatação óbvia da falta de piloto."
)
CURATIONS[5726] = (
    "Você não pretendia levar a diretora Krusche?",
    "rewritten",
    "Mecânico lembrando do papel indispensável da diretora Krusche nos comandos de voo."
)
CURATIONS[5727] = (
    "Hã?! Bem, eu até tentei pedir...\nmas ela recusou na lata.",
    "rewritten",
    "Desabafo constrangido de Lyner sobre a recusa teimosa de Krusche."
)
CURATIONS[5728] = (
    "Ora, não me diga. Sendo assim,\nninguém vai conseguir tirar este navio do chão.",
    "rewritten",
    "Constatação fatalista sobre a dependência técnica das habilidades de Krusche."
)
CURATIONS[5729] = (
    "Ugh... Então vou ter que implorar de novo...?",
    "rewritten",
    "Lamento cômico de Lyner sabendo o trabalho que dá convencer a amiga de infância."
)
CURATIONS[5730] = (
    "Ela é uma mulher de fases, sabe...",
    "rewritten",
    "Observação bem-humorada sobre a personalidade volúvel e imprevisível de Krusche."
)
CURATIONS[5731] = (
    "Basta piscar que ela já sai voando por aí,\ne ninguém mais descobre onde ela foi parar.",
    "rewritten",
    "Descrição pitoresca dos sumiços repentinos da jovem mecânica prodígio."
)
CURATIONS[5732] = (
    "Pois é, exatamente isso...\nEla nem estava no aeroporto agora há pouco...",
    "rewritten",
    "Lyner confirmando a ausência de Krusche nas imediações do terminal aéreo."
)
CURATIONS[5733] = (
    "No aeroporto?\nMas a diretora Krusche não subiu a Torre?",
    "rewritten",
    "A revelação surpreendente do engenheiro apontando para a gigantesca estrutura da Torre."
)
CURATIONS[5734] = (
    "Hã?! A Torre?!",
    "rewritten",
    "Choque e perplexidade de Lyner com o arrojo de Krusche."
)
CURATIONS[5735] = (
    "Sim. Ela não tinha dito antes que queria subir?",
    "rewritten",
    "Mecânico relembrando as aspirações antigas de Krusche de alcançar o topo do mundo."
)
CURATIONS[5736] = (
    "Conhecendo a diretora, pensei que ela fosse subir junto de vocês.",
    "rewritten",
    "Suposição natural de que trabalhariam em equipe na grande escalada."
)
CURATIONS[5737] = (
    "A Krusche já está a caminho?!",
    "rewritten",
    "Urgência de Lyner percebendo que a companheira partiu em disparada na frente."
)
CURATIONS[5738] = (
    "Sim. Ela deduziu que vocês já haviam começado a escalada e deve estar subindo a todo vapor a esta hora...",
    "rewritten",
    "Explicação do mal-entendido hilário que levou Krusche a se adiantar sozinha."
)
CURATIONS[5739] = (
    "A Krusche já começou a subir a Torre na nossa frente! Vamos atrás dela!",
    "rewritten",
    "Convocação decidida de Lyner liderando o grupo no encalço de Krusche."
)

# ==========================================
# EVENT 621: IDs 5740..5753 (Misha's Cosmosphere Level 5 / School uniform)
# ==========================================
CURATIONS[5740] = (
    "Cheguei finalmente ao Nível 5...",
    "rewritten",
    "Marco de progressão psicológica de Lyner adentrando o Nível 5 da mente de Misha."
)
CURATIONS[5741] = (
    "Depois daquela balbúrdia violenta no nível anterior, imaginei que o mundo estaria em ruínas... mas parece surpreendentemente pacífico.",
    "rewritten",
    "Reflexão de Lyner contrastando a turbulência emocional do nível anterior com a serenidade aparente deste estrato."
)
CURATIONS[5742] = (
    "...L-Lyner...?\nO que você tá fazendo aqui?!",
    "rewritten",
    "Gaguejo envergonhado e surpresa fofa de Misha flagrada em seu refúgio escolar."
)
CURATIONS[5743] = (
    "...Misha?!",
    "approved_as_is",
    "Espanto recíproco de Lyner mantido perfeitamente."
)
CURATIONS[5744] = (
    "O que você tá fazendo aqui... Não, espera!\nPor que você tá vestida desse jeito...?!",
    "rewritten",
    "Lyner boquiaberto ao contemplar o uniforme colegial inesperado de Misha."
)
CURATIONS[5745] = (
    "...Ué? Mas a gente ainda é estudante, não é?\nEssa roupa... pra mim é a coisa mais normal do mundo...",
    "rewritten",
    "Lógica sonhadora de Misha justificando a vestimenta com a realidade paralela da Cosmosfera."
)
CURATIONS[5746] = (
    "É-É mesmo...? Mas por que você veio parar\nnum lugar desses? Isso é bem raro.",
    "rewritten",
    "Curiosidade de Lyner sondando os motivos da solidão de Misha naquele cenário."
)
CURATIONS[5747] = (
    "É que... eu não queria voltar pra casa...",
    "rewritten",
    "Confissão melancólica e vulnerável de Misha expressando seu refúgio emocional."
)
CURATIONS[5748] = (
    "...Entendi...",
    "rewritten",
    "Compaixão empática de Lyner compreendendo o peso do passado dela."
)
CURATIONS[5749] = (
    "(A Misha tem muito disso...)",
    "rewritten",
    "Monólogo interno carinhoso de Lyner reconhecendo as manias melancólicas da amiga."
)
CURATIONS[5750] = (
    "Os espinhos desapareceram por completo...",
    "rewritten",
    "Observação ambiental simbólica: as amarras e espinhos que afligiam Misha se dissiparam."
)
CURATIONS[5751] = (
    "......",
    "approved_as_is",
    "Pausa reflexiva contemplando o novo horizonte da psique."
)
CURATIONS[5752] = (
    "Hum...? Que prédio será aquele no centro?\nParece até uma miragem...",
    "rewritten",
    "Identificação de uma estrutura misteriosa translúcida no núcleo daquele estrato mental."
)
CURATIONS[5753] = (
    "Mas tirando isso, tudo parece normal. Dentre todos até agora, este é o mundo mais realista...",
    "rewritten",
    "Sensação de verossimilhança cotidiana que surpreende Lyner no mundo de Misha."
)

# ==========================================
# EVENT 736: IDs 5754..5781 (Aurica's Cosmosphere Level 5 / Bourd & Little Aurica)
# ==========================================
CURATIONS[5754] = (
    "E aí, menininha... Sabia que é perigoso andar\npor aí sozinha num lugar desses?",
    "rewritten",
    "Abordagem intimidadora e canhestra de Bourd (incorporado na mente) encurralando a pequena Aurica."
)
CURATIONS[5755] = (
    "Um tiozão malvado pode te levar embora e fazer tantas coisas terríveis com você... Hehehe...",
    "rewritten",
    "Ameaça caricata e sinistra de sequestro infantil representada nos medos da infância de Aurica."
)
CURATIONS[5756] = (
    "Bourd...?!",
    "rewritten",
    "Lyner reconhecendo o algoz da Tenba personificado no pesadelo de Aurica."
)
CURATIONS[5757] = (
    "...Tio... quem é você?",
    "rewritten",
    "A pureza amedrontada da pequena Aurica (Criança da Igreja) sem entender a crueldade do homem."
)
CURATIONS[5758] = (
    "Eu não sou um tio malvado, não! Sou só um tio bonzinho que tá com uma fominha danada.",
    "rewritten",
    "Cínica e patética tentativa de Bourd de posar de coitado faminto."
)
CURATIONS[5759] = (
    "Sendo assim, como a minha barriga tá roncando... que tal me emprestar um dinheirinho?",
    "rewritten",
    "Extorsão descarada exigindo dinheiro de uma criança indefesa."
)
CURATIONS[5760] = (
    "Mas... eu... não tenho dinheiro nenhum...",
    "rewritten",
    "Inocência da garotinha chorosa diante da ameaça."
)
CURATIONS[5761] = (
    "...O quê? Deixa de mentira! Pelo visto vou ter que te dar uma lição no couro pra você aprender!",
    "rewritten",
    "Explosão violenta e covarde de Bourd partindo para a agressão física (身体に教えないと)."
)
CURATIONS[5762] = (
    "Droga! Preciso salvá-la!",
    "rewritten",
    "Instinto heroico e protetor imediato de Lyner sacando a espada."
)
CURATIONS[5763] = (
    "Don Leon!! Me acodeee!!",
    "rewritten",
    "Grito desesperado da pequena Aurica clamando pelo seu boneco e guardião de pelúcia."
)
CURATIONS[5764] = (
    "Você está bem, Aurica?!",
    "rewritten",
    "A heroína Aurica adulta surgindo triunfante para resgatar sua versão infantil."
)
CURATIONS[5765] = (
    "Olha só, aquele tio malvado ali tava tentando me assaltar...",
    "rewritten",
    "A menininha denunciando o valentão para sua versão mais velha e forte."
)
CURATIONS[5766] = (
    "Então é você quem fica atormentando a Aurica?! Eu jamais vou te perdoar por isso!",
    "rewritten",
    "Fúria justa e protetora de Aurica defendendo sua própria criança interior ferida."
)
CURATIONS[5767] = (
    "Quem é você?! Veio se intrometer? Pois vou arrancar na marra de você também!",
    "rewritten",
    "Agressividade cega de Bourd atacando a heroína que se interpôs."
)
CURATIONS[5768] = (
    "Cai dentro!! Não vou deixar você encostar um dedo sequer na Aurica!",
    "rewritten",
    "Desafio destemido de Aurica assumindo a postura de muralha inquebrável."
)
CURATIONS[5769] = (
    "Toma isso! Yaaaah!!",
    "rewritten",
    "Grito de guerra furioso de Bourd desferindo seu golpe com tudo."
)
CURATIONS[5770] = (
    "O-O quê?! Uma barreira mágica?!",
    "rewritten",
    "Choque estupefato de Bourd tendo seu ataque ricocheteado pelo escudo espiritual de Aurica."
)
CURATIONS[5771] = (
    "Acabou o showzinho?! Então agora é a minha vez! Toma issoooo!!",
    "rewritten",
    "Contra-ataque vibrante e eletrizante de Aurica descarregando seu poder sonoro."
)
CURATIONS[5772] = (
    "Uwaaaaaahhh...!!",
    "rewritten",
    "Grito grotesco de derrota de Bourd sendo arremessado pelos ares."
)
CURATIONS[5773] = (
    "I-Incrível...",
    "rewritten",
    "Lyner boquiaberto diante da demonstração avassaladora de coragem e poder de Aurica."
)
CURATIONS[5774] = (
    "Aurica! Você se machucou?",
    "rewritten",
    "Carinho maternal e protetor de Aurica acolhendo sua essência de infância."
)
CURATIONS[5775] = (
    "Não... Muito obrigada, moça bonita!",
    "rewritten",
    "Gratidão luminosa e doce da garotinha à heroína protetora (おねえちゃん)."
)
CURATIONS[5776] = (
    "De nada! O cara malvado já era, não precisa mais ter medo.",
    "rewritten",
    "Conforto terno de Aurica curando os traumas e pavores do passado."
)
CURATIONS[5777] = (
    "Você é tão forte, moça! Eu quero ser uma garota corajosa e forte igualzinha a você!",
    "rewritten",
    "A reconciliação da psique: a criança interior aceitando o amadurecimento e a força de si mesma."
)
CURATIONS[5778] = (
    "Ufufu! Tenho certeza de que vai ser! Até logo, Aurica! Tchauzinho!",
    "rewritten",
    "Despedida afetuosa selando o pacto de autocura da heroína com sua história."
)
CURATIONS[5779] = (
    "Tchaaau!!",
    "rewritten",
    "Aceno infantil transbordando alegria e alívio renovados."
)
CURATIONS[5780] = (
    "...E aí, o que me diz dessa atuação triunfal da Aurica?",
    "rewritten",
    "Don Leon comovido e orgulhoso da superação moral e afetiva de sua protegida."
)
CURATIONS[5781] = (
    "Ao proteger a si mesma com bravura, Aurica\nteceu a Magia Vermelha [Erupção de Don Leon]!",
    "rewritten",
    "Consagração ritualística: tecer da magia canônica nascida da reconciliação com a própria força."
)

# ==========================================
# EVENT 421: ID 5782 (Aurica question)
# ==========================================
CURATIONS[5782] = (
    "Aonde você pensa que vai?!",
    "rewritten",
    "Bronca enérgica e possessiva de Aurica impedindo Lyner de se afastar."
)

# ==========================================
# EVENT 726: IDs 5783..5796 (School Rush Comedy / Late for class!)
# ==========================================
CURATIONS[5783] = (
    "Este lugar... parece uma escola.",
    "rewritten",
    "Lyner examinando o novo cenário que mimetiza um colégio moderno."
)
CURATIONS[5784] = (
    "Que tipo de mundo será desta vez?",
    "rewritten",
    "Curiosidade habitual de Lyner tentando decifrar o subtexto daquele devaneio."
)
CURATIONS[5785] = (
    "Ai caramba... Tô atrasada, muito atrasada!!",
    "rewritten",
    "Correria hilária clássica com Aurica afobada em pânico pelo horário escolar."
)
CURATIONS[5786] = (
    "Hum? Mas o que...?",
    "rewritten",
    "Lyner ouvindo passos apressados sem entender o que se aproxima."
)
CURATIONS[5787] = (
    "Aaaaaiii!!",
    "rewritten",
    "Colisão cômica e barulhenta com o herói."
)
CURATIONS[5788] = (
    "Ai, ai, ai...!",
    "rewritten",
    "Lyner massageando as dores após o encontrão violento."
)
CURATIONS[5789] = (
    "Olha por onde anda, seu idiota!\nEspera aí... Lyner?!",
    "rewritten",
    "Bravata típica seguida do susto ao reconhecer quem ela acabou de atropelar."
)
CURATIONS[5790] = (
    "A-Aurica...\nSuas roupas estão ficando cada vez mais extravagantes...",
    "rewritten",
    "Comentário tímido e atônito de Lyner sobre a ousadia estilística do uniforme de estudante (ぶっ飛んでいってる)."
)
CURATIONS[5791] = (
    "Do que você tá falando?! Se não andar logo, você também vai se atrasar pra aula! Anda! Rápido!",
    "rewritten",
    "Aurica puxando o protagonista para dentro da encenação colegial sem dar tempo para perguntas."
)
CURATIONS[5792] = (
    "E-Espera aí! Pra onde é que a gente tem que ir?!",
    "rewritten",
    "Desorientação total de Lyner sendo arrastado sem rumo."
)
CURATIONS[5793] = (
    "Pro colégio, né, óbvio!\nEu já tô indo na frente!",
    "rewritten",
    "Resposta óbvia e impaciente de Aurica disparando em corrida."
)
CURATIONS[5794] = (
    "Caramba, ferrou de vez...\nSe eu me atrasar hoje, vai ser o terceiro dia seguido...",
    "rewritten",
    "Monólogo de pânico de Aurica temendo as broncas disciplinares de atrasos consecutivos."
)
CURATIONS[5795] = (
    "Mas que mundo mais doido foram arranjar...\nBem, ao menos parece bem mais divertido que o anterior.",
    "rewritten",
    "Conclusão bem-humorada de Lyner achando graça na maluquice colegial criada pela mente de Aurica."
)
CURATIONS[5796] = (
    "...Você não aprende mesmo, né?\nPensa um pouco: por que diabos ela criaria um mundo desses?",
    "rewritten",
    "Don Leon provocando o senso crítico de Lyner sobre a carência afetiva e os desejos de normalidade por trás do delírio escolar."
)

# ==========================================
# EVENT 433: ID 5797 (Power Department / Setor de Força)
# ==========================================
CURATIONS[5797] = (
    "Não adianta nada eu ir para o setor de força agora...",
    "rewritten",
    "Alinhamento terminológico estrito com [setor de força] (動力部) descartando rotas irrelevantes."
)

# ==========================================
# EVENT 104: IDs 5798..5799 (Combat Mechanics / Ambience Field)
# ==========================================
CURATIONS[5798] = (
    "Se você não atacar aquele inimigo,\no [Campo de Ambiente] não vai se expandir!",
    "rewritten",
    "Instrução tática crucial de Misha fixando o conceito do HUD [Campo de Ambiente] (アンビエンスフィールド)."
)
CURATIONS[5799] = (
    "Ataque continuamente para expandi-lo\naté o ponto crítico de uma vez só!",
    "rewritten",
    "Comando de batalha para encadear golpes até atingir o ápice de ressonância fônica."
)

# ==========================================
# EVENT 807: IDs 5800..5803 (Childhood Vow & Reyvateil Mortality)
# ==========================================
CURATIONS[5800] = (
    "Este é o lugar onde prometemos ficar\njuntos para sempre... Onde juramos nunca nos separar...",
    "rewritten",
    "Memória comovente e lírica de infância de Lyner revivendo o juramento de união eterna."
)
CURATIONS[5801] = (
    "Eu nem sei quanto tempo de vida\nainda me resta...",
    "rewritten",
    "O drama trágico da finitude e mortalidade das Reyvateils ecoando na voz da jovem estudante."
)
CURATIONS[5802] = (
    "...!!",
    "approved_as_is",
    "O choque lancinante no coração de Lyner ao recordar a brevidade da vida de sua companheira."
)
CURATIONS[5803] = (
    "......",
    "approved_as_is",
    "Silêncio fúnebre e doloroso absorvendo o peso existencial daquela perda iminente."
)

# ==========================================
# EVENT 947: ID 5804 (Path block)
# ==========================================
CURATIONS[5804] = (
    "Não é hora de ir por este caminho...",
    "rewritten",
    "Recusa sóbria e focada de Lyner mantendo a rota da missão principal."
)

print(f"Total entries in CURATIONS: {len(CURATIONS)}")

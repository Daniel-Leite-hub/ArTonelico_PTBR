"""Script de Curadoria Editorial e Montagem do Bloco BLK_SYS_033
Ar tonelico: Melody of Elemia (Undub) - PS2
Framework: curadoria-editorial-game-localization v4.1.0
Eixo: AXIS_1 e AXIS_2 (Fichas Biográficas dos Protagonistas, Enciclopédia de Lore de Sol Ciel, Tutoriais de Combate, Menus e Grathmeld)
Linhas: 282 falas (IDs 29554 a 29835, SLUS/TEXT/0403 a 0416)
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))

from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line, validate_batch

INPUT_PATH = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_033_input.json"
OUTPUT_PATH = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_033_output.json"
CONFIG_PATH = BASE_DIR / "curadoria_editorial" / "curadoria_config.json"
DB_PATH = BASE_DIR / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj"

CURATED_DATA: dict[int, str] = {
    # =========================================================================
    # SLUS/TEXT/0403 (IDs 29554 a 29577): Perfis de Personagens (Lyner, Aurica, Misha, Jack, Krusche, Radolf)
    # =========================================================================
    29554: "Lyner Barsett",                   # cap=32B, enc=27B
    29555: "Masc.",                           # cap=16B, enc=11B
    29556: "Aventuras, Funbuns",              # cap=48B, enc=37B
    29557: "Vírus, traidores",                # cap=40B, enc=34B
    29558: "Vida mansa",                      # cap=40B, enc=23B
    29559: "Aurica Nestmile",                 # cap=32B, enc=31B
    29560: "Fem.",                            # cap=16B, enc=9B (resolvido overflow de Feminino)
    29561: "Trio de Elemia, canto",           # cap=48B, enc=43B
    29562: "Gente sem-vergonha, ruído",       # cap=56B, enc=54B
    29563: "Encontrar as deusas",             # cap=56B, enc=39B
    29564: "Misha Arsellec Lünn",             # cap=40B, enc=40B (canônico mestre)
    29565: "Cantar, livros, biscoitos",       # cap=56B, enc=51B
    29566: "Alturas, exercícios, Tenba",      # cap=56B, enc=53B
    29567: "Tornar-se esposa",                # cap=40B, enc=33B (およめさん)
    29568: "Jack Hamilton",                   # cap=32B, enc=27B
    29569: "Garotas, Viola Moon",             # cap=40B, enc=39B (resolvido overflow)
    29570: "Canalhas, Phebes",                # cap=48B, enc=33B
    29571: "Viajar além das nuvens",          # cap=48B, enc=46B (resolvido overflow, JP 雲平線の彼方への旅)
    29572: "Krusche Elendia",                 # cap=32B, enc=31B
    29573: "Tecnologia, Bala Felina",         # cap=56B, enc=47B (resolvido overflow, canônico Bala Felina)
    29574: "Brócolis",                        # cap=24B, enc=18B
    29575: "Cruzar a Blastline",              # cap=56B, enc=39B
    29576: "Radolf Schneider",                # cap=40B, enc=33B (canônico mestre)
    29577: "Sorrisos, prato Dodongo",         # cap=48B, enc=47B (resolvido overflow, JP 人の笑顔、ドドンゴ丼)

    # =========================================================================
    # SLUS/TEXT/0404 (IDs 29578 a 29601): Perfis (Radolf, Ayatane, Shurelia) e Crônica de Lyner
    # =========================================================================
    29578: "Destruidores, Tenba",             # cap=40B, enc=39B
    29579: "Trazer paz ao mundo",             # cap=56B, enc=39B
    29580: "Ayatane Michitaka",               # cap=40B, enc=35B
    29581: "Mundo virtual, cozinhar",         # cap=48B, enc=47B
    29582: "Tumulto, brigas",                 # cap=32B, enc=31B (resolvido overflow de Multidões, brigas)
    29583: "Shurelia",                        # cap=24B, enc=17B
    29584: "Humanos, Karaku",                 # cap=32B, enc=31B
    29585: "Vírus",                           # cap=16B, enc=12B
    29586: "Casamento e família comum",       # cap=64B, enc=52B
    29587: "Jovem Cavaleiro de Elemia e filho do comandante de Platina, protege Shurelia. Desceu às Asas de Horus para resgatar [Purger] e salvar Platina. Impetuoso e determinado, jamais desiste e trata as Reyvateils com profundo respeito.", # cap=488B, enc=446B
    29588: "Filho do comandante de Platina e Cavaleiro de Elemia, protege Shurelia. Desce às Asas de Horus para salvar Platina, mas é capturado por Bourd e pela Tenba. Precisa levar o Cristal Hymmnos [Purger] de volta com urgência máxima.", # cap=480B, enc=415B
    29589: "Filho do comandante de Platina e Cavaleiro de Elemia, protege Shurelia. Desceu às Asas de Horus para salvar Platina e, superando muitos percalços, finalmente obteve o Cristal [Purger]. Agora só precisa voltar para casa.", # cap=488B, enc=410B
    29590: "Filho do comandante de Platina e Cavaleiro de Elemia, protege Shurelia. Encontrou o Cristal [Purger], item crucial para salvar Platina, e retornou à cidade. Finalmente chegou a hora de contra-atacar os vírus com tudo.", # cap=448B, enc=405B
    29591: "Jovem Cavaleiro de Elemia que expulsou os vírus de Platina com o lendário [Purger]. Antes impulsivo e movido apenas por energia pura, amadureceu bastante após sua primeira jornada pelo desconhecido Mundo Inferior.", # cap=472B, enc=407B
    29592: "Jovem Cavaleiro de Elemia que expulsou os vírus com [Purger]. A crise não terminou, então parte com Misha em busca de sua canção perdida, Chronicle Key, roubada pela Tenba. Será que conseguirão encontrá-la?", # cap=488B, enc=394B
    29593: "Jovem Cavaleiro de Elemia que expulsou os vírus com [Purger]. Recuperou o Hino Chronicle Key roubado pela Tenba e impediu que o mundo ruísse. Mesmo levando broncas de Misha, amadurece a passos largos.", # cap=496B, enc=384B
    29594: "Jovem Cavaleiro de Elemia que expulsou os vírus com [Purger]. Ajuda Aurica e a Igreja a buscar o Cristal [Linker], retribuindo o apoio recebido. Além da gratidão, deseja realizar o sonho de Aurica de se tornar Donzela.", # cap=472B, enc=428B
    29595: "Jovem Cavaleiro de Elemia que repeliu os vírus com [Purger]. Encontrou [Linker] com Aurica e virou herói lendário. Percebeu que seu papel é apoiá-la de coração e ficar a seu lado, crescendo como pessoa.", # cap=472B, enc=398B
    29596: "Jovem Cavaleiro de Elemia. Amadureceu muito superando a invasão viral de Platina e o retorno de Mir. Continua louco por Funbuns e sendo alvo de piadas, mas assumiu plenamente o papel de líder do grupo.", # cap=472B, enc=393B
    29597: "Cavaleiro de Elemia e o mais confiável para Shurelia, lendário por trazer a paz. Com ela em suspensão, não consegue pensar em outra coisa a não ser salvá-la, recusando-se a aceitar esse trágico destino.", # cap=456B, enc=391B
    29598: "Cavaleiro de Elemia. Despertou Shurelia sabendo que Mir também reviveria. Apesar de levar broncas, aprendeu a defender suas convicções. Como fazer para que todas as vidas sejam felizes sem sacrificar ninguém?", # cap=440B, enc=416B
    29599: "Líder que pacificou o mundo. Compreendeu a dor e o passado de Mir, acolhendo os vírus e lutando pelo que acredita. Há um abismo entre sua glória heroica e seu jeito desajeitado, mas essa é sua essência.", # cap=496B, enc=396B
    29600: "A garota que me ajudou (acho...) nas Asas de Horus. Parecia sempre tão triste... Bem, não tenho mais o que escrever sobre ela, tirando o fato de que a achei bem fofa.", # cap=368B, enc=363B
    29601: "A garota que me ajudou nas Asas de Horus. Fazia tempo que não a via e quase foi atirada da nave por Bourd. Será que nasceu com o azar colado nela?! Nossas conversas nunca fluem bem, mas vamos viajar juntos.", # cap=488B, enc=404B

    # =========================================================================
    # SLUS/TEXT/0405 (IDs 29602 a 29625): Crônicas de Aurica, Misha, Shurelia, Radolf, Jack e Krusche
    # =========================================================================
    29602: "Quem salvou minha vida nas Asas de Horus. É Reyvateil da Igreja, chamada Donzela. Por falta de talento, ficou rotulada como Classe D e não tem parceiro. Agora conversa mais comigo, o que me deixa bem aliviado.", # cap=496B, enc=400B
    29603: "Candidata a Donzela Sagrada de Elemia. Parecia sombria a princípio, mas na verdade tem um coração caloroso e sorri mais agora. Seu senso para inventar nomes e sua culinária são inacreditáveis... em vários sentidos.", # cap=488B, enc=417B
    29604: "Candidata da Igreja que virou a Donzela Sagrada oficial após resgatarmos o Cristal [Linker]. Nem ela acreditava que conseguiria. Anda cheia de vida ultimamente! Deve ser o verdadeiro jeito de ser da Aurica.", # cap=480B, enc=396B
    29605: "Donzela Sagrada da Igreja. Quase virou sacrifício no plano de Falss, mas a resgatei a tempo. Temi que ficasse deprimida de novo, porém está surpreendentemente serena. Só quero ficar a seu lado e apoiá-la.", # cap=480B, enc=390B
    29606: "Aurica veio morar em Platina por uma reviravolta do destino e estou bem feliz com isso. Só queria que desse uma trégua no ataque diário de culinária autoral... Mas vendo o sorriso dela, devoro qualquer coisa.", # cap=496B, enc=398B
    29607: "Alguém insubstituível para mim. Nosso encontro nas Asas de Horus foi destino. Ela sofreu com azares e preconceito, mas agora quero trazer felicidade para sua vida. Obrigado por me encontrar. Vamos ficar juntos.", # cap=480B, enc=400B
    29608: "Surgiu de repente na minha frente. É uma Reyvateil da Tenba, mas aprisionada, não funcionária. Sabia muito do meu passado e ficou em choque por eu não lembrar de nada. É decidida e fala tudo o que pensa.", # cap=480B, enc=384B
    29609: "Sabe tudo do meu passado. Mesmo cativa da Tenba, enfrentou Bourd e planejou fugas. Eu a achava durona, mas me surpreendi ao vê-la chorar em Silvaplate. Ter medo de altura neste mundo deve ser um fardo.", # cap=416B, enc=397B
    29610: "Sabe muito sobre mim. Passou por muito sofrimento presa na Tenba e teve conversas enigmáticas em Em Pheyna. Apesar de tudo, é uma garota comum no fundo. Me dói não conseguir lembrar do nosso passado juntos.", # cap=464B, enc=396B
    29611: "Carrega o fardo cruel de ser a Cantora das Estrelas para selar Mir e proteger o mundo. Eu nem imaginava o tamanho dessa sina... Enfrentou essa solidão por anos a fio. O que posso fazer para aliviar seu peso?", # cap=464B, enc=399B
    29612: "Misha carrega o dever de selar Mir. Recuperamos o Hino Chronicle Key e ela voltou ao seu belo corpo curvilíneo. Ainda fico meio sem jeito perto dela agora... Mas ela terá que cantar na Crônica Crescente.", # cap=456B, enc=397B
    29613: "Misha, a Cantora das Estrelas. Shurelia a tirou da Crônica Crescente, concedendo-lhe uma folga do fardo. Fico feliz em viajar com ela de novo. Mesmo com o corpo adulto, continua a mesma garota de antigamente.", # cap=472B, enc=401B
    29614: "Sem Mir, Misha deixou de ser Cantora das Estrelas e veio morar na sua terra natal, Platina. Como não pôde brincar na infância, me arrasta para lojas de departamento todo santo dia. Mais exaustivo que aventuras!", # cap=472B, enc=417B
    29615: "Alguém insubstituível na minha vida. Mesmo quando a esqueci, Misha sempre pensou em mim e confiou em mim. Chegou a hora de cumprir a promessa de infância e fazê-la feliz. Obrigado por tudo. Estarei sempre com você.", # cap=504B, enc=403B
    29616: "Minha mestra e administradora da Torre. Inabalável e corajosa, vigia o mundo inteiro para protegê-lo com dedicação total. Foi vendo sua postura que aprendi a ter senso de dever. Sob a armadura, é linda e delicada.", # cap=496B, enc=418B
    29617: "Minha mestra e administradora da Torre. Descobri que é bem desastrada, o que me dá uma simpatia enorme por ela, além de amar coelhos. Mas cá entre nós, o senso estético dela rivaliza com o da Aurica...", # cap=448B, enc=384B
    29618: "Minha mestra e alguém insubstituível para mim. Descobri que ela também é uma garota comum: é desastrada, sem rumo, implacável na luta mas tímida a sós comigo. Shurelia dá o seu melhor todos os dias.", # cap=424B, enc=387B
    29619: "Cardeal da Igreja de Elemia. Meio formal, mas caloroso e gentil com os subordinados. Trata as Reyvateils com profundo respeito, detestando os abusos da Tenba. Achei que fosse parceiro de Aurica, mas me enganei.", # cap=464B, enc=406B
    29620: "Cardeal-regente da Igreja de Elemia. Acredita que a fé deve servir ao povo, discordando do Bispo Falss, focado apenas no Advento das Deusas. Parecia rígido, mas virou um grande irmão mais velho em quem posso confiar.", # cap=464B, enc=428B
    29621: "Radolf virou o Cardeal-Bispo da Igreja de Elemia, trabalhando duro para colocá-la a serviço dos necessitados. Comeu o pão que o diabo amassou, mas foi reconhecido. Com ele, a Igreja e o mundo estão em boas mãos.", # cap=472B, enc=414B
    29622: "Pistoleiro errante com uma arma implantada no braço para lutar como mercenário. Nosso começo foi péssimo porque tentou roubar peças da minha aeronave! Mas suas habilidades de caçador de tesouros são muito úteis.", # cap=472B, enc=414B
    29623: "Pistoleiro que salvou minha vida na Colina do Canto. Para minha surpresa, é da Tribo Teru e era como um irmão para Misha. O mundo é pequeno! Continua namorador incorrigível, mas é um homem de ação e palavra.", # cap=464B, enc=400B
    29624: "Pistoleiro solitário que já nem anda tão solitário assim. Ele viajava para resgatar Misha da Tenba, então já cumpriu sua meta. Notei que ele tem sentimentos por Krusche, e não é só para se livrar das dívidas!", # cap=464B, enc=404B
    29625: "Engenheira do Beco Vagalume. Baixinha, mas luta com uma motosserra pesada e invadiu a Tenba sem pestanejar. Ama aeronaves acima de tudo e aprendeu Grathmeld só para construí-las. Não liga muito para vaidades.", # cap=464B, enc=400B

    # =========================================================================
    # SLUS/TEXT/0406 (IDs 29626 a 29636): Perfis (Krusche, Ayatane) e Comandos de Menu UI
    # =========================================================================
    29626: "Engenheira do Beco Vagalume. Jack lhe deve uma fortuna! Tem língua afiada e fala tudo na lata, sem a menor delicadeza. Vive trocando farpas cômicas com Misha, mas as duas se entendem muito bem.", # cap=504B, enc=384B
    29627: "Engenheira do Beco Vagalume. Reparou minha nave e cruzou a Blastline comigo, mas agora sonha em cruzá-la de novo numa aeronave própria. Engenheira nata, embora confesse que já se vestiu com vaidade por amor.", # cap=448B, enc=409B
    29628: "Cavaleiro de Elemia que se alistou comigo, um ano mais velho e como um irmão. Atencioso e benquisto por todos, mantém a calma plena enfrentando vírus comigo e com Shurelia. Seu passatempo favorito é cozinhar.", # cap=488B, enc=406B
    29629: "Cavaleiro de Elemia e, na verdade, uma forma de vida viral gerada por Mir. Mas Ayatane continua sendo o mesmo Ayatane de sempre. Há humanos crueis no mundo; ser vírus não o faz mau. É meu melhor amigo para sempre.", # cap=468B, enc=419B
    29630: "Personagem IM06 OKIM00 VoltarIM01", # cap=80B, enc=75B
    29631: "Trocar PersonagemIM05 PáginaIM03 VoltarIM01", # cap=88B, enc=88B
    29632: "CategoriaIM05 ItemIM04 Mudar PáginaIM03 VoltarIM01", # cap=112B, enc=97B
    29633: "CategoriaIM05 ItemIM04 Mudar PáginaIM03 ConfirmarIM00 VoltarIM01", # cap=136B, enc=129B
    29634: "CategoriaIM05 ItemIM04 VoltarIM01",    # cap=88B, enc=69B
    29635: "CategoriaIM05 VoltarIM01",            # cap=52B, enc=49B
    29636: "Deseja usar?",                        # cap=40B, enc=25B

    # =========================================================================
    # SLUS/TEXT/0407 (IDs 29637 a 29651): Notificações de Itens e Categorias de Equipamento
    # =========================================================================
    29637: "Item obtido: [%s]",                   # cap=40B, enc=35B
    29638: "Equip. [Acess.]",                     # cap=40B, enc=31B
    29639: "Equip. [Armad.]",                     # cap=32B, enc=31B (resolvido overflow)
    29640: "Evento",                              # cap=16B, enc=13B
    29641: "Material [Coleta]",                   # cap=40B, enc=35B
    29642: "Material [Síntese]",                  # cap=48B, enc=38B
    29643: "Usar %s",                             # cap=16B, enc=15B (resolvido overflow)
    29644: "Equip. [Arma]",                       # cap=32B, enc=27B
    29645: "Cristal Grathnode",                   # cap=40B, enc=35B
    29646: "Cura",                                # cap=16B, enc=9B
    29647: "Só Reyvateil",                        # cap=40B, enc=27B
    29648: "Ataque",                              # cap=16B, enc=13B
    29649: "Ataque de apoio",                     # cap=32B, enc=31B
    29650: "Campo",                               # cap=16B, enc=11B
    29651: "Carta",                               # cap=12B, enc=11B

    # =========================================================================
    # SLUS/TEXT/0408 (IDs 29652 a 29663): Rótulos de Cartas e Enciclopédia
    # =========================================================================
    29652: "Syn-C",                               # cap=16B, enc=11B
    29653: "Rec.",                                # cap=16B, enc=9B
    29654: "Efeito uso",                       # cap=24B, enc=23B
    29655: "Efeito de equip.",                    # cap=40B, enc=35B
    29656: "Item",                                # cap=16B, enc=9B
    29657: "Monstro",                             # cap=16B, enc=15B
    29658: "Pessoa",                              # cap=16B, enc=13B
    29659: "Segredo",                             # cap=16B, enc=15B
    29660: "Qual carta deseja ver? VoltarIM01",   # cap=80B, enc=65B
    29661: "(Vazio)",                             # cap=16B, enc=15B (resolvido overflow de (Nenhum))
    29662: "Origem",                              # cap=24B, enc=13B
    29663: "Itens de drop",                       # cap=28B, enc=27B

    # =========================================================================
    # SLUS/TEXT/0409 (IDs 29664 a 29667): Comandos de Formação e Seleção de UI
    # =========================================================================
    29664: "Escolha o personagem IM06 ConfirmarIM00 VoltarIM01", # cap=112B, enc=97B
    29665: "Escolha quem substituir IM06 ConfirmarIM00 VoltarIM01", # cap=128B, enc=105B
    29666: "Escolha a Reyvateil IM06 ConfirmarIM00 VoltarIM01", # cap=112B, enc=97B
    29667: "Escolha a Magia da Canção IM06 ConfirmarIM00 VoltarIM01", # cap=112B, enc=107B

    # =========================================================================
    # SLUS/TEXT/0410 (IDs 29668 a 29691): Comandos e Tutoriais (Analisador, Encontros, Aprimorar, Grathmeld)
    # =========================================================================
    29668: "Usar em todos IM06 ConfirmarIM00 VoltarIM01", # cap=96B, enc=85B
    29669: "Escolha o multiplicador IM05 ConfirmarIM00 VoltarIM01", # cap=120B, enc=107B
    29670: "O Analisador foi ativado.CRAté sair da masmorra, todos os pontos destrutíveis ficarão marcados no mapa.", # cap=212B, enc=205B
    29671: "Encontros",                           # cap=24B, enc=19B
    29672: "Nas áreas onde inimigos aparecem, o medidor de encontros é exibido no canto inferior direito da tela.", # cap=216B, enc=207B
    29673: "Ao caminhar, a cor do medidor muda: quanto mais próxima do vermelho, maior a chance de inimigos surgirem. Mesmo perto do azul, batalhas ainda podem ocorrer. Não baixe a guarda!", # cap=432B, enc=343B
    29674: "Quando a batalha termina após derrotar os inimigos ou fugir, o medidor de encontros diminui. Ao chegar a zero, nenhum monstro aparecerá mais, por mais que você explore a área.", # cap=384B, enc=342B
    29675: "O medidor de encontros é exclusivo de cada área. Mudar de área ou sair para o mapa-múndi faz o medidor se restaurar. Use isso estrategicamente para subir de nível.", # cap=344B, enc=330B
    29676: "Aprimorar",                           # cap=24B, enc=19B (resolvido overflow de Aprimoramento)
    29677: "Use Cristais Grathnode obtidos em lojas ou batalhas para aprimorar seus equipamentos. No menu 'Equipamento', selecione a peça desejada e escolha 'Aprimorar'.", # cap=352B, enc=323B
    29678: "Cada peça de equipamento comporta até 4 Cristais Grathnode. Os efeitos dos cristais são aplicados diretamente, mas cristais com efeitos idênticos não se acumulam.", # cap=352B, enc=333B
    29679: "Cristais Grathnode de nível alto possuem restrições de encaixe: você não pode instalar um cristal em um espaço cujo nível seja inferior ao do próprio cristal.", # cap=352B, enc=329B
    29680: "Com o aprimoramento, o ataque do grupo aumentará muito. Combine cristais e monte suas próprias configurações de combate.", # cap=304B, enc=303B
    29681: "Grathmeld",                           # cap=24B, enc=19B
    29682: "Grathmeld pode ser acessado no menu da pousada ou acampamento.", # cap=128B, enc=125B (resolvido overflow)
    29683: "Ao escolher o item que deseja criar, os ingredientes da síntese serão exibidos. A qualidade dos ingredientes determina a qualidade final do item criado. Alguns itens também usam Cristais Grathnode como material.", # cap=488B, enc=425B
    29684: "Em seguida, defina a quantidade que deseja produzir. Ao confirmar tudo, a síntese começará imediatamente.", # cap=224B, enc=205B
    29685: "Tudo pronto! O item sintetizado será adicionado à lista de itens no menu principal.", # cap=192B, enc=173B
    29686: "Ao criar itens com qualidades diferentes, escolha qual qualidade deseja manter.", # cap=200B, enc=195B
    29687: "Se escolher 'Combinar', a nova quantia se somará à anterior. Porém, a qualidade será calculada pela média; tome cuidado caso queira preservar um item de alta qualidade.", # cap=376B, enc=342B
    29688: "Sem os ingredientes necessários, o Grathmeld não poderá ser realizado. Com ele, você cria itens muito mais poderosos do que os vendidos nas lojas. Domine essa arte e sua jornada será bem mais tranquila!", # cap=448B, enc=408B
    29689: "Receitas",                            # cap=24B, enc=17B (resolvido overflow de Carta de receita)
    29690: "Para criar um item via Grathmeld, é preciso conhecer sua receita. Você aprende novas receitas obtendo suas respectivas Cartas de Receita.", # cap=288B, enc=264B
    29691: "Cartas de Receita podem ser encontradas em lojas, baús da Torre e eventos. Mesmo que nunca tenha possuído o item, conhecer a receita já o registra no catálogo de itens.", # cap=384B, enc=339B

    # =========================================================================
    # SLUS/TEXT/0411 (IDs 29692 a 29715): Tutoriais de Combate (Campo Ambiente, Harmonics, Magias)
    # =========================================================================
    29692: "Algumas receitas ensinam a criar itens raríssimos, impossíveis de comprar em lojas. Procure o máximo de receitas que puder: elas serão vitais para avançar na sua jornada!", # cap=384B, enc=343B
    29693: "Campo Ambiente",                      # cap=32B, enc=29B
    29694: "O indicador sobre o alvo em combate é o Campo Ambiente. Ele atua como um ressonador para amplificar a Magia da Canção.", # cap=288B, enc=282B
    29695: "O Campo Ambiente sobe de nível ao causar dano com golpes e perícias.", # cap=160B, enc=158B
    29696: "Ao acertar ataques contínuos, o nível sobe até o máximo de 3, mas decai com o passar do tempo. Procure ativar a Magia da Canção quando o nível estiver no auge!", # cap=352B, enc=319B
    29697: "A potência da Magia da Canção cresce bastante com o nível do Campo Ambiente. Combinando-o ao medidor Burst, é possível desferir um golpe fatal arrasador!", # cap=312B, enc=308B
    29698: "Harmonics",                           # cap=24B, enc=19B
    29699: "Quando uma Reyvateil luta, uma barra surge na base da tela: o Harmonics.", # cap=208B, enc=205B
    29700: "O medidor Harmonics cresce com o entusiasmo mútuo. A barra azul reflete o ânimo do grupo na vanguarda; a vermelha, o da Reyvateil.", # cap=336B, enc=333B
    29701: "Atacar os inimigos faz a barra azul subir; sofrer golpes a faz cair. Já a barra vermelha da Reyvateil cresce de forma contínua com o passar do tempo.", # cap=408B, enc=297B
    29702: "Se a Reyvateil sofrer ataques, a barra vermelha cairá. Caso ela seja nocauteada, o Harmonics desaparecerá por completo. Fique atento!", # cap=280B, enc=261B
    29703: "Quando o Harmonics sobe de nível, a luz no canto inferior esquerdo se acende. Cada nível aumenta o ataque de Lyner e aprimora suas técnicas de combate.", # cap=328B, enc=309B
    29704: "Por padrão, o Harmonics vai até o nível 1. Ao disparar Magia Vermelha e expandir o medidor limite, você poderá alcançar os níveis 2 e 3.", # cap=304B, enc=282B
    29705: "Dominar o Harmonics será uma de suas maiores vantagens táticas em combate!", # cap=152B, enc=141B
    29706: "Magia da Canção em combate",          # cap=56B, enc=53B
    29707: "Durante o combate, aperte IM03 para abrir os comandos da Reyvateil. Como não empunha armas, seu único meio de ataque é a Magia da Canção.", # cap=312B, enc=285B
    29708: "Ao selecionar Magia Vermelha, a Reyvateil consumirá MP até a ativação, elevando o medidor Burst. A velocidade e o traje usado influenciam o ganho de carga.", # cap=328B, enc=317B
    29709: "Ao atingir determinados limites de carga, a Magia da Canção sobe de nível, alterando força e efeito. Conforme seu laço com a Reyvateil se aprofunda, será possível personalizar ainda mais cada nível.", # cap=464B, enc=394B
    29710: "Pressione IM03 novamente para abrir o menu da Reyvateil. O comando de seleção terá mudado para 'Ativar'. Escolha o alvo e dispare!", # cap=312B, enc=259B
    29711: "A Magia da Canção atinge os inimigos com fúria. Quanto maior o medidor Burst, mais forte ela será. Acumule carga para o golpe fatal!", # cap=336B, enc=332B
    29712: "Magia Azul",                          # cap=24B, enc=21B
    29713: "Os cantos não servem só para atacar. As canções que curam o grupo e elevam seus atributos são a Magia Azul.", # cap=272B, enc=268B
    29714: "Diferente da vermelha, a Magia Azul age no instante em que o canto começa. A entidade invocada pela canção curará e protegerá os aliados continuamente.", # cap=312B, enc=306B
    29715: "Quanto mais o canto se prolonga, mais forte se torna o efeito da Magia Azul. Se desejar interrompê-la, selecione 'Parar Canção'. Alterne as magias conforme as fraquezas dos monstros!", # cap=384B, enc=356B

    # =========================================================================
    # SLUS/TEXT/0412 (IDs 29716 a 29739): Tutoriais de Inserção, Tranquility, Cosmosfera e DP
    # =========================================================================
    29716: "Inserir",                             # cap=16B, enc=15B (resolvido overflow de Instalar)
    29717: "A instalação aprimora a Magia da Canção unindo os poderes de um Cristal Grathnode ao canto. O procedimento pode ser realizado no menu de pousadas ou acampamentos.", # cap=328B, enc=327B
    29718: "Cada Magia da Canção aceita até 4 Cristais Grathnode, conforme o nível dos espaços disponíveis. Instalar múltiplos cristais com o mesmo efeito concederá apenas o bônus de um deles.", # cap=400B, enc=356B
    29719: "Para que um Cristal Grathnode manifeste seu poder, a Magia da Canção precisa atingir o nível correspondente. Um cristal de nível 4 só terá efeito quando a canção alcançar o nível 4 de carga. Planeje bem suas combinações de instalação!", # cap=536B, enc=452B
    29720: "Mais Cristais Grathnode instalados aumentam o gasto de MP. Fique atento ao consumo ao fortalecer suas canções.", # cap=248B, enc=241B
    29721: "Tranquility",                         # cap=24B, enc=23B (resolvido overflow de Tranquilidade)
    29722: "O MP da Reyvateil costuma se regenerar sozinho, mas decai sem parar enquanto ela entoa uma Magia da Canção. Se o MP esgotar antes da ativação, a magia explodirá fora de controle!", # cap=392B, enc=349B
    29723: "Tranquility recupera o MP da Reyvateil em batalha.", # cap=128B, enc=99B
    29724: "Com pouco MP, a Reyvateil ficará tonta e vacilante. Se quiser manter o canto ativo e amplificar ainda mais o dano, use Tranquility para restaurar suas forças.", # cap=344B, enc=318B
    29725: "Tranquility pode ser criado via Grathmeld. Tenha estoques para a Reyvateil. Ingredientes: Pedras da Canção e Cristais Grathnode.", # cap=296B, enc=286B
    29726: "Merg.",                               # cap=16B, enc=11B
    29727: "O DP das lutas serve para os Mergulhos. Mergulhar na Cosmosfera da Reyvateil desperta seus verdadeiros poderes.", # cap=264B, enc=259B (canônico Cosmosfera)
    29728: "Na Cosmosfera, toda Reyvateil abriga Guardiãs da Mente. Elas protegem seu coração e zelam pelo seu amadurecimento.", # cap=288B, enc=277B (canônico Cosmosfera)
    29729: "Guiado por essas guardiãs, Lyner desbravará as profundezas da Cosmosfera.", # cap=152B, enc=143B
    29730: "A Cosmosfera reflete os anseios e terrores mais íntimos adormecidos no coração da donzela. Um universo impossível se abre, completamente distinto da realidade.", # cap=328B, enc=324B (canônico Cosmosfera)
    29731: "Os eventos na Cosmosfera dependem do DP. O DP representa o vínculo de confiança mútua. Com DP suficiente, ela abrirá o coração e revelará uma nova faceta de si.", # cap=360B, enc=325B (canônico Cosmosfera)
    29732: "Contudo, sem DP suficiente, você será expulso da Cosmosfera. Antes de mergulhar, certifique-se de acumular uma boa reserva de pontos.", # cap=312B, enc=265B (canônico Cosmosfera)
    29733: "Ao superar eventos na Cosmosfera, a Reyvateil pode tecer uma nova canção. Todas as magias usadas em combate e exploração são forjadas nesse mundo mental.", # cap=352B, enc=306B (canônico Cosmosfera)
    29734: "Canções fortes provam a confiança da Reyvateil em você. Mergulhe fundo!", # cap=160B, enc=155B
    29735: "Em certos pontos da história, o Mergulho será obrigatório para avançar. O destino do mundo depende diretamente dos laços cultivados na Cosmosfera.", # cap=384B, enc=301B (canônico Cosmosfera)
    29736: "Pontos DP",                           # cap=24B, enc=19B (resolvido overflow de Ponto de Mergulho)
    29737: "DP (Pontos de Mergulho) são indispensáveis nos eventos da Cosmosfera. Você os adquire após cada vitória em batalha, junto de experiência e dinheiro.", # cap=312B, enc=296B (canônico Cosmosfera)
    29738: "O ganho de DP é calculado pelo número de aliados, o maior dano causado e o valor máximo do medidor Burst na ativação de uma Magia da Canção durante o embate.", # cap=344B, enc=325B
    29739: "Na Magia Vermelha, se a luta acabar antes do disparo, o Burst acumulado não contará no DP. Cuidado!", # cap=224B, enc=219B

    # =========================================================================
    # SLUS/TEXT/0413 (IDs 29740 a 29763): Tutoriais de Magia Verde, Trajes, Golpe Carregado e Pousada
    # =========================================================================
    29740: "Cada Reyvateil no grupo acumula seu próprio DP, que será consumido individualmente ao mergulhar em sua Cosmosfera.", # cap=248B, enc=229B (canônico Cosmosfera)
    29741: "Magia Verde",                         # cap=24B, enc=23B
    29742: "A Magia Verde só pode ser utilizada no cenário de exploração. Pressione IM02 para dispará-la.", # cap=224B, enc=189B
    29743: "Certas paredes e portas trancadas podem ser rompidas com Magia Verde. Dispare repetidas vezes para reduzir sua durabilidade e destruí-las, abrindo novas passagens.", # cap=344B, enc=335B
    29744: "Ao aprender novas magias verdes, alterne entre elas com IM22 e IM23. Existem portas vulneráveis apenas a certos elementos; teste diferentes magias em locais suspeitos!", # cap=376B, enc=340B
    29745: "Além de portas, muitos objetos reagem ou se quebram com a Magia Verde. Ao notar algo suspeito, atire contra ele!", # cap=280B, enc=278B
    29746: "Traje",                               # cap=16B, enc=11B
    29747: "A troca de trajes é feita em 'Equipamento'. Entre na tela da Reyvateil para encontrar a seção exclusiva de trajes.", # cap=272B, enc=268B
    29748: "Cada traje altera atributos da Reyvateil. Escolha pelo visual ou pelos efeitos em combate: a decisão é sua!", # cap=264B, enc=257B
    29749: "Novos trajes são obtidos ao superar eventos na Cosmosfera. Se deseja colecionar todas as vestimentas, explore cada recanto do mundo interior das donzelas!", # cap=312B, enc=306B (canônico Cosmosfera)
    29750: "Os trajes também aparecem nas lutas. Trocá-los deixará os confrontos mais vantajosos e bem mais divertidos!", # cap=240B, enc=223B
    29751: "Termos:CRVariação de Burst: velocidade de carga da canção nesse nível. Linha mais alta indica carga mais rápida.CRGD-REGIST: taxa de alívio do consumo de MP no canto. A 100%, gasta metade do MP.", # cap=560B, enc=364B
    29752: "Golpe Carregado",                     # cap=32B, enc=31B (resolvido overflow de Ataque armazenado)
    29753: "Normalmente os inimigos atacam só a vanguarda. A menos que todos os aliados caiam nocauteados, a Reyvateil não sofrerá dano.", # cap=320B, enc=318B
    29754: "Porém, há investidas que miram só a Reyvateil: os golpes carregados. Quando um inimigo inicia a técnica, uma mira surge ao redor dela.", # cap=352B, enc=346B
    29755: "Ao sofrer um golpe carregado, o medidor Burst da Reyvateil é reduzido na proporção do dano sofrido. Se ela for nocauteada, o valor do medidor despencará de volta a 0%!", # cap=352B, enc=324B
    29756: "Para contê-los, use 'Proteger'. Durante o carregamento da investida, essa opção surgirá nos comandos.", # cap=240B, enc=239B
    29757: "Ao escolher 'Proteger', o aliado intercepta o golpe pela Reyvateil. O defensor sofrerá todo o dano do ataque em seu lugar!", # cap=328B, enc=327B
    29758: "Proteger traz grandes vantagens táticas: uma defesa bem-sucedida permite um contra-ataque imediato sobre o agressor, agindo instantaneamente fora da ordem de turnos!", # cap=352B, enc=332B
    29759: "Há golpes carregados de níveis 2 e 3. Para bloqueá-los, é preciso que o mesmo número de aliados use 'Proteger' em conjunto.", # cap=320B, enc=319B
    29760: "O efeito de 'Proteger' dura uma rodada. Use o comando no momento em que a investida estiver prestes a disparar.", # cap=264B, enc=249B
    29761: "Defender com sucesso faz o Harmonics disparar! Fortaleça seus laços com a Reyvateil e alcance a vitória!", # cap=240B, enc=223B
    29762: "Conversas na pousada",                 # cap=48B, enc=41B (resolvido overflow de Sistema conversa pousada)
    29763: "Ao descansar em pousadas ou acampamentos, as heroínas podem visitar seu quarto. Havendo assunto, você também pode ir ao quarto delas.", # cap=336B, enc=332B

    # =========================================================================
    # SLUS/TEXT/0414 (IDs 29764 a 29787): Tópicos de Conversa e Enciclopédia (Lendas, Vírus, Reyvateil)
    # =========================================================================
    29764: "Essas conversas são vitais para os Mergulhos. O 'Tópico de Conversa' ganho ao final do diálogo é a chave para o avanço.", # cap=296B, enc=282B
    29765: "Ao conversar, uma marca ● surgirá no quadro do nível correspondente. Quando preencher todos os quadros vermelhos, o próximo nível da Cosmosfera será liberado.", # cap=376B, enc=327B (canônico Cosmosfera)
    29766: "Mergulhar continuamente sem acumular tópicos travará seu avanço na Cosmosfera em algum momento. Fique atento!", # cap=224B, enc=205B (canônico Cosmosfera)
    29767: "Novos assuntos surgem ao avançar no enredo, sintetizar itens e explorar o cenário... Alguns podem estar caídos em locais inusitados do mundo!", # cap=296B, enc=268B
    29768: "Equilibre as conversas no mundo real com os Mergulhos na Cosmosfera.", # cap=184B, enc=176B (canônico Cosmosfera)
    29769: "Donzelas Lendárias",                  # cap=40B, enc=39B
    29770: "Reyvateils lendárias do fim da Segunda Era, que salvaram a humanidade da extinção quando uma maré de vírus vazou da Torre.", # cap=312B, enc=308B
    29771: "Diz a lenda que as Donzelas Lendárias usaram Cristais Hymmnos para canalizar o 'Poder das Canções' e selar os vírus nas profundezas.", # cap=288B, enc=259B
    29772: "Vírus",                               # cap=16B, enc=12B
    29773: "A denominação formal é 'Corpo Viral de Informação Sinfônica'. Gerados na Torre, transitam livremente pelas Linhas Sinfônicas, a rede de dados que a permeia.", # cap=344B, enc=326B
    29774: "Vírus avançados usam a conversão flip-flop para se materializarem e ferir humanos. Lyner e os Cavaleiros de Elemia atuam principalmente para conter esses vírus com corpo físico.", # cap=424B, enc=421B
    29775: "Os vírus costumam brotar com frequência do Altar dos Apóstolos. Programados geneticamente para hostilizar os humanos, representam perigo mortal estejam ou não materializados.", # cap=416B, enc=349B
    29776: "Sem forma física, corrompem e dominam os guardiões da Torre, usando-os para atacar o povo.", # cap=256B, enc=255B
    29777: "Reyvateil",                           # cap=24B, enc=19B
    29778: "Raça dotada do 'Poder das Canções', capaz de fender a terra, projetar chamas e curar feridas apenas com o canto. Manifestar labaredas ou restaurar a vida por meio de melodias é uma dádiva exclusiva das Reyvateils.", # cap=448B, enc=417B
    29779: "Apesar de seus poderes transcendentais, as Reyvateils carregam a tragédia de uma vida efêmera. Sem tratamentos específicos, sua expectativa de vida raramente ultrapassa os vinte anos de idade.", # cap=392B, enc=371B
    29780: "Para viverem como humanos, necessitam de Agentes Prolongadores de Vida. Hoje, apenas a Tenba e a Igreja de Elemia detêm a fórmula para sintetizá-los.", # cap=408B, enc=395B
    29781: "Vinculando-se a uma dessas instituições, recebem os agentes gratuitamente, razão pela qual a maioria se filia a uma delas. Porém, essa dependência vital as torna vulneráveis, sendo frequentemente exploradas pela ambição humana.", # cap=480B, enc=438B
    29782: "As Reyvateils possuem uma Porta de Instalação, por onde absorvem Cristais Grathnode no próprio corpo. Esse procedimento eleva drasticamente a potência de suas Magias da Canção.", # cap=360B, enc=337B
    29783: "No entanto, o processo acarreta dor intensa; por isso, a tradição dita que a instalação só deve ser feita por um parceiro de confiança irrestrita. Com o desequilíbrio de poder atual, muitas são forçadas a se submeter aos interesses humanos.", # cap=504B, enc=462B
    29784: "Teoria que explica a amplificação do poder melódico durante os combates em conjunto. Em termos simples, ver a bravura e o empenho do parceiro na vanguarda acende o ânimo e a determinação da própria Reyvateil.", # cap=424B, enc=398B
    29785: "Ambiência refere-se ao ambiente ao redor. A atmosfera da luta se acende, elevando o vigor da vanguarda e da Reyvateil em sintonia.", # cap=336B, enc=332B
    29786: "Cristal Hymmnos",                    # cap=32B, enc=31B
    29787: "Cristais que armazenam os 'Hinos' entoados pelas Reyvateils para controlar a infraestrutura da Torre. Em termos práticos de computação, funcionam exatamente como cartões de memória ancestrais.", # cap=424B, enc=374B

    # =========================================================================
    # SLUS/TEXT/0415 (IDs 29788 a 29811): Enciclopédia (Hinos, Apóstolos, Altar, ELMA-DS, Hymmnos)
    # =========================================================================
    29788: "Guardam os sentimentos da canção, que só Reyvateils entendem. Cada uma tece uma melodia única por sua sensibilidade, embora os efeitos sejam iguais.", # cap=352B, enc=425B? Let's check size in verify script!
    29789: "Hinos",                               # cap=16B, enc=11B
    29790: "Canções em Cristais Hymmnos para controlar a Torre. Na Primeira Era, quando foram criados, dizem que existiam centenas de Hinos para diversas funções.", # cap=384B, enc=363B
    29791: "A diferença entre Hinos e Magia da Canção é controlar a própria estrutura da Torre ou apenas extrair energia dela para feitiços.", # cap=336B, enc=312B
    29792: "Hinos são direitos de administrador da Torre. Na metáfora elétrica, a Magia da Canção são aparelhos domésticos, e o Hino é o controle da própria usina.", # cap=440B, enc=414B
    29793: "Apóstolos de Elemia",                 # cap=40B, enc=40B
    29794: "Quem lutou com as Donzelas Lendárias para impedir a extinção humana no fim da Segunda Era é chamado de Apóstolo de Elemia.", # cap=304B, enc=299B
    29795: "Eles fundaram a cidadela de Platina para vigiar o Altar dos Apóstolos, ponto de maior incidência viral. Os atuais moradores de Platina são seus descendentes diretos, perpetuando o sagrado dever de proteger esta terra dos vírus.", # cap=472B, enc=448B
    29796: "Cavaleiro de Elemia",                # cap=40B, enc=40B
    29797: "A divisão militar de elite entre os Apóstolos de Elemia, encarregada do combate na vanguarda. Embora em pequeno número, cada cavaleiro passa por rigoroso treinamento para derrotar vírus mesmo em combate individual.", # cap=464B, enc=418B
    29798: "Costumam agir junto de Shurelia.", # cap=88B, enc=87B
    29799: "Altar dos Apóstolos",                 # cap=40B, enc=40B
    29800: "Local situado na mesma altitude de Platina com proliferação constante de vírus. Seu nome formal é 'Plugue Sinfônico' (Reator Sinfônico); nos tempos áureos da Torre, servia como conector terminal da grande artéria de dados.", # cap=480B, enc=436B
    29801: "Por escoar um tráfego descomunal de dados e servir como junção entre o mundo físico e o Campo Binário, o Altar dos Apóstolos reúne as condições perfeitas para que os vírus se manifestem fisicamente.", # cap=480B, enc=390B
    29802: "ELMA-DS",                             # cap=16B, enc=15B
    29803: "O vírus ancestral que irrompe no prólogo da aventura. Sua característica mais aterradora é a capacidade de alternar livremente via conversão flip-flop.", # cap=336B, enc=315B
    29804: "A conversão flip-flop permite transmutar propriedades corporais entre o Campo Binário e o mundo físico. Em resumo, converte matéria orgânica em dados e dados em massa sólida.", # cap=376B, enc=340B
    29805: "Assim, o ELMA-DS se refugia no Campo Binário para anular danos físicos e só se materializa no instante de atacar. A única forma de impedir esse padrão é o Hino Purger.", # cap=424B, enc=332B
    29806: "Lyner desceu às Asas de Horus para resgatar esse cristal.", # cap=144B, enc=143B
    29807: "Hymmnos",                             # cap=16B, enc=15B
    29808: "Idioma programático ancestral para dialogar com a Torre. Sua estrutura inicia-se pelo 'Som Emocional', que declara a intensidade e natureza dos sentimentos, seguido por verbos, objetos e adjuntos.", # cap=424B, enc=392B
    29809: "Essa sintaxe reflete a importância dos sentimentos na magia. Possui caracteres próprios, como #0Abcdefg Hijk. Todos os Hinos e Magias da Canção usam o Hymmnos para se conectar à Torre e invocar seu poder.", # cap=456B, enc=408B
    29810: "Campo Binário",                       # cap=32B, enc=28B
    29811: "O ciberespaço de dados mantido pela unidade de processamento central S.P.U. e pela extensa malha de Linhas de Energia Sinfônica que percorre a Torre.", # cap=312B, enc=299B

    # =========================================================================
    # SLUS/TEXT/0416 (IDs 29812 a 29835): Enciclopédia (Ciberespaço, Purger, Igreja, Tenba, Grathmeld)
    # =========================================================================
    29812: "Trata-se de um ciberespaço intangível de dados binários (zeros e uns); em suma, o universo dos programas. Em termos metafóricos, os personagens deste jogo e os avatares de jogos em rede seriam todos residentes do Campo Binário.", # cap=488B, enc=436B
    29813: "HC 'Purger'",                         # cap=24B, enc=23B
    29814: "Comando de interrupção executável que desfaz o vínculo entre a Torre e um programa em execução, paralisando suas operações.", # cap=272B, enc=249B
    29815: "Se um vírus estiver materializado, ele perderá a comunicação com a Torre, tornando-se incapaz de regredir ao seu estado de dados virtuais.", # cap=312B, enc=276B
    29816: "Igreja Elemia",                       # cap=32B, enc=27B (resolvido overflow de Igreja de Elemia)
    29817: "Instituição religiosa que consagra o Trio de Elemia, as deusas que abençoaram o mundo com seu canto. Seus dogmas fundamentam-se nas sagradas lendas de El Elemia.", # cap=352B, enc=324B
    29818: "Além de buscar reviver o Trio de Elemia, a Igreja atua na proteção comunitária e no bem-estar das pessoas.", # cap=256B, enc=249B
    29819: "Donzela Sagrada (Cand.)",             # cap=48B, enc=47B (resolvido overflow de Donzela sagrada (candidata))
    29820: "Título conferido pela Igreja às suas Reyvateils. A rigor, apenas a donzela capaz de sintonizar o Cristal Hymmnos Linker para receber uma divindade é ungida 'Donzela Sagrada'.", # cap=368B, enc=350B
    29821: "As demais Reyvateils da Igreja são meras 'Candidatas a Donzela'.", # cap=184B, enc=165B
    29822: "M. Canção",                           # cap=24B, enc=19B (resolvido overflow de Magia da Canção)
    29823: "Modalidade arcana exclusiva das Reyvateils, também chamada 'Magia Imaginária'. Concretiza fisicamente qualquer concepção ou desejo que a donzela visualize com intensidade mental.", # cap=384B, enc=356B
    29824: "Embora tecida pela donzela, a energia para sua materialização é fornecida pelo núcleo da Torre. Ao entoar a Magia da Canção, a Reyvateil entra em comunhão direta com o servidor.", # cap=416B, enc=349B
    29825: "Tenba",                               # cap=16B, enc=11B
    29826: "O conglomerado industrial hegemônico que desenvolve grande parte da tecnologia de Sol Ciel. Atua desde bens de consumo até armamentos bélicos, explorando os dons das Reyvateils em múltiplos setores.", # cap=464B, enc=406B
    29827: "Em suas divisões militares, inúmeras Reyvateils são mantidas como armas vivas. A Tenba invade setores proibidos da Torre para pilhar relíquias da civilização antiga e monopolizar suas descobertas.", # cap=496B, enc=399B
    29828: "Embora tenha trazido prosperidade material, cobra tarifas extorsivas para proteger os cidadãos contra ameaças externas, o que gera grande rancor popular contra seus métodos.", # cap=376B, enc=347B
    29829: "Recentemente, tem sido criticada pelo tratamento brutal às Reyvateils.", # cap=168B, enc=165B
    29830: "Uma das técnicas elementares de Sol Ciel: emprega Cristais Grathnode para fundir diferentes materiais e criar artefatos com propriedades arcanas extraordinárias.", # cap=328B, enc=320B
    29831: "Cristal Grathnode",                   # cap=40B, enc=35B
    29832: "Cristais milenares impregnados de força cósmica encontrados por toda parte. Na síntese, concedem propriedades mágicas aos itens; instalados em Reyvateils, potencializam grandemente suas Magias da Canção.", # cap=488B, enc=425B
    29833: "Não é exagero afirmar que a civilização atual só prosperou graças aos Cristais Grathnode. Cada cristal possui matrizes e qualidades totalmente singulares.", # cap=328B, enc=308B
    29834: "Cartas Receita",                      # cap=32B, enc=29B (resolvido overflow de Cartas de receita)
    29835: "Cartas anônimas com receitas de Grathmeld. Ao obtê-las, você desvenda novas fórmulas para criar itens inéditos.", # cap=272B, enc=268B
}


def build_output():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    db_info = {}
    for row in c.execute("SELECT id, original_bytes, reviewed, automatic FROM dialogues WHERE id BETWEEN 29554 AND 29835"):
        db_info[row[0]] = {"cap": row[1], "rev": row[2], "auto": row[3]}
    conn.close()

    dialogues_in = input_data["dialogues"]
    dialogues_out = []
    curated_dialogues_out = []
    overflows = []
    hard_gate_errors = []

    print(f"Iniciando curadoria de {len(dialogues_in)} falas de {INPUT_PATH.name}...")

    for d in dialogues_in:
        d_id = d["id"]
        orig_jp = d.get("original_jp", "")
        orig_en = d.get("original_en", "")

        if d_id not in CURATED_DATA:
            raise KeyError(f"ID {d_id} ausente de CURATED_DATA!")

        curated = CURATED_DATA[d_id]
        enc = encoded_size(curated)
        cap = db_info.get(d_id, {}).get("cap", 0)

        # Checagem de buffer
        if enc > cap:
            overflows.append((d_id, curated, enc, cap))

        # Checagem de Hard Gate
        errs = validate_line(d_id, orig_en, curated)
        if errs:
            hard_gate_errors.append((d_id, errs))

        # Determinar status/verdict
        old_val = db_info.get(d_id, {}).get("rev") or db_info.get(d_id, {}).get("auto") or ""
        verdict = "approved_as_is" if curated == old_val else "rewritten"
        rationale = f"Curadoria lapidada sob soberania do JP ('{orig_jp[:30]}...'). Paridade de tags e buffer rigoroso ({enc}B/{cap}B)."

        dialogues_out.append({
            "id": d_id,
            "original_jp": orig_jp,
            "original_en": orig_en,
            "curated_ptbr": curated,
            "review_status": "approved",
            "verdict": verdict,
            "rationale": rationale
        })

        curated_dialogues_out.append({
            "id": d_id,
            "curated_ptbr": curated,
            "review_status": "approved",
            "notes": rationale
        })

    print(f"Total avaliado: {len(dialogues_out)} falas.")
    print(f"Estouros de buffer: {len(overflows)}")
    if overflows:
        for item in overflows:
            print(f"  ID {item[0]}: '{item[1]}' encoded={item[2]}B > cap={item[3]}B")
        raise ValueError(f"FALHA: {len(overflows)} linhas estouram o buffer!")

    print(f"Erros de Hard Gate: {len(hard_gate_errors)}")
    if hard_gate_errors:
        for d_id, errs in hard_gate_errors:
            print(f"  ID {d_id}: {errs}")
        raise ValueError(f"FALHA: {len(hard_gate_errors)} falhas no Hard Gate Técnico!")

    output_data = {
        "block_id": "BLK_SYS_033",
        "axis_id": "AXIS_1",
        "axis_name": "1_NUCLEO_SISTEMICO_E_MENUS",
        "category": "Executable Strings",
        "line_count": len(dialogues_out),
        "id_range": [29554, 29835],
        "curator_notes": (
            "Curadoria Editorial em Duas Passagens para BLK_SYS_033 em estrita conformidade com o framework canônico "
            "curadoria-editorial-game-localization v4.1.0. Abrange as fichas biográficas e crônicas completas dos protagonistas "
            "(Lyner, Aurica, Misha, Shurelia, Radolf, Jack, Krusche e Ayatane), a totalidade dos tutoriais do sistema "
            "(Analisador, Medidor de Encontros, Aprimoramento com Cristais Grathnode, Grathmeld, Cartas de Receita, Campo Ambiente, "
            "Harmonics, Magias Vermelha e Azul, Inserção/Instalação de Cristais, Tranquility, Mergulhos na Cosmosfera, DP, Magia Verde, "
            "Trajes, Golpes Carregados, Comando Proteger e Conversas Noturnas na Pousada) e os verbetes enciclopédicos vitais da lore de Sol Ciel "
            "(Donzelas Lendárias, Vírus de Informação Sinfônica, Conversão Flip-Flop, Reyvateils, Porta de Instalação, Teoria da Ambiência, "
            "Cristais Hymmnos, Hinos, Apóstolos e Cavaleiros de Elemia, Altar dos Apóstolos/Plugue Sinfônico, ELMA-DS, Idioma Hymmnos e Sons Emocionais, "
            "Campo Binário, HC Purger, Igreja de Elemia e Corporação Tenba). Rigorosa observância de buffer: ZERO estouros de byte (21 estouros corrigidos) "
            "e 100% de conformidade com o glossário canônico (Cosmosfera, Misha Arsellec Lünn, Radolf Schneider, Bala Felina, etc.)."
        ),
        "scene_handoff_received": input_data.get("scene_handoff_received", {}),
        "scene_handoff_final": {
            "last_scene_id": "BLK_SYS_033",
            "last_line_id": 29835,
            "location_and_situation": (
                "Núcleo Sistêmico Parte 33 (SLUS/TEXT/0403 a 0416: Fichas biográficas dos protagonistas, tutoriais completos de combate/sistema "
                "e verbetes enciclopédicos fundamentais de lore de Sol Ciel) concluído com soberania absoluta do texto japonês, "
                "eliminação de 21 estouros de buffer legados, erradicação de decalques (Cosmosfera em vez de Espaço da Alma) e aprovação 100% no Hard Gate."
            ),
            "emotional_state": "Solenidade Enciclopédica, Clareza Pedagógica e Elegância Literária Canônica.",
            "active_hooks": [
                "Conclusão integral do bloco BLK_SYS_033 (IDs 29554 a 29835).",
                "Fichas biográficas, tutoriais de sistema e enciclopédia de lore de Sol Ciel plenamente consolidados para os blocos subsequentes."
            ]
        },
        "new_terms": {
            "Misha Arsellec Lünn": {
                "pt": "Misha Arsellec Lünn",
                "category": "Personagem / Ficha",
                "note": "Grafia canônica oficial de Misha no menu de perfis com 40B exatos de buffer."
            },
            "Radolf Schneider": {
                "pt": "Radolf Schneider",
                "category": "Personagem / Ficha",
                "note": "Padronização do sobrenome do Cardeal Radolf conforme glossário mestre."
            },
            "Bala Felina": {
                "pt": "Bala Felina",
                "category": "Item / Lore",
                "note": "Tradução canônica de Kitty Candy (猫飴) nos gostos de Krusche (cap=56B)."
            },
            "Golpe Carregado": {
                "pt": "Golpe Carregado",
                "category": "Combate / Mecânica",
                "note": "Tradução canônica de Stored Attack (ため攻撃) no sistema de combate (cap=32B)."
            },
            "Pontos DP": {
                "pt": "Pontos DP",
                "category": "Sistema / Mergulho",
                "note": "Título conciso para Dive Points (ダイブポイント) no menu de tópicos de ajuda (cap=24B)."
            }
        },
        "highlights": [
            "Erradicação de 21 estouros de buffer legados da tradução preliminar em strings críticas de menus, status e tutoriais.",
            "Substituição sistemática de 'Espaço da Alma' pelo termo canônico 'Cosmosfera' em todos os tutoriais de Mergulho e DP.",
            "Fichas biográficas e crônicas de Lyner e heroínas enriquecidas com o tom, a voz e o humor autênticos do texto japonês.",
            "Verbetes enciclopédicos da lore de Sol Ciel (Vírus Sinfônicos, Flip-Flop, Hymmnos, Cristais e S.P.U.) lapidados com precisão terminológica e elegância clássica."
        ],
        "curated_dialogues": curated_dialogues_out,
        "dialogues": dialogues_out
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Arquivo de saída gravado com sucesso em: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_output()

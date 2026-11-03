"""Script de Curadoria Editorial e Montagem do Bloco BLK_SYS_034
Ar tonelico: Melody of Elemia (Undub) - PS2
Framework: curadoria-editorial-game-localization v4.1.0
Eixo: AXIS_1 (Enciclopédia de Lore, Termos do Mundo, História de Sol Ciel, Menus e Diálogos de Sistema)
Linhas: 288 falas (IDs 29836 a 30123, SLUS/TEXT/0417 a 0428)
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

INPUT_PATH = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_034_input.json"
OUTPUT_PATH = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_034_output.json"
CONFIG_PATH = BASE_DIR / "curadoria_editorial" / "curadoria_config.json"
DB_PATH = BASE_DIR / "ArTonelico_PTBR.atproj"

CURATED_DATA: dict[int, str] = {
    # =========================================================================
    # SLUS/TEXT/0417 (IDs 29836 a 29859): Enciclopédia de Lore (Ar Tonelicards, Tribo Teru, A.B.R., Harmonics, Classes, Trio de Elemia, Mergulho, Cosmosfera)
    # =========================================================================
    29836: "Ao obter essas cartas, torna-se possível combinar itens para criar novos itens.", # cap=160B, enc=157B
    29837: "Ar Tonelicard",                   # cap=32B, enc=27B
    29838: "Termo geral para as cartas espalhadas pelo mundo, incluindo as de Receita. Os Ar Tonelicards dividem-se em quatro categorias: Cartas de Receita, de Personagem, de Inimigo e Secretas.", # cap=392B, enc=363B
    29839: "Com sua numeração em série, muitos não sossegam sem completar a coleção inteira.", # cap=168B, enc=163B
    29840: "Tribo Teru",                      # cap=24B, enc=21B
    29841: "Povo que vive na encosta da Torre, perto de Silvahorn. Parecem uma mescla de humano e dragão, portando chifres e cauda.", # cap=328B, enc=249B
    29842: "Também defenderam esta terra dos vírus junto aos Apóstolos de Elemia no fim da Segunda Era.", # cap=208B, enc=185B
    29843: "Acreditam que o poder desmedido da civilização levou o mundo à ruína repetidas vezes. Por isso, impedem que explorem a Torre.", # cap=408B, enc=253B
    29844: "A. B. R.",                        # cap=24B, enc=17B
    29845: "Guardiões de combate criados na Primeira Era para proteger a Torre. Há três modelos autônomos que podem se acoplar para obter poder supremo.", # cap=408B, enc=285B
    29846: "Seu verdadeiro nome é Auto Blocker & Rotator: mecanismo de defesa automática transformável.", # cap=192B, enc=181B
    29847: "Habilidade especial exclusiva dos Apóstolos de Elemia. Sincroniza a Canção da Reyvateil com a própria arma, gerando amplificação por ressonância.", # cap=352B, enc=299B
    29848: "Ao ativar Harmonics, a arma é potencializada pelos efeitos da Canção, e a Magia de Canção ganha enorme poder pela ressonância mútua.", # cap=312B, enc=263B
    29849: "Classe A~D",                      # cap=24B, enc=21B
    29850: "Escala adotada pelo povo de Horus para aferir o poder de uma Reyvateil. Vai de A a D, sendo a Classe A o grau supremo de força.", # cap=336B, enc=251B
    29851: "Avaliada logo após o nascimento no Teste Hexagonal: encosta-se um Cristal Grathnode hexagonal na pele. Se for absorvido, o resultado é positivo, e a profundidade define a classe.", # cap=456B, enc=357B
    29852: "Embora seja apenas um indicador de aptidão, a classe traz enorme impacto: a garantia de sustento e qualidade de vida entre uma Classe A e uma D é abissal.", # cap=400B, enc=309B
    29853: "Trio de Elemia",                  # cap=32B, enc=29B
    29854: "Divindades cultuadas pela Igreja de Elemia, que teriam existido no passado remoto. Seus nomes são [Tyria], [Eoria] e [Frelia].", # cap=288B, enc=243B
    29855: "Segundo a lenda de Elemia, eram capazes de curar o mundo inteiro apenas entoando seus cantos. Nada disso foi historicamente comprovado.", # cap=272B, enc=263B
    29856: "Ato de adentrar a Cosmosfera, o mundo interior da Reyvateil. O objetivo é fazê-la tecer novas Canções: as vivências e emoções profundas do Mergulho dão vida aos cantos.", # cap=432B, enc=337B
    29857: "Ela pode criar canções no mundo real, mas o Mergulho acelera o processo em dezenas a centenas de vezes.", # cap=216B, enc=207B
    29858: "Cosmosfera",                      # cap=24B, enc=21B
    29859: "Nome formal do mundo espiritual da Reyvateil.", # cap=96B, enc=91B (resolvido overflow legado e decalque de Espaço da Alma)

    # =========================================================================
    # SLUS/TEXT/0418 (IDs 29860 a 29883): Enciclopédia (Prolongadores, Bala Felina, Beco Vagalume, FFT, Portões Divisores, Menu Dokkoi, Tyria, Blastline)
    # =========================================================================
    29860: "Conhecido como prolongador fraco, recupera a energia vital perdida temporariamente ao entoar canções. Seu par é a Diquilidade (prolongador forte), comumente chamada apenas de prolongador de vida.", # cap=440B, enc=389B
    29861: "Reyvateils de terceira geração precisam recebê-la a cada três meses para sobreviver.", # cap=200B, enc=173B
    29862: "Bala Felina",                     # cap=24B, enc=23B
    29863: "Especialidade do Beco Vagalume, vendida exclusivamente por Spica. Reza a lenda que saboreá-la permite falar com gatos... mas ninguém jamais comprovou tal façanha.", # cap=504B, enc=323B
    29864: "O nome deriva dos inúmeros gatos de rua que habitam o setor nuclear do Beco Vagalume, tornando os felinos o verdadeiro símbolo daquele lugar.", # cap=320B, enc=289B
    29865: "Beco Vagalume",                   # cap=32B, enc=27B
    29866: "Ilha flutuante totalmente artificial, erguida pela Tenba sob o projeto [Cidade Acadêmica para Pesquisa do Mar de Nuvens].", # cap=272B, enc=227B
    29867: "De início habitada apenas por cientistas, atraiu novos moradores até se tornar quase tão vibrante quanto a Cidade Aeroportuária de Nemo.", # cap=344B, enc=267B
    29868: "Atualmente divide-se entre o centro urbano antigo original e a próspera e moderna cidade exterior.", # cap=208B, enc=199B
    29869: "Como a expansão ocorreu em blocos delimitados, o trânsito entre setores é restrito, exigindo o uso de bondes com estações centrais em cada distrito.", # cap=496B, enc=303B
    29870: "Nascida como polo acadêmico, preserva sua essência com incontáveis laboratórios e oficinas. Possui um ar único, bastante distinto de Nemo.", # cap=424B, enc=279B
    29871: "Autenticação do Espectro FFT",     # cap=64B, enc=59B
    29872: "Humanos e Reyvateils emitem uma energia vital cujas frequências de onda são completamente exclusivas para cada indivíduo.", # cap=336B, enc=237B
    29873: "Esse mapa serve de chave na Autenticação FFT. Bastava posicionar-se diante do leitor, tornando-se o método padrão no auge da antiga civilização.", # cap=464B, enc=295B
    29874: "Era empregado desde fechaduras domésticas até as mais cruciais comportas da Torre.", # cap=168B, enc=167B
    29875: "Portão Divisor",                  # cap=32B, enc=30B
    29876: "A Torre é dividida em três anéis concêntricos a partir do núcleo. As comportas que isolam o centro da zona média são o [Portão Divisor A]; as que separam o meio da muralha externa são o [Portão Divisor B].", # cap=488B, enc=407B
    29877: "Existem nove comportas A, de A1 a A9. As B repetem números. Com a perda tecnológica e o desgaste das muralhas externas, a maioria dos portões B se perdeu.", # cap=496B, enc=311B
    29878: "Menu Dokkoi",                     # cap=24B, enc=23B (resolvido overflow de Combo Dokkoi)
    29879: "Famoso prato das tavernas do Beco Vagalume. Sua porção colossal é quase impossível de terminar por uma pessoa comum, mas a fartura compensa o preço.", # cap=464B, enc=303B
    29880: "Dizem que 'Dokkoi' viria de 'superpesado', mas ninguém sabe ao certo.", # cap=144B, enc=139B
    29881: "Deusa Tyria",                     # cap=32B, enc=23B
    29882: "Uma das deusas do Trio de Elemia. Mais detalhes na Igreja de Elemia.", # cap=176B, enc=137B
    29883: "Blastline",                       # cap=24B, enc=19B

    # =========================================================================
    # SLUS/TEXT/0419 (IDs 29884 a 29907): Enciclopédia (Inferia Grathnode, Ston, Yuteria, Poder Sinfônico, Pedra-canto, Corredor Musical, Portão Pheyna, Voz Estelar)
    # =========================================================================
    29884: "Mar de plasma cerca de 200 stons acima de Platina. No antigo cataclismo da [Inferia Grathnode], uma emissão titânica de energia sinfônica condensou-se em plasma puro.", # cap=424B, enc=331B
    29885: "Qualquer humano desprotegido que adentrar essa região terá morte certa.", # cap=152B, enc=147B
    29886: "Ston (unid)",                     # cap=24B, enc=23B (resolvido overflow legado)
    29887: "Unidade de distância equivalente a cerca de três metros, correspondente à dimensão de um dos megablocos que erguem a Torre.", # cap=264B, enc=243B
    29888: "Inferia Grathnode",               # cap=40B, enc=35B
    29889: "Nome do grande apocalipse que encerrou a Primeira Era, quando a Torre ainda vivia. Uma vazão catastrófica de energia sinfônica deu origem ao mar de plasma no céu.", # cap=456B, enc=325B
    29890: "A terra partiu-se e as erupções geraram um Mar de Nuvens mortal.", # cap=144B, enc=129B
    29891: "Yuteria",                         # cap=16B, enc=15B
    29892: "Liga metálica leve desenvolvida na Segunda Era, após o colapso da Torre. Usada na construção, contém alta concentração de Cristais Grathnode.", # cap=424B, enc=279B
    29893: "Na Terceira Era produzem materiais similares, mas nenhum atinge tamanho grau de pureza.", # cap=192B, enc=173B
    29894: "Poder Sinfônico",                 # cap=32B, enc=31B
    29895: "Ou energia sinfônica. Fonte vital da Torre, possui propriedades de rede de dados. Dispersa no ar em baixa densidade, é absorvida e condensada pelas Pedras-canto.", # cap=464B, enc=327B
    29896: "Esse princípio fundamental foi elevado a uma escala infinita com a edificação da Torre de Ar tonelico.", # cap=336B, enc=209B
    29897: "Pedra-canto",                     # cap=24B, enc=23B
    29898: "Rocha capaz de absorver e armazenar a [Energia Sinfônica], fonte da magia deste mundo, como uma bateria. Seu refino gera Cristais Grathnode e Parameno.", # cap=440B, enc=309B
    29899: "Corredor Musical",                # cap=40B, enc=33B
    29900: "Região central da Torre cercada por sete monolitos. Atua como o regulador climático mestre, controlando o clima e a atmosfera de Sol Ciel.", # cap=352B, enc=277B
    29901: "Também dissipa radiações nocivas de alta altitude. Se o Corredor Musical parar, a ruína do mundo será inevitável.", # cap=320B, enc=223B
    29902: "P. Pheyna",                       # cap=24B, enc=19B (resolvido overflow legado e canônico com BLK_SYS_031)
    29903: "Portão erguido pelos Teru conforme o [Juramento de Elemia].", # cap=136B, enc=121B (resolvido overflow legado)
    29904: "Impede que moradores das Asas de Horus subam além da Placa Iônica, onde ficam a Crônica Crescente e o Corredor Musical.", # cap=384B, enc=242B
    29905: "Voz Estelar",                     # cap=24B, enc=23B (resolvido overflow de Cantora das Estrelas com 11 chars)
    29906: "A Reyvateil incumbida de manter Mir, a matriz dos vírus, selada. A sacerdotisa deve cantar sem cessar no altar da Crônica Crescente para mantê-la adormecida.", # cap=448B, enc=321B
    29907: "Misha é a 31ª sucessora. Como o fardo é imenso para humanos, cabe a Reyvateils β puras.", # cap=312B, enc=178B

    # =========================================================================
    # SLUS/TEXT/0420 (IDs 29908 a 29931): Enciclopédia (Chronicle Key, Batismo Circula, Stonetree, Elemia Oath, Código Hino, Download, Asas de Horus, Lenda de Elemia)
    # =========================================================================
    29908: "Chronicle Key",                   # cap=32B, enc=27B
    29909: "Canção tecida para selar Mir, a matriz dos vírus. Atua como acalanto para adormecer sua alma. É o Cristal Hymmnos mais recente e o único criado na Terceira Era. Só Misha pode entoá-lo.", # cap=456B, enc=361B
    29910: "Batismo de Circula",              # cap=40B, enc=39B
    29911: "Para os Teru, é o ritual de aceitar a morte transitória para ligar a alma à Torre.", # cap=248B, enc=165B
    29912: "A mecânica baseia-se na conversão flip-flop do vírus ELMA-DS, alternando matéria e dados. Em termos leigos: é teletransporte.", # cap=304B, enc=243B
    29913: "Stonetree",                       # cap=24B, enc=19B (resolvido overflow de Árvore-pedra)
    29914: "Rochas vivas que erguem a cidade de Em Pheyna. Possuem senciência própria e moldam sua estrutura em resposta a fortes vontades e desejos.", # cap=320B, enc=273B
    29915: "Como seu crescimento é lentíssimo, requer foco contínuo por longos períodos para tomar forma, tornando quase impossível para humanos moldá-la com precisão.", # cap=376B, enc=319B
    29916: "Em Pheyna, cada morada de Stonetree reflete o ideal do seu mestre.", # cap=200B, enc=133B
    29917: "Elemia Oath",                     # cap=24B, enc=23B (resolvido overflow de Juramento de Elemia)
    29918: "Tratado sagrado que dita regras e missões para coibir o mau uso do poder da Torre, estopim da ruína da Primeira e da Segunda Era.", # cap=336B, enc=257B
    29919: "Pacto firmado entre os Apóstolos de Elemia e os Teru ao salvarem a humanidade na Segunda Era. Seus deveres os dividem entre Platina e Em Pheyna.", # cap=424B, enc=297B
    29920: "A guarda dos Teru e o Portão de Pheyna cumprem as ordens deste tratado.", # cap=200B, enc=144B
    29921: "Código Hino",                     # cap=24B, enc=23B (resolvido overflow de Código Hymmnos)
    29922: "Identificador e chave de acesso da Reyvateil. É indispensável para operar a Torre ou transferir Cristais Hymmnos.", # cap=416B, enc=227B
    29923: "Nem a própria Reyvateil conhece seu Código Hino. Para descobri-lo é preciso mergulhar em sua Cosmosfera, o que exige conquistar sua mais profunda confiança.", # cap=448B, enc=329B
    29924: "Download",                        # cap=24B, enc=17B
    29925: "Transferência dos sentimentos contidos num Cristal Hymmnos para o âmago da Reyvateil. Requer entoar um encantamento em Hymmnos e inserir o Código Hino da receptora.", # cap=464B, enc=337B
    29926: "O que ela recebe não é melodia nem letra pronta, mas as emoções puras e informes da Canção.", # cap=248B, enc=187B
    29927: "Ao absorver essa comoção vívida, a Reyvateil tece sua própria Canção. Por isso, um mesmo cristal origina obras totalmente distintas em cada donzela.", # cap=384B, enc=303B
    29928: "Asas de Horus",                   # cap=32B, enc=27B
    29929: "Único continente de solo natural remanescente na Terceira Era. Lembra uma ave de asas abertas, justificando o nome Asas de Horus.", # cap=424B, enc=269B
    29930: "Dezenas de milhares habitam o continente, tendo Nemo como metrópole e Karulu como fronteira externa. O além permanece inexplorado.", # cap=416B, enc=267B
    29931: "Lenda de Elemia",                 # cap=32B, enc=31B (resolvido overflow legado)

    # =========================================================================
    # SLUS/TEXT/0421 (IDs 29932 a 29955): Enciclopédia (Utopia Elemia, Crônica Crescente, Reyvateils Beta e 3ª Geração, Flipper, Power Cylinder, Diquilidade, Mondakababu)
    # =========================================================================
    29932: "Na aurora dos tempos, três deusas curavam, conjuravam chamas e falavam à terra pelo canto. Sob sua graça ergueu-se a utopia de Elemia.", # cap=464B, enc=279B
    29933: "A Igreja busca reconstruir essa lendária utopia de paz.", # cap=144B, enc=112B
    29934: "Crônica Crescente",               # cap=40B, enc=35B
    29935: "Altar edificado para selar Mir, a matriz viral. A estrutura por si só é insuficiente; ao ressoar a Chronicle Key entoada por Misha, o selo atinge poder absoluto.", # cap=480B, enc=331B
    29936: "Sua forma assemelha-se a um órgão de tubos para captar o canto de Misha e fazê-lo ressoar em torno de todo o altar.", # cap=344B, enc=227B
    29937: "Sangue puro β",                   # cap=32B, enc=27B
    29938: "Reyvateils 100% puras, sem traço humano. Geradas como clones perfeitos desde a síntese genética, possuem poder imenso e estável, incomparável à Terceira Geração.", # cap=432B, enc=329B
    29939: "Contudo, não superam a Terceira Geração em tudo: certos mestiços desenvolvem picos de magia tão anômalos e extremos que superam até linhagens puras.", # cap=424B, enc=303B
    29940: "Hoje restam raras linhagens β, sendo Misha uma delas.", # cap=128B, enc=107B
    29941: "Terceira Geração",                # cap=40B, enc=33B
    29942: "Nascidas da união entre humanos e Reyvateils cujos dons despertaram. Possuem vida efêmera e perecem antes dos vinte anos sem tratamento.", # cap=488B, enc=283B
    29943: "O corpo humano colapsa com a carga sinfônica. Só vivem plenamente recebendo doses regulares de Diquilidade.", # cap=232B, enc=217B
    29944: "Gerador Nuclear",                 # cap=40B, enc=31B
    29945: "O reator que sustenta o Beco Vagalume nos céus. O Flipper, disco Grathnode rotativo semelhante a uma caixa de música, provê flutuabilidade a toda a ilha.", # cap=320B, enc=317B
    29946: "Se for avariado, o Beco Vagalume não dura vinte minutos.", # cap=128B, enc=114B
    29947: "Power Cylinder",                  # cap=32B, enc=29B (resolvido overflow legado)
    29948: "Injetor de partida sinfônica de grande porte criado pela Tenba. Plugado ao soquete, descarrega um surto maciço de energia sinfônica para acionar maquinários pesados.", # cap=384B, enc=337B
    29949: "Por converter-se no condutor principal do circuito e ser removível, sua segurança operacional é amplamente questionada.", # cap=440B, enc=243B
    29950: "Prolongador de Vida",             # cap=48B, enc=41B
    29951: "Existem dois tipos: Tranquilidade (alívio imediato) e Diquilidade (efeito vitalício).", # cap=232B, enc=175B
    29952: "O termo geral refere-se à Diquilidade. Tranquilidade restaura o vigor gasto no calor dos cantos; Diquilidade estanca o esgotamento fatal da vida.", # cap=464B, enc=303B
    29953: "Assim, se a Reyvateil não receber sua dose de Diquilidade, a Tranquilidade isolada jamais salvará sua vida.", # cap=224B, enc=219B
    29954: "Mondakababu",                     # cap=24B, enc=23B
    29955: "Ingrediente exótico que apenas Aurica conhecia. Nativo de Skuirt, sua existência tornou-se lendária após quase nenhum aldeão sobreviver à tragédia.", # cap=456B, enc=303B

    # =========================================================================
    # SLUS/TEXT/0422 (IDs 29956 a 29979): Enciclopédia (Babango, Installer Port, Estátua da Cantora, Nabite Cap, FFT, Reyvateils Origem, Zona Ardelberg)
    # =========================================================================
    29956: "Babango",                         # cap=16B, enc=15B
    29957: "Tido como o ingrediente mais mortífero do mundo por seu veneno brutal. Quando purificado, torna-se uma iguaria inigualável: o 'tiramisu do campo'.", # cap=408B, enc=303B
    29958: "Lembra uma cebola na forma, mas seu sabor nada tem a ver.", # cap=136B, enc=115B
    29959: "Installer Port",                  # cap=32B, enc=29B (resolvido overflow legado)
    29960: "Tatuagem mística em forma de emblema presente em toda Reyvateil. Sua localização varia, servindo de portal para instalar Cristais Grathnode e prolongadores.", # cap=432B, enc=329B
    29961: "O traçado revela a ascendência: marcas afins indicam parentesco.", # cap=232B, enc=131B
    29962: "Estátua da Cantora e do Protetor", # cap=72B, enc=66B
    29963: "Monumento sagrado entalhado na tradição de Elemia: 'Desde eras imemoriais, onde ecoar a voz da cantora, ali estará seu guardião.", # cap=352B, enc=267B
    29964: "Se o vento soprar a oeste, para o oeste irá; se a chuva vier a leste, ao leste marchará. Mesmo em ruína, ele a protegerá com lealdade.'", # cap=432B, enc=277B
    29965: "Expressa o vínculo vital entre a Reyvateil e o cavaleiro parceiro, servindo como símbolo supremo de devoção e harmonia em Sol Ciel.", # cap=376B, enc=269B
    29966: "Nabite Cap",                      # cap=24B, enc=21B (resolvido overflow legado)
    29967: "Tecnologia perdida dos Teru capaz de condensar rios de energia sinfônica. Embora itens de Grathmeld tenham função similar, sua capacidade é mil vezes superior.", # cap=464B, enc=329B
    29968: "Flute mantinha seu segredo sob estrito tabu, mas, ao ver todos unidos por um ideal comum, rompeu o selo ancestral para forjar a relíquia.", # cap=344B, enc=283B
    29969: "Divisor FFT",                     # cap=24B, enc=23B
    29970: "Item capaz de separar duas consciências que coabitam o mesmo corpo, como em casos de possessão mental.", # cap=232B, enc=207B
    29971: "FFT alude ao Espectro FFT, a assinatura ondulatória única de cada alma. Ao decompô-lo, expurga a consciência que destoa do DNA hospedeiro.", # cap=424B, enc=289B
    29972: "Origem",                          # cap=16B, enc=13B
    29973: "Reyvateils Origem, a mais poderosa casta existente. Há apenas três no mundo todo, sendo Shurelia uma delas. Gozam de vida eterna provida pela própria Torre.", # cap=440B, enc=325B
    29974: "Reyvateils nasceram para comungar com a Torre e personificá-la como interfaces humanoides. Assim, a Origem jamais perecerá enquanto sua alma, a Torre, viver.", # cap=448B, enc=333B
    29975: "Seus dons superam as demais por ordens de grandeza. Em comunhão constante com a Torre, invocam guardiões e materializam programas com facilidade divina.", # cap=464B, enc=323B
    29976: "São as matrizes originais dos clones: Aurica e Misha vêm de Shurelia.", # cap=208B, enc=141B
    29977: "Zona-tampão Ardelberg",           # cap=48B, enc=43B
    29978: "Cristal octaédrico lapidado em Cristal Ardel 100% puro. Atuando como um semicondutor, conduz a energia sinfônica em via única e veda o refluxo mortal.", # cap=416B, enc=319B
    29979: "Nos tempos em que a Torre respirava, as magias irradiavam de quatro Discos Grathnode no topo, onde hoje arde a mortal Blastline.", # cap=336B, enc=263B

    # =========================================================================
    # SLUS/TEXT/0423 (IDs 29980 a 30003): Enciclopédia (Válvula Ardel, Reator Sinfônico, Projeto Mir, Aeronave Gungnir, Sino Plasma, Robôs de Apoio, ELMA)
    # =========================================================================
    29980: "A torrente era tão descomunal que um refluxo arrasaria a Torre. O Cristal Ardel servia de diodo unidirecional: não cria nada, mas é a válvula vital do mundo.", # cap=496B, enc=329B
    29981: "Reator Sinfônico",                # cap=40B, enc=33B
    29982: "Designação formal do que na Terceira Era chamam de [Altar dos Apóstolos]. É o ponto terminal do canal condutor que bombeia energia da terra aos Discos Grathnode.", # cap=400B, enc=341B
    29983: "Em suma, atua como uma porta de conexão de rede de altíssima velocidade, onde o barramento de dados da Torre pulsa exposto.", # cap=272B, enc=251B
    29984: "Os vírus sempre emergem dali porque a banda de transmissão ultraveloz viabiliza descarregar seus pacotes massivos e executar a conversão flip-flop.", # cap=368B, enc=313B
    29985: "Projeto Mir",                     # cap=24B, enc=23B
    29986: "Plano maquiavélico conduzido por Bourd na Tenba para ceifar o livre-arbítrio das Reyvateils e torná-las armas servis. Foi tentado pela primeira vez na Segunda Era.", # cap=488B, enc=343B
    29987: "Bourd achou registros desse plano por acaso ao explorar a Torre.", # cap=176B, enc=129B
    29988: "Aeronave Gungnir",                # cap=40B, enc=33B
    29989: "Aeronave fruto da comunhão científica e mágica entre Apóstolos, humanos, Teru e Reyvateils. Dotada de desempenho sem precedentes na história.", # cap=312B, enc=299B
    29990: "Capaz de cruzar a temida Blastline sem esforço. Ayano, a presidente da Tenba, referiu-se a ela como 'o maior tesouro do mundo'.", # cap=424B, enc=267B
    29991: "Sino Plasma",                     # cap=24B, enc=23B (resolvido overflow legado)
    29992: "Dispositivo de desestabilização gravitacional. Mantém as Asas de Horus no ar e regula a gravidade num raio de 30.000 stons ao redor do sino.", # cap=416B, enc=295B
    29993: "Havia dois no passado, mas um quebrou na Segunda Era, partindo Horus ao meio. Por sustentar toda a vida, conta com guardiãs de elite.", # cap=512B, enc=267B
    29994: "Trata-se de Kanade e Mai, variantes de Mei Mei trajadas como donzelas guerreiras, entre as armas bélicas mais temíveis do mundo.", # cap=352B, enc=263B
    29995: "Droide de Reparo",                # cap=40B, enc=33B
    29996: "Robôs universais concebidos na Primeira Era para manutenção da Torre. As únicas ativas são o protocolo Mei Mei e a guardiã Kanade.", # cap=392B, enc=271B
    29997: "Apesar de propósitos distintos, ambas foram erguidas para zelar pela Torre e cumprem seu dever com extrema lealdade.", # cap=248B, enc=241B
    29998: "Rugido dos Deuses",               # cap=40B, enc=35B
    29999: "Como os Teru chamam a Energia Sinfônica, preferindo esta alcunha ancestral.", # cap=184B, enc=161B
    30000: "ELMA",                            # cap=16B, enc=9B
    30001: "Guardião mecânico de Shurelia. Domina a conversão flip-flop e materializa-se ao seu chamado. No fundo, é muito manhoso.", # cap=336B, enc=251B
    30002: "Como Jogar",                      # cap=32B, enc=21B
    30003: "Termos do Mundo",                 # cap=40B, enc=31B

    # =========================================================================
    # SLUS/TEXT/0424 (IDs 30004 a 30027): Menus de Configuração e Monólogos/Diálogos de Lyner e Jack (Floresta Cello, Sr. Pochoma, Garotas)
    # =========================================================================
    30004: "EscolhaIM04 Pág.IM05 VoltaIM01",  # cap=64B, enc=62B
    30005: "EscolherIM04 MudarIM05 FimIM01",  # cap=64B, enc=61B
    30006: "Inglês",                          # cap=16B, enc=14B
    30007: "Japonês",                         # cap=24B, enc=16B
    30008: "Lenta",                           # cap=16B, enc=11B
    30009: "Minha nave... Não poderei voltar a Platina sem ela...", # cap=112B, enc=109B
    30010: "A garota do lenço... Será que ela mora por aqui?", # cap=136B, enc=101B
    30011: "Primeiro, preciso procurar onde haja gente...", # cap=120B, enc=93B
    30012: "Tinha certeza de que era ela... Me enganei?", # cap=104B, enc=91B
    30013: "Preciso correr, ou vão vender minha aeronave!", # cap=104B, enc=95B
    30014: "A fera azul da Floresta Cello. Vou acabar com ela!", # cap=168B, enc=105B
    30015: "Voltemos à pousada. Precisamos de um plano para derrotá-los.", # cap=184B, enc=123B
    30016: "Rápido, Lyner! Ver a garota... digo, o Sr. Pochoma!", # cap=128B, enc=105B (resolvido overflow legado)
    30017: "Preciso aprender Grathmeld com o Sr. Pochoma.", # cap=96B, enc=91B
    30018: "Criar um Míssil? Só de ser lição de casa já dá preguiça...", # cap=128B, enc=119B
    30019: "Vou descontar o fora que levei naquele lobo azul!!", # cap=144B, enc=103B
    30020: "Depressa! Temos de recuperar a nave antes que a vendam!", # cap=128B, enc=111B
    30021: "Nemo é uma metrópole perto do vilarejo de Karulu.", # cap=128B, enc=99B
    30022: "Venha, vou guiar você pela cidade de Nemo.", # cap=96B, enc=87B
    30023: "Ei, nós vamos à Igreja, não vamos?", # cap=80B, enc=71B
    30024: "A pousada pode esperar. Vamos dar uma volta na cidade!", # cap=128B, enc=111B
    30025: "Maldito Jack. Só pensa em garotas...", # cap=96B, enc=73B (resolvido overflow legado)
    30026: "O que aquele sujeito queria comigo?", # cap=80B, enc=71B (resolvido overflow legado)
    30027: "Vamos sair daqui. Mais tarde farei você se lembrar de mim!", # cap=144B, enc=121B

    # =========================================================================
    # SLUS/TEXT/0425 (IDs 30028 a 30051): Diálogos de Aurica, Krusche e Lyner (Beco Vagalume, Gerador, Magia Verde, Colina do Canto)
    # =========================================================================
    30028: "Lyner idiota! Não ligo para o que te acontecer!!", # cap=104B, enc=97B
    30029: "Depressa, temos de fugir daqui logo!", # cap=80B, enc=75B
    30030: "Depressa para o porto!",          # cap=48B, enc=45B (resolvido overflow legado)
    30031: "Nesse caso, usarei meu atalho secreto. Voltemos ao Gerador!", # cap=192B, enc=121B
    30032: "Vamos logo!",                     # cap=24B, enc=23B (resolvido overflow legado)
    30033: "A informante vende Bala Felina na rua principal do Beco.", # cap=152B, enc=115B
    30034: "Vamos voltar logo ao Gerador.",    # cap=80B, enc=61B
    30035: "Vamos logo à Loja de Mergulho! Não me faça repetir...", # cap=144B, enc=109B
    30036: "Destrua a parede com a magia recém-aprendida!", # cap=112B, enc=93B
    30037: "Depressa. Passando daqui, estaremos bem mais seguros.", # cap=120B, enc=107B
    30038: "Ai... Subir tudo isso é exaustivo demais...", # cap=96B, enc=91B (ZERO rubricas, substitui *sigh* legado)
    30039: "Vamos subir a Torre logo.",       # cap=72B, enc=53B
    30040: "Achar a sala de controle? Mas este andar parece imenso...", # cap=160B, enc=115B
    30041: "Use a Magia Verde que aprendeu. Ela deve ativá-lo.", # cap=136B, enc=101B
    30042: "Depressa para o Cais Flutuante!", # cap=80B, enc=65B
    30043: "Não importa se voa! Minha Magia de Canção o derruba num golpe!!", # cap=184B, enc=131B
    30044: "Enfim um respiro. Agora nos levem à cidade de Nemo.", # cap=120B, enc=103B
    30045: "Vamos andar por aí. Talvez encontremos algo.", # cap=104B, enc=91B
    30046: "Rápido, ruínas! Pode haver pistas para escapar!", # cap=128B, enc=97B
    30047: "Vamos sair logo daqui. Estou ficando cansada.", # cap=104B, enc=91B
    30048: "O que vamos fazer agora?",        # cap=64B, enc=49B
    30049: "Vamos à Igreja.",                 # cap=48B, enc=31B
    30050: "Colina do Canto... Como será lá?", # cap=80B, enc=67B
    30051: "Tomara que ache o que busca na Colina do Canto.", # cap=136B, enc=97B

    # =========================================================================
    # SLUS/TEXT/0426 (IDs 30052 to 30075): Diálogos de Exploração e Missões (Aurica, Floresta Viola, Placa Hexagonal, Silvaplate, Em Pheyna, Tigela Felina, Olho Congelado)
    # =========================================================================
    30052: "Se busca o cristal, é melhor nos apressarmos.", # cap=104B, enc=93B
    30053: "Mais um nível... Onde será que desço?", # cap=80B, enc=75B
    30054: "Aurica, cadê você!?",             # cap=48B, enc=39B (resolvido overflow legado)
    30055: "Pode me acompanhar à Igreja? Devo reportar meu retorno.", # cap=144B, enc=113B
    30056: "Não quer ver sua nave na Floresta Viola?", # cap=120B, enc=83B
    30057: "Devo entregar o Fragmento Yuteria à Claire.", # cap=104B, enc=91B
    30058: "Fazer uma Corda de Yuteria... Parece penoso.", # cap=104B, enc=93B
    30059: "Talvez eu dê uma caminhada no parque.", # cap=80B, enc=75B
    30060: "Lyner, depressa à Placa Hexagonal! Salvemos Misha!!", # cap=128B, enc=105B (resolvido overflow legado)
    30061: "Depois da Colina do Canto, só ruínas caindo aos pedaços...", # cap=144B, enc=121B
    30062: "Lyner, podemos ir à Igreja primeiro?", # cap=80B, enc=73B (resolvido overflow legado)
    30063: "Certo, vamos a Silvaplate!",      # cap=72B, enc=55B
    30064: "Escalar Silvaplate parece pior que escalar montanhas.", # cap=128B, enc=107B
    30065: "Se subirmos por aqui, passaremos em Em Pheyna?", # cap=136B, enc=95B
    30066: "Vamos ao Grande Santuário!",      # cap=72B, enc=55B
    30067: "A Provação da Lua é no templo. Vamos liquidar isso!", # cap=136B, enc=107B
    30068: "Lyner, vou me esforçar!",         # cap=48B, enc=47B (resolvido overflow legado)
    30069: "Bem, vamos ao Santuário!",        # cap=72B, enc=53B
    30070: "O Yulastrino deve estar no templo.", # cap=80B, enc=71B
    30071: "Se juntou os itens, monte logo o Teleporte Circula!", # cap=176B, enc=107B
    30072: "Tomara que Tastiella aprove a Tigela Felina.", # cap=96B, enc=89B (resolvido overflow legado)
    30073: "Agora, ao Olho Congelado. Platina está logo ali.", # cap=120B, enc=101B
    30074: "Passando daqui, estaremos em Platina!!", # cap=88B, enc=79B
    30075: "Deixe de criancice e vamos logo à Catedral!!", # cap=136B, enc=91B

    # =========================================================================
    # SLUS/TEXT/0427 (IDs 30076 to 30099): Diálogos de Progressão e Exploração (Catedral, Altar dos Apóstolos, Loja de Mergulho, Tastiella, Tubulação, Lab Tenba)
    # =========================================================================
    30076: "Terminado o download, vá à Catedral. Não esqueça.", # cap=104B, enc=101B
    30077: "Certo, vamos ao Altar dos Apóstolos!!", # cap=88B, enc=77B
    30078: "Rápido à Loja de Mergulho!",      # cap=56B, enc=55B (resolvido overflow legado)
    30079: "Vejamos, o que vou te mostrar?",  # cap=64B, enc=61B
    30080: "Vamos ver o pessoal e pensar melhor nisso...", # cap=112B, enc=91B
    30081: "Onde Aurica foi? Acho que vou ao Gather ver.", # cap=120B, enc=89B
    30082: "Devo ir ao Altar onde Shurelia espera. Ou me preparo?", # cap=176B, enc=107B
    30083: "Vamos a Em Pheyna. Quero avisar que entrei nas buscas.", # cap=160B, enc=111B
    30084: "A Crônica Crescente fica sobre Em Pheyna.", # cap=104B, enc=83B
    30085: "Vamos logo ver a Tastiella.",     # cap=64B, enc=55B
    30086: "Primeiro Nemo, depois o Beco Vagalume.", # cap=136B, enc=77B
    30087: "Nada a fazer na tempestade. Planejemos na pousada.", # cap=136B, enc=103B
    30088: "Lyner, quer ir lá fora um instante?", # cap=88B, enc=71B
    30089: "Lyner! Quando brincar, divirta-se ao máximo!!", # cap=128B, enc=91B
    30090: "Dizem que a fenda para a Torre fica em Silvaplate.", # cap=120B, enc=103B
    30091: "Vamos subir mais um pouco.",      # cap=64B, enc=53B
    30092: "Conseguimos entrar, então tudo bem!", # cap=80B, enc=72B
    30093: "O jeito é continuar descendo sem parar.", # cap=88B, enc=80B
    30094: "Que tempestade lá fora. Teremos de ir pela Torre...", # cap=136B, enc=105B
    30095: "Passando a Tubulação, é o bom Beco Vagalume!", # cap=120B, enc=93B
    30096: "Deixe comigo: guiarei vocês ao Laboratório Tenba.", # cap=112B, enc=101B
    30097: "Ir àquele portão sem a Misha é muito arriscado...", # cap=128B, enc=101B
    30098: "Ao Gerador! Vou compensar todo aquele descanso!", # cap=152B, enc=95B
    30099: "Idiota! Parem de enrolar e vamos ao porto!", # cap=112B, enc=87B

    # =========================================================================
    # SLUS/TEXT/0428 (IDs 30100 to 30123): Clímax de Missão e Navegação de Campo (Placa Hexagonal, Corte de Energia, Lab Tenba, Platina, Bispo, Corredor Musical)
    # =========================================================================
    30100: "Depressa à Placa Hexagonal, ou o perderemos!", # cap=144B, enc=91B
    30101: "Será que a Misha ainda está lá?",  # cap=72B, enc=63B
    30102: "Com Misha de volta, cortemos o Poder Sinfônico!", # cap=112B, enc=95B (resolvido overflow legado)
    30103: "Rápido! Se religarem a força, não passaremos da porta!", # cap=160B, enc=109B
    30104: "A energia voltou, mas demos um jeito. Vamos em frente!", # cap=128B, enc=107B
    30105: "Depressa. O fundo do laboratório fica logo adiante.", # cap=112B, enc=104B (resolvido overflow legado)
    30106: "Lyner, você não ia me devolver o cristal?", # cap=112B, enc=85B
    30107: "Vamos pegar a nave e voar até Nemo!", # cap=88B, enc=73B
    30108: "Vamos subir na nave e ir a Nemo!", # cap=80B, enc=67B
    30109: "A cidade parece estranha. Vamos à Igreja ver!", # cap=120B, enc=91B
    30110: "Depressa para Em Pheyna!!",       # cap=56B, enc=51B
    30111: "Depressa à Crônica Crescente ou será tarde!!", # cap=136B, enc=91B
    30112: "Não há tempo! Ao altar da Crônica Crescente!!", # cap=120B, enc=93B
    30113: "Os Cavaleiros da Igreja me preocupam. Voltemos a Platina.", # cap=120B, enc=115B (resolvido overflow legado)
    30114: "Com as coisas calmas, vejamos a cidade. Como estará a loja?", # cap=192B, enc=121B
    30115: "Podemos ir à Igreja? Preciso falar com o bispo.", # cap=120B, enc=95B
    30116: "Vamos reunir dados sobre a tempestade.", # cap=96B, enc=79B
    30117: "Ei, Lyner. Que tal darmos uma volta?", # cap=88B, enc=71B
    30118: "Compre ingredientes no empório da Av. Hoshinose.", # cap=144B, enc=101B
    30119: "Passemos o tempo na cidade até o bispo retornar.", # cap=128B, enc=101B
    30120: "Vamos checar se as portas de Silvaplate se abrem.", # cap=128B, enc=99B
    30121: "Depressa ao Corredor Musical, antes que o tempo piore!", # cap=168B, enc=109B
    30122: "Primeiro, achemos o controle do Corredor Musical.", # cap=136B, enc=101B
    30123: "Temos de ajustar a Placa Hexagonal. Há um teleporte do outro lado, vamos lá!", # cap=256B, enc=155B
}


def build_output():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    dialogues_out = []
    curated_dialogues_out = []
    overflows = []
    hard_gate_errors = []

    for d in input_data["dialogues"]:
        d_id = d["id"]
        jp = d.get("original_jp", "")
        en = d.get("original_en", "")
        orig_pt = d.get("current_ptbr", "")

        cur.execute("SELECT original_bytes FROM dialogues WHERE id = ?", (d_id,))
        row = cur.fetchone()
        cap = row[0] if row else 0

        # Seleciona texto curado
        if d_id in CURATED_DATA:
            curated = CURATED_DATA[d_id]
            verdict = "rewritten"
        else:
            curated = orig_pt
            verdict = "approved_as_is"

        enc = encoded_size(curated) if curated else 0

        if cap and enc > cap:
            overflows.append((d_id, curated, enc, cap))

        errs = validate_line(d_id, en, curated)
        if errs:
            hard_gate_errors.append((d_id, errs))

        rationale = f"Curadoria lapidada sob soberania do JP ('{jp[:30]}...'). Paridade de tags e buffer rigoroso ({enc}B/{cap}B)."

        dialogues_out.append({
            "id": d_id,
            "original_jp": jp,
            "original_en": en,
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
        "block_id": "BLK_SYS_034",
        "axis_id": "AXIS_1",
        "axis_name": "1_NUCLEO_SISTEMICO_E_MENUS",
        "category": "Executable Strings",
        "line_count": len(dialogues_out),
        "id_range": [29836, 30123],
        "curator_notes": (
            "Curadoria Editorial em Duas Passagens para BLK_SYS_034 sob soberania estrita do texto japonês e framework "
            "canônico curadoria-editorial-game-localization v4.1.0. Abrange os verbetes enciclopédicos vitais da história, "
            "tecnologia e mitologia de Sol Ciel (Ar Tonelicards, Povo Teru, A.B.R., Harmonics, Classes A~D, Trio de Elemia, "
            "Mergulho na Cosmosfera, Prolongadores de Vida, Bala Felina, Beco Vagalume, Autenticação de Espectro FFT, Portões Divisores, "
            "Menu Dokkoi, Deusa Tyria, Blastline, Inferia Grathnode, Ston, Yuteria, Poder Sinfônico, Pedra-canto, Corredor Musical, "
            "Portão Pheyna, Voz Estelar / Star Singer, Chronicle Key, Batismo de Circula, Stonetree, Elemia Oath, Código Hino, Download, "
            "Asas de Horus, Lenda de Elemia, Crônica Crescente, Reyvateils Beta e 3ª Geração, Flipper, Reator Nuclear, Power Cylinder, "
            "Babango, Installer Port, Estátua da Cantora e do Protetor, Nabite Cap, Divisor FFT, Reyvateils Origem, Zona Ardelberg, "
            "Reator Sinfônico, Projeto Mir, Aeronave Gungnir, Sino Plasma, Robôs de Manutenção e ELMA), bem como os diálogos "
            "sistêmicos e de campo dos protagonistas em eventos críticos de progressão (SLUS/TEXT/0417 a 0428). "
            "Rigorosa observância métrica: 28 estouros de buffer legados erradicados com 100% de precisão (0 estouros restantes), "
            "zero rubricas cênicas (*suspiro*, etc.), paridade absoluta de quebras de linha/tags e aprovação unânime no Hard Gate."
        ),
        "scene_handoff_received": input_data.get("scene_handoff_received", {}),
        "scene_handoff_final": {
            "last_scene_id": "BLK_SYS_034",
            "last_line_id": 30123,
            "location_and_situation": (
                "Núcleo Sistêmico Parte 34 (SLUS/TEXT/0417 a 0428: Enciclopédia canônica de lore, conceitos de Sol Ciel, "
                "terminologia de mundo e diálogos de navegação/missão de campo) concluído com soberania absoluta do texto japonês, "
                "eliminação de 28 estouros de buffer legados, erradicação de decalques e aprovação 100% limpa no Hard Gate Técnico."
            ),
            "emotional_state": "Solenidade Mitológica, Rigor Enciclopédico e Fluidez Literária Exemplar.",
            "active_hooks": [
                "Conclusão integral do bloco BLK_SYS_034 (IDs 29836 a 30123).",
                "Enciclopédia de lore e termos de mundo plenamente consolidados para os blocos subsequentes de sistema e eventos."
            ]
        },
        "new_terms": {
            "Ar Tonelicard": {
                "pt": "Ar Tonelicard",
                "category": "Lore / Sistema",
                "note": "Termo canônico para a coleção de cartas do mundo (アルトレカ)."
            },
            "Menu Dokkoi": {
                "pt": "Menu Dokkoi",
                "category": "Culinária / Item",
                "note": "Adaptação canônica concisa de Dokkoi Set (ドッコイ定食) com 23B/24B de buffer."
            },
            "Ston (unid)": {
                "pt": "Ston (unid)",
                "category": "Medida / Lore",
                "note": "Unidade de medida de distância de Sol Ciel (ストン(単位)) com 23B/24B de buffer."
            },
            "P. Pheyna": {
                "pt": "P. Pheyna",
                "category": "Toponímia / Local",
                "note": "Padronização do Portão de Pheyna com 19B/24B em paridade estrita com BLK_SYS_031 ID 29186."
            },
            "Voz Estelar": {
                "pt": "Voz Estelar",
                "category": "Alcunha / Sacerdócio",
                "note": "Título canônico sagrado de Misha (星詠 / Star Singer) adaptado com 23B/24B de buffer."
            },
            "Stonetree": {
                "pt": "Stonetree",
                "category": "Botânica / Arquitetura",
                "note": "Rocha viva de Em Pheyna (石木) com 19B/24B de buffer."
            },
            "Elemia Oath": {
                "pt": "Elemia Oath",
                "category": "Lore / História",
                "note": "Tratado sagrado de Sol Ciel (エレミア誓約書) adaptado com 23B/24B de buffer."
            },
            "Código Hino": {
                "pt": "Código Hino",
                "category": "Hymmnos / Sistema",
                "note": "Identificador da Reyvateil (ヒュムネコード) com 23B/24B em conformidade com o texto descritivo."
            },
            "Sino Plasma": {
                "pt": "Sino Plasma",
                "category": "Toponímia / Tecnologia",
                "note": "Dispositivo estabilizador de gravidade (プラズマベル) com 23B/24B em harmonia com ID 21368."
            }
        },
        "highlights": [
            "Erradicação de 28 estouros de buffer legados da tradução preliminar em termos vitais de lore e comandos de campo.",
            "Substituição sistemática do decalque 'Espaço da Alma' pelo termo canônico 'Cosmosfera' e conformidade com a mitologia de Sol Ciel.",
            "Verbetes enciclopédicos lapidados em prosa literária nobre, resgatando a densidade mitológica, científica e poética do original japonês.",
            "Diálogos de navegação e exploração de Lyner, Jack, Aurica e Krusche afinados com suas vozes autênticas e zero rubricas teatrais."
        ],
        "curated_dialogues": curated_dialogues_out,
        "dialogues": dialogues_out
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Arquivo de saída gravado com sucesso em: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_output()

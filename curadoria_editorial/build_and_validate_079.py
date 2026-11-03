# -*- coding: utf-8 -*-
"""
build_and_validate_079.py - Constrói e valida BLK_EVD_079_output.json
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_079_input.json")
output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_079_output.json")

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

curated_dict = {
    # ==================== Event/147.evd (IDs 17835 - 17900) ====================
    17835: {
        "text": "O que é isto...?",
        "notes": "Radolf estupefato ao encontrar as câmaras de experimentos secretos da Tenba."
    },
    17836: {
        "text": "É a divisão onde realizávamos experimentos\npara amplificar as habilidades das Reyvateils.",
        "notes": "Bourd detalhando com cinismo e orgulho corporativo os testes desumanos em Reyvateils."
    },
    17837: {
        "text": "Bourd!",
        "notes": "Radolf reagindo com ódio incontido à aparição de Bourd."
    },
    17838: {
        "text": "Seus canalhas... Como ousam submeter as Reyvateils\na um tratamento tão desumano outra vez?!",
        "notes": "Radolf denunciando veementemente a crueldade sistemática da Tenba contra as Reyvateils."
    },
    17839: {
        "text": "Uma Reyvateil só tem razão de existir\nse for poderosa.",
        "notes": "Bourd expondo a ideologia utilitarista e perversa da corporação Tenba."
    },
    17840: {
        "text": "Nós só estamos conduzindo uma pesquisa\nque é do mais absoluto interesse delas. Não concorda?!",
        "notes": "Bourd tripudiando com deboche sádico."
    },
    17841: {
        "text": "...Você enlouqueceu de vez\nou está falando sério...?",
        "notes": "Lyner atônito diante do cinismo escancarado de Bourd."
    },
    17842: {
        "text": "Os podres de uma corporação sem escrúpulos\nescarrapachados bem na nossa frente... É dose.",
        "notes": "Jack com desdém de mercenário calejado vendo os bastidores sujos da Tenba."
    },
    17843: {
        "text": "Tantas atrocidades cometidas contra as Reyvateils...\nIsso é imperdoável! Vou acertar as contas com você aqui e agora!",
        "notes": "Radolf empunhando sua arma para pôr um fim aos crimes de Bourd."
    },
    17844: {
        "text": "Ora, que divertido, Radolf!\nHouve dia melhor para transformar este lugar na sua cova?!",
        "notes": "Bourd aceitando o desafio com provocação sanguinária."
    },
    17845: {
        "text": "Ambos, contenham-se!",
        "notes": "A Presidente Ayano intervindo com autoridade máxima indiscutível."
    },
    17846: {
        "text": "Senhora Presidente.",
        "notes": "Bourd recuando imediatamente sob a presença imponente de sua líder executiva."
    },
    17847: {
        "text": "Misha...",
        "notes": "Lyner avistando Misha ao lado da presidente corporativa."
    },
    17848: {
        "text": "Misha?!",
        "notes": "Jack em choque ao reencontrar a protegida de infância."
    },
    17849: {
        "text": "Lyner...\nE... Maninho Harm...?!",
        "notes": "Misha reconhecendo atônita Lyner e Jack (pelo nome de infância Maninho Harm / アル兄ぃ)."
    },
    17850: {
        "text": "Fiquem longe da Reyvateil mais valiosa da Tenba.\nNão admito essa intimidade toda.",
        "notes": "Bourd intervindo para afastar os intrusos do trunfo corporativo da Tenba."
    },
    17851: {
        "text": "Este não é momento para lutas.\nNós também fomos vítimas dessa catástrofe. A nossa situação é a mesma.",
        "notes": "Presidente Ayano pacificando o confronto, reconhecendo que todos sofreram com a queda da Placa Hexagonal."
    },
    17852: {
        "text": "Presidente!",
        "notes": "Bourd protestando contrariado com a ordem de recuo."
    },
    17853: {
        "text": "Peço desculpas pela nossa recepção tão hostil.",
        "notes": "Ayano desculpando-se com elegância e diplomacia executiva."
    },
    17854: {
        "text": "Eu sou Ayano Raizer Elduke,\npresidente do Conglomerado Empresarial Tenba.",
        "notes": "Apresentação formal canônica da líder máxima da corporação Tenba."
    },
    17855: {
        "text": "A presidente da Tenba?!",
        "notes": "Lyner surpreso com o status daquela figura imponente."
    },
    17856: {
        "text": "Precisamente.",
        "notes": "Ayano confirmando com sobriedade."
    },
    17857: {
        "text": "Seja por qual motivo for,\nagradeço pelo socorro prestado à nossa Tenba diante da tragédia.",
        "notes": "Ayano agradecendo diplomaticamente pelos esforços de resgate prestados ao grupo corporativo."
    },
    17858: {
        "text": "Senhor Radolf, os seus valorosos feitos\ncomo a lâmina da Igreja sempre chegam aos meus ouvidos.",
        "notes": "Ayano dirigindo-se respeitosamente a Radolf Schnaider, reconhecendo sua honra como espada clerical."
    },
    17859: {
        "text": "Mas, apenas por hoje,\npoderia ter a benevolência de relevar a situação?",
        "notes": "Ayano propondo uma trégua estratégica e digna."
    },
    17860: {
        "text": "Quanta conveniência...",
        "notes": "Radolf desconfiado da audácia calculista da proposta."
    },
    17861: {
        "text": "Tenho plena consciência da minha audácia.\nE é exatamente por isso que proponho esta trégua. Poderia aceitar?",
        "notes": "Ayano argumentando com franqueza cortês e visão pragmática sem eco em mente."
    },
    17862: {
        "text": "Compreendo. Pelo bem de ambos os lados,\nconcordo em recuar por enquanto.",
        "notes": "Radolf aceitando cessar as hostilidades para evitar baixas desnecessárias após o desastre."
    },
    17863: {
        "text": "Sou-lhe imensamente grata pela sua ponderação.",
        "notes": "Ayano demonstrando gratidão pela maturidade do comandante de Elemia."
    },
    17864: {
        "text": "Agora, vamos andando.",
        "notes": "Ayano ordenando a retirada da comitiva de Tenba."
    },
    17865: {
        "text": "Sim, senhora.",
        "notes": "Bourd obedecendo de má vontade."
    },
    17866: {
        "text": "Misha!",
        "notes": "Jack tentando alcançar Misha antes que ela parta."
    },
    17867: {
        "text": "...Maninho Harm.",
        "notes": "Misha despedindo-se com carinho e dor contida."
    },
    17868: {
        "text": "Misha... Você...\nÉ realmente a Misha?!",
        "notes": "Jack confuso e atordoado ao fitar a garota."
    },
    17869: {
        "text": "...",
        "notes": "Misha calando-se para proteger seus segredos."
    },
    17870: {
        "text": "O que houve, Misha?",
        "notes": "Ayano percebendo o atraso e chamando a menina com gentileza."
    },
    17871: {
        "text": "Não... não é nada.",
        "notes": "Misha disfarçando sua turbulência emocional."
    },
    17872: {
        "text": "Compreendo. Então, com sua licença.",
        "notes": "Ayano despedindo-se com reverência formal."
    },
    17873: {
        "text": "Misha, por que você...\nÉ mesmo... mesmo a Misha...?",
        "notes": "Jack perplexo diante da aparência inalterada da jovem."
    },
    17874: {
        "text": "...Jack. Não é como se a Misha\nestivesse falando sério sobre aquilo.",
        "notes": "Lyner tentando acalmar o amigo veterano."
    },
    17875: {
        "text": "Ela provavelmente só está mentindo para nós\na fim de manter a Tenba desatenta...",
        "notes": "Lyner deduzindo uma encenação tática por parte de Misha."
    },
    17876: {
        "text": "Não é isso!\nNão estou falando nesse sentido!",
        "notes": "Jack corrigindo energicamente o equívoco de Lyner."
    },
    17877: {
        "text": "Se a minha memória não falha...\na Misha já deveria ter dezoito anos agora.",
        "notes": "Jack revelando o mistério cronológico que abala o grupo."
    },
    17878: {
        "text": "E mesmo assim...\nela não cresceu absolutamente nada...",
        "notes": "Jack apontando que Misha parece estagnada na infância."
    },
    17879: {
        "text": "...O quê?!",
        "notes": "Lyner em choque com a revelação da verdadeira idade de Misha."
    },
    17880: {
        "text": "Ela continua rigorosamente a mesma\nde quando a vi pela última vez, há seis anos!",
        "notes": "Jack atestando a paralisação do crescimento biológico de Misha."
    },
    17881: {
        "text": "...Como assim? O que isso significa...?",
        "notes": "Lyner tentando digerir o enigma inacreditável."
    },
    17882: {
        "text": "Não faço ideia. O ideal seria perguntar\ndiretamente a ela, mas...",
        "notes": "Jack impotente diante das circunstâncias da separação."
    },
    17883: {
        "text": "Ficar parados aqui não vai resolver nada.\nVamos voltar para a pousada.",
        "notes": "Krusche restaurando o foco prático do grupo."
    },
    17884: {
        "text": "Pessoal, me perdoem...\nMas eu vou subir a Torre agora mesmo.",
        "notes": "Lyner tomando uma decisão heroica urgente diante da escalada do perigo."
    },
    17885: {
        "text": "Lyner...!?\nO que deu em você de repente?!",
        "notes": "Radolf surpreso com a súbita determinação do jovem cavaleiro."
    },
    17886: {
        "text": "Depois de tudo o que houve, ficou claro\nque não temos nem mais um segundo a perder.",
        "notes": "Lyner ciente do agravamento das perturbações na Torre de Ar tonelico."
    },
    17887: {
        "text": "A queda da Placa Hexagonal,\nos Guardiões nos atacando do nada...",
        "notes": "Lyner conectando os recentes desastres à crise sistêmica."
    },
    17888: {
        "text": "Tudo isso tem uma única causa:\nos tais vírus que infestam o interior da Torre.",
        "notes": "Lyner diagnosticando a corrupção viral como origem das catástrofes."
    },
    17889: {
        "text": "...Vírus. Você já tinha falado deles antes, não é?",
        "notes": "Krusche recordando os avisos prévios de Lyner."
    },
    17890: {
        "text": "Este cristal Purger que lutei tanto para conseguir\nserve justamente para combater os vírus.",
        "notes": "Lyner reafirmando o propósito do Cristal Hymmnos Purger."
    },
    17891: {
        "text": "Só que a situação não vai mudar em nada\nenquanto eu não conseguir levá-lo de volta a Platina.",
        "notes": "Lyner destacando o dever de entregar a vacina ao topo da Torre."
    },
    17892: {
        "text": "...",
        "notes": "Aurica em silêncio compungido perante a partida iminente de Lyner."
    },
    17893: {
        "text": "...",
        "notes": "Jack ponderando a gravidade da conjuntura."
    },
    17894: {
        "text": "Eu acabei baixando a guarda por tempo demais.",
        "notes": "Lyner assumindo a responsabilidade pela hesitação anterior."
    },
    17895: {
        "text": "Eu vou... começar a subir a Torre agora mesmo.",
        "notes": "Lyner reafirmando sua partida inegociável rumo a Platina."
    },
    17896: {
        "text": "Eu me preocupo com a Misha...\ne temos um mar de outros problemas, mas...",
        "notes": "Lyner dilacerado entre o afeto pessoal e a salvação do mundo."
    },
    17897: {
        "text": "Se eu não entregar o Purger em Platina primeiro,\nninguém sabe que outra catástrofe pode acontecer...",
        "notes": "Lyner ciente de que sem o Purger toda a civilização sucumbirá."
    },
    17898: {
        "text": "Entendo. Mas, antes de partir,\npoderia nos conceder uma última visita à Igreja?",
        "notes": "Radolf solicitando uma audiência de despedida no templo clerical."
    },
    17899: {
        "text": "Com certeza. A Igreja cuidou tão bem de mim,\no mínimo que posso fazer é deixar meus agradecimentos...",
        "notes": "Lyner retribuindo a acolhida com honra e nobreza de espírito."
    },
    17900: {
        "text": "Muito obrigado. Sendo assim, vamos?",
        "notes": "Radolf agradecendo e conduzindo o grupo de partida."
    },

    # ==================== Event/603.evd (IDs 17901 - 17939) ====================
    17901: {
        "text": "A cidade está toda branca...\nMas é exatamente como a Misha disse:\nquando a neve cai, o mundo fica mais claro e iluminado.",
        "notes": "Lyner contemplando a paisagem nevada no Nível 3 da Cosmosfera de Misha."
    },
    17902: {
        "text": "E sem dúvida tem uma beleza fantástica...\nEmbora faça um bocado de frio aqui fora.",
        "notes": "Lyner apreciando a atmosfera etérea, mas sentindo o rigor da baixa temperatura."
    },
    17903: {
        "text": "C-com licença...",
        "notes": "Aurica aparecendo trêmula e desamparada em meio à nevasca onírica."
    },
    17904: {
        "text": "Uau! A-Aurica!?\nO que houve com você? E que roupa é essa...?!",
        "notes": "Lyner chocado ao ver Aurica com vestimentas inadequadas para o gelo."
    },
    17905: {
        "text": "Q-que frio... Estou congelando...",
        "notes": "Aurica tiritando de frio na mente de Misha."
    },
    17906: {
        "text": "Mas é claro que vai passar frio vestida desse jeito...",
        "notes": "Lyner repreendendo o figurino de verão em pleno inverno."
    },
    17907: {
        "text": "Lyner?!",
        "notes": "Misha manifestando-se como habitante local da Cosmosfera."
    },
    17908: {
        "text": "Você veio! Que alegria!\nOlha só, olha só! Esta neve não é linda?",
        "notes": "Misha radiante ao ver seu convidado de Dive contemplando sua neve onírica."
    },
    17909: {
        "text": "E-espera um pouco!\nQue visual é esse...?! E você encolheu de novo...",
        "notes": "Lyner estupefato com a persona infantil e o figurino místico de Fada da Canção de Misha."
    },
    17910: {
        "text": "Você... por acaso seria a Fada da Canção?!\nPor favor, Fada da Canção, ouça o meu pedido! Estou com tanto frio... Poderia me dar algo para me aquecer...?",
        "notes": "Aurica implorando por auxílio à manifestação mitológica da Cosmosfera."
    },
    17911: {
        "text": "F-Fada da Canção?!",
        "notes": "Lyner sem compreender o papel alegórico atribuído a Misha."
    },
    17912: {
        "text": "...\nO quê? Tá com frio aí, humana?\nTá bom, eu realizo o seu desejo, mas depois suma da minha frente.",
        "notes": "Misha com postura desdenhosa e impaciente atendendo à humana forasteira."
    },
    17913: {
        "text": "Chamou por mim, Senhora Misha?",
        "notes": "Guarda Gelo (氷護) manifestando-se prontamente ao chamado da sua mestra."
    },
    17914: {
        "text": "Guarda Gelo. Essa humana está morrendo de frio.\nÉ a sua especialidade, não é? Dá um jeito de aquecê-la.",
        "notes": "Misha ordenando ao seu servo onírico que resolva o desconforto de Aurica."
    },
    17915: {
        "text": "Às suas ordens!\nHaaah!!",
        "notes": "Guarda Gelo liberando seu calor mágico benevolente."
    },
    17916: {
        "text": "Uau... Ficou tão quentinho!\nSenhora Fada da Canção, muito obrigada!",
        "notes": "Aurica confortada e transbordando gratidão."
    },
    17917: {
        "text": "E-ei, Aurica...?!",
        "notes": "Lyner boquiaberto vendo a saída repentina da donzela aquecida."
    },
    17918: {
        "text": "Francamente, viu...\nPor que cargas d'água eu tenho que entoar magias\npara uma garota que nem sequer conheço...?",
        "notes": "Misha resmungando indignada com a obrigação de servir estranhos."
    },
    17919: {
        "text": "Misha...?\nÉ... o que seria essa tal 'Fada da Canção'?",
        "notes": "Lyner interrogando a natureza simbólica daquela identidade onírica."
    },
    17920: {
        "text": "Fada da Canção é uma raça que se desgasta dia após dia,\nsacrificando a própria vida para realizar os desejos dos humanos.\nE agora, sou eu que estou nesse papel.",
        "notes": "Misha desvelando a terrível metáfora psicológica de seu trauma como Reyvateil utilitária."
    },
    17921: {
        "text": "Mas eu já estou de saco cheio dessa história de Fada da Canção!\nQue graça tem em ficar realizando os desejos\nde humanos que nunca vi na vida?!",
        "notes": "Misha expressando sua revolta legítima contra o sacrifício imposto à sua infância."
    },
    17922: {
        "text": "Ah... Como eu queria ser uma humana de verdade...",
        "notes": "O anseio visceral e doloroso de Misha por humanidade e liberdade plena."
    },
    17923: {
        "text": "Ué? Mas você também é humana, Misha!",
        "notes": "Lyner tentando confortá-la sob a perspectiva do mundo exterior."
    },
    17924: {
        "text": "Do que você tá falando?!\nEu já disse que sou a Fada da Canção!\nFadas da Canção são totalmente diferentes de humanos!",
        "notes": "Misha refutando energicamente a negação de seu estatuto alienado."
    },
    17925: {
        "text": "Uma Fada da Canção...\né apenas uma máquina fabricada... para servir aos humanos.",
        "notes": "O trauma nuclear de Misha: a desumanização de ser tratada como mera máquina biológica de canções."
    },
    17926: {
        "text": "(Lá vem mais uma encrenca daquelas...)",
        "notes": "Lyner percebendo a magnitude do conflito existencial a ser desatado na Cosmosfera."
    },
    17927: {
        "text": "Já sei! Lyner, tenho um pedido!\nMe ajuda a me transformar em humana!\nEu não aguento mais ser a Fada da Canção! Eu quero ser humana!",
        "notes": "Misha clamando desesperadamente pelo apoio de Lyner para conquistar sua emancipação."
    },
    17928: {
        "text": "Ai! M-mas que pedido repentino foi esse...?\nMesmo que você me peça isso,\no que é que eu posso fazer?!",
        "notes": "Lyner atordoado com o desafio incomum colocado à sua frente."
    },
    17929: {
        "text": "Só existe um único método\npara uma Fada da Canção se tornar humana.",
        "notes": "Misha revelando a premissa da busca onírica deste nível mental."
    },
    17930: {
        "text": "É tomar o elixir guardado pelo eremita chamado 'Yakuan',\nque vive nas montanhas! Esse é o remédio supremo,\ncapaz de curar qualquer mal e realizar qualquer desejo!",
        "notes": "Misha citando o remédio milagroso de Yakuan (薬庵), o eremita lendário das montanhas."
    },
    17931: {
        "text": "Nossa... Que remédio extraordinário...",
        "notes": "Lyner impressionado com as propriedades fabulosas do medicamento."
    },
    17932: {
        "text": "Então, eu só preciso subir até a montanha, mas...\nVocê não iria comigo?",
        "notes": "Misha pedindo carinhosamente a companhia protetora de Lyner na jornada."
    },
    17933: {
        "text": "Bem, por mim... tudo bem...",
        "notes": "Lyner aceitando com lealdade guiar sua amiga através das provações."
    },
    17934: {
        "text": "Ebaaa! Então tá combinado!",
        "notes": "Misha comemorando com euforia infantil e afetiva."
    },
    17935: {
        "text": "Você teceu a Magia Azul [Guarda Gelo]!",
        "notes": "Notificação canônica de síntese da Magia Azul Guarda Gelo (青魔法【氷護】)."
    },
    17936: {
        "text": "...Você aprontou mais uma das suas, hein?",
        "notes": "A Moradora do Mundo Inferior advertindo Lyner sobre as consequências de suas palavras involuntárias."
    },
    17937: {
        "text": "Hã?! C-como assim, o que foi que eu fiz?!",
        "notes": "Lyner assustado sem perceber o dano infligido à psique de Misha."
    },
    17938: {
        "text": "Você feriu os sentimentos da Misha sem nem perceber.\nÉ por isso que ela encolheu desse jeito outra vez.",
        "notes": "A guardiã psicológica explicando o mecanismo de regressão infantil por ferimento afetivo inconsciente."
    },
    17939: {
        "text": "F-foi isso...?",
        "notes": "Lyner percebendo a fragilidade comovente do coração de sua amiga."
    },

    # ==================== Event/228.evd (IDs 17940 - 17993) ====================
    17940: {
        "text": "M-mas o que é isto...?!",
        "notes": "Lyner assombrado ao vislumbrar o interior sagrado e imenso da Crônica Crescente."
    },
    17941: {
        "text": "Esta é a Crônica Crescente.\nO altar erguido para selar os vírus que infestam a Torre.",
        "notes": "Tastiella apresentando o santuário arcaico de contenção viral."
    },
    17942: {
        "text": "Num lugar desses...",
        "notes": "Lyner impactado pela atmosfera sagrada e opressiva do confinamento."
    },
    17943: {
        "text": "Sim. É aqui onde a Misha...",
        "notes": "Tastiella introduzindo o martírio histórico a que Misha foi submetida."
    },
    17944: {
        "text": "Onde a Reyvateil que herda a Linhagem Lünn entoa a sua canção,\nprotegendo o mundo contra a ameaça dos vírus.",
        "notes": "Tastiella explicando o sacrifício sacerdotal perpétuo da linhagem Lünn."
    },
    17945: {
        "text": "Sim. Eu sou a 31ª Lünn.\nMeu verdadeiro nome é Misha Arsellec Lünn...",
        "notes": "Misha proclamando com pesar seu nome canônico ancestral (彌紗・アルトセルク・リューン)."
    },
    17946: {
        "text": "Há muito tempo, houve uma grande guerra neste mundo.",
        "notes": "Tastiella rememorando o cataclismo histórico do passado de Sol Ciel."
    },
    17947: {
        "text": "Uma guerra colossal... entre humanos e Reyvateils.",
        "notes": "A Guerra das Reyvateils que redefiniu o destino do planeta."
    },
    17948: {
        "text": "Mir liderava o lado das Reyvateils rebeladas contra a humanidade.",
        "notes": "A insurreição da Reyvateil de Primeira Geração Mir contra a subjugação humana."
    },
    17949: {
        "text": "E nessa guerra, Mir fez metade do Continente Flutuante despencar,\nprovocando a pior das catástrofes.",
        "notes": "A tragédia histórica da queda de metade do Continente Flutuante (Silvaplate)."
    },
    17950: {
        "text": "E quem selou essa Mir... fui eu mesma.",
        "notes": "Tastiella revelando seu papel como executora do selamento ancestral."
    },
    17951: {
        "text": "E o meu verdadeiro corpo...\né esta colossal relíquia sagrada, a Crônica Crescente.",
        "notes": "A revelação ontológica de que Tastiella fundiu sua existência ao altar da Crônica Crescente."
    },
    17952: {
        "text": "O... o quê?!",
        "notes": "Lyner estarrecido com a identidade transcendente do monumento sagrado."
    },
    17953: {
        "text": "...Não me faça repetir.\nEsta Crônica Crescente é quem eu realmente sou.",
        "notes": "Tastiella reafirmando a dura verdade de sua fusão físico-espiritual."
    },
    17954: {
        "text": "A entidade chamada 'Tastiella'\nnão passa dos meus 'olhos' para observar o mundo.",
        "notes": "A projeção física de Tastiella atuando unicamente como receptáculo sensorial exterior."
    },
    17955: {
        "text": "Como assim?! A Tastiella não é uma Teru?!",
        "notes": "Lyner confuso confrontando a origem étnica e mitológica da sacerdotisa."
    },
    17956: {
        "text": "Parece que fui uma Teru no passado remoto.\nMas lembranças de tempos tão distantes já se apagaram da minha memória.",
        "notes": "Tastiella atestando a perda de sua individualidade mortal ao longo dos séculos."
    },
    17957: {
        "text": "A minha única missão é manter Mir confinada\npor toda a eternidade... Nada mais.",
        "notes": "O desígnio imutável que rege a existência da guardiã do altar."
    },
    17958: {
        "text": "E afinal de contas, quem ou o que é essa Mir?\nVocê disse que ela comandava as Reyvateils...",
        "notes": "Krusche questionando a natureza ontológica e periculosidade da entidade Mir."
    },
    17959: {
        "text": "...\nHoje em dia ela é apenas um vírus.\nUm corpo de energia puro, desprovido de forma física.",
        "notes": "Tastiella definindo Mir como uma massa colossal de energia e corrupção viral pura."
    },
    17960: {
        "text": "Exatamente como esta projeção de 'Tastiella' que serve de meus olhos.",
        "notes": "Tastiella comparando a imaterialidade energética de Mir com seu próprio avatar."
    },
    17961: {
        "text": "De todo modo, aquele Vírus-Mãe primordial, 'Mir',\nestá em processo de reativação.",
        "notes": "O alarme grave do despertar iminente do Vírus-Mãe (母なるウイルス体「ミュール」)."
    },
    17962: {
        "text": "E não é para menos. Afinal, a canção que lhe serve de vacina,\na [Chave da Crônica], deixou de ser entoada.",
        "notes": "Tastiella apontando a cessação do canto sagrado da Chave da Crônica (クロニクルキー)."
    },
    17963: {
        "text": "...",
        "notes": "Misha silenciosa, carregando o peso da culpa e o pavor de seu destino."
    },
    17964: {
        "text": "Se continuarmos assim, a própria Crônica Crescente\nnão resistirá por mais de um ano.",
        "notes": "O prazo fatal de colapso estrutural do altar de contenção sem o canto de vacina."
    },
    17965: {
        "text": "Por isso, preciso que recuperem a [Chave da Crônica]\no mais depressa possível.",
        "notes": "Tastiella comissionando o grupo a recuperar o Cristal Hymmnos indispensável."
    },
    17966: {
        "text": "Escuta aqui... Se a Crônica Crescente for destruída,\no que acontece com a Tastiella...?",
        "notes": "Jack perspicaz antevendo o desenlace trágico caso o altar seja danificado."
    },
    17967: {
        "text": "Ela vai desaparecer para sempre, é claro.",
        "notes": "Tastiella confirmando a aniquilação inevitável de sua existência com serenidade trágica."
    },
    17968: {
        "text": "...",
        "notes": "Jack assimilando o destino cruel da companheira Teru."
    },
    17969: {
        "text": "Diga, Tastiella...\nSe recuperarmos a Canção... o meu corpo vai voltar ao normal...?",
        "notes": "Misha interrogando com angústia e receio a restauração de seu corpo biológico adulto."
    },
    17970: {
        "text": "Pelo que você me contou,\ntenho certeza absoluta de que você voltará à forma anterior.",
        "notes": "Tastiella assegurando que a cura do canto reverterá a involução física."
    },
    17971: {
        "text": "Entendo...",
        "notes": "Misha desanimada com a perspectiva da maturidade forçada."
    },
    17972: {
        "text": "Não precisa ficar tão aflita.\nSem dúvida haverá um jeito de recuperar o seu corpo.",
        "notes": "Tastiella interpretando equivocadamente o temor da garota."
    },
    17973: {
        "text": "Não é isso!\nÉ exatamente o oposto!",
        "notes": "Misha gritando com desespero para corrigir o mal-entendido."
    },
    17974: {
        "text": "Eu... tenho pavor de voltar àquele corpo!\nTenho pavor de crescer...!",
        "notes": "A confissão dilacerante de Misha: o pavor de atingir a idade adulta e herdar o poço de selamento perpétuo."
    },
    17975: {
        "text": "Como...? Mas por quê?",
        "notes": "Tastiella atônita diante da recusa em voltar à maturidade."
    },
    17976: {
        "text": "...É que...",
        "notes": "Misha reprimindo as lágrimas e as dores da infância roubada."
    },
    17977: {
        "text": "Quem teria roubado a Chave da Crônica?!\nNão traz vantagem nenhuma para ninguém.",
        "notes": "Krusche indagando os motivos por trás do furto da vacina cósmica."
    },
    17978: {
        "text": "...O Bourd?",
        "notes": "Lyner desconfiando do comandante mercenário da Tenba."
    },
    17979: {
        "text": "...Hã?",
        "notes": "Krusche surpreendendo-se com a suspeita."
    },
    17980: {
        "text": "O Bourd não tinha falado alguma coisa sobre a Mir antes...?",
        "notes": "Lyner resgatando pistas verbais deixadas pelo vilão nos embates anteriores."
    },
    17981: {
        "text": "Droga... Nós baixamos a guarda demais na Placa Hexagonal...",
        "notes": "Radolf amargando a falha tática durante a batalha nos laboratórios da corporação."
    },
    17982: {
        "text": "...Essa tal de Tenba não passa de uma corja imunda até o tutano...",
        "notes": "Jack repudiando com asco as maquinações inescrupulosas do conglomerado."
    },
    17983: {
        "text": "Mas... contudo, porém!!\nIsso tudo não passa de futilidade insignificante para mim!",
        "notes": "Flashback da voz maníaca de Bourd ecoando na mente de Lyner."
    },
    17984: {
        "text": "Assim que a Mir despertar, estorvos irritantes\ncomo a Tenba e a Igreja vão ser varridos do mapa!",
        "notes": "Bourd delirando em suas ambições niilistas de destruição institucional total."
    },
    17985: {
        "text": "...Mir?!",
        "notes": "Lyner conectando as palavras fanáticas de Bourd à identidade do Vírus-Mãe."
    },
    17986: {
        "text": "Pensando bem... Ele disse isso mesmo!",
        "notes": "Lyner comprovando a cumplicidade de Bourd na conspiração de libertação viral."
    },
    17987: {
        "text": "Mas o Bourd já está morto...",
        "notes": "Krusche lembrando o desfecho trágico do comandante corporativo."
    },
    17988: {
        "text": "Muita ingenuidade sua. É da Tenba que estamos falando.\nNão é só o Bourd. A Tenba inteira está tramando algo podre.",
        "notes": "Jack alertando que a ameaça institucional ultrapassa qualquer indivíduo isolado."
    },
    17989: {
        "text": "Seja como for, o melhor a fazer é irmos\nao Beco Vagalume o mais rápido possível.",
        "notes": "Lyner traçando a rota estratégica rumo a Firefly Alley (ほたる横丁)."
    },
    17990: {
        "text": "Misha!",
        "notes": "Lyner avistando Misha que retorna de sua conversa confidencial com Tastiella."
    },
    17991: {
        "text": "Desculpem... Fiz vocês esperarem um tempão, né?",
        "notes": "Misha desculpando-se com doçura e disfarçando o peso do sacrifício anunciado."
    },
    17992: {
        "text": "Sobre o que você e a Tastiella estavam conversando?",
        "notes": "Lyner curioso e protetor querendo saber o conteúdo da conferência secreta."
    },
    17993: {
        "text": "Hihihi...\nIsto é segredo de estado!\nVamos, temos que nos apressar!",
        "notes": "Misha desconversando com um riso tsundere e afetuoso para poupar o amigo da dor."
    },

    # ==================== Event/116.evd (IDs 17994 - 18019) ====================
    17994: {
        "text": "Então este é o Cais Flutuante...",
        "notes": "Lyner chegando às instalações portuárias do Cais Flutuante (滞空岸壁)."
    },
    17995: {
        "text": "É o Cais Flutuante mesmo...\nEu nem imaginava que conseguiríamos chegar aqui tão rápido.",
        "notes": "Krusche admirada com a rapidez da travessia até a doca aérea."
    },
    17996: {
        "text": "E tudo graças a nós duas, claro!",
        "notes": "Misha gabando-se alegremente da contribuição feminina para a viagem."
    },
    17997: {
        "text": "Ei, acho bom lembrar que eu trabalhei pesado também, tá bom?!",
        "notes": "Krusche exigindo seus créditos mecânicos legítimos em tom cômico."
    },
    17998: {
        "text": "...!",
        "notes": "Misha captando um sinal de perturbação no ar."
    },
    17999: {
        "text": "Lyner!",
        "notes": "Misha alertando o protagonista em alerta de perigo."
    },
    18000: {
        "text": "O que foi...?",
        "notes": "Lyner virando-se para conferir a ameaça."
    },
    18001: {
        "text": "Uma aeronave...?!",
        "notes": "Krusche identificando a silhueta da nau voadora sob ataque."
    },
    18002: {
        "text": "Hum? Tem algo de muito errado ali.",
        "notes": "Lyner observando manobras irregulares e fumaça na embarcação."
    },
    18003: {
        "text": "M-mas o que é aquilo?! O que está acontecendo?!",
        "notes": "Lyner alarmado com o combate aéreo em pleno cais."
    },
    18004: {
        "text": "Evacuem em direção à Torre!\nMovam-se depressa!",
        "notes": "Radolf coordenando a evacuação militar dos civis sob saraivada inimiga."
    },
    18005: {
        "text": "Radolf!",
        "notes": "Lyner reconhecendo o capitão dos Cavaleiros de Elemia em ação."
    },
    18006: {
        "text": "Lyner!\nÉ você, Lyner?! O que está fazendo num lugar desses?!",
        "notes": "Radolf atônito ao ver o jovem escudeiro na linha de fogo."
    },
    18007: {
        "text": "Eu é que pergunto isso a você!\nO que houve aqui?!",
        "notes": "Lyner demandando explicações diante do caos súbito."
    },
    18008: {
        "text": "Fomos atacados pelos Guardiões da Torre\nenquanto cumpríamos nossa missão!",
        "notes": "Radolf relatando a emboscada aérea dos autômatos corrompidos da Torre sem eco sonoro."
    },
    18009: {
        "text": "Droga!",
        "notes": "Lyner praguejando perante a ferocidade do assalto inimigo."
    },
    18010: {
        "text": "Rápido, Lyner, você também precisa fugir!",
        "notes": "Radolf priorizando a segurança de Lyner e do grupo."
    },
    18011: {
        "text": "De jeito nenhum, eu vou lutar!",
        "notes": "Lyner sacando a espada e recusando-se a abandonar o aliado."
    },
    18012: {
        "text": "Ficou louco?!\nOs inimigos estão no ar!",
        "notes": "Radolf alertando para a desvantagem tática contra alvos voadores."
    },
    18013: {
        "text": "Não se preocupe!\nCom a minha Magia da Canção, é só um golpe e chão!",
        "notes": "Misha garantindo suporte balístico com sua Magia da Canção."
    },
    18014: {
        "text": "Você... é uma Reyvateil?!",
        "notes": "Radolf assombrado ao constatar a presença de uma cantora de suporte."
    },
    18015: {
        "text": "Eu também dou uma força!",
        "notes": "Krusche empunhando suas ferramentas de combate para a refrega."
    },
    18016: {
        "text": "Sou-lhes profundamente grato.\nUnirei minhas forças às suas na batalha!",
        "notes": "Radolf comovido com a lealdade dos camaradas, assumindo a liderança conjunta."
    },
    18017: {
        "text": "Radolf se juntou ao grupo!",
        "notes": "Notificação canônica de sistema da adesão oficial de Radolf Schnaider à equipe."
    },
    18018: {
        "text": "Os Guardiões estão atacando pelo flanco oposto da aeronave.",
        "notes": "Radolf orientando o posicionamento tático dos inimigos."
    },
    18019: {
        "text": "Vamos atravessar por dentro da nau para alcançá-los!",
        "notes": "Radolf ordenando a manobra de flanqueamento pelo interior da embarcação aérea."
    }
}

print(f"Total curated entries defined: {len(curated_dict)}")
assert len(curated_dict) == 185, f"Expected 185, got {len(curated_dict)}"

# Validação estrita linha por linha
hard_gate_errors = 0
lint_warnings = 0
syntactic_fracture_errors = 0
orphan_punct_errors = 0

for item in input_data["dialogues"]:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    curated_info = curated_dict[item_id]
    trad = curated_info["text"]

    # Hard gate
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

    # Lint
    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

    # Sem \r
    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    # Pontuação órfã após \n
    parts = trad.split("\n")
    for line_part in parts[1:]:
        line_strip = line_part.strip()
        if line_strip.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation: {line_part!r}")
            orphan_punct_errors += 1
        if line_part.startswith("..."):
            print(f"[ERROR] ID {item_id}: Line starts with reticências: {line_part!r}")
            orphan_punct_errors += 1

    # Fratura sintática antes de \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r} in {trad!r}")
        syntactic_fracture_errors += 1

print("\n--- Diagnostic Check ---")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")
print(f"Orphan Punctuation Errors: {orphan_punct_errors}")
print(f"Syntactic Fracture Errors: {syntactic_fracture_errors}")

if hard_gate_errors == 0 and lint_warnings == 0 and orphan_punct_errors == 0 and syntactic_fracture_errors == 0:
    print("[SUCCESS] All 185 lines are perfectly compliant!")
else:
    print("[FAIL] Fix issues before building output JSON.")
    sys.exit(1)

# Constrói o arquivo de saída
output_dialogues = []
output_curated_lines = []

for item in input_data["dialogues"]:
    item_id = item["id"]
    curated_info = curated_dict[item_id]
    trad_text = curated_info["text"]
    notes_text = curated_info["notes"]

    curated_line = {
        "id": item_id,
        "text": trad_text,
        "ptbr_curated": trad_text,
        "status": "approved",
        "origin": "curadoria_editorial",
        "notes": notes_text,
        "rationale": notes_text
    }
    output_curated_lines.append(curated_line)

    d_out = dict(item)
    d_out["review_status"] = "approved"
    d_out["text_ptbr"] = trad_text
    d_out["curated_ptbr"] = trad_text
    d_out["final_ptbr"] = trad_text
    d_out["texto_ptbr_curado"] = trad_text
    d_out["custom_text"] = trad_text
    d_out["ptbr_curated"] = trad_text
    d_out["reviewed"] = True
    d_out["notes"] = notes_text
    d_out["curation_notes"] = notes_text
    d_out["curadoria_notes"] = notes_text
    output_dialogues.append(d_out)

scene_handoff = {
    "last_scene_id": "Event/116.evd",
    "last_line_id": 18019,
    "resumo_dramatico": "O bloco BLK_EVD_079 abrange quatro momentos capitais da trama de Ar tonelico: (1) Em Event/147.evd, nas instalações secretas de experimentos em Reyvateils da Tenba na Placa Hexagonal, Radolf e Bourd quase duelam até a morte antes da intervenção solene da Presidente Ayano Raizer Elduke, que decreta trégua mútua diante da tragédia comum da queda. Jack Hamilton reencontra sua antiga protegida Misha e revela a verdade estarrecedora: Misha tem 18 anos, mas seu corpo não envelheceu um único dia nos últimos seis anos. Diante da ameaça crescente dos vírus e do descontrole da Torre, Lyner decide subir imediatamente com o cristal Purger para Platina, despedindo-se da Igreja de Elemia. (2) Em Event/603.evd, no Nível 3 da Cosmosfera de Misha, Lyner explora uma cidade onírica sob a neve onde Misha encarna a 'Fada da Canção', tecendo a Magia Azul [Guarda Gelo] para aquecer Aurica. Misha expressa sua dor e trauma por ser tratada como mera máquina utilitária para servir humanos e suplica a ajuda de Lyner para tornar-se humana através do remédio do eremita Yakuan das montanhas. (3) Em Event/228.evd, no altar da Crônica Crescente, Tastiella revela sua verdadeira natureza como a alma fundida ao colossal mecanismo de contenção e narra a Grande Guerra onde Mir derrubou metade do Continente Flutuante. Misha revela ser a 31ª da Linhagem Lünn (Misha Arsellec Lünn) encarregada de cantar perpetuamente o Chronicle Key como vacina. Misha confessa seu pavor de crescer e voltar ao corpo adulto para não herdar o fardo eterno de confinamento. O grupo conecta os delírios de Bourd à reativação de Mir pela Tenba e parte rumo ao Beco Vagalume. (4) Em Event/116.evd, o grupo chega ao Cais Flutuante, onde uma aeronave dos Cavaleiros de Elemia é emboscada por Guardiões voadores da Torre. Radolf reencontra Lyner, Misha oferece suporte com sua Magia da Canção e Radolf junta-se oficialmente ao grupo em combate.",
    "decisoes_terminologicas": {
        "Crônica Crescente": "クレセントクロニクル / Crescent Chronicle (altar sagrado e relíquia ancestral de selamento de Mir)",
        "Chave da Crônica": "クロニクルキー / Chronicle Key (Cristal Hymmnos que serve de canção-vacina para o selamento)",
        "Guarda Gelo": "青魔法【氷護】 / Magia Azul Guarda Gelo (Magia Azul tecida no Nível 3 da Cosmosfera de Misha)",
        "Yakuan": "薬庵 / Yakuan (eremita lendário das montanhas possuidor do elixir supremo)",
        "Presidente Ayano": "亜耶乃・ライザー・エルデューク / Presidente Ayano Raizer Elduke (líder máxima do Conglomerado Tenba)",
        "Maninho Harm": "アル兄ぃ / Maninho Harm (tratamento carinhoso de Misha para Jack Hamilton)",
        "Linhagem Lünn": "リューンの系譜 / Linhagem Lünn (linhagem sagrada das 31 sacerdotisas do selamento)",
        "Misha Arsellec Lünn": "彌紗・アルトセルク・リューン / Misha Arsellec Lünn (verdadeiro nome canônico de Misha)",
        "Cais Flutuante": "滞空岸壁 / Floating Wharf (doca e porto de aeronaves em Sol Ciel)",
        "Vírus-Mãe": "母なるウイルス体「ミュール」 / Mother Virus Mir (forma primordial e desincorporada de Mir)"
    },
    "alertas_para_proximo_bloco": "Para os blocos seguintes (BLK_EVD_080 em diante), atentar para as investigações e confrontos no Beco Vagalume (Firefly Alley), a busca pelo Cristal Hymmnos Chronicle Key e o desenvolvimento das tensões entre Tenba, Igreja e a libertação de Mir."
}

glossary_additions = {
    "Guarda Gelo": {
        "pt": "Guarda Gelo",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia da Canção / Azul",
        "note": "青魔法【氷護】 (Aomahō Hyōgo / Ice Guardian). Magia Azul tecida por Misha no Nível 3 de sua Cosmosfera para aquecer e proteger Aurica do frio intenso da nevasca onírica."
    },
    "Yakuan (Eremita)": {
        "pt": "Yakuan",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Personagem Lendário",
        "note": "薬庵 (Yakuan). Sábio eremita recluso nas montanhas da Cosmosfera de Misha, possuidor do elixir supremo capaz de curar qualquer mal e realizar o anseio de humanidade da Fada da Canção."
    },
    "Fada da Canção": {
        "pt": "Fada da Canção",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Conceito Psicológico",
        "note": "詩の精 (Uta no Sei / Song Fairy). Personificação onírica assumida por Misha no Nível 3, simbolizando sua alienação e o trauma de ser tratada como mera máquina utilitária destinada a se sacrificar pelas vontades humanas."
    }
}

output_payload = {
    "block_id": "BLK_EVD_079",
    "axis_id": input_data.get("axis_id", "3_HISTORIA_E_EVENTOS"),
    "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
    "category": input_data.get("category", "Event Dialogue"),
    "line_count": len(output_dialogues),
    "id_range": [output_dialogues[0]["id"], output_dialogues[-1]["id"]],
    "stats": {
        "total_lines": len(output_dialogues),
        "lines_rewritten": len(output_dialogues),
        "lines_approved_as_is": 0,
        "new_terms_added": len(glossary_additions)
    },
    "curated_lines": output_curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": output_dialogues,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_payload, f, indent=2, ensure_ascii=False)

print(f"\n[OUTPUT SAVED] Successfully written {output_path}")
print(f"Total lines in output: {len(output_dialogues)}")

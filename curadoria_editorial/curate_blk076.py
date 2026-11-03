# -*- coding: utf-8 -*-
"""
curate_blk076.py - Curadoria Editorial Canônica para BLK_EVD_076
"""
import sys
import json
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

INPUT_PATH = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_076_input.json"
OUTPUT_PATH = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_076_output.json"

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Dicionário de curadoria: ID -> (texto_curado, nota_editorial)
CURATED_MAP = {
    # -------------------------------------------------------------
    # Event/293.evd: IDs 17206..17244 (39 falas)
    # Retorno à Igreja de Elemia em Nemo, relato da salvação de Platina,
    # revelação do prolongador de vida e alerta de tornado no cais.
    # -------------------------------------------------------------
    17206: (
        "Certo! Antes de mais nada, vamos à igreja.\nPreciso me apresentar ao senhor Bispo.",
        "Radolf prioriza o dever clerical e militar de reportar o retorno a Nemo ao Bispo Falss."
    ),
    17207: (
        "Senhor Bispo.\nO Comandante-Geral Radolf e Aurica\nacabam de regressar.",
        "Relato formal e solene de Radolf, usando seu título canônico de Comandante-Geral (ラードルフ総司)."
    ),
    17208: (
        "Fico radiante ao ver que ambos regressaram em segurança.\nEsta foi a bênção sagrada do Trio de Elemia.",
        "Falss mantém a fachada pastoral benevolente, invocando o sagrado Trio de Elemia (エレミア三謳神)."
    ),
    17209: (
        "E quanto a vós, nobre Lyner...\nCheguei a cogitar, mas...\nveio mesmo cumprir a promessa daquela ocasião?",
        "Falss interpela Lyner formalmente (ライナー殿), lembrando a promessa de servir à Igreja."
    ),
    17210: (
        "Sim! Agora é o momento de retribuir a ajuda da Igreja.\nAfinal, só conseguimos cumprir a missão\ngraças ao apoio de vocês.",
        "Lyner reafirma sua lealdade e gratidão sincera pelo auxílio prestado pelos clérigos na crise de Platina."
    ),
    17211: (
        "Oh! Quer dizer então que a vossa missão...?",
        "Falss manifesta expectativa contida quanto ao desfecho do conflito em Platina."
    ),
    17212: (
        "Graças ao apoio de vocês, Platina foi salva!",
        "Lyner anuncia o triunfo de sua cruzada e a salvação de sua terra natal."
    ),
    17213: (
        "Compreendo! Que alívio imenso...\nFico verdadeiramente feliz.",
        "Falss encena emoção e regozijo piedoso pela vitória da expedição."
    ),
    17214: (
        "Por isso, gostaria de prestar serviços aqui na Igreja\nao lado da Aurica por algum tempo.",
        "Lyner formaliza seu voluntariado pastoral ao lado de sua parceira Reyvateil."
    ),
    17215: (
        "Ora, mas isso é esplêndido...\nNem sei como expressar tamanha gratidão.",
        "Falss acolhe a proposta com aparente humildade e louvor reverente."
    ),
    17216: (
        "Com isso, Aurica finalmente se torna\numa Reyvateil de pleno direito.\nDedique-se com fervor ao nobre Lyner.",
        "Falss outorga a Aurica o reconhecimento de Reyvateil emancipada (一人前), orientando-a a devotar-se a Lyner."
    ),
    17217: (
        "Sim!\nLyner...\nconto com você de agora em diante.",
        "Aurica aceita seu papel sagrado com candura e discreta timidez."
    ),
    17218: (
        "Bem, encerremos por aqui hoje. Descansem à vontade.\nJá deixei reservada a vossa hospedagem de costume.",
        "Falss dispensa a comitiva, providenciando o repouso na estalagem habitual."
    ),
    17219: (
        "Trataremos das próximas missões amanhã.",
        "Falss agenda a próxima conferência eclesiástica para o dia seguinte."
    ),
    17220: (
        "Muito obrigado.",
        "Lyner expressa gratidão polida pelo acolhimento pastoral."
    ),
    17221: (
        "Ah, antes que eu me esqueça, Aurica.\nNão está quase na hora de administrar\no seu agente prolongador de vida?",
        "Falss introduz a necessidade vital da injeção do agente prolongador de vida (延命剤)."
    ),
    17222: (
        "Ah...\nSim, o senhor tem razão...",
        "Aurica vacila e demonstra apreensão silenciosa perante o procedimento."
    ),
    17223: (
        "Vamos providenciar a aplicação ainda hoje.\nNos tempos atuais, nunca se sabe o que pode acontecer.",
        "Falss insiste na inoculação imediata sob o pretexto de instabilidade social."
    ),
    17224: (
        "Pois bem, venha aos aposentos internos.",
        "Falss convoca Aurica à sala reservada para a injeção do mantenedor vital."
    ),
    17225: (
        "Lyner, me desculpe.\nPode ir na frente...\neu vou direto para a pousada depois.",
        "Aurica oculta seu desconforto e pede para Lyner adiantar-se à estalagem."
    ),
    17226: (
        "A-ah, tá legal.",
        "Lyner consente, pressentindo algo estranho na reação da companheira."
    ),
    17227: (
        "Aurica deixou o grupo.",
        "Mensagem de sistema: Aurica ausenta-se do grupo para a aplicação médica."
    ),
    17228: (
        "Radolf.\nO que é esse tal agente prolongador de vida?",
        "Lyner indaga ao comandante sobre a natureza e função do composto farmacológico."
    ),
    17229: (
        "É um fardo doloroso e cruel que apenas\nas Reyvateils de Terceira Geração carregam.",
        "Radolf elucida a dolorosa dependência biológica que aflige as Terceiras Gerações."
    ),
    17230: (
        "Sem o prolongador de vida, uma Terceira Geração\nsó sobrevive por cerca de três meses.\nPor isso é preciso administrá-lo com regularidade.",
        "Explicação clínica sobre o curto ciclo biológico e a ameaça de colapso sem o remédio."
    ),
    17231: (
        "...Era isso, então?\nEu não fazia a menor ideia...",
        "Lyner cai em si, consternado com a fragilidade física e o drama das donzelas cantoras."
    ),
    17232: (
        "A aplicação causa um sofrimento tremendo.\nSempre penso se não haveria uma alternativa menos dolorosa, mas...",
        "Radolf lamenta a crueldade do método de dosagem e a ausência de tratamentos amenos."
    ),
    17233: (
        "Por isso a Aurica fez aquela cara tão abatida...",
        "Lyner compreende a relutância e a melancolia estampadas no rosto de Aurica."
    ),
    17234: (
        "...Hm? O que foi?",
        "Radolf percebe um murmúrio incomum vindo do exterior do templo."
    ),
    17235: (
        "...Parece haver algo estranho no ar.",
        "Radolf fareja a inquietação e o tumulto que se espalham pela cidade."
    ),
    17236: (
        "É verdade. As ruas estão agitadas demais.\nSerá que aconteceu alguma coisa...?",
        "Lyner nota a balbúrdia repentina entre os cidadãos nas vias de Nemo."
    ),
    17237: (
        "Com licença!\nAconteceu alguma coisa?",
        "Lyner interpela os transeuntes para averiguar a origem do alvoroço."
    ),
    17238: (
        "Se aconteceu?! É uma tempestade!\nUma baita tempestade!",
        "Transeunte em pânico relata a violência inaudita da tormenta atmosférica."
    ),
    17239: (
        "Bem abaixo do continente,\nsurgiu uma espécie de tornado gigantesco!",
        "Moradora descreve a formação de um vórtice colossal nos estratos inferiores da Torre."
    ),
    17240: (
        "Um tornado?!",
        "Lyner reage estupefato diante do fenômeno climático anômalo."
    ),
    17241: (
        "O vento já vinha soprando com força nos últimos dias...\ne agora olhem só no que deu!",
        "Cidadão comenta o agravamento progressivo dos vendavais até o ponto crítico."
    ),
    17242: (
        "Por causa disso, todos os barcos para o Beco Vagalume\nforam cancelados! Não temos como voltar para casa!",
        "Moradora lamenta o cancelamento de todas as naus aéreas rumo ao Beco Vagalume."
    ),
    17243: (
        "Que situação terrível...\nUm tornado de tamanha magnitude é algo sem precedentes.",
        "Radolf analisa a gravidade ímpar da tempestade que bloqueia as rotas de navegação."
    ),
    17244: (
        "É melhor conversarmos com outras pessoas\npara reunir mais detalhes.",
        "Lyner sugere interrogar os demais transeuntes em busca de rotas alternativas."
    ),

    # -------------------------------------------------------------
    # Event/605.evd: IDs 17245..17296 (52 falas)
    # Cosmosfera de Misha: a tentação de abandonar o papel de Fada da Canção,
    # Krusche em estado terminal, o conflito do remédio de Yakuan e o fardo de cantar.
    # -------------------------------------------------------------
    17245: (
        "Oba, finalmente vou poder virar humana!",
        "Misha comemora com entusiasmo a perspectiva de deixar a condição de Fada da Canção."
    ),
    17246: (
        "Pois é...\nMas você não vai sentir falta de ser a Fada da Canção?",
        "Lyner sonda se Misha não guardará arrependimentos ao renegar sua identidade mística."
    ),
    17247: (
        "Nem pensar!\nNão vou mais precisar ficar cuidando de humanos.\nNão existe nada mais maravilhoso que isso!",
        "Misha desabafa com bom humor sobre o cansaço de ser a protetora altruísta da humanidade."
    ),
    17248: (
        "Sendo assim...",
        "Misha prepara-se para o rito de transformação existencial."
    ),
    17249: (
        "Ué? Quem será que vem aí...?",
        "Lyner escuta passos apressados interrompendo a conversa."
    ),
    17250: (
        "Socorro! Tem alguém desmaiada lá fora!\nEu tentei curá-la de várias formas,\nmas com o meu poder não consigo fazer mais nada!",
        "Habitante do vilarejo onírico clama por socorro diante de uma vítima moribunda."
    ),
    17251: (
        "Eu vi a Fada da Canção entrando aqui há pouco...\ne vim correndo na esperança de conseguir socorro!",
        "A moradora relata ter avistado a fada protetora e roga por sua intercessão mágica."
    ),
    17252: (
        "Desmaiada lá fora?!\nMisha, vamos depressa!",
        "O instinto protetor de Lyner é acionado de imediato para resgatar a vítima."
    ),
    17253: (
        "...Tá...",
        "Misha hesita e aquiesce a contragosto diante do chamado urgente de Lyner."
    ),
    17254: (
        "Por aqui!",
        "A habitante guia a dupla até o local onde jaz a enferma."
    ),
    17255: (
        "Não aguento mais...\nEu... já não tenho salvação, não é...?",
        "Krusche (em projeção mental onírica) sussurra em agonia, à beira da morte."
    ),
    17256: (
        "Vai ficar tudo bem!\nA Fada da Canção veio nos acudir!",
        "A aldeã tenta infundir esperança à enferma ao apresentar Misha."
    ),
    17257: (
        "A Fada da Canção?! É sério mesmo?!\nQuer dizer então que eu...\nvou conseguir escapar...?",
        "Krusche recupera um tênue vislumbre de alívio e esperança diante da fada mística."
    ),
    17258: (
        "E-espera aí um instante!\nEu ainda não disse nem meia palavra sobre te salvar!",
        "Misha recua arisca, relutante em reassumir os votos sacrificiais de salvadora."
    ),
    17259: (
        "...Hã?",
        "Krusche fica atônita com a recusa gélida da lendária entidade benevolente."
    ),
    17260: (
        "Eu já resolvi largar o posto de Fada da Canção!\nPor isso, não vou mais ficar salvando humanos!",
        "Misha bate o pé, rebelando-se contra a sina de servir eternamente aos desejos alheios."
    ),
    17261: (
        "Misha! Como você tem coragem de falar isso?!\nDiante de alguém nesse estado, fada ou humana,\nqualquer pessoa tentaria ajudar!",
        "Lyner reprova com severidade o egoísmo da amiga perante a agonia alheia."
    ),
    17262: (
        "...Tá, já entendi!\nÉ só curar essa chata, não é?!\nMas fique sabendo que é a última vez!",
        "Misha cede sob a repreensão moral de Lyner, invocando seu poder sob protesto."
    ),
    17263: (
        "Toma!!",
        "Misha conjura seu feitiço de cura na tentativa de estancar a deterioração de Krusche."
    ),
    17264: (
        "...Será que... surtiu efeito...?",
        "Krusche busca sentir alguma melhora vital em seu organismo."
    ),
    17265: (
        "...Ela não melhorou nadinha, sabe?",
        "A habitante constata com desânimo a ineficácia total do encanto da fada."
    ),
    17266: (
        "...U-ué?\nNão faz sentido, devia ter funcionado...\nToma de novo!!",
        "Misha entra em pânico técnico e redobra a potência mágica, sem resultados."
    ),
    17267: (
        "Não adiantou...",
        "Krusche atesta o fracasso do feitiço e a persistência de suas dores fatais."
    ),
    17268: (
        "Deixa pra lá... obrigada mesmo assim.\nO médico já me disse que eu não tenho cura.\nProvavelmente nem mesmo a Fada da Canção consegue dar jeito.",
        "Krusche aceita com estoicismo e desilusão o veredito irreversível da medicina."
    ),
    17269: (
        "Ei, e aquele remédio que recebemos do Mestre Yakuan...?",
        "Lyner recorda o elixir milagroso concedido pelo eremita Yakuan (薬庵先生)."
    ),
    17270: (
        "Aquele não!\nDe jeito nenhum!!",
        "Misha entra em desespero: aquele frasco é o seu passaporte para a humanidade."
    ),
    17271: (
        "Tem alguém entre a vida e a morte bem aqui!",
        "Lyner insiste na primazia absoluta da preservação da vida humana imediata."
    ),
    17272: (
        "Mas e se usarmos e mesmo assim não adiantar nada?!\nEu vou me arrepender pelo resto da vida!",
        "Misha externa seu pavor de desperdiçar sua única chance de emancipação existencial."
    ),
    17273: (
        "...Mesmo assim, se houver uma chance de salvar uma vida...",
        "Lyner apela à compaixão altruísta, ainda que sob risco de fracasso."
    ),
    17274: (
        "Chega!\nVocê não entende nada do que sinto!",
        "Misha explode de mágoa pela incompreensão de Lyner perante seus sacrifícios e foge."
    ),
    17275: (
        "Misha!!",
        "Lyner grita pela amiga em fuga, dividido entre o resgate e o vínculo afetivo."
    ),
    17276: (
        "De qualquer forma, vamos levar a Krusche até a pousada!",
        "Lyner prioriza a remoção emergencial da paciente debilitada até um leito protegido."
    ),
    17277: (
        "S-sim!",
        "A habitante onírica acata a ordem com solicitude."
    ),
    17278: (
        "Pronto, por enquanto ela vai ficar segura.\nEmbora a vida dela continue em perigo...",
        "Lyner acomoda a enferma na estalagem, ciente da precariedade do quadro clínico."
    ),
    17279: (
        "Essa jovem me preocupa, mas...\nserá que a Misha vai ficar bem...?",
        "A habitante expressa apreensão com o abalo emocional e o sumiço de Misha."
    ),
    17280: (
        "A Misha já não suporta mais a ideia de continuar cantando pelos outros.\nPor enquanto, essa aversão ainda é contida, mas...",
        "A aldeã analisa a rejeição inconsciente de Misha à sua sina de sacrifício contínuo."
    ),
    17281: (
        "Então ela realmente odeia isso...\nClaro, ser forçada a cantar sem parar\ndeve ser um tormento terrível...",
        "Lyner compreende com compaixão a dor visceral da reclusão e do cântico imposto."
    ),
    17282: (
        "De qualquer modo, preciso encontrar a Misha.",
        "Lyner reafirma sua determinação de dialogar e amparar o coração fragilizado de Misha."
    ),
    17283: (
        "Espera um pouco.\nO que você quis dizer com a Misha continuar cantando?",
        "Lyner atenta para a amplitude cósmica da revelação e pede esclarecimentos adicionais."
    ),
    17284: (
        "Será que ela no fundo detesta entoar canções em combate,\nderrotar inimigos e nos curar durante as lutas...?",
        "Lyner questiona se até os combates táticos ao seu lado eram motivo de repulsa íntima."
    ),
    17285: (
        "Não é nada disso.\nA Misha carrega um destino muito mais grandioso e pesado sobre os ombros.",
        "A habitante pontua a gravidade do selo místico ancestral que Misha sustenta no mundo real."
    ),
    17286: (
        "Quer dizer então que ela ainda não te revelou a verdade, Lyner...?",
        "A projeção mental surpreende-se com a ignorância de Lyner quanto ao sacerdócio de Misha."
    ),
    17287: (
        "...",
        "Lyner silencia, tomado pelo peso do segredo guardado por sua parceira de infância."
    ),
    17288: (
        "Não posso pronunciar mais nenhuma palavra sobre isso.\nSe eu falar, poderei ser apagada deste mundo para sempre.",
        "A habitante alerta sobre as defesas psíquicas inconscientes da Cosmosfera."
    ),
    17289: (
        "Apagada?!",
        "Lyner reage chocado com a severidade da censura psíquica da mente de Misha."
    ),
    17290: (
        "Sim. Nós, que habitamos o interior do coração da Misha,\nse expressarmos algo que ela rejeita no inconsciente,\ncorremos o risco de ter a própria existência apagada.",
        "Conceito canônico do mundo mental: personas censuradas pelo ego são aniquiladas."
    ),
    17291: (
        "É-é mesmo...?\nEntão não se pode dar nenhum passo em falso.",
        "Lyner percebe o perigo iminente de pisar em traumas não resolvidos no mergulho."
    ),
    17292: (
        "Por essa razão, peço que ouça essa história\ndos próprios lábios da Misha...",
        "A entidade adverte que somente a própria donzela pode romper o véu do segredo."
    ),
    17293: (
        "Entendido.\nDe qualquer forma, preciso encontrar a Misha agora mesmo.",
        "Lyner decide procurá-la com respeito e delicadeza para acalmar seu espírito."
    ),
    17294: (
        "Ei, você sabe para onde a Misha foi?",
        "Lyner interroga outra residente sobre o paradeiro da fada em fuga."
    ),
    17295: (
        "E eu lá vou saber?\nNão pense que eu sei de tudo nesta vida.",
        "A moradora responde com sarcasmo e indiferença típica das personas mundanas da Cosmosfera."
    ),
    17296: (
        "...Compreendo.",
        "Lyner aceita a negativa lacônica e prossegue na busca pela amiga."
    ),

    # -------------------------------------------------------------
    # Event/376.evd: IDs 17297..17327 (31 falas)
    # Mundo Real (Platina/Catedral): expulsão de Misha por Shurelia,
    # revelação da forma adulta de 18 anos e mistério da Crônica Crescente.
    # -------------------------------------------------------------
    17297: (
        "...Lyner...",
        "Misha surge frágil e desolada nos corredores da Catedral de Platina."
    ),
    17298: (
        "Misha?!",
        "Lyner sobressalta-se ao avistar a amiga em prantos e desorientada."
    ),
    17299: (
        "O que houve?! Você está bem?\nO que diabos aconteceu aqui?!",
        "Lyner acolhe a donzela e indaga com urgência o motivo de seu desalento."
    ),
    17300: (
        "É que... de repente a Senhora Shurelia apareceu...\ne me expulsou de lá...",
        "Misha relata ter sido abruptamente destituída de seu posto na câmara de canto."
    ),
    17301: (
        "Ela disse que... eu não precisava mais cantar...",
        "A ordem de Shurelia quebra a razão de viver que sustentou Misha por anos a fio."
    ),
    17302: (
        "...O quê?",
        "Lyner fica boquiaberto diante da dispensa arbitrária da divindade da Torre."
    ),
    17303: (
        "O que significa eu não ter mais que cantar?!\nO que foi que aconteceu?!",
        "Misha externa seu desespero por não entender a súbita perda de sua sagrada missão."
    ),
    17304: (
        "Eu detesto até cogitar isso, mas...\na Senhora Shurelia pode ter sido dominada por Mir.",
        "Lyner levanta a temível hipótese de corrupção viral da Guardiã Ancestral da Torre."
    ),
    17305: (
        "Não pode ser... Por quê?!\nEu estava cantando com todas as minhas forças...",
        "Misha lamenta a inutilidade de sua vigília lírica ininterrupta contra as trevas."
    ),
    17306: (
        "Tenho certeza de que a culpa não foi sua, Misha.\nDeve haver algum outro motivo por trás disso...",
        "Lyner consola a amiga, desvencilhando-a de qualquer culpa pelo colapso do selo."
    ),
    17307: (
        "De qualquer forma, precisamos encontrar o meu pai\nou a Senhora Shurelia para descobrir a verdade...",
        "Lyner traça a linha de investigação com Leard e a Deusa para elucidar a crise."
    ),
    17308: (
        "Vamos voltar à Catedral primeiro\ne traçar o nosso plano...",
        "Lyner propõe recuar ao centro de operações antes de iniciar o rastreamento."
    ),
    17309: (
        "Eu também vou!\nNão adianta nada eu ficar aqui plantada.",
        "Misha recusa o papel passivo e exige acompanhar o destacamento de Lyner."
    ),
    17310: (
        "...Compreendo.\nSendo assim, vamos poder lutar juntos de novo.",
        "Lyner acolhe com carinho o reencontro operacional com sua leal companheira."
    ),
    17311: (
        "...Ai, ai. Depois de toda aquela despedida em lágrimas,\na gente até parece um bando de bobos.",
        "Misha quebra a solenidade com sua habitual autoironia travessa."
    ),
    17312: (
        "Bora, chega de conversa fiada e ladainha.\nHora de voltar pra Platina!",
        "Jack interrompe o sentimentalismo com seu pragmatismo cínico de mercenário."
    ),
    17313: (
        "Misha entrou para o grupo!",
        "Mensagem de sistema: Misha reintegra a equipe ativa do jogador."
    ),
    17314: (
        "...",
        "Pausa cênica com a metamorfose visual de Misha em sua plenitude corpórea."
    ),
    17315: (
        "Misha...\nE-essa aparência...\nO que diabos aconteceu com você?!",
        "Lyner embasbaca-se ao deparar com as formas adultas e exuberantes de Misha."
    ),
    17316: (
        "Como assim o que aconteceu...?\nEsta aqui... é a minha verdadeira aparência.",
        "Misha esclarece que o corpo desenvolvido sempre foi sua silhueta real e canônica."
    ),
    17317: (
        "Quer dizer então que...",
        "Lyner começa a conectar os fatos sobre o roubo do Cristal Hymmnos."
    ),
    17318: (
        "Sim. Quando o Bourd roubou a [Chronicle Key],\nparece que roubou o meu corpo junto.",
        "Misha revela o nexo místico entre a subtração do hino e sua regressão biológica."
    ),
    17319: (
        "Por isso eu acabei regredindo àquela forma infantil...",
        "Explicação definitiva para o confinamento em forma de criança no início da aventura."
    ),
    17320: (
        "...",
        "Lyner absorve a magnitude do trauma e a restauração anatômica da donzela."
    ),
    17321: (
        "...Afinal de contas, eu lembro perfeitamente\nde quando você era pequeno, não lembra?",
        "Misha aponta o absurdo temporal de parecer menor que seu companheiro contemporâneo."
    ),
    17322: (
        "A minha idade verdadeira é de 18 anos...\nNão tinha cabimento continuar parecendo uma menininha.",
        "Misha reivindica com orgulho sua maioridade e feminilidade de dezoito anos."
    ),
    17323: (
        "...",
        "Lyner fica ruborizado e sem palavras diante da presença feminina imponente de Misha."
    ),
    17324: (
        "...É-é verdade.\nSeja como for, fico feliz que tenha recuperado\no seu verdadeiro corpo.",
        "Lyner recompõe-se com delicadeza e congratula a amiga pela recuperação de sua forma."
    ),
    17325: (
        "......",
        "Misha acolhe as palavras de Lyner com uma doçura discreta e cúmplice."
    ),
    17326: (
        "Ei, tem coisas bem mais urgentes\nque vocês deveriam estar perguntando, não acham?",
        "Jack traz o foco da equipe de volta aos aspectos táticos da missão de segurança."
    ),
    17327: (
        "Misha...\nO que aconteceu com a Crônica Crescente?!",
        "Jack interroga Misha sobre a integridade e estabilidade do colossal órgão ritual."
    ),

    # -------------------------------------------------------------
    # Event/752.evd: IDs 17328..17371 (44 falas)
    # Cosmosfera de Aurica: destruição do Stonehenge pela Aurica Maligna,
    # rito de restauração, tecitura da Chuva Vital e desabafo sacrificial.
    # -------------------------------------------------------------
    17328: (
        "Que alívio...\nUma Mudança de Paradigma aconteceu neste mundo também.",
        "Aurica celebra o salto consciencial alcançado em seu mundo psicológico."
    ),
    17329: (
        "O próximo nível é o mundo da Aurica Maligna.\nNão sabemos o que pode acontecer,\nentão mantenha a guarda bem alta...",
        "Aurica adverte Lyner quanto à hostilidade e vileza de sua persona sombria (悪魔オリカ)."
    ),
    17330: (
        "Pode deixar...",
        "Lyner tranquiliza Aurica com firmeza e bravura cavalheiresca."
    ),
    17331: (
        "Uou!!",
        "O chão estremece com a eclosão violenta de uma fenda mágica destrutiva."
    ),
    17332: (
        "O-o que foi isso?!",
        "Aurica sobressalta-se com a interferência externa no Stonehenge."
    ),
    17333: (
        "...Não pode ser... É mentira?!",
        "Aurica contempla o desmoronamento dos monólitos sagrados de transição de nível."
    ),
    17334: (
        "Acha mesmo que vou deixar vocês virem\nao meu nível com tanta facilidade?",
        "Aurica Maligna manifesta-se através de sua projeção zombeteira e ameaçadora."
    ),
    17335: (
        "Você...?!",
        "Lyner reconhece a aura nefasta e provocadora da sombra psicológica."
    ),
    17336: (
        "...Nós duas somos a mesmíssima Aurica,\nmas pra mim você vem cheio de frieza me chamando de \"você\"?",
        "A sombra zomba da relutância de Lyner em tratá-la com intimidade carinhosa."
    ),
    17337: (
        "...!!",
        "Lyner é desarmado pela audácia lasciva e provocativa da persona oculta."
    ),
    17338: (
        "Ah, ou será que já estamos tão íntimos a ponto\nde nos tratarmos por \"benzinho\" e \"amor\"? Ahahaha!",
        "Provocação explícita com o tratamento íntimo conjugal japonês ('omae' e 'anata')."
    ),
    17339: (
        "Dá para parar com isso?!\nDestruir o altar da Mudança de Paradigma...\nÉ inacreditável...",
        "Aurica indigna-se com o vandalismo descarado contra a arquitetura mental do nível."
    ),
    17340: (
        "Ora, ora... Olha só quem fala!\nUma criaturinha que força a Mudança de Paradigma na marra\ntem moral para reclamar de quê?",
        "Aurica Maligna rebate com cinismo, denunciando a violência da Aurica consciente."
    ),
    17341: (
        "Aquilo... foi um mal necessário!",
        "Aurica tenta racionalizar a coação psicológica aplicada nos níveis precedentes."
    ),
    17342: (
        "Bem, que seja.\nDe qualquer forma, seria um aborrecimento\nse você chegasse lá com tanta facilidade.",
        "A sombra desdenha do debate ético e impõe sua condição de acesso ao seu domínio."
    ),
    17343: (
        "Se você conseguir consertar este Stonehenge\ne reativar a Mudança de Paradigma,\naí sim eu permito a sua entrada no meu nível.",
        "Desafio formal lançado a Lyner: reconstituir a integridade do santuário megalítico."
    ),
    17344: (
        "Ficarei te esperando, Lyner...\nFufufu...",
        "Aurica Maligna desvanece rindo, deixando uma névoa de sedução perigosa no ar."
    ),
    17345: (
        "...",
        "Silêncio tenso diante dos escombros do círculo de pedras sagradas."
    ),
    17346: (
        "Existe alguma forma de consertar isso?",
        "Lyner busca uma saída prática para reparar a mecânica do salto de paradigma."
    ),
    17347: (
        "Existe... Mas...\neu não sei se quero consertar...",
        "Aurica hesita em restaurar o portal por pavor de expor Lyner à maldade de seu outro eu."
    ),
    17348: (
        "P-por que não...?",
        "Lyner estranha a súbita relutância de sua parceira em avançar."
    ),
    17349: (
        "Lyner... Se você for além deste ponto,\nnão há garantia alguma de que voltará com vida!\nEla destruiu o Stonehenge com a maior facilidade...",
        "Aurica confessa seu pavor de perder Lyner para a selvageria de sua psique recalcada."
    ),
    17350: (
        "Eu tenho ciência disso.",
        "Lyner assume conscientemente o perigo com a dignidade estóica de guardião."
    ),
    17351: (
        "Mesmo que sobreviva,\ntenho certeza de que passará por provações terríveis...",
        "Aurica reforça o aviso sobre as torturas psicológicas inerentes ao mundo das trevas."
    ),
    17352: (
        "Já estou preparado para o que der e vier.",
        "Declaração solene e inabalável de devoção protetora de Lyner."
    ),
    17353: (
        "...Está bem.\nEntão vou tentar consertar de qualquer jeito...",
        "Sensibilizada pela coragem de Lyner, Aurica resolve canalizar suas energias de síntese."
    ),
    17354: (
        "Haaah!!",
        "Kiai concentrado de liberação mágica para transmutação do espaço onírico."
    ),
    17355: (
        "Por favor... restaure este Stonehenge...",
        "Invocação sacra aos espíritos artesãos da mente para erguer novamente os megálitos."
    ),
    17356: (
        "Compreendido... vou tentar...",
        "A fada arquiteta atende à prece e empenha sua energia na reconstrução."
    ),
    17357: (
        "Conseguimos! Funcionou!",
        "Lyner comemora a reativação gloriosa das energias do Stonehenge."
    ),
    17358: (
        "...Que alívio...",
        "Aurica suspira, confortada pelo sucesso do milagre arquitetônico interior."
    ),
    17359: (
        "Felizes para sempre... não é?\nBom, então me despeço por aqui.\nAté o dia em que nos reencontrarmos!",
        "A artífice despede-se com candura após cumprir sua nobre missão estrutural."
    ),
    17360: (
        "Muito bem, agora sim... vamos nessa?",
        "Lyner incentiva o avanço decisivo rumo ao portal desbloqueado."
    ),
    17361: (
        "Sim...\nLyner... a minha versão seguinte já se revelou uma demônia,\nmas... por favor, seja paciente comigo.",
        "Aurica pede complacência e compaixão diante de suas facetas mais sombrias."
    ),
    17362: (
        "...Pede para ela pegar leve comigo.",
        "Lyner responde com afeto bem-humorado, buscando aliviar a tensão da donzela."
    ),
    17363: (
        "Pensando bem... desde que te conheci,\nsinto que... amoleci um pouco o coração...",
        "Aurica admite com ternura comovente a influência pacificadora de Lyner em sua alma."
    ),
    17364: (
        "Então... vamos nessa...",
        "Aurica dá o passo final em direção à travessia de nível."
    ),
    17365: (
        "Você teceu a Magia Azul [Chuva Vital]!",
        "Mensagem de sistema: conquista canônica da Magia Azul Chuva Vital (青魔法【ライフシャワー】)."
    ),
    17366: (
        "Ora, puxa... parece que não teve jeito...\nO meu poder não foi suficiente para ajudar.\nSinto muito, de verdade...",
        "Linha de ramificação alternativa: falha no reparo do Stonehenge por insuficiência de poder."
    ),
    17367: (
        "Me perdoe, Lyner...\nAcho que... no fundo, eu ainda não confio\nplenamente em você...",
        "Aurica admite que o fracasso mágico decorre de suas próprias travas de desconfiança."
    ),
    17368: (
        "Não importa o que você diga...\nEu simplesmente não acredito que vá sair ileso\nse avançarmos para o mundo da Aurica Maligna...",
        "A donzela confessa sua incapacidade de arriscar a sanidade de quem tanto ama."
    ),
    17369: (
        "Eu jamais conseguiria te empurrar\npara uma missão suicida dessas...",
        "O instinto de preservação sacrificial supera a ambição de vencer o trauma."
    ),
    17370: (
        "Por isso não consigo restaurar o Stonehenge...\nMe perdoe...",
        "Aurica assume a responsabilidade pela paralisação do portal da Mudança de Paradigma."
    ),
    17371: (
        "...Compreendo...",
        "Lyner acolhe a dor e o medo de Aurica com respeito silencioso e paciência."
    ),

    # -------------------------------------------------------------
    # Event/727.evd: IDs 17372..17406 (35 falas)
    # Cosmosfera de Misha (Cais do Mundo Inferior): chegada da embarcação natal,
    # explicação sobre a separação da Chronicle Key pela Tenba e perdão de Ayano.
    # -------------------------------------------------------------
    17372: (
        "Ora, é você...\nFazia um bom tempo que não aparecia por aqui.",
        "Moradora do cais onírico cumprimenta Lyner com familiaridade mundana."
    ),
    17373: (
        "Haha, é verdade.\nPassei algum tempo longe da Misha recentemente.",
        "Lyner justifica sua ausência pelos compromissos militares e pelo afastamento temporário."
    ),
    17374: (
        "Hm, então era isso...\nBem que achei estranho a Misha andar tão cabisbaixa ultimamente...",
        "A residente conecta a melancolia de Misha à carência da presença de seu guardião."
    ),
    17375: (
        "Hã?",
        "Lyner surpreende-se com a revelação da tristeza que afligia sua amiga de infância."
    ),
    17376: (
        "Não é nada, esquece.",
        "A mulher disfarça com desdém para não alimentar a vaidade do rapaz."
    ),
    17377: (
        "Mais importante: enquanto você andava perambulando por aí,\num acontecimento grandioso se deu com a Misha.",
        "A moradora anuncia o grande marco ocorrido durante a separação da dupla."
    ),
    17378: (
        "Acontecimento grandioso...?\nVocê está falando do fato de ela ter crescido?",
        "Lyner associa a novidade à transformação corporal da jovem no mundo de vigília."
    ),
    17379: (
        "Exatamente.\nE como reflexo disso aqui na Cosmosfera,\numa embarcação acabou de atracar no cais.",
        "A moradora relata o impacto arquitetônico no mundo mental: o ancoramento da nau."
    ),
    17380: (
        "O quê? Um barco?!\nMas o que isso tem a ver com o fato de ela ter crescido?",
        "Lyner busca decifrar a metáfora onírica entre o navio no cais e o corpo adulto de Misha."
    ),
    17381: (
        "Não vou te contar.\nA culpa é sua por não estar ao lado dela no momento em que cresceu.",
        "A moradora repreende a negligência de Lyner ao não testemunhar a superação de Misha."
    ),
    17382: (
        "Droga...\nDe qualquer forma, gostaria de dar uma olhada no cais. Tudo bem?",
        "Lyner ignora a provocação e pede permissão para explorar a orla do porto."
    ),
    17383: (
        "Vá em frente, faça o que bem entender.",
        "A mulher dá de ombros, liberando a passagem para as docas da mente."
    ),
    17384: (
        "Lyner! Você veio me ver de novo!\nPuxa, você demorou tanto que cheguei a pensar\nque nunca mais colocaria os pés aqui!",
        "Misha recebe Lyner com euforia radiante e suas habituais queixas afetuosas."
    ),
    17385: (
        "Me perdoe, estivemos separados por algum tempo.\nA propósito, me disseram que uma embarcação atracou?",
        "Lyner desculpa-se com ternura e questiona sobre a nau ancorada ao largo."
    ),
    17386: (
        "Sim! Graças a você.\nAgora eu finalmente posso retornar à minha terra natal.",
        "Misha credita a Lyner o resgate simbólico de sua conexão com as próprias raízes."
    ),
    17387: (
        "Quer dizer então que... você vai partir daqui?",
        "Lyner teme uma despedida definitiva diante da menção ao retorno à pátria."
    ),
    17388: (
        "Não, bobinho! Vou ficar aqui para sempre.\nAfinal, a minha terra natal fica dentro da embarcação.",
        "Misha esclarece com fofura que seu lar ancestral viaja consigo no interior do navio."
    ),
    17389: (
        "Além disso, eu não estou mais acorrentada a este lugar.\nPor isso, agora posso emprestar todo o meu poder para você, Lyner!",
        "A superação dos grilhões psicológicos libera o fluxo total de poder da Reyvateil Origin."
    ),
    17390: (
        "Isso quer dizer que...",
        "Lyner intui o ganho substancial de suporte tático para os combates vindouros."
    ),
    17391: (
        "Quer contar com a minha ajuda em combate?\nTenho certeza de que serei muito útil!",
        "Misha oferece seus talentos mágicos com entusiasmo e espírito de parceria."
    ),
    17392: (
        "Pensando bem... quando foi que a Misha do mundo real\nvoltou a ter o corpo adulto?",
        "Lyner aproveita a intimidade para sanar a curiosidade sobre a cronologia da mudança."
    ),
    17393: (
        "No momento em que ela recuperou o Hino [Chronicle Key]!",
        "Misha fixa o nexo causal inequívoco entre o cântico ancestral e sua maturidade."
    ),
    17394: (
        "Aquele meu corpo de menininha era porque eu havia sido\nseparada à força do meu Hino em um laboratório da Tenba...",
        "Misha revela os experimentos desumanos de extração forçada conduzidos pela corporação."
    ),
    17395: (
        "Lembra que eu disse que estava procurando algo quando fugimos da Tenba?\nAquilo se referia à minha canção, mas também ao meu próprio corpo!",
        "Resgate narrativo da fuga do início do jogo, amarrando todas as pontas do enredo."
    ),
    17396: (
        "...Então era isso...\nMisha, me desculpe. Se eu pudesse,\nteria ido com você para resgatar a sua canção.",
        "Lyner manifesta pesar genuíno por não ter estado na vanguarda da recuperação do hino."
    ),
    17397: (
        "Não se preocupe!\nO que importa é que recuperei o meu verdadeiro corpo sã e salva.",
        "Misha conforta o amigo, celebrando a integridade física e espiritual reconquistada."
    ),
    17398: (
        "Não precisa esquentar a cabeça com essa história do meu corpo.\nSó de poder te ver são e salvo de novo,\neu já me sinto imensamente feliz!",
        "Declaração luminosa de afeto fraternal e devoção mútua de Misha por seu companheiro."
    ),
    17399: (
        "A Misha recuperou o próprio corpo junto com a canção.\nQue notícia maravilhosa!",
        "Lyner regozija-se com o encerramento do longo pesadelo de mutilação de Misha."
    ),
    17400: (
        "Pois é, né?",
        "A moradora encerra o assunto com sua usual concisão cética."
    ),
    17401: (
        "Por falar nisso, agora que a embarcação atracou,\nvocê pode explorar o interior dela.\nSeria uma boa você dar uma passada lá dentro.",
        "A residente informa sobre a liberação de acesso ao convés e camarotes da nau."
    ),
    17402: (
        "Novo destino liberado no mapa: [Interior da Embarcação]!",
        "Mensagem de sistema padronizada com BLK_EVD_026 para o novo ponto no mapa onírico."
    ),
    17403: (
        "A Presidente Ayano da Tenba pediu sinceras desculpas sobre o caso.\nEla disse que também quer se desculpar pessoalmente com você, Lyner.",
        "Misha relata a postura honrosa da Presidente Ayano ao tomar ciência dos abusos corporativos."
    ),
    17404: (
        "Como é que é...? Que reviravolta tão repentina é essa...?",
        "Lyner estranha o gesto ético vindo da liderança máxima do conglomerado rival."
    ),
    17405: (
        "Pelo visto, tudo o que fizeram comigo foi armação oculta do Bourd.\nNem a Presidente sabia de nada!",
        "Misha esclarece que os experimentos clandestinos foram conspiração isolada de Bourd."
    ),
    17406: (
        "Então foi isso...",
        "Lyner compreende os meandros da cisão e da traição interna que corroeu a Tenba."
    )
}

print(f"Total curated entries mapped: {len(CURATED_MAP)}")
assert len(CURATED_MAP) == 201, f"Expected 201 entries, got {len(CURATED_MAP)}"
# -*- coding: utf-8 -*-
# Continuação de curate_blk076.py

# Validação e montagem
dialogues = input_data["dialogues"]
curated_lines = []
output_dialogues = []

hard_gate_errors = 0
lint_warnings = 0

for d in dialogues:
    item_id = d["id"]
    orig_jp = d["original_jp"]
    orig_en = d["original_en"]
    cur_pt = d.get("current_ptbr", "")
    spk = d.get("speaker", "")
    ev = d.get("event_file", "")
    spk_id = d.get("speaker_id")

    if item_id not in CURATED_MAP:
        print(f"[MISSING ID] {item_id}")
        hard_gate_errors += 1
        continue

    trad, note = CURATED_MAP[item_id]

    # Validação Hard Gate
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

    # Linter editorial
    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

    # Checagem de \r
    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    # Checagem de pontuação órfã após \n
    parts = trad.split("\n")
    for line_part in parts[1:]:
        line_strip = line_part.strip()
        if line_strip.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1
        if line_part.startswith("..."):
            print(f"[ERROR] ID {item_id}: Line starts with reticências after newline: {line_part!r}")
            hard_gate_errors += 1

    # Checagem de fratura sintática antes de \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

    # Monta objetos para curated_lines e dialogues
    curated_lines.append({
        "id": item_id,
        "text": trad,
        "ptbr_curated": trad,
        "status": "approved",
        "origin": "curadoria_editorial",
        "notes": note,
        "rationale": note
    })

    output_dialogues.append({
        "id": item_id,
        "event_file": ev,
        "speaker_id": spk_id,
        "speaker": spk,
        "original_jp": orig_jp,
        "original_en": orig_en,
        "current_ptbr": cur_pt,
        "review_status": "approved",
        "text_ptbr": trad,
        "curated_ptbr": trad,
        "final_ptbr": trad,
        "texto_ptbr_curado": trad,
        "custom_text": trad,
        "ptbr_curated": trad,
        "reviewed": True,
        "notes": note,
        "curation_notes": note,
        "curadoria_notes": note
    })

print(f"\n--- Resultado da Validação Prévia ---")
print(f"Total avaliado: {len(dialogues)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors > 0 or lint_warnings > 0:
    print("\n[ERRO] Corrija os erros e avisos antes de gravar o arquivo de saída!")
    sys.exit(1)

# Se tudo perfeito, monta o JSON de saída final
scene_handoff = {
    "last_scene_id": "Event/727.evd",
    "last_line_id": 17406,
    "resumo_dramatico": (
        "O bloco BLK_EVD_076 reúne cinco arcos dramáticos capitais de revelação e desenvolvimento: "
        "(1) Em Event/293.evd, Radolf e Aurica retornam triunfantes com Lyner à Igreja de Elemia em Nemo após salvarem Platina. "
        "Falss, mantendo sua máscara de benevolência pastoral e invocando o Trio de Elemia, aceita o voluntariado de Lyner e outorga a Aurica "
        "o reconhecimento de Reyvateil de pleno direito, enviando-a em seguida para receber seu agente prolongador de vida (延命剤). "
        "Fora do templo, Radolf revela a Lyner a tragédia das Reyvateils de Terceira Geração, que sem o composto sobrevivem apenas cerca de "
        "três meses sob dolorosas injeções periódicas. Logo após, a cidade é tomada pelo pânico com a formação de um tornado colossal abaixo do "
        "continente, suspendendo todas as rotas de naus para o Beco Vagalume. "
        "(2) Em Event/605.evd, no mergulho da Cosmosfera de Misha, esta se ilude com a ideia de abandonar o sacerdócio da Fada da Canção para tornar-se humana. "
        "Quando Krusche surge moribunda na aldeia onírica e a magia curativa fracassa, Lyner insiste em usar o elixir concedido pelo Mestre Yakuan (薬庵先生), "
        "o que desencadeia a fúria em prantos de Misha, para quem aquele frasco representava seu único meio de virar humana. As personas oníricas "
        "revelam a Lyner que Misha carrega o fardo cósmico de um selo sagrado e que revelar o trauma acarreta a pena de apagamento imediato pelo inconsciente. "
        "(3) Em Event/376.evd, de volta a Platina, Lyner resgata Misha em lágrimas após ser sumariamente expulsa da câmara de canto por Shurelia "
        "sob a ordem de que não precisava mais cantar, temendo-se a corrupção viral da Guardiã por Mir. Ao reintegarem-se, revela-se a verdadeira "
        "aparência adulta de 18 anos de Misha, cujo corpo fora sequestrado e regredido à infância quando Bourd roubou o Hino [Chronicle Key] na Tenba. "
        "Jack interrompe a emoção do grupo cobrando respostas urgentes sobre a estabilidade do órgão ritual Crônica Crescente. "
        "(4) Em Event/752.evd, na Cosmosfera de Aurica, a Mudança de Paradigma é violentamente interrompida pelo surgimento da Aurica Maligna (悪魔オリカ), "
        "que destrói os megálitos de Stonehenge e desafia Lyner a reconstruí-los se quiser entrar em seu domínio tenebroso. Lyner aceita o perigo com "
        "bravura incondicional ('覚悟の上だ'), permitindo que Aurica convoque a reconstrução mística e teça a Magia Azul [Chuva Vital] (青魔法【ライフシャワー】), "
        "admitindo enternecida que o convívio com Lyner amoleceu seu coração outrora traumatizado. "
        "(5) Em Event/727.evd, nas docas oníricas da Cosmosfera de Misha, uma moradora relata que o amadurecimento corpóreo de Misha no mundo desperto "
        "fez atracar a embarcação de sua terra natal, abrindo o novo destino [Interior da Embarcação]. Misha celebra a libertação de seus grilhões e "
        "oferece seu poder integral de combate a Lyner, detalhando a separação cruel de seu hino nos laboratórios da Tenba e revelando que a Presidente "
        "Ayano pediu sinceras desculpas, pois todas as atrocidades haviam sido arquitetadas às escondidas pelo inescrupuloso Bourd."
    ),
    "decisoes_terminologicas": {
        "Supreme Commander Radolf": "ラードルフ総司 (Comandante-Geral Radolf; título formal de líder militar dos Cavaleiros)",
        "Life-Extending Agent": "延命剤 (agente prolongador de vida / prolongador de vida; mantenedor vital de Terceiras Gerações)",
        "Trio of Elemia": "エレミア三謳神 (Trio de Elemia; deusas ancestrais Eoria, Frelia e Tyria)",
        "Chronicle Key": "ヒュムノス『クロニクルキー』 / [Chronicle Key] (Hino/Cristal ancestral selador de Mir e restaurador do corpo de Misha)",
        "Crescent Chronicle": "クレセントクロニクル (Crônica Crescente; órgão monumental de amplificação acústica em Platina)",
        "Devilish Aurica": "悪魔オリカ (Aurica Maligna; persona sombria e desiludida da Cosmosfera de Aurica)",
        "Stonehenge": "ストーンヘンジ (Stonehenge; círculo megalítico sagrado do rito de Mudança de Paradigma)",
        "Life Shower": "青魔法【ライフシャワー】 / [Chuva Vital] (Magia Azul tecida por Aurica para cura vital)",
        "Master Yakuan": "薬庵先生 (Mestre Yakuan / eremita Yakuan; sábio das ervas e elixires da Cosmosfera de Misha)",
        "Inside the Ship": "船の中 / [Interior da Embarcação] (novo destino liberado no cais onírico de Misha)",
        "President Ayano": "天覇の亜耶乃社長 (Presidente Ayano da Tenba; líder executiva da corporação)"
    },
    "alertas_para_proximo_bloco": (
        "Nos blocos subsequentes (BLK_EVD_077 em diante), zelar pela preservação da voz adulta e curvilínea de Misha, "
        "o aprofundamento das intrigas políticas com a Presidente Ayano e a Tenba, a exploração do mundo sombrio da Aurica Maligna "
        "e a investigação da corrupção viral da Torre sob o domínio de Mir."
    )
}

glossary_additions = {
    "Life Shower": {
        "pt": "Chuva Vital",
        "gender": "feminino",
        "number": "singular",
        "category": "Combate / Magia Azul",
        "note": "青魔法【ライフシャワー】 (Aomahō Raifu Shawā). Magia Azul curativa de alta intensidade tecida por Aurica em sua Cosmosfera para restauração contínua de vitalidade (padronizado com BLK_SYS_001 e BLK_SYS_010)."
    },
    "Inside the Ship": {
        "pt": "Interior da Embarcação",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Destino do Mapa",
        "note": "船の中 (Fune no naka). Ponto navegável e destino interior do navio ancestral atracado no cais da Cosmosfera de Misha após ela recuperar a Chronicle Key (padronizado com BLK_EVD_026 ID 6608)."
    }
}

output_data = {
    "block_id": "BLK_EVD_076",
    "axis_id": input_data.get("axis_id", "AXIS_3"),
    "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
    "category": input_data.get("category", "Event Dialogue"),
    "line_count": len(curated_lines),
    "id_range": [curated_lines[0]["id"], curated_lines[-1]["id"]],
    "stats": {
        "total_lines": len(curated_lines),
        "lines_rewritten": len(curated_lines),
        "lines_approved_as_is": 0,
        "new_terms_added": len(glossary_additions)
    },
    "curated_lines": curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": output_dialogues,
    "scene_handoff": scene_handoff
}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"\n[SUCESSO] Arquivo de saída gerado com sucesso em: {OUTPUT_PATH}")
print(f"Total de falas gravadas: {len(output_dialogues)}")

# -*- coding: utf-8 -*-
"""Script gerador e validador da curadoria editorial do bloco BLK_EVD_029."""

import json
import sys
from pathlib import Path

# Adiciona o diretório de ferramentas ao sys.path para importar o validador oficial
sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\tools")
from curadoria_validate import validate_batch, validate_line

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_029_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_029_output.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

raw_dialogues = input_data["dialogues"]
assert len(raw_dialogues) == 223, f"Esperado 223 falas, obtido {len(raw_dialogues)}"

curations = {
    # =========================================================================
    # EVENT: Event/686.evd (IDs 7260 - 7360) [101 falas] - Nível 8 da Cosmosfera de Misha: Paródia de Atelier Elie
    # =========================================================================
    7260: (
        "Prontinho, chegamos!\nEsta é a cidade portuária de Castagne!",
        "rewritten",
        "Misha anunciando radiante a chegada a Castagne na paródia de Atelier Elie."
    ),
    7261: (
        "Uma cidade com peixes maravilhosos!\nTem arenque, peixe-agulha, carapau, olhete...\ne até tubarão!",
        "rewritten",
        "Misha listando as iguarias marítimas da cidade de forma cômica e entusiasmada."
    ),
    7262: (
        "Tubarão?!\nMas o que é isso?",
        "rewritten",
        "Lyner, nascido no topo da Torre de Sol Ciel, espantado por nunca ter ouvido falar de animais marinhos."
    ),
    7263: (
        "Ué? Lyner, você não sabe\no que é um tubarão?",
        "rewritten",
        "Misha zombando da inocência de Lyner sobre o mundo aquático."
    ),
    7264: (
        "Sei lá, nunca ouvi falar.\nMas então esse é o mar...\nÉ a primeira vez que vejo, mas parece uma grande inundação!",
        "rewritten",
        "Lyner boquiaberto diante da imensidão do oceano, confundindo o mar com um dilúvio."
    ),
    7265: (
        "Não é inundação, é o mar!\nE, se atravessarmos essas águas,\nfinalmente poderei rever a Marlone...",
        "rewritten",
        "Misha corrigindo Lyner e suspirando de saudade ao lembrar de Marlone (Marie)."
    ),
    7266: (
        "...Marlone...?",
        "rewritten",
        "Lyner indagando intrigado sobre o nome citado por Misha."
    ),
    7267: (
        "Você de novo por aqui?\nNão importa quantas vezes tente, não vai dar pé.",
        "rewritten",
        "Yurika (avatar de Aurica como pescadora) desdenhando das tentativas de Misha de cruzar o mar."
    ),
    7268: (
        "Yurika!\nRelaxa, desta vez vai ser diferente.\nEu até preparei uma bomba especial!",
        "rewritten",
        "Misha rebatendo com confiança de que criou um artefato alquímico definitivo."
    ),
    7269: (
        "...Uma bomba, é?",
        "rewritten",
        "Yurika desconfiada e curiosa sobre o trunfo de Misha."
    ),
    7270: (
        "Isso! Eu fiz com alquimia!\nÉ um item que faz chover meteoros.\nNão importa que seja um dragão: se cair um meteoro na cabeça dele...!",
        "rewritten",
        "Misha explicando a premissa de sua bomba Meteoro com empolgação juvenil."
    ),
    7271: (
        "Meteoro?!\nDá um certo arrepio, mas...\nparece que temos boas chances desta vez.",
        "rewritten",
        "Yurika ponderando o plano explosivo com otimismo cauteloso."
    ),
    7272: (
        "Gostei, tô dentro!\nVou colocar o barco no mar mais uma vez!",
        "rewritten",
        "Yurika topando a travessia de barco para enfrentar a criatura marinha."
    ),
    7273: (
        "Ebaaa!",
        "rewritten",
        "Misha comemorando alegremente a cooperação da pescadora."
    ),
    7274: (
        "...Er... quem é a senhorita,\nexatamente?",
        "rewritten",
        "Lyner educado e sem jeito diante da desconhecida que se parece com Aurica."
    ),
    7275: (
        "Hã? Quem é você pra começo de conversa?!",
        "rewritten",
        "Yurika cobrando que ele se apresente primeiro antes de fazer perguntas."
    ),
    7276: (
        "Ah, desculpa!\nEste é o meu parceiro desta vez: o Lyner!",
        "rewritten",
        "Misha apresentando seu escudeiro de jornada com orgulho."
    ),
    7277: (
        "E esta é a Yurika. Ela é pescadora em Castagne\ne a minha única esperança para navegar e derrotar o dragão!",
        "rewritten",
        "Misha esclarecendo o papel de Yurika na empreitada náutica."
    ),
    7278: (
        "Prazer, Lyner.\nMas você também não deu sorte na vida, hein?\nLogo cair na lábia dessa garota tão inconsequente...",
        "rewritten",
        "Yurika solidarizando-se sarcasticamente com a enrascada em que Lyner se meteu."
    ),
    7279: (
        "A-haha... pode ser...\nMas nisso estamos no mesmo barco, não acha?",
        "rewritten",
        "Lyner desconversando com bom humor sobre ambos estarem envolvidos na loucura."
    ),
    7280: (
        "Tem razão.\nBom, vou preparar o barco para zarpar.\nEsperem aqui um instante.",
        "rewritten",
        "Yurika saindo de cena para aprontar os preparativos da embarcação."
    ),
    7281: (
        "...É agora.\nAté me deu um frio na barriga...",
        "rewritten",
        "Misha confessando a ansiedade que antecede a partida para o reencontro sonhado."
    ),
    7282: (
        "Vem cá, Elie...\nPor que você quer tanto encontrar essa pessoa?\nEssa tal de Marlone?",
        "rewritten",
        "Lyner chamando Misha por seu codinome Elie e perguntando sobre a motivação da busca."
    ),
    7283: (
        "...A Marlone salvou a minha vida.\nQuando eu era pequena e estava à beira da morte com uma febre alta,\nela usou alquimia para me curar...",
        "rewritten",
        "Misha narrando a lenda de Elie e sua salvadora Marlone (Marie de Atelier Marie), corrigindo o gênero deturpado pelo inglês."
    ),
    7284: (
        "Como ela era uma viajante, foi embora da minha vila logo depois.\nEu nem sequer sabia quem ela era ou de onde vinha.",
        "rewritten",
        "Misha descrevendo a partida súbita da misteriosa alquimista itinerante."
    ),
    7285: (
        "Mais tarde, quando soube que a arte que me curou se chamava alquimia...\neu entrei para a Academia de Salburg.",
        "rewritten",
        "Misha relatando a vocação despertada pela lembrança do milagre da cura."
    ),
    7286: (
        "Eu também queria salvar pessoas com a alquimia.\nE me tornar alguém incrível, exatamente como a Marlone...",
        "rewritten",
        "Misha expressando o nobre ideal que herdou da lendária Marie."
    ),
    7287: (
        "Virei alquimista porque ela era minha grande inspiração.\nPor isso, reencontrar a Marlone é o meu maior sonho.",
        "rewritten",
        "Misha reafirmando que reencontrar sua mentora e ídolo é o objetivo de sua vida."
    ),
    7288: (
        "...Entendi. Foi por isso, então.",
        "rewritten",
        "Lyner compreendendo a beleza e o peso sentimental daquela jornada."
    ),
    7289: (
        "Tudo pronto por aqui...",
        "rewritten",
        "Yurika avisando que o barco está pronto para a travessia."
    ),
    7290: (
        "Maravilha! Já que tá tudo pronto...\nVamos nessa!",
        "rewritten",
        "Misha convocando o time para a partida com disposição máxima."
    ),
    7291: (
        "É isso aí!",
        "rewritten",
        "Lyner correspondendo com vigor cavalheiresco."
    ),
    7292: (
        "Humpf... Ora, se não é a pivete de novo!\nPode tentar quantas vezes quiser: o resultado será o mesmo!",
        "rewritten",
        "O Dragão Marinho rugindo soberbo ao avistar a pequena desafiante."
    ),
    7293: (
        "Achou errado!\nDesta vez não vai ser que nem antes!",
        "rewritten",
        "Misha confrontando o monstro marinho sem pestanejar."
    ),
    7294: (
        "Patético!\nVou calar essa sua boca atrevida agora mesmo!\nTome isto: Fúria das Marés!",
        "rewritten",
        "O Dragão invocando seu ataque náutico devastador contra os invasores."
    ),
    7295: (
        "Não vai, não!\nMeteoro!!",
        "rewritten",
        "Misha contra-atacando no ato com seu artefato de destruição em massa."
    ),
    7296: (
        "O-o quê?!",
        "rewritten",
        "O monstro em pânico ao ver o céu se abrir em chamas."
    ),
    7297: (
        "Caia na cabeça deleee!! Meteoooro!!",
        "rewritten",
        "Misha gritando o comando de queda com veemência cômica."
    ),
    7298: (
        "...Hã?",
        "rewritten",
        "Lyner atordoado ao ver o que de fato caiu do céu."
    ),
    7299: (
        "Guaaaarrrgh!!",
        "rewritten",
        "O Dragão sucumbindo ao impacto bizarro e avassalador."
    ),
    7300: (
        "Ué? E-e-ei?!\nEu venci o bicho?!",
        "rewritten",
        "Misha estupefata e surpresa com a vitória instantânea."
    ),
    7301: (
        "...Ela derrotou... um dragão... com uma bacia...",
        "rewritten",
        "Lyner chocado diante do clássico gag japonês da bacia de metal caindo na cabeça do dragão."
    ),
    7302: (
        "C-consegui! Eu consegui, Lyner!",
        "rewritten",
        "Misha vibrando pelo feito inacreditável nos braços de Lyner."
    ),
    7303: (
        "M-mas que loucura é essa, afinaaal?!",
        "rewritten",
        "Lyner berrando em choque com a falta de lógica da física da Cosmosfera."
    ),
    7304: (
        "Conseguimos!\nFinalmente chegamos... a Kentonis!!",
        "rewritten",
        "Misha anunciando a chegada triunfal ao destino almejado."
    ),
    7305: (
        "Então este é... Kentonis...\nÉ aqui que mora essa tal de Marlone?",
        "rewritten",
        "Lyner observando a cidade acadêmica e buscando a lendária aluna."
    ),
    7306: (
        "Sim, tenho quase certeza!\nDe qualquer forma, vamos até a Academia de Alquimia.",
        "rewritten",
        "Misha conduzindo Lyner diretamente aos portões da venerável instituição."
    ),
    7307: (
        "A Marlone está aqui...\nMeu coração começou a disparar de repente...\nComo será que ela é?",
        "rewritten",
        "Misha ansiosa e emocionada na soleira da academia dos seus sonhos."
    ),
    7308: (
        "Com certeza é uma mulher linda, sábia e refinada,\no modelo de perfeição que qualquer mulher sonha em ser!",
        "rewritten",
        "Misha idealizando Marlone com reverência sublime, corrigindo o erro grosseiro do inglês."
    ),
    7309: (
        "...Olha, acho melhor não romantizar tanto\nem cima das suas fantasias...",
        "rewritten",
        "Lyner aconselhando prudência antes do choque da realidade."
    ),
    7310: (
        "Ué? Você não é aquela...?",
        "rewritten",
        "Uma voz familiar se aproximando e reconhecendo Misha de relance."
    ),
    7311: (
        "Quanto tempo! Pelo visto,\nvocê se curou daquela doença direitinho, né?",
        "rewritten",
        "Aurica (encarnando Marie/Marlone) cumprimentando Misha com afeto caloroso."
    ),
    7312: (
        "...Hã? ...Você...?",
        "rewritten",
        "Misha paralisada ao reconhecer os traços inconfundíveis de sua rival."
    ),
    7313: (
        "Se você tá por aqui...\nentão conseguiu entrar para a Academia! Como tá a Professora Ingrid?",
        "rewritten",
        "Aurica entusiasmada com as lembranças nostálgicas da mestra Ingrid."
    ),
    7314: (
        "E-espera um pouco...",
        "rewritten",
        "Misha tentando processar o pesadelo cômico em que se meteu."
    ),
    7315: (
        "Hum? O que foi?",
        "rewritten",
        "Aurica fingindo inocência e candura diante da reação da amiga."
    ),
    7316: (
        "Aurica! O que você tá fazendo aqui?!\nLogo no clímax da minha cena emocionante de reencontro?!",
        "rewritten",
        "Misha explodindo de indignação por ver sua rival profanando seu grande momento."
    ),
    7317: (
        "Eu não sou a Aurica!\nEu sou a Marlone! Sou a Marie!!",
        "rewritten",
        "Aurica insistindo com vigor cômico em seu papel canônico de heroína de Salburg."
    ),
    7318: (
        "Não pode seeer! Que ódiooo!!\nPor que passei por todo esse perrengue\nsó pra dar de cara com a Aurica?!",
        "rewritten",
        "Misha em crise dramática ao descobrir que seu ídolo supremo é encarnado pela rival."
    ),
    7319: (
        "Nossa, precisava dessa grosseria toda...?",
        "rewritten",
        "Aurica ofendida com o desprezo teatral de Misha."
    ),
    7320: (
        "Mas é claro!\nPra começo de conversa, não fica se enfiando\nno mundo dos outros sem ser chamada!",
        "rewritten",
        "Misha expulsando Aurica de sua Cosmosfera particular."
    ),
    7321: (
        "Já não basta viver se fazendo de coitadinha\npra chamar a atenção do Lyner?!\nNão seja cara de pau de aparecer até aqui!",
        "rewritten",
        "Misha expondo sem filtro seu ciúme ardente da atenção que Aurica recebe de Lyner."
    ),
    7322: (
        "O-olha, gente...",
        "rewritten",
        "Lyner tentando em vão acalmar os ânimos bélicos das duas heroínas."
    ),
    7323: (
        "Olha quem fala! Você vive arrastando o Lyner\nna marra pra todo lado! Parece até uma megera controlando o marido!",
        "rewritten",
        "Aurica retrucando com veneno certeiro sobre o autoritarismo cômico de Misha com Lyner."
    ),
    7324: (
        "M-megera controladora, eu?!\nRepete isso se tiver coragem,\nque eu te taco um Meteoro!",
        "rewritten",
        "Misha engatilhando sua bomba mais destrutiva diante da acusação."
    ),
    7325: (
        "Pois eu te taco uma Bomba Megaflam!",
        "rewritten",
        "Aurica puxando a bomba clássica e flamejante de Marie para revidar."
    ),
    7326: (
        "P-parem com isso agora!!",
        "rewritten",
        "Lyner apavorado vendo a iminência de um cataclismo em plena academia."
    ),
    7327: (
        "Toma essa!!",
        "rewritten",
        "Misha arremessando o Meteoro com fúria cômica."
    ),
    7328: (
        "Toma vocêeee!!",
        "rewritten",
        "Aurica jogando a Bomba Megaflam com igual desespero bélico."
    ),
    7329: (
        "Uoooou! O prédio vai desabar!\nOlha a besteira que vocês fizeram...!!",
        "rewritten",
        "Lyner berrando enquanto as paredes do templo acadêmico vêm abaixo."
    ),
    7330: (
        "Deu ruim! Lyner, corre!!",
        "rewritten",
        "Misha puxando Lyner para escapar do desmoronamento generalizado."
    ),
    7331: (
        "O Lyner vai fugir comigo!!",
        "rewritten",
        "Aurica disputando o braço de Lyner em meio aos escombros."
    ),
    7332: (
        "Comigo! Enlouqueceu de vez?!",
        "rewritten",
        "Misha puxando de volta com ciúmes possessivo."
    ),
    7333: (
        "Não interessa, só corram logo!!",
        "rewritten",
        "Lyner desesperado para não ser esmagado pelas pedras que caem."
    ),
    7334: (
        "E foi assim! 『Atelier Elie: O Alquimista de Salburg 2』\né um jogo desse jeitinho! Não deixem de comprar e jogar, pessoal!",
        "rewritten",
        "Misha quebrando a quarta parede com o comercial promocional canônico de Gust."
    ),
    7335: (
        "N-nada a ver, nada a ver! Não tem nada a ver!\nO jogo não tem nada disso, gente!",
        "rewritten",
        "Lyner protestando indignado com a propaganda absurdamente enganosa de Misha."
    ),
    7336: (
        "Bora pra Stonehenge!\nPrecisamos dar o fora deste mundo!",
        "rewritten",
        "Misha convocando o parceiro para o marco sagrado de saída do mundo mental."
    ),
    7337: (
        "...Ninguém merece.",
        "rewritten",
        "Lyner soltando o clássico desabafo de quem suportou uma tempestade sem sentido."
    ),
    7338: (
        "Ai, ai... Passamos por poucas e boas, hein?",
        "rewritten",
        "Lyner respirando aliviado após a evasão caótica."
    ),
    7339: (
        "Mas que foi divertido, foi!",
        "rewritten",
        "Misha sorrindo radiante e satisfeita com a brincadeira interdimensional."
    ),
    7340: (
        "Você retornou à Cosmosfera de Misha.",
        "rewritten",
        "Mensagem de sistema notificando o retorno ao espaço base da mente de Misha."
    ),
    7341: (
        "Você teceu a Magia Vermelha [Meteoro]!",
        "rewritten",
        "Mensagem de sistema cravando o nascimento da Magia Vermelha conforme o glossário."
    ),
    7342: (
        "Sejam bem-vindos de volta, rapaz e Misha.",
        "rewritten",
        "Fukashigi (Guia da Cosmosfera) acolhendo a dupla com nobre serenidade."
    ),
    7343: (
        "U-ué? Eu ainda tô com essa roupa...?!",
        "rewritten",
        "Misha notando com surpresa que continuou vestida com o traje de Elie."
    ),
    7344: (
        "Esta vestimenta é um presente meu.\nFaça bom proveito dela.",
        "rewritten",
        "Fukashigi presenteando Misha com a vestimenta especial de alquimista."
    ),
    7345: (
        "...Voltei ao normal...",
        "rewritten",
        "Misha reassumindo suas roupas tradicionais de Reyvateil."
    ),
    7346: (
        "Mas me digam: como foi a experiência?\nPuderam desfrutar plenamente do mundo virtual?",
        "rewritten",
        "Fukashigi avaliando o grau de imersão e aprendizado dos viajantes mentais."
    ),
    7347: (
        "Mais do que diversão,\neu nem entendi o que diabos tava acontecendo.",
        "rewritten",
        "Lyner admitindo com franqueza que foi arrastado por um turbilhão caótico."
    ),
    7348: (
        "Fico imensamente satisfeita.\nComo atingiram meus padrões de avaliação,\ntenho mais uma dádiva a lhes conceder.",
        "rewritten",
        "Fukashigi atestando o sucesso da provação e anunciando a recompensa definitiva."
    ),
    7349: (
        "Peço-lhes que aceitem minha humilde essência\ne a entoem como a Canção de Misha.",
        "rewritten",
        "Fukashigi oferecendo sua própria alma para ser entoada como poder harmônico."
    ),
    7350: (
        "Hã?",
        "rewritten",
        "Misha pega de surpresa pelo desprendimento da guia."
    ),
    7351: (
        "Eu sou a guardiã do mistério e do insólito que habitam em Misha.\nAqui e agora, me unirei a ela por completo.",
        "rewritten",
        "Fukashigi revelando ser a personificação do Enigma interior e consumando a fusão psíquica."
    ),
    7352: (
        "Sendo assim, até o dia em que nos reencontrarmos...\nPassar bem...",
        "rewritten",
        "Fukashigi despedindo-se com reverência e dissolvendo-se na essência de Misha."
    ),
    7353: (
        "......",
        "approved_as_is",
        "Silêncio reflexivo após a fusão da guia com a psique de Misha."
    ),
    7354: (
        "Ela desapareceu.",
        "rewritten",
        "Lyner constatando o sumiço sereno da entidade mental."
    ),
    7355: (
        "Parece até... que tudo acabou agora.",
        "rewritten",
        "Misha sentindo a completude de sua alma e o fechamento de um ciclo profundo."
    ),
    7356: (
        "É o que você sente?",
        "rewritten",
        "Lyner sintonizando a sensibilidade e a paz da amiga de infância."
    ),
    7357: (
        "Sim. Não restou mais nada.\nNão tem mais nada que eu precise mostrar pro Lyner.\nNem nenhum segredo que eu ainda esteja escondendo.",
        "rewritten",
        "Misha declarando com pureza cristalina que sua alma está 100% aberta e entregue a Lyner."
    ),
    7358: (
        "É maravilhoso ter uma cumplicidade assim, não é?",
        "rewritten",
        "Misha exaltando a beleza de um amor sem amarras nem segredos."
    ),
    7359: (
        "É verdade. Com certeza é.",
        "rewritten",
        "Lyner correspondendo com calor e serenidade ao vínculo inquebrantável."
    ),
    7360: (
        "Você teceu a Magia Azul [Enigma]!",
        "rewritten",
        "Mensagem de sistema sacramentando a aquisição da magia azul [Enigma] (Fukashigi/Miracle)."
    ),

    # =========================================================================
    # EVENT: Event/802.evd (IDs 7361 - 7414) [54 falas] - Cosmosfera de Shurelia: Escola Secundária & Confissão de Leila
    # =========================================================================
    7361: (
        "...M-malditos...!\nAté quando vão ficar no meu caminho...?!!",
        "rewritten",
        "Claire (antagonista escolar da Cosmosfera) praguejando contra as interferências da dupla."
    ),
    7362: (
        "Já que é assim,\nvou espalhar todos os vírus que tenho pela cidade inteira!",
        "rewritten",
        "Claire ameaçando libertar uma praga virótica em escala urbana."
    ),
    7363: (
        "Haaah!!",
        "rewritten",
        "Claire tentando acionar seu comando supremo de liberação de vírus."
    ),
    7364: (
        "......",
        "approved_as_is",
        "Pausa dramática onde nenhum efeito ocorre."
    ),
    7365: (
        "Por que?! Por que não tá saindo nada?!",
        "rewritten",
        "Claire desesperada com a falha de seu mecanismo de invocação."
    ),
    7366: (
        "...É inútil.\nNós destruímos todo o seu depósito de vírus.",
        "rewritten",
        "Reyvateil da Cosmosfera anunciando com firmeza a aniquilação prévia do arsenal biológico."
    ),
    7367: (
        "O-o-o quê?! O que você disseee?!",
        "rewritten",
        "Claire em choque e desespero diante da derrota esmagadora."
    ),
    7368: (
        "Os meus... os meus vírus...!",
        "rewritten",
        "Claire lamentando a perda do trabalho de sua vida virótica."
    ),
    7369: (
        "Uaaaarghhh!!",
        "rewritten",
        "Claire fugindo aos berros em humilhação absoluta."
    ),
    7370: (
        "......",
        "approved_as_is",
        "Silêncio aliviado após a expulsão da vilã."
    ),
    7371: (
        "......",
        "approved_as_is",
        "Leila (Shurelia estudante) imóvel, processando a tensão acumulada."
    ),
    7372: (
        "Togasaki... me perdoa...\nEu não consegui confiar plenamente em você...",
        "rewritten",
        "Lyner Harasett pedindo desculpas sinceras por ter hesitado em estender a mão a Leila Togasaki."
    ),
    7373: (
        "...Harasett...",
        "rewritten",
        "Leila chamando Lyner pelo sobrenome escolar com comoção contida."
    ),
    7374: (
        "Por causa disso, quando encontramos o ELMA pela primeira vez,\neu não fui capaz de segurar a sua mão...",
        "rewritten",
        "Lyner confessando a dor de ter falhado na hora em que ela mais precisava de amparo diante de ELMA."
    ),
    7375: (
        "...Eu é que... devo pedir desculpas...",
        "rewritten",
        "Leila assumindo sua parcela de culpa na desconfiança mútua."
    ),
    7376: (
        "...Hã?",
        "rewritten",
        "Lyner sem entender por que ela estaria se desculpando."
    ),
    7377: (
        "Até o dia de hoje, eu também não conseguia confiar de verdade.\nAchei que você não se importava nem um pouco comigo...",
        "rewritten",
        "Leila desabafando sobre sua profunda insegurança de se sentir descartável para Lyner."
    ),
    7378: (
        "Você tinha a Aurica ao seu lado.\nMesmo dizendo que eram só amigos de infância,\nparecia que seus corações estavam unidos.\nPor isso, senti que não havia espaço para mim...",
        "rewritten",
        "Leila revelando a dor silenciosa de ter se sentido uma intrusa diante do vínculo entre Lyner e Aurica."
    ),
    7379: (
        "Quando você me convidou para a piscina,\nachei que fosse só por pena...\nPor isso... acordei tão desanimada esta manhã.",
        "rewritten",
        "Leila explicando a tristeza que sentiu pela manhã ao interpretar o convite como mera caridade."
    ),
    7380: (
        "Não é nada disso!\nEu esperei ansioso por este dia o tempo todo.\nDepois de tudo o que houve, fiquei inseguro, mas...",
        "rewritten",
        "Lyner desmentindo veementemente e confessando sua ansiedade pura pelo encontro com ela."
    ),
    7381: (
        "...É mesmo...?\nQue bom... Agora meu coração se acalmou...",
        "rewritten",
        "Leila suspirando aliviada, vendo suas angústias se dissiparem na ternura de Lyner."
    ),
    7382: (
        "......",
        "approved_as_is",
        "Olhar mútuo de cumplicidade amorosa em meio à cidade."
    ),
    7383: (
        "É muito lindo esse clima de romance entre vocês,\nmas ficar no meio da cidade só de roupa de banho\né meio sem noção, não acham?",
        "rewritten",
        "Reyvateil da Cosmosfera quebrando o clima romântico ao alertar que estão em trajes de banho em público."
    ),
    7384: (
        "...Hã?!",
        "rewritten",
        "Leila caindo na realidade de sua nudez relativa no asfalto."
    ),
    7385: (
        "Uou! E-eita nós!\nEu nem tinha reparado!",
        "rewritten",
        "Lyner entrando em pânico ao notar que também está de calção de banho no meio da multidão."
    ),
    7386: (
        "Aaaah, que vergonha!!\nNão tenho mais cara pra andar na rua...",
        "rewritten",
        "Leila cobrindo o rosto em vergonha mortal."
    ),
    7387: (
        "Ai, que horror! Que humilhação!\nTava todo mundo encarando a gente agorinha mesmo...",
        "rewritten",
        "Leila indignada com os olhares indiscretos que receberam dos transeuntes."
    ),
    7388: (
        "E você queria o quê...? É a reação normal de qualquer um.",
        "rewritten",
        "Lyner admitindo com bom senso que qualquer um olharia duas pessoas de maiô na rua."
    ),
    7389: (
        "Ai, seu idiota!\nPor que não percebeu antes?!",
        "rewritten",
        "Leila jogando a culpa em Lyner com charme irritadiço de colegial."
    ),
    7390: (
        "A culpa é minha agora?!",
        "rewritten",
        "Lyner reagindo com indignação cômica à transferência de culpa."
    ),
    7391: (
        "Humf!!",
        "rewritten",
        "Leila inflando as bochechas emburrada."
    ),
    7392: (
        "Tá bom, tá bom... Foi mal, eu errei.",
        "rewritten",
        "Lyner cedendo prontamente para desarmar o bico da garota."
    ),
    7393: (
        "Hehe, assim tá melhor!",
        "rewritten",
        "Leila sorrindo vitoriosa ao arrancar o pedido de desculpas."
    ),
    7394: (
        "Caramba, não tem como vencer a Togasaki mesmo...",
        "rewritten",
        "Lyner admitindo resignado o poder avassalador do charme feminino de Togasaki."
    ),
    7395: (
        "......",
        "approved_as_is",
        "Hesitação tímida de Leila antes de dar um passo decisivo em direção à intimidade."
    ),
    7396: (
        "...Olha, tem uma coisa...\nEu queria te pedir um favor...",
        "rewritten",
        "Leila puxando assunto com timidez adorável."
    ),
    7397: (
        "Será que... de agora em diante...\nvocê poderia me chamar pelo meu primeiro nome...?",
        "rewritten",
        "Leila rompendo a barreira formal e pedindo para ser chamada pelo primeiro nome (Leila)."
    ),
    7398: (
        "...Hã...?",
        "rewritten",
        "Lyner atônito diante do pedido tão íntimo no contexto escolar japonês."
    ),
    7399: (
        "F-falando sério?",
        "rewritten",
        "Lyner gaguejando diante do avanço afetivo inesperado."
    ),
    7400: (
        "Sim.\nChama agora.",
        "rewritten",
        "Leila exigindo a pronúncia imediata com autoridade meiga."
    ),
    7401: (
        "......",
        "approved_as_is",
        "Lyner engolindo em seco, reunindo coragem para falar."
    ),
    7402: (
        "Vai logo!",
        "rewritten",
        "Leila impaciente e divertida pressionando o parceiro."
    ),
    7403: (
        "Lei... Leila...",
        "rewritten",
        "Lyner pronunciando 'Leila' pela primeira vez com extrema hesitação e rubor."
    ),
    7404: (
        "Aahahaha! Que engraçado!\nVocê tá todo nervoso!",
        "rewritten",
        "Leila caindo na gargalhada diante do constrangimento fofo de Lyner."
    ),
    7405: (
        "N-não enche!\nMe deixa em paz...",
        "rewritten",
        "Lyner resmungando envergonhado, tentando disfarçar as bochechas coradas."
    ),
    7406: (
        "Hehe, desculpa.",
        "rewritten",
        "Leila se recompondo docemente com um sorriso terno."
    ),
    7407: (
        "Será que eu também posso...\nte chamar de Lyner daqui em diante...?",
        "rewritten",
        "Leila pedindo reciprocidade para abandonar o formal 'Harasett' e chamá-lo de 'Lyner'."
    ),
    7408: (
        "É... claro.\nFazer o quê, eu deixo.",
        "rewritten",
        "Lyner concedendo com pose arrogante mas transbordando felicidade por dentro."
    ),
    7409: (
        "Ora, ora... quanta pose pro meu gosto, Lyner.",
        "rewritten",
        "Leila saboreando o prazer de chamá-lo de 'Lyner' pela primeira vez, zombando de sua empáfia."
    ),
    7410: (
        "...Pfft... Aahahaha!",
        "rewritten",
        "Lyner desabando em riso frouxo ao lado dela."
    ),
    7411: (
        "...Aahahaha!",
        "rewritten",
        "Leila unindo sua risada à dele em harmonia perfeita."
    ),
    7412: (
        "Ai! Os fogos de artifício já começaram!",
        "rewritten",
        "Leila avistando o espetáculo pirotécnico no céu noturno."
    ),
    7413: (
        "Droga!\nA gente enrolou demais!",
        "rewritten",
        "Lyner notando que a conversa íntima consumiu o horário do festival."
    ),
    7414: (
        "Vou dar um pulo em casa para me trocar!\nA gente se vê no Parque com Vista pro Mar!",
        "rewritten",
        "Leila despedindo-se correndo para o ponto de encontro romântico."
    ),

    # =========================================================================
    # EVENT: Event/405.evd (IDs 7415 - 7482) [68 falas] - Mundo Real: O Resgate do Divisor FFT e o Encontro com ELMA
    # =========================================================================
    7415: (
        "Aqui dentro...\nestá o [Divisor FFT]...",
        "rewritten",
        "Lyner contemplando o interior da barreira de energia onde jaz o artefato crucial."
    ),
    7416: (
        "Senhora Shurelia...\nEu juro que vou levar isso\ne resgatar a senhora!",
        "rewritten",
        "Lyner jurando solene libertar Shurelia do martírio com a ajuda do Divisor FFT."
    ),
    7417: (
        "...Muito bem!\nÉ agora ou nunca!",
        "rewritten",
        "Lyner preparando-se psicologicamente para enfrentar o escudo de força."
    ),
    7418: (
        "...Hã?!",
        "rewritten",
        "Misha percebendo o movimento temerário de Lyner em direção ao escudo."
    ),
    7419: (
        "Uoooou...!",
        "rewritten",
        "Lyner sendo repelido com violência pelo choque do campo de força."
    ),
    7420: (
        "Lyner!!",
        "rewritten",
        "Misha gritando em pânico ao ver o companheiro atingido pela energia."
    ),
    7421: (
        "Lyner! Você está bem?!",
        "rewritten",
        "Radolf correndo em socorro militar do companheiro."
    ),
    7422: (
        "Francamente...\nsempre imprudente desse jeito...",
        "rewritten",
        "Jack reprovando com ceticismo a impulsividade de Lyner."
    ),
    7423: (
        "Aiaiai...\nAcabei baixando a guarda.",
        "rewritten",
        "Lyner queixando-se da dor mas mantendo o foco analítico."
    ),
    7424: (
        "Ei! Ficou maluco?!\nMeu coração quase saiu pela boca!",
        "rewritten",
        "Misha esbravejando em desespero e alívio por ele estar vivo."
    ),
    7425: (
        "Hehe, foi mal, foi mal.",
        "rewritten",
        "Lyner rindo sem jeito para tranquilizar a amiga."
    ),
    7426: (
        "Mas, pelo que senti agora,\ntenho a impressão de que consigo passar por aquela barreira.",
        "rewritten",
        "Lyner avaliando a resistência física necessária para cruzar o limiar de choque."
    ),
    7427: (
        "O quê?!\nIsso é loucura demais...",
        "rewritten",
        "Misha implorando contra o suicídio quase certo de atravessar a barreira viva."
    ),
    7428: (
        "Misha...\nPreciso da sua cobertura.",
        "rewritten",
        "Lyner pedindo com seriedade inabalável o apoio mágico da amiga."
    ),
    7429: (
        "...Hã?",
        "rewritten",
        "Misha atônita diante da confiança plena que Lyner deposita nela."
    ),
    7430: (
        "Continue entoando a magia de cura mais poderosa\nque você for capaz de tecer. Sem parar nem por um segundo.",
        "rewritten",
        "Lyner confiando seu corpo biológico à ressonância de regeneração contínua de Misha."
    ),
    7431: (
        "...Lyner.",
        "rewritten",
        "Misha comovida e assombrada pelo peso da responsabilidade sobre a vida dele."
    ),
    7432: (
        "Meu pai me avisou.\nNão existe jeito de desativar aquela barreira.",
        "rewritten",
        "Lyner lembrando as palavras do Patriarca Leard sobre a impenetrabilidade do santuário."
    ),
    7433: (
        "Mas a gente não pode se dar ao luxo\nde ficar empacado aqui.",
        "rewritten",
        "Lyner demonstrando a coragem estoica de arriscar a própria carne pelo bem do mundo."
    ),
    7434: (
        "......",
        "approved_as_is",
        "Misha em silêncio angustiado diante da gravidade da escolha."
    ),
    7435: (
        "Por favor... Misha!",
        "rewritten",
        "Lyner reiterando seu apelo fraternal de pura entrega."
    ),
    7436: (
        "......",
        "approved_as_is",
        "Misha respirando fundo, conectando-se ao seu dever supremo como Cantora das Estrelas."
    ),
    7437: (
        "É porque é você, Misha...\nÉ por isso que confio a minha vida nas suas mãos.",
        "rewritten",
        "Lyner expressando com clareza cristalina a lição que Aurica lhe ensinou no bloco anterior: confiar e se deixar amparar por Misha."
    ),
    7438: (
        "Porque... sou eu?",
        "rewritten",
        "Misha sentindo o calor e o eco das palavras de infância ressoarem em sua alma."
    ),
    7439: (
        "Sim...",
        "rewritten",
        "Lyner assentindo com olhar firme e amoroso."
    ),
    7440: (
        "...Entendido.\nSe é o seu pedido, Lyner...\nEu vou cantar!",
        "rewritten",
        "Misha aceitando com honra e determinação entoar a canção que preservará a vida dele."
    ),
    7441: (
        "Obrigado.\nConto com você...",
        "rewritten",
        "Lyner agradecendo antes de mergulhar na energia devastadora."
    ),
    7442: (
        "#0Was yant ga exec heas lyner.",
        "approved_as_is",
        "Preservação canônica estrita da tag ancestral de Hymmnos e da Canção de cura de Misha para proteger Lyner."
    ),
    7443: (
        "...\nMisha... conto com você...",
        "rewritten",
        "Lyner adentrando o escudo de energia concentrada, sussurrando sua fé na Canção."
    ),
    7444: (
        "Ugh...\nGuaaah...!",
        "rewritten",
        "Lyner suportando a descarga maciça de eletricidade e estática nos músculos."
    ),
    7445: (
        "Lyner! Não vá além das suas forças!",
        "rewritten",
        "Radolf clamando do lado de fora com angústia de comandante."
    ),
    7446: (
        "...Eu tô bem...\nA Misha tá... me protegendo...",
        "rewritten",
        "Lyner sentindo as ondas restauradoras de Hymmnos cicatrizando sua carne no mesmo milissegundo."
    ),
    7447: (
        "...É... isso...?\nEste é o [Divisor FFT]...?",
        "rewritten",
        "Lyner alcançando o núcleo do pedestal e tocando o componente lendário."
    ),
    7448: (
        "Atenção! Tem alguma coisa vindo aí!!",
        "rewritten",
        "Jack detectando aproximação hostil no radar mecânico do setor."
    ),
    7449: (
        "Mas o que é isso...?!!",
        "rewritten",
        "Jack surpreso diante do vulto cibernético maciço que desponta."
    ),
    7450: (
        "Lyner, depressa!!\nSaia daí imediatamente!",
        "rewritten",
        "Radolf ordenando a retirada emergencial antes que o guardião cerre a saída."
    ),
    7451: (
        "Tô... saindo...",
        "rewritten",
        "Lyner recolhendo o artefato e forçando o passo de volta através da barreira."
    ),
    7452: (
        "Lyner!!",
        "rewritten",
        "Misha acolhendo o retorno do jovem cavaleiro."
    ),
    7453: (
        "...Eu... tô bem...\nMais importante que isso...",
        "rewritten",
        "Lyner recuperando o fôlego e apontando para a ameaça que acaba de se materializar."
    ),
    7454: (
        "Pelo visto, temos a honra\nde receber o Guardião deste lugar!",
        "rewritten",
        "Jack anunciando sarcasticamente a chegada do sentinela dos santuários."
    ),
    7455: (
        "Lyner! Você tá bem...?!\nParecia sentir tanta dor lá dentro...",
        "rewritten",
        "Misha examinando o corpo dele em busca de queimaduras ou feridas profundas."
    ),
    7456: (
        "Não, eu tô legal...\nMuito obrigado, Misha.",
        "rewritten",
        "Lyner tranquilizando-a com carinho fraternal e sincera gratidão."
    ),
    7457: (
        "...De nada.",
        "rewritten",
        "Misha sorrindo aliviada por ter mantido seu parceiro a salvo com sua melodia."
    ),
    7458: (
        "...\nMisha... conto com você...",
        "rewritten",
        "Ramificação alternativa/loop do script de travessia do escudo."
    ),
    7459: (
        "Ugh...\nGuaaah...!",
        "rewritten",
        "Ramificação alternativa de Lyner suportando a descarga de força."
    ),
    7460: (
        "Lyner! Não vá além das suas forças!",
        "rewritten",
        "Ramificação alternativa de Radolf alertando sobre o risco de sobrecarga."
    ),
    7461: (
        "...Eu tô bem...\nA Misha tá... me protegendo...",
        "rewritten",
        "Ramificação alternativa de Lyner reafirmando a proteção de Misha."
    ),
    7462: (
        "...É... isso...?\nEste é o [Divisor FFT]...?",
        "rewritten",
        "Ramificação alternativa confirmando a posse do Divisor FFT."
    ),
    7463: (
        "Atenção! Tem alguma coisa vindo aí!!",
        "rewritten",
        "Ramificação alternativa de Jack soando o alarme de perigo."
    ),
    7464: (
        "Mas o que é isso...?!!",
        "rewritten",
        "Ramificação alternativa do espanto de Jack."
    ),
    7465: (
        "Lyner, depressa!!\nSaia daí imediatamente!",
        "rewritten",
        "Ramificação alternativa de Radolf exigindo a evasão célere."
    ),
    7466: (
        "Tô... saindo...",
        "rewritten",
        "Ramificação alternativa da saída extenuada de Lyner."
    ),
    7467: (
        "Lyner!!",
        "rewritten",
        "Ramificação alternativa de Misha chamando pelo companheiro."
    ),
    7468: (
        "...Eu... tô bem...\nMais importante que isso...",
        "rewritten",
        "Ramificação alternativa do cavaleiro focalizando o inimigo."
    ),
    7469: (
        "Pelo visto, temos a honra\nde receber o Guardião deste lugar!",
        "rewritten",
        "Ramificação alternativa de Jack preparando as armas."
    ),
    7470: (
        "Lyner! Você tá legal...?\nA minha Canção...\nchegou até você com força total?",
        "rewritten",
        "Misha perguntando ansiosa se a pulsação de sua Canção de proteção operou com eficácia."
    ),
    7471: (
        "Com certeza, sem sombra de dúvida.\nObrigado, Misha.",
        "rewritten",
        "Lyner louvando a perfeição da sintonia mágica que os une."
    ),
    7472: (
        "...Uhum.",
        "rewritten",
        "Misha assentindo docemente e cheia de orgulho."
    ),
    7473: (
        "Mas que diabos era essa carcaça...?\nEra o guardião deste setor?",
        "rewritten",
        "Jack examinando a carcaça mecânica do inimigo abatido."
    ),
    7474: (
        "Eu...\neu conheço esse carinha...",
        "rewritten",
        "Misha reconhecendo o design ancestral do autômato sagrado."
    ),
    7475: (
        "Se não me engano, é o Guardião pessoal\nda Senhora Shurelia.\nO nome dele é [ELMA].",
        "rewritten",
        "Misha identificando o autômato sagrado ELMA, sentinela exclusivo de Shurelia."
    ),
    7476: (
        "O quê?! Pessoal da Senhora Shurelia?!\nExistia mesmo um autômato desses?!",
        "rewritten",
        "Radolf perplexo ao saber da existência de um guardião direto da Administradora."
    ),
    7477: (
        "ELMA, é...?\nO formato dele é tão parecido\ncom os vírus que enfrentamos antes...",
        "rewritten",
        "Lyner notando a semelhança morfológica estarrecedora entre o nobre ELMA e as bestas viróticas."
    ),
    7478: (
        "Talvez a Mir tenha criado aqueles vírus\ncomo uma paródia doentia deste guardião...",
        "rewritten",
        "Krusche lançando a brilhante dedução técnica sobre o ódio e a ironia de Mir contra Shurelia."
    ),
    7479: (
        "Maldita seja, Mir...\nAté o Guardião da Senhora Shurelia você profanou...",
        "rewritten",
        "Lyner cerrando os punhos com indignação moral diante da corrupção operada por Mir."
    ),
    7480: (
        "Precisamos usar este [Divisor FFT]\npara arrancá-la da Senhora Shurelia de uma vez por todas...!!",
        "rewritten",
        "Lyner reafirmando o propósito sagrado da missão: libertar Shurelia usando o Divisor FFT."
    ),
    7481: (
        "Agora, resta apenas\nescalar a Torre.",
        "rewritten",
        "Radolf apontando o caminho rumo ao cume onde se decidirá o destino de Sol Ciel."
    ),
    7482: (
        "É isso aí, vamos depressa!",
        "rewritten",
        "Krusche incitando o avanço imediato sem perder um segundo sequer."
    )
}

# Verificação de cobertura total
assert len(curations) == 223, f"Esperado 223 falas mapeadas, obtido {len(curations)}"

curated_dialogues = []
translations_list = []
validation_errors = {}

lines_rewritten = 0
lines_approved_as_is = 0

for d in raw_dialogues:
    d_id = d["id"]
    event_file = d["event_file"]
    speaker_id = d["speaker_id"]
    speaker = d["speaker"]
    orig_jp = d["original_jp"]
    orig_en = d["original_en"]
    current_ptbr = d["current_ptbr"]
    
    if d_id not in curations:
        print(f"ERRO: ID {d_id} ausente do dicionário de curadoria!")
        sys.exit(1)
        
    curated_text, verdict, rationale = curations[d_id]
    
    # Validação determinística
    errs = validate_line(d_id, orig_en, curated_text)
    if errs:
        validation_errors[d_id] = errs
        
    if verdict == "rewritten":
        lines_rewritten += 1
    elif verdict == "approved_as_is":
        lines_approved_as_is += 1
        
    entry = {
        "id": d_id,
        "event_file": event_file,
        "speaker_id": speaker_id,
        "speaker": speaker,
        "original_jp": orig_jp,
        "original_en": orig_en,
        "current_ptbr": current_ptbr,
        "curated_ptbr": curated_text,
        "text": curated_text,
        "verdict": verdict,
        "rationale": rationale
    }
    curated_dialogues.append(entry)
    translations_list.append({
        "id": d_id,
        "text": curated_text
    })

if validation_errors:
    print(f"ERROS DE VALIDAÇÃO TÉCNICA DETECTADOS ({len(validation_errors)}):")
    for d_id, err_list in validation_errors.items():
        print(f"  ID {d_id}: {err_list}")
    sys.exit(1)
else:
    print("Todas as 223 falas passaram com 100% de sucesso no Hard Gate Técnico!")

highlights = [
    {
        "id": 7283,
        "speaker": "Misha / Lyner",
        "description": "Correção dramática e canônica crucial da identidade de Marlone (Marie de Atelier Marie), errada pelo inglês que a tratou como homem ('he/him'). Misha narra com beleza literária sua inspiração de infância por Marie e sua entrada na Academia de Salburg."
    },
    {
        "id": 7317,
        "speaker": "Aurica / Misha / Lyner",
        "description": "Clímax cômico da paródia de Atelier Elie na Cosmosfera de Misha: a revelação de que a reverenciada Marlone é encarnada por Aurica, desencadeando um duelo de ciúmes e arremesso de bombas (Meteoro vs Bomba Megaflam) que derruba a Academia de Alquimia."
    },
    {
        "id": 7334,
        "speaker": "Misha / Lyner",
        "description": "Quebra genial da quarta parede onde Misha faz o comercial promocional canônico de 'Atelier Elie: O Alquimista de Salburg 2' e Lyner protesta aos berros contra a propaganda absurda e enganosa."
    },
    {
        "id": 7357,
        "speaker": "Misha / Lyner",
        "description": "Fusão mística de Fukashigi com a psique de Misha gerando a Magia Azul [Enigma] e a confissão sublime de Misha de que sua alma está inteiramente exposta a Lyner, sem mais nenhum segredo ou barreira entre eles."
    },
    {
        "id": 7378,
        "speaker": "Leila (Shurelia) / Lyner",
        "description": "Na Cosmosfera escolar, Leila desabafa sua dor silenciosa e insegurança diante do vínculo de Lyner com Aurica, culminando no pedido meigo e íntimo para que ambos abandonem a formalidade dos sobrenomes e se chamem pelos primeiros nomes (Leila e Lyner)."
    },
    {
        "id": 7437,
        "speaker": "Lyner / Misha",
        "description": "Lyner arrisca o próprio corpo para atravessar o escudo letal de força em busca do [Divisor FFT], entregando sua vida à Canção de cura de Misha ('É porque é você, Misha... É por isso que confio a minha vida nas suas mãos'), consolidando o amadurecimento e a cumplicidade de ambos."
    },
    {
        "id": 7475,
        "speaker": "Misha / Krusche / Lyner",
        "description": "Identificação do Guardião sagrado ELMA, sentinela exclusivo de Shurelia, e a brilhante dedução de Krusche de que os vírus de Mir foram criados como uma paródia doentia deste nobre autômato."
    }
]

new_terms = {
    "FFT Divider": {
        "pt": "Divisor FFT",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Síntese Grathmeld",
        "note": "FFTディバイダ. Dispositivo de alta frequência para separação e purificação harmônica, apelidado de 'O Início do Perigo'."
    },
    "ELMA": {
        "pt": "ELMA",
        "gender": "masculino",
        "number": "singular",
        "category": "Guardião / Mecânico",
        "note": "エルマ. Guardião ancestral pessoal construído por Shurelia para proteger os santuários da Torre de Ar tonelico."
    },
    "Castagne": {
        "pt": "Castagne",
        "gender": "feminino",
        "number": "singular",
        "category": "Topônimo / Atelier Elie",
        "note": "港町カスターニェ. Cidade portuária célebre por sua pesca no mundo de Salburg em Atelier Elie."
    },
    "Salburg Academy": {
        "pt": "Academia de Salburg",
        "gender": "feminino",
        "number": "singular",
        "category": "Local / Atelier",
        "note": "ザールブルグのアカデミー. Academia de alquimistas frequentada por Marie e Elie."
    },
    "Marlone": {
        "pt": "Marlone",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / Atelier Marie",
        "note": "マルローネ / マリー. Protagonista de Atelier Marie, salvadora de Elie na infância e grande ídolo de Misha na Cosmosfera."
    },
    "Megaflam": {
        "pt": "Megaflam",
        "gender": "feminino",
        "number": "singular",
        "category": "Item / Alquimia",
        "note": "メガフラム. Bomba alquímica clássica de dano ígneo maciço da franquia Atelier."
    }
}

updated_address_matrix = {
    "Lyner": {
        "Misha": "Confiança incondicional de entregar a própria vida à Canção de cura dela para cruzar a barreira de energia letal.",
        "Shurelia": "Tratamento na Cosmosfera evoluindo de 'Togasaki' formal para o primeiro nome íntimo 'Leila', rindo juntos com cumplicidade."
    },
    "Misha": {
        "Lyner": "Entrega emocional sublime ('não tenho mais nenhum segredo escondendo de você') e orgulho de protegê-lo com a Canção de cura.",
        "Aurica": "Disputa cômica de ciúmes arremessando bombas em meio à paródia de Atelier Elie na Cosmosfera."
    },
    "Aurica": {
        "Misha": "Troca de farpas bem-humorada acusando Misha de ser uma megera controladora e disputando o braço de Lyner."
    },
    "Shurelia": {
        "Lyner": "Superação da timidez escolar pedindo a Lyner que a chame de 'Leila' e chamando-o carinhosamente de 'Lyner' pela primeira vez."
    }
}

scene_handoff = {
    "resumo_dramatico": "A hilaridade e o vínculo afetuoso no Nível 8 da Cosmosfera de Misha, onde ela recria o universo de Atelier Elie buscando sua salvadora Marlone (Marie), culminando na revelação cômica de que Marie é encarnada por Aurica, em um duelo bombástico e na fusão sublime da guia Fukashigi concedendo a Magia Azul [Enigma] e selando uma cumplicidade sem segredos com Lyner; o momento romântico e comovente na Cosmosfera escolar de Shurelia, onde Leila Togasaki e Lyner Harasett superam inseguranças e começam a se chamar pelos primeiros nomes ('Leila' e 'Lyner'); e no mundo real, a prova cabal de confiança onde Lyner arrisca o próprio corpo sob o escudo letal de força contando com a Canção contínua de Misha para resgatar o [Divisor FFT], enfrentando o Guardião pessoal da Senhora Shurelia, [ELMA], cujos dados revelam que os vírus de Mir foram criados como uma cópia profanada dele, partindo agora com determinação renovada para a escalada final da Torre.",
    "decisoes_terminologicas": {
        "Divisor FFT": "[Divisor FFT] (FFTディバイダ, artefato alquímico de alta frequência para libertação de Shurelia)",
        "ELMA": "[ELMA] (エルマ, autômato guardião sagrado pessoal de Shurelia)",
        "Marlone": "Marlone (マルローネ / マリー, heroína de Atelier Marie, mantida feminina no cânone)",
        "Megaflam": "Bomba Megaflam (メガフラム爆弾, item alquímico lendário de Atelier)",
        "Meteoro": "Magia Vermelha [Meteoro] (赤魔法【金属爆撃】)",
        "Enigma": "Magia Azul [Enigma] (青魔法【不可思議】)"
    },
    "alertas_para_proximo_bloco": "Atenção máxima à posse do Divisor FFT pelo grupo, à escalada vertical definitiva da Torre de Ar tonelico em direção ao santuário de Shurelia e Mir, e à preparação técnica para a cerimônia de separação harmônica de Mir."
}

output_data = {
    "block_id": "BLK_EVD_029",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "total_lines": len(curated_dialogues),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "highlights": highlights,
    "new_terms": new_terms,
    "updated_address_matrix": updated_address_matrix,
    "scene_handoff": scene_handoff,
    "dialogues": curated_dialogues,
    "entries": curated_dialogues,
    "translations": translations_list
}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Sucesso absoluto! Gravado {OUTPUT_PATH.name} com {len(curated_dialogues)} falas ({lines_rewritten} reescritas, {lines_approved_as_is} aprovadas).")

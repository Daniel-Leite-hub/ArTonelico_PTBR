# -*- coding: utf-8 -*-
import json
from pathlib import Path

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_036_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_036_output.json")

# Mapeamento ID -> (text_ptbr, justificativa)
CURATED_DATA = {
    8817: (
        "Olá, sejam muito bem-vindos!\nEsta é a Loja de Mergulho.",
        "Saudação calorosa e hospitaleira do atendente da Dive Shop com quebra de linha equilibrada ('いらっしゃい。ダイブ屋へようこそ')."
    ),
    8818: (
        "Moço, a gente quer mergulhar. Dá essa força pra gente?",
        "Misha solicitando o mergulho com sua habitual espontaneidade atirada e fofa ('おじさん、ダイブしたいの。お願い')."
    ),
    8819: (
        "Uau... mas que Reyvateil mais atirada!",
        "Espanto maravilhado do atendente diante do desprendimento e da petulância adorável de Misha ('うわぁ、大胆なレーヴァテイルたん!')."
    ),
    8820: (
        "Pois bem, como é a regra da casa,\nvou explicar o procedimento uma vez.",
        "Explicação do protocolo padrão da loja de forma natural em português ('それじゃ、決まり事だから一度説明するよ')."
    ),
    8821: (
        "O Mergulho é o processo de tecer uma Magia da Canção\ndentro do coração de uma donzela Reyvateil.",
        "Definição canônica do Mergulho com o verbo sagrado 'tecer' e preservação do termo 'Magia da Canção' ('ダイブってのは、レーヴァテイルたんの心の中で詩魔法を作り出す作業だ')."
    ),
    8822: (
        "Mais precisamente, é o trabalho de converter os sentimentos\nno coração dela... na Cosmosfera, em Canções.",
        "Explicação refinada da conversão dos sentimentos da Cosmosfera em Canções ('厳密には、彼女の心...コスモスフィアの中にある想いを詩に変換する作業なんだよ')."
    ),
    8823: (
        "A Cosmosfera está repleta de tudo o que ela já viveu...\ne de um monte de fantasias da cabeça dela.",
        "Restauração do termo 'fantasias / delírios' ('妄想'), essencial para a diegese e o humor psicológico de Ar tonelico, que havia sido apagado no inglês."
    ),
    8824: (
        "Você escolhe uma dessas memórias ou fantasias\ne tece uma Magia da Canção a partir dela.",
        "Conexão entre as memórias/fantasias e o ato de tecer a Magia da Canção ('その妄想や記憶の中から1つをピックアップして、詩魔法を作り出す')."
    ),
    8825: (
        "Esse é o seu papel aqui, amigão.",
        "Tom despojado e encorajador do terapeuta instruindo Lyner ('それがキミの仕事なんだ')."
    ),
    8826: (
        "Nós temos o poder de transformar os devaneios e memórias\nda nossa mente em Canções e materializá-los.",
        "Misha explicando o poder das Reyvateils de materializar ('具現化させる') pensamentos e memórias em forma de Canções."
    ),
    8827: (
        "Só que encarar esse processo de 'materializar'\ntudo sozinha dá um trabalho descomunal.",
        "Oralidade expressiva de Misha destacando as aspas em 'materializar' ('『具現化させる』') e o esforço solitário ('ものすごく大変なのよ')."
    ),
    8828: (
        "E como a gente tem que escancarar o próprio coração,\nnão dá pra ser com qualquer um, né?",
        "Subtexto de intimidade e cumplicidade de Misha com Lyner ('自分の心の中を見せるわけだから、誰でもイイわけじゃない')."
    ),
    8829: (
        "Por isso que elas precisam de um parceiro de confiança, entendeu?",
        "Comentário compreensivo do atendente reforçando a necessidade do parceiro de mergulho ('だから、信頼できるパートナーが必要なんだな')."
    ),
    8830: (
        "Exatamente.",
        "Assentimento confiante de Misha ('そういうこと')."
    ),
    8831: (
        "Além do mais, quanto mais a donzela Reyvateil confia em você,\nmais ela permite enxergar o fundo da sua alma.",
        "Tradução poética e precisa de '心を許せば許すほど、心の奥底まで見せてくれるよ'."
    ),
    8832: (
        "E, como os sentimentos mais profundos são os mais intensos,\neles naturalmente geram magias muito mais poderosas.",
        "Lógica causal da Cosmosfera entre profundidade emocional e poder mágico ('当然心の奥の方が強い思念を持ってるから、強い魔法になりやすい')."
    ),
    8833: (
        "Então, por esse motivo também, o laço que você constrói\ncom a donzela Reyvateil é fundamental.",
        "Enfatização do vínculo afetivo/espiritual ('絆') para o sucesso do Mergulho."
    ),
    8834: (
        "Lyner!",
        "Chamado direto e enérgico de Misha com exclamação conforme o original ('ライナー!')."
    ),
    8835: (
        "S-sim?!",
        "Hesitação cômica de Lyner diante da postura solene da amiga ('は、はい!?')."
    ),
    8836: (
        "Estou em suas mãos!",
        "Expressão cerimoniosa e dócil de Misha se entregando aos cuidados do parceiro ('よろしくお願いします!'), superando o decalque inventado do inglês."
    ),
    8837: (
        "É-é... pode deixar...",
        "Resposta acanhada e desajeitada de Lyner ('あ、ああ。よろしく...')."
    ),
    8838: (
        "Os tutoriais [Dive] e [Dive Point] foram adicionados.",
        "Mensagem de sistema com paridade estrita de colchetes e termos conforme original em inglês ('The [Dive] and [Dive Point] tutorials have been added')."
    ),
    8839: (
        "Gostaria de ver a explicação detalhada deste tutorial?",
        "Prompt de tutorial polido e direto ('このヘルプについての詳細な説明を見ますか?')."
    ),
    8840: (
        "Os DP obtidos nas batalhas podem ser usados durante o Mergulho.",
        "Concordância gramatical escorreita (DP como Pontos de Mergulho, masculino plural: 'Os DP') e termo canônico 'Mergulho'."
    ),
    8841: (
        "Ao mergulhar no mundo mental de uma Reyvateil,\nLyner é capaz de despertar o verdadeiro poder dela.",
        "Harmonização terminológica de '精神世界' como mundo mental e 'その力を引き出して' como despertar o verdadeiro poder dela."
    ),
    8842: (
        "Os Mergulhos são realizados nas Lojas de Mergulho presentes nas cidades.",
        "Termo canônico 'Loja de Mergulho' ('ダイブ屋') em frase elegante e concisa."
    ),
    8843: (
        "O custo para mergulhar varia de acordo com o nível do mundo mental.",
        "Eliminação do decalque errôneo 'Espaço da Alma' do inglês, restituindo o conceito canônico de mundo mental ('精神世界のレベル')."
    ),
    8844: (
        "Toda Reyvateil possui uma entidade em seu mundo mental conhecida como [Mind Guardian].",
        "Aplicação do termo canônico do Glossário Mestre [Mind Guardian] ('心の護 / Mind Guardian') com paridade estrita de colchetes com o original em inglês."
    ),
    8845: (
        "Eles têm a missão de proteger o coração da Reyvateil e acompanhar o seu crescimento.",
        "Definição do papel dos Guardiões Mentais ('彼女達はレーヴァテイルの心を護り、またその成長を見守っていく役目を持っています')."
    ),
    8846: (
        "Lyner viajará pelo mundo mental guiado pelas orientações dessa entidade.",
        "Papel de navegação do Guardião Mental no mundo mental ('ライナーは彼女達のナビゲートを受け、精神世界を旅して行くことになります')."
    ),
    8847: (
        "Dentro do mundo mental, utilize os botões direcionais para escolher o local até onde deseja ir.",
        "Instrução ergonômica de controle no mundo mental ('精神世界では方向キーを使って、行きたい場所へ移動します')."
    ),
    8848: (
        "Ao entrar em um dos pontos do mapa, um evento terá início.",
        "Clareza instrucional de acionamento de eventos ('ポインタに入るとイベントが発生します')."
    ),
    8849: (
        "O desfecho dos eventos no mundo mental é determinado pela quantidade de DP que você possui.",
        "Explicação do consumo e exigência de DP para sucesso nos eventos ('精神世界で起きるイベントは、DPによってその成否が決まります')."
    ),
    8850: (
        "Os DP também representam o nível de confiança mútua entre você e a Reyvateil.",
        "Correção crítica do erro de tradução do inglês (que dizia 'depends on you'), restituindo o sentido original de confiança mútua ('信頼度')."
    ),
    8851: (
        "Ao gastar DP, a Reyvateil abre o coração para você,\nrevelando novas facetas de sua personalidade.",
        "Expressão lírica e precisa de '心を許し、彼女達の新たな一面を見せてくれます' com quebra balanceada."
    ),
    8852: (
        "Porém, se faltarem DP,\nvocê será expulso do mundo mental da Reyvateil.",
        "Aviso de mecânica de expulsão por escassez de DP ('精神世界から追い出されてしまいます')."
    ),
    8853: (
        "Por isso, ao mergulhar em um mundo mental,\né recomendável acumular uma boa quantia de DP com antecedência.",
        "Dica prática de gerenciamento de DP ('精神世界へダイブする時は、DPを多めに持っておいた方がいいでしょう')."
    ),
    8854: (
        "Ao concluir com sucesso um evento no mundo mental,\na Reyvateil poderá tecer uma nova Canção.",
        "Uso do verbo canônico 'tecer' ('詩を紡ぎ出す') em sintonia com a cosmologia das Reyvateils."
    ),
    8855: (
        "Todas as Canções utilizadas em batalha ou nos cenários são obtidas no mundo mental.",
        "Esclarecimento sobre a origem de todas as Canções de combate e exploração ('戦闘やフィールドで使用する詩は、すべて精神世界から手に入ります')."
    ),
    8856: (
        "Se deseja usar Canções poderosas,\nmergulhe frequentemente para tecê-las!",
        "Estímulo instrucional ao jogador com quebra harmônica ('強力な詩を使いたいプレイヤーは、ダイブして詩を紡ぐといいでしょう')."
    ),
    8857: (
        "Haverá ocasiões no enredo em que o Mergulho será indispensável para avançar na história.",
        "Notificação de progressão obrigatória por eventos de história ('ストーリー上、先に進むためにダイブが必要となる場面も出てきます')."
    ),
    8858: (
        "Domine a arte do Mergulho\ne aprofunde seus laços com as Reyvateils!",
        "Chamada vibrante de encerramento do tutorial ('ダイブを使いこなして、レーヴァテイルとの絆を深めていってください!')."
    ),
    8859: (
        "Os DP (Pontos de Mergulho) são os pontos necessários\npara agir dentro do mundo mental de uma Reyvateil.",
        "Definição da sigla DP e sua aplicação no mundo mental ('DP=ダイブポイントは、レーヴァテイルの精神世界で、必要となるポイントです')."
    ),
    8860: (
        "Os Pontos de Mergulho são obtidos ao fim de cada batalha, junto com a experiência e o dinheiro.",
        "Clareza sobre o ganho de DP pós-batalha ('ダイブポイントは戦闘終了時、経験値、お金と一緒に手に入ります')."
    ),
    8861: (
        "A quantidade de DP recebida é calculada com base no desempenho na batalha, conforme os fatores a seguir.",
        "Apresentação dos fatores determinantes do bônus de DP ('もらえるDPの値は、戦闘中の次のような値によって決定されます')."
    ),
    8862: (
        "Os DP são contabilizados individualmente para cada Reyvateil, e todas as donzelas do grupo recebem pontos.",
        "Explicação da distribuição individual de DP ('DPはレーヴァテイルごとに設定され、仲間のレーヴァテイル全員が入手することができます')."
    ),
    8863: (
        "Utilize bem a Magia da Canção em combate para acumular muitos DP e facilitar suas jornadas no mundo mental.",
        "Dica estratégica conectando o uso de Magia da Canção ao rendimento de DP ('詩魔法を上手く使って、DPをたくさん貯めて精神世界での行動を有利に進めてください')."
    ),
    8864: (
        "Uma versão resumida deste tutorial pode ser consultada a qualquer momento no menu de [Help], em 'Como Jogar'.",
        "Referência de interface mantendo o marcador canônico [Help] com paridade estrita com o original em inglês ('menu of the [Help] menu')."
    ),
    8865: (
        "Além disso, os locais marcados com uma ★ são pontos cruciais onde ocorrem os eventos para a heroína tecer novas Canções.",
        "Explicação dos pontos com estrela ★ ('★マークの付いた場所は、ヒロインが詩を紡ぐ為に特に重要となるイベントが発生する場所です')."
    ),
    8866: (
        "É perigoso demais tentar chegar até lá...!",
        "Alerta temeroso e angustiado de Aurica diante da instabilidade mortal da plataforma ('あんな危ないところに...')."
    ),
    8867: (
        "Mas é o único jeito.",
        "Determinação concisa e corajosa de Lyner ('けど、行くしかない')."
    ),
    8868: (
        "...Vou avançar pelas colunas.\nEsperem por mim aqui.",
        "Correção fiel ao japonês ('柱伝いに行く' - avançar pelas colunas), superando a generalização frouxa do inglês ('go to the other side')."
    ),
    8869: (
        "...Lyner!!",
        "Grito desesperado de Aurica vendo-o partir para o abismo ('...ライナー!!')."
    ),
    8870: (
        "Vai dar tudo certo!\nNão se preocupe...",
        "Palavras de consolo de Lyner tentando acalmar Aurica no meio do perigo ('大丈夫だ! 心配するな...')."
    ),
    8871: (
        "Lyner!!!",
        "Clímax de aflição na voz de Aurica ao ver o desmoronamento ('ライナー!!!')."
    ),
    8872: (
        "Droga! O cristal...!!",
        "Grito de Lyner reagindo à perda do apoio do cristal ('やばい!クリスタルが!!')."
    ),
    8873: (
        "Pessoal!\nA coisa desandou de vez! Fujam daqui, rápido!!",
        "Grito de emergência de Lyner alertando o grupo com naturalidade e urgência ('みんな! さすがにやばくなってきた!もう逃げてくれ!!')."
    ),
    8874: (
        "...Podem ir! Eu não vou morrer\nnum buraco desses!",
        "Fibra heroica e teimosia protetora de Lyner ('...大丈夫、俺はこんなところでくたばったりしない')."
    ),
    8875: (
        "...Lyner.",
        "Tensão de Radolf vendo a gravidade da situação ('...ライナー')."
    ),
    8876: (
        "Deu ruim!\nSe continuarmos aqui, este nosso lado vai desabar antes...",
        "Pragmatismo técnico e incisivo de Krusche avaliando o colapso estrutural ('まずい。このままだと、こっちの方が先に落ちるかも...')."
    ),
    8877: (
        "...Lyner!",
        "Apelo dilacerado de Aurica recusando-se a abandonar o cavaleiro ('...ライナー!')."
    ),
    8878: (
        "Droga!! Não temos saída...\nRecuar agora mesmo!",
        "Ordem militar peremptória de Radolf sob risco de morte ('まずい!! ...仕方ない、一時撤退だ!'), restituindo o comando tático de '一時撤退'."
    ),
    8879: (
        "...Não! Eu me recuso!",
        "Recusa veemente e comovente de Aurica ('...イヤです'), eliminando o 'Não quero saber' apático do rascunho anterior."
    ),
    8880: (
        "Aurica!\nO chão onde nós estamos pode despencar antes do dele, sabia?!",
        "Alerta enérgico de Radolf tentando fazê-la cair em si ('オリカ! こっちの方が先に落ちるかもしれないんだぞ!?')."
    ),
    8881: (
        "......",
        "Silêncio resoluto de Aurica tomando uma decisão transcendental ('...')."
    ),
    8882: (
        "...#0Vasiyat gegis exeks suant, Lyner##...",
        "Preservação rigorosa do cântico Hymmnos quebrado pelo pavor emocional e paridade estrita de controles (#0...##)."
    ),
    8883: (
        "Aurica?! ...Você tá bem?!",
        "Espanto e preocupação imediata de Krusche ('オリカ!?...大丈夫?')."
    ),
    8884: (
        "Esperem!... O que é isso...?\nEla está tecendo uma Canção?!",
        "Percepção militar e espiritual de Radolf testemunhando o milagre sonoro ('待て!...これは... 詩を紡いでいる!?')."
    ),
    8885: (
        "...#0Vasiyat gegis exeks suant, Lyner##...",
        "Preservação estrita do verso Hymmnos entoado com fervor crescente ('#0...##')."
    ),
    8886: (
        "...#0Vasiyat gegis exeks suant, Lyner##...",
        "Preservação estrita do verso Hymmnos sagrado ('#0...##')."
    ),
    8887: (
        "Não me diga que... Mas como?!",
        "Incredulidade e assombro teológico de Radolf diante da luz do cântico ('これは...まさか!?')."
    ),
    8888: (
        "...#0Vasiyat gegis exeks suant, Lyner##...",
        "Preservação estrita do clímax do cântico Hymmnos ('#0...##')."
    ),
    8889: (
        "...A Magia Azul!!?",
        "Identificação atônita da milagrosa Magia Azul por Radolf ('...青魔法!!?')."
    ),
    8890: (
        "Não pode ser... A Aurica teceu uma Magia Azul... em prol do Lyner?!",
        "Restauração do espanto teológico de Radolf ('まさか...オリカがライナーのために...青魔法を紡いだというのか!?'), superando o clichê 'It's incredible'."
    ),
    8891: (
        "E não dentro da Cosmosfera,\nmas no mundo real...?! É inacreditável!",
        "Assombro de Radolf com a quebra das leis da ressonância mágica ('それもコスモスフィアではなく、現実世界で!? あり得ん!')."
    ),
    8892: (
        "Depressa!! Vamos sair daqui!",
        "Grito urgente de fuga de Radolf ('いかん!!行くぞ!'), corrigindo a calmaria artificial do inglês ('Okay! Let's go!')."
    ),
    8893: (
        "A Magia Azul [Thunder Guard] foi tecida!",
        "Mensagem de sistema com paridade estrita de colchetes com o termo original em inglês [Thunder Guard], remoção de aspas redundantes e emprego do verbo sagrado 'tecer' ('青魔法『サンダーガード』を紡いだ!')."
    ),
    8894: (
        ".........",
        "Silêncio exausto e atordoado de Aurica após o despertar do poder ('.........')."
    ),
    8895: (
        "Aurica... aquela Magia da Canção de agora há pouco...\nO que foi aquilo exatamente...?",
        "Pergunta reverente e atônita de Radolf após o perigo ('オリカ...さっきの詩魔法... あれは一体...')."
    ),
    8896: (
        "Nem eu sei... De repente, aquilo brotou com força de dentro do meu peito...\ne, quando me dei conta, eu já estava cantando...",
        "Relato lírico e comovente de Aurica sobre o impulso incontrolável de sua alma ('わからない...。急に身体の中から沸き出してきて... いつの間にか謳ってた...')."
    ),
    8897: (
        "Aquilo pertence à linhagem da Magia Azul.\nÉ um milagre que só se tece quando você anseia, do fundo da alma,\nproteger quem mais ama neste mundo.",
        "Tradução monumental e poética do cerne da Magia Azul ('あれは青魔法の類だ。大切な人を心の底から護りたいと思わなければ紡げない')."
    ),
    8898: (
        "Quanto mais sem estar na Cosmosfera,\nmas tecida por conta própria, em pleno mundo real...",
        "Reforço do prodígio de tecer a canção fora do mundo mental ('ましてやコスモスフィアではなく、現実世界で一人で紡いだんだ...')."
    ),
    8899: (
        "...Eu... nunca tinha sentido algo assim antes.",
        "Aurica reconhecendo a novidade do sentimento de amor e devoção que floresceu nela ('...あたし、こんな気持ちになったの初めて')."
    ),
    8900: (
        "Que nostalgia...\nIsso me traz lembranças da época em que eu servia ativamente como sacerdote.",
        "Radolf relembrando seus dias na ativa na Igreja ('昔俺がまだ現役の神官だった頃の事を思い出すよ')."
    ),
    8901: (
        "Naqueles tempos, eu também tinha uma parceira Reyvateil.\nE ela também, uma única vez, teceu uma Canção no mundo real para me salvar.",
        "Confidência comovente de Radolf sobre seu passado sagrado com sua antiga parceira ('当時は俺にも相方がいてな。あの子も一度だけ、俺のために現実世界で詩を紡いだ')."
    ),
    8902: (
        "...Hã?",
        "Reação delicada e surpresa de Aurica ('...え?')."
    ),
    8903: (
        "Todo esse sentimento sincero que você nutre pelo Lyner\ndeve ter alcançado a alma dele.",
        "Afirmação paternal e sábia de Radolf sobre a ressonância entre Aurica e Lyner ('オリカのライナーを想う気持ちが伝わったんだろうな')."
    ),
    8904: (
        "S-será mesmo...? Seria isso...?",
        "Hesitação encabulada e ruborizada de Aurica compreendendo o peso do que sente ('そ、そうなんでしょうか...')."
    ),
    8905: (
        "Com certeza.\nA Magia da Canção é exatamente isso.",
        "Afirmação serena e definitiva de Radolf sobre o poder do coração na Magia da Canção ('ああ。詩魔法ってのはそういうモンだ')."
    ),
    8906: (
        "Pela Aurica de antigamente,\neu jamais conseguiria imaginar uma coisa dessas.",
        "Constatação afetuosa do crescimento emocional de Aurica após o trauma ('昔のオリカからは想像できないよ')."
    ),
    8907: (
        "......",
        "Silêncio contemplativo de Aurica assimilando as palavras ('...')."
    ),
    8908: (
        "...!!",
        "Sobressalto de vergonha intensa e pudor quando a realidade do sentimento cai sobre ela ('...!!')."
    ),
    8909: (
        "E-eu...\nVou dar uma volta por aí agora mesmo!",
        "Fuga apressada e tímida de Aurica tentando disfarçar o rosto vermelho ('あたし... ちょっとその辺見てきます!')."
    ),
    8910: (
        "Ei, Aurica?!",
        "Reação surpresa de Krusche vendo a garota sair correndo ('あ、オリカ!?')."
    ),
    8911: (
        "Mesmo no mundo real, uma Reyvateil é capaz de tecer uma Canção\nquando o coração dela é profundamente abalado.",
        "Explicação psicológica de Radolf sobre o abalo emocional das Reyvateils ('レーヴァテイルは現実世界でも、心が相当揺さぶられれば詩を紡ぐ')."
    ),
    8912: (
        "Para a Aurica, o simples pesadelo de perder o Lyner\ndeve ter sido uma dor quase insuportável...",
        "Compreensão compassiva da agonia interior de Aurica ('オリカにとって、ライナーを失うことは相当な痛みだったのかもしれないな...')."
    ),
    8913: (
        "...Aquela menina nunca tinha escancarado\no que sentia para ninguém até hoje.",
        "Observação comovida sobre o isolamento afetivo anterior de Aurica ('...あの子は今まで感情を露わにしたことがなかった')."
    ),
    8914: (
        "É a primeira vez que a vejo demonstrar uma emoção tão pura.",
        "Celebração sóbria da libertação afetiva de Aurica ('初めてだよ。あんなに感情を露わにしたのは')."
    ),
    8915: (
        "Será que o Lyner tá bem...?",
        "Preocupação genuína e afetuosa de Krusche sob o verniz durão ('ライナー、大丈夫かな...')."
    ),
    8916: (
        "Logo com ele, duvido que tenha acontecido o pior, mas...",
        "Confiança e preocupação velada de Radolf ('あいつに限って万が一のことはないと思うが...')."
    ),
    8917: (
        "Mas aquela situação toda era desesperadora.",
        "Avaliação crua e realista de Krusche sobre o colapso ('でもあの状況は絶望的')."
    ),
    8918: (
        "De fato...",
        "Concordância solene e preocupada de Radolf ('確かに...')."
    ),
    8919: (
        ".........",
        "Pausa angustiada compartilhada por Krusche diante do abismo ('.........')."
    ),
    8920: (
        ".........",
        "Silêncio pesado de Radolf meditando sobre o destino de Lyner ('.........')."
    ),
    8921: (
        "Pensando bem...\naté onde será que a Aurica foi parar?",
        "Quebra de silêncio de Radolf voltando a atenção para o paradeiro de Aurica ('そういえば...オリカはどこまで行ったんだ?')."
    ),
    8922: (
        "...Melhor a gente ir atrás dela.",
        "Decisão prática e rápida de Krusche para reencontrar Aurica ('...探しに行こう')."
    ),
    8923: (
        "Francamente... esse moleque...\nO que ele tinha na cabeça, me diz...?",
        "Dicção resmungona e afetuosa de veterano Teru de Jack diante de Lyner desmaiado ('全く...こいつは...。何をやってるんだかねぇ...')."
    ),
    8924: (
        "Se eu não tivesse achado você aqui,\ncomo é que ia ser, hein...?",
        "Cobrança fraternal e alívio cínico de Jack ('俺が見つけなかったらどうしてたんだか...')."
    ),
    8925: (
        "Onde... onde estou...?",
        "Despertar confuso e desorientado de Lyner recobrando a consciência ('ここは...')."
    )
}

def main():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    dialogues = input_data.get("dialogues", [])
    print(f"Total de diálogos de entrada: {len(dialogues)}")

    curated_lines = []
    lines_rewritten = 0
    lines_approved_as_is = 0

    for d in dialogues:
        d_id = d["id"]
        orig_en = d.get("original_en", "")
        orig_jp = d.get("original_jp", "")
        current_pt = d.get("current_ptbr", "")

        if d_id in CURATED_DATA:
            text_ptbr, justificativa = CURATED_DATA[d_id]
        else:
            print(f"AVISO: ID {d_id} não mapeado!")
            text_ptbr = current_pt
            justificativa = "Mantida a tradução base sem alterações."

        if text_ptbr.strip() != current_pt.strip():
            lines_rewritten += 1
        else:
            lines_approved_as_is += 1

        curated_lines.append({
            "id": d_id,
            "text_ptbr": text_ptbr,
            "curated_ptbr": text_ptbr,
            "original_en": orig_en,
            "original_jp": orig_jp,
            "justificativa": justificativa
        })

    output_json = {
        "block_id": "BLK_EVD_036",
        "axis_id": "AXIS_3",
        "axis_name": "3_HISTORIA_E_EVENTOS",
        "total_lines": len(curated_lines),
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "highlights": [
            {
                "id": 8818,
                "speaker": "Misha",
                "jp": "おじさん、ダイブしたいの。お願い。",
                "before": "Senhor, queremos mergulhar. Você pode nos ajudar?",
                "after": "Moço, a gente quer mergulhar. Dá essa força pra gente?",
                "rationale": "Restauração da dicção atirada, desinibida e cativante de Misha ao se dirigir ao terapeuta da Loja de Mergulho ('おじさん、ダイブしたいの。お願い')."
            },
            {
                "id": 8823,
                "speaker": "Personagem [87]",
                "jp": "コスモスフィアには、彼女が今まで経験してきたことやCR妄想なんかがいっぱいある。",
                "before": "A Cosmosfera é preenchida por suas emoções e experiências passadas.",
                "after": "A Cosmosfera está repleta de tudo o que ela já viveu...\ne de um monte de fantasias da cabeça dela.",
                "rationale": "Restauração do termo crucial 'fantasias / devaneios' ('妄想') da psique das Reyvateils, que havia sido higienizado para o insosso 'emotions' no inglês."
            },
            {
                "id": 8850,
                "speaker": "Sistema / Caixa Narrativa / Tutorial",
                "jp": "DPはレーヴァテイルとの信頼度でもあります。",
                "before": "O DP também representa o quanto uma Reyvateil depende de você.",
                "after": "Os DP também representam o nível de confiança mútua entre você e a Reyvateil.",
                "rationale": "Correção de erro crasso de tradução do inglês ('depends on you'), restituindo o sentido canônico de confiança mútua ('信頼度')."
            },
            {
                "id": 8868,
                "speaker": "Lyner",
                "jp": "...柱伝いに行く。みんなはCRここで待っていてくれ。",
                "before": "Vou tentar ir pro outro lado. Esperem por mim aqui.",
                "after": "...Vou avançar pelas colunas.\nEsperem por mim aqui.",
                "rationale": "Fidelidade à ação física espacial descrita no original japonês ('柱伝いに行く' - avançar pelas colunas), superando o vago 'go to the other side' americano."
            },
            {
                "id": 8879,
                "speaker": "Aurica",
                "jp": "...イヤです。",
                "before": "...Não quero saber.",
                "after": "...Não! Eu me recuso!",
                "rationale": "Eliminação da tradução insensível e fria 'Não quero saber', restituindo a recusa desesperada e comovente de Aurica diante da ordem de abandono ('...イヤです')."
            },
            {
                "id": 8890,
                "speaker": "Radolf",
                "jp": "まさか...オリカがライナーのために...青魔法を紡いだというのか!?",
                "before": "É incrível... A Aurica criou a Magia Azul para o Lyner...",
                "after": "Não pode ser... A Aurica teceu uma Magia Azul... em prol do Lyner?!",
                "rationale": "Restituição do choque teológico e militar de Radolf ('まさか...紡いだというのか!?'), superando o clichê domesticado 'It's incredible'."
            },
            {
                "id": 8897,
                "speaker": "Radolf",
                "jp": "あれは青魔法の類だ。CR大切な人を心の底から護りCRたいと思わなければ紡げない。",
                "before": "Aquilo era a Magia Azul. Só dá para criá-la quando você quer desesperadamente proteger alguém.",
                "after": "Aquilo pertence à linhagem da Magia Azul.\nÉ um milagre que só se tece quando você anseia, do fundo da alma,\nproteger quem mais ama neste mundo.",
                "rationale": "Lapidação poética monumental do dogma e filosofia da Magia Azul ('大切な人を心の底から護りたいと思わなければ紡げない')."
            }
        ],
        "character_dynamic_evolution": {
            "Aurica": {
                "Lyner": "Despertar do amor incondicional no mundo real: superação da timidez e trauma para entoar a Magia Azul [Thunder Guard] a fim de salvar seu protetor da morte certa.",
                "Radolf": "Pudor e timidez avassaladora ao ser confrontada com o significado sagrado da Magia Azul, fugindo vermelha de vergonha."
            },
            "Radolf": {
                "Aurica / Lyner": "Testemunha solene e sábia do milagre da Magia Azul, compartilhando suas memórias nostálgicas de seus dias como sacerdote da Igreja de Elemia.",
                "Krusche": "Companheirismo e preocupação estóica mútua diante da gravidade do colapso da plataforma e desaparecimento de Lyner."
            },
            "Misha": {
                "Lyner": "Entrega afetuosa e cumplicidade na Loja de Mergulho ('Estou em suas mãos!'), reafirmando a intimidade inquebrantável entre amigos de infância."
            },
            "Jack": {
                "Lyner": "Cuidado fraternal e resmungão de veterano Teru ao resgatar o jovem cavaleiro desmaiado nos confins do abismo."
            }
        },
        "scene_handoff": {
            "resumo_dramatico": "O bloco BLK_EVD_036 consolida dois marcos narrativos e emocionais de transcendência absoluta na saga de Ar tonelico: primeiro, na Loja de Mergulho, o terapeuta e Misha detalham as engrenagens psicológicas da Cosmosfera — o processo íntimo de converter fantasias e lembranças em Magia da Canção através do vínculo incondicional entre a Reyvateil e seu parceiro; em seguida, no terrível desabamento da plataforma, Lyner se arrisca para recuperar o cristal e o grupo fica à beira do abismo. Diante da ordem de recuo de Radolf, Aurica quebra seu silêncio dócil em uma recusa dilacerante e, movida pelo desejo ardente e desesperado de salvar Lyner, entoa no mundo real o cântico sagrado que desperta a lendária Magia Azul [Thunder Guard]. Radolf testemunha o milagre atônito, revelando a filosofia sagrada das Reyvateils e suas próprias memórias de quando servia como sacerdote. Ao se dar conta de que seus sentimentos mais íntimos foram expostos, Aurica foge ruborizada de vergonha, enquanto Krusche e Radolf temem pelo destino de Lyner — que desperta resgatado pelo olhar calejado e resmungão de Jack.",
            "decisoes_terminologicas": {
                "Magia Azul": "青魔法 (Blue Magic, modalidade sagrada de canção protetora tecida por amor incondicional)",
                "Loja de Mergulho": "ダイブ屋 (Dive Shop, estabelecimento onde terapeutas operam a máquina de mergulho mental)",
                "Mundo Mental / Cosmosfera": "精神世界 / コスモスフィア (padronização canônica, eliminando o decalque 'Espaço da Alma')",
                "Guardião Mental": "心の護 / [Mind Guardian] (entidade protetora da psique da Reyvateil)",
                "DP / Pontos de Mergulho": "DP / ダイブポイント (recurso de ressonância e confiança mútua)",
                "Tecer Canções": "詩を紡ぐ (verbo canônico da criação de Magias da Canção)",
                "Thunder Guard": "サンダーガード / [Thunder Guard] (Magia Azul protetora despertada por Aurica)"
            },
            "alertas_para_proximo_bloco": "Lyner recobrou a consciência aos cuidados de Jack nos escombros. Resta saber o paradeiro exato de Aurica, que fugiu desconcertada pela revelação de seus sentimentos, e a reunião do grupo para planejar os próximos passos com a recém-despertada Magia Azul e os mistérios da conspiração política na Torre."
        },
        "curated_lines": curated_lines
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_json, f, ensure_ascii=False, indent=2)

    print(f"[SUCESSO] Arquivo gerado em {OUTPUT_PATH}")
    print(f"Linhas reescritas: {lines_rewritten}/{len(curated_lines)}")
    print(f"Linhas mantidas: {lines_approved_as_is}/{len(curated_lines)}")

if __name__ == "__main__":
    main()

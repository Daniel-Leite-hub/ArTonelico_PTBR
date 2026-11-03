# -*- coding: utf-8 -*-
"""
Script de Curadoria Editorial e LQA para BLK_EVD_055
IDs: 12916 a 13105 (190 linhas)
Eventos:
  - Event/170.evd (12916-12973): Tastiella, Batismo de Circula, confronto entre Lyner e o grupo sobre seguir sozinho.
  - Event/191.evd (12974-13050): Cosmosfera de Aurica, devastação do vírus, Aurica cristalizada, intervenção de Shurelia.
  - Event/606.evd (13051-13105): Cosmosfera de Misha, dilema existencial, Krusche vs. liberdade de Misha, remédio do Yakuan.
"""

import sys
import json
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_055_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_055_output.json"
report_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_055_report.json"
master_glossary_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Dicionário de curadoria id -> (texto_curado, notas)
CURATED = {}

# =========================================================================
# EVENT/170.evd (12916 - 12973) - 58 linhas
# =========================================================================
CURATED[12916] = (
    "Vocês demoraram.\nJá prepararam bem o coração para o ritual?",
    "Tastiella (ID 19) recebe o grupo para o Batismo de Circula. '心の準備は十分にしてきたかしら?' -> preparação do coração/espírito."
)
CURATED[12917] = (
    "...Com certeza.",
    "Lyner responde com firmeza inicial."
)
CURATED[12918] = (
    "......",
    "Hesitação de Lyner ao refletir sobre o peso do ritual."
)
CURATED[12919] = (
    "...?",
    "Radolf nota o silêncio atípico de Lyner."
)
CURATED[12920] = (
    "...O que foi?",
    "Misha percebe a inquietação do amigo de infância."
)
CURATED[12921] = (
    "Eu andei pensando muito e...\nDaqui em diante, acho melhor eu seguir sozinho.",
    "Lyner tenta assumir o fardo da missão solitária ('ここから先は俺一人で行くよ')."
)
CURATED[12922] = (
    "...Lyner?! Por que isso agora?!",
    "Aurica chocada com a declaração repentina ('...ライナー!?どうして?')."
)
CURATED[12923] = (
    "O-o que você tá dizendo, moleque?!",
    "Jack indignado ('な、何いってんだよ!'). Correção do decalque da NISA ('are you outta your mind?')."
)
CURATED[12924] = (
    "O [Batismo de Circula] é um ritual\nem que a gente passa por algo parecido com a morte, não é?",
    "Lyner relembra o perigo do Batismo de Circula ('一度死んだりするような儀式'). NISA distorceu para 'requires you to die'."
)
CURATED[12925] = (
    "...Eu falei aquilo apenas como força de expressão.\nNão é nada perigoso.",
    "Tastiella tranquiliza o grupo ('ものの例えでそう言っただけよ')."
)
CURATED[12926] = (
    "Além disso, se subirmos, não tem como voltar.\nEu não posso arrastar vocês para um lugar assim!",
    "Lyner expõe o dilema da viagem sem volta à parte superior da Torre ('上に行ったら帰って来れないんだ')."
)
CURATED[12927] = (
    "Lyner... que decepção.\nA esta altura dos acontecimentos, você ainda me vem\ncom esse tipo de conversa...",
    "Radolf expressa decepção madura diante do retrocesso emocional de Lyner ('この期に及んでまだそんなことを言うとはな...')."
)
CURATED[12928] = (
    "Quer dizer que, no seu coração,\nnós ainda somos um bando indigno de confiança.",
    "Radolf confronta a falta de fé mútua ('未だにライナーの中では、俺たちは信頼に値しない連中なわけだ')."
)
CURATED[12929] = (
    "Não é isso!... Eu só pensei que não devia\nsobrecarregar vocês com tantos problemas...",
    "Lyner na defensiva ('みんなにそこまで迷惑を掛けるわけにはいかないと思って...')."
)
CURATED[12930] = (
    "...E você acha mesmo que agir assim não é nos causar problemas?\nTá de brincadeira com a nossa cara...",
    "Jack furioso com a atitude superprotetora ('なめられたモンだぜ...')."
)
CURATED[12931] = (
    "Quem foi que disse que isso é um estorvo?!",
    "Misha reage indignada ('誰が迷惑だって言った?')."
)
CURATED[12932] = (
    "B-bem, isso...",
    "Lyner sem resposta ('そ、それは...')."
)
CURATED[12933] = (
    "Você não percebe?!\nTá todo mundo decepcionado com você!...",
    "Misha repreende a cegueira afetiva de Lyner ('みんながっかりしてるのよ...'). Correção do erro da NISA ('pissing everybody off')."
)
CURATED[12934] = (
    "É só você, Lyner, que fica\ncom essa preocupação sem cabimento!",
    "Misha rebate ('ライナーだけよ、そんな意味のない心配してるの')."
)
CURATED[12935] = (
    "Mas eu me preocupo com vocês, caramba!\nNão existe garantia nenhuma de que todos vão sair ilesos!",
    "Lyner explode de frustração e cuidado protetor ('とにかく俺は心配なんだよ!')."
)
CURATED[12936] = (
    "Lyner... você acha mesmo\nque tá dizendo isso por consideração aos outros?",
    "Misha questiona o altruísmo tóxico de Lyner ('相手のことを思いやって言ってる言葉だと思う?'). Correção do texto inventado da NISA."
)
CURATED[12937] = (
    "O que você tá fazendo agora\né só empurrar a sua própria vontade goela abaixo!",
    "Misha aponta a imposição unilateral ('自分の想いを相手に押しつけてるだけよ!')."
)
CURATED[12938] = (
    "Por que você não consegue\nperceber o que todo mundo sente?!",
    "Misha exige empatia real ('どうしてみんなの想いを感じ取ってくれないの!?'). Correção de 'read between the lines' da NISA."
)
CURATED[12939] = (
    "Ninguém aqui quer dar adeus a você!",
    "Misha expressa a lealdade incondicional do grupo ('誰も、ライナーとサヨナラなんて考えてない!')."
)
CURATED[12940] = (
    "Todo mundo quer acompanhar você, Lyner!\nNão importa até onde seja!",
    "Misha afirma o pacto de companheirismo ('みんなライナーに着いていくつもりなのよ。どこまでだって!')."
)
CURATED[12941] = (
    "E mesmo assim, você tá pisoteando\no que a gente sente... Como aconteceu naquela vez...",
    "Misha lembra da ferida não cicatrizada do Mergulho ('その気持ちを踏みにじってるの...。あの時だって...')."
)
CURATED[12942] = (
    "Por que você nunca me diz:\n\"Vamos mergulhar juntos\"?!",
    "Misha expõe a mágoa sincera ('どうしてライナーは『ダイブしよう』って言ってくれないの!?')."
)
CURATED[12943] = (
    "E... hããã?!",
    "Lyner pego de surpresa com o desabafo pessoal ('え...ええっ!?')."
)
CURATED[12944] = (
    "...Não, é que... eu achei\nque você fosse detestar a ideia...",
    "Lyner confessa sua insegurança ('嫌がるかな...って思って...')."
)
CURATED[12945] = (
    "Eu nunca detestaria!...\nEu já não te falei isso agorinha mesmo?!",
    "Misha reafirma seu desejo de intimidade e conexão ('そんなことない!...さっきもそう言ったじゃない!')."
)
CURATED[12946] = (
    "...Hum, mas ainda assim...\neu fico meio sem jeito...",
    "Lyner admite seu constrangimento ('やっぱりちょっと気がひけるな...'). Restauração da frase cortada pela NISA."
)
CURATED[12947] = (
    "Chega!... Lyner!",
    "Misha impaciente com a teimosia dele ('もういい!...ライナー!')."
)
CURATED[12948] = (
    "Eu fiquei tão triste naquela hora...\nEu queria muito que você mergulhasse comigo, Lyner.",
    "Misha revela a vulnerabilidade ('私、ライナーにダイブして欲しかったもの')."
)
CURATED[12949] = (
    "Foram só as suas próprias ideias que decidiram,\npor conta própria, rejeitar o Mergulho comigo...",
    "Misha explica o julgamento precipitado de Lyner ('ライナーの価値観が勝手に私とのダイブを拒んでいただけで...')."
)
CURATED[12950] = (
    "......",
    "Lyner reflete em silêncio, absorvendo a lição."
)
CURATED[12951] = (
    "Pensar de verdade no outro, moleque,\nnão é só ficar se preocupando de forma unilateral.",
    "Jack ensina a verdadeira maturidade afetiva ('一方的に心配するだけじゃダメなんだぜ')."
)
CURATED[12952] = (
    "Até mesmo essa pessoa tem uma ou duas coisas\nque preza muito mais do que a própria vida.",
    "Jack elucida a dignidade de quem luta pelo que ama ('自分の命より大切なものくらい、1つや2つはあるモンさ')."
)
CURATED[12953] = (
    "...Tente enxergar isso, entendeu?",
    "Jack conclui o conselho fraterno ('...それを感じ取ってくれや。な')."
)
CURATED[12954] = (
    "Eu entendi... Quer dizer, na verdade\na ficha ainda não caiu por completo, mas...",
    "Lyner sincero sobre sua digestão emocional ('実はまだしっくり来てはいないけど...')."
)
CURATED[12955] = (
    "Mas o que vocês sentem por mim,\ndisso eu não tenho mais dúvida nenhuma.",
    "Lyner acolhe a determinação dos companheiros ('でも、みんなの想いは良くわかったよ')."
)
CURATED[12956] = (
    "Então, vamos juntos... rumo a Platina!",
    "Lyner retoma a liderança com espírito renovado ('それじゃ、一緒に行こうか...プラティナへ!')."
)
CURATED[12957] = (
    "...Sim!",
    "Misha responde aliviada e feliz ('...うん')."
)
CURATED[12958] = (
    "O coração de vocês está preparado?",
    "Tastiella inicia a invocação sagrada ('心の準備はいいかしら')."
)
CURATED[12959] = (
    "#0Ma nam ra flip 0x1011001101##\n#0yor enter ARTONELICO.",
    "Código de comando sagrado em Hymmnos entoado por Tastiella. Preservação estrita dos tokens de sistema (estava vazio no input preliminar)."
)
CURATED[12960] = (
    "Aquela luz é o portal.\nAo passarem por ela... sairão diretamente no topo da Torre.",
    "Tastiella orienta a transição de fase ('その光がゲート。そこをくぐれば...次にでてくるときは塔の上側よ')."
)
CURATED[12961] = (
    "Tastiella... obrigado por tudo o que fez por nós.",
    "Lyner despede-se com gratidão da guardiã secular ('タスティエーラ...色々世話になったな。ありがとう')."
)
CURATED[12962] = (
    "...Estarei orando para que Platina fique a salvo.",
    "Tastiella despede-se com prece solene ('...プラティナが無事であることを祈っているわ')."
)
CURATED[12963] = (
    "Obrigado. ...Até logo.",
    "Lyner despede-se ('ああ。...それじゃ')."
)
CURATED[12964] = (
    "Velhota...\nA Misha voltou, mas...",
    "Jack fala a sós com Tastiella após a passagem dos jovens ('オババ様。ミシャは帰ってきましたが...')."
)
CURATED[12965] = (
    "Pelo visto, ela acabou deixando o seu Hino esquecido em algum lugar.",
    "Tastiella constata a perda da Magia de Hino de Misha ('どうやら『詩』を、どこかに忘れてきてしまったみたいね')."
)
CURATED[12966] = (
    "...O hino da Misha...\neu juro que vou recuperar para ela.",
    "Jack assume a responsabilidade moral de resgatar o hino ('ミシャの詩は必ず、俺が取り戻してきます')."
)
CURATED[12967] = (
    "Estou contando com você.\nAfinal de contas, você foi um dos culpados por isso.",
    "Tastiella lembra da culpa pretérita de Jack na fuga da infância ('元はと言えば、貴方も原因の1つなんだから')."
)
CURATED[12968] = (
    "Pegou pesado como sempre...\nOuvir isso me machuca lá no fundo do peito.",
    "Jack reage com bom humor ferido ('相変わらずキッツイな...。それを言われるととても心が痛みますよ')."
)
CURATED[12969] = (
    "Era brincadeira.\nMas ande logo, antes que seja tarde demais.",
    "Tastiella adverte sobre a urgência temporal ('冗談よ。でも、早くしないと取り返しのつかないことになるわ')."
)
CURATED[12970] = (
    "...Eu sei.\nAssim que resolvermos as coisas lá em cima, vou procurar na mesma hora.",
    "Jack sela o compromisso de buscar o hino ('今回の件が片付いたら、すぐにでも探します')."
)
CURATED[12971] = (
    "Até mais.",
    "Jack despede-se com brevidade respeitosa ('では')."
)
CURATED[12972] = (
    "...Depressa.\nJack, Misha...",
    "Tastiella murmura em prece silenciosa ('...急いで。ジャック、ミシャ...')."
)
CURATED[12973] = (
    "Entendo... Avise-me quando estiverem prontos.",
    "Linha de retorno de diálogo de sistema caso o jogador interaja antes do salto ('そう...。それじゃ準備が出来たら教えて')."
)

# =========================================================================
# EVENT/191.evd (12974 - 13050) - 77 linhas
# =========================================================================
CURATED[12974] = (
    "Que horror...",
    "Lyner depara-se com o Nível da Cosmosfera devastado ('ひどい...')."
)
CURATED[12975] = (
    "O estrago aqui foi feio demais...",
    "Jack constata a ruína do cenário ('随分な状態じゃねぇか')."
)
CURATED[12976] = (
    "...Pobrezinha da Aurica.\nSe fosse comigo, eu não conseguiria suportar...",
    "Misha penalizada com o trauma refletido no mundo mental de Aurica ('オリカ、かわいそう。私だったら耐えられないよ...')."
)
CURATED[12977] = (
    "De qualquer forma, vamos seguir este rastro\nde destruição e encontrar os vírus!",
    "Lyner foca na perseguição aos vírus ('傷跡をたどってウイルスを探そう!'). Correção do decalque da NISA."
)
CURATED[12978] = (
    "O coração da Aurica...\nreduzido a terra devastada até onde a vista alcança...",
    "Radolf estarrecido com a extensão do dano ('オリカの心の中が...地の果てまで荒野に...')."
)
CURATED[12979] = (
    "Esse é o poder... dos vírus...",
    "Misha assustada com a força destrutiva ('これがウイルスの力...なの...')."
)
CURATED[12980] = (
    "Lyner!!\nAconteceu uma tragédia daquelas!...",
    "Don Leon (Donsuke) chega esbaforido em pânico ('ライナー!!大変なことになった...')."
)
CURATED[12981] = (
    "Don Leon!\n...A Aurica... O que aconteceu com a Aurica?!",
    "Lyner aflito pelo destino de Aurica ('オリカはどうした!?')."
)
CURATED[12982] = (
    "Eu pensei que um meteorito tivesse caído do céu,\nmas na verdade era um monstro medonho!...",
    "Don Leon descreve a invasão do vírus na Cosmosfera ('突然隕石が落ちてきたかと思ったら、バケモノだった...')."
)
CURATED[12983] = (
    "A senhorita Aurica foi cristalizada por aquele monstro...\ne ficou presa lá dentro!",
    "Don Leon relata o aprisionamento de Aurica em cristal ('水晶にされて...閉じこめられちまったんだ!')."
)
CURATED[12984] = (
    "O quê?!",
    "Lyner chocado ('なんだって!?')."
)
CURATED[12985] = (
    "Por aqui!!",
    "Don Leon guia o grupo ('こっちだ!!')."
)
CURATED[12986] = (
    "Dá para ver alguma coisa logo adiante!...",
    "Krusche avista a estrutura ao longe ('向こうに何か見える...!')."
)
CURATED[12987] = (
    "Aquilo ali é...",
    "Lyner reconhece a silhueta ('あれは...')."
)
CURATED[12988] = (
    "Aurica!!",
    "Lyner corre ao encontro ('オリカ!!')."
)
CURATED[12989] = (
    "......",
    "Aurica catatônica selada no cristal ('...')."
)
CURATED[12990] = (
    "Aurica! Você tá bem?!",
    "Lyner desesperado para reanimá-la ('オリカ!大丈夫か!?')."
)
CURATED[12991] = (
    "CRIATURAS TOLAS...\nHUMANOS INSENSATOS QUE FEREM AS REYVATEILS...",
    "Voz robótica e ameaçadora do vírus possuindo Aurica em katakana ('オロカナルモノヨ...レーヴァテイルヲキズツケル オロカナ ニンゲンヨ...')."
)
CURATED[12992] = (
    "O... do que você tá falando?!\nEu vim aqui para salvar a Aurica...",
    "Lyner atônito diante das palavras hostis ('な...何言ってるんだよ!俺はオリカを助けに...')."
)
CURATED[12993] = (
    "HUMANOS NÃO TÊM COMO SALVAR\nAS REYVATEILS...",
    "Vírus repete o dogma alienante através do corpo de Aurica ('ニンゲン ニ レーヴァテイル ハタスケラレナイ...')."
)
CURATED[12994] = (
    "Aurica?!",
    "Lyner perplexo ('オリカ!?')."
)
CURATED[12995] = (
    "Lyner! Essa aí não é a Aurica!\nEla só tá sendo controlada pelos vírus.",
    "Jack alerta o herói para não se deixar enganar ('ライナー!これはオリカじゃねぇ。多分ウイルスに操られているだけだ')."
)
CURATED[12996] = (
    "Miseráveis covardes... que truque desprezível...!!",
    "Radolf indignado com a manipulação vil dos vírus ('どこまでも姑息なまねを...!!')."
)
CURATED[12997] = (
    "O VERDADEIRO VÍRUS SÃO OS HUMANOS...\nNÓS SOMOS OS GUARDIÕES DAS REYVATEILS.",
    "A ideologia antagônica dos vírus revelada em toda sua plenitude filosófica ('ホントノ ウイルス ハ ニンゲン...ワレワレハ レーヴァテイルノ シュゴシャ')."
)
CURATED[12998] = (
    "Guardiões, uma ova...?!",
    "Lyner rebate com desdém indignado ('守護者だって...!?')."
)
CURATED[12999] = (
    "HUMANOS NÃO TÊM COMO SALVAR\nAS REYVATEILS...",
    "Repetição hipnótica do vírus para quebrar o espírito do herói."
)
CURATED[13000] = (
    "......",
    "Lyner respira fundo para contra-atacar ideologicamente."
)
CURATED[13001] = (
    "Mentira!... É verdade que, entre os humanos,\nexistem pessoas horríveis...",
    "Lyner reconhece as falhas da humanidade ('そんなことはない...。確かに人間の中には、ひどいヤツもいるさ...')."
)
CURATED[13002] = (
    "Mas até elas são fichinha\ncomparadas ao que vocês estão fazendo!",
    "Lyner confronta a hipocrisia dos vírus ('だけどな!...そういうヤツだって、お前がやってることに比べたら可愛いものだ')."
)
CURATED[13003] = (
    "Brincar com a vida de tanta gente...\nTripudiar sobre o coração das pessoas...",
    "Lyner denuncia as atrocidades do vírus ('沢山の人の命...沢山の人の心をもてあそびやがって...')."
)
CURATED[13004] = (
    "Eu vou acabar com vocês aqui mesmo!",
    "Determinação combativa inabalável de Lyner ('必ずここでお前を倒す!')."
)
CURATED[13005] = (
    "Lyner... eu... vou ser morta...?",
    "A voz assustada da verdadeira Aurica quebra o transe ('ライナー...アタシコロサレルノ...?')."
)
CURATED[13006] = (
    "!!",
    "Lyner estaca diante do terror de ferir Aurica."
)
CURATED[13007] = (
    "Tô com tanto medo... Eu não quero morrer...",
    "O desespero infantil e puro de Aurica aprisionada ('コワイヨ...シニタクナイ...?')."
)
CURATED[13008] = (
    "Aurica! É você mesma, Aurica?!",
    "Lyner tenta desesperadamente alcançar a mente dela ('オリカ!オリカなのか!?')."
)
CURATED[13009] = (
    "Aguenta firme! Espera aí,\neu vou te salvar agora mesmo!...",
    "Lyner promete proteção imediata ('大丈夫だ!待ってろ、今助けてやるからな...')."
)
CURATED[13010] = (
    "HUMANOS NÃO TÊM COMO SALVAR AS REYVATEILS...",
    "O vírus retoma violentamente o controle."
)
CURATED[13011] = (
    "Não é você, Aurica?!\nÉ o vírus falando...?!",
    "Lyner atordoado pela alternância de personalidades ('オリカじゃないのか!?ウイルスなのか...?')."
)
CURATED[13012] = (
    "Não tô entendendo mais nada!\nAgora seja o que Deus quiser!",
    "Lyner à beira do desespero decide arriscar tudo ('もうわけわからねぇ!こうなりゃヤケクソだ!')."
)
CURATED[13013] = (
    "Não, Lyner!\nVocê vai acabar ferindo a Aurica!",
    "Misha intervém para impedir um golpe fatal precipitado ('ライナー、だめ!オリカを傷つけちゃう!')."
)
CURATED[13014] = (
    "Mas essa coisa não é a Aurica!\nÉ o vírus, não é?!",
    "Lyner tenta justificar o ataque de desespero ('コイツはオリカじゃないんだろ!ウイルスなんだろ!?')."
)
CURATED[13015] = (
    "Pode até ser, mas também\npode ser a verdadeira Aurica ali dentro!",
    "Misha faz o apelo à prudência e compaixão ('そうかもしれないけど...ホンモノのオリカかもしれないのよ!')."
)
CURATED[13016] = (
    "...Droga!\nO que eu faço agora...?!",
    "Lyner paralisado pelo dilema ético ('...ちくしょう。どうすればいいんだ...')."
)
CURATED[13017] = (
    "NÃO CONSEGUEM MOVER UMA PALHA?\nBEM FEITO, HUMANOS...\nFUFUFU.",
    "O vírus tripudia da hesitação dos heróis ('テモ アシモ デナイノ?イイキミネ ニンゲン...フフフ')."
)
CURATED[13018] = (
    "Aurica...",
    "Lyner impotente ('オリカ...')."
)
CURATED[13019] = (
    "...!!",
    "Shurelia detecta a crise no núcleo da Torre e prepara intervenção divina."
)
CURATED[13020] = (
    "Lyner, estou intervindo agora...",
    "Shurelia surge em comunicação de emergência ('ライナー、今行きます...')."
)
CURATED[13021] = (
    "#0Wee i ga flip 0x1011001101 enter ARTONELICO...",
    "Comando místico executado em Hymmnos ancestral por Shurelia. Preservação estrita dos códigos de sistema da deusa."
)
CURATED[13022] = (
    "Guh...",
    "O vírus reage com dor e choque à intervenção cibernética divina ('クッ...')."
)
CURATED[13023] = (
    "...O quê?!",
    "Lyner surpreso ('...なんだ!?')."
)
CURATED[13024] = (
    "Grrr...!!",
    "Rosnado de fúria do monstro viral se manifestando ('グルルル...')."
)
CURATED[13025] = (
    "O vírus?!\n...Quer dizer então que...",
    "Lyner percebe que o vírus foi ejetado da consciência de Aurica ('ウイルス!?...ということは...')."
)
CURATED[13026] = (
    "Senhora Shurelia!!",
    "Lyner reconhece a salvadora divina ('シュレリア様!!')."
)
CURATED[13027] = (
    "Desconectei o vínculo\nentre a Aurica e o vírus.",
    "Shurelia confirma o sucesso do isolamento do parasita ('オリカとウイルスの接続を解除しました')."
)
CURATED[13028] = (
    "Agora... confio o restante a vocês.",
    "Shurelia entrega a batalha final aos Cavaleiros ('後は...よろしくお願いします')."
)
CURATED[13029] = (
    "Senhora Shurelia...\nmuito obrigado!",
    "Lyner grato e revigorado ('シュレリア様...ありがとうございます!')."
)
CURATED[13030] = (
    "Com este golpe...\neu dou um fim definitivo em vocês!!",
    "Grito de guerra triunfal de Lyner ('これで...本当の終わりにしてやる!!')."
)
CURATED[13031] = (
    "...Haa, haa...",
    "Respiração ofegante pós-batalha ('...はぁ、はぁ...'). Transcrição sonora original sem rubricas."
)
CURATED[13032] = (
    "...Acabou...?",
    "Misha conferindo o silêncio da arena ('...おわった...の?')."
)
CURATED[13033] = (
    "Sim...",
    "Lyner confirma com alívio ('ああ...')."
)
CURATED[13034] = (
    "Com isso... os vírus...\ndevem ter sido completamente expurgados...",
    "Lyner certifica a erradicação dos vírus ('これで...ウイルスは...完全に消去したはずだ...')."
)
CURATED[13035] = (
    "Aurica...",
    "Lyner volta-se para a garota libertada ('オリカ...')."
)
CURATED[13036] = (
    "Lyner... eu... fui salva, não fui...?",
    "Aurica acorda serena nos braços dele ('ライナー...あたし...助かったのね...')."
)
CURATED[13037] = (
    "Sim.",
    "Lyner confirma com carinho ('ああ')."
)
CURATED[13038] = (
    "...Que alívio.",
    "Aurica agradecida ('...よかった')."
)
CURATED[13039] = (
    "O mundo...!",
    "Misha contempla a regeneração da Cosmosfera ('世界が!!')."
)
CURATED[13040] = (
    "Está se cobrindo de verde outra vez...",
    "Krusche testemunha a flora renascendo ('緑に包まれていく...')."
)
CURATED[13041] = (
    "Chegou ao fim de verdade.",
    "Radolf solene ('これで本当の終わりだな')."
)
CURATED[13042] = (
    "É... Essa estrada foi longa demais...",
    "Jack desabafa o cansaço da batalha ('ああ...。長かったぜ...')."
)
CURATED[13043] = (
    "Gente... muito obrigada.",
    "Aurica comovida com a dedicação de todos os amigos ('みんな...ありがとう')."
)
CURATED[13044] = (
    "Aurica... Você vai conseguir voltar...\npara o mundo real com a gente, não vai...?",
    "Lyner pergunta com ternura se ela despertará do Mergulho ('現実世界に...帰ってこれるよな...?')."
)
CURATED[13045] = (
    "Com certeza.",
    "Aurica confirma convicta ('もちろんだよ')."
)
CURATED[13046] = (
    "Então, a gente se vê assim que acordar...",
    "Lyner combina o reencontro fora da Cosmosfera ('それじゃ、目が覚めたらまた会おうな...')."
)
CURATED[13047] = (
    "Sim...",
    "Aurica concorda suavemente ('うん...')."
)
CURATED[13048] = (
    "Lyner.",
    "Aurica chama a atenção dele antes de partir ('ライナー')."
)
CURATED[13049] = (
    "...Hum?",
    "Lyner olha surpreso ('...ん?')."
)
CURATED[13050] = (
    "Ter companheiros por perto... é uma sensação tão boa.",
    "Aurica encerra a cena comovente expressando o calor de ter amigos fiéis ('仲間がいるって...ちょっといいね')."
)

# =========================================================================
# EVENT/606.evd (13051 - 13105) - 55 linhas
# =========================================================================
CURATED[13051] = (
    "Misha!",
    "Lyner encontra Misha reclusa na Cosmosfera ('ミシャ!')."
)
CURATED[13052] = (
    "......",
    "Misha em profunda angústia contemplativa ('...')."
)
CURATED[13053] = (
    "Você tava aqui?! Fiquei preocupado!",
    "Lyner repreende com carinho ('こんなところにいたのか、心配したぞ!')."
)
CURATED[13054] = (
    "Lyner...\nPara que será que eu existo, afinal?",
    "Misha faz o questionamento existencial comovente ('私って、何のために生きてるんだろう')."
)
CURATED[13055] = (
    "M-mas que assunto complicado você foi arrumar...",
    "Lyner embaraçado diante da profundidade do tema ('ま、また難しい事を...')."
)
CURATED[13056] = (
    "Não tô falando de filosofia nenhuma.",
    "Misha corta qualquer tentativa de superficialidade ('別に哲学的な話をしているわけじゃないのよ')."
)
CURATED[13057] = (
    "Sabe, desde pequena, quando me separei de você e dos outros,\nfiquei entoando hinos sem parar numa \"certa área\".\nDia e noite, sem descanso algum...",
    "Misha revela o confinamento eterno em Platina ('ずっと「ある領域」で詩を歌い続けていたわ。それこそ、昼も夜もなく...')."
)
CURATED[13058] = (
    "Por isso, eu não conhecia nada do mundo lá fora.\nE nem tinha permissão de conhecer.",
    "Misha narra o isolamento forçado da infância ('知ることも許されなかった')."
)
CURATED[13059] = (
    "Uma vida como a que qualquer garota comum leva...\nEssa rotina comum que aparece em tantos livros, eu nunca vivi.",
    "Misha lamenta a juventude roubada ('普通の女の子がしているような生活...したことが無いの')."
)
CURATED[13060] = (
    "Qual é o propósito da minha existência?\nSe o meu destino é apenas entoar hinos,\nteria sido muito melhor se eu nem conseguisse pensar nessas coisas...",
    "Misha expressa a dor da senciência sem liberdade ('詩を謳う事だけが定めなら、私...こんな色々なことを考えたり出来ない方が良かった...')."
)
CURATED[13061] = (
    "Teria sido tão mais fácil...\nSe eu tivesse nascido como uma boneca de cantar,\nnão precisaria passar por essa angústia toda...",
    "Misha compara-se a um autômato musical ('謳う人形として生まれていれば、こんな苦悩もしないで済んだのに...')."
)
CURATED[13062] = (
    "Misha...",
    "Lyner comovido com a dor da amiga de infância ('ミシャ...')."
)
CURATED[13063] = (
    "Mas... pensando com a cabeça fria, percebi uma coisa.\nSalvar a vida da Krusche e a minha liberdade\nsão questões completamente diferentes.",
    "Misha eleva-se moralmente em altruísmo ('クルシェの命を助けることと、私の自由とはまた別の問題だって')."
)
CURATED[13064] = (
    "Não importa como se olhe, salvar uma vida é o mais importante.\nMesmo que eu não seja uma ninfa dos hinos... não é?",
    "Misha prioriza a vida de Krusche ('私が詩の精じゃなくても...ね'). Restauração da menção poética à 'ninfa/fada dos hinos' apagada pela NISA."
)
CURATED[13065] = (
    "...Se ela morrer, não haverá volta.\nEnquanto eu ainda posso ter outra chance de ser livre...",
    "Misha aceita postergar sua liberdade pessoal ('死んじゃったらもう戻らないものね。私はまた、自由になれるチャンスがあるかもしれないし...')."
)
CURATED[13066] = (
    "Tem certeza de que isso é o melhor?",
    "Voz misteriosa (Amiga de Infância da Cosmosfera, ID 55) questiona o sacrifício ('本当にそれで良いのかしら?')."
)
CURATED[13067] = (
    "...Hã?",
    "Misha sobressaltada ('...え?')."
)
CURATED[13068] = (
    "Quem é você... afinal?!\nÉ a Misha?!",
    "Lyner confronta a aparição espiritual idêntica a Misha ('お前は...一体!?ミシャなのか!?')."
)
CURATED[13069] = (
    "É claro que sou a Misha.\nSó que eu sou a Misha que veio de um mundo\nque vocês ainda não conhecem.",
    "A entidade espiritual da Cosmosfera revela sua origem ('まだ貴方達が知らない世界から来たミシャ'). Correção do insulto inventado pela NISA ('feeble mind')."
)
CURATED[13070] = (
    "No estado em que estão agora,\nvocês não conseguem sequer me tocar.",
    "A manifestação intangível do inconsciente ('私に触れることすらも出来ない')."
)
CURATED[13071] = (
    "......",
    "Lyner impotente diante do plano mental superior."
)
CURATED[13072] = (
    "Misha. Tem certeza de que vai se conformar com isso?\nVocê queria ser livre... Não era essa a sua vontade?",
    "A contraparte psicológica tenta incitar o egoísmo reprimido ('あなたは自由になりたい...そうじゃなかったかしら?')."
)
CURATED[13073] = (
    "Eu... queria ser livre...",
    "Misha vacila na convicção ('私は...自由に...')."
)
CURATED[13074] = (
    "Mesmo que se sacrifique por uma completa desconhecida,\nnão vai receber nada em troca.\nEm vez disso, você devia dar mais valor à sua própria vida.",
    "A sombra incita Misha a abandonar Krusche ('見ず知らずの誰かに奉仕したって、何かが返ってくるわけじゃないわ')."
)
CURATED[13075] = (
    "E-espera um pouco aí! Não venha do nada\nempurrar os sentimentos da Misha para o rumo errado!",
    "Lyner sai em defesa do equilíbrio emocional da amiga ('ミシャの気持ちを変な方向に持っていかないでくれ')."
)
CURATED[13076] = (
    "Essa frase devia ser minha.",
    "A sombra mental rebate com frieza ('それは私のセリフよ')."
)
CURATED[13077] = (
    "Você é que é um intruso aqui, então não se intrometa mais.\nEu estou agindo pelo que é a verdadeira felicidade da Misha.",
    "A manifestação rejeita a autoridade externa de Lyner na psique dela ('貴方こそ部外者なんだから、これ以上干渉しないで')."
)
CURATED[13078] = (
    "Misha. É você quem deve tomar esse remédio do Yakuan.\nE então, tornar-se humana...\npara viver a vida do jeito que sempre quis.",
    "A tentação máxima: tomar o remédio de Yakuan e abandonar a servidão das Reyvateils ('その薬庵の薬は貴方が飲むべきよ。そして、人間になって...'). Termo canônico 'Yakuan' respeitado."
)
CURATED[13079] = (
    "...Misha...",
    "Lyner angustiado aguardando a decisão dela ('...ミシャ...')."
)
CURATED[13080] = (
    "...Eu decidi: vou salvar a Krusche.\nA minha vida é preciosa, sim,\nmas a vida dos outros é tão preciosa quanto.",
    "Ramo canônico de vitória moral: Misha recusa o egoísmo ('やっぱり私はクルシェを助ける')."
)
CURATED[13081] = (
    "Mesmo se eu não tomar o remédio agora, eu não vou morrer.\nAinda terei outras chances de recomeçar.",
    "Misha abraça a esperança resiliente ('私は今回薬を飲まなくても、決して死ぬわけじゃない')."
)
CURATED[13082] = (
    "Mas com a Krusche...\nse ela morrer, tudo estará acabado para sempre...",
    "A compaixão pura de Misha por Krusche ('死んじゃったら、全てが終わっちゃう...')."
)
CURATED[13083] = (
    "Então essa é a sua escolha.\nEssa decisão trará um impacto profundo\nao âmago do seu inconsciente.",
    "A sombra mental prevê as consequências na psique ('その答えが、深層心理の深いところに多大な影響をもたらすわ')."
)
CURATED[13084] = (
    "Se você continuar tomando apenas decisões que reprimem o que sente,\nas correntes do seu coração nunca se quebrarão.\nGuarde bem o que estou dizendo.",
    "A advertência sobre a repressão dos desejos ('心のクサリは外れないわよ')."
)
CURATED[13085] = (
    "As correntes do meu coração...",
    "Misha ecoa o conceito fundamental da Cosmosfera ('心のクサリ...')."
)
CURATED[13086] = (
    "Se for preciso, eu volto a aparecer.\nAté lá...",
    "A entidade despede-se prometendo retornar ('また必要があれば出てくるわ。それじゃ...')."
)
CURATED[13087] = (
    "...Ela foi embora.",
    "Misha aliviada pelo fim da tentação ('...いっちゃった')."
)
CURATED[13088] = (
    "Vamos voltar para a estalagem.\nEnquanto a gente perde tempo aqui, a Krusche tá sofrendo.",
    "Lyner apressa o retorno para socorrer Krusche ('宿屋へ戻ろう。こうしている間も、クルシェが苦しんでる')."
)
CURATED[13089] = (
    "Sim, você tem razão...",
    "Misha concorda ('うん、そうだね...')."
)
CURATED[13090] = (
    "Será que eu sou meio burro?...\nTem hora que eu simplesmente não consigo entender o que a Misha diz...",
    "Lyner reflete com candura sobre sua dificuldade em alcançar os sentimentos sutis dela ('ミシャが言ってること、よくわからない時があるんだよな...')."
)
CURATED[13091] = (
    "Mas é claro!\nA Misha foi feita com uma inteligência bem superior à sua.",
    "Moradora do Mundo Inferior zomba da ingenuidade masculina de Lyner ('そりゃミシャは、アンタとは頭のデキが違うもの')."
)
CURATED[13092] = (
    "...Desculpa aí, sabichona.",
    "Lyner retruca emburrado com o desaforo ('...悪かったな')."
)
CURATED[13093] = (
    "Além disso, você mal conhece as circunstâncias dela, né?\nSe você descobrir mais sobre os vários lados da Misha,\ncom certeza vai entender tudo.",
    "A moradora mental ensina sobre a necessidade de mergulhar mais fundo ('もっと色々なミシャを知れば、きっと色々わかるのよ')."
)
CURATED[13094] = (
    "...É mesmo?\nBom, não dá para fazer nada quanto a isso agora.",
    "Lyner pragmático encerra o ramo positivo ('...そうか。まあ、今は仕方ないか')."
)
CURATED[13095] = (
    "...Mudei de ideia: eu mesma vou tomar esse remédio.\nAfinal de contas, não é ajudando os outros\nque eu vou encontrar a minha própria felicidade.",
    "Ramo alternativo amargo: Misha sucumbe ao egoísmo e cinismo ('確かに人助けしたところで、自分が幸せになれるとは思えないもの'). Correção da inversão da NISA."
)
CURATED[13096] = (
    "Misha...",
    "Lyner chocado com a virada sombria dela ('ミシャ...')."
)
CURATED[13097] = (
    "Você no fundo é um baita hipócrita, Lyner.\nOu será... que você ainda não tem ideia\ndo tamanho do sofrimento que eu passei?",
    "Misha ataca a hipocrisia e a cegueira de Lyner ('ライナーって意外と偽善者ね')."
)
CURATED[13098] = (
    "De qualquer forma, eu não quero que você\nse intrometa nas minhas decisões de agora em diante.\nPor favor, fique na sua.",
    "Misha rompe o pacto de cumplicidade com o herói ('今後私の判断に口を挟まないで欲しいの。お願いね')."
)
CURATED[13099] = (
    "É exatamente isso.\nA única capaz de sentir a dor da Misha é ela mesma...",
    "A entidade comemora o triunfo do cinismo ('ミシャの苦しみを感じることが出来るのは、ミシャ自身だけ...')."
)
CURATED[13100] = (
    "No fim das contas, você não passa de um intruso.\nNunca será capaz de compreender os verdadeiros sentimentos da Misha.",
    "A sombra condena Lyner à exclusão total ('所詮貴方は部外者よ。ミシャの本当の気持ちを感じ取ることは出来ないわ')."
)
CURATED[13101] = (
    "Por esse motivo, agora você vai desaparecer.",
    "A expulsão forçada de Lyner da mente de Misha ('そんなわけで、貴方には消えてもらうわね')."
)
CURATED[13102] = (
    "E-espera aí!\nEi! Ficou tudo num breu total!",
    "Lyner é engolido pela escuridão do nível corrompido ('ちょ、ちょっと待て!おーい!真っ暗だよ!')."
)
CURATED[13103] = (
    "Não dá para enxergar nada...",
    "Lyner cego no abismo mental ('何も見えない...')."
)
CURATED[13104] = (
    "Pelo visto ela te pegou numa birra daquelas, hein?\nA Misha ainda não confia em você nem um pouco.",
    "A moradora zomba do fracasso relacional de Lyner ('随分と派手に嫌われたのね。まだまだミシャはアンタを信用していないのよ')."
)
CURATED[13105] = (
    "Para conquistar a confiança dela, são as atitudes cotidianas que contam.\nCuide com carinho da Misha no dia a dia e tome prumo na vida!",
    "Conselho de ouro para desbloquear o progresso na Cosmosfera ('信用してもらうには、日頃の行いが物をいうのよ。日常生活でもミシャを大切にしてしっかり生きるのよ')."
)

print(f"Total curated lines defined: {len(CURATED)}")
assert len(CURATED) == 190, f"Expected 190 lines, got {len(CURATED)}"

# Validação linha a linha contra o validador_editorial
input_lines = input_data["dialogues"]
hard_gate_errors = 0
lint_warnings = 0

for item in input_lines:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    trad, note = CURATED[item_id]

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

    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

print(f"\n--- VALIDAÇÃO PRELIMINAR ---")
print(f"Total de Linhas: {len(CURATED)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("\n[PERFEIÇÃO] Todas as 190 linhas passaram com 0 erros e 0 avisos!")
else:
    print("\n[ATENÇÃO] Ajustes necessários.")

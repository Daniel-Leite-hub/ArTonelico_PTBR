# -*- coding: utf-8 -*-
"""Gerador do BLK_EVD_025_output.json com curadoria editorial completa."""

import json
from pathlib import Path

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_025_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_025_output.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

raw_dialogues = input_data["dialogues"]
assert len(raw_dialogues) == 217, f"Esperado 217 falas, obtido {len(raw_dialogues)}"

# Mapeamento ID -> (curated_ptbr, verdict, rationale)
curations = {
    # Event/816.evd (IDs 6349 - 6385)
    6349: (
        "...Misha!?",
        "approved_as_is",
        "Reação espontânea e direta de Lyner ao ver a amiga."
    ),
    6350: (
        "!!\nL-Lyner...!",
        "rewritten",
        "Gaguejo emotivo e surpresa de Misha restaurados conforme JP (ら、頼奈...!)."
    ),
    6351: (
        "O que você está fazendo em frente à minha casa...?\nSe não me engano, hoje... devia ser o dia da cerimônia...",
        "rewritten",
        "Cadência natural, dêixis residencial e hesitação sobre a cerimônia (式の日の式)."
    ),
    6352: (
        "...A-ah, não.\nNão é nada.",
        "rewritten",
        "Hesitação e constrangimento de Misha (あ、ううん。何でもないの)."
    ),
    6353: (
        "Fiquei preocupado agora.\nVocê não tinha algum assunto comigo?",
        "rewritten",
        "Lyner percebe que algo está errado e insiste com empatia (何か用があったんじゃないのか)."
    ),
    6354: (
        "...É, bem... É que...\nÉ sobre a Leila...",
        "rewritten",
        "Construção pausada e relutante de Misha ao mencionar Leila (澪羅のこと)."
    ),
    6355: (
        "...Sobre a Leila?!",
        "rewritten",
        "Eco surpreso de Lyner com ênfase dramática (澪羅の!?)."
    ),
    6356: (
        "Ah, mas hoje é um dia importante, e você deve ter seus preparativos, não é, Lyner? Então... venho de novo amanhã...",
        "rewritten",
        "Misha tenta recuar por consideração aos preparativos de Lyner (大切な日だし、頼奈も準備があるでしょ)."
    ),
    6357: (
        "De jeito nenhum!\nMe conta agora mesmo!!",
        "rewritten",
        "Urgência incisiva e imperativa de Lyner (今から話してくれ!!)."
    ),
    6358: (
        "...!!\nO quê...?! O-o que deu em você...?",
        "rewritten",
        "Susto genuíno de Misha diante do desespero repentino dele (ど、どうしたの)."
    ),
    6359: (
        "É sobre a Leila, não é?!\nAmanhã não vai dar tempo...\nAmanhã... já vai ser tarde demais!",
        "rewritten",
        "Clímax de urgência: Lyner sabe do destino trágico e não pode adiar (明日じゃ間に合わない...手遅れなんだ)."
    ),
    6360: (
        "O-o que foi...?\nVocê sabe de alguma coisa?! ...Me diz!",
        "rewritten",
        "Misha pressiona confusa ao perceber que Lyner sabe algo que ela ignora (何か知ってるの!?...ねえ!)."
    ),
    6361: (
        "De qualquer forma, não adianta a gente ficar conversando aqui fora. Entra em casa.",
        "rewritten",
        "Transição espacial fluida para o interior da residência (家に上がってくれよ)."
    ),
    6362: (
        "...M-mas você...\nQue sujeira é essa?! Não podia ter limpado nem um pouco?",
        "rewritten",
        "Choque doméstico cômico de Misha com a bagunça do quarto de solteiro de Lyner (何?この汚さ...)."
    ),
    6363: (
        "N-não enche!\nHoje foi uma emergência, não tive culpa!\nNormalmente fica bem mais arrumado...!",
        "rewritten",
        "Defesa embaraçada e adolescente de Lyner justificando o caos (緊急事態だから仕方ないだろ)."
    ),
    6364: (
        "Hummm...\nSei, até parece.",
        "rewritten",
        "Ironia afetuosa e cética de Misha (ふーん...。本当かしら)."
    ),
    6365: (
        "Mas enfim, o que é isso sobre a Leila?!",
        "rewritten",
        "Retomada incisiva do foco dramático por Lyner (それで、澪羅の話って何なんだよ!)."
    ),
    6366: (
        "...É. Na verdade...",
        "rewritten",
        "Transição séria de tom de Misha (...ええ。実は...)."
    ),
    6367: (
        "Este mundo... tem alguma coisa de muito estranha com ele.",
        "rewritten",
        "Declaração metafísica de Misha sobre a anomalia do mundo simulado (この世界...何か変なのよ)."
    ),
    6368: (
        "...Estranha?",
        "rewritten",
        "Eco intrigado de Lyner."
    ),
    6369: (
        "Sim.\nÉ verdade que a Leila na Facção Mir...\nNão, ela é um vírus criado por mim.",
        "rewritten",
        "Termo canônico Facção Mir (ミュール団) e confissão autoral de Misha sobre o vírus (私が生んだウイルス)."
    ),
    6370: (
        "Mas mesmo assim, por mais que eu pense nisso, não faz sentido. Ela não conseguir sobreviver sem passar por uma depuração toda semana...",
        "rewritten",
        "Reflexão técnica de Misha sobre a exigência de depuração semanal (1週間ごとにリフレッシュ)."
    ),
    6371: (
        "Eu nunca programei nada disso!\nMesmo revirando as especificações que escrevi,\nnão existe uma linha sequer sobre isso!",
        "rewritten",
        "Vocabulário de programação e lógica de sistemas da mente (仕様書をひっくり返しても、どこにもそんな記述はない)."
    ),
    6372: (
        "V-você me falando isso assim, mas...",
        "rewritten",
        "Desconcerto de Lyner diante dos termos técnicos de criação (そ、そんなこと言われてもなぁ)."
    ),
    6373: (
        "Este mundo...\npode estar sob a 'Ameaça do Mundo Exterior'.",
        "rewritten",
        "Conceito filosófico central da cena (外界からの脅威)."
    ),
    6374: (
        "A... ame... aça... do... mundo... exterior?\nN-não vai me dizer... que você acha que tem alienígenas...?",
        "rewritten",
        "Lyner soletrando perplexo a palavra silabada em hiragana (が...がいかい...からの...きょうい?)."
    ),
    6375: (
        "Muito mais que alienígenas!\nNão estou falando de fora deste planeta, e sim de fora deste mundo!",
        "rewritten",
        "Misha esclarece que a fronteira é dimensional/simulada, não astronômica (宇宙人どころじゃないわよ)."
    ),
    6376: (
        "Se a minha dedução estiver correta, do lado de fora deste mundo existe uma imensa entidade que rege a nossa própria ordem.",
        "rewritten",
        "Intuição genial de Misha sobre o operador/mundo real fora da Cosmosfera (大きな存在がある)."
    ),
    6377: (
        "E essa entidade estaria... manipulando tudo nas sombras, é isso o que está dizendo?",
        "rewritten",
        "Lyner interpretando o conceito de intervenção externa (裏操作された...っていうのか)."
    ),
    6378: (
        "...Exatamente.",
        "rewritten",
        "Confirmação categórica de Misha (...そうよ)."
    ),
    6379: (
        "Mundo de fora...\nSerá que... você está falando do mundo fora da Cosmosfera...?",
        "rewritten",
        "Lyner quase quebrando a quarta parede da Cosmosfera ao reconhecer o mundo real (コスモスフィアの外の世界)."
    ),
    6380: (
        "Cosmo-o quê...?",
        "rewritten",
        "Incompreensão genuína de Misha com a palavra proibida (コスモス...?)."
    ),
    6381: (
        "A-ah, não, não é nada.",
        "rewritten",
        "Recuo apressado de Lyner para preservar a integridade mental dela (あ、いや、何でもない)."
    ),
    6382: (
        "Se eu conseguisse enxergar esse tal 'Mundo Exterior'...",
        "rewritten",
        "Anseio transcendental de Misha (その『外側の世界』を見ることができたら)."
    ),
    6383: (
        "...",
        "rewritten",
        "Silêncio reflexivo de Lyner."
    ),
    6384: (
        "Acho que o nosso próprio mundo mudaria drasticamente.",
        "rewritten",
        "Premonição de Misha sobre o impacto da verdade (この世界自体が、大きく変わると思うのよ)."
    ),
    6385: (
        "De qualquer forma, vamos dar uma volta na cidade para ver se encontramos mais alguma pista.",
        "rewritten",
        "Ação pragmática de Misha para iniciar a investigação (町に出て、何か他にも手がかりがないか)."
    ),

    # Event/623.evd (ID 6386)
    6386: (
        "Vocês aí... Nem pensem em cruzar a soleira\ndesta casa sem trazer bebida antes!!",
        "rewritten",
        "Registro popular e agressivo de bêbado/morador do mundo inferior (敷居またぐんじゃネェ!!)."
    ),

    # Event/51.evd (ID 6387)
    6387: (
        "Não pode. Primeiro você precisa me dar a ordem.\nAperte o botão IM03 para abrir os comandos...",
        "rewritten",
        "Preservação estrita da tag de botão IM03 e instruções calmas de Aurica em combate."
    ),

    # Event/89.evd (IDs 6388 - 6409)
    6388: (
        "Sejam bem-vindos!\nBoas-vindas à Loja de Mergulho.",
        "rewritten",
        "Recepção comercial alegre do atendente do Dive Shop (ダイブ屋へようこそ)."
    ),
    6389: (
        "Ora, ora... que armadura diferente essa sua...",
        "rewritten",
        "Comentário curioso sobre o traje de Cavaleiro de Platina de Lyner (見かけない鎧だね)."
    ),
    6390: (
        "Mas pelo jeitinho... essa mocinha linda é uma Reyvateilzinha...?",
        "rewritten",
        "Tom afetuoso e fã de Reyvateil do atendente (レーヴァテイルたん)."
    ),
    6391: (
        "É-é... bem, sou sim.",
        "rewritten",
        "Misha tímida e desconfiada com a abordagem (え、ええ...まあ)."
    ),
    6392: (
        "E-eu sabia! O meu faro ainda\nnão perdeu o costume!\nHehehe...",
        "rewritten",
        "Entusiasmo cômico do atendente (ボクの勘はまだ鈍ってなかったよ! フフフ...)."
    ),
    6393: (
        "Ééé...",
        "rewritten",
        "Pigarro sem graça de Lyner estranhando o sujeito (えっと...)."
    ),
    6394: (
        "Ah, mil desculpas! Vocês vieram\npara um Mergulho, não é?\nSendo assim...",
        "rewritten",
        "O atendente se recompõe e convida para a câmara de Mergulho (ダイブしに来たんだよね)."
    ),
    6395: (
        "E-espera um segundo!!",
        "rewritten",
        "Pânico repentino de Misha interrompendo a entrada (ちょ、ちょっと待って!!)."
    ),
    6396: (
        "Misha?",
        "approved_as_is",
        "Perplexidade de Lyner."
    ),
    6397: (
        "...O-o que foi?",
        "rewritten",
        "Atendente confuso com a hesitação dela (...ど、どうしたのかな)."
    ),
    6398: (
        "P-preciso me preparar psicologicamente...\nSó mais um pouquinho...!",
        "rewritten",
        "Angústia e timidez diante da intimidade do Mergulho (も、もうちょっと心の準備させて...!)."
    ),
    6399: (
        "Hã?...\nAh, por mim sem problema nenhum,\nmas tem certeza?",
        "rewritten",
        "Compreensão paciente e acolhedora de Lyner (そりゃ全然構わないけど)."
    ),
    6400: (
        "Me perdoa de verdade. Outro dia\neu disse 'Se for com o Lyner, tudo bem...',\nmas...",
        "rewritten",
        "Misha relembrando sua promessa com culpa e vulnerabilidade (『ライナーならいいよ...』なんて言ったけど)."
    ),
    6401: (
        "O Mergulho...\né algo sagrado demais para uma Reyvateil...",
        "rewritten",
        "Peso solene do Mergulho na alma de uma donzela (とても大切な事だから)."
    ),
    6402: (
        "Eu sei disso, Misha.",
        "rewritten",
        "Resposta serena de respeito mútuo de Lyner (わかってるさ)."
    ),
    6403: (
        "Sinto muitíssimo mesmo!",
        "rewritten",
        "Desculpas sinceras de Misha (ホントにごめんなさい!)."
    ),
    6404: (
        "Mas entenda uma coisa, por favor!\nNão é que eu não queira fazer isso com você!",
        "rewritten",
        "Misha garantindo com afeto que confia nele plenamente (相手がライナーじゃダメ...って事じゃないの!)."
    ),
    6405: (
        "É que ainda preciso colocar em ordem\nos sentimentos dentro de mim...\nMe desculpa, tá?",
        "rewritten",
        "Confissão emocional doce de Misha (気持ちの整理の問題だから)."
    ),
    6406: (
        "Ela tem toda razão.\nPara uma Reyvateilzinha, o Mergulho\né um evento de extrema importância.",
        "rewritten",
        "Atendente demonstrando respeito pela dignidade das Reyvateils (一大行事)."
    ),
    6407: (
        "Hoje em dia as pessoas perderam esse bom senso\ne mergulham a torto e a direito,\nsem ligar para o que a parceira sente...",
        "rewritten",
        "Crítica contextual ao abuso da tecnologia de mergulho (好き嫌い関係ナシにダイブしやがる)."
    ),
    6408: (
        "Eu até ficava meio triste com isso.\nMas vejo que vocês dois são bem diferentes.",
        "rewritten",
        "Elogio caloroso à sintonia do casal (お兄さん達は違うみたいだね)."
    ),
    6409: (
        "Voltem sempre, viu?\nNa próxima visita eu dou um agrado para vocês...\nHehehe...",
        "rewritten",
        "Despedida bem-humorada do lojista (サービスするよ、フフフ...)."
    ),

    # Event/335.evd (IDs 6410 - 6417)
    6410: (
        "Com licença.\nGostaria de perguntar uma coisa...",
        "rewritten",
        "Polidez natural de Aurica ao abordar NPC (すいません。少し聞きたい事があるんです)."
    ),
    6411: (
        "Hum, entendi.\nSe não me engano, já ouvi falar\nde um item assim, sim...",
        "rewritten",
        "NPC buscando na memória o item citado (確かそんなアイテム有ったわね)."
    ),
    6412: (
        "Deixa eu ver...",
        "rewritten",
        "Pausa reflexiva (んーと...)."
    ),
    6413: (
        "Ééé...",
        "rewritten",
        "Hesitação cômica contínua (えーと...)."
    ),
    6414: (
        "...E então?!",
        "rewritten",
        "Aurica demonstrando expectativa ansiosa (...さあ!)."
    ),
    6415: (
        "...Esqueci.",
        "rewritten",
        "Quebra cômica seca do NPC (...忘れちゃった)."
    ),
    6416: (
        "Ah, não...",
        "rewritten",
        "Frustração graciosa de Aurica (えー...。)."
    ),
    6417: (
        "Talvez o rapaz da loja de variedades lá embaixo\nentenda melhor dessas coisas.",
        "rewritten",
        "Encaminhamento para o comerciante (下の雑貨屋のお兄さん)."
    ),

    # Event/496.evd (IDs 6418 - 6435)
    6418: (
        "Então é este...\no gerador de força motriz que mantém\nesta ilha flutuando...",
        "rewritten",
        "Admiração solene de Shurelia pela engenharia (この島を浮かしている動力なんですね)."
    ),
    6419: (
        "Dizem que deu um trabalhão danado\npara colocar esta ilha no ar.",
        "rewritten",
        "Tom direto e prático de Krusche (随分苦労したらしいよ)."
    ),
    6420: (
        "Eles construíram só este núcleo de propulsão lá no Cais Flutuante e, depois de colocá-lo no ar, foram erguendo a cidade em volta.",
        "rewritten",
        "Explicação de engenharia: Cais Flutuante (滞空岸壁) e núcleo de propulsão (核動力部)."
    ),
    6421: (
        "Para a sustentação, adotaram o Circuito\nde Equilíbrio Classe I, Série 3, não foi?",
        "rewritten",
        "Conhecimento técnico refinado de Shurelia: Circuito de Equilíbrio (平衡回路I属三系)."
    ),
    6422: (
        "De fato, em termos de economia e estabilidade\né a melhor opção. Considero uma escolha\nmuito acertada.",
        "rewritten",
        "Avaliação sóbria da deusa sobre eficiência energética (経済性と安定性では一番)."
    ),
    6423: (
        "Nossa, você entende mesmo do assunto, hein?",
        "rewritten",
        "Krusche impressionada com o conhecimento técnico de Shurelia (色々知ってるんだね)."
    ),
    6424: (
        "Sim. Afinal de contas, até o Beco Vagalume\nflutua graças ao poder do Silver Horn.",
        "rewritten",
        "Termos canônicos Beco Vagalume (ほたる横丁) e Silver Horn (シルヴァホルン)."
    ),
    6425: (
        "Graças ao poder... do Silver Horn?",
        "rewritten",
        "Lyner indagando sobre a influência remota do Silver Horn."
    ),
    6426: (
        "Exato. A tecnologia de levitação do Beco Vagalume\ntambém provém do Grathmeld.",
        "rewritten",
        "Termo canônico Grathmeld (グラスメルク)."
    ),
    6427: (
        "O princípio teórico é exatamente o mesmo das bombas que você costuma criar, Lyner.",
        "rewritten",
        "Analogia direta entre alquimia de combate e flutuação de cidades."
    ),
    6428: (
        "Afinal, o Grathmeld é um sistema mágico\nsuprido e sustentado pelo Silver Horn.",
        "rewritten",
        "Cosmologia fônica: Silver Horn como servidor do sistema mágico Grathmeld."
    ),
    6429: (
        "É verdade... Pensando bem, o Grathmeld\nnão é uma força da natureza, né...?",
        "rewritten",
        "Lyner assimilando a natureza tecnológica da magia de Sol Ciel."
    ),
    6430: (
        "O Silver Horn apenas capta os sinais emitidos\npelos Cristais Grathnode e devolve\nseus respectivos efeitos.",
        "rewritten",
        "Mecânica de ressonância dos Cristais Grathnode (グラスノ結晶)."
    ),
    6431: (
        "Contudo... esta ilha é uma criação\nque vai muito além da minha imaginação...",
        "rewritten",
        "Humildade tocante da deusa perante o engenho dos mortais."
    ),
    6432: (
        "Jamais imaginei que alguém pudesse erguer\nalgo dessa magnitude a partir daquele sistema mágico.",
        "rewritten",
        "Admiração profunda pelo triunfo da arquitetura humana."
    ),
    6433: (
        "Puxa... é mesmo?",
        "rewritten",
        "Krusche fascinada ao ouvir isso da própria criadora (そうなんだ...)."
    ),
    6434: (
        "Os habitantes de Horus... demonstram uma energia\ne uma força de vontade impressionantes.",
        "rewritten",
        "Elogio à perseverança do povo de Horus (ホルスの住人)."
    ),
    6435: (
        "Expresso a todos o meu mais sincero respeito.\nMuito obrigada por levarem o Grathmeld\na um patamar tão sublime...",
        "rewritten",
        "Reverência solene e graciosa de Shurelia (敬意を表します)."
    ),

    # Event/72.evd (IDs 6436 - 6438)
    6436: (
        "Bela defesa! Agora aproveita o embalo\ne manda um contra-ataque certeiro!",
        "rewritten",
        "Tutorial dinâmico em combate de Misha (ナイスガード! そのまま一気にカウンター決めちゃえ!)."
    ),
    6437: (
        "Aperte os botões que aparecem na tela, viu?",
        "rewritten",
        "Comando claro de gameplay (表示されているボタンを押してね)."
    ),
    6438: (
        "Se você ficar moscando,\no contra-ataque vai falhar, então presta atenção!",
        "rewritten",
        "Voz viva e expressiva de Misha alertando sobre o timing (ボーっとしてると)."
    ),

    # Event/201.evd (IDs 6439 - 6449)
    6439: (
        "Sejam bem-vindos!\nOra, se não é o herdeirinho!\nQuanto tempo, rapaz!",
        "rewritten",
        "Comerciante tratando Lyner pelo apelido de infância (おぼっちゃん! 久しぶりだねぇ)."
    ),
    6440: (
        "...Herdeirinho...?",
        "rewritten",
        "Aurica repetindo com curiosidade tímida (...おぼっちゃん...)."
    ),
    6441: (
        "Larga dessa mania de me chamar assim!\nÉ uma vergonha, sabia?!",
        "rewritten",
        "Lyner irritado e envergonhado diante de Aurica (その言い方やめてくれよ! 恥ずかしいだろ?)."
    ),
    6442: (
        "Mas do que está reclamando?\nSendo filho do Comandante Supremo,\nvocê é o herdeiro mais mimado de Platina inteira!",
        "rewritten",
        "Humor sobre o status nobre da família Barsett (総帥の息子なんだから、プラティナ1のおぼっちゃま)."
    ),
    6443: (
        "Lyner, eu não fazia ideia de que você\nera alguém tão importante...",
        "rewritten",
        "Aurica impressionada de maneira inocente (そんなにすごい人だったんだ)."
    ),
    6444: (
        "Não tem nada de importante em mim...",
        "rewritten",
        "Lyner desconversando com modéstia sincera (俺がすごいんじゃないよ)."
    ),
    6445: (
        "E ultimamente, será que vocês dois\nnão fizeram as pazes nem um pouquinho?",
        "rewritten",
        "Comerciante sondando a relação tensa de Lyner com o pai (少しは仲直りしたんじゃないのかい)."
    ),
    6446: (
        "Que nada!\nEle continua na mesma de sempre:\n'Vá estudar! Vá estudar!'... não larga do meu pé.",
        "rewritten",
        "Lyner imitando a cobrança rígida do Comandante Leard (相変わらず「勉強しろ!」)."
    ),
    6447: (
        "É, meus pêsames então.\nSeja como for, faz tempo que não aparece.\nHoje vou te dar um Funbun por conta da casa!",
        "rewritten",
        "Termo canônico Funbun (オボンヌ) e cortesia comercial de vizinhança."
    ),
    6448: (
        "Que maravilha!!\nMuito obrigado, tio!",
        "rewritten",
        "Alegria pueril de Lyner ao ganhar sua guloseima predileta (ラッキー!! ありがとう、おじさん!)."
    ),
    6449: (
        "Obteve o item [Doce Famoso Funbun]!",
        "rewritten",
        "Padronização canônica de obtenção de item com colchetes balanceados."
    ),

    # Event/678.evd (IDs 6450 - 6481)
    6450: (
        "A Academia deve ser aqui mesmo.\nOnde será que ela está...?",
        "rewritten",
        "Monólogo de Lyner procurando a colega de Elie na Academia (アカデミーって、ここだよな)."
    ),
    6451: (
        "Ué? Quem é você?\nNão é estudante desta Academia, é?",
        "rewritten",
        "Eizel abordando o forasteiro de forma assertiva (このアカデミーの生徒じゃないわよね)."
    ),
    6452: (
        "A-ah... é que me pediram um favor...\nEstou procurando por uma tal de Eizel...",
        "rewritten",
        "Lyner explicando seu recado (アイゼルって人を探してるんだけど)."
    ),
    6453: (
        "Hã?! ...Mas essa... sou eu.\nO que você quer comigo, afinal?",
        "rewritten",
        "Surpresa e pose desconfiada de Eizel (え!?...それ...私よ。一体何の用?)."
    ),
    6454: (
        "O quê...?! Então você é a Eizel?!\nQue alívio! Já me poupou o trabalho de procurar!",
        "rewritten",
        "Espontaneidade de Lyner comemorando o encontro (探す手間が省けたよ!)."
    ),
    6455: (
        "E então?... O que você quer de mim?!",
        "rewritten",
        "Eizel impaciente cobrando o objetivo da visita (で?...何の用なの!?)."
    ),
    6456: (
        "A-ah, sim...\nBem, na verdade a Misha... não, digo,\na Elie me pediu um favor...",
        "rewritten",
        "Lyner quase tropeçando no nome real de Misha no papel de Elie (ミシャ...じゃなかった、エリーから)."
    ),
    6457: (
        "...Da Elfir...?!",
        "rewritten",
        "Eizel pronunciando o nome completo canônico da protagonista de Atelier Elie (エルフィールから)."
    ),
    6458: (
        "Parece que ela está tentando criar uma bomba chamada Meteoro, mas não dá certo de jeito nenhum.",
        "rewritten",
        "Termo alquímico Meteoro (メテオール) e as constantes falhas de síntese de Elie."
    ),
    6459: (
        "Então ela me pediu para te entregar estas anotações...",
        "rewritten",
        "Entrega do bilhete com a fórmula (メモを預かってきたんだけど)."
    ),
    6460: (
        "Um Meteoro, é?!\nSerá que aquela garota quer caçar um dragão por acaso? Enfim, deixa eu dar uma olhada nisso aqui.",
        "rewritten",
        "Comentário cômico de Eizel sobre o poder destrutivo da bomba (竜でも倒しに行く気なのかしら)."
    ),
    6461: (
        "Mas o que é isso... Não tem nem metade dos materiais necessários! Ela não tem jeito mesmo...",
        "rewritten",
        "Diagnóstico imediato de alquimista veterana criticando a distração de Elie (全然材料が足りないじゃない)."
    ),
    6462: (
        "Tudo bem, eu vou escrever a receita certa para ela.\nEspere aqui um instante.",
        "rewritten",
        "Prontidão prestativa de Eizel apesar das queixas (私がレシピ書いてあげるから)."
    ),
    6463: (
        "(Dá para ver na hora que é o quarto de uma garota...\nFico até meio sem jeito...)",
        "rewritten",
        "Timidez e pureza de Lyner sozinho no quarto de uma moça (女の子の部屋って感じだな... ちょっと緊張する)."
    ),
    6464: (
        "Prontinho.\nEsquecer um ingrediente tão importante assim...\nEla é mesmo uma desastrada sem cura.",
        "rewritten",
        "Afeto severo característico de Eizel por Elie (本当にどんくさい子ね)."
    ),
    6465: (
        "Faltava o ingrediente mais importante de todos:\no [Fragmento de Estrela].",
        "rewritten",
        "Termo canônico [Fragmento de Estrela] (星のかけら)."
    ),
    6466: (
        "Muito provavelmente ela não deve ter nenhum,\nentão acho bom você ir buscar um para ela.",
        "rewritten",
        "Instrução direta para a missão de coleta (取りに行ってあげた方がいいんじゃない)."
    ),
    6467: (
        "C-certo...\nMas você falando assim... eu não faço ideia\nde onde encontrar isso...",
        "rewritten",
        "Incerteza desarmada de Lyner (俺...場所知らないし)."
    ),
    6468: (
        "Não sabe? Você também é um baita cabeça-dura, hein? O Fragmento de Estrela é uma estrela cadente que cai no [Planalto Oriental], bem ao leste.",
        "rewritten",
        "Termo canônico [Planalto Oriental] (東の台地) e bronca divertida de Eizel (相当どんくさいわね)."
    ),
    6469: (
        "...E isso fica onde exatamente?",
        "rewritten",
        "Pergunta cândida de Lyner que desarma qualquer paciência (...それって、どこ?)."
    ),
    6470: (
        "...",
        "rewritten",
        "Silêncio estupefato de Eizel perante a ignorância geográfica dele."
    ),
    6471: (
        "Hahaha... foi mal...",
        "rewritten",
        "Riso sem graça e envergonhado de Lyner (ははは...ごめん)."
    ),
    6472: (
        "Haa... tudo bem. Não tem outro jeito mesmo.\nEu vou junto com você.",
        "rewritten",
        "Vocalização natural Haa... sem rubricas (*suspiro*) e resignação solícita (私も一緒に行ってあげるわよ)."
    ),
    6473: (
        "Hã?! N-não precisa, não quero incomodar tanto...",
        "rewritten",
        "Lyner tentando recusar por constrangimento (い、いいよ、さすがにそこまでは)."
    ),
    6474: (
        "Se você for sozinho, é certeza que vai acabar\ncatando uma pedra que não tem nada a ver.",
        "rewritten",
        "Ironia perspicaz de Eizel prevendo o desastre (全然違う石を拾って来そうだもの)."
    ),
    6475: (
        "...Entendi. Muito obrigado.\nE desculpa te dar esse trabalho por minha causa...",
        "rewritten",
        "Agradecimento caloroso de Lyner (悪いな、俺何かのために)."
    ),
    6476: (
        "Não estou fazendo isso por você!",
        "rewritten",
        "Reação clássica tsundere de Eizel cortando a intimidade (あなたの為じゃないわよ!)."
    ),
    6477: (
        "...Hã?",
        "rewritten",
        "Perplexidade ingênua de Lyner (...え?)."
    ),
    6478: (
        "...",
        "rewritten",
        "Pausa sem palavras de Eizel disfarçando a vergonha."
    ),
    6479: (
        "E-enfim, nós vamos ou não? O [Planalto Oriental] fica longe. Como não dá para confiar na sua segurança sozinho, vamos contratar mais um guarda-costas para acompanhar.",
        "rewritten",
        "Termo [Planalto Oriental] e dinâmica clássica de RPG/Atelier de contratar guarda-costas na taverna."
    ),
    6480: (
        "Na taverna [Pavilhão Alado]... ou em frente ao portão do castelo, deve ter alguém à toa querendo trabalho. Vamos passar lá e recrutar alguém.",
        "rewritten",
        "Local canônico da série Atelier: taverna [Pavilhão Alado] (酒場「飛翔亭」, Flying Pavilion/Hishotei)."
    ),
    6481: (
        "...T-tudo bem. Combinado.\nVamos passar lá, então.",
        "rewritten",
        "Aceitação dócil e cooperativa de Lyner (...あ、ああ。わかった。寄っていこう)."
    ),

    # Event/207.evd (IDs 6482 - 6488)
    6482: (
        "Falando nisso, Krusche...\nvocê é mesmo uma das integrantes da equipe de busca?",
        "rewritten",
        "Pergunta de Lyner sobre a comitiva oficial (捜索隊のメンバーなのか)."
    ),
    6483: (
        "Bom, eu até fui indicada como candidata da equipe,\nmas, pessoalmente, ainda não decidi nada.",
        "rewritten",
        "Concordância correta no feminino para Krusche (indicada como candidata) preservando tom informal."
    ),
    6484: (
        "Acho que vou ver como as coisas andam\nna hora... talvez.",
        "rewritten",
        "Indecisão descontraída (その時の状況を見て...かな)."
    ),
    6485: (
        "Mais do que isso, o que me deixa intrigada\né saber o que tem lá em cima...",
        "rewritten",
        "Fascínio de Krusche pelo horizonte superior da Torre (ここより上が気になってて)."
    ),
    6486: (
        "...Lá em cima?",
        "rewritten",
        "Eco reflexivo de Lyner."
    ),
    6487: (
        "É, lá no alto. Muito acima da Blastline...\nQue tipo de lugar será que existe por lá?",
        "rewritten",
        "Termo canônico Blastline e a poesia da aspiração aeronáutica de Krusche."
    ),
    6488: (
        "Enfim, é mais ou menos isso o que sinto.\nDesculpe se fiquei divagando.",
        "rewritten",
        "Krusche desculpando-se por expressar devaneios (曖昧でごめん)."
    ),

    # Event/585.evd (IDs 6489 - 6502)
    6489: (
        "Hama!?\nHama!!",
        "approved_as_is",
        "Gritos urgentes de Lyner chamando a guardiã."
    ),
    6490: (
        "Mas o que foi?!\nNão precisa berrar desse jeito,\neu não sou surda!",
        "rewritten",
        "Resposta ríspida e cômica de Hama com dicção natural brasileira (そんなに大声出さなくても聞こえてるわよ)."
    ),
    6491: (
        "Hama, por favor!\nMe ensina o tal do 'Código Hymmnos' da Misha.\nVocê sabe qual é, não sabe?!",
        "rewritten",
        "Termo canônico 'Código Hymmnos' (ヒュムネコード) substituindo o decalque errôneo 'Código do Hino'."
    ),
    6492: (
        "M-mas o que deu em você assim do nada...?\nÉ claro que eu sei, ora essa.",
        "rewritten",
        "Soberba protetora de Hama admitindo posse do segredo (当然知ってるに決まってるじゃない)."
    ),
    6493: (
        "É sério?!\nPor favor! Me ensina!!",
        "rewritten",
        "Apelo impaciente e ingênuo de Lyner (頼む! 教えてくれ!!)."
    ),
    6494: (
        "...",
        "rewritten",
        "Pausa teatral e julgadora de Hama."
    ),
    6495: (
        "E quem foi que disse que eu vou dar\no Código Hymmnos dela para você, seu palerma?",
        "rewritten",
        "Ironia ácida de Hama protegendo a intimidade de Misha (誰がアンタに教えるモンですか)."
    ),
    6496: (
        "Não faz assim... Não fala isso, por favor...",
        "rewritten",
        "Lamento frustrado de Lyner (そんなこと言わずに...)."
    ),
    6497: (
        "Fique sabendo que o Código Hymmnos é como se fosse\na chave privada do coração de uma garota.\nVocê acha que uma donzela entregaria a chave\ndo próprio quarto de bandeja para qualquer um?",
        "rewritten",
        "Metáfora canônica de Ar tonelico: a chave privada (プライベートキー) e o quarto da garota."
    ),
    6498: (
        "Você ainda não conquistou confiança suficiente\npara merecer essa chave.\nTrate de cuidar melhor da Misha primeiro!",
        "rewritten",
        "Exigência de maturidade emocional e compromisso (もっとミシャを大切にしなさい)."
    ),
    6499: (
        "...",
        "rewritten",
        "Silêncio cabisbaixo de Lyner."
    ),
    6500: (
        "Vejamos... Quando você alcançar pelo menos\no Nível 4 da Cosmosfera dela, talvez eu pense no seu caso.",
        "rewritten",
        "Mecânica de progressão mental: Nível 4 da Cosmosfera (コスモスフィアのレベルが4くらいになったら)."
    ),
    6501: (
        "É sério?!",
        "rewritten",
        "Esperança renovada de Lyner (本当か!?)."
    ),
    6502: (
        "Por isso mesmo, trate a Misha com todo o carinho.\nNão é como se eu estivesse sendo implicante por maldade.",
        "rewritten",
        "Subtexto de afeto maternal/protetor de Hama por Misha (私だって意地悪してるワケじゃないんだから)."
    ),

    # Event/515.evd (IDs 6503 - 6519)
    6503: (
        "Aqui é a Krusche, chefe do [Projeto Shoga].\nA Presidente Ayano está?",
        "rewritten",
        "Termos canônicos [Projeto Shoga] (プロジェクト『翔雅』) e Presidente Ayano (亜耶乃社長)."
    ),
    6504: (
        "Um momento, por favor.",
        "rewritten",
        "Polidez corporativa formal da secretária da Tenba (少々お待ちください)."
    ),
    6505: (
        "Agradeço a espera. Vou conduzi-los.\nPor favor, queiram me acompanhar.",
        "rewritten",
        "Atendimento cerimonioso da recepção (それではご案内します。こちらへどうぞ)."
    ),
    6506: (
        "Fico grata por sua vinda, Sir Lyner.\nPeço escusas por minhas constantes ausências.",
        "rewritten",
        "Tratamento solene e nobre da Presidente Ayano com concordância feminina (よく来てくれた、ライナー殿。留守が多くてすまんな)."
    ),
    6507: (
        "Ultimamente tenho liderado expedições de reconhecimento\na novos setores da Torre, por isso mal tenho\npermanecido na sede da empresa.",
        "rewritten",
        "Liderança executiva e exploração pioneira da Torre por Ayano (塔の新地点の探索)."
    ),
    6508: (
        "Novos setores... a senhora diz?",
        "rewritten",
        "Lyner tratando a Presidente com respeito protocolar (新地点...ですか?)."
    ),
    6509: (
        "Sim, na verdade é um local muitíssimo\npróximo de Nemo.",
        "rewritten",
        "Topônimo canônico Nemo (ネモ)."
    ),
    6510: (
        "Mas deixando isso de lado, o incidente com Bourd causou-lhes transtornos incomensuráveis. Gostaria de reiterar minhas mais sinceras desculpas.",
        "rewritten",
        "Pedido de desculpas institucional e digno pela traição de Bourd (ボルドの件は本当に迷惑を掛けた。改めて詫びを言う)."
    ),
    6511: (
        "Não se preocupe, não precisa mais se desculpar por isso. Além do mais, a reputação da Tenba anda excelente ultimamente.",
        "rewritten",
        "Generosidade e diplomacia calorosa de Lyner (最近は天覇の評判いいみたいですね)."
    ),
    6512: (
        "Graças aos seus esforços. Contudo, as conspirações de Bourd ainda não foram completamente desvendadas.",
        "rewritten",
        "Ayano reconhecendo o mérito de Lyner e a persistência das intrigas de Bourd (ボルドの陰謀)."
    ),
    6513: (
        "Especialmente no laboratório situado no local da queda da Placa Hexagonal... onde incontáveis dados de sua pesquisa devem permanecer soterrados.",
        "rewritten",
        "Correção do erro crasso da NISA ('research data was lost'): em JP há muitos dados soterrados para resgate (沢山埋もれているはずだ)."
    ),
    6514: (
        "...A Placa Hexagonal... Devem existir informações bastante valiosas por lá...",
        "rewritten",
        "Reflexão estratégica de Lyner sobre a importância dos dados (六角板... 結構役に立つ情報)."
    ),
    6515: (
        "Senhora Ayano.\nA senhora nos concederia autorização para vasculhar a Placa Hexagonal?",
        "rewritten",
        "Solicitação formal respeitosa de expedição (亜耶乃さん。俺たちに六角板の探索を許可してもらえませんか)."
    ),
    6516: (
        "Hum... Por se tratar de uma instalação onde repousam segredos vitais de segurança máxima, eu jamais autorizaria a entrada de civis, mas...",
        "rewritten",
        "Dilema ético e institucional da líder corporativa (最重要機密の沢山眠る場所故、部外者の探索は認めないのだが)."
    ),
    6517: (
        "Tratando-se de um pedido seu, Lyner, e de mais ninguém... eu concedo a autorização de acesso.",
        "rewritten",
        "Confiança pessoal absoluta de Ayano no Cavaleiro (他でもないライナーの頼みだ。立ち入りを許可しよう)."
    ),
    6518: (
        "Muito obrigado, Senhora Ayano!",
        "rewritten",
        "Agradecimento vibrante e respeitoso de Lyner (ありがとうございます!)."
    ),
    6519: (
        "Certo! Vamos agora mesmo ao laboratório\nda Placa Hexagonal!",
        "rewritten",
        "Entusiasmo da liderança em ação partindo para o local da queda (さっそく六角板の研究所へ行こう!)."
    ),

    # Event/971.evd (IDs 6520 - 6541)
    6520: (
        "Ficou pronto!\nNão parecia, mas deu um trabalhão danado...\nAinda assim, consegui terminar a tempo...",
        "rewritten",
        "Alívio de Lyner após o minucioso trabalho de confecção artesanal do boneco (出来た! 結構大変だったけど)."
    ),
    6521: (
        "Vou logo dar de presente para a Aurica...",
        "rewritten",
        "Intenção afetuosa e ansiosa de presenteá-la (さっそくオリカにプレゼントするか)."
    ),
    6522: (
        "Aurica. Tem um minutinho?",
        "rewritten",
        "Abordagem carinhosa e direta (オリカ。ちょっといいか?)."
    ),
    6523: (
        "Lyner?... O que foi?",
        "rewritten",
        "Doçura e curiosidade receptiva de Aurica (ライナー?...どうしたの?)."
    ),
    6524: (
        "Isto aqui... fui eu mesmo quem fiz.\nSe você gostar... aceitaria ficar com ele?",
        "rewritten",
        "Pudor e generosidade ao oferecer o presente (受け取ってもらえないか)."
    ),
    6525: (
        "Entregou o item [Don Leon].",
        "rewritten",
        "Formato canônico de entrega de item com colchetes balanceados."
    ),
    6526: (
        "Isto é... o Don Leon...?\nLyner, por que você... fez o Don Leon...?",
        "rewritten",
        "Surpresa comovida e tímida de Aurica diante da pelúcia (ライナーがどうして...どんすけを...)."
    ),
    6527: (
        "Você gostava tanto dele no passado, não era?\nDesde quando era criança... e soube que, até hoje,\nele é o maior esteio do seu coração...",
        "rewritten",
        "Conceito fundamental de worldbuilding emocional: esteio do coração (心の支え)."
    ),
    6528: (
        "...\nQuem foi que te contou uma coisa dessas...?",
        "rewritten",
        "Vulnerabilidade e pudor de Aurica ao ver sua dor secreta exposta (誰がそんなことを...?)."
    ),
    6529: (
        "D-desculpa...\nNa verdade, quando entrei na sua Cosmosfera,\nacabei descobrindo muitas coisas sobre o seu passado.",
        "rewritten",
        "Lyner assumindo com humildade o conhecimento obtido no Mergulho (オリカのコスモスフィアの中で、色々過去のことを知ったんだ)."
    ),
    6530: (
        "Descobri que você deixou para trás o Don Leon, que era o esteio do seu coração, lá no Vilarejo de Skuwat... e que vem lutando sozinha desde então.",
        "rewritten",
        "Termos canônicos Vilarejo de Skuwat (スクワート村) e a solidão heroica de Aurica."
    ),
    6531: (
        "Por isso quis te dar este presente.\nPensei que, se você o tivesse por perto,\ntalvez pudesse te devolver um pouco do ânimo.",
        "rewritten",
        "Compaixão pura de Lyner desejando trazer alegria à parceira (少しでもオリカの元気に繋がればと思って)."
    ),
    6532: (
        "...Lyner...",
        "approved_as_is",
        "Sensibilidade tocada de Aurica."
    ),
    6533: (
        "Ter um esteio para o coração é algo essencial.\nSó de saber que temos esse apoio, a nossa coragem\nse multiplica e dá forças para seguir em frente.",
        "rewritten",
        "Visão madura de Lyner sobre apoio mútuo e coragem emocional (支えがあるだけで、やる気が何倍にもなる)."
    ),
    6534: (
        "Eu só espero... conseguir ser um apoio para você\ntanto quanto o Don Leon é.",
        "rewritten",
        "Voto íntimo de Lyner de tornar-se o guardião protetor dela (どんすけと同じくらいオリカの支えになれれば)."
    ),
    6535: (
        "Eu também... Eu só vivo te dando trabalho,\nmas tenho fé de que, um dia... também possa\nme tornar um esteio para o seu coração, Lyner...",
        "rewritten",
        "Reciprocidade profunda de Aurica aspirando a apoiá-lo (いつかは...ライナーの心の支えになれれば)."
    ),
    6536: (
        "Aurica, você já é um esteio imenso para mim.",
        "rewritten",
        "Reconhecimento imediato e caloroso de Lyner (オリカは十分、俺の心の支えになってくれてるよ)."
    ),
    6537: (
        "Muito obrigado por estar sempre comigo.\nTer você ao meu lado me dá tanta força...\nContinuo contando com você daqui em diante!",
        "rewritten",
        "Correção essencial do gênero de Lyner ('Muito obrigado' masculino) e calor afetivo fraterno."
    ),
    6538: (
        "...Muito obrigada...\nVou cuidar deste Don Leon que você fez\ncom todo o carinho do mundo.",
        "rewritten",
        "Gratidão eterna e carinho de Aurica pelo presente artesanal (ライナーのどんすけも、大切にするね)."
    ),
    6539: (
        "...",
        "rewritten",
        "Pausa silenciosa de observação."
    ),
    6540: (
        "(Ela não pareceu lá muito alegre...\nSerá que eu agi certo?...)",
        "rewritten",
        "Dúvida autocrítica cômica de Lyner sobre a reação comedida dela (あまり嬉しそうじゃなかったけど、これで良かったのかな)."
    ),
    6541: (
        "(Por enquanto, o melhor é voltar\npara a Cosmosfera dela.)",
        "rewritten",
        "Decisão de retornar ao Mergulho na mente de Aurica (とりあえず、コスモスフィアに戻ってみよう)."
    ),

    # Event/425.evd (IDs 6542 - 6556)
    6542: (
        "Krusche...?",
        "approved_as_is",
        "Abordagem atenta de Lyner."
    ),
    6543: (
        "Ah, é você, Lyner.",
        "rewritten",
        "Saudação casual e cúmplice de Krusche (ああ、ライナーか)."
    ),
    6544: (
        "As aeronaves de Platina decolam\nde um lugar desses, hein...",
        "rewritten",
        "Termo aeronave (飛空挺) e observação da pista de decolagem de Platina."
    ),
    6545: (
        "Vai muito além do nosso senso comum lá embaixo...",
        "rewritten",
        "Contraste entre a engenharia do Mundo Superior e Inferior (ボク達の常識を遙かに超えている)."
    ),
    6546: (
        "Você ama mesmo construir aeronaves, né, Krusche?",
        "rewritten",
        "Percepção afetuosa de Lyner sobre a vocação da amiga (本当に飛空挺が好きなんだな)."
    ),
    6547: (
        "...Pois é.\nQuando me dei conta, já tinha virado esse tipo de mulher.",
        "rewritten",
        "Autoaceitação descontraída e feminina de sua identidade de mecânica (いつの間にか、こんな女になっちゃったみたい)."
    ),
    6548: (
        "Pensar que, no começo, eu só construía aeronaves para poder ir atrás do Luke...",
        "rewritten",
        "Memória íntima do amor de juventude por Luke (ルークを追いかけるために)."
    ),
    6549: (
        "...Pensando bem, nós cruzamos a Blastline, mas... não encontramos nenhuma pista dele.",
        "rewritten",
        "Termo canônico Blastline e a delicadeza de Lyner sobre a ausência de pistas."
    ),
    6550: (
        "Cruzamos, sim, mas... também não tivemos\ntempo nenhum para procurar, né?",
        "rewritten",
        "Pragmatismo lúcido de Krusche aliviando a culpa do grupo (探す暇なんて無かったでしょ)."
    ),
    6551: (
        "É, tem toda razão.",
        "rewritten",
        "Concordância compreensiva de Lyner (そりゃそうだ)."
    ),
    6552: (
        "E além do mais... ele já deve...",
        "rewritten",
        "Suspensão dolorosa aceitando a fatalidade do destino de Luke (それにもう...彼は...)."
    ),
    6553: (
        "...",
        "rewritten",
        "Respeito ao luto e ao silêncio da amiga."
    ),
    6554: (
        "Mas quer saber? Acho que acabei me apaixonando de verdade pela construção de aeronaves em si. Ehehe.",
        "rewritten",
        "Transcendência do luto em vocação artística com riso característico Ehehe (えへへ)."
    ),
    6555: (
        "Assim que voltarmos ao Beco Vagalume, vou usar toda a experiência desta viagem para finalmente cruzar a Blastline de novo.",
        "rewritten",
        "Termos canônicos Beco Vagalume e Blastline na renovação do sonho de voar."
    ),
    6556: (
        "...E vai ser a bordo de uma aeronave\nconstruída pelas minhas próprias mãos.",
        "rewritten",
        "Juramento de orgulho profissional e independência (自分の作った飛空挺でね)."
    ),

    # Event/6.evd (IDs 6557 - 6561)
    6557: (
        "Hã...?",
        "rewritten",
        "Despertar confuso de Lyner no chão do Mundo Inferior (ん...?)."
    ),
    6558: (
        "Isto aqui... é um lenço...",
        "rewritten",
        "Descoberta do objeto deixado pela salvadora misteriosa (これは...ハンカチ...)."
    ),
    6559: (
        "Obteve o item [Lenço]!",
        "rewritten",
        "Item canônico obtido com colchetes balanceados."
    ),
    6560: (
        "É verdade. Tinha uma garota cuidando de mim quando acordei.",
        "rewritten",
        "Lembrança dos cuidados de Aurica logo após a queda da Blastline (介抱してもらってたんだ)."
    ),
    6561: (
        "Será que ela mora por estas bandas...?",
        "rewritten",
        "Curiosidade de Lyner sobre a identidade da benfeitora (この近辺の子かな...)."
    ),

    # Event/614.evd (IDs 6562 - 6565)
    6562: (
        "Ei, Lyner... até onde será\nque esta Torre continua subindo?",
        "rewritten",
        "Contemplação monumental da Torre Ar tonelico por Misha (ねえねえ、この塔って、どこまで続いてるのかな?)."
    ),
    6563: (
        "Sei lá...\nSe nem você sabe, Misha,\neu é que não vou saber mesmo...",
        "rewritten",
        "Humor e cumplicidade entre os amigos de infância (ミシャにわからなかったら、俺にはもっとわからないな)."
    ),
    6564: (
        "O que será que tem do outro lado desta porta, né? Sei muito bem que não dá para entrar, mas dá uma curiosidade danada, não dá?",
        "rewritten",
        "Gênero feminino correto para Misha (curiosa/curiosidade danada) eliminando o erro de tradução anterior."
    ),
    6565: (
        "É verdade.",
        "rewritten",
        "Concordância calma de fechamento de cena (そうだな)."
    ),
}

# Verificação de cobertura total
missing_ids = [d["id"] for d in raw_dialogues if d["id"] not in curations]
assert not missing_ids, f"Faltam falas para curadoria: {missing_ids}"

curated_dialogues = []
lines_rewritten = 0
lines_approved_as_is = 0

for d in raw_dialogues:
    d_id = d["id"]
    cur_text, verdict, rationale = curations[d_id]
    if verdict == "rewritten":
        lines_rewritten += 1
    else:
        lines_approved_as_is += 1

    curated_entry = {
        "id": d_id,
        "event_file": d.get("event_file", ""),
        "speaker_id": d.get("speaker_id", 0),
        "speaker": d.get("speaker", ""),
        "original_jp": d.get("original_jp", ""),
        "original_en": d.get("original_en", ""),
        "current_ptbr": d.get("current_ptbr", ""),
        "curated_ptbr": cur_text,
        "verdict": verdict,
        "rationale": rationale
    }
    curated_dialogues.append(curated_entry)

# Destaques editoriais
highlights = [
    {
        "id": 6359,
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "description": "Urgência dramática de salvar Leila: Lyner rejeita adiar a conversa com Misha ('Amanhã... já vai ser tarde demais!'), quebrando o protocolo ritual para intervir no destino da mente."
    },
    {
        "id": 6373,
        "speaker": "Reyvateil da Cosmosfera (Misha)",
        "description": "Descoberta metafísica da simulação: Misha intui que seu mundo mental foi invadido por uma 'Ameaça do Mundo Exterior', deduzindo a existência de uma realidade operando acima de sua própria criação."
    },
    {
        "id": 6387,
        "speaker": "Aurica",
        "description": "Preservação estrita de instrução de combate: manutenção exata do comando de botão IM03 para seleção de táticas na interface de batalha."
    },
    {
        "id": 6400,
        "speaker": "Misha",
        "description": "Vulnerabilidade e intimidade do Mergulho: Misha expressando o nervosismo genuíno e sagrado de abrir a alma a Lyner na Loja de Mergulho, diferenciando sua hesitação de rejeição."
    },
    {
        "id": 6424,
        "speaker": "Shurelia",
        "description": "Revelação cosmológica da tecnologia de levitação: Shurelia esclarece que o Beco Vagalume flutua graças ao Grathmeld mantido pelo Silver Horn, louvando o gênio dos habitantes de Horus."
    },
    {
        "id": 6442,
        "speaker": "Personagem [65] (Comerciante de Platina)",
        "description": "Humor de infância em Platina: o lojista provocando Lyner como o 'herdeirinho mimado do Comandante Supremo' e presenteando-o com o [Doce Famoso Funbun]."
    },
    {
        "id": 6460,
        "speaker": "Personagem [154] (Eizel)",
        "description": "Homenagem canônica à série Atelier: estreia da alquimista Eizel zombando da ambição de Elie de criar um Meteoro para caçar dragões e enviando Lyner ao Planalto Oriental para buscar um Fragmento de Estrela."
    },
    {
        "id": 6480,
        "speaker": "Personagem [154] (Eizel)",
        "description": "Referência clássica à Taverna Pavilhão Alado (飛翔亭 / Hishotei): sugestão de recrutar guarda-costas aventureiros em frente ao castelo para a expedição alquímica."
    },
    {
        "id": 6497,
        "speaker": "Moradora do Mundo Inferior (Hama)",
        "description": "Guarda solene do Código Hymmnos: Hama repreendendo Lyner e ensinando que o código de uma Reyvateil é a chave privada de seu coração, exigindo alcance do Nível 4 da Cosmosfera."
    },
    {
        "id": 6513,
        "speaker": "Oficial da Igreja (Presidente Ayano)",
        "description": "Correção de erro crasso da NISA e conspiração da Tenba: Ayano confirmando que os dados confidenciais de Bourd continuam soterrados na Placa Hexagonal e concedendo autorização exclusiva a Lyner."
    },
    {
        "id": 6530,
        "speaker": "Lyner",
        "description": "Cura afetiva e o esteio do coração: Lyner presenteia Aurica com um Don Leon esculpido por suas mãos para curar as feridas do orfanato de Skuwat, selando apoio mútuo incondicional."
    },
    {
        "id": 6548,
        "speaker": "Krusche",
        "description": "Superação do luto por Luke: Krusche confessa no hangar de Platina que sua busca por Luke tornou-se uma paixão genuína por construir aeronaves para cruzar a Blastline com as próprias mãos."
    },
    {
        "id": 6564,
        "speaker": "Misha",
        "description": "Contemplação sublime da Torre: Misha e Lyner fitando os portões selados da superestrutura de Ar tonelico imaginando o infinito além das nuvens."
    }
]

# Novos termos identificados
new_terms = {
    "Fragmento de Estrela": {
        "pt": "Fragmento de Estrela",
        "category": "Item / Alquimia",
        "note": "星のかけら / Star Piece. Mineral estelar cadente colhido no Planalto Oriental para a síntese do Meteoro."
    },
    "Meteoro": {
        "pt": "Meteoro",
        "category": "Item / Alquimia",
        "note": "メテオール / Meteor. Poderosa bomba alquímica sintetizada por Elie com auxílio de Eizel na Academia."
    },
    "Pavilhão Alado": {
        "pt": "Pavilhão Alado",
        "category": "Local / Taverna",
        "note": "酒場「飛翔亭」 / Hishotei Tavern. Tradicional taverna da franquia Atelier onde se contratam aventureiros e mercenários."
    },
    "Doce Famoso Funbun": {
        "pt": "Doce Famoso Funbun",
        "category": "Item / Alimento",
        "note": "銘菓オボンヌ / Funbun. Famosa iguaria doce tradicional de Platina, adorada compulsivamente por Lyner."
    },
    "Lenço": {
        "pt": "Lenço",
        "category": "Item / Memória",
        "note": "ハンカチ / Handkerchief. Lenço deixado por Aurica ao socorrer Lyner ferido após sua queda no Mundo Inferior."
    }
}

# Matriz de tratamento atualizada
updated_address_matrix = {
    "Eizel": {
        "Lyner": "Tratamento impaciente, mordaz e severo ('você'), tratando-o como desastrado ('cabeça-dura') mas demonstrando generosidade relutante ao acompanhá-lo.",
        "Elie": "Tratamento de veterana exigente e carinhosa com a colega ('aquela desastrada sem cura')."
    },
    "Ayano": {
        "Lyner": "Tratamento nobre, cerimonioso e respeitoso ('Sir Lyner', 'Lyner'), com profunda dívida de honra e concessão de privilégios executivos da Tenba."
    },
    "Krusche": {
        "Lyner": "Tratamento de extrema confiança e intimidade fraterna ('você'), abrindo seu coração sobre o luto por Luke e o sonho de cruzar a Blastline.",
        "Ayano": "Tratamento profissional corporativo como chefe do Projeto Shoga diante da Presidente da Tenba."
    },
    "Aurica": {
        "Lyner": "Tratamento tímido, comovido e vulnerável ('você'), aceitando o Don Leon artesanal como símbolo de que ele agora é seu esteio emocional."
    },
    "Hama": {
        "Lyner": "Tratamento desconfiado, implacável e instrutivo ('você', 'seu palerma'), zelando ferozmente pelo Código Hymmnos e pela honra de Misha."
    }
}

# Scene handoff final
scene_handoff_final = {
    "resumo_dramatico": "A revelação metafísica no Nível profundo da Cosmosfera onde Misha intui que seu mundo é simulado e controlado pela 'Ameaça do Mundo Exterior'; o reencontro desajeitado na Loja de Mergulho com Misha pedindo tempo para preparar a alma e o atendente elogiando a pureza de Lyner; as lições de Shurelia sobre a sustentação do Beco Vagalume pelo poder fônico do Silver Horn em contraste com o gênio construtivo de Horus; as memórias de infância de Lyner em Platina sendo caçoado pelo dono da mercearia como o 'herdeirinho do Comandante Supremo' e ganhando seu amado Funbun; o crossover histórico com o universo Atelier na Academia com a estreia da tsundere Eizel ajudando Lyner com a receita do Meteoro e rumando ao Planalto Oriental; as duras lições morais de Hama em defesa do segredo do Código Hymmnos de Misha exigindo a conquista do Nível 4 da Cosmosfera; a solene audiência com a Presidente Ayano da Tenba concedendo passe livre para investigar o laboratório soterrado de Bourd na Placa Hexagonal; o momento de intimidade sublime em que Lyner presenteia Aurica com um Don Leon esculpido por suas mãos para curar seu passado em Skuwat; o desabafo maduro de Krusche nas docas de Platina superando o luto por Luke ao descobrir sua verdadeira paixão em cruzar a Blastline em sua própria aeronave; a recordação do lenço de Aurica no despertar de Lyner após a queda do céu; e a contemplação de Lyner e Misha diante dos portões insondáveis da superestrutura de Ar tonelico.",
    "decisoes_terminologicas": {
        "Projeto Shoga": "[Projeto Shoga] (プロジェクト『翔雅』, projeto aeronáutico liderado por Krusche na Tenba)",
        "Planalto Oriental": "[Planalto Oriental] (東の台地, região ao leste onde caem os Fragmentos de Estrela)",
        "Fragmento de Estrela": "[Fragmento de Estrela] (星のかけら, mineral estelar cadente)",
        "Meteoro": "[Meteoro] (メテオール, potente explosivo alquímico)",
        "Pavilhão Alado": "[Pavilhão Alado] (酒場「飛翔亭」, taverna onde se contratam aventureiros)",
        "Doce Famoso Funbun": "[Doce Famoso Funbun] (銘菓オボンヌ, doce típico favorito de Platina)",
        "Silver Horn": "Silver Horn (シルヴァホルン, instalação ancestral de ressonância da Torre)",
        "Lenço": "[Lenço] (ハンカチ, objeto de Aurica resgatado na queda da Blastline)",
        "Ameaça do Mundo Exterior": "Ameaça do Mundo Exterior (外界からの脅威, intuição filosófica de Misha)"
    },
    "alertas_para_proximo_bloco": "Atenção ao avanço na exploração dos dados confidenciais de Bourd no laboratório da Placa Hexagonal, aos preparativos para a expedição ao Planalto Oriental e à progressão no Nível 4 da Cosmosfera de Misha para o resgate definitivo de seu Código Hymmnos com Hama."
}

output_data = {
    "block_id": "BLK_EVD_025",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "total_lines": len(curated_dialogues),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "highlights": highlights,
    "new_terms": new_terms,
    "updated_address_matrix": updated_address_matrix,
    "scene_handoff": scene_handoff_final,
    "dialogues": curated_dialogues
}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Sucesso! Gravado {OUTPUT_PATH.name} com {len(curated_dialogues)} falas ({lines_rewritten} reescritas, {lines_approved_as_is} aprovadas).")

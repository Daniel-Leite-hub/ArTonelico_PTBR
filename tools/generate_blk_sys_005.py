import json
import sqlite3
import sys
from pathlib import Path

tools_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(tools_path))
sys.path.append(str(tools_path / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

# Carregar dados brutos
scratch_path = tools_path / "curadoria_editorial" / "blocos" / "scratch_sys_005.json"
with open(scratch_path, "r", encoding="utf-8") as f:
    raw_items = json.load(f)

curated_dict = {
    # File 0051 (21459..21482)
    21459: ("Pague!", "JP 金勘定に容赦なし (Krusche; 13B <= 16B; mantido conciso e imperativo de cobrança sem fiado)"),
    21460: ("Engenheira de Grathmeld moradora do Beco Vagalume. Tem vasto saber sobre aeronaves e itens Grath. Cresceu solta numa família grande, tem tiradas irônicas afiadas e é implacável com dinheiro.", "JP ほたる横丁に住むグラスメイクのエンジニア (Krusche; 366B <= 440B; restaura nuances de tirada afiada e rigor financeiro)"),
    21461: ("PC: Krusche", "JP 人C:クルシェ (Person Card Krusche; 23B <= 24B; paridade canônica com PC)"),
    21462: ("Radolf", "JP ラードルフ (Radolf; 13B <= 16B; nome mantido)"),
    21463: ("Vila Karulu", "JP カルル村 (Karulu Village; 23B <= 32B; topônimo canônico)"),
    21464: ("Sacerdote", "JP 教会の神官戦士 (21B <= 24B; restaura神官戦士 da Igreja de Elemia em vez de Cardeal ocidentalizado)"),
    21465: ("24 anos", "JP 24歳 (24 anos; 15B <= 24B; mantido)"),
    21466: ("Sorrisos e bem", "JP 人々の笑顔、正義 (Likes Radolf; 29B <= 32B; soluciona overflow de 36B em 32B mantendo o apreço aos sorrisos e à retidão/bem do povo)"),
    21467: ("Mal, Tenba", "JP 悪、天覇 (Dislikes Radolf; 21B <= 24B; mantido)"),
    21468: ("Criar um mundo pacífico", "JP 平和な世界を築く事 (Sonho Radolf; 46B <= 48B; mantido)"),
    21469: ("Proteger a paz", "JP 平和を守ること (Hobby Radolf; 29B <= 48B; mantido)"),
    21470: ("Seja homem de palavra!", "JP 有言実行 (Lema Radolf; 45B <= 48B; cumprir o que promete)"),
    21471: ("Habitante do Mundo Inferior e cardeal da Igreja de Elemia. Seu talento nato com a espada o alçou ao posto supremo de sacerdote-guerreiro em apenas cinco anos, recebendo como parceira a RT Fayma. Nunca se deu bem com o bispo Falss.", "JP 塔の下層世界の住民で、エル・エレミア教会の神官戦士 (Perfil Radolf; 436B <= 480B; restaura títulos e dinâmica com Falss)"),
    21472: ("PC: Radolf", "JP 人C:ラードルフ (Person Card Radolf; 21B <= 24B)"),
    21473: ("Ayatane", "JP 絢胤(アヤタネ) (Ayatane; 15B <= 16B)"),
    21474: ("Altar dos Apóstolos", "JP 使徒の祭壇 (Altar of Apostles; 39B <= 40B)"),
    21475: ("Aparenta 19", "JP 19歳相当 (32B limit; soluciona overflow de 33B para 23B <= 32B com paridade canônica)"),
    21476: ("Dados, Funbuns", "JP 情報世界、オボンヌ (Likes Ayatane; soluciona overflow de 47B em 40B; 29B <= 40B com fidelidade a 情報世界 e Funbuns)"),
    21477: ("Tumulto, brigas", "JP 人混み、喧嘩 (Dislikes Ayatane; soluciona overflow de 36B em 32B; 31B <= 32B; tumulto de multidões e brigas)"),
    21478: ("Ação confiável", "JP 信頼される行動 (Objetivo Ayatane; 29B <= 40B)"),
    21479: ("Cozinha", "JP 料理 (Hobby Ayatane; soluciona overflow de 17B em 16B; 15B <= 16B)"),
    21480: ("Lealdade à missão!", "JP 使命は忠実にこなす (Lema Ayatane; 37B <= 48B; fidelidade à missão recebida)"),
    21481: ("Cavaleiro de Elemia da mesma turma de Lyner, mas na verdade um vírus enviado por Mir para dominar o coração de Shurelia. Antes de se revelar, agia como um jovem cortês, sorridente e exemplar.", "JP ライナーと同期のエレミアの騎士だが (Perfil Ayatane; 385B <= 408B; restaura a sutileza do disfarce de aluno exemplar)"),
    21482: ("PC: Ayatane", "JP 人C:アヤタネ (Person Card Ayatane; 23B <= 24B)"),

    # File 0052 (21483..21506)
    21483: ("Shurelia", "JP シュレリア (Shurelia; 17B <= 24B)"),
    21484: ("Rinkernator", "JP リンカーネイション (Rinkernator / Reincarnation; 23B <= 24B)"),
    21485: ("Senhora da Torre", "JP 塔の管理者 (Shurelia; soluciona overflow de 47B em 40B; 33B <= 40B com reverência e nobreza divina)"),
    21486: ("Milhares de anos", "JP 何千歳 (Shurelia; soluciona overflow de 47B em 40B; 33B <= 40B)"),
    21487: ("ELMA", "JP ELMA、カラク (Likes Shurelia; 9B <= 16B)"),
    21488: ("ELMA-DS", "JP ELMA-DS (Dislikes Shurelia; 15B <= 16B)"),
    21489: ("Ser recém-casada", "JP 新婚生活 (Sonho Shurelia; soluciona overflow de 44B em 40B; 35B <= 40B; doce aspiração conjugal)"),
    21490: ("Comer doces", "JP 甘い物の食べ歩き (Hobby Shurelia; 23B <= 32B)"),
    21491: ("Quero ser livre!", "JP 身軽になりたい (Lema Shurelia; 33B <= 40B)"),
    21492: ("Sem a armadura pesada, seus verdadeiros sentimentos reprimidos vêm à tona. É carente, detesta a solidão e, ao revelar seu lado íntimo, mostra uma faceta surpreendentemente mimada e dengosa que pega qualquer um de surpresa.", "JP 装甲を外した状態 (Perfil Shurelia A; 437B <= 464B; resgata a doçura e dengosidade do JP 甘えたがり・ワガママ)"),
    21493: ("PC: Shurelia A", "JP 人C:シュレリアA (Person Card Shurelia A; 27B <= 32B)"),
    21494: ("Claire", "JP クレア (Claire; 13B <= 16B)"),
    21495: ("Dona do bar", "JP ネモの酒場の店長 (Claire; 23B <= 32B)"),
    21496: ("20 anos", "JP 20歳 (Idade Claire; 15B <= 24B)"),
    21497: ("Aurica, realejos", "JP オリカ、オルゴール (Likes Claire; soluciona overflow de 47B em 40B; 33B <= 40B; オルゴール = realejos/caixas musicais)"),
    21498: ("Abusar do canto", "JP 詩を利用する人達 (Dislikes Claire; soluciona overflow de 45B em 32B; 31B <= 32B; aversão a quem abusa das canções sagradas)"),
    21499: ("Cantar para 10 mil", "JP 一万人の前で謳う (Sonho Claire; soluciona overflow de 53B em 48B; 37B <= 48B)"),
    21500: ("Cantar", "JP 謳うこと (Hobby Claire; 13B <= 16B)"),
    21501: ("Canções pelo povo!", "JP 詩は庶民の為に (Lema Claire; soluciona overflow de 52B em 48B; 39B <= 48B; restaura o JP 詩は庶民の為に apagado no EN)"),
    21502: ("Jovem que comanda a taverna de Nemo. Reyvateil sem laços com a Tenba ou a Igreja, entoa canções de cura aos clientes. Vinda do Vilarejo Skuwat assim como Aurica, sempre cuidou dela como irmã caçula.", "JP ネモの酒場を切り盛りするお姉さん (Perfil Claire; 400B <= 456B; aprofunda vínculos de afeto fraternal com Aurica)"),
    21503: ("PC: Claire", "JP 人C:クレア (Person Card Claire; 21B <= 24B)"),
    21504: ("Leard", "JP レアード (Leard; 11B <= 16B)"),
    21505: ("Comandante", "JP プラティナ総帥 (Leard; 21B <= 24B)"),
    21506: ("58 anos", "JP 58歳 (Idade Leard; 15B <= 24B)"),

    # File 0053 (21507..21530)
    21507: ("Política, ciência", "JP 人との交流、音科学 (Likes Leard; 38B <= 40B)"),
    21508: ("Esgrima, frio", "JP 剣術、寒いの (Dislikes Leard; 27B <= 40B)"),
    21509: ("Erradicar os vírus", "JP 世界からバグを消す (Sonho Leard; soluciona overflow de 50B em 48B; 39B <= 48B)"),
    21510: ("Xadrez", "JP チェス (Hobby Leard; 13B <= 16B)"),
    21511: ("Filho como sucessor!", "JP 息子を跡継ぎに (Lema Leard; soluciona overflow de 49B em 48B; 41B <= 48B; herança política)"),
    21512: ("Comandante de Platina e pai de Lyner. Galgou velozmente a hierarquia política até consolidar seu poder. Quer fazer de Lyner seu sucessor legítimo, mas o rapaz não tem o menor interesse, gerando atritos constantes.", "JP プラティナの総帥であり、ライナーの父親 (Perfil Leard; 431B <= 472B; dinâmica severa e autoritária de pai e governante)"),
    21513: ("PC: Leard", "JP 人C:レアード (Person Card Leard; 19B <= 24B)"),
    21514: ("Lyra", "JP リルラ (Lyra; 9B <= 16B)"),
    21515: ("Caçadora de itens", "JP 塔探索代行 (Lyra; 37B <= 40B)"),
    21516: ("Aparenta 13", "JP 13歳(外見) (Lyra; soluciona overflow de 27B em 24B; 23B <= 24B)"),
    21517: ("Gatos, coletar itens", "JP ねこ、アイテム集め (Likes Lyra; 43B <= 48B)"),
    21518: ("Ser tratada como criança", "JP 子ども扱い、獣扱い (Dislikes Lyra; 51B <= 56B)"),
    21519: ("Coleção total", "JP アイテムコンプ (Sonho Lyra; 27B <= 32B)"),
    21520: ("Encontrar itens na Torre", "JP 塔内のアイテム拾い (Hobby Lyra; 51B <= 56B)"),
    21521: ("Zero reclamações!", "JP クレーム0の仕事を (Lema Lyra; soluciona overflow de 51B em 48B; 38B <= 48B; paridade estrita com JP クレーム0)"),
    21522: ("Jovem da tribo Teru residente em Em Pheyna. Pertencente à linhagem mágica Jemina, tem o poder de se teletransportar livremente pela Torre. De tanto explorar seus meandros, fez do hábito de catar itens raros um negócio lucrativo.", "JP イム・フェーナにすむテル族の子 (Perfil Lyra; 446B <= 488B; lore da linhagem mágica Jemina e comércio de exploração)"),
    21523: ("PC: Lyra", "JP 人C:リルラ (Person Card Lyra; 17B <= 24B)"),
    21524: ("Spica", "JP スピカ (Spica; 11B <= 16B)"),
    21525: ("Doces, informante", "JP 猫飴屋、情報屋 (Spica; soluciona overflow de 53B em 40B; 35B <= 40B; vendedora de doces e informante)"),
    21526: ("25 anos", "JP 25歳 (Idade Spica; 15B <= 24B)"),
    21527: ("Dados secretos", "JP 年下の異性、闇情報 (Likes Spica; soluciona overflow de 39B em 32B; 29B <= 32B; 闇情報 = informações confidenciais)"),
    21528: ("Câmara de comércio", "JP ほたる商工会 (Dislikes Spica; 39B <= 40B)"),
    21529: ("Rainha do Submundo", "JP 表は街娘、裏は女王 (Sonho Spica; 39B <= 48B)"),
    21530: ("Coleta de segredos", "JP レア情報集め (Hobby Spica; soluciona overflow de 47B em 40B; 37B <= 40B)"),

    # File 0054 (21531..21554)
    21531: ("Nunca vender boatos!", "JP ガセネタは売らず (Lema Spica; soluciona overflow de 61B em 48B; 41B <= 48B; integridade de negociante)"),
    21532: ("Vende Bala Gatinho no Beco Vagalume, mero disfarce para o público. No submundo, atua como informante de elite e compradora clandestina, negociando segredos valiosos e Cristais Grathnode de altíssima pureza.", "JP ほたる横丁の中心商業地 (Perfil Spica; 415B <= 472B; lore profunda do comércio clandestino e fachada de doces)"),
    21533: ("PC: Spica", "JP 人C:スピカ (Person Card Spica; 19B <= 24B)"),
    21534: ("Mei Mei", "JP メイメイ (Mei Mei; 15B <= 16B)"),
    21535: ("Torre", "JP 塔 (Origem Mei Mei; 11B <= 16B)"),
    21536: ("Aia de cúpula", "JP 天文台のメイドさん (Mei Mei; soluciona overflow de 41B em 40B; 29B <= 40B; aia mecânica do Observatório)"),
    21537: ("Aparenta 17", "JP 17歳(外見) (Mei Mei; soluciona overflow de 27B em 24B; 23B <= 24B)"),
    21538: ("Dados e energia", "JP 導力、データバンク (Likes Mei Mei; soluciona overflow de 33B em 32B; 31B <= 32B; 導力 e データバンク)"),
    21539: ("Ficar sem energia", "JP バッテリー切れ (Dislikes Mei Mei; 35B <= 48B)"),
    21540: ("Rever a irmã menor", "JP 妹に会うこと (Sonho Mei Mei; soluciona overflow de 51B em 48B; 39B <= 48B)"),
    21541: ("Modo suspender", "JP 昼寝(サスペンド) (Hobby Mei Mei; soluciona overflow de 37B em 32B; 29B <= 32B; suspensão de sistema)"),
    21542: ("Acorde-me se precisar", "JP 目指せ万能メイド (Lema Mei Mei; 43B <= 48B)"),
    21543: ("Aia mecânica que serve no Observatório, ruína ancestral acima da Blastline. Autômato doméstico construído na mesma era da Torre, funciona como chave mestra de conexão ao Centro de Dados e sistema de autenticação dos serviços de segurança.", "JP ブラストレインより上にある古代遺跡 (Perfil Mei Mei; 474B <= 496B; terminologia de robótica ancestral e chaves de segurança)"),
    21544: ("PC: Mei Mei", "JP 人C:メイメイ (Person Card Mei Mei; 23B <= 24B)"),
    21545: ("Mir", "JP ミュール (Mir; 7B <= 8B)"),
    21546: ("Campo binário", "JP 塔のバイナリ情報野 (Mir; 29B <= 32B)"),
    21547: ("Exterminar humanos", "JP 人間を滅ぼすこと (Classe Mir; 39B <= 40B)"),
    21548: ("Centenas de anos", "JP 何百歳 (Idade Mir; 33B <= 40B)"),
    21549: ("Reyvateil", "JP レーヴァテイル (Raça Mir; 19B <= 24B)"),
    21550: ("Linhagem Lune", "JP リリューンとその末裔 (Origem Mir; 27B <= 32B)"),
    21551: ("Exterminar os humanos", "JP 人間を滅ぼすこと (Sonho Mir; soluciona overflow de 53B em 48B; 43B <= 48B; ódio visceral)"),
    21552: ("Criar vírus", "JP ウイルス作り (Hobby Mir; 25B <= 32B)"),
    21553: ("Por um mundo em paz", "JP 平穏な世界のために (Lema Mir; soluciona overflow de 43B em 40B; 39B <= 40B; resgata a trágica convicção pacifista distorcida do JP)"),
    21554: ("A Reyvateil mais forte da Segunda Era. Seu poder e processamento chegam a superar os de Shurelia. Criada por humanos como mera ferramenta sem direitos, jurou vingança e busca erradicar a humanidade.", "JP 第二紀に生み出された最強のRT (Perfil Mir; 398B <= 432B; restaura a tragédia de ter sido tratada como objeto sem vida)"),

    # File 0055 (21555..21578)
    21555: ("PC: Mir", "JP 人C:ミュール (Person Card Mir; 15B <= 16B)"),
    21556: ("Shurelia (Armadura)", "JP シュレリア(武装形態) (Shurelia B; 41B <= 48B)"),
    21557: ("Administradora da Torre e do continente flutuante. Criada na Primeira Era como mãe das Reyvateils, é a Origem e matriz dos tipos β puro-sangue. Cumpre a diretriz de proteger os humanos e manter o mundo.", "JP 塔の管理者で、浮遊大陸を管理している (Perfil Shurelia B; 407B <= 456B; solenidade divina e lore dos tipos β puro-sangue)"),
    21558: ("PC: Shurelia B", "JP 人C:シュレリアB (Person Card Shurelia B; 27B <= 32B)"),
    21559: ("Bourd Rade", "JP ボルド・レール (Bourd Rade; 21B <= 24B)"),
    21560: ("Nemo", "JP ネモの街 (Nemo; 9B <= 16B)"),
    21561: ("2º na Tenba", "JP 天覇のナンバー2 (Bourd; soluciona overflow de 27B em 24B; 24B <= 24B; exata paridade)"),
    21562: ("33 anos", "JP 33歳 (Idade Bourd; 15B <= 24B)"),
    21563: ("Poder, destruição", "JP 権力、破壊者 (Likes Bourd; 38B <= 40B)"),
    21564: ("Dominar o mundo", "JP 世界を牛耳ること (Sonho Bourd; 31B <= 56B)"),
    21565: ("Tramar esquemas", "JP 策略を練ること (Hobby Bourd; 31B <= 40B; resgata o JP 策略を練ること adulterado no EN)"),
    21566: ("O que é seu é meu!", "JP おまえの物は俺の物 (Lema Bourd; 41B <= 48B)"),
    21567: ("Segundo em comando da Tenba. Guerreiro brutal recrutado por sua força, conspirou com o bispo Falss para reviver a puro-sangue β Mir. Planejou matar Misha, a Cantora das Estrelas, mas, fascinado por seu poder, levou-a para a Tenba.", "JP 天覇のナンバー2で、元は屈強な戦士だったが (Perfil Bourd; 462B <= 480B; restaura ambição militar e aliança espúria com Falss)"),
    21568: ("PC: Bourd", "JP 人C:ボルド (Person Card Bourd; 19B <= 24B)"),
    21569: ("Flute", "JP フラウト (Flute; 11B <= 16B)"),
    21570: ("Chefe Teru", "JP イム・フェーナの長 (Flute; 21B <= 24B)"),
    21571: ("22 anos", "JP 22歳 (Idade Flute; 15B <= 24B)"),
    21572: ("Cello Moon", "JP チェロ月 (Likes Flute; 21B <= 24B)"),
    21573: ("Gente mesquinha", "JP 貪欲な人間、バグ (Dislikes Flute; soluciona overflow de 41B em 32B; 31B <= 32B; repulsa à ambição humana)"),
    21574: ("Buscar vasto saber", "JP 豊富な知識を得る事 (Sonho Flute; soluciona overflow de 51B em 48B; 37B <= 48B; nobre busca do saber)"),
    21575: ("Tocar alaúde", "JP リュート演奏 (Hobby Flute; 27B <= 40B)"),
    21576: ("Honrar o pacto", "JP 盟約に従い続ける (Lema Flute; soluciona overflow de 41B em 32B; 29B <= 32B; fidelidade à aliança de Elemia)"),
    21577: ("Líder supremo dos Teru em Em Pheyna. Conforme o Juramento de Elemia, vigia a Crônica Crescente, protege a Cantora das Estrelas e barra a passagem dos povos inferiores. Nutre devoção por Tastiella, a quem sempre consulta em momentos cruciais.", "JP イム・フェーナの長。エレミア誓約書の盟約通り (Perfil Flute; 484B <= 496B; gravidade do juramento ancestral e tutela de Misha)"),
    21578: ("PC: Flute", "JP 人C:フラウト (Person Card Flute; 19B <= 24B)"),

    # File 0056 (21579..21602)
    21579: ("Tastiella", "JP タスティエーラ (Tastiella; 19B <= 24B)"),
    21580: ("Guardiã", "JP フェーナ門の門番 (Tastiella; soluciona overflow de 38B em 24B; 16B <= 24B; guardiã do portão)"),
    21581: ("Aparenta 16", "JP 16歳(外見) (Tastiella; 23B <= 40B)"),
    21582: ("Magia, Niji, Sue", "JP 魔法、ニジ、スゥ (Likes Tastiella; 33B <= 40B)"),
    21583: ("Tempo infinito", "JP 終わらない刻 (Dislikes Tastiella; 29B <= 32B)"),
    21584: ("Não ser necessária", "JP 自分が必要ない世界 (Sonho Tastiella; 39B <= 40B)"),
    21585: ("Brincar com Niji e Sue", "JP ニジとスゥと遊ぶ (Hobby Tastiella; 49B <= 56B)"),
    21586: ("Não me chame de vovó", "JP 私はオババではない (Lema Tastiella; 44B <= 48B; repulsa a ser chamada de velha)"),
    21587: ("Guarda o Portão de Pheyna e zela pelo Olho de Gelo, mas é na verdade uma heroína lendária que selou Mir ao lado de Shurelia. Transferiu sua alma para a Crônica Crescente e resiste há séculos. No passado, era alegre e cheia de inocência.", "JP フェーナ門の門番、氷の瞳の維持管理 (Perfil Tastiella; 465B <= 488B; sacrifício da alma e luto pelo selamento de Mir)"),
    21588: ("PC: Tastiella", "JP 人C:タスティエーラ (Person Card Tastiella; 27B <= 32B)"),
    21589: ("Ayano", "JP 亜耶乃 (Ayano; 11B <= 16B)"),
    21590: ("Presidente", "JP 天覇の総帥 (Ayano; 21B <= 24B)"),
    21591: ("36 anos", "JP 36歳 (Idade Ayano; 15B <= 24B)"),
    21592: ("Aventuras", "JP 冒険、豪儀なヤツ (Likes Ayano; 19B <= 24B)"),
    21593: ("Papelada", "JP 経理、ハンコ押し (Dislikes Ayano; 17B <= 24B)"),
    21594: ("Voar numa aeronave", "JP 飛空挺で旅に出る事 (Sonho Ayano; 37B <= 48B)"),
    21595: ("Achar diversão", "JP 面白いこと探し (Hobby Ayano; soluciona overflow de 33B em 32B; 31B <= 32B)"),
    21596: ("Honrar o acordo", "JP 信頼関係第一 (Lema Ayano; 31B <= 32B)"),
    21597: ("Presidente do Conglomerado Tenba. Farta do tédio burocrático, caça novidades pela sede e adora o Prato Dokkoi do bar do Beco Vagalume. Detesta contabilidade, mas é brilhante na arte de negociar e cativar pessoas.", "JP 複合企業集団天覇の総帥 (Perfil Ayano; 429B <= 472B; personalidade carismática e avessa à burocracia corporativa)"),
    21598: ("PC: Ayano", "JP 人C:亜耶乃 (Person Card Ayano; 19B <= 24B)"),
    21599: ("Bispo Falss", "JP ファルス司祭 (Falss; 23B <= 32B)"),
    21600: ("Bispo da Igreja", "JP 教会の教皇 (Falss; soluciona overflow de 33B em 32B; 31B <= 32B)"),
    21601: ("72 anos", "JP 72歳 (Idade Falss; 15B <= 24B)"),
    21602: ("Ciência antiga", "JP ロストテクノロジー (Likes Falss; soluciona overflow de 39B em 32B; 31B <= 32B; tecnologia ancestral perdida)"),

    # File 0057 (21603..21626)
    21603: ("Amarras, os Teru", "JP 縛られること、テル (Dislikes Falss; soluciona overflow de 43B em 40B; 33B <= 40B; ódio a restrições e aos Teru)"),
    21604: ("Criar estratégias", "JP 方策を練ること (Sonho Falss; 38B <= 48B)"),
    21605: ("Banir oposição", "JP 自分に邪魔者は追放 (Lema Falss; 32B <= 40B)"),
    21606: ("Bispo da Igreja de Elemia à frente das paróquias de Nemo e dos continentes flutuantes. Antigo comandante de Platina sob o nome Kyle Clancy, foi desmascarado ao tentar reviver Mir, fugindo por pouco da morte ao Mundo Inferior.", "JP エル・エレミア教会の司祭 (Perfil Falss; 453B <= 488B; revelação da identidade de Kyle Clancy e planos de heresia)"),
    21607: ("PC: Falss", "JP 人C:ファルス司祭 (Person Card Falss; 19B <= 24B)"),
    21608: ("Garzburn", "JP ガルツベルン (Garzburn; 17B <= 24B)"),
    21609: ("Ninho do Draco", "JP 龍の巣 (Garzburn; soluciona overflow de 34B em 32B; 29B <= 32B; topônimo canônico da Blastline)"),
    21610: ("Antiquário", "JP 骨董ブローカー (Garzburn; soluciona overflow de 49B em 32B; 24B <= 32B; corretor de antiguidades raras)"),
    21611: ("Pessoas fortes", "JP 強いやつ (Likes Garzburn; 31B <= 32B)"),
    21612: ("Os fracos", "JP 弱いやつ (Dislikes Garzburn; soluciona overflow de 29B em 24B; 19B <= 24B; desprezo por fraqueza)"),
    21613: ("Um mundo cheio de monstros", "JP 魔物だらけの世界 (Sonho Garzburn; 55B <= 56B)"),
    21614: ("Enganar monstros fortes", "JP 強い怪物のねつ造 (Hobby Garzburn; 47B <= 48B)"),
    21615: ("Só os fortes sobrevivem", "JP 弱肉強食 (Lema Garzburn; 47B <= 48B)"),
    21616: ("Dragão que vive no Ninho do Draco, na Blastline. Comercializa antiguidades recolhidas em ruínas ancestrais. Entre seus achados, ocultam-se relíquias incríveis...", "JP ブラストラインにある龍の巣に住むドラゴン (Perfil Garzburn; 327B <= 344B; tom sarcástico de mascate mítico da Blastline)"),
    21617: ("PC: Garzburn", "JP 人C:ガルツベルン (Person Card Garzburn; 25B <= 32B)"),
    21618: ("Destruir humanos", "JP 人間を滅ぼすこと (Objetivo ELMA-DS; 33B <= 40B)"),
    21619: ("Vírus", "JP ウイルス (Raça ELMA-DS; 13B <= 16B)"),
    21620: ("Pessoas", "JP 人類 (Dislikes ELMA-DS; 15B <= 16B)"),
    21621: ("Erradicar pessoas", "JP 人類の根絶やし (Sonho ELMA-DS; 35B <= 40B)"),
    21622: ("Hacking", "JP ハッキング (Hobby ELMA-DS; soluciona overflow de 17B em 16B; 15B <= 16B; paridade com JP)"),
    21623: ("Ordens primeiro", "JP 命令第一 (Lema ELMA-DS; 31B <= 32B)"),
    21624: ("Vírus programado por Mir à imagem do autômato ELMA de Shurelia. Tem funções idênticas e conversão flip-flop, sendo capaz de invadir e corromper qualquer sistema movido a energia sinfônica.", "JP ミュールによってプログラムされたウイルス (Perfil ELMA-DS; 383B <= 400B; terminologia de cibersegurança e espelhamento corrompido)"),
    21625: ("PC: ELMA-DS", "JP 人C:ELMA-DS (Person Card ELMA-DS; 23B <= 24B)"),
    21626: ("Elma", "JP エルマ (Elma; 9B <= 16B)"),

    # File 0058 (21627..21650)
    21627: ("Guarda da Torre", "JP 塔のガーディアン (Elma; soluciona overflow de 36B em 32B; 31B <= 32B)"),
    21628: ("Vírus", "JP ウイルス (Dislikes Elma; 13B <= 16B)"),
    21629: ("Virar pet de colo", "JP 室内用ペットになる (Sonho Elma; soluciona overflow de 63B em 48B; 35B <= 48B; desejo infantil de ser bicho de colo de Shurelia)"),
    21630: ("Adular Shurelia", "JP シュレリアに甘える (Hobby Elma; 31B <= 40B)"),
    21631: ("Torre segura", "JP 塔内安全 (Lema Elma; soluciona overflow de 37B em 32B; 25B <= 32B)"),
    21632: ("O guardião supremo concebido por Shurelia. A exemplo de sua mestra de armadura, assume uma postura feroz para patrulhar a Torre. No entanto, nas horas vagas, corre para receber dengos e carinho de Shurelia, um guardião travesso e apegado.", "JP シュレリアの作り出した最強の塔のガーディアン (Perfil Elma; 479B <= 480B; contraste cômico entre ferocidade em combate e dengo infantil)"),
    21633: ("PC: ELMA", "JP 人C:ELMA (Person Card ELMA; 17B <= 24B)"),
    21634: ("Noelle", "JP ナール (Noelle; 13B <= 16B)"),
    21635: ("Lojista", "JP 雑貨屋の店主 (Noelle; 15B <= 24B)"),
    21636: ("Avô", "JP 祖父 (Likes Noelle; 10B <= 16B)"),
    21637: ("Piadas do avô", "JP 祖父のツッコミ (Dislikes Noelle; 26B <= 32B)"),
    21638: ("Uma bela anfitriã", "JP 美人女将 (Sonho Noelle; 37B <= 40B)"),
    21639: ("Novos cardápios", "JP 新メニューの開発 (Hobby Noelle; soluciona overflow de 47B em 40B; 33B <= 40B)"),
    21640: ("Sempre ser alegre", "JP 常に明るく元気良く (Lema Noelle; 35B <= 40B)"),
    21641: ("Dona da loja Guardião da Torre no Vilarejo Karulu. Vive chamando o avô Pochoma de 'velho ranzinza', mas mudou-se para a vila só para cuidar de sua velhice. No fundo, zela por ele com imenso carinho.", "JP カルル村にあるタワーガーディアンの店主 (Perfil Noelle; 400B <= 448B; afeição genuína escondida sob broncas cotidianas)"),
    21642: ("PC: Noelle", "JP 人C:ナール (Person Card Noelle; 21B <= 24B)"),
    21643: ("Sr. Pochoma", "JP ポチョマー先生 (Pochoma; 23B <= 24B)"),
    21644: ("Mestre Grathmelder", "JP 元高名なメルク (Pochoma; soluciona overflow de 47B em 40B; 37B <= 40B; título honroso de sintetizador lendário)"),
    21645: ("76 anos", "JP 76歳 (Idade Pochoma; 15B <= 24B)"),
    21646: ("Grathmeld, neta", "JP グラスメルク、孫 (Likes Pochoma; 33B <= 40B)"),
    21647: ("Passear", "JP 動くこと (Dislikes Pochoma; 15B <= 32B)"),
    21648: ("Manter a rotina", "JP 今の生活を続ける (Sonho Pochoma; soluciona overflow de 35B em 32B; 31B <= 32B)"),
    21649: ("Olhar o vazio", "JP 店の隅でボンヤリ (Hobby Pochoma; 29B <= 40B)"),
    21650: ("Impossível!", "JP あり得ん! (Lema Pochoma; 24B <= 24B; encaixe perfeito)"),

    # File 0059 (21651..21674)
    21651: ("Grathmelder lendário de renome mundial. Compartilha sua vasta sabedoria com quem pede, mas anda um tanto caduco. Vive zombando da neta Noelle, irritando a jovem e arrumando confusão.", "JP 高名なメルクとして名を知られる人 (Perfil Pochoma; 346B <= 384B; velhice excêntrica e sabedoria alquímica)"),
    21652: ("PC: Pochoma", "JP 人C:ポチョマー (Person Card Pochoma; 23B <= 24B)"),
    21653: ("Garota da Tenba", "JP 天覇の娘 (Tenba Girl; soluciona overflow de 41B em 40B; 31B <= 40B)"),
    21654: ("Tenba", "JP 天覇 (Tenba; 11B <= 16B)"),
    21655: ("Ser tratada como pessoa", "JP 人として扱われたい (Sonho Moça Tenba; 51B <= 56B)"),
    21656: ("Falar com Aloe", "JP アロエに話しかける (Hobby Moça Tenba; soluciona overflow de 39B em 32B; 29B <= 32B)"),
    21657: ("Ainda tenho sorte...", "JP 自分はまだ幸せな方 (Lema Moça Tenba; 41B <= 56B; resignação dolorosa)"),
    21658: ("Reyvateil a serviço da Tenba. Foi salva por Radolf no Vilarejo Karulu ao ser espancada por um comandante da corporação. Embora sonhe em desertar desde então, segue presa à empresa, submetida a constantes humilhações.", "JP 天覇所属のRT。カルル村で天覇の指揮官に (Perfil Moça Tenba; 418B <= 440B; denúncia da exploração de Reyvateils descartáveis pela Tenba)"),
    21659: ("PC: Moça Tenba", "JP 人C:天覇の娘 (Person Card Tenba Girl; 29B <= 32B)"),
    21660: ("Don Leon", "JP どんすけ (Don Leon; 17B <= 24B)"),
    21661: ("Alma de Aurica", "JP オリカの精神世界 (Don Leon; soluciona overflow de 51B em 40B; 29B <= 40B; Cosmosfera de Aurica)"),
    21662: ("Guia da alma", "JP 精神世界の案内人 (Don Leon; soluciona overflow de 34B em 32B; 25B <= 32B; guia do mundo interior)"),
    21663: ("Quem machuca Aurica", "JP オリカを傷つける奴 (Dislikes Don Leon; 41B <= 48B)"),
    21664: ("Proteger Aurica sempre", "JP オリカを護り続ける (Sonho Don Leon; soluciona overflow de 57B em 56B; 45B <= 56B)"),
    21665: ("Tirar bolas de pelo", "JP 毛玉取り (Hobby Don Leon; 41B <= 48B)"),
    21666: ("Tudo por Aurica", "JP 常にオリカのために (Lema Don Leon; soluciona overflow de 33B em 32B; 31B <= 32B; fidelidade incondicional)"),
    21667: ("Entidade que habita a Cosmosfera de Aurica. Urso de pelúcia dado por Claire antes de ir à Tenba, ganhou vida no Espaço da Alma pelo apego da garota. É um cavaleiro leal que vela por Aurica dia e noite.", "JP オリカの心の世界に住んでいる生命体 (Perfil Don Leon; 407B <= 464B; afeto protetor forjado na infância com Claire)"),
    21668: ("PC: Don Leon", "JP 人C:どんすけ (Person Card Don Leon; 25B <= 32B)"),
    21669: ("Hama", "JP ハマ (Hama; 9B <= 16B)"),
    21670: ("Alma de Misha", "JP ミシャの精神世界 (Hama; 27B <= 40B)"),
    21671: ("Misha, Lyner", "JP ミシャ、ライナー (Likes Hama; 25B <= 32B)"),
    21672: ("Quem machuca Misha", "JP ミシャを傷つける奴 (Dislikes Hama; 39B <= 48B)"),
    21673: ("Continuar protegendo Misha", "JP ミシャを護り続ける (Sonho Hama; 55B <= 56B)"),
    21674: ("Limpeza", "JP 掃除 (Hobby Hama; 15B <= 24B)"),

    # File 0060 (21675..21698)
    21675: ("Devoção filial", "JP 親孝行 (Lema Hama; 32B <= 32B; encaixe perfeito)"),
    21676: ("Entidade que reside na Cosmosfera de Misha. Materialização da ocarina de madeira que Lyner entalhou para a garota na infância. Ficou traumatizada ao descobrir que Lyner, considerado seu criador e pai, havia se esquecido totalmente dela.", "JP ミシャの心の世界に住んでいる生命体 (Perfil Hama; 457B <= 480B; mágoa infantil e luto pela ocarina esquecida por Lyner)"),
    21677: ("PC: Hama", "JP 人C:ハマ (Person Card Hama; 17B <= 24B)"),
    21678: ("Segredo ABR 1", "JP ABRのひみつ1 (Lore ABR 1; soluciona overflow de 33B em 32B; 27B <= 32B)"),
    21679: ("O A.B.R. é um guardião autônomo composto por três módulos. Em condições normais, vigiam a Torre separados; sob ameaça, acoplam-se e desferem uma ofensiva combinada implacável.", "JP ABRは3体の独立した機関から構成される (Mecânica ABR 1; 358B <= 392B; arquitetura militar tripartite da Torre)"),
    21680: ("SC: Segredo ABR 1", "JP 秘C:ABRの秘密#11 (Secret Card ABR 1; soluciona overflow de 43B em 40B; 35B <= 40B)"),
    21681: ("Segredo ABR 2", "JP ABRのひみつ2 (Lore ABR 2; soluciona overflow de 33B em 32B; 27B <= 32B)"),
    21682: ("A.B.R. α contém o sistema central. Quando combinado, regenera-se automaticamente, tornando inútil o dano físico.", "JP ABR(α)はABRの中枢機関を持ち (Mecânica ABR 2; 236B <= 256B; regeneração da unidade central)"),
    21683: ("SC: Segredo ABR 2", "JP 秘C:ABRの秘密#12 (Secret Card ABR 2; soluciona overflow de 43B em 40B; 35B <= 40B)"),
    21684: ("Segredo ABR 3", "JP ABRのひみつ3 (Lore ABR 3; soluciona overflow de 33B em 32B; 27B <= 32B)"),
    21685: ("O A.B.R. β carrega a unidade propulsora primária. Dono de agilidade extrema, desfere investidas fulminantes, mas seu perigo real reside em absorver e anular por completo o poder de Canção de qualquer Reyvateil.", "JP ABR(β)はABRのメインエンジンを搭載 (Mecânica ABR 3; 412B <= 456B; dreno e anulação de canções)"),
    21686: ("SC: Segredo ABR 3", "JP 秘C:ABRの秘密#13 (Secret Card ABR 3; soluciona overflow de 43B em 40B; 35B <= 40B)"),
    21687: ("Segredo ABR 4", "JP ABRのひみつ4 (Lore ABR 4; soluciona overflow de 33B em 32B; 27B <= 32B)"),
    21688: ("O A.B.R. γ opera como a artilharia pesada. Dispara projéteis de múltiplos elementos e, ao se acoplar, transfere carga para o módulo α disparar o devastador Canhão de Ondas de Choque, de poder estarrecedor.", "JP ABR(γ)はABRの主砲となる火力重視 (Mecânica ABR 4; 422B <= 472B; artilharia pesada e Canhão de Ondas de Choque)"),
    21689: ("SC: Segredo ABR 4", "JP 秘C:ABRの秘密#14 (Secret Card ABR 4; soluciona overflow de 43B em 40B; 35B <= 40B)"),
    21690: ("Segredo ABR 5", "JP ABRのひみつ5 (Lore ABR 5; soluciona overflow de 33B em 32B; 27B <= 32B)"),
    21691: ("O Canhão de Ondas exige energia provinda da Magia da Canção das Reyvateils, carga que apenas o módulo β é capaz de drenar. Sendo assim, o A.B.R. γ é totalmente incapaz de disparar essa arma quando isolado.", "JP 波動砲は、エネルギーの充填にレーヴァテイルの詩魔法の力を必要とし (Mecânica ABR 5; 416B <= 424B; interdependência de módulos bélicos)"),
    21692: ("SC: Segredo ABR 5", "JP 秘C:ABRの秘密#15 (Secret Card ABR 5; soluciona overflow de 43B em 40B; 35B <= 40B)"),
    21693: ("Segredo ABR 6", "JP ABRのひみつ6 (Lore ABR 6; soluciona overflow de 33B em 32B; 27B <= 32B)"),
    21694: ("O ponto fraco do disparo é a drenagem de energia: os módulos α e β ficam inativos. É nessa janela que ambos devem ser destruídos.", "JP また、波動砲の最大の弱点は (Tática de Chefe ABR 6; soluciona overflow de 385B para 263B <= 352B; tática precisa de interrupção e foco de dano)"),
    21695: ("SC: Segredo ABR 6", "JP 秘C:ABRの秘密#16 (Secret Card ABR 6; soluciona overflow de 43B em 40B; 35B <= 40B)"),
    21696: ("Informação de Spica 1", "JP スピカの裏情報1 (Relatório Spica 1; 45B <= 56B)"),
    21697: ("Se quer bons Cristais Grathnode, venha sempre à minha loja. Mas o estoque demora... Dê uma volta fora da cidade, trave algumas batalhas e novas remessas chegarão!", "JP いいグラスノ結晶が欲しかったら (Dica Spica 1; soluciona overflow de 445B para 328B <= 376B; tom informal e malicioso da negociante do submundo)"),
    21698: ("SC: Relatório Spica 1", "JP 秘C:スピカ裏情報#11 (Secret Card Spica 1; soluciona overflow de 50B em 48B; 44B <= 48B)"),

    # File 0061 (21699..21722)
    21699: ("Informação de Spica 2", "JP スピカの裏情報2 (Relatório Spica 2; 45B <= 56B)"),
    21700: ("O lema da loja é: 'vender cristais que o freguês ainda não tem'. Por isso, o estoque muda conforme o que você carrega. Como descubro o que tem na bolsa? Hehe, segredo do ofício!", "JP 私のお店のモットーは (Dica Spica 2; soluciona overflow de 443B para 360B <= 392B; riso matreiro hehe sem rubrica e lábia comercial)"),
    21701: ("SC: Relatório Spica 2", "JP 秘C:スピカ裏情報#12 (Secret Card Spica 2; soluciona overflow de 50B em 48B; 44B <= 48B)"),
    21702: ("Informação de Spica 3", "JP スピカの裏情報3 (Relatório Spica 3; 45B <= 56B)"),
    21703: ("Acha meus Cristais Grathnode caros? Sabia que já cobro 80% do valor de mercado? Se quiser pedras raras sem gastar tanto ouro, recomendo aproveitar ao máximo o processo de [Recristalização].", "JP 私の売ってるグラスノ結晶が高いですって? (Dica Spica 3; 353B <= 384B; preserva tag de comando [Recristalização])"),
    21704: ("SC: Relatório Spica 3", "JP 秘C:スピカ裏情報#13 (Secret Card Spica 3; soluciona overflow de 50B em 48B; 44B <= 48B)"),
    21705: ("Informação de Spica 4", "JP スピカの裏情報4 (Relatório Spica 4; 45B <= 56B)"),
    21706: ("A pureza do cristal obtido na [Recristalização] é diretamente proporcional à qualidade do item de origem. O grande macete é usar cristais refinados para forjar itens nobres e depois [Recristalizar]. Fica a dica!", "JP 「再結晶化」でもらえるグラスノ結晶の品質は (Dica Spica 4; 376B <= 464B; lógica de síntese avançada)"),
    21707: ("SC: Relatório Spica 4", "JP 秘C:スピカ裏情報#14 (Secret Card Spica 4; soluciona overflow de 50B em 48B; 44B <= 48B)"),
    21708: ("Informação de Spica 5", "JP スピカの裏情報5 (Relatório Spica 5; 45B <= 56B)"),
    21709: ("Quase todo Cristal Grathnode pode ser forjado via [Recristalização], mas sabia que certas pedras das lojas jamais surgem nesse processo? Guarde bem essa informação!", "JP ほとんどのグラスノ結晶は (Dica Spica 5; 320B <= 368B; mecânica de exclusividade de lojistas)"),
    21710: ("SC: Relatório Spica 5", "JP 秘C:スピカ裏情報#15 (Secret Card Spica 5; soluciona overflow de 50B em 48B; 44B <= 48B)"),
    21711: ("Informação de Spica 6", "JP スピカの裏情報6 (Relatório Spica 6; 45B <= 56B)"),
    21712: ("Dizem por aí que o cristal gerado na [Recristalização] reflete o valor intrínseco do item. Aqueles de Grau S que exigem montanhas de cristais nobres no preparo... rendem pedras inacreditáveis!", "JP 「再結晶化」する際に出来上がるグラスノ結晶は (Dica Spica 6; 372B <= 440B; recompensas de Grau S)"),
    21713: ("SC: Relatório Spica 6", "JP 秘C:スピカ裏情報#16 (Secret Card Spica 6; soluciona overflow de 50B em 48B; 44B <= 48B)"),
    21714: ("Dica da Lyra 1", "JP リルラの◎テク1 (Lyra Tech 1; soluciona overflow de 51B em 32B; 29B <= 32B)"),
    21715: ("Aqui é a Lyra! Se quiser ver a Lyra trabalhando duro, é só me agradar com Cristais Grathnode raros! Aí a Lyra vai caçar com todo o empenho!", "JP リルラなのだー! (Dica Lyra 1; 260B <= 288B; cacoete infantil e entusiasmo de expedição)"),
    21716: ("SC: Lyra◎ 1", "JP 秘C:リルラ◎テク#11 (Secret Card Lyra 1; 21B <= 24B)"),
    21717: ("Dica da Lyra 2", "JP リルラの◎テク2 (Lyra Tech 2; soluciona overflow de 51B em 32B; 29B <= 32B)"),
    21718: ("É a Lyra! Subir o topo da Torre cansa e tira a coragem da Lyra! Mas, se me der um cristal raro, talvez a Lyra faça uma força!", "JP リルラなのだー!塔の高いとこは (Dica Lyra 2; soluciona overflow de 333B para 254B <= 304B; preguiça e ganância ingênua de criança Teru)"),
    21719: ("SC: Lyra◎ 2", "JP 秘C:リルラ◎テク#12 (Secret Card Lyra 2; 21B <= 24B)"),
    21720: ("Dica da Lyra 3", "JP リルラの◎テク3 (Lyra Tech 3; soluciona overflow de 51B em 32B; 29B <= 32B)"),
    21721: ("Aqui é a Lyra! Se não aguenta de ansiedade esperando a Lyra voltar, vá lutar por perto enquanto espera! Se travar umas dez lutas, a Lyra já deve ter retornado!", "JP リルラなのだー!リルラが帰ってくるのが (Dica Lyra 3; 303B <= 336B; dica mecânica de ciclos de batalha)"),
    21722: ("SC: Lyra◎ 3", "JP 秘C:リルラ◎テク#13 (Secret Card Lyra 3; 21B <= 24B)"),

    # File 0062 (21723..21746)
    21723: ("Dica da Lyra 4", "JP リルラの◎テク4 (Lyra Tech 4; soluciona overflow de 51B em 32B; 29B <= 32B)"),
    21724: ("É a Lyra! Nas expedições a Lyra acha de tudo! Os itens raros variam conforme a região, então não seja mão de vaca e peça um montão de buscas pra Lyra!", "JP リルラなのだー!調達で探してくるアイテムは (Dica Lyra 4; 288B <= 312B; pedido sem vergonha de patrocínio)"),
    21725: ("SC: Lyra◎ 4", "JP 秘C:リルラ◎テク#14 (Secret Card Lyra 4; 21B <= 24B)"),
    21726: ("Dica da Lyra 5", "JP リルラの◎テク5 (Lyra Tech 5; soluciona overflow de 51B em 32B; 29B <= 32B)"),
    21727: ("É a Lyra! Outra vantagem incrível é que a Lyra acha muitos ingredientes para Grathmeld! Se faltar algum material para sua síntese, pode confiar tudo à Lyra!", "JP リルラなのだー!調達のもうひとつのポイントは (Dica Lyra 5; 309B <= 352B; coleta de ingredientes raros)"),
    21728: ("SC: Lyra◎ 5", "JP 秘C:リルラ◎テク#15 (Secret Card Lyra 5; 21B <= 24B)"),
    21729: ("Dica de chefes", "JP ボスのひみつ (Lore Chefes; soluciona overflow de 33B em 32B; 29B <= 32B)"),
    21730: ("Chefes são fortes, mas vencê-los com Nível Harmônico no ápice pode render Cristais Grathnode raríssimos. Vale a pena encarar o desafio sempre que der!", "JP 強敵であるボスだが (Mecânica de drop Harmo máximo; soluciona overflow de 388B para 307B <= 344B; precisão terminológica e incentivo tático)"),
    21731: ("SC: Seg. chefe", "JP 秘C:ボスの秘密 (Secret Card Boss; 29B <= 32B)"),
    21732: ("Diário Ikaruga 1", "JP 斑鳩開発記1 (Log Ikaruga 1; soluciona overflow de 41B em 40B; 35B <= 40B)"),
    21733: ("Blindado de alta mobilidade criado com tecnologia de ponta da Tenba. Tem propulsor potente e dispara uma salva quádrupla de mísseis de ampla área. Sua blindagem é altíssima, mas quase não resiste à Magia da Canção.", "JP 天覇の技術の粋を結集して作られた高機動兵器 (Dossiê Ikaruga 1; soluciona overflow de 502B para 436B <= 480B; terminologia militar bélica da Tenba)"),
    21734: ("SC: Dados Ikaruga 1", "JP 秘C:斑鳩情報#11 (Secret Card Ikaruga 1; soluciona overflow de 43B em 40B; 39B <= 40B)"),
    21735: ("Diário Ikaruga 2", "JP 斑鳩開発記2 (Log Ikaruga 2; soluciona overflow de 41B em 40B; 35B <= 40B)"),
    21736: ("Com base nos destroços da Unidade 1, criou-se em segredo o Ikaruga Unidade 2 para sanar todas as falhas. Foi projetado para repelir quase todo ataque (salvo certos efeitos residuais de Magia da Canção).", "JP 何者かによって破壊されたイカルガ一号 (Dossiê Ikaruga 2; soluciona overflow de 495B para 406B <= 480B; projeto de blindagem total e exceção de canções)"),
    21737: ("SC: Dados Ikaruga 2", "JP 秘C:斑鳩情報#12 (Secret Card Ikaruga 2; soluciona overflow de 43B em 40B; 39B <= 40B)"),
    21738: ("Diário Ikaruga 3", "JP 斑鳩開発記3 (Log Ikaruga 3; soluciona overflow de 41B em 40B; 35B <= 40B)"),
    21739: ("Após dezenas de combates simulados, detectou-se uma falha: certos ataques elementais causam sobrecarga e pane na CPU. Após agir sem controle, o sistema reinicia, deixando o mecha totalmente exposto.", "JP 数十回に渡る戦闘データ収集の結果 (Dossiê Ikaruga 3; soluciona overflow de 488B para 399B <= 472B; vulnerabilidade de sobrecarga e reboot)"),
    21740: ("SC: Dados Ikaruga 3", "JP 秘C:斑鳩情報#13 (Secret Card Ikaruga 3; soluciona overflow de 43B em 40B; 39B <= 40B)"),
    21741: ("Diário Ikaruga 4", "JP 斑鳩開発記4 (Log Ikaruga 4; soluciona overflow de 41B em 40B; 35B <= 40B)"),
    21742: ("O caça de escolta Asuka priorizou tanto o ataque que, ao ser abatido, o combustível sofre ignição em cadeia e provoca explosões capazes de estraçalhar até o próprio Ikaruga 2...", "JP さらに完全な防衛システムとして期待された戦闘機:飛鳥 (Dossiê Ikaruga 4; soluciona overflow de 454B para 361B <= 408B; ignição em cadeia e destruição mútua)"),
    21743: ("SC: Dados Ikaruga 4", "JP 秘C:斑鳩情報#14 (Secret Card Ikaruga 4; soluciona overflow de 43B em 40B; 39B <= 40B)"),
    21744: ("Trovão selvagem", "JP 荒ぶる稲妻 (Alcunha Bourd; 31B <= 32B)"),
    21745: ("Bourd Rade, segundo da Tenba, era chamado de 'Trovão Selvagem'. Como o nome diz, controla raios. Costuma reter esse poder, mas, ao lutar para valer, absorve raios pelas asas e atinge força descomunal.", "JP 天覇No2のボルド・レードはかつて (Perfil Trovão Selvagem; soluciona overflow de 500B para 403B <= 448B; poder elétrico e asas de absorção)"),
    21746: ("SC: Trovão selvagem", "JP 秘C:荒ぶる稲妻 (Secret Card Bourd; 37B <= 40B)")
}

# Verificação rigorosa
errors = []
overflows = []
validated_dialogues = []

lines_rewritten = 0
lines_approved_as_is = 0

for item in raw_items:
    id_ = item["id"]
    ob = item["original_bytes"]
    orig_en = item["original_en"]
    orig_jp = item["original_jp"]
    ef = item["event_file"]
    cur_db = item["current_ptbr"]
    
    if id_ not in curated_dict:
        errors.append(f"ID {id_} ausente do dicionário curado!")
        continue
    
    curated_text, justif = curated_dict[id_]
    
    # 1. Checagem de tamanho de bytes
    enc = encoded_size(curated_text)
    if enc is None or enc > ob:
        overflows.append(f"ID {id_} OVERFLOW: {enc}B > {ob}B (Texto: '{curated_text}')")
    
    # 2. Hard Gate Técnico
    val_errs = validate_line(id_, orig_en, curated_text)
    if val_errs:
        for ve in val_errs:
            errors.append(f"ID {id_} VALIDAÇÃO: {ve}")
            
    if curated_text != cur_db:
        lines_rewritten += 1
    else:
        lines_approved_as_is += 1
        
    validated_dialogues.append({
        "id": id_,
        "event_file": ef,
        "speaker_id": 0,
        "speaker": "Sistema / Narração",
        "original_jp": orig_jp,
        "original_en": orig_en,
        "current_ptbr": cur_db,
        "curated_ptbr": curated_text,
        "justification": justif
    })

print(f"Total processados: {len(validated_dialogues)}/288")
print(f"Linhas reescritas: {lines_rewritten}")
print(f"Linhas aprovadas mantidas: {lines_approved_as_is}")
print(f"Erros de validação técnica: {len(errors)}")
print(f"Estouros de bytes (overflows): {len(overflows)}")

if errors:
    for e in errors[:10]:
        print("  -", e)
if overflows:
    for ov in overflows[:10]:
        print("  -", ov)

if not errors and not overflows and len(validated_dialogues) == 288:
    print("\n[PERFEITO] 100% dos 288 IDs calibrados e aprovados sem nenhum erro nem estouro!")
    
    # Montar JSON final do bloco
    output_data = {
        "block_id": "BLK_SYS_005",
        "axis_id": "1_NUCLEO_SISTEMICO_E_MENUS",
        "axis_name": "1_NUCLEO_SISTEMICO_E_MENUS",
        "category": "Executable Strings",
        "total_lines": len(validated_dialogues),
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "new_terms": {
            "SC: [Segredo]": {
                "pt": "SC: [Segredo]",
                "category": "Segredo / Sistema",
                "note": "Prefixo canônico de Secret Card (Card de Segredo / 秘C:). Mantido com 'SC:' para concisão de bytes e paridade com a UI."
            },
            "A.B.R.": {
                "pt": "A.B.R.",
                "gender": "masculino",
                "number": "singular",
                "category": "Bestiário / Mecânico",
                "note": "Guardião autônomo tripartite da Torre de Elemia composto pelos módulos α, β e γ (JP ABR)."
            },
            "Ikaruga": {
                "pt": "Ikaruga",
                "gender": "masculino",
                "number": "singular",
                "category": "Bélico / Tecnologia Tenba",
                "note": "Mecha bélico de alta mobilidade desenvolvido secretamente pelo Conglomerado Tenba (JP 斑鳩 / イカルガ)."
            },
            "Asuka": {
                "pt": "Asuka",
                "gender": "masculino",
                "number": "singular",
                "category": "Bélico / Tecnologia Tenba",
                "note": "Caça de escolta defensiva fabricado pela Tenba para escoltar o mecha Ikaruga (JP 戦闘機:飛鳥)."
            },
            "Wild Thunder": {
                "pt": "Trovão Selvagem",
                "gender": "masculino",
                "number": "singular",
                "category": "Alcunha / Personagem",
                "note": "Alcunha bélica lendária de Bourd Rade nos seus tempos de combatente brutal (JP 荒ぶる稲妻)."
            },
            "Shockwave Cannon": {
                "pt": "Canhão de Ondas de Choque",
                "gender": "masculino",
                "number": "singular",
                "category": "Bélico / Mecânica de Chefe",
                "note": "Arma suprema acoplada disparada pelo guardião A.B.R. alimentada por Magia da Canção drenada (JP 波動砲)."
            }
        },
        "scene_handoff_final": {
            "last_scene_id": "BLK_SYS_005",
            "last_line_id": 21746,
            "location_and_situation": "Núcleo Sistêmico Parte 5 (Dossiers canônicos de todos os aliados, sacerdotes, rivais, guardiões da Torre, espíritos mentais, segredos do A.B.R., relatórios comerciais de Spica, dicas de expedição de Lyra e registros bélicos do mecha Ikaruga) concluído e 100% calibrado dentro dos tetos de memória.",
            "emotional_state": "Sistêmico / Concluído com louvor.",
            "active_hooks": [
                "Encadear com BLK_SYS_006 (continuação do Núcleo Sistêmico, itens, sínteses e menus)."
            ]
        },
        "highlights": [
            {
                "id": 21466,
                "jp": "人々の笑顔、正義",
                "en": "Smiles, Justice",
                "before": "Sorrisos, justiça",
                "after": "Sorrisos e bem",
                "reason": "JP 人々の笑顔、正義 (elimina estouro crítico de 36B para 29B <= 32B preservando o afeto de Radolf ao bem-estar do povo)"
            },
            {
                "id": 21485,
                "jp": "塔の管理者",
                "en": "Tower Administrator",
                "before": "Administradora da torre",
                "after": "Senhora da Torre",
                "reason": "JP 塔の管理者 (elimina estouro crítico de 47B para 33B <= 40B com dignidade e nobreza divina de Shurelia)"
            },
            {
                "id": 21489,
                "jp": "新婚生活",
                "en": "Life as Newlyweds",
                "before": "Vida de recém-casados",
                "after": "Ser recém-casada",
                "reason": "JP 新婚生活 (elimina estouro de 44B para 35B <= 40B capturando a aspiração romântica secreta de Shurelia)"
            },
            {
                "id": 21501,
                "jp": "詩は庶民の為に",
                "en": "Songs are wonderful!",
                "before": "Canções são maravilhosas!",
                "after": "Canções pelo povo!",
                "reason": "JP 詩は庶民の為に (elimina estouro de 52B para 39B <= 48B e restaura o lema social de Claire apagado na localização americana)"
            },
            {
                "id": 21531,
                "jp": "ガセネタは売らず",
                "en": "Never sell false info",
                "before": "Nunca vender informação falsa",
                "after": "Nunca vender boatos!",
                "reason": "JP ガセネタは売らず (elimina estouro maciço de 61B para 41B <= 48B com fala afiada e concisa de Spica)"
            },
            {
                "id": 21553,
                "jp": "平穏な世界のために",
                "en": "Reyvateilia Rocks",
                "before": "Reyvateilia é demais",
                "after": "Por um mundo em paz",
                "reason": "JP 平穏な世界のために (elimina estouro de 43B para 39B <= 40B e resgata o idealismo pacifista trágico de Mir adulterado na versão em inglês)"
            },
            {
                "id": 21561,
                "jp": "天覇のナンバー2",
                "en": "Tenba’s 2nd",
                "before": "Nº 2 da Tenba",
                "after": "2º na Tenba",
                "reason": "JP 天覇のナンバー2 (elimina estouro de 27B para exatos 24B <= 24B sem truncamento)"
            },
            {
                "id": 21565,
                "jp": "策略を練ること",
                "en": "Making Misha small",
                "before": "Encolher Misha",
                "after": "Tramar esquemas",
                "reason": "JP 策略を練ること (restaura o perfil estratégico maquiavélico de Bourd adulterado jocosamente no inglês)"
            },
            {
                "id": 21629,
                "jp": "室内用ペットになる",
                "en": "Become an indoor pet",
                "before": "Virar um animal de estimação",
                "after": "Virar pet de colo",
                "reason": "JP 室内用ペットになる (elimina estouro absurdo de 63B para 35B <= 48B capturando o dengo de ELMA)"
            },
            {
                "id": 21666,
                "jp": "常にオリカのために",
                "en": "Aurica first",
                "before": "Aurica primeiro",
                "after": "Tudo por Aurica",
                "reason": "JP 常にオリカのために (elimina estouro de 33B para 31B <= 32B com lealdade cavalheiresca de Don Leon)"
            },
            {
                "id": 21700,
                "jp": "私のお店のモットーは「お客さんの持っていないグラスノ結晶を集める」ことよ。",
                "en": "My motto for this shop is ”Get Grathnode Crystals that customers don’t have.” So, my lineup changes depending on what crystals you’ve got. How I know what you already have...is a trade secret.",
                "before": "Meu lema é vender Cristais Grathnode que o cliente ainda não tem. O estoque muda conforme seus cristais. Como sei quais você já tem? Segredo comercial.",
                "after": "O lema da loja é: 'vender cristais que o freguês ainda não tem'. Por isso, o estoque muda conforme o que você carrega. Como descubro o que tem na bolsa? Hehe, segredo do ofício!",
                "reason": "JP 企業秘密 (lapidação dramática de Spica com riso natural hehe, malícia de submundo e 360B <= 392B)"
            },
            {
                "id": 21715,
                "jp": "リルラなのだー!リルラに頑張って欲しいときは、珍しいグラスノ結晶を貢ぐといいのだ。そうすればリルラも頑張って調達してくるのだ。",
                "en": "It’s me, Lyra-! If you want Lyra to work hard, it is good to give rare Grathnode Crystal tributes. Then Lyra will work hard and find things.",
                "before": "Sou eu, Lyra! Se quer que Lyra trabalhe bastante, ofereça Cristais Grathnode raros. Assim Lyra se esforça e encontra coisas!",
                "after": "Aqui é a Lyra! Se quiser ver a Lyra trabalhando duro, é só me agradar com Cristais Grathnode raros! Aí a Lyra vai caçar com todo o empenho!",
                "reason": "JP リルラなのだー (infusão do socioleto infantil e assinatura vocal enérgica de Lyra; 260B <= 288B)"
            },
            {
                "id": 21729,
                "jp": "ボスのひみつ",
                "en": "Boss’ Secret",
                "before": "Segredo do chefe",
                "after": "Dica de chefes",
                "reason": "JP ボスのひみつ (elimina estouro de 33B para 29B <= 32B com concisão de UI)"
            },
            {
                "id": 21733,
                "jp": "天覇の技術の粋を結集して作られた高機動兵器。",
                "en": "A High Mobility Weapon created by Tenba’s most advanced technology.",
                "before": "Arma de alta mobilidade feita com tecnologia avançada da Tenba. Tem propulsor potente e uma salva de quatro mísseis que cobre grande área. Sua defesa é alta, mas quase não resiste à Magia da Canção.",
                "after": "Blindado de alta mobilidade criado com tecnologia de ponta da Tenba. Tem propulsor potente e dispara uma salva quádrupla de mísseis de ampla área. Sua blindagem é altíssima, mas quase não resiste à Magia da Canção.",
                "reason": "JP 高機動兵器 (dossiê militar com vocabulário bélico denso e diegético; 436B <= 480B)"
            },
            {
                "id": 21745,
                "jp": "天覇No2のボルド・レードはかつて「荒ぶる稲妻」の異名を持っていた。",
                "en": "Tenba’s 2nd-in-command, Bourd Rade, used to have the nickname ”Wild Thunder.”",
                "before": "Bourd Rade, segundo no comando da Tenba, era chamado de 'Trovão Selvagem'. Pode controlar raios. Raramente usa esse poder, mas pode recorrer a ele para vencer uma batalha.",
                "after": "Bourd Rade, segundo da Tenba, era chamado de 'Trovão Selvagem'. Como o nome diz, controla raios. Costuma reter esse poder, mas, ao lutar para valer, absorve raios pelas asas e atinge força descomunal.",
                "reason": "JP 荒ぶる稲妻 (restaura o impacto da alcunha marcial e asas de relâmpago de Bourd; 403B <= 448B)"
            }
        ],
        "dialogues": validated_dialogues
    }
    
    output_file = tools_path / "curadoria_editorial" / "blocos" / "BLK_SYS_005_output.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"Salvo arquivo de saída em: {output_file}")

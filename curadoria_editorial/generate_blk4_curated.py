# -*- coding: utf-8 -*-
"""
Script mestre de geração e validação do bloco BLK_SYS_004.
Gera BLK_SYS_004_output.json com todas as 288 falas calibradas e validadas.
"""

import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\tools")
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line, validate_batch

INPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_SYS_004_input.json")
OUTPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_SYS_004_output.json")
DB_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\release\ArTonelico_PTBR_adaptado_108_20260926.atproj")

# Mapeamento completo dos 288 IDs: (curated_ptbr, justification)
CURATED_DATA = {
    # File 0039 (IDs 21171 - 21194)
    21171: ("Wind Guarder", "JP ウインドガーダー (Bit Ball com barreira aerodinâmica de vento; 23B <= 32B; paridade com a série Guarder)"),
    21172: ("Bit Ball modificada para resistir a ataques especiais. Uma barreira protetora ao seu redor concede alta resistência ao vento.", "Descrição refinada de bestiário; 237B <= 264B"),
    21173: ("MC: Ball8", "JP 敵C:ボール系8 (Card de Monstro da Família Esfera 8; 19B <= 24B)"),
    21174: ("Big Guarder", "JP ビッグガーダー (Bit Ball ampliada com barreira geral; 23B <= 24B; resolve overflow de 32B da tradução anterior)"),
    21175: ("Bit Ball colossal reforçada contra magias. Ergue uma barreira ao seu redor que resiste a todo ataque especial.", "Descrição refinada de bestiário; 222B <= 232B"),
    21176: ("MC: Ball9", "JP 敵C:ボール系9 (Card de Monstro da Família Esfera 9; 19B <= 24B)"),
    21177: ("Mother Bit", "JP マザービット (Bit Ball de porte colossal; 21B <= 24B; preserva nome canônico mecânico)"),
    21178: ("Bit Ball de porte gigantesco. Suas táticas são idênticas às da comum, mas seu poder de destruição é colossal.", "Descrição refinada de bestiário; 224B <= 240B"),
    21179: ("MC: Ball10", "JP 敵C:ボール系10 (Card de Monstro da Família Esfera 10; 21B <= 24B)"),
    21180: ("Mother Bit v2", "JP マザービット改 (Mother Bit modificada; 27B <= 32B; paridade com Bit Ball v2)"),
    21181: ("Mother Bit modificada e reforçada. A carcaça é similar, mas quem a confunde com a original paga muito caro...", "Descrição refinada de bestiário; 222B <= 240B"),
    21182: ("MC: Ball11", "JP 敵C:ボール系11 (Card de Monstro da Família Esfera 11; 21B <= 24B)"),
    21183: ("Satellite Star", "JP サテライトスター (Esfera satélite; 29B <= 32B; resolve overflow de 34B da tradução anterior)"),
    21184: ("Mother Bit escoltada por Bit Balls menores. Ao engajar em combate, todas as esferas atacam em sincronia.", "Descrição refinada de bestiário; 209B <= 216B"),
    21185: ("MC: Ball12", "JP 敵C:ボール系12 (Card de Monstro da Família Esfera 12; 21B <= 24B)"),
    21186: ("Olho Deus-Máquina", "JP 機神の瞳 (Olho do Deus-Máquina; 36B <= 40B; elimina overflow grave de 42B da tradução anterior)"),
    21187: ("Uma Mother Bit de poder aterrador. Fora concebida para outra função, mas seu poder de fogo é estarrecedor.", "Descrição refinada de bestiário; 214B <= 216B"),
    21188: ("MC: Ball13", "JP 敵C:ボール系13 (Card de Monstro da Família Esfera 13; 21B <= 24B)"),
    21189: ("Tipo II", "JP 弐式 (Robô bípedo flutuante Tipo II; 15B <= 16B)"),
    21190: ("Robô flutuante. Embora tenha formato humanoide, não possui pernas.", "Descrição refinada de bestiário; 135B <= 144B"),
    21191: ("MC: Robot1", "JP 敵C:ロボ系1 (Card de Monstro da Família Robô 1; 21B <= 24B)"),
    21192: ("Tipo III", "JP 参式 (Robô aperfeiçoado Tipo III; 17B <= 24B)"),
    21193: ("Robô aprimorado a partir do Tipo II. Suas falhas foram sanadas, elevando seu poder a um patamar muito superior.", "Descrição refinada de bestiário; 224B <= 256B"),
    21194: ("MC: Robot2", "JP 敵C:ロボ系2 (Card de Monstro da Família Robô 2; 21B <= 24B)"),

    # File 0040 (IDs 21195 - 21218)
    21195: ("Protótipo", "JP 無式 (Robô primordial sem número; 19B <= 24B)"),
    21196: ("Robô ancestral construído antes do Tipo II. Apesar de antigo, seu poder colossal supera de longe os Tipos II e III.", "Descrição refinada de bestiário; 233B <= 264B"),
    21197: ("MC: Robot3", "JP 敵C:ロボ系3 (Card de Monstro da Família Robô 3; 21B <= 24B)"),
    21198: ("Tipo 28", "JP 二八式 (Robô humanoide Tipo 28; 15B <= 16B)"),
    21199: ("Robô feito à imagem humana. Ao contrário do Tipo II, possui pernas e silhueta completa.", "Descrição refinada de bestiário; 178B <= 208B"),
    21200: ("MC: Robot4", "JP 敵C:ロボ系4 (Card de Monstro da Família Robô 4; 21B <= 24B)"),
    21201: ("Tipo 48", "JP 四八式 (Robô reforçado Tipo 48; 15B <= 16B)"),
    21202: ("Versão aprimorada do Tipo 28. Embora sua carcaça externa seja igual, seus circuitos internos foram reformulados do zero, deixando o Tipo 28 para trás.", "Descrição refinada de bestiário; 304B <= 312B"),
    21203: ("MC: Robot5", "JP 敵C:ロボ系5 (Card de Monstro da Família Robô 5; 21B <= 24B)"),
    21204: ("Tipo 88", "JP 八八式 (Robô avançado Tipo 88; 15B <= 16B)"),
    21205: ("Evolução do Tipo 48 com variado arsenal de ataques.", "Descrição refinada de bestiário; 103B <= 112B"),
    21206: ("MC: Robot6", "JP 敵C:ロボ系6 (Card de Monstro da Família Robô 6; 21B <= 24B)"),
    21207: ("Tipo Zero", "JP 零式 (Robô de metal líquido Tipo Zero; 19B <= 24B)"),
    21208: ("Robô feito de metal líquido. Graças à sua maleabilidade, pode alterar a própria forma livremente.", "Descrição refinada de bestiário; 200B <= 216B"),
    21209: ("MC: Robot7", "JP 敵C:ロボ系7 (Card de Monstro da Família Robô 7; 21B <= 24B)"),
    21210: ("Tipo Não-Zero", "JP 裏零式 (Variante sombria do Tipo Zero; 29B <= 32B)"),
    21211: ("Robô similar ao Tipo Zero, mas formado por um lodo negro e viscoso em vez de metal reluzente.", "Descrição refinada de bestiário; 188B <= 240B"),
    21212: ("MC: Robot8", "JP 敵C:ロボ系8 (Card de Monstro da Família Robô 8; 21B <= 24B)"),
    21213: ("Zero", "JP 零 (Protótipo supremo Zero; 9B <= 16B)"),
    21214: ("O modelo original do Tipo Zero. Dotado de altíssimo desempenho, repele golpes físicos e anula magias de todos os elementos, exceto vento. Derrube-o de vez com fortes rajadas eólicas!", "Descrição refinada de bestiário; 368B <= 368B"),
    21215: ("MC: Robot9", "JP 敵C:ロボ系9 (Card de Monstro da Família Robô 9; 21B <= 24B)"),
    21216: ("Wyrm", "JP ワイアーム (Réptil alado serpentino; 9B <= 16B)"),
    21217: ("Parente menor dos dragões, com asas. Não é um chefe, mas passa longe de ser fraco em batalha.", "Descrição refinada de bestiário; 190B <= 200B"),
    21218: ("MC: Dragon1", "JP 敵C:竜系1 (Card de Monstro da Família Dragão 1; 23B <= 24B)"),

    # File 0041 (IDs 21219 - 21242)
    21219: ("Thunder Wyrm", "JP サンダーアーム (Wyrm relampejante; 25B <= 32B)"),
    21220: ("Réptil alado da família dos Wyrms. Desfere investidas baseadas em relâmpagos.", "Descrição refinada de bestiário; 158B <= 168B"),
    21221: ("MC: Dragon2", "JP 敵C:竜系2 (Card de Monstro da Família Dragão 2; 23B <= 24B)"),
    21222: ("Hellstorm", "JP ヘルストーム (Wyrm das tempestades; 19B <= 24B; resolve overflow de 39B da tradução anterior)"),
    21223: ("Réptil alado da família dos Wyrms. Usa ataques especiais do elemento vento.", "Descrição refinada de bestiário; 153B <= 160B"),
    21224: ("MC: Dragon3", "JP 敵C:竜系3 (Card de Monstro da Família Dragão 3; 23B <= 24B)"),
    21225: ("Mini Wyrm", "JP ミニアーム (Wyrm minúsculo; 19B <= 24B)"),
    21226: ("Réptil alado da família dos Wyrms, porém minúsculo. Quem o subestima pelo porte pequeno sofre graves ferimentos.", "Descrição refinada de bestiário; 229B <= 272B"),
    21227: ("MC: Dragon4", "JP 敵C:竜系4 (Card de Monstro da Família Dragão 4; 23B <= 24B)"),
    21228: ("Wyvern", "JP ワイバーン (Dragão bípede alado; 13B <= 16B)"),
    21229: ("Dragão intermediário entre Wyrms e grandes dracos. Possui patas e demonstra vigor e fúria superiores aos do Wyrm.", "Descrição refinada de bestiário; 230B <= 232B"),
    21230: ("MC: Dragon5", "JP 敵C:竜系5 (Card de Monstro da Família Dragão 5; 23B <= 24B)"),
    21231: ("Wyvern Azul", "JP エアバーン (Wyvern rochoso azulado; 23B <= 24B)"),
    21232: ("Híbrido entre dragão e Wyrm. Sua couraça cor de pedra vulcânica passa uma nítida impressão de solidez.", "Descrição refinada de bestiário; 211B <= 240B"),
    21233: ("MC: Dragon6", "JP 敵C:竜系6 (Card de Monstro da Família Dragão 6; 23B <= 24B)"),
    21234: ("Flame Wyvern", "JP フレイムティアー (Wyvern flamejante; 25B <= 32B)"),
    21235: ("Dragão híbrido de escamas tingidas em carmim e branco. Concentra sua ofensiva em baforadas e ataques ardentes de fogo.", "Descrição refinada de bestiário; 239B <= 256B"),
    21236: ("MC: Dragon7", "JP 敵C:竜系7 (Card de Monstro da Família Dragão 7; 23B <= 24B)"),
    21237: ("Mini Wyvern", "JP ミニバーン (Wyvern pequeno; 23B <= 24B)"),
    21238: ("Dragão híbrido de porte diminuto, similar ao de um Mini Wyrm. Ainda assim, não se engane: na agressividade, continua sendo um Wyvern.", "Descrição refinada de bestiário; 270B <= 288B"),
    21239: ("MC: Dragon8", "JP 敵C:竜系8 (Card de Monstro da Família Dragão 8; 23B <= 24B)"),
    21240: ("Drake", "JP エンリュー (Grande dragão com garras; 11B <= 16B)"),
    21241: ("Dragão bípede munido de garras afiadas nas patas. Não dispõe de truques arcanos, mas compensa com força bruta.", "Descrição refinada de bestiário; 226B <= 256B"),
    21242: ("MC: Dragon9", "JP 敵C:竜系9 (Card de Monstro da Família Dragão 9; 23B <= 24B)"),

    # File 0042 (IDs 21243 - 21266)
    21243: ("Poison Drake", "JP ドクリュー (Drake venenoso; 25B <= 32B)"),
    21244: ("Draco peçonhento mais selvagem que o Drake comum. Como castiga a presa com golpes vorazes e veneno, quanto mais a luta dura, pior fica para o grupo.", "Descrição refinada de bestiário; 298B <= 336B"),
    21245: ("MC: Dragon10", "JP 敵C:竜系10 (Card de Monstro da Família Dragão 10; 25B <= 32B)"),
    21246: ("Lorde Drake", "JP リュージーン (Patriarca dos dragões; 23B <= 24B; resolve overflow de 25B da tradução anterior)"),
    21247: ("Dragão da classe mais alta. Usa várias habilidades especiais e desfere golpes físicos devastadores.", "Descrição refinada de bestiário; 202B <= 208B"),
    21248: ("MC: Dragon11", "JP 敵C:竜系11 (Card de Monstro da Família Dragão 11; 25B <= 32B)"),
    21249: ("Mini Drake", "JP ミニドラ (Dragão dourado raro minúsculo; 21B <= 24B)"),
    21250: ("Dragão de escamas douradas. Muito menor que outros dragões, raramente se mostra diante das pessoas. Monstro raro.", "Descrição refinada de bestiário; 229B <= 240B"),
    21251: ("MC: Dragon12", "JP 敵C:竜系12 (Card de Monstro da Família Dragão 12; 25B <= 32B)"),
    21252: ("Beast User", "JP ビーストユーザー (Domadora novata de feras; 21B <= 24B; resolve overflow de 35B da tradução anterior)"),
    21253: ("Domadora que comanda feras amestradas. Como o poder reside nos bichos e ela é frágil, não há o que temer.", "Descrição refinada de bestiário; 215B <= 232B"),
    21254: ("MC: Girl A1", "JP 敵C:娘I系1 (Card de Monstro da Família Domadora I 1; 23B <= 24B)"),
    21255: ("Beast Master", "JP ビーストマスター (Domadora veterana de feras; 25B <= 32B; resolve overflow de 33B da tradução anterior)"),
    21256: ("Domadora que incita feras mais perigosas contra o grupo, exigindo cautela. Como sua força física individual é medíocre, derrote-a rápido!", "Descrição refinada de bestiário; 280B <= 288B"),
    21257: ("MC: Girl A2", "JP 敵C:娘I系2 (Card de Monstro da Família Domadora I 2; 23B <= 24B)"),
    21258: ("Beast Lord", "JP ビーストミュール (Patriarca domadora de feras; 21B <= 24B; resolve overflow de 35B da tradução anterior)"),
    21259: ("Adestradora experiente que domina monstros ferozes. Além das feras vorazes, ela própria luta com perícia, tornando o duelo bem difícil.", "Descrição refinada de bestiário; 275B <= 288B"),
    21260: ("MC: Girl A3", "JP 敵C:娘I系3 (Card de Monstro da Família Domadora I 3; 23B <= 24B)"),
    21261: ("Bird User", "JP バードユーザー (Domadora novata de aves; 19B <= 24B; resolve overflow de 33B da tradução anterior)"),
    21262: ("Treinadora novata que usa aves para atacar. Como ainda é mera aprendiz, suas aves e sua força física não oferecem perigo.", "Descrição refinada de bestiário; 247B <= 256B"),
    21263: ("MC: Girl B1", "JP 敵C:娘II系1 (Card de Monstro da Família Domadora II 1; 23B <= 24B)"),
    21264: ("Bird Master", "JP バードマスター (Domadora veterana de aves; 23B <= 24B; resolve overflow de 31B da tradução anterior)"),
    21265: ("Adestradora que combate ao lado de aves de rapina. Embora seus pássaros causem dano, a treinadora em si é vulnerável. Ao iniciar o duelo, foque nela para vencer logo!", "Descrição refinada de bestiário; 336B <= 352B"),
    21266: ("MC: Girl B2", "JP 敵C:娘II系2 (Card de Monstro da Família Domadora II 2; 23B <= 24B)"),

    # File 0043 (IDs 21267 - 21290)
    21267: ("Bird Lord", "JP バードミュール (Patriarca domadora de aves; 19B <= 24B; resolve overflow de 33B da tradução anterior)"),
    21268: ("Domadora de aves velozes e fortes. Seus pássaros ferem com fúria e ela própria luta muito bem: não baixe a guarda!", "Descrição refinada de bestiário; 233B <= 248B"),
    21269: ("MC: Girl B3", "JP 敵C:娘II系3 (Card de Monstro da Família Domadora II 3; 23B <= 24B)"),
    21270: ("Mech User", "JP メックユーザー (Controladora novata de mecas; 19B <= 24B; resolve overflow de 38B da tradução anterior)"),
    21271: ("Controla máquinas de guerra. Como não comanda autômatos avançados, não oferece grande perigo.", "Descrição refinada de bestiário; 192B <= 200B"),
    21272: ("MC: Girl C1", "JP 敵C:娘III系1 (Card de Monstro da Família Domadora III 1; 23B <= 24B)"),
    21273: ("Mech Master", "JP メックマスター (Controladora veterana de mecas; 23B <= 24B; resolve overflow de 32B da tradução anterior)"),
    21274: ("Ela é frágil, mas os autômatos sob seu comando são fortes e perigosos.", "Descrição refinada de bestiário; 145B <= 152B"),
    21275: ("MC: Girl C2", "JP 敵C:娘III系2 (Card de Monstro da Família Domadora III 2; 23B <= 24B)"),
    21276: ("Mech Lord", "JP メックミュール (Patriarca controladora de mecas; 19B <= 24B; resolve overflow de 34B da tradução anterior)"),
    21277: ("Tanto as máquinas quanto a sua perícia bélica são formidáveis. Enfrentá-la com descuido resultará em graves danos.", "Descrição refinada de bestiário; 236B <= 248B"),
    21278: ("MC: Girl C3", "JP 敵C:娘III系3 (Card de Monstro da Família Domadora III 3; 23B <= 24B)"),
    21279: ("Balthazaar", "JP バルタザール (Dron aéreo de combate; 21B <= 24B)"),
    21280: ("Pequeno robô voador. Muito veloz no ar, desfere fortes ataques contra o grupo.", "Descrição refinada de bestiário; 158B <= 168B"),
    21281: ("MC: Aircraft1", "JP 敵C:航空系1 (Card de Monstro da Família Aeronave 1; 27B <= 32B)"),
    21282: ("Deltathor", "JP デルタオール (Dron aéreo blindado; 19B <= 24B)"),
    21283: ("Robô voador, forma final de Balthazaar. Ataque, defesa e resistência contra ataques especiais foram ampliados.", "Descrição refinada de bestiário; 223B <= 248B"),
    21284: ("MC: Aircraft2", "JP 敵C:航空系2 (Card de Monstro da Família Aeronave 2; 27B <= 32B)"),
    21285: ("Ishtamon", "JP イシュタムーン (Dron aéreo de alta performance; 17B <= 24B)"),
    21286: ("Robô voador com o dobro do desempenho de Balthazaar. Seus métodos e padrões de ataque continuam os mesmos.", "Descrição refinada de bestiário; 216B <= 248B"),
    21287: ("MC: Aircraft3", "JP 敵C:航空系3 (Card de Monstro da Família Aeronave 3; 27B <= 32B)"),
    21288: ("Melchior", "JP メルキオール (Dron aéreo com rifle; 17B <= 24B)"),
    21289: ("Robô voador. Balthazaar munido de rifle longo para elevar seu ataque. Tem alto poder de fogo.", "Descrição refinada de bestiário; 188B <= 208B"),
    21290: ("MC: Aircraft4", "JP 敵C:航空系4 (Card de Monstro da Família Aeronave 4; 27B <= 32B)"),

    # File 0044 (IDs 21291 - 21314)
    21291: ("Droomzen", "JP ドルムゼーン (Dron dourado com rifle; 17B <= 24B)"),
    21292: ("Robô voador na versão de elite de Melchior. Sua blindagem e seu rifle reluzem esculpidos em puro ouro.", "Descrição refinada de bestiário; 207B <= 208B"),
    21293: ("MC: Aircraft5", "JP 敵C:航空系5 (Card de Monstro da Família Aeronave 5; 27B <= 32B)"),
    21294: ("Valhallan", "JP バルハラーン (Dron aéreo com escolta; 19B <= 24B)"),
    21295: ("Robô voador escoltado por Bit Balls que orbitam Melchior. O rifle somado aos feixes das esferas faz dele um inimigo formidável.", "Descrição refinada de bestiário; 257B <= 296B"),
    21296: ("MC: Aircraft6", "JP 敵C:航空系6 (Card de Monstro da Família Aeronave 6; 27B <= 32B)"),
    21297: ("Casper", "JP カスパー (Dron aéreo pesado; 13B <= 16B)"),
    21298: ("Robô voador. Embora pareça um Balthazaar, trata-se do autômato Casper, de projeto distinto e com poder muito superior.", "Descrição refinada de bestiário; 240B <= 248B"),
    21299: ("MC: Aircraft7", "JP 敵C:航空系7 (Card de Monstro da Família Aeronave 7; 27B <= 32B)"),
    21300: ("Dathzaak", "JP ダスザーク (Dron aéreo de assalto; 17B <= 24B)"),
    21301: ("Robô voador na versão de assalto de Casper. Apesar de não ter rifle como Melchior, sua blindagem e ataque rivalizam com grandes armas.", "Descrição refinada de bestiário; 272B <= 304B"),
    21302: ("MC: Aircraft8", "JP 敵C:航空系8 (Card de Monstro da Família Aeronave 8; 27B <= 32B)"),
    21303: ("Miraclious", "JP ミラクリオス (Dron aéreo supremo; 21B <= 24B)"),
    21304: ("Robô voador escoltado por Bit Balls. Na prática, seria mais correto defini-lo como uma variante de Ishtamon.", "Descrição refinada de bestiário; 219B <= 224B"),
    21305: ("MC: Aircraft9", "JP 敵C:航空系9 (Card de Monstro da Família Aeronave 9; 27B <= 32B)"),
    21306: ("Nyo?", "JP にょ? (Criatura mascote felina esférica; 9B <= 16B)"),
    21307: ("Daria até um bicho de estimação, mas ainda é um monstro, embora sem imponência. Segura uma gema verde com a cauda. É um monstro raro.", "Descrição refinada de bestiário; 271B <= 336B"),
    21308: ("MC: Nyo?1", "JP 敵C:にょ?系1 (Card de Monstro da Família Nyo? 1; 19B <= 24B)"),
    21309: ("Nyonyo?", "JP にょにょ? (Nyo? verde com gema carmim; 13B <= 16B)"),
    21310: ("Um Nyo? verde cuja cauda envolve uma gema vermelha. Não importa a espécie, continua sendo Nyo?. A interrogação no nome dá um ar misterioso.", "Descrição refinada de bestiário; 282B <= 296B"),
    21311: ("MC: Nyo?2", "JP 敵C:にょ?系2 (Card de Monstro da Família Nyo? 2; 19B <= 24B)"),
    21312: ("NYO!?", "JP ニョ!? (Nyo? espalhafatoso de pelagem rosa; 11B <= 16B)"),
    21313: ("Nyo? de pelo rosa que segura uma pedra roxa com a cauda. Pela cor extravagante, qualquer um se assusta quando ele surge do nada. Daí o nome: NYO!?", "Descrição refinada de bestiário; 294B <= 320B"),
    21314: ("MC: Nyo?3", "JP 敵C:にょ?系3 (Card de Monstro da Família Nyo? 3; 19B <= 24B)"),

    # File 0045 (IDs 21315 - 21338)
    21315: ("Big Nyo?", "JP でっかいにょ? (Nyo? gigante; 17B <= 24B)"),
    21316: ("Trata-se de um Nyo? bem maior que o normal. Cuidado: quem zomba do nome óbvio acaba se ferindo feio. Por trás dessa carinha inofensiva, esconde-se um inimigo forte.", "Descrição refinada de bestiário; 331B <= 336B"),
    21317: ("MC: Nyo?4", "JP 敵C:にょ?系4 (Card de Monstro da Família Nyo? 4; 19B <= 24B)"),
    21318: ("Tipo 1025", "JP 千弐拾伍式 (Fortaleza voadora Tipo 1025; 19B <= 24B)"),
    21319: ("Fortaleza aérea que patrulha o interior da Torre. Possui blindagem espessa e disparos avassaladores. Faz jus absoluto ao nome de fortaleza.", "Descrição refinada de bestiário; 280B <= 296B"),
    21320: ("MC: Fort1", "JP 敵C:要塞系1 (Card de Monstro da Família Fortaleza 1; 19B <= 24B)"),
    21321: ("Air Fort One", "JP エアフォート・ワン (Fortaleza voadora imperial; 25B <= 32B; resolve overflow de 38B da tradução anterior)"),
    21322: ("Variante aprimorada do Tipo 1025. Sua blindagem e seu ataque foram bastante fortalecidos.", "Descrição refinada de bestiário; 179B <= 192B"),
    21323: ("MC: Fort2", "JP 敵C:要塞系2 (Card de Monstro da Família Fortaleza 2; 19B <= 24B)"),
    21324: ("Auto-blaster", "JP オートブラスター (Fortaleza voadora automática; 25B <= 32B; resolve overflow de 37B da tradução anterior)"),
    21325: ("Fortaleza voadora escoltada por Bit Balls. O poder da base junto aos disparos das esferas faz dela um verdadeiro baluarte.", "Descrição refinada de bestiário; 245B <= 248B"),
    21326: ("MC: Fort3", "JP 敵C:要塞系3 (Card de Monstro da Família Fortaleza 3; 19B <= 24B)"),
    21327: ("ELMA", "JP ELMA-I (Autômato guardião divino de Shurelia; 9B <= 16B)"),
    21328: ("O guardião mais forte da Torre criado por Shurelia. Fiel ao dever, aniquila sem piedade quem ameace a Torre.", "Descrição refinada de bestiário; 218B <= 248B"),
    21329: ("MC: ELMA", "JP 敵C:#1ELMA-I## (Card de Monstro de ELMA; 17B <= 24B)"),
    21330: ("SPU", "JP SPU (Unidade de Processamento Simbólico / Chefe; 7B <= 8B)"),
    21331: ("Ikaruga Mk.I", "JP 斑鳩1号 (Baluarte de exploração da Tenba; 25B <= 32B)"),
    21332: ("Arma de exploração da Tenba. Além de enorme, vem com uma metralhadora giratória pesada capaz de varrer monstros comuns em segundos.", "Descrição refinada de bestiário; 265B <= 272B"),
    21333: ("MC: Ikaruga Mk.I", "JP 敵C:斑鳩一号 (Card de Monstro de Ikaruga Mk.I; 33B <= 40B)"),
    21334: ("Reator do Beco Vagalume", "JP ほたる動力部 (Instalação motriz do Beco Vagalume; 47B <= 48B)"),
    21335: ("Flute", "JP フラウト (Patriarca de Em Pheyna; 11B <= 16B)"),
    21336: ("Líder de Em Pheyna. Conforme o Juramento de Elemia, vigia a Crônica Crescente, protege a Cantora das Estrelas e impede a subida de pessoas do Mundo Inferior.", "Descrição refinada de bestiário; 317B <= 352B"),
    21337: ("MC: Flute", "JP 敵C:フラウト (Card de Monstro de Flute; 19B <= 24B)"),
    21338: ("Templo", "JP 寺院 (Santuário sagrado; 13B <= 16B)"),

    # File 0046 (IDs 21339 - 21362)
    21339: ("ELMA-DS", "JP ELMA-II (Vírus réplica de ELMA criado por Mir; 15B <= 16B)"),
    21340: ("Vírus de Mir à semelhança do autômato ELMA de Shurelia. Além do visual idêntico, seu poder e ataques rivalizam com os da original.", "Descrição refinada de bestiário; 267B <= 272B"),
    21341: ("MC: ELMA-DS", "JP 敵C:#1ELMA-II## (Card de Monstro de ELMA-DS; 23B <= 24B)"),
    21342: ("Altar dos Apóstolos", "JP 使徒の祭壇 (Local sagrado de Mir e dos apóstolos; 39B <= 40B)"),
    21343: ("Bispo Falss", "JP ファルス司祭 (Prelado renegado da Igreja de Elemia; 23B <= 32B)"),
    21344: ("Sacerdote da Igreja de Elemia. Antes era Kyle Clancy, de Platina. Ao conspirar para reviver Mir, quase foi morto e fugiu para o Mundo Inferior.", "Descrição refinada de bestiário; 287B <= 360B"),
    21345: ("MC: Falss", "JP 敵C:ファルス (Card de Monstro de Falss; 19B <= 24B)"),
    21346: ("Bourd Rade", "JP ボルド・レール (Comandante da Tenba; 21B <= 24B)"),
    21347: ("Segundo no comando da Tenba. Guerreiro brutal que planeja reviver Mir. Quando luta a sério, envolve o próprio corpo em relâmpagos.", "Descrição refinada de bestiário; 264B <= 352B"),
    21348: ("MC: Bourd", "JP 敵C:ボルド (Card de Monstro de Bourd; 19B <= 24B)"),
    21349: ("Silvaplate", "JP シルヴァプレート (Plataforma prateada / Cidade flutuante; 21B <= 24B)"),
    21350: ("A.B.R.α", "JP A.B.R.α (Guardião mecânico da Torre modelo Alpha; 15B <= 16B)"),
    21351: ("Baluarte da Torre. Um dos três da patrulha ABR, forte sozinho. Modelo α. Ao ser atacado quando combinado, ativa o autorreparo.", "Descrição refinada de bestiário; 254B <= 312B"),
    21352: ("MC: A.B.R.α", "JP 敵C:#1A.B.R.##α (Card de Monstro de A.B.R.α; 23B <= 24B)"),
    21353: ("Av. Hoshinose", "JP ほしのせ通り (Avenida Hoshinose; 27B <= 32B)"),
    21354: ("A.B.R.β", "JP A.B.R.β (Guardião mecânico da Torre modelo Beta; 15B <= 16B)"),
    21355: ("Baluarte da Torre. Um dos três da patrulha ABR, forte sozinho. Modelo β. Quando combinado, absorve toda Magia da Canção.", "Descrição refinada de bestiário; 242B <= 288B"),
    21356: ("MC: A.B.R.β", "JP 敵C:#1A.B.R.##β (Card de Monstro de A.B.R.β; 23B <= 24B)"),
    21357: ("Colina Cantante", "JP 謳う丘 (Local sagrado de Ar tonelico; 31B <= 32B)"),
    21358: ("A.B.R.γ", "JP A.B.R.γ (Guardião mecânico da Torre modelo Gamma; 15B <= 16B)"),
    21359: ("Baluarte da Torre. Um dos três da patrulha ABR, forte sozinho. Modelo γ. Quando combinado, dispara um forte canhão de fótons.", "Descrição refinada de bestiário; 254B <= 312B"),
    21360: ("MC: A.B.R.γ", "JP 敵C:#1A.B.R.##γ (Card de Monstro de A.B.R.γ; 23B <= 24B)"),
    21361: ("Slepnir", "JP スレイプニル (Dragão lendário da Blastline; 15B <= 16B)"),
    21362: ("Dragão colossal da Blastline, dito Demônio da Blastline. Inúmeros foram os dirigíveis abatidos em pleno voo por essa fera.", "Descrição refinada de bestiário; 249B <= 264B"),

    # File 0047 (IDs 21363 - 21386)
    21363: ("MC: Slepnir", "JP 敵C:スレイプニル (Card de Monstro de Slepnir; 23B <= 24B)"),
    21364: ("Blastline", "JP ブラストライン (Barreira de plasma tempestuosa; 19B <= 24B)"),
    21365: ("Ikaruga Mk.II", "JP 斑鳩2号 (Supermáquina de exploração da Tenba; 27B <= 32B)"),
    21366: ("Máquina da Tenba baseada no Ikaruga. Tem blindagem reforçada e canhão condutor potente. Só peca por perder o controle de vez em quando.", "Descrição refinada de bestiário; 275B <= 296B"),
    21367: ("MC: Ikaruga Mk.II", "JP 敵C:斑鳩二号 (Card de Monstro de Ikaruga Mk.II; 35B <= 40B)"),
    21368: ("Área da Plasma Bell", "JP プラズマベル付近 (Proximidades da Plasma Bell; 40B <= 40B; resolve overflow de 41B da tradução anterior)"),
    21369: ("Shadow Head", "JP シャドウ頭 (Cabeça da encarnação final de Mir; 23B <= 24B; resolve overflow de 30B da tradução anterior)"),
    21370: ("Forma final de Mir Sombria, cujo tamanho reflete seu ódio pelos humanos. Divide-se em cabeça, tronco e braços; esta é a cabeça.", "Descrição refinada de bestiário; 260B <= 320B"),
    21371: ("MC: Shadow Head", "JP 敵C:シャドウ頭 (Card de Monstro de Shadow Head; 31B <= 32B; resolve overflow de 38B da tradução anterior)"),
    21372: ("Crônica Crescente", "JP クレセントクロニクル (Artefato lendário de Em Pheyna; 35B <= 40B)"),
    21373: ("Shadow Body", "JP シャドウ腹 (Tronco da encarnação final de Mir; 23B <= 24B; resolve overflow de 27B da tradução anterior)"),
    21374: ("Forma final de Mir Sombria, cujo tamanho reflete seu ódio pelos humanos. Divide-se em cabeça, tronco e braços; este é o tronco.", "Descrição refinada de bestiário; 259B <= 320B"),
    21375: ("MC: Shadow Body", "JP 敵C:シャドウ腹 (Card de Monstro de Shadow Body; 31B <= 32B; resolve overflow de 35B da tradução anterior)"),
    21376: ("Shadow Arm", "JP シャドウ腕 (Garras da encarnação final de Mir; 21B <= 24B; resolve overflow de 28B da tradução anterior)"),
    21377: ("Forma final de Mir Sombria, cujo tamanho reflete seu ódio pelos humanos. Divide-se em cabeça, tronco e braços; estes são os braços.", "Descrição refinada de bestiário; 268B <= 320B"),
    21378: ("MC: Shadow Arm", "JP 敵C:シャドウ腕 (Card de Monstro de Shadow Arm; 29B <= 32B; resolve overflow de 36B da tradução anterior)"),
    21379: ("Mir Sombria", "JP 魔神ミュール (Primeira encarnação demoníaca de Mir; 23B <= 24B)"),
    21380: ("Primeira forma de Mir Sombria, que personifica seu ódio aos humanos. É enorme como um demônio.", "Descrição refinada de bestiário; 192B <= 208B"),
    21381: ("MC: Mir Sombria", "JP 敵C:魔神ミュール (Card de Monstro de Mir Sombria; 31B <= 32B)"),
    21382: ("Rinkernator", "JP リンカーネーション (Reencarnador da Torre Ar tonelico; 23B <= 24B)"),
    21383: ("Mir", "JP ミュール (Forma original da Reyvateil renegada; 7B <= 8B)"),
    21384: ("Forma real de Mir. Em essência uma Reyvateil, parece uma garota comum, mas ataca envolta em uma aura de puro ódio.", "Descrição refinada de bestiário; 231B <= 240B; resolve overflow grave de 247B da tradução anterior)"),
    21385: ("MC: Mir", "JP 敵C:ミュール (Card de Monstro de Mir; 15B <= 16B)"),
    21386: ("Criança da Luz", "JP 光の御子 (Kanade / Guardiã sagrada da Plasma Bell; 29B <= 32B)"),

    # File 0048 (IDs 21387 - 21410)
    21387: ("A guardiã mais forte da Torre e protetora da Plasma Bell. Sua identidade real é Kanade, terceira androide de manutenção e irmã menor de Mei Mei. Fica mais forte a cada luta.", "Descrição refinada de bestiário; 350B <= 368B"),
    21388: ("MC: Criança da Luz", "JP 敵C:光の御子 (Card de Monstro de Criança da Luz; 37B <= 40B)"),
    21389: ("Plasma Bell", "JP プラズマベル (Instalação sagrada de Sol Ciel; 23B <= 24B; resolve overflow de 29B da tradução anterior)"),
    21390: ("Shurelia", "JP シュレリア (Administradora da Torre / Origin; 17B <= 24B)"),
    21391: ("Administradora da Torre que rege o continente flutuante. Vida artificial criada na Primeira Era e pioneira das Reyvateils. É a mestra das β de sangue puro, tida como Origin.", "Descrição refinada de bestiário; 348B <= 352B"),
    21392: ("MC: Shurelia", "JP 敵C:シュレリア (Card de Monstro de Shurelia; 25B <= 32B)"),
    21393: ("Ayatane", "JP 絢胤 (Agente viral infiltrado de Mir; 15B <= 16B)"),
    21394: ("Vírus de informação enviado por Mir. Sua missão é aproximar-se de Shurelia e controlar sua mente.", "Descrição refinada de bestiário; 198B <= 264B"),
    21395: ("MC: Ayatane", "JP 敵C:絢胤 (Card de Monstro de Ayatane; 23B <= 24B)"),
    21396: ("Catwalk", "JP キャットウォーク (Passarela industrial da Torre; 15B <= 16B; resolve overflow de 19B da tradução anterior)"),
    21397: ("Asuka", "JP 飛鳥 (Autômato voador explosivo de assalto; 11B <= 16B)"),
    21398: ("Pequeno robô voador. Parece um Melchior, mas é um projeto à parte. Tem especificações superiores, mas por carregar muito combustível, explode com violência ao ser abatido.", "Descrição refinada de bestiário; 348B <= 360B"),
    21399: ("MC: Asuka", "JP 敵C:飛鳥 (Card de Monstro de Asuka; 19B <= 24B)"),
    21400: ("Guardião", "JP ガーディアン (Sentinela voador tradicional da Torre; 19B <= 24B)"),
    21401: ("Guardião clássico na defesa da Torre. Funciona como fortaleza aérea e desfere fortes descargas elétricas.", "Descrição refinada de bestiário; 215B <= 224B"),
    21402: ("MC: Superfortaleza", "JP 敵C:超要塞 (Card de Monstro de Guardião / Superfortaleza; 37B <= 40B)"),
    21403: ("Cais Flutuante", "JP 滞空岸壁 (Porto de atracação de dirigíveis; 29B <= 32B)"),
    21404: ("Tastiella", "JP タスティエーラ (Guardiã milenar do Portão de Pheyna; 19B <= 24B)"),
    21405: ("Guardiã do Portão de Pheyna que cuida do Olho Congelado. Na antiguidade, selou Mir ao lado de Shurelia com seu poder formidável. Permanece viva e vigilante após séculos.", "Descrição refinada de bestiário; 344B <= 360B"),
    21406: ("MC: Tastiella", "JP 敵C:タスティ (Card de Monstro de Tastiella; 27B <= 32B)"),
    21407: ("Diante da Crônica Crescente", "JP クレセントクロニクル前 (Localização de confronto; 55B <= 64B)"),
    21408: ("Lyner Barsett", "JP ライナー・バルセルト (Nome canônico do protagonista; 27B <= 32B)"),
    21409: ("Platina", "JP プラティナ (Cidade natal de Lyner no topo da Torre; 15B <= 16B)"),
    21410: ("Cavaleiro de Elemia", "JP エレミアの騎士 (Título militar sagrado de Lyner; 39B <= 40B)"),

    # File 0049 (IDs 21411 - 21434)
    21411: ("18 anos", "JP 18歳 (Idade de Lyner; 15B <= 24B)"),
    21412: ("Reyvateil, Funbun", "JP RT、オボンヌ (Gostos de Lyner: Reyvateils e doce Funbun; 37B <= 40B)"),
    21413: ("Bugs e traíras", "JP バグ、裏表のある奴 (Aversões de Lyner: bugs e falsos amigos; 29B <= 32B)"),
    21414: ("Vida boa e mansa", "JP 寝て暮らす生活 (Sonho de Lyner: viver na boa; 33B <= 40B)"),
    21415: ("Aventuras", "JP 剣と冒険 (Hobbies de Lyner: espadas e aventuras; 19B <= 24B)"),
    21416: ("Agir sem pensar!", "JP 考えるより即行動 (Lema de Lyner: ação imediata sem hesitação; 33B <= 40B; resolve overflow de 43B da tradução anterior)"),
    21417: ("O protagonista. Cabeça-dura e ingênuo, não entende nada de romances e cede fácil à pressão alheia. Apesar de simplório, odeia injustiças e tem forte senso de dever. Como Cavaleiro de Elemia dedicado a Shurelia, combate a praga dos vírus.", "Dossiê canônico de Lyner lapidado com subtexto; 484B <= 488B"),
    21418: ("PC: Lyner", "JP 人C:ライナー (Person Card de Lyner; 19B <= 24B)"),
    21419: ("Aurica", "JP オリカ (Protagonista feminina / Reyvateil; 13B <= 16B)"),
    21420: ("Vila Skuwat", "JP スクワート村 (Vila natal de Aurica destruída pela Tenba; 23B <= 32B)"),
    21421: ("Donzela da Igreja", "JP 教会の聖女候補 (Ocupação de Aurica: candidata a donzela sagrada; 35B <= 40B)"),
    21422: ("17 anos", "JP 17歳 (Idade de Aurica; 15B <= 24B)"),
    21423: ("Don Leon, Claire", "JP どんすけ、クレア (Afeições de Aurica: seu guardião Donsuke e sua amiga Claire; 33B <= 40B)"),
    21424: ("Tribo Teru", "JP 図々しい人、テル族 (Aversões de Aurica: gente folgada e a Tribo Teru; 21B <= 24B)"),
    21425: ("Ver as Três Deusas", "JP 三謳神と逢うこと (Sonho de Aurica: conhecer as Três Deusa Cantoras; 37B <= 40B)"),
    21426: ("Cantar e cozinhar", "JP 謳うこと、料理 (Hobbies de Aurica: canto de Reyvateil e culinária; 35B <= 40B)"),
    21427: ("Ficar mais forte!", "JP 強くなりたい (Lema de Aurica: superar fraquezas do passado; 35B <= 40B)"),
    21428: ("De coração afável e gentil, costuma ficar quieta e abatida devido aos traumas que carrega. Perdeu os pais no massacre da Vila Skuwat e hoje atua como donzela da Igreja. Por ter baixa potência de canto, não tem parceiro fixo.", "Dossiê canônico de Aurica lapidado com temperatura dramática; 452B <= 488B"),
    21429: ("PC: Aurica", "JP 人C:オリカ (Person Card de Aurica; 21B <= 24B)"),
    21430: ("Misha", "JP 彌紗(ミシャ) (Heroína Reyvateil / Cantora das Estrelas; 11B <= 16B)"),
    21431: ("Reyvateil Tenba", "JP 天覇所属のRT (Ocupação de Misha sob contrato corporativo; 31B <= 32B)"),
    21432: ("18 anos", "JP 18歳 (Idade real de Misha; 15B <= 24B)"),
    21433: ("Lyner, Manuais", "JP ライナー、専門書 (Gostos de Misha: Lyner e livros técnicos; 29B <= 32B)"),
    21434: ("Alturas, Tenba", "JP 高い所、運動、天覇 (Aversões de Misha: lugares altos, esforço físico e corporação Tenba; 29B <= 40B)"),

    # File 0050 (IDs 21435 - 21458)
    21435: ("Noiva de Lyner", "JP ライナーのお嫁さん (Sonho secreto de infância de Misha; 29B <= 32B)"),
    21436: ("Leitura", "JP 読書 (Hobby acadêmico de Misha; 15B <= 16B)"),
    21437: ("Mente sobre força!", "JP 体力よりも頭脳 (Lema intelectual de Misha; 37B <= 40B; resolve overflow de 43B da tradução anterior)"),
    21438: ("Sincera e dedicada até o fim. Apesar dos modos serenos, tem vasto saber e solta palavras difíceis com naturalidade. Embora aparente perfeição, odeia esforço físico e tem pavor de altura. Prestava serviços à Tenba até rever Lyner.", "Dossiê canônico de Misha lapidado com sua voz erudita; 466B <= 488B"),
    21439: ("PC: Misha", "JP 人C:ミシャ (Person Card de Misha; 19B <= 24B)"),
    21440: ("Jack", "JP ジャック (Guerreiro mercenário Teru; 9B <= 16B)"),
    21441: ("Em Pheyna", "JP イム・フェーナ (Origem de Jack no Santuário de Pheyna; 19B <= 24B)"),
    21442: ("Viajante", "JP 旅人 (Ocupação andarilha de Jack; 17B <= 24B)"),
    21443: ("Aparenta 19", "JP 19歳(外見) (Aparência física jovem de Jack; 23B <= 24B; resolve overflow de 27B da tradução anterior)"),
    21444: ("Misha, charutos", "JP ミシャ、巻きたばこ (Afeições de Jack: proteger Misha e fumar charutos; 29B <= 32B)"),
    21445: ("Gente podre", "JP 腐ったヤツ (Aversões de Jack: canalhas hipócritas; 23B <= 32B)"),
    21446: ("Além das nuvens", "JP 雲平線の果てへの旅 (Sonho de Jack: viajar ao confim do mar de nuvens; 31B <= 32B; resolve overflow de 33B da tradução anterior)"),
    21447: ("Xavecar garotas", "JP ナンパ (Passatempo fanfarrão de Jack; 31B <= 40B)"),
    21448: ("Soberano de mim mesmo", "JP 唯我独尊 (Lema altivo e independente de Jack; 43B <= 48B)"),
    21449: ("Pertence aos Teru, povo que usa magia, mas não sabe usá-la, preferindo armas do Mundo Inferior. Há 4 anos, lutou pela Tenba em Skuwat, onde sofreu graves ferimentos e recebeu um braço mecânico.", "Dossiê canônico de Jack lapidado com histórico militar; 392B <= 472B"),
    21450: ("PC: Jack", "JP 人C:ジャック (Person Card de Jack; 17B <= 24B)"),
    21451: ("Krusche", "JP クルシェ (Garota prodígio engenheira de dirigíveis; 15B <= 16B)"),
    21452: ("Beco Vagalume", "JP ほたる横丁 (Oficina de dirigíveis de Krusche no Mundo Inferior; 27B <= 32B)"),
    21453: ("Engenheira", "JP エンジニア (Profissão de Krusche; 21B <= 24B)"),
    21454: ("15 anos", "JP 15歳 (Idade de Krusche; 15B <= 24B)"),
    21455: ("Bala Gatinho, Luke", "JP 猫飴、ルーク (Gostos de Krusche: o dirigível Luke e doces de Spica; 37B <= 40B)"),
    21456: ("Brócolis", "JP ブロッコリー (Aversão infantil de Krusche a verduras; 17B <= 24B)"),
    21457: ("Cruzar a Blastline", "JP ブラストライン越え (Grande ambição técnica de Krusche; 37B <= 48B)"),
    21458: ("Grathmeld", "JP グラスメルク (Especialidade técnica de síntese de Krusche; 19B <= 24B)")
}

# Principais destaques de curadoria para o relatório executivo
HIGHLIGHTS = [
    {
        "id": 21174,
        "jp": "ビッグガーダー",
        "en": "Big Guarder",
        "before": "Guardião grande",
        "after": "Big Guarder",
        "reason": "JP ビッグガーダー (Bit Ball ampliada; 23B <= 24B; paridade canônica com a família Guarder que elimina estouro de 32B)"
    },
    {
        "id": 21183,
        "jp": "サテライトスター",
        "en": "Satellite Star",
        "before": "Estrela satélite",
        "after": "Satellite Star",
        "reason": "JP サテライトスター (Esfera satélite; 29B <= 32B; soluciona overflow de 34B da tradução preliminar)"
    },
    {
        "id": 21186,
        "jp": "機神の瞳",
        "en": "Eye of Machine God",
        "before": "Olho do Deus Máquina",
        "after": "Olho Deus-Máquina",
        "reason": "JP 機神の瞳 (Olho do Deus-Máquina; 36B <= 40B; concisão literária que elimina estouro de 42B)"
    },
    {
        "id": 21222,
        "jp": "ヘルストーム",
        "en": "Hellstorm",
        "before": "Tempestade infernal",
        "after": "Hellstorm",
        "reason": "JP ヘルストーム (Wyrm alado de tempestades; 19B <= 24B; restaura nome canônico e elimina grave estouro de 39B)"
    },
    {
        "id": 21246,
        "jp": "リュージーン",
        "en": "Drake Lord",
        "before": "Senhor Drake",
        "after": "Lorde Drake",
        "reason": "JP リュージーン (Dragão supremo; 23B <= 24B; elegância aristocrática que corrige overflow de 25B)"
    },
    {
        "id": 21252,
        "jp": "ビーストユーザー / バード / メック",
        "en": "Beast / Bird / Mech User, Master, Lord",
        "before": "Domadora de feras / Operadora mecânica (estouros de 31B a 38B)",
        "after": "Beast / Bird / Mech User, Master, Lord",
        "reason": "JP ビーストユーザー / バードミュール / メックマスター (Padronização das classes de adestradoras dentro do limite rígido de 24B/32B, eliminando 9 overflows)"
    },
    {
        "id": 21321,
        "jp": "エアフォート・ワン",
        "en": "Air Fort One",
        "before": "Fortaleza Aérea Um",
        "after": "Air Fort One",
        "reason": "JP エアフォート・ワン (Fortaleza voadora inspirada em aeronaves imperiais; 25B <= 32B; elimina estouro de 38B)"
    },
    {
        "id": 21368,
        "jp": "プラズマベル付近",
        "en": "Near Plasma Bell",
        "before": "Perto do Sino Plasma",
        "after": "Área da Plasma Bell",
        "reason": "JP プラズマベル付近 (Proximidades da instalação Plasma Bell; 40B <= 40B; resolve overflow de 41B)"
    },
    {
        "id": 21369,
        "jp": "シャドウ頭 / 腹 / 腕",
        "en": "Shadow Head / Body / Arm",
        "before": "Cabeça Sombria / Corpo Sombrio / Braço Sombrio (estouros de 27B a 38B)",
        "after": "Shadow Head / Shadow Body / Shadow Arm",
        "reason": "JP シャドウ頭 / シャドウ腹 / シャドウ腕 (Componentes de batalha da encarnação final de Mir; 23B/23B/21B <= 24B; elimina 6 overflows)"
    },
    {
        "id": 21384,
        "jp": "ミュールの真の姿",
        "en": "Mir’s true form",
        "before": "Forma verdadeira de Mir... (estouro de 247B)",
        "after": "Forma real de Mir. Em essência uma Reyvateil, parece uma garota comum, mas ataca envolta em uma aura de puro ódio.",
        "reason": "JP ミュールの真の姿 (Captura a nuance de ataque da aura e calibra estritamente a 231B <= 240B, resolvendo overflow crítico)"
    },
    {
        "id": 21389,
        "jp": "プラズマベル",
        "en": "Plasma Bell",
        "before": "Sino de plasma",
        "after": "Plasma Bell",
        "reason": "JP プラズマベル (Instalação vital da Torre de Sol Ciel; 23B <= 24B; preserva identidade diegética e elimina estouro de 29B)"
    },
    {
        "id": 21391,
        "jp": "塔の管理者...オリジンと言われている",
        "en": "The administrator... master Pureblooded β-type",
        "before": "Administradora da Torre... matriz das Reyvateils β",
        "after": "Administradora da Torre que rege o continente flutuante. Vida artificial criada na Primeira Era e pioneira das Reyvateils. É a mestra das β de sangue puro, tida como Origin.",
        "reason": "Restaura o título canônico de Origin (オリジン) suprimido pela localização ocidental em inglês; 348B <= 352B"
    },
    {
        "id": 21396,
        "jp": "キャットウォーク",
        "en": "Catwalk",
        "before": "Passarela",
        "after": "Catwalk",
        "reason": "JP キャットウォーク (Passarela industrial de manutenção da Torre; 15B <= 16B; resolve estouro de 19B)"
    },
    {
        "id": 21416,
        "jp": "考えるより即行動",
        "en": "Never think ahead!",
        "before": "Nunca pensar adiante!",
        "after": "Agir sem pensar!",
        "reason": "JP 考えるより即行動 (Lema de ação impulsiva de Lyner; 33B <= 40B; elimina decalque mecânico e corrige estouro de 43B)"
    },
    {
        "id": 21446,
        "jp": "雲平線の果てへの旅",
        "en": "See the world",
        "before": "Conhecer o mundo",
        "after": "Além das nuvens",
        "reason": "JP 雲平線の果てへの旅 (Sonho de Jack de navegar até os limites do horizonte de nuvens; 31B <= 32B; restaura cosmologia e elimina estouro de 33B)"
    }
]

NEW_TERMS = {
    "Eye of Machine God": {
        "pt": "Olho Deus-Máquina",
        "gender": "masculino",
        "number": "singular",
        "category": "Bestiário / Mecânico",
        "note": "Mother Bit colossal ancestral venerada como o olho do Deus-Máquina (JP 機神の瞳)."
    },
    "Plasma Bell": {
        "pt": "Plasma Bell",
        "gender": "feminino",
        "number": "singular",
        "category": "Localização / Instalação",
        "note": "Instalação vital no alto da Torre de Sol Ciel que sustenta a vida no continente flutuante e é vigiada por Kanade."
    },
    "Child of Light": {
        "pt": "Criança da Luz",
        "gender": "feminino",
        "number": "singular",
        "category": "Título / Personagem",
        "note": "Alcunha mística de Kanade (JP 光の御子), a terceira filha androide de manutenção e guardiã da Plasma Bell."
    },
    "PC: [Personagem]": {
        "pt": "PC: [Personagem]",
        "category": "Dossiê / Sistema",
        "note": "Prefixo canônico de Person Card (Card de Personagem / 人C:). Mantido com 'PC:' para concisão de bytes e paridade com a UI."
    }
}

SCENE_HANDOFF_FINAL = {
    "last_scene_id": "BLK_SYS_004",
    "last_line_id": 21458,
    "location_and_situation": "Núcleo Sistêmico Parte 4 (Bestiário avançado, autômatos bélicos, dracos, demônios de Mir, chefes da Torre e dossiers canônicos dos protagonistas Lyner, Aurica, Misha, Jack e Krusche) concluído e 100% calibrado dentro dos tetos de memória.",
    "emotional_state": "Sistêmico / Neutro.",
    "active_hooks": [
        "Encadear com BLK_SYS_005 (continuação dos perfis e dossiers de personagens, aliados, sacerdotes e sistema)."
    ]
}


def main():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    # Obter original_bytes do banco SQLite para conferência cruzada
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, original_bytes, automatic, reviewed FROM dialogues WHERE id BETWEEN 21171 AND 21458")
    db_info = {r[0]: {"max_bytes": r[1], "auto": r[2], "rev": r[3]} for r in c.fetchall()}
    conn.close()

    dialogues_out = []
    lines_rewritten = 0
    lines_approved_as_is = 0

    print("Verificando as 288 falas...")
    for d in input_data.get("dialogues", []):
        d_id = d["id"]
        orig_en = d.get("original_en", "")
        orig_jp = d.get("original_jp", "")
        current_pt = d.get("current_ptbr", "")
        speaker = d.get("speaker", "Sistema / Narração")
        speaker_id = d.get("speaker_id", 0)
        event_file = d.get("event_file", "")
        max_bytes = db_info.get(d_id, {}).get("max_bytes", 9999)

        if d_id not in CURATED_DATA:
            raise ValueError(f"Falta ID {d_id} no dicionário CURATED_DATA!")

        curated_text, justification = CURATED_DATA[d_id]

        # Teste 1: Validação técnica de integridade
        errs = validate_line(d_id, orig_en, curated_text)
        if errs:
            raise ValueError(f"ID {d_id} falhou na validação técnica: {errs}")

        # Teste 2: Limite físico de bytes
        enc_sz = encoded_size(curated_text)
        if enc_sz is None:
            raise ValueError(f"ID {d_id} contém caracteres não suportados pela tabela Shift-JIS do jogo!")
        if enc_sz > max_bytes:
            raise ValueError(f"ID {d_id} excede o teto de bytes: {enc_sz} > {max_bytes} ('{curated_text}')")

        # Contabilização de reescrita vs aprovação
        old_text = db_info[d_id]["rev"] or db_info[d_id]["auto"] or current_pt
        if curated_text != old_text:
            lines_rewritten += 1
        else:
            lines_approved_as_is += 1

        d_entry = {
            "id": d_id,
            "event_file": event_file,
            "speaker_id": speaker_id,
            "speaker": speaker,
            "original_jp": orig_jp,
            "original_en": orig_en,
            "current_ptbr": current_pt,
            "curated_ptbr": curated_text,
            "justification": justification
        }
        dialogues_out.append(d_entry)

    out_obj = {
        "block_id": "BLK_SYS_004",
        "axis_id": "AXIS_1",
        "axis_name": "1_NUCLEO_SISTEMICO_E_MENUS",
        "category": "Bestiário Avançado, Chefes Mecânicos, Demônios de Mir e Dossiês de Personagens",
        "total_lines": len(dialogues_out),
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "new_terms": NEW_TERMS,
        "scene_handoff_final": SCENE_HANDOFF_FINAL,
        "highlights": HIGHLIGHTS,
        "dialogues": dialogues_out
    }

    # Validação em lote pelo validador oficial
    is_valid, all_errors = validate_batch(out_obj)
    if not is_valid:
        raise ValueError(f"Falha no validate_batch com {len(all_errors)} erros!")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out_obj, f, ensure_ascii=False, indent=2)

    print(f"[OK] BLK_SYS_004 gerado com sucesso!")
    print(f"Total: {len(dialogues_out)} falas | Reescritas: {lines_rewritten} | Aprovadas: {lines_approved_as_is}")


if __name__ == "__main__":
    main()

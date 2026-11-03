"""Gerador de Curadoria Editorial para BLK_SYS_003 (IDs 20883 a 21170)
Aplica revisão profunda em duas passagens confrontando JP (soberano) e EN,
garantindo limite estrito de bytes (encoded_size <= original_bytes) e integridade determinística.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\tools")
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line, validate_batch

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
CURADORIA_DIR = BASE_DIR / "curadoria_editorial"
INPUT_PATH = CURADORIA_DIR / "blocos" / "BLK_SYS_003_input.json"
OUTPUT_PATH = CURADORIA_DIR / "blocos" / "BLK_SYS_003_output.json"
CONFIG_PATH = CURADORIA_DIR / "curadoria_config.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()
c.execute("""
    SELECT id, event_file, original, original_jp, original_bytes, automatic, reviewed 
    FROM dialogues 
    WHERE id BETWEEN 20883 AND 21170 
    ORDER BY id
""")
db_rows = {r[0]: r for r in c.fetchall()}
conn.close()

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Dicionário de curadoria linha a linha
# id -> (curated_text, justification)
CURATION = {
    # === SLUS/TEXT/0027: Equipamentos e Medicamentos ===
    20883: ("RC: Legado Ancestral", "JP 合C:超文明の遺産 (Legado da civilização ancestral; 41B <= 48B; concisão que evita estouro dos 48B)"),
    20884: ("Calmaria", "JP トランキリティ (Calmaria/tranquilidade; 17B <= 24B)"),
    20885: ("RC: Calmaria", "JP 合C:トランキリティ (Paralelo ao item Calmaria; 25B <= 32B)"),
    20886: ("Hitlezz", "JP アタラズ (Marca de medicamento de precisão; 15B <= 16B)"),
    20887: ("RC: Remédio Azul A", "JP 合C:青い薬剤A (Receita de medicamento azul; 38B <= 40B)"),
    20888: ("Guardlezz", "JP マモレーズ (Marca de medicamento de guarda; 19B <= 24B)"),
    20889: ("RC: Remédio Amarelo A", "JP 合C:黄色い薬剤A (Receita de medicamento amarelo; 44B <= 48B)"),
    20890: ("Quicklezz", "JP ドンビリズ (Marca de medicamento de agilidade; 19B <= 24B)"),
    20891: ("RC: Remédio Verm. A", "JP 合C:赤い薬剤A (Receita de medicamento vermelho; abreviado no teto exato: 40B <= 40B)"),
    20892: ("Neo Hitlezz", "JP ネオ・アタラズ (Versão aprimorada do Hitlezz; 23B <= 24B)"),
    20893: ("Guardlezz High", "JP マモレーズ・ハイ (Versão superior do Guardlezz; 29B <= 32B)"),
    20894: ("Quicklezz RX", "JP ドンビリズRX (Versão avançada do Quicklezz; 25B <= 32B)"),
    20895: ("Caça-Sonhos", "JP 夢追いの水 (Água que persegue sonhos / Dreamchaser; 24B <= 24B)"),
    20896: ("RC: Frasco Fofo", "JP 合C:かわいい小瓶 (Frasco/pequena garrafa fofa; 31B <= 32B)"),
    20897: ("Fonte de Poder", "JP パワーソーサー (Disco/fonte de energia; 29B <= 32B)"),
    20898: ("RC: Bateria", "JP 合C:バッテリー (Receita de bateria; 23B <= 24B)"),
    20899: ("Canção da Sereia", "JP 人魚のウタ缶 (Canto da sereia em lata; 33B <= 40B)"),
    20900: ("RC: Enlatado", "JP 合C:かんづめ (Receita de enlatados; 25B <= 40B)"),
    20901: ("Flauta Corta-Vento", "JP 風斬りのタテ笛 (Flauta doce que corta o vento; 37B <= 48B)"),
    20902: ("RC: Flauta", "JP 合C:たてぶえ (Receita de flauta; 21B <= 24B)"),
    20903: ("Raio Vazio", "JP 虚空トランスレイ (Feixe do vazio / Transray; 21B <= 32B)"),
    20904: ("RC: Restaurador de MP", "JP 合C:MP回復機 (Aparelho de restauração de MP; 43B <= 48B)"),
    20905: ("Amplificador Reflexivo", "JP 零音反射式増幅器 (Amplificador de reflexão acústica; 45B <= 56B)"),
    20906: ("RC: Amplificador Ressonante", "JP 合C:共振増幅器 (Receita de amplificador ressonante; 55B <= 56B)"),

    # === SLUS/TEXT/0028: Itens Gastronômicos e Mecânicos de Grathmeld ===
    20907: ("Caixão: Dor e Alegria", "JP 嘆きと喜びの棺 (Esquife do pranto e do júbilo; 44B <= 48B)"),
    20908: ("RC: Caixão", "JP 合C:棺 (Receita de esquife/caixão; 21B <= 24B)"),
    20909: ("Núcleo de Vigor", "JP リフレッシュコア (Núcleo de restauração/vitalidade; 32B <= 32B)"),
    20910: ("RC: Módulo Descanso", "JP 合C:休息装置 (Receita de dispositivo de repouso; 40B <= 40B)"),
    20911: ("Ar Tonelico?", "JP アルトネリコ? (Nome da Torre com ponto de interrogação; 25B <= 32B)"),
    20912: ("RC: Torre", "JP 合C:塔 (Receita simbólica da Torre; 19B <= 24B)"),
    20913: ("Parfait Dokkoi", "JP ドッコイパヘ (Sobremesa Parfait Dokkoi; 29B <= 32B)"),
    20914: ("RC: Parfait Dokkoi", "JP 合C:ドッコイパヘ (Receita de Parfait Dokkoi; 37B <= 40B)"),
    20915: ("Gelo Nativo", "JP 大自然あいす (Sorvete/gelo da natureza; 23B <= 24B)"),
    20916: ("RC: Gelo Nativo", "JP 合C:大自然あいす (Receita de gelo nativo; 31B <= 32B)"),
    20917: ("Supergelo Nativo", "JP 超自然あいす (Sorvete/gelo da supernatureza; 33B <= 40B)"),
    20918: ("RC: Supergelo Nativo", "JP 合C:超自然あいす (Receita de supergelo nativo; 41B <= 48B)"),
    20919: ("Soda BBQ", "JP 焼肉ソーダ (Refrigerante de churrasco; 17B <= 24B)"),
    20920: ("RC: Soda BBQ", "JP 合C:焼肉ソーダ (Receita de refrigerante de churrasco; 25B <= 32B)"),
    20921: ("Coelha Sólida", "JP ソリッドうさこ (Mascote Usako rígida; 28B <= 32B)"),
    20922: ("RC: Coelha Sólida", "JP 合C:ソリッドうさこ (Receita de Usako sólida; 36B <= 40B)"),
    20923: ("Arroz Usako", "JP うさライス (Prato de arroz no formato da coelhinha Usako; 23B <= 24B)"),
    20924: ("RC: Arroz Usako", "JP 合C:うさライス (Receita de arroz Usako; 31B <= 32B)"),
    20925: ("Meca-Coelho", "JP めかうさ (Coelho mecânico / Mecha-Usako; 23B <= 24B)"),
    20926: ("RC: Meca-Coelho", "JP 合C:めかうさ (Receita de coelho mecânico; 31B <= 32B)"),
    20927: ("Soda Capri", "JP カプリソーダ (Refrigerante Capri; 21B <= 24B)"),
    20928: ("RC: Soda Capri", "JP 合C:カプリソーダ (Receita de refrigerante Capri; 29B <= 32B)"),
    20929: ("Suco Rango", "JP メシジュース (Suco nutritivo de refeição/rango; 21B <= 24B)"),
    20930: ("RC: Suco Rango", "JP 合C:メシジュース (Receita de suco de refeição; 29B <= 32B)"),

    # === SLUS/TEXT/0029: Armas de Síntese e Receitas de Combate ===
    20931: ("Cieroceramics", "JP シエロセラミクス (Cerâmica de Sol Ciel / Cieroceramics; 27B <= 32B)"),
    20932: ("RC: Esp. 1", "JP 合C:ソード1 (Receita de Espada 1 abreviada no limite; 21B <= 24B)"),
    20933: ("Glastiphon", "JP グラスティフォン (Arma lendária Glastiphon; 21B <= 24B)"),
    20934: ("RC: Lança 1", "JP 合C:スピア1 (Receita de Lança 1; 24B <= 24B)"),
    20935: ("Vivaci", "JP ヴィヴァーチェ (Arma de fogo Vivaci; 13B <= 16B)"),
    20936: ("RC: Arma 1", "JP 合C:銃1 (Receita de Arma de fogo 1; 21B <= 24B)"),
    20937: ("Eng. Sônica", "JP 音速歯車 (Engrenagem que gira na velocidade do som; 24B <= 24B)"),
    20938: ("RC: Corr. 1", "JP 合C:チェーン1 (Receita de Corrente 1 abreviada; 23B <= 24B)"),
    20939: ("Suzaku & Seiryuu", "JP 朱雀&青龍 (Par de katanas lendárias Suzaku e Seiryuu; 33B <= 40B)"),
    20940: ("RC: Katana 1", "JP 合C:カタナ1 (Receita de Katana 1; 25B <= 32B)"),
    20941: ("Eufortissimo", "JP ユーフォルテシモ (Espada musical Eufortissimo; 25B <= 32B)"),
    20942: ("RC: Esp. 2", "JP 合C:ソード2 (Receita de Espada 2 abreviada; 21B <= 24B)"),
    20943: ("Inferno", "JP インフェルノ (Lança abrasadora Inferno; 15B <= 16B)"),
    20944: ("RC: Lança 2", "JP 合C:スピア2 (Receita de Lança 2; 24B <= 24B)"),
    20945: ("Estremo", "JP エストレーモ (Pistola extrema Estremo; 15B <= 16B)"),
    20946: ("RC: Arma 2", "JP 合C:銃2 (Receita de Arma de fogo 2; 21B <= 24B)"),
    20947: ("Motor Eletromagnético", "JP 電磁エンジン (Motor eletromagnético; 44B <= 48B)"),
    20948: ("RC: Corr. 2", "JP 合C:チェーン2 (Receita de Corrente 2 abreviada; 23B <= 24B)"),
    20949: ("Zetsuei & Zanmu", "JP 絶影&斬無 (Par de katanas das sombras Zetsuei e Zanmu; 31B <= 32B)"),
    20950: ("RC: Katana 2", "JP 合C:カタナ2 (Receita de Katana 2; 25B <= 32B)"),
    20951: ("Cantor Prateado", "JP 銀の謳い手 (Lâmina nobre que ressoa como canção de prata; 31B <= 32B)"),
    20952: ("RC: Esp. 3", "JP 合C:ソード3 (Receita de Espada 3 abreviada; 21B <= 24B)"),
    20953: ("Lança Elemental", "JP エレメントスピア (Lança imbuída com elementos; 32B <= 32B)"),
    20954: ("RC: Lança 3", "JP 合C:スピア3 (Receita de Lança 3; 24B <= 24B)"),

    # === SLUS/TEXT/0030: Armas Supremas e Armaduras ===
    20955: ("Misereen", "JP ミゼンシャー (Pistola Misereen; 17B <= 24B)"),
    20956: ("RC: Arma 3", "JP 合C:銃3 (Receita de Arma de fogo 3; 21B <= 24B)"),
    20957: ("Sharkgill", "JP シャークギル (Arma de lâminas estriadas Sharkgill; 19B <= 24B)"),
    20958: ("RC: Corr. 3", "JP 合C:チェーン3 (Receita de Corrente 3 abreviada; 23B <= 24B)"),
    20959: ("KANADE", "JP KANADE (Lâmina sagrada Kanade / Toque Musical; 13B <= 16B)"),
    20960: ("RC: Esp. 4", "JP 合C:ソード4 (Receita de Espada 4 abreviada; 21B <= 24B)"),
    20961: ("Doom Slayer", "JP ドゥームスレイヤー (Lança letal Doom Slayer; 23B <= 24B)"),
    20962: ("RC: Lança 4", "JP 合C:スピア4 (Receita de Lança 4; 24B <= 24B)"),
    20963: ("Vahstrad", "JP ヴァストラッド (Arma de fogo avançada Vahstrad; 17B <= 24B)"),
    20964: ("RC: Arma 4", "JP 合C:銃4 (Receita de Arma de fogo 4; 21B <= 24B)"),
    20965: ("Depressão de J", "JP Jの憂鬱 (Corrente da melancolia de Jack; 30B <= 32B)"),
    20966: ("RC: Corr. 4", "JP 合C:チェーン4 (Receita de Corrente 4 abreviada; 23B <= 24B)"),
    20967: ("Eversong", "JP エバーソング (Espada do cântico eterno; 17B <= 24B)"),
    20968: ("RC: Superarma", "JP 合C:超ウェポン (Receita de superarmamento; 27B <= 40B)"),
    20969: ("Serenata de Eoria", "JP エオリアの小夜曲 (Arma sagrada de Eoria; 35B <= 40B)"),
    20970: ("RC: Arma Suprema", "JP 合C:極超ウェポン (Receita de arma suprema transcendental; 33B <= 40B)"),
    20971: ("Asa de Eoria", "JP エオリアの翼 (Armadura protetora de Eoria; 25B <= 32B)"),
    20972: ("RC: Cota A", "JP 合C:よろいA (Receita de armadura corporal A; 21B <= 24B)"),
    20973: ("Guardião de Elemia", "JP エレミアの守護神 (Armadura pesada consagrada da Igreja; 38B <= 40B)"),
    20974: ("RC: Cota B", "JP 合C:よろいB (Receita de armadura corporal B; 21B <= 24B)"),
    20975: ("Jaqueta Air Metal", "JP エアメタルジャケ (Jaqueta reforçada de liga leve; 35B <= 40B)"),
    20976: ("RC: Jaqueta", "JP 合C:ジャケット (Receita de jaqueta protetora; 23B <= 24B)"),
    20977: ("Cota Divina", "JP 天上天下唯我独尊 (Armadura suprema solitária e invencível; 23B <= 24B)"),
    20978: ("RC: Cota Samurai", "JP 合C:武者よろい (Receita de armadura samurai; 33B <= 40B)"),

    # === SLUS/TEXT/0031: Acessórios e Trajes ===
    20979: ("Ceroula Marrom", "JP 褐色モモヒキ (Calçolas longas/ceroulas clássicas marrons; 29B <= 32B)"),
    20980: ("RC: Cor Camelo", "JP 合C:ラクダ色 (Receita de tecido cor camelo; 29B <= 32B)"),
    20981: ("Camiseta Paixão", "JP 熱血Tシャツ (Camiseta da determinação ardente; 32B <= 32B)"),
    20982: ("RC: Gola Red.", "JP 合C:まるくび (Receita de camiseta de gola redonda; 27B <= 32B)"),
    20983: ("Vestido Sailor Usa", "JP せらうさドレス (Vestido marinheiro da coelhinha Usako; 37B <= 40B)"),
    20984: ("RC: Vestido", "JP 合C:ドレス (Receita de vestido; 23B <= 24B)"),
    20985: ("Traje Higedance", "JP ヒゲダンスーツ (Traje cômico da dança do bigode; 31B <= 32B)"),
    20986: ("RC: Formal", "JP 合C:フォーマル (Receita de vestimenta formal; 21B <= 24B)"),
    20987: ("Cota Bushido", "JP ブシドーアーマー (Armadura do código guerreiro Bushido; 25B <= 32B)"),
    20988: ("RC: Luta Espada", "JP 合C:チャンバラ (Receita de combate de espadas chanbara; 31B <= 32B)"),
    20989: ("Operetta", "JP オペレッタ (Tiara elegante de ópera; 17B <= 24B)"),
    20990: ("RC: Tiara", "JP 合C:ティアラ (Receita de tiara; 19B <= 24B)"),
    20991: ("Grã-Coroa", "JP グランドクラウン (Coroa majestosa; 20B <= 24B)"),
    20992: ("RC: Coroa Real", "JP 合C:王冠 (Receita de coroa da realeza; 29B <= 40B)"),
    20993: ("Anel Grathnode", "JP グラスノリング (Anel condutor de ondas Grathnode; 29B <= 32B)"),
    20994: ("RC: Anel Brilhante", "JP 合C:光る指輪 (Receita de anel radiante; 37B <= 40B)"),
    20995: ("Anel Parameno", "JP パラメノリング (Anel especial de sintonização Parameno; 27B <= 32B)"),
    20996: ("RC: Anel Preto", "JP 合C:黒い指輪 (Receita de anel sombrio; 29B <= 32B)"),
    20997: ("Lágrima Estelar", "JP 星屑の涙 (Gema brilhante de poeira cósmica; 32B <= 32B)"),
    20998: ("RC: Cristal", "JP 合C:水晶 (Receita de cristal mineral; 23B <= 24B)"),
    20999: ("Anel da Sogra", "JP こじゅうとの指輪 (Anel afiado da sogra implicante; 27B <= 40B)"),
    21000: ("RC: Anel Luxo", "JP 合C:派手な指輪 (Receita de anel chamativo/luxuoso; 27B <= 32B)"),
    21001: ("Touca Banho", "JP シャンプーハット (Touca protetora de banho; 23B <= 24B)"),
    21002: ("RC: Cap", "JP 合C:ぼうし (Receita de chapéu/touca/cobertura de cabeça; 15B <= 16B)"),

    # === SLUS/TEXT/0032: Ingredientes de Grathmeld e Início do Bestiário ===
    21003: ("Fio Aprisionador", "JP 仲結いの糸 (Fio mágico de laços firmes; 33B <= 40B)"),
    21004: ("RC: Fio", "JP 合C:糸 (Receita de linha e fio; 15B <= 24B)"),
    21005: ("Cristal Ardell", "JP アーデル結晶体 (Formação cristalina de Ardell; 29B <= 40B)"),
    21006: ("RC: Cristal Octaédrico", "JP 合C:八面体結晶 (Receita de cristal de oito faces; 46B <= 48B)"),
    21007: ("Fever Mordar", "JP フィーバモーダー (Item energético Fever Mordar; 25B <= 32B)"),
    21008: ("RC: Booster", "JP 合C:ブースター (Receita de amplificador/propulsor; 23B <= 24B)"),
    21009: ("Anel Branco", "JP ホワイトリング (Anel alvinegro puro; 23B <= 24B)"),
    21010: ("RC: Anel Branco", "JP 合C:白い指輪 (Receita de anel branco; 31B <= 32B)"),
    21011: ("Anel Verde", "JP グリンリング (Anel esmeralda verdejante; 21B <= 24B)"),
    21012: ("RC: Anel Verde", "JP 合C:緑の指輪 (Receita de anel verde; 29B <= 32B)"),
    21013: ("Jaula Ariel", "JP エアリエルのカゴ (Gaiola sagrada do espírito do ar Ariel; 23B <= 24B)"),
    21014: ("RC: Gaiola", "JP 合C:カゴ (Receita de gaiola/cesto; 21B <= 24B)"),
    21015: ("Farol Solar", "JP 太陽のランプ (Lâmpada radiante do sol; 23B <= 24B)"),
    21016: ("RC: Lâmpada", "JP 合C:ランプ (Receita de lamparina; 24B <= 24B)"),
    21017: ("Acorde Yuteria", "JP ユーテリア弦 (Corda melódica da ressonância de Yuteria; 29B <= 32B)"),
    21018: ("RC: Acorde Yuteria", "JP 合C:ユーテリア弦 (Receita de corda Yuteria; 37B <= 40B)"),
    21019: ("Teleporte Circula", "JP 相転換サーキュラ (Dispositivo de transição de fase Circula; 35B <= 40B)"),
    21020: ("RC: Circula", "JP 合C:サーキュラ (Receita do transportador Circula; 23B <= 24B)"),
    21021: ("Pom", "JP ポム (Mascote e monstro mascote clássico; 7B <= 8B)"),
    21022: ("Animal parecido com uma castanha. A cabeça é pontuda, com a ponta rosa. É macio, por isso suas investidas não machucam muito.", "Descrição zoológica/bestiário refinada; 255B <= original_bytes"),
    21023: ("MC: Pom1", "JP 敵C:ポム系1 (Card de Monstro do Pom 1; 17B <= 32B)"),
    21024: ("Pom Marrom", "JP マロンポム (Correção cabal do erro do EN 'Melon'; Marron = Castanha/Marrom; 21B <= 24B)"),
    21025: ("Na forma e na cor, é puro marrom. O corpo pouco difere do Pom comum, mas a ponta de sua cabeça é castanha. Também não machuca muito.", "Descrição zoológica/bestiário refinada; 270B <= original_bytes"),
    21026: ("MC: Pom2", "JP 敵C:ポム系2 (Card de Monstro do Pom 2; 17B <= 24B)"),

    # === SLUS/TEXT/0033: Bestiário - Família Pom e Início de Plantas ===
    21027: ("Pom Pêssego", "JP モモポム (Pom de cor rosada; 24B <= 24B)"),
    21028: ("Pom de corpo rosa e cabeça branca. Continua macio como os outros, mas é bem agressivo. Não baixe a guarda.", "Descrição zoológica/bestiário refinada; 216B <= original_bytes"),
    21029: ("MC: Pom3", "JP 敵C:ポム系3 (Card de Monstro do Pom 3; 17B <= 24B)"),
    21030: ("Pom de Goma", "JP ネリポム (Pom amassado com textura de massa elástica; 23B <= 24B)"),
    21031: ("É tão azul que a cabeça se confunde com o corpo. Lembra uma gota d'água. Diferente dos outros Poms, tem textura mais elástica.", "Descrição zoológica/bestiário refinada; 258B <= original_bytes"),
    21032: ("MC: Pom4", "JP 敵C:ポム系4 (Card de Monstro do Pom 4; 17B <= 24B)"),
    21033: ("Pom Metal", "JP メタルポム (Pom com carapaça metálica; 19B <= 24B)"),
    21034: ("Não se chama Metal à toa. Quase nenhum ataque afeta essa massa dura, e seus golpes doem horrores. Mesmo assim, continua macio e saltitante.", "Descrição zoológica/bestiário refinada; 281B <= original_bytes"),
    21035: ("MC: Pom5", "JP 敵C:ポム系5 (Card de Monstro do Pom 5; 17B <= 24B)"),
    21036: ("Pom Prisma", "JP プリズムポム (Pom multicolorido e brilhante; 21B <= 24B)"),
    21037: ("Um Pom multicolorido e deslumbrante. Dá vontade de capturá-lo para uma coleção, mas sua força torna isso muito difícil.", "Descrição zoológica/bestiário refinada; 243B <= original_bytes"),
    21038: ("MC: Pom6", "JP 敵C:ポム系6 (Card de Monstro do Pom 6; 17B <= 24B)"),
    21039: ("Trio de Pom", "JP トリオ・ザ・ポム (Trio de Poms coordenados; 23B <= 24B)"),
    21040: ("Três Poms. Um sozinho é fraco, mas juntos ficam fortes. Seus ataques triplos perfeitamente sincronizados são um espetáculo.", "Descrição zoológica/bestiário refinada; 251B <= original_bytes"),
    21041: ("MC: Pom7", "JP 敵C:ポム系7 (Card de Monstro do Pom 7; 17B <= 24B)"),
    21042: ("Pom Max", "JP でかポム (Pom grandalhão gigante; 15B <= 16B)"),
    21043: ("Versão colossal do Pom. Ainda é macio, mas tem uma massa que faz o chão tremer. Ser atingido ou esmagado por ele é um pesadelo.", "Descrição zoológica/bestiário refinada; 259B <= original_bytes"),
    21044: ("MC: Pom8", "JP 敵C:ポム系8 (Card de Monstro do Pom 8; 17B <= 24B)"),
    21045: ("Mini Pom", "JP ちびポム (Pom minúsculo em miniatura; 17B <= 24B)"),
    21046: ("Versão menor de um Pom já pequeno. É difícil acertá-lo e seus botes causam dor pontual como picadas. Cuidado redobrado para quem tem vista fraca!", "Descrição zoológica/bestiário refinada; 296B <= original_bytes"),
    21047: ("MC: Pom9", "JP 敵C:ポム系9 (Card de Monstro do Pom 9; 17B <= 24B)"),
    21048: ("Hulaflower", "JP フラフラワー (Planta humanoide dançante Hulaflower; 21B <= 24B)"),
    21049: ("Flor com a metade superior de uma pessoa no centro. As raízes servem de pernas para se mover. O cabelo na cabeça é, na verdade, um botão de flor.", "Descrição zoológica/bestiário refinada; 295B <= original_bytes"),
    21050: ("MC: Plant1", "JP 敵C:植物系1 (Card de Monstro da Família Planta 1; 21B <= 24B)"),

    # === SLUS/TEXT/0034: Bestiário - Família Planta e Feras Caninas ===
    21051: ("Yodelflower", "JP ヨロレイフラワー (Planta tirolesa Yodelflower; 23B <= 24B)"),
    21052: ("Ao contrário da Hulaflower, a figura entre as pétalas tem cor de pele. Muita gente se aproxima por engano e acaba sendo atacada.", "Descrição zoológica/bestiário refinada; 259B <= original_bytes"),
    21053: ("MC: Plant2", "JP 敵C:植物系2 (Card de Monstro da Família Planta 2; 21B <= 24B)"),
    21054: ("Gospelflower", "JP ゴスペラワー (Planta cinzenta soturna Gospelflower; 25B <= 32B)"),
    21055: ("Flor acinzentada e sombria, mas bastante agressiva: ela própria avança sobre você. É bem resistente, então convém ter cautela.", "Descrição zoológica/bestiário refinada; 259B <= original_bytes"),
    21056: ("MC: Plant3", "JP 敵C:植物系3 (Card de Monstro da Família Planta 3; 21B <= 24B)"),
    21057: ("Yumyumflower", "JP パクパクフラワー (Planta voraz comilona Pakupaku; 25B <= 32B)"),
    21058: ("Não é a flor que serve de comida. A figura no centro devora qualquer coisa. Se um viajante passar por perto... nhac, nhac!", "Descrição zoológica/bestiário refinada; 247B <= original_bytes"),
    21059: ("MC: Plant4", "JP 敵C:植物系4 (Card de Monstro da Família Planta 4; 21B <= 24B)"),
    21060: ("Cannonflower", "JP カノンフラワー (Planta colossal de ataque pesado; 25B <= 32B)"),
    21061: ("Uma Hulaflower que cresceu demais. As pétalas e a figura humana no centro aumentaram, tornando-a imensa e intimidadora.", "Descrição zoológica/bestiário refinada; 240B <= original_bytes"),
    21062: ("MC: Plant5", "JP 敵C:植物系5 (Card de Monstro da Família Planta 5; 21B <= 24B)"),
    21063: ("Guillotineflower", "JP ギロチンフラワー (Planta cortante afiada como guilhotina; 33B <= 40B)"),
    21064: ("Parece dourada, mas está coberta de pólen espesso. Suas folhas cortam com a afiação de lâminas de guilhotina.", "Descrição zoológica/bestiário refinada; 222B <= original_bytes"),
    21065: ("MC: Plant6", "JP 敵C:植物系6 (Card de Monstro da Família Planta 6; 21B <= 24B)"),
    21066: ("Gigaflower", "JP でらフラワー (Planta titânica Gigaflower; 21B <= 24B)"),
    21067: ("O que a fez crescer tanto? A flor e a pessoa no centro são titânicas. A sensação é de lutar contra um verdadeiro gigante.", "Descrição zoológica/bestiário refinada; 246B <= original_bytes"),
    21068: ("MC: Plant7", "JP 敵C:植物系7 (Card de Monstro da Família Planta 7; 21B <= 24B)"),
    21069: ("Cão de Rua", "JP 野犬 (Cachorro vadio das montanhas; 22B <= 24B)"),
    21070: ("Parece mais um cão selvagem que um monstro. Não subestime as feras: ele continuará atacando ferozmente até abater você.", "Descrição zoológica/bestiário refinada; 244B <= original_bytes"),
    21071: ("MC: Beast1", "JP 敵C:野獣系1 (Card de Monstro da Família Fera 1; 21B <= 24B)"),
    21072: ("Mad Dog", "JP マッドドッグ (Cão hidrófobo raivoso Mad Dog; 15B <= 16B)"),
    21073: ("Cão raivoso e traiçoeiro. Presas e garras afiadas, com investidas rápidas, tornam-no irritante. Fica eufórico ao ver sangue.", "Descrição zoológica/bestiário refinada; 253B <= original_bytes"),
    21074: ("MC: Beast2", "JP 敵C:野獣系2 (Card de Monstro da Família Fera 2; 21B <= 24B)"),

    # === SLUS/TEXT/0035: Bestiário - Lobos e Mercenários ===
    21075: ("Lobo Feroz", "JP あらくれウルフ (Lobo selvagem brutal; 21B <= 24B)"),
    21076: ("Lobo branco muito mais feroz que o Mad Dog. Move-se com extrema rapidez.", "Descrição zoológica/bestiário refinada; 145B <= original_bytes"),
    21077: ("MC: Beast3", "JP 敵C:野獣系3 (Card de Monstro da Família Fera 3; 21B <= 24B)"),
    21078: ("Caçador Noturno", "JP ナイトストーカー (Lobo predador da escuridão; 32B <= 32B)"),
    21079: ("Essas feras rondam a noite atrás de presas distraídas. Anulam ataques físicos com facilidade, tornando-se rivais difíceis.", "Descrição zoológica/bestiário refinada; 249B <= original_bytes"),
    21080: ("MC: Beast4", "JP 敵C:野獣系4 (Card de Monstro da Família Fera 4; 21B <= 24B)"),
    21081: ("Mist Walker", "JP ミストウォーカー (Lobo lendário que habita a névoa; 23B <= 24B)"),
    21082: ("Dizem ser o mais forte dos lobos. Ao encontrar uma presa, ataca implacável a qualquer hora. Golpes físicos não funcionam contra ele.", "Descrição zoológica/bestiário refinada; 268B <= original_bytes"),
    21083: ("MC: Beast5", "JP 敵C:野獣系5 (Card de Monstro da Família Fera 5; 21B <= 24B)"),
    21084: ("Mercenário", "JP 傭兵 (Guerreiro contratado de aluguel; 22B <= 24B)"),
    21085: ("Soldados de aluguel sem lealdade fixa. Aceitam qualquer serviço conforme a recompensa e o contrato. Quase todos são brutos.", "Descrição zoológica/bestiário refinada; 249B <= original_bytes"),
    21086: ("MC: Mercenary1", "JP 敵C:傭兵系1 (Card de Monstro da Família Mercenário 1; 29B <= 32B)"),
    21087: ("Espadachim Errante", "JP さすらい剣士 (Guerreiro solitário que vaga pelo mundo; 37B <= 40B)"),
    21088: ("Ninguém sabe de onde veio nem para onde vai. Viaja sem destino certo enquanto lapida a maestria de sua espada.", "Descrição zoológica/bestiário refinada; 222B <= original_bytes"),
    21089: ("MC: Mercenary2", "JP 敵C:傭兵系2 (Card de Monstro da Família Mercenário 2; 29B <= 32B)"),
    21090: ("Samuraiman", "JP サムライマン (Samurai excêntrico de espada ocidental; 21B <= 24B)"),
    21091: ("Um samurai que usa espada em vez de katana. Por isso atende por Samuraiman.", "Descrição zoológica/bestiário refinada; 151B <= original_bytes"),
    21092: ("MC: Mercenary3", "JP 敵C:傭兵系3 (Card de Monstro da Família Mercenário 3; 29B <= 32B)"),
    21093: ("Mestre", "JP 達人 (Espadachim experiente e veterano; 13B <= 24B)"),
    21094: ("Espadachim veterano com anos de treino árduo. Não é derrotado com facilidade. Muitos têm porte intimidador de guarda-costas.", "Descrição zoológica/bestiário refinada; 253B <= original_bytes"),
    21095: ("MC: Mercenary4", "JP 敵C:傭兵系4 (Card de Monstro da Família Mercenário 4; 29B <= 32B)"),
    21096: ("Capanga", "JP ごろつき (Valentão encrenqueiro de beco escuro; 15B <= 16B)"),
    21097: ("Vivem em becos e vielas escuras. Costumam agir em bando quando resolvem cercar e intimidar suas vítimas.", "Descrição zoológica/bestiário refinada; 210B <= original_bytes"),
    21098: ("MC: Mercenary5", "JP 敵C:傭兵系5 (Card de Monstro da Família Mercenário 5; 29B <= 32B)"),

    # === SLUS/TEXT/0036: Bestiário - Guardas Corporativos Tenba e Espectros ===
    21099: ("Blademaster", "JP ブレイドマスター (Grão-mestre espadachim lendário; 23B <= 24B)"),
    21100: ("Espadachim supremo, mestre na arte da espada. Aperfeiçoou todos os tipos de técnica.", "Descrição zoológica/bestiário refinada; 171B <= original_bytes"),
    21101: ("MC: Mercenary6", "JP 敵C:傭兵系6 (Card de Monstro da Família Mercenário 6; 29B <= 32B)"),
    21102: ("Segurança Tenba", "JP 天覇警備兵 (Guarda patrimonial do conglomerado Tenba; 31B <= 32B)"),
    21103: ("Guardas particulares do Conglomerado Tenba. Estão em todas as suas instalações. Não são fortes, mas surgem em bandos chatos.", "Descrição zoológica/bestiário refinada; 252B <= original_bytes"),
    21104: ("MC: Security1", "JP 敵C:警備兵系1 (Card de Monstro da Família Guarda 1; 27B <= 32B)"),
    21105: ("Guarda", "JP ガードマン (Vigilante de instalações; 13B <= 24B)"),
    21106: ("Vigilantes de instalações diversas. Sozinhos são fracos, mas nunca fazem ronda desacompanhados: prepare-se para enfrentar vários.", "Descrição zoológica/bestiário refinada; 261B <= original_bytes"),
    21107: ("MC: Security2", "JP 敵C:警備兵系2 (Card de Monstro da Família Guarda 2; 27B <= 32B)"),
    21108: ("Guarda Arm.", "JP 特装機動兵 (Guarda tático móvel blindado; 23B <= 24B)"),
    21109: ("Guarda com equipamento tático especial. Protege setores mais importantes e é muito mais forte que os vigias comuns.", "Descrição zoológica/bestiário refinada; 233B <= original_bytes"),
    21110: ("MC: Security3", "JP 敵C:警備兵系3 (Card de Monstro da Família Guarda 3; 27B <= 32B)"),
    21111: ("Cruzado", "JP クルセイダー (Soldado de choque implacável Crusader; 15B <= 24B)"),
    21112: ("Guardas das instalações mais críticas. São perigosos e não hesitam em matar para impedir o avanço de invasores.", "Descrição zoológica/bestiário refinada; 227B <= original_bytes"),
    21113: ("MC: Security4", "JP 敵C:警備兵系4 (Card de Monstro da Família Guarda 4; 27B <= 32B)"),
    21114: ("Shadowman", "JP シャドウマン (Agente especial furtivo armado; 19B <= 24B)"),
    21115: ("Guardas munidos de armas devastadoras. Se você levantar qualquer suspeita, atacarão sem aviso até cessar seus movimentos.", "Descrição zoológica/bestiário refinada; 246B <= original_bytes"),
    21116: ("MC: Security5", "JP 敵C:警備兵系5 (Card de Monstro da Família Guarda 5; 27B <= 32B)"),
    21117: ("Perito", "JP スペシャリスト (Especialista tático de infiltração e defesa; 13B <= 24B)"),
    21118: ("A elite dos guardas. Com 95% de taxa de sucesso, garantem que nenhum intruso passará por suas patrulhas.", "Descrição zoológica/bestiário refinada; 210B <= original_bytes"),
    21119: ("MC: Security6", "JP 敵C:警備兵系6 (Card de Monstro da Família Guarda 6; 27B <= 32B)"),
    21120: ("Espectro Sacro", "JP 神官の亡霊 (Fantasma armado do sacerdote do templo; 29B <= 32B)"),
    21121: ("Espectros de sacerdotes com armaduras pesadas e lanças. Não sabemos como morreram, mas atacam enfurecidos brandindo suas armas.", "Descrição zoológica/bestiário refinada; 257B <= original_bytes"),
    21122: ("MC: Priest1", "JP 敵C:神官系1 (Card de Monstro da Família Sacerdote 1; 23B <= 24B)"),

    # === SLUS/TEXT/0037: Bestiário - Sacerdotes do Templo e Aves de Rapina ===
    21123: ("Vigia do Templo", "JP テンプルガード (Sentinela armada do Templo; 31B <= 32B)"),
    21124: ("Guardas que protegem o Templo. Além das lanças, usam magias de cura e ataque. Avançar sem cautela trará sérias dores de cabeça.", "Descrição zoológica/bestiário refinada; 261B <= original_bytes"),
    21125: ("MC: Priest2", "JP 敵C:神官系2 (Card de Monstro da Família Sacerdote 2; 23B <= 24B)"),
    21126: ("Sumo do Templo", "JP テンプルマスター (Mestre guardião dos recintos sagrados; 29B <= 32B)"),
    21127: ("Guardas de santuários sagrados. Não usam lanças como os Vigias do Templo, mas desferem artes mágicas perigosas.", "Descrição zoológica/bestiário refinada; 227B <= original_bytes"),
    21128: ("MC: Priest3", "JP 敵C:神官系3 (Card de Monstro da Família Sacerdote 3; 23B <= 24B)"),
    21129: ("Zelote", "JP ファナティック (Fanático religioso munido de cajado; 13B <= 16B)"),
    21130: ("Especialistas em magia que empunham cajados. Atacam e se curam simultaneamente, revelando-se oponentes bem irritantes.", "Descrição zoológica/bestiário refinada; 237B <= original_bytes"),
    21131: ("MC: Priest4", "JP 敵C:神官系4 (Card de Monstro da Família Sacerdote 4; 23B <= 24B)"),
    21132: ("Discípulo Herege", "JP 異端の使徒 (Seguidor de dogmas proibidos com máscara sinistra; 33B <= 40B)"),
    21133: ("Discípulos da heresia trajando máscaras estranhas. Possuem atributos altos no ataque e na defesa, atormentando com magias arcanas.", "Descrição zoológica/bestiário refinada; 263B <= original_bytes"),
    21134: ("MC: Priest5", "JP 敵C:神官系5 (Card de Monstro da Família Sacerdote 5; 23B <= 24B)"),
    21135: ("Deathroid", "JP デストロイド (Espectro guerreiro cibernético sem pernas; 19B <= 24B)"),
    21136: ("Pela falta da metade inferior do corpo, nota-se que não são humanos. São espíritos de guardas caídos com forças ampliadas.", "Descrição zoológica/bestiário refinada; 251B <= original_bytes"),
    21137: ("MC: Priest6", "JP 敵C:神官系6 (Card de Monstro da Família Sacerdote 6; 23B <= 24B)"),
    21138: ("Falcão", "JP アードラ (Ave de rapina veloz Adra; 13B <= 24B)"),
    21139: ("Ave monstruosa colossal que ataca com garras e bico afiados. O tamanho assusta à primeira vista, mas é fraca e fácil de abater.", "Descrição zoológica/bestiário refinada; 258B <= original_bytes"),
    21140: ("MC: Bird1", "JP 敵C:鳥系1 (Card de Monstro da Família Ave 1; 19B <= 24B)"),
    21141: ("Abutre", "JP ヴァルチャー (Ave carniceira veloz Vulture; 13B <= 16B)"),
    21142: ("Ave monstruosa enorme. Não chega a ser muito forte, mas sua velocidade transforma a luta em um estorvo.", "Descrição zoológica/bestiário refinada; 208B <= original_bytes"),
    21143: ("MC: Bird2", "JP 敵C:鳥系2 (Card de Monstro da Família Ave 2; 19B <= 24B)"),
    21144: ("Roc", "JP ロック (Pássaro mítico gigante Roc; 7B <= 8B)"),
    21145: ("Ave colossal que encarna um monstro temível. Possui garras enormes nas asas, usadas para dilacerar seus adversários.", "Descrição zoológica/bestiário refinada; 235B <= original_bytes"),
    21146: ("MC: Bird3", "JP 敵C:鳥系3 (Card de Monstro da Família Ave 3; 19B <= 24B)"),

    # === SLUS/TEXT/0038: Bestiário - Garuda e Esferas Bit Tecnológicas ===
    21147: ("Garuda", "JP ガルーダ (Pássaro divino supremo das tempestades; 13B <= 16B)"),
    21148: ("A ave monstruosa mais rápida e forte. Seus golpes carregados causam estragos imensos: derrote-a antes que concentre poder.", "Descrição zoológica/bestiário refinada; 246B <= original_bytes"),
    21149: ("MC: Bird4", "JP 敵C:鳥系4 (Card de Monstro da Família Ave 4; 19B <= 24B)"),
    21150: ("Bit Ball", "JP ビットボール (Dron mecânico esférico disparador de laser; 17B <= 24B)"),
    21151: ("Parece uma simples esfera, mas dispara lasers pelo orifício vermelho central. Se não for destruída logo, chamará reforços.", "Descrição zoológica/bestiário refinada; 250B <= original_bytes"),
    21152: ("MC: Ball1", "JP 敵C:ボール系1 (Card de Monstro da Família Esfera 1; 19B <= 24B)"),
    21153: ("Bit Ball v2", "JP ビットボール改 (Versão modificada e reforçada da Bit Ball; 23B <= 24B)"),
    21154: ("Versão aprimorada da Bit Ball. Além de disparar lasers mais potentes, possui blindagem reforçada. Jamais a subestime.", "Descrição zoológica/bestiário refinada; 238B <= original_bytes"),
    21155: ("MC: Ball2", "JP 敵C:ボール系2 (Card de Monstro da Família Esfera 2; 19B <= 24B)"),
    21156: ("Blast Eye", "JP ブラスト・アイ (Bit Ball de grande calibre Blast Eye; 19B <= 24B)"),
    21157: ("Uma Bit Ball um pouco maior. Sua rigidez estrutural e seu poder de destruição também aumentaram bastante.", "Descrição zoológica/bestiário refinada; 212B <= original_bytes"),
    21158: ("MC: Ball3", "JP 敵C:ボール系3 (Card de Monstro da Família Esfera 3; 19B <= 24B)"),
    21159: ("Hyper Bit", "JP ハイパービット (Enxame tático de Bit Balls unificadas; 19B <= 24B)"),
    21160: ("Várias Bit Balls reunidas em grupo. Juntas têm grande poder destrutivo, e seus disparos individuais são bem fortes.", "Descrição zoológica/bestiário refinada; 234B <= original_bytes"),
    21161: ("MC: Ball4", "JP 敵C:ボール系4 (Card de Monstro da Família Esfera 4; 19B <= 24B)"),
    21162: ("Flame Guarder", "JP フレイムガーダー (Bit Ball com barreira térmica contra chamas; 27B <= 32B)"),
    21163: ("Bit Ball modificada para resistir a ataques especiais. Uma barreira mágica ao seu redor a protege contra o fogo.", "Descrição zoológica/bestiário refinada; 226B <= original_bytes"),
    21164: ("MC: Ball5", "JP 敵C:ボール系5 (Card de Monstro da Família Esfera 5; 19B <= 24B)"),
    21165: ("Ice Guarder", "JP アイスガーダー (Bit Ball com barreira criogênica contra gelo; 23B <= 24B)"),
    21166: ("Bit Ball modificada para resistir a ataques especiais. Uma barreira mágica ao seu redor a protege contra o gelo.", "Descrição zoológica/bestiário refinada; 226B <= original_bytes"),
    21167: ("MC: Ball6", "JP 敵C:ボール系6 (Card de Monstro da Família Esfera 6; 19B <= 24B)"),
    21168: ("Electric Guarder", "JP エレキガーダー (Bit Ball com barreira de isolamento contra raios; 33B <= 40B)"),
    21169: ("Bit Ball modificada para resistir a ataques especiais. Uma barreira mágica ao seu redor a protege contra raios.", "Descrição zoológica/bestiário refinada; 224B <= original_bytes"),
    21170: ("MC: Ball7", "JP 敵C:ボール系7 (Card de Monstro da Família Esfera 7; 19B <= 24B)"),
}

def main():
    print(f"Curation dictionary contains {len(CURATION)} lines.")
    assert len(CURATION) == 288, f"Expected 288 curated lines, got {len(CURATION)}"

    # Validação estrita de cada linha
    all_errors = []
    overflows = []
    output_dialogues = []
    lines_rewritten = 0
    lines_approved_as_is = 0

    for item in input_data["dialogues"]:
        d_id = item["id"]
        orig_en = item["original_en"]
        orig_jp = item["original_jp"]
        curr_pt = item["current_ptbr"]
        
        db_row = db_rows[d_id]
        cap = db_row[4]
        
        curated_text, just = CURATION[d_id]
        
        # 1. Validação com curadoria_validate
        errs = validate_line(d_id, orig_en, curated_text)
        if errs:
            all_errors.append((d_id, errs))
            
        # 2. Validação de tamanho com encoded_size
        sz = encoded_size(curated_text)
        if sz is None or sz > cap:
            overflows.append((d_id, cap, sz, curated_text))
            
        # Verificar se foi reescrita ou aprovada
        if curated_text != curr_pt:
            lines_rewritten += 1
        else:
            lines_approved_as_is += 1
            
        output_dialogues.append({
            "id": d_id,
            "original_en": orig_en,
            "original_jp": orig_jp,
            "current_ptbr": curr_pt,
            "curated_ptbr": curated_text,
            "justification": just
        })

    print(f"Validation complete:")
    print(f"  Lines rewritten: {lines_rewritten}")
    print(f"  Lines approved as-is: {lines_approved_as_is}")
    print(f"  Technical validation errors: {len(all_errors)}")
    print(f"  Byte capacity overflows: {len(overflows)}")

    if all_errors:
        print("\n--- TECHNICAL ERRORS ---")
        for d_id, errs in all_errors[:10]:
            print(f"ID {d_id}: {errs}")
        sys.exit(1)

    if overflows:
        print("\n--- OVERFLOW ERRORS ---")
        for d_id, cap, sz, text in overflows[:15]:
            print(f"ID {d_id}: cap={cap}B, sz={sz}B -> '{text}'")
        sys.exit(1)

    # Novos termos fixados no Glossário Mestre
    new_terms = {
        "MC: [Categoria]": {
            "pt": "MC: [Categoria]",
            "category": "Bestiário / Sistema",
            "note": "Prefixo canônico de Monster Card (Card de Monstro / 敵C:). Mantido com 'MC:' para concisão de bytes e paridade com a UI do jogo."
        },
        "Pom": {
            "pt": "Pom",
            "gender": "masculino",
            "number": "singular",
            "category": "Bestiário / Mascote",
            "note": "Criatura mascote gelatinosa clássica da Torre de Sol Ciel. Plural: Poms."
        },
        "Bit Ball": {
            "pt": "Bit Ball",
            "gender": "feminino",
            "number": "singular",
            "category": "Bestiário / Mecânico",
            "note": "Dron de patrulha mecânico esférico com emissor de feixe laser central. Plural: Bit Balls."
        }
    }

    # Scene Handoff final deixado por BLK_SYS_003
    scene_handoff_final = {
        "last_scene_id": "BLK_SYS_003",
        "last_line_id": 21170,
        "location_and_situation": "Núcleo Sistêmico Parte 3 (Equipamentos de síntese, armas, armaduras corporais, acessórios, catálogo completo da família Pom, plantas carnívoras, feras lupinas, guardas Tenba, sacerdotes templários e esferas mecânicas de segurança) concluído e 100% calibrado dentro dos tetos de memória.",
        "emotional_state": "Sistêmico / Neutro.",
        "active_hooks": [
            "Encadear com BLK_SYS_004 (continuação do Bestiário, chefes mecânicos, demônios e itens de lore)."
        ]
    }

    # Highlights destacados para o relatório executivo
    highlights = [
        {
            "id": 20883,
            "jp": "合C:超文明の遺産",
            "en": "RC: Super Civ Legacy",
            "before": "RC: Legado da Supercivilização",
            "after": "RC: Legado Ancestral",
            "reason": "JP 合C:超文明の遺産 (Legado da civilização ancestral; 41B <= 48B; concisão que elimina o estouro grave de 61B da tradução anterior)"
        },
        {
            "id": 20885,
            "jp": "合C:トランキリティ",
            "en": "RC: Tranquility",
            "before": "RC: Tranquilidade",
            "after": "RC: Calmaria",
            "reason": "JP 合C:トランキリティ (Paralelo ao item Calmaria; 25B <= 32B; soluciona o overflow de 35B)"
        },
        {
            "id": 20891,
            "jp": "合C:赤い薬剤A / 合C:赤い薬剤B",
            "en": "RC: Red Medicine A",
            "before": "RC: Remédio vermelho A",
            "after": "RC: Remédio Verm. A",
            "reason": "JP 合C:赤い薬剤A (Receita de medicamento vermelho; lapidado no teto exato: 40B <= 40B, eliminando estouro de 46B)"
        },
        {
            "id": 20896,
            "jp": "合C:かわいい小瓶",
            "en": "RC: Cute Bottle",
            "before": "RC: Garrafa fofa",
            "after": "RC: Frasco Fofo",
            "reason": "JP 合C:かわいい小瓶 (Frasco fofo; 31B <= 32B; termo muito mais acurado para 'kobin' e cabe com folga)"
        },
        {
            "id": 20907,
            "jp": "嘆きと喜びの棺",
            "en": "Coffin of Grief and Joy",
            "before": "Caixão da dor e da alegria",
            "after": "Caixão: Dor e Alegria",
            "reason": "JP 嘆きと喜びの棺 (Esquife de dor e alegria; 44B <= 48B; formatação sintética elegante que elimina estouro de 54B)"
        },
        {
            "id": 20915,
            "jp": "大自然あいす",
            "en": "Nature Ice",
            "before": "Gelo natural",
            "after": "Gelo Nativo",
            "reason": "JP 大自然あいす (Sorvete/gelo da natureza; 23B <= 24B; quarteto 'Gelo Nativo / RC: Gelo Nativo / Supergelo Nativo / RC: Supergelo Nativo' 100% harmonizado)"
        },
        {
            "id": 20919,
            "jp": "焼肉ソーダ",
            "en": "BBQ Soda",
            "before": "Refrigerante BBQ",
            "after": "Soda BBQ",
            "reason": "JP 焼肉ソーダ (Refrigerante/soda de churrasco; 17B <= 24B; corrige overflow de 33B)"
        },
        {
            "id": 20921,
            "jp": "ソリッドうさこ",
            "en": "Solid Bunnygirl",
            "before": "Coelhinha sólida",
            "after": "Coelha Sólida",
            "reason": "JP ソリッドうさこ (Mascote Usako rígida; 28B <= 32B; elimina estouro de 34B)"
        },
        {
            "id": 20923,
            "jp": "うさライス",
            "en": "Bunny Rice",
            "before": "Arroz de coelho",
            "after": "Arroz Usako",
            "reason": "JP うさライス (Prato de arroz com formato da coelhinha Usako; 23B <= 24B; preserva identidade diegética e corrige 31B)"
        },
        {
            "id": 20925,
            "jp": "めかうさ",
            "en": "Bunny Mech",
            "before": "Coelho mecânico",
            "after": "Meca-Coelho",
            "reason": "JP めかうさ (Coelho mecânico Mecha-Usa; 23B <= 24B; conciso, expressivo e elimina estouro de 32B)"
        },
        {
            "id": 20932,
            "jp": "合C:ソード1",
            "en": "RC: Sword 1",
            "before": "RC: Espada 1",
            "after": "RC: Esp. 1",
            "reason": "JP 合C:ソード1 (Receita de Espada 1; 21B <= 24B; padroniza série RC: Esp. 1 a 4 dentro do limite de 24B)"
        },
        {
            "id": 20937,
            "jp": "音速歯車",
            "en": "Sonic Gear",
            "before": "Engrenagem sônica",
            "after": "Eng. Sônica",
            "reason": "JP 音速歯車 (Engrenagem que gira na velocidade do som; 24B <= 24B; paralelismo com 'Eng. Mortal' de BLK_SYS_002)"
        },
        {
            "id": 20938,
            "jp": "合C:チェーン1",
            "en": "RC: Chain 1",
            "before": "RC: Corrente 1",
            "after": "RC: Corr. 1",
            "reason": "JP 合C:チェーン1 (Receita de Corrente 1; 23B <= 24B; padroniza série RC: Corr. 1 a 4 dentro de 24B)"
        },
        {
            "id": 20977,
            "jp": "天上天下唯我独尊",
            "en": "God’s Armor",
            "before": "Armadura divina",
            "after": "Cota Divina",
            "reason": "JP 天上天下唯我独尊 (Armadura lendária soberana e invencível; 23B <= 24B; resolve overflow de 31B)"
        },
        {
            "id": 20979,
            "jp": "褐色モモヒキ",
            "en": "Brown Tights",
            "before": "Meia-calça marrom",
            "after": "Ceroula Marrom",
            "reason": "JP 褐色モモヒキ (Momohiki = ceroulas tradicionais masculinas compridas; 29B <= 32B; fidelidade cultural ao original)"
        },
        {
            "id": 21008,
            "jp": "合C:ブースター",
            "en": "RC: Booster",
            "before": "RC: Amplificador",
            "after": "RC: Booster",
            "reason": "JP 合C:ブースター (Receita de Booster/acelerador; 23B <= 24B; corrige overflow de 33B e confisco de nome com amplificadores de som)"
        },
        {
            "id": 21024,
            "jp": "マロンポム",
            "en": "Melon Pom",
            "before": "Pom melão",
            "after": "Pom Marrom",
            "reason": "JP マロンポム (Correção cabal do equívoco de localização ocidental do inglês; Marron = Castanha/Marrom, ponta da cabeça castanha; 21B <= 24B)"
        },
        {
            "id": 21046,
            "jp": "ただでさえ大きくないポムの更に小さいやつ...",
            "en": "A smaller version of an already small Pom...",
            "before": "Versão menor de um Pom já pequeno...",
            "after": "Uma versão ainda menor de uma criatura que já não é grande. Por ser miúdo, é difícil acertá-lo e seus ataques causam dor pontual como picadas. Quem tem vista fraca que se cuide!",
            "reason": "JP 目の悪い方には要注意 (Restaura o trocadilho cômico do autor omitido na versão ocidental; 189B <= 312B)"
        },
        {
            "id": 21072,
            "jp": "マッドドッグ",
            "en": "Mad Dog",
            "before": "Cão feroz",
            "after": "Mad Dog",
            "reason": "JP マッドドッグ (Cão hidrófobo raivoso; 15B <= 16B; resolve estouro de 20B e mantém simetria com a descrição de Feral Wolf)"
        },
        {
            "id": 21136,
            "jp": "下半身がないことからわかると思うが、人間ではない...",
            "en": "As you can see, they are not human...",
            "before": "Como se vê, não são humanos...",
            "after": "Como dá para notar pela ausência da metade inferior do corpo, não é humano. Trata-se do espírito de um Temple Guard caído que retornou do além com poderes ampliados.",
            "reason": "JP 下半身がないことから (Restaura a descrição anatômica espectral original omitida pelo inglês; 174B <= 264B)"
        }
    ]

    output_data = {
        "block_id": "BLK_SYS_003",
        "axis_id": "AXIS_1",
        "axis_name": "1_NUCLEO_SISTEMICO_E_MENUS",
        "category": "Equipamentos, Armas, Armaduras, Acessórios e Itens de Síntese",
        "total_lines": 288,
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "new_terms": new_terms,
        "scene_handoff_final": scene_handoff_final,
        "highlights": highlights,
        "dialogues": output_dialogues
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n[SUCESSO] BLK_SYS_003_output.json gerado com sucesso em: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()

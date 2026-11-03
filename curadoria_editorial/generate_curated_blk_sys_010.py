"""Script de Geração e Validação Rigorosa de Curadoria Editorial para BLK_SYS_010
Cobre IDs 22917 a 23204 (288 falas executáveis em SLUS/TEXT/0113 a 0124).
Garante conformidade com os 12 Critérios Canônicos, teto de bytes (encoded_size <= original_bytes),
e integridade de tags de engine.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

# Paths
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "tools"))

import artonelico_tool.project as proj
from curadoria_validate import validate_line, validate_batch

CONFIG_PATH = BASE_DIR / "curadoria_editorial" / "curadoria_config.json"
INPUT_PATH = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_010_input.json"
OUTPUT_PATH = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_010_output.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    cfg = json.load(f)

conn = sqlite3.connect(cfg["database_path"])
c = conn.cursor()
c.execute("""
    SELECT id, event_file, speaker_id, original_jp, original, translation, reviewed, original_bytes
    FROM dialogues
    WHERE id BETWEEN 22917 AND 23204
    ORDER BY id
""")
db_rows = {r[0]: r for r in c.fetchall()}
conn.close()

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Dicionário mestre de curadoria com (texto_curado, justificativa)
CURATED_MAP: dict[int, tuple[str, str]] = {
    # --- Parte 1: Progressão de HP e MP (22917 a 22939) ---
    22917: (
        "[Equipamento]CRConcede HP +150.",
        "JP: 【装備品用】CRHPが150上昇する。Padronização com BLK_SYS_009 (22913/22915 Concede HP +X)."
    ),
    22918: (
        "Super HP+",
        "JP: かなりHPアップ. Elimina calque 'Muito HP' e dá continuidade à série Leve/Médio/Alto/Super HP+."
    ),
    22919: (
        "[Equipamento]CRConcede HP +250.",
        "JP: 【装備品用】CRHPが250上昇する。Padronização com a progressão de equipamentos."
    ),
    22920: (
        "Chip de Reforço",
        "JP: 体力増強チップ. Capitalização canônica de itens/efeitos de equipamento."
    ),
    22921: (
        "[Equipamento]CRConcede HP +500.",
        "JP: 【装備品用】CRHPが500上昇する。Padronização com a progressão de equipamentos."
    ),
    22922: (
        "Stamina Plus",
        "JP: スタミナプラス. Transcrição direta do katakana japonês respeitando o teto de 32B."
    ),
    22923: (
        "[Equipamento]CRConcede HP +750.",
        "JP: 【装備品用】CRHPが750上昇する。Padronização com a progressão de equipamentos."
    ),
    22924: (
        "Life Booster",
        "JP: ライフブースター. Elimina estouro de bytes ('Amplificador vital' tinha 37B > 32B; Life Booster tem 25B <= 32B)."
    ),
    22925: (
        "[Equipamento]CRConcede HP +1250.",
        "JP: 【装備品用】CRHPが1250上昇する。Padronização com a progressão de equipamentos."
    ),
    22926: (
        "Leve MP+",
        "JP: ちょっとMPアップ. Elimina calque 'Pouco MP' e alinha perfeitamente com Leve HP+ (22912)."
    ),
    22927: (
        "[Equipamento]CRConcede MP +50.",
        "JP: 【装備品用】CRMPが50上昇する。Padronização com a progressão de equipamentos (61B <= 64B)."
    ),
    22928: (
        "Médio MP+",
        "JP: まあまあMPアップ. Elimina calque culinário americano ('Spoonful of MP' -> 'Colher de MP'), alinhando com Médio HP+."
    ),
    22929: (
        "[Equipamento]CRConcede MP +100.",
        "JP: 【装備品用】CRMPが100上昇する。Padronização com a progressão de equipamentos."
    ),
    22930: (
        "Alto MP+",
        "JP: なかなかMPアップ. Elimina calque culinário americano ('Cup of MP' -> 'Copo de MP'), alinhando com Alto HP+."
    ),
    22931: (
        "[Equipamento]CRConcede MP +150.",
        "JP: 【装備品用】CRMPが150上昇する。Padronização com a progressão de equipamentos."
    ),
    22932: (
        "Super MP+",
        "JP: かなりMPアップ. Elimina calque 'Muito MP', alinhando com Super HP+."
    ),
    22933: (
        "[Equipamento]CRConcede MP +250.",
        "JP: 【装備品用】CRMPが250上昇する。Padronização com a progressão de equipamentos."
    ),
    22934: (
        "Mega Memory",
        "JP: メガメモリー. Elimina estouro de bytes ('Memória mega' tinha 26B > 24B; Mega Memory é transcrição do katakana em 23B <= 24B)."
    ),
    22935: (
        "[Equipamento]CRConcede MP +500.",
        "JP: 【装備品用】CRMPが500上昇する。Padronização com a progressão de equipamentos."
    ),
    22936: (
        "Giga Memory",
        "JP: ギガメモリー. Elimina estouro de bytes ('Memória giga' tinha 26B > 24B; Giga Memory é transcrição do katakana em 23B <= 24B)."
    ),
    22937: (
        "[Equipamento]CRConcede MP +750.",
        "JP: 【装備品用】CRMPが750上昇する。Padronização com a progressão de equipamentos."
    ),
    22938: (
        "Tera Memory",
        "JP: テラメモリー. Elimina estouro de bytes ('Memória tera' tinha 26B > 24B; Tera Memory é transcrição do katakana em 23B <= 24B)."
    ),
    22939: (
        "[Equipamento]CRConcede MP +1250.",
        "JP: 【装備品用】CRMPが1250上昇する。Padronização com a progressão de equipamentos."
    ),

    # --- Parte 2: Parâmetros de Ataque e Crítico (22940 a 22959) ---
    22940: (
        "Ataque Leve",
        "JP: ちょい攻撃力アップ. Série de progressão de ataque em 23B <= 32B."
    ),
    22941: (
        "[Equipamento]CREleva levemente o ataque.",
        "JP: 【装備品用】CR攻撃力をわずかに上昇させる。Concisão e corte de gordura textual (81B <= 96B)."
    ),
    22942: (
        "Ataque Médio",
        "JP: やや攻撃力アップ. Série de progressão de ataque em 26B <= 32B."
    ),
    22943: (
        "[Equipamento]CREleva um pouco o ataque.",
        "JP: 【装備品用】CR攻撃力をそこそこ上昇させる。Concisão e corte de gordura textual (79B <= 88B)."
    ),
    22944: (
        "Ataque Alto",
        "JP: 結構攻撃力アップ. Elimina estouro e ajusta concisão para caber no teto físico de 24B (23B <= 24B)."
    ),
    22945: (
        "[Equipamento]CREleva bem o ataque.",
        "JP: 【装備品用】CR攻撃力を結構上昇させる。Concisão e corte de gordura textual (69B <= 96B)."
    ),
    22946: (
        "Ataque Real",
        "JP: かなり攻撃力アップ. Elimina estouro de bytes ('Realmente forte' tinha 31B > 24B; Ataque Real tem 23B <= 24B)."
    ),
    22947: (
        "[Equipamento]CREleva bastante o ataque.",
        "JP: 【装備品用】CR攻撃力をかなり上昇させる。Concisão e corte de gordura textual (79B <= 88B)."
    ),
    22948: (
        "Técnica de Mestre",
        "JP: 達人テクニック. Capitalização e elegância em 36B <= 40B."
    ),
    22949: (
        "[Equipamento]CREleva enormemente o ataque.",
        "JP: 【装備品用】CR攻撃力を大幅に上昇させる。Concisão e corte de gordura textual (85B <= 96B)."
    ),
    22950: (
        "Crítico Leve",
        "JP: ちょいクリティカル. Série de progressão de taxa crítica em 26B <= 32B."
    ),
    22951: (
        "[Equipamento]CREleva levemente o crítico.",
        "JP: 【装備品用】CRクリティカル率をわずかに上昇させる。Elimina estouro de bytes (antigo tinha 108B > 96B; novo tem 81B <= 96B)."
    ),
    22952: (
        "Crítico Médio",
        "JP: ややクリティカル. Série de progressão de taxa crítica em 28B <= 32B."
    ),
    22953: (
        "[Equipamento]CREleva um pouco o crítico.",
        "JP: 【装備品用】CRクリティカル率をそこそこ上昇させる。Elimina estouro de bytes (antigo tinha 106B > 88B; novo tem 79B <= 88B)."
    ),
    22954: (
        "Crítico Alto",
        "JP: 結構クリティカル. Série de progressão de taxa crítica em 26B <= 32B."
    ),
    22955: (
        "[Equipamento]CREleva bem o crítico.",
        "JP: 【装備品用】CRクリティカル率を結構上昇させる。Elimina estouro de bytes (antigo tinha 116B > 96B; novo tem 69B <= 96B)."
    ),
    22956: (
        "Super Crítico",
        "JP: かなりクリティカル. Elimina estouro de bytes ('Realmente crítico' tinha 36B > 32B; Super Crítico tem 27B <= 32B)."
    ),
    22957: (
        "[Equipamento]CREleva bastante o crítico.",
        "JP: 【装備品用】CRクリティカル率をかなり上昇させる。Elimina estouro de bytes (antigo tinha 100B > 88B; novo tem 79B <= 88B)."
    ),
    22958: (
        "Crítico Absoluto",
        "JP: 絶対クリティカル. Adaptação elegante e fiel em 34B <= 40B."
    ),
    22959: (
        "[Equipamento]CREleva muito o crítico.",
        "JP: 【装備品用】CRクリティカル率を大幅に上昇させる。Elimina estouro de bytes (antigo tinha 116B > 96B; novo tem 71B <= 96B)."
    ),

    # --- Parte 3: Parâmetros de Defesa e Agilidade/Velocidade (22960 a 22979) ---
    22960: (
        "Defesa Leve",
        "JP: ちょい防御力アップ. Série de progressão defensiva em 25B <= 32B."
    ),
    22961: (
        "[Equipamento]CREleva pouco a defesa.",
        "JP: 【装備品用】CR防御力をわずかに上昇させる。Elimina estouro de bytes (antigo tinha 81B > 80B; novo tem 73B <= 80B)."
    ),
    22962: (
        "Defesa Média",
        "JP: やや防御力アップ. Série de progressão defensiva em 27B <= 40B."
    ),
    22963: (
        "[Equipamento]CREleva um pouco a defesa.",
        "JP: 【装備品用】CR防御力をそこそこ上昇させる。Elimina estouro de bytes (antigo tinha 83B > 80B; novo tem 65B <= 80B)."
    ),
    22964: (
        "Defesa Alta",
        "JP: 結構防御力アップ. Série de progressão defensiva em 25B <= 32B."
    ),
    22965: (
        "[Equipamento]CREleva bem a defesa.",
        "JP: 【装備品用】CR防御力を結構上昇させる。Concisão e corte de gordura textual (71B <= 88B)."
    ),
    22966: (
        "Super Defesa",
        "JP: かなり防御力アップ. Elimina estouro de bytes ('Realmente defensivo' tinha 39B > 32B; Super Defesa tem 25B <= 32B)."
    ),
    22967: (
        "[Equipamento]CREleva bastante a defesa.",
        "JP: 【装備品用】CR防御力をかなり上昇させる。Elimina estouro de bytes (antigo tinha 81B > 80B; novo tem 75B <= 80B)."
    ),
    22968: (
        "Proteção Diamante",
        "JP: 金剛プロテクション. Adaptação elegante do kanji Kongou (diamante/vajra indestrutível) em 35B <= 40B."
    ),
    22969: (
        "[Equipamento]CREleva enormemente a defesa.",
        "JP: 【装備品用】CR防御力を大幅に上昇させる。Concisão e corte de gordura textual (87B <= 88B)."
    ),
    22970: (
        "Veloz Leve",
        "JP: ちょい素早さアップ. Elimina estouro de bytes ('Pouco rápido' tinha 26B > 24B; Veloz Leve tem 21B <= 24B)."
    ),
    22971: (
        "[Equipamento]CREleva leve a agilidade.",
        "JP: 【装備品用】CR素早さをわずかに上昇させる。Elimina estouro de bytes (antigo tinha 83B > 80B; novo tem 69B <= 80B)."
    ),
    22972: (
        "Veloz Médio",
        "JP: やや素早さアップ. Série de progressão de agilidade em 23B <= 24B."
    ),
    22973: (
        "[Equipamento]CREleva pouco a agilidade.",
        "JP: 【装備品用】CR素早さをそこそこ上昇させる。Elimina estouro de bytes (antigo tinha 89B > 80B; novo tem 79B <= 80B)."
    ),
    22974: (
        "Veloz Alto",
        "JP: 結構素早さアップ. Elimina estouro de bytes ('Muito rápido' tinha 26B > 24B; Veloz Alto tem 21B <= 24B)."
    ),
    22975: (
        "[Equipamento]CREleva bem a agilidade.",
        "JP: 【装備品用】CR素早さを結構上昇させる。Elimina estouro de bytes (antigo tinha 91B > 88B; novo tem 69B <= 88B)."
    ),
    22976: (
        "Super Veloz",
        "JP: かなり素早さアップ. Elimina estouro de bytes ('Realmente rápido' tinha 34B > 24B; Super Veloz tem 23B <= 24B)."
    ),
    22977: (
        "[Equipamento]CREleva muito a agilidade.",
        "JP: 【装備品用】CR素早さをかなり上昇させる。Elimina estouro de bytes (antigo tinha 87B > 80B; novo tem 79B <= 80B)."
    ),
    22978: (
        "Agil Mach",
        "JP: マッハな速さ. Elimina estouro de bytes ('Velocidade Mach' tinha 31B > 24B; Agil Mach tem 19B <= 24B)."
    ),
    22979: (
        "[Equipamento]CREleva ao máximo a agilidade.",
        "JP: 【装備品用】CR素早さを大幅に上昇させる。Elimina estouro de bytes (antigo tinha 92B > 88B; novo tem 81B <= 88B)."
    ),

    # --- Parte 4: Dano Direto, Overclock e Resistência GD (22980 a 23001) ---
    22980: (
        "Dano Leve+",
        "JP: ちょいダメージ+. Série de dano direto adicional em 23B <= 32B."
    ),
    22981: (
        "[Equipamento]CRCausa dano leve ao alvo.",
        "JP: 【装備品用】CR相手にわずかなダメージを与える。Padronização de 'alvo' e concisão (71B <= 96B)."
    ),
    22982: (
        "Dano Médio+",
        "JP: ややダメージ+. Série de dano direto adicional em 26B <= 32B."
    ),
    22983: (
        "[Equipamento]CRCausa dano baixo ao alvo.",
        "JP: 【装備品用】CR相手にそこそこのダメージを与える。Padronização e concisão (71B <= 88B)."
    ),
    22984: (
        "Dano Alto+",
        "JP: 結構ダメージ+. Série de dano direto adicional em 23B <= 40B."
    ),
    22985: (
        "[Equipamento]CRCausa dano moderado ao alvo.",
        "JP: 【装備品用】CR相手に結構なダメージを与える。Padronização e concisão (79B <= 96B)."
    ),
    22986: (
        "Super Dano+",
        "JP: かなりダメージ+. Série de dano direto adicional em 25B <= 32B."
    ),
    22987: (
        "[Equipamento]CRCausa dano alto ao alvo.",
        "JP: 【装備品用】CR相手にかなりのダメージを与える。Padronização e concisão (69B <= 88B)."
    ),
    22988: (
        "Super Atacante",
        "JP: グレイトアタッカー. Elimina estouro de bytes ('Grande destruidor' tinha 35B > 32B; Super Atacante tem 29B <= 32B)."
    ),
    22989: (
        "[Equipamento]CRCausa dano extremo ao alvo.",
        "JP: 【装備品用】CR相手に強烈なダメージを与える。Padronização e concisão (75B <= 96B)."
    ),
    22990: (
        "Overclock",
        "JP: オーバークロック. Transcrição direta do termo técnico em 19B <= 24B."
    ),
    22991: (
        "[Equipamento]CREleva atributos além do limite. Reduz resist. GD.",
        "JP: 【装備品用】CR限界を超えて能力を高める。GD耐性低下。Elimina estouro de bytes (antigo tinha 157B > 136B; novo tem 127B <= 136B)."
    ),
    22992: (
        "Coração Forte",
        "JP: 強いココロ. Elimina estouro de bytes ('Sentimentos fortes' tinha 37B > 32B; Coração Forte tem 27B <= 32B)."
    ),
    22993: (
        "[Equipamento]CREleva levemente a resist. GD.",
        "JP: 【装備品用】CRGD耐性をわずかに上昇する。Elimina estouro de bytes (antigo tinha 102B > 96B; novo tem 79B <= 96B)."
    ),
    22994: (
        "Relaxamento",
        "JP: リラクゼーション. Tradução fiel do katakana em 23B <= 24B."
    ),
    22995: (
        "[Equipamento]CREleva bastante a resist. GD.",
        "JP: 【装備品用】CRGD耐性を結構上昇させる。Elimina estouro de bytes (antigo tinha 110B > 96B; novo tem 77B <= 96B)."
    ),
    22996: (
        "Brave Note",
        "JP: ブレイブノート. Elimina estouro de bytes ('Nota valente' tinha 25B > 24B; Brave Note tem 21B <= 24B)."
    ),
    22997: (
        "[Equipamento]CREleva enormemente a resist. GD.",
        "JP: 【装備品用】CRGD耐性を大幅に上昇させる。Elimina estouro de bytes (antigo tinha 110B > 104B; novo tem 83B <= 104B)."
    ),
    22998: (
        "Glass Heart",
        "JP: ガラスのハート. Elimina estouro de bytes ('Coração de vidro' tinha 33B > 24B; Glass Heart é transcrição do katakana em 23B <= 24B)."
    ),
    22999: (
        "[Equipamento]CREleva BS e Influência, mas reduz resist. GD.",
        "JP: 【装備品用】CRBS、インフルエンス上昇。GD耐性減少。Elimina estouro de bytes (antigo tinha 137B > 136B; novo tem 113B <= 136B)."
    ),
    23000: (
        "Emoção 0",
        "JP: エモーション0. Tradução concisa e exata em 17B <= 24B."
    ),
    23001: (
        "[Equipamento]CRMaximiza resist. GD, mas reduz BS e Influência.",
        "JP: 【装備品用】CRGD耐性最大。BSとインフルエンス減少。Elimina estouro de bytes (antigo tinha 135B > 128B; novo tem 117B <= 128B)."
    ),

    # --- Parte 5: Selos Dracônicos Elementais 100% (23002 a 23009) ---
    23002: (
        "Selo Salamandra",
        "JP: 火竜印シール. Selo elemental do dragão de fogo em 31B <= 32B."
    ),
    23003: (
        "[Equipamento]CRCausa +100% do dano base em fogo.",
        "JP: 【装備品用】CRダメージの100%分の炎追加ダメージ。Elimina estouro de bytes (antigo tinha 121B > 120B; novo tem 89B <= 120B) e harmoniza com BLK_SYS_009."
    ),
    23004: (
        "Selo Leviatã",
        "JP: 水竜印シール. Selo elemental do dragão de gelo em 26B <= 32B."
    ),
    23005: (
        "[Equipamento]CRCausa +100% do dano base em gelo.",
        "JP: 【装備品用】CRダメージの100%分の氷追加ダメージ。Elimina estouro de bytes (antigo tinha 121B > 120B; novo tem 87B <= 120B) e harmoniza com BLK_SYS_009."
    ),
    23006: (
        "Selo Indra",
        "JP: 雷竜印シール. Selo elemental do dragão de raio em 21B <= 24B."
    ),
    23007: (
        "[Equipamento]CRCausa +100% do dano base em raio.",
        "JP: 【装備品用】CRダメージの100%分の雷追加ダメージ。Elimina estouro de bytes (antigo tinha 121B > 112B; novo tem 87B <= 112B) e harmoniza com BLK_SYS_009."
    ),
    23008: (
        "Selo Grifo",
        "JP: 風竜印シール. Selo elemental do dragão de vento em 21B <= 32B."
    ),
    23009: (
        "[Equipamento]CRCausa +100% do dano base em vento.",
        "JP: 【装備品用】CRダメージの100%分の風追加ダメージ。Elimina estouro de bytes (antigo tinha 123B > 120B; novo tem 89B <= 120B) e harmoniza com BLK_SYS_009."
    ),

    # --- Parte 6: Potencial, Vigor/Konjou, MP Convert e Velocidade (23010 a 23034) ---
    23010: (
        "Potencial+",
        "JP: ポテンシャルアップ. Elimina estouro de bytes ('Aumenta potencial' tinha 35B > 32B; Potencial+ tem 23B <= 32B)."
    ),
    23011: (
        "[Equipamento]CRDesperta o potencial de quem equipa.",
        "JP: 【装備品用】CR装備者の潜在能力を引き出してくれる。Elegância e concisão em 93B <= 128B."
    ),
    23012: (
        "Vigor Guerreiro",
        "JP: 戦士のコンジョー. Adaptação idiomática de 'Konjou' (garra, fibra, vigor) em 31B <= 40B."
    ),
    23013: (
        "[Equipamento]CREleva levemente HP, ataque e defesa.",
        "JP: 【装備品用】CRHP、攻撃力、防御力が若干上昇する。Concisão em 95B <= 128B."
    ),
    23014: (
        "Vigor Cavaleiro",
        "JP: 騎士のコンジョー. Elimina estouro de bytes ('Espírito cavaleiro' tinha 38B > 32B; Vigor Cavaleiro tem 31B <= 32B)."
    ),
    23015: (
        "[Equipamento]CREleva bem HP, ataque e defesa.",
        "JP: 【装備品用】CRHP、攻撃力、防御力が結構上昇する。Concisão em 81B <= 128B."
    ),
    23016: (
        "Vigor Bushido",
        "JP: ブシドーコンジョー. Elimina estouro de bytes ('Espírito bushido' tinha 34B > 32B; Vigor Bushido tem 27B <= 32B)."
    ),
    23017: (
        "[Equipamento]CREleva muito HP, ataque e defesa.",
        "JP: 【装備品用】CRHP、攻撃力、防御力が大幅に上昇する。Concisão em 83B <= 128B."
    ),
    23018: (
        "Vigor Heroico",
        "JP: 勇者のコンジョー. Elimina estouro de bytes ('Espírito heroico' tinha 34B > 32B; Vigor Heroico tem 27B <= 32B)."
    ),
    23019: (
        "[Equipamento]CRMelhora atributos e todas as resistências.",
        "JP: 【装備品用】CRステータス強化に加え全属性の耐性アップ。Concisão em 101B <= 136B."
    ),
    23020: (
        "Vigor Real",
        "JP: 王者のコンジョー. Adaptação idiomática de 'Konjou' do Rei em 21B <= 32B."
    ),
    23021: (
        "[Equipamento]CREleva atributos e dá dano extra forte.",
        "JP: 【装備品用】CR装備者を強化。強力な追加ダメージもあり。Elimina estouro de bytes (antigo tinha 123B > 120B; novo tem 99B <= 120B)."
    ),
    23022: (
        "Vigor Soberano",
        "JP: 覇王のコンジョー. Elimina estouro de bytes ('Espírito conquistador' tinha 44B > 40B; Vigor Soberano tem 29B <= 40B)."
    ),
    23023: (
        "[Equipamento]CREleva muito os atributos e dá dano extra forte.",
        "JP: 【装備品用】CR装備者を大幅に強化。追加ダメージもあり。Elimina estouro de bytes (antigo tinha 141B > 128B; novo tem 111B <= 128B)."
    ),
    23024: (
        "MP Convert",
        "JP: MPコンバート. Elimina estouro de bytes ('Converter MP' tinha 25B > 24B; MP Convert é transcrição do katakana em 21B <= 24B)."
    ),
    23025: (
        "[Equipamento]CRConverte levemente HP max em MP.",
        "JP: 【装備品用】CR最大HPをわずかにMPに変換。Elimina estouro de bytes (antigo tinha 124B > 96B; novo tem 81B <= 96B)."
    ),
    23026: (
        "MP Converter",
        "JP: MPコンバータ. Transcrição direta do katakana em 25B <= 32B."
    ),
    23027: (
        "[Equipamento]CRConverte pouco HP max em MP.",
        "JP: 【装備品用】CR最大HPをそこそこMPに変換。Elimina estouro de bytes (antigo tinha 126B > 96B; novo tem 87B <= 96B)."
    ),
    23028: (
        "MP Conversion",
        "JP: MPコンバーター. Adaptação técnica em 27B <= 32B."
    ),
    23029: (
        "[Equipamento]CRConverte bem o HP max em MP.",
        "JP: 【装備品用】CR最大HPを結構MPに変換。Elimina estouro de bytes (antigo tinha 116B > 88B; novo tem 73B <= 88B)."
    ),
    23030: (
        "MP Convertist",
        "JP: MPコンバーテスト. Transcrição do katakana humorístico em 27B <= 32B."
    ),
    23031: (
        "[Equipamento]CRConverte HP em MP.",
        "JP: 【装備品用】CR最大HPをMPに変換. Elimina estouro de bytes (antigo tinha 86B > 72B; novo tem 67B <= 72B)."
    ),
    23032: (
        "Poder Impuro",
        "JP: 汚れた力. Elimina estouro de bytes ('Poder corrompido' tinha 33B > 32B; Poder Impuro tem 25B <= 32B)."
    ),
    23033: (
        "Hipervelocidade",
        "JP: 神速の極み. Elimina estouro de bytes ('Velocidade extrema' tinha 37B > 32B; Hipervelocidade tem 31B <= 32B)."
    ),
    23034: (
        "[Equipamento]CRDá +5 ataques e eleva a velocidade.",
        "JP: 【装備品用】CR攻撃回数を5回増加。速度も上昇する。Elimina estouro de bytes (antigo tinha 115B > 112B; novo tem 83B <= 112B)."
    ),

    # --- Parte 7: Auras, Goith, Origens, Yuteria e Bênçãos (23035 a 23070) ---
    23035: (
        "Battle Aura",
        "JP: バトルオーラ. Elimina estouro de bytes ('Aura de batalha' tinha 31B > 24B; Battle Aura tem 23B <= 24B)."
    ),
    23036: (
        "Brave Aura",
        "JP: ブレイブオーラ. Elimina estouro de bytes ('Aura valente' tinha 25B > 24B; Brave Aura tem 21B <= 24B)."
    ),
    23037: (
        "Master Aura",
        "JP: マスターオーラ. Transcrição do katakana em 23B <= 24B."
    ),
    23038: (
        "[Equipamento]CRAdiciona autorregeneração de HP.",
        "JP: 【装備品用】CR装備品にHP自動回復効果追加。Elimina estouro de bytes (antigo tinha 108B > 104B; novo tem 87B <= 104B)."
    ),
    23039: (
        "Ira Max",
        "JP: 怒りMAXモード. Concisão para efeito berserk em 15B <= 24B."
    ),
    23040: (
        "[Equipamento]CREleva muito o ataque.",
        "JP: 【装備品用】CR攻撃力を大きく上昇させる。Concisão em 63B <= 96B."
    ),
    23041: (
        "Escudo Goith",
        "JP: ゴイス防壁. Nome do mineral Goith em 25B <= 32B."
    ),
    23042: (
        "[Equipamento]CRReduz o dano físico sofrido.",
        "JP: 【装備品用】CR受ける物理ダメージを軽減させる。Concisão em 69B <= 96B."
    ),
    23043: (
        "Barreira Goith",
        "JP: ゴイス結界. Nome da barreira Goith em 29B <= 32B."
    ),
    23044: (
        "[Equipamento]CRReduz o dano mágico sofrido.",
        "JP: 【装備品用】CR受ける魔法ダメージを軽減させる。Elimina estouro de bytes (antigo tinha 90B > 88B; novo tem 71B <= 88B)."
    ),
    23045: (
        "Alma Insana",
        "JP: 狂エル戦士ノ魂. Adaptação expressiva do guerreiro enlouquecido em 23B <= 24B."
    ),
    23046: (
        "[Equipamento]CRA fúria eleva o ataque, mas reduz muito a defesa.",
        "JP: 【装備品用】CR怒りにまかせて攻撃力+、防御力大幅ダウン。Elegância e concisão em 119B <= 144B."
    ),
    23047: (
        "Origem: α",
        "JP: オリジン:α. Série dos quatro núcleos de Origem em 19B <= 24B."
    ),
    23048: (
        "[Equipamento]CREleva o ataque e a defesa de todos os elementos.",
        "JP: 【装備品用】CR全属性の攻撃、防御を中心に上昇させる。Fidelidade ao kanji em 113B <= 128B."
    ),
    23049: (
        "Origem: β",
        "JP: オリジン:β. Série dos quatro núcleos de Origem em 19B <= 24B."
    ),
    23050: (
        "[Equipamento]CRFoca em elevar MP e defesa.",
        "JP: 【装備品用】CRMPと防御力を中心に強化してくれる。Elimina estouro de bytes (antigo tinha 99B > 88B; novo tem 69B <= 88B)."
    ),
    23051: (
        "Origem: γ",
        "JP: オリジン:γ. Série dos quatro núcleos de Origem em 19B <= 24B."
    ),
    23052: (
        "[Equipamento]CRFortalece toda a defesa de quem equipa.",
        "JP: 【装備品用】CR装備者の防御力を全体的に強化してくれる。Elegância em 89B <= 120B."
    ),
    23053: (
        "Origem: Ω",
        "JP: オリジン:Ω. Série dos quatro núcleos de Origem em 19B <= 24B."
    ),
    23054: (
        "[Equipamento]CREleva HP, MP e resist. GD.",
        "JP: 【装備品用】CRHP、MP、GD耐性を強化する。Concisão em 69B <= 96B."
    ),
    23055: (
        "Arma Yuteria",
        "JP: ユーテリアウェポン. Termo canônico Yuteria em 25B <= 32B."
    ),
    23056: (
        "[Equipamento]CREleva o ataque e a taxa de crítico.",
        "JP: 【装備品用】CR攻撃力とクリティカル値が上昇する。Concisão em 89B <= 112B."
    ),
    23057: (
        "Guarda Yuteria",
        "JP: ユーテリアガード. Elimina estouro de bytes ('Proteção Yuteria' tinha 33B > 32B; Guarda Yuteria tem 29B <= 32B)."
    ),
    23058: (
        "[Equipamento]CREleva o dano extra e a defesa de tudo.",
        "JP: 【装備品用】CR全属性の追加ダメージ、防御力を上げる。Concisão em 95B <= 120B."
    ),
    23059: (
        "Poder do Reforço",
        "JP: 強化の力. Série de bênçãos em 35B <= 40B."
    ),
    23060: (
        "[Equipamento]CRFortalece levemente quem equipa.",
        "JP: 【装備品用】CR装備者をわずかに強化してくれる。Concisão em 81B <= 96B."
    ),
    23061: (
        "Poder da Proteção",
        "JP: 加護の力. Série de bênçãos em 35B <= 40B."
    ),
    23062: (
        "[Equipamento]CRFortalece um pouco quem equipa.",
        "JP: 【装備品用】CR装備者をそこそこ強化してくれる。Concisão em 79B <= 104B."
    ),
    23063: (
        "Poder da Bênção",
        "JP: 祝福の力. Série de bênçãos em 31B <= 32B."
    ),
    23064: (
        "[Equipamento]CRFortalece bastante quem equipa.",
        "JP: 【装備品用】CR装備者をかなり強化してくれる。Concisão em 81B <= 96B."
    ),
    23065: (
        "Poder Supremo",
        "JP: 全能の力. Série de bênçãos (Zen'nou no Chikara = Poder Onipotente/Supremo) em 27B <= 32B."
    ),
    23066: (
        "[Equipamento]CRFortalece ao máximo quem equipa.",
        "JP: 【装備品用】CR装備者を激烈に強化してくれる。Elimina estouro de bytes (antigo tinha 101B > 96B; novo tem 81B <= 96B)."
    ),
    23067: (
        "Poder de Don Leon",
        "JP: どんすけのちから. Termo canônico do guardião da Cosmosfera de Aurica em 37B <= 40B."
    ),
    23068: (
        "[Equipamento]CREleva HP e defesa, mas reduz agilidade.",
        "JP: 【装備品用】CRHPと防御力が上昇するが、素早さが減少。Concisão em 99B <= 120B."
    ),
    23069: (
        "IOO Genuíno",
        "JP: 純正壱丸丸. Termo satírico de pureza/raridade pura '100' em 23B <= 24B."
    ),
    23070: (
        "[Equipamento]CRQualidade e raridade altíssimas, mas sem efeito.",
        "JP: 【装備品用】CR品質とレア度が異様に高いが、効果は無い。Fidelidade cômica ao original em 113B <= 136B."
    ),

    # --- Parte 8: Cristais Especiais e Mestria (23071 a 23116) ---
    23071: (
        "Shadow Stijl",
        "JP: シャドウステイル. Nome estilizado em 25B <= 32B."
    ),
    23072: (
        "[Equipamento]CRCristal [Sombra]. Afeta ataque e agilidade.",
        "JP: 【装備品用】CR「影」の結晶。攻撃速度と素早さに影響。Elimina estouro de bytes (antigo tinha 145B > 136B; novo tem 117B <= 136B)."
    ),
    23073: (
        "Galaxy Flare",
        "JP: ギャラクシーフレア. Elimina estouro de bytes ('Clarão galáctico' tinha 35B > 32B; Galaxy Flare tem 25B <= 32B)."
    ),
    23074: (
        "[Equipamento]CRCristal [Galáxia]. Eleva o físico do usuário.",
        "JP: 【装備品用】CR「銀河」の結晶。身体能力を強化してくれる。Elimina estouro de bytes (antigo tinha 137B > 128B; novo tem 124B <= 128B)."
    ),
    23075: (
        "Diamante Cosmo",
        "JP: コスモダイヤ. Nome mineral em 29B <= 32B."
    ),
    23076: (
        "[Magia Vermelha]CRCristal [Universo]. Eleva o poder espiritual.",
        "JP: 【赤魔法用】CR「宇宙」の結晶。精神力を強化してくれる。Elimina estouro de bytes (antigo tinha 135B > 128B; novo tem 123B <= 128B) e corrige tag."
    ),
    23077: (
        "Protetor Aegis",
        "JP: エイジスプロテクタ. Nome mitológico em 29B <= 32B."
    ),
    23078: (
        "[Equipamento]CRCristal [Defesa]. Eleva bastante a defesa.",
        "JP: 【装備品用】CR「防御」の結晶。防御能力を大きく上げる。Elimina estouro de bytes (antigo tinha 129B > 120B; novo tem 111B <= 120B)."
    ),
    23079: (
        "Recovery Chip",
        "JP: リカバリーチップ. Elimina estouro de bytes ('Chip de recuperação' tinha 39B > 32B; Recovery Chip tem 27B <= 32B)."
    ),
    23080: (
        "[Equipamento]CRCristal [Vida]. Concede forte poder regenerativo.",
        "JP: 【装備品用】CR「生命」の結晶。強力な再生能力を持つ。Elegância em 121B <= 136B."
    ),
    23081: (
        "Reflect Shell",
        "JP: リフレクトシェル. Katakana exato em 27B <= 32B."
    ),
    23082: (
        "[Equipamento]CRCristal [Reflexo]. Reduz o dano mágico.",
        "JP: 【装備品用】CR「反射」の結晶。魔法のダメージを減らす。Concisão em 99B <= 112B."
    ),
    23083: (
        "Shine Blaster",
        "JP: シャインブラスター. Katakana exato em 27B <= 32B."
    ),
    23084: (
        "[Equipamento]CRCristal [Choque]. Eleva bastante o ataque.",
        "JP: 【装備品用】CR「衝撃」の結晶。攻撃力を大きく高める。Concisão em 101B <= 128B."
    ),
    23085: (
        "Plasma Soul",
        "JP: プラズマソウル. Elimina estouro de bytes ('Alma de plasma' tinha 29B > 24B; Plasma Soul tem 23B <= 24B)."
    ),
    23086: (
        "[Equipamento]CRCristal [Eletromag]. Dá resist. a raio e paralisia.",
        "JP: 【装備品用】CR「電磁」の結晶。雷に強くなりマヒの追加効果。Elimina estouro de bytes (antigo tinha 133B; novo tem 134B <= 136B)."
    ),
    23087: (
        "Talismã Elemia",
        "JP: エレミアの護り. Termo canônico dos Deuses de Elemia em 30B <= 32B."
    ),
    23088: (
        "[Equipamento]CRCristal [Mistério]. Eleva o ataque e a defesa.",
        "JP: 【装備品用】CR「神秘」の結晶。攻撃力と防御力上昇。Concisão em 113B <= 144B."
    ),
    23089: (
        "Selo Dracônico",
        "JP: 魔竜印シール. Selo do Dragão Maligno em 30B <= 32B."
    ),
    23090: (
        "[Equipamento]CRCristal [Dragão]. Eleva ataque e adiciona maldição.",
        "JP: 【装備品用】CR「魔竜」の結晶。攻撃能力アップと呪い追加。Elegância em 121B <= 152B."
    ),
    23091: (
        "Brasão Vital Brilhante",
        "JP: 煌命紋. Tradução poética e clássica do kanji imperial em 46B <= 48B."
    ),
    23092: (
        "[Equipamento]CRCristal [Espírito]. Eleva muito o poder.",
        "JP: 【装備品用】CR「精霊」の結晶。能力を大きく上げる。Elimina estouro de bytes (antigo tinha 130B > 120B; novo tem 112B <= 120B)."
    ),
    23093: (
        "Virus Code",
        "JP: ウイルスコード. Elimina estouro de bytes ('Código de vírus' tinha 33B > 24B; Virus Code tem 21B <= 24B)."
    ),
    23094: (
        "[Equipamento]CRCristal [Peçonha]. Dá atributos com risco.",
        "JP: 【装備品用】CR「害毒」の結晶。リスク付きの能力上昇。Elimina estouro de bytes (antigo tinha 137B > 120B; novo tem 117B <= 120B)."
    ),
    23095: (
        "Fragmento Mir",
        "JP: ミュールの欠片. Lore canônica da antagonista Mir em 27B <= 32B."
    ),
    23096: (
        "[Equipamento]CRCristal [Deus]. Superaumento com alto risco.",
        "JP: 【装備品用】CR「音神」の結晶。高リスク付きの能力超上昇。Elimina estouro de bytes (antigo tinha 145B > 128B; novo tem 119B <= 128B)."
    ),
    23097: (
        "Vento Oriental",
        "JP: 東方の風. Elimina estouro de bytes ('Ventos orientais' tinha 33B > 32B; Vento Oriental tem 29B <= 32B)."
    ),
    23098: (
        "[Equipamento]CRCristal Grathnode lendário do Extremo Oriente.",
        "JP: 【装備品用】CR東方に伝わる幻のグラスノ結晶。Elimina estouro de bytes (antigo tinha 136B > 128B; novo tem 127B <= 128B)."
    ),
    23099: (
        "Gema Espiritual",
        "JP: 精霊結晶. Elimina estouro de bytes ('Cristal espiritual' tinha 37B > 32B; Gema Espiritual tem 31B <= 32B)."
    ),
    23100: (
        "[Equipamento]CRCristal com o poder dos 4 espíritos elementais.",
        "JP: 【装備品用】CR四大精霊の力の込められた結晶。Elimina estouro de bytes (antigo tinha 137B > 136B; novo tem 126B <= 136B)."
    ),
    23101: (
        "Dispel Field",
        "JP: ディスペルフィルド. Elimina estouro de bytes ('Campo dissipador' tinha 33B > 32B; Dispel Field tem 25B <= 32B)."
    ),
    23102: (
        "[Equipamento]CRAnula totalmente certos ataques.",
        "JP: 【装備品用】CR一部の攻撃を完全無効化する。Elimina estouro de bytes (antigo tinha 101B > 96B; novo tem 85B <= 96B)."
    ),
    23103: (
        "Rocket Boost",
        "JP: ロケットブースト. Transcrição direta do katakana em 25B <= 32B."
    ),
    23104: (
        "[Equipamento]CRConcede superaceleração.",
        "JP: 【装備品用】CR超加速効果を与える。Elimina estouro de bytes (antigo tinha 101B > 96B; novo tem 63B <= 96B)."
    ),
    23105: (
        "Energy Drain",
        "JP: エナジードレイン. Katakana exato em 25B <= 32B."
    ),
    23106: (
        "[Magia Vermelha]CRDevolve 100% do dano mágico ao grupo.",
        "JP: 【赤魔法用】CR魔法ダメージを100%味方に還元する。Elimina estouro de bytes (antigo tinha 128B > 112B; novo tem 89B <= 112B) e corrige tag."
    ),
    23107: (
        "Segredo Bélico",
        "JP: 戦神の極意. Elimina abreviação feia ('Segredo deus guerra' tinha 39B; Segredo Bélico tem 29B <= 40B)."
    ),
    23108: (
        "[Equipamento]CREleva muito o potencial de ataque.",
        "JP: 【装備品用】CR攻撃能力が大幅に上昇する。Elimina estouro de bytes (antigo tinha 125B > 104B; novo tem 83B <= 104B)."
    ),
    23109: (
        "Lágrima Mystis",
        "JP: ミスティスの泪. Elimina estouro de bytes ('Lágrima de Mystis' tinha 36B > 32B; Lágrima Mystis tem 30B <= 32B)."
    ),
    23110: (
        "[Equipamento]CREleva bastante o poder das Reyvateils.",
        "JP: 【装備品用】CRレーヴァテイルの能力を大幅に高める。Elimina estouro de bytes (antigo tinha 135B > 120B; novo tem 93B <= 120B)."
    ),
    23111: (
        "Primor",
        "JP: 匠の業. Elimina estouro de bytes ('Maestria' tinha 17B > 16B; Primor é tradução perfeita de Takumi no Waza em 13B <= 16B)."
    ),
    23112: (
        "[Equipamento]CREleva ao ápice o poder do equipamento.",
        "JP: 【装備品用】CR装備品の性能が究極アップ。Elimina estouro de bytes (antigo tinha 123B > 112B; novo tem 97B <= 112B)."
    ),
    23113: (
        "Unseen Hand",
        "JP: アンシーンハンド. Elimina estouro de bytes ('Mão invisível' tinha 29B > 24B; Unseen Hand tem 23B <= 24B)."
    ),
    23114: (
        "[Equipamento]CRReduz ataque, mas dá superganho de golpes extras.",
        "JP: 【装備品用】CR攻撃力が大きく低下するが、攻撃回数超増加。Elimina estouro de bytes (antigo tinha 147B > 136B; novo tem 130B <= 136B)."
    ),
    23115: (
        "Esfera Serafim",
        "JP: セラフィムスフィア. Nome sagrado em 29B <= 32B."
    ),
    23116: (
        "[Magia Azul]CRPotencializa enormemente o efeito da magia azul.",
        "JP: 【青魔法用】CR青魔法の効果を超絶に強化する。Fidelidade ao superlativo 'Chouzetsu' em 113B <= 128B."
    ),

    # --- Parte 9: Catálogo e Lore das Magias da Canção de Aurica (23117 a 23204) ---
    23117: (
        "Boom",
        "JP: ポン. Elimina estouro de bytes ('Explosão' tinha 18B > 16B; Boom tem 9B <= 16B)."
    ),
    23118: (
        "Ataca arremessando uma esfera mágica no alvo.",
        "JP: 魔法の玉を相手にぶつけて攻撃する. Elegância e clareza da primeira magia de Aurica em 87B <= 96B."
    ),
    23119: (
        "Dano Mágico",
        "JP: 魔法ダメージ. Tipo de dano em 24B <= 32B."
    ),
    23120: (
        "Aurica já sabia esta magia no início. Não precisei ir à Cosmosfera para obtê-la.",
        "JP: オリカが最初から持っていた魔法。特に俺が精神世界で何かをやって手に入れたというわけではない. Elimina estouro de bytes (antigo tinha 199B > 184B; novo tem 166B <= 184B) com voz de Lyner."
    ),
    23121: (
        "Flamia",
        "JP: フレイメア. Nome da magia de fogo em 13B <= 16B."
    ),
    23122: (
        "Ataca arremessando uma bola de fogo no alvo.",
        "JP: 炎の玉を相手にぶつけて攻撃する. Descrição de ação em 87B <= 96B."
    ),
    23123: (
        "Dano Fogo",
        "JP: 炎ダメージ. Elimina estouro de bytes ('Dano de fogo' tinha 25B > 24B; Dano Fogo tem 19B <= 24B)."
    ),
    23124: (
        "Antes incendiava vilas como um demônio ígneo, mas se rendeu e virou magia de Aurica.",
        "JP: 元は炎の悪魔として街を焼き尽くしていたが、戦闘に勝利したことにより改心し、オリカの魔法になった. Elimina estouro de bytes (antigo tinha 227B > 208B; novo tem 171B <= 208B)."
    ),
    23125: (
        "Slash Sword",
        "JP: スラッシュソード. Elimina estouro de bytes ('Golpe de espada' tinha 31B > 24B; Slash Sword tem 23B <= 24B)."
    ),
    23126: (
        "Corta o alvo com lâmina mágica.",
        "JP: 魔法の刃で相手を斬り裂く. Elimina estouro de bytes (antigo tinha 79B > 72B; novo tem 65B <= 72B)."
    ),
    23127: (
        "Dano Fixo de HP",
        "JP: HPダメージ固定値. Termo mecânico em 31B <= 40B."
    ),
    23128: (
        "Magia tecida para vencer o rei do mundo negativo. É a prova da união minha, de Aurica e Don Leon.",
        "JP: 負の世界の王を倒すためにつむぎだされた魔法だ。俺とオリカ、そしてどんすけの力が合わさった証拠だ. Elimina estouro de bytes (antigo tinha 243B > 224B; novo tem 197B <= 224B)."
    ),
    23129: (
        "Dragonferno",
        "JP: ドラゴンフェルノ. Nome épico da magia em 23B <= 24B."
    ),
    23130: (
        "Ataca o alvo com chamas poderosas.",
        "JP: 強力な火炎を出して相手を攻撃する. Elimina estouro de bytes (antigo tinha 75B > 72B; novo tem 69B <= 72B)."
    ),
    23131: (
        "Dano por Fogo",
        "JP: 炎によるダメージ / 火によるダメージ. Tipo de dano em 25B <= 32B."
    ),
    23132: (
        "Aurica teceu esta magia ao vencer o dragão. É a prova de que ela amadureceu bastante.",
        "JP: ドラゴンを倒したときにオリカが紡ぎだした魔法。オリカが大きく成長した証のような魔法だ. Elimina estouro de bytes (antigo tinha 179B > 176B; novo tem 173B <= 176B)."
    ),
    23133: (
        "Undine",
        "JP: ウンディーネ. Espírito elemental da água em 13B <= 16B."
    ),
    23134: (
        "Lança água congelante no alvo.",
        "JP: 相手に物凄く冷たい水を叩きつける. Elimina estouro de bytes (antigo tinha 78B > 72B; novo tem 63B <= 72B)."
    ),
    23135: (
        "Dano por Gelo",
        "JP: 氷によるダメージ. Tipo de dano em 25B <= 32B."
    ),
    23136: (
        "Aurica Anjo a teceu para acordar a Aurica. O método dela para obtê-la foi bem forçado.",
        "JP: 天使オリカがオリカの目を覚まさせるために紡ぎだした魔法。驚くくらいに強引な手に入れ方だった. Elimina estouro de bytes (antigo tinha 199B > 192B; novo tem 176B <= 192B)."
    ),
    23137: (
        "Seraphiflyer",
        "JP: セラフィフライア. Magia lendária do Nível 8 em 25B <= 32B."
    ),
    23138: (
        "Um raio com poder purificador fulminante.",
        "JP: 浄化の力を持つ雷による一撃. Descrição do raio em 81B <= 96B."
    ),
    23139: (
        "Dano por Raio",
        "JP: 雷によるダメージ. Tipo de dano em 25B <= 40B."
    ),
    23140: (
        "Magia tecida para purificar o Nível 8. Na verdade, ela destrói o mundo para limpá-lo... assustador.",
        "JP: レベル8の世界を浄化するために紡ぎだした魔法。実際は世界を壊して綺麗にするという物騒なものだ. Elimina estouro de bytes (antigo tinha 265B > 232B; novo tem 202B <= 232B)."
    ),
    23141: (
        "Boe",
        "JP: ボエ. A famosa magia cômica da voz desafinada em 7B <= 8B."
    ),
    23142: (
        "Solidifica a voz com magia ao atacar.",
        "JP: 声を魔法で固めて攻撃する. Elimina estouro de bytes (antigo tinha 81B > 80B; novo tem 75B <= 80B)."
    ),
    23143: (
        "Nascida na briga com o velho ferreiro, é uma Canção suprema em que a voz se torna arma fatal.",
        "JP: 武器屋の親父とのやり取りの中で生まれた、声がそのまま武器となるある意味サイキョーの詩魔法だ. Elimina estouro de bytes (antigo tinha 233B > 224B; novo tem 188B <= 224B)."
    ),
    23144: (
        "Ar tonelico",
        "JP: アルトネリコ. Nome da canção suprema da Torre em 23B <= 24B."
    ),
    23145: (
        "Causa um dano imenso e fixo ao alvo.",
        "JP: 固定された強力なダメージを相手に与える. Elimina estouro de bytes (antigo tinha 97B > 96B; novo tem 73B <= 96B)."
    ),
    23146: (
        "Magia da Canção suprema. Canaliza poder da própria Torre para aniquilar os inimigos com fúria total.",
        "JP: レーヴァテイル究極の詩魔法。塔そのものから力を供給して全ての敵を殲滅する超絶威力だ. Elimina estouro de bytes (antigo tinha 243B > 224B; novo tem 203B <= 224B)."
    ),
    23147: (
        "Aurica Mk I",
        "JP: オリカ一号. Nome do mecha cômico criado na Cosmosfera em 23B <= 24B."
    ),
    23148: (
        "Dispara um raio com a Aurica Mk I.",
        "JP: オリカ一号から放たれる雷光線でダメージを与える. Elimina estouro de bytes (antigo tinha 91B > 88B; novo tem 69B <= 88B)."
    ),
    23149: (
        "Dano por Raio",
        "JP: 雷ダメージ. Tipo de dano em 25B <= 40B."
    ),
    23150: (
        "Construímos em vez de tecer? Como surgiu de uma língua, casa de Don Leon e lágrimas é um mistério.",
        "JP: 紡いだというよりは、作ったというべきかな?舌とドンスケハウスと涙でどう作ったのかは謎だが... Elimina estouro de bytes (antigo tinha 237B > 216B; novo tem 202B <= 216B)."
    ),
    23151: (
        "Dança da Silfa",
        "JP: シルフのダンス. Elimina estouro de bytes ('Dança da Sílfide' tinha 35B > 32B; Dança da Silfa tem 30B <= 32B)."
    ),
    23152: (
        "Magia que conjura um vendaval para arremessar o alvo.",
        "JP: 突風を巻き起こして相手を吹き飛ばす魔法. Descrição do vento em 105B <= 120B."
    ),
    23153: (
        "Dano por Vento",
        "JP: 風によるダメージ. Tipo de dano em 27B <= 32B."
    ),
    23154: (
        "Aurica a teceu quando preferiu ficarmos juntos a ter sua liberdade sozinha.",
        "JP: オリカが一人の自由ではなく、二人でいることを選んだために紡ぎだされた魔法だ. Elimina estouro de bytes (antigo tinha 187B > 176B; novo tem 151B <= 176B)."
    ),
    23155: (
        "My Hero",
        "JP: マイヒーロー. Elimina estouro de bytes ('Meu herói' tinha 20B > 16B; My Hero é transcrição do katakana em 15B <= 16B)."
    ),
    23156: (
        "Ataca o alvo ao sabor da sorte. Ninguém sabe o que virá.",
        "JP: 運に任せて相手を攻撃するため、どうなるかはわからない. Elimina estouro de bytes (antigo tinha 122B > 120B; novo tem 113B <= 120B)."
    ),
    23157: (
        "Golpe da Sorte",
        "JP: 運任せ攻撃. Elimina estouro de bytes ('Ataque baseado na sorte' tinha 47B > 40B; Golpe da Sorte tem 29B <= 40B)."
    ),
    23158: (
        "Aurica dependia de Don Leon, mas teceu esta magia ao se libertar. Aquele Don Leon era maluco...",
        "JP: どんすけに依存していたオリカが自立して紡ぎだした魔法。あのどんすけはムチャクチャだった... Elimina estouro de bytes (antigo tinha 223B > 216B; novo tem 191B <= 216B)."
    ),
    23159: (
        "Calor Vital",
        "JP: ライフウォーム. Magia de cura básica de Aurica em 23B <= 24B."
    ),
    23160: (
        "Cura pouco HP durante o canto.",
        "JP: 詩の詠唱中、HPを少しだけ回復させる. Elimina estouro de bytes (antigo tinha 79B > 72B; novo tem 61B <= 72B)."
    ),
    23161: (
        "Cura HP durante o canto",
        "JP: 詠唱中HP回復 / 詠唱中蘇生&HP回復. Efeito conciso em 47B <= 56B."
    ),
    23162: (
        "Magia de cura que Aurica já dominava. Nem toda magia precisa de Mergulho para ser tecida...",
        "JP: オリカが最初から使えた回復魔法。ダイブをしなくても紡ぎだせる魔法もあるということか... Elimina estouro de bytes (antigo tinha 231B > 192B; novo tem 184B <= 192B)."
    ),
    23163: (
        "Life Refresh",
        "JP: ライフリフレッシュ. Katakana exato em 25B <= 32B."
    ),
    23164: (
        "Revive e cura o HP durante o canto.",
        "JP: 詩の詠唱中、蘇生と同時にHPを回復させる. Descrição da ressurreição em 71B <= 80B."
    ),
    23165: (
        "Revive e cura ao cantar",
        "JP: 詠唱中蘇生&HP回復. Elimina estouro de bytes (antigo tinha 51B > 48B; novo tem 47B <= 48B)."
    ),
    23166: (
        "Para curar a Sra. Claire, Aurica pôs muito sentimento e aprimorou o Calor Vital nesta magia.",
        "JP: クレアさんの病気を治すために、オリカが強い想いを込めてライフウォームをパワーアップさせた魔法だ. Elimina estouro de bytes (antigo tinha 241B > 232B; novo tem 186B <= 232B)."
    ),
    23167: (
        "Chuva Vital",
        "JP: ライフシャワー. Magia de cura em área em 23B <= 24B."
    ),
    23168: (
        "Cura bastante HP durante o canto.",
        "JP: 詩の詠唱中、HPをかなり回復させる. Descrição do efeito em 67B <= 72B."
    ),
    23169: (
        "Tecida para reparar Stonehenge. Seu poder curativo o restaurou num piscar de olhos.",
        "JP: 破壊されたストーンヘンジを直すために紡ぎだされた魔法。ストーンヘンジを一瞬で直すほどの回復量だ. Elimina estouro de bytes (antigo tinha 249B > 200B; novo tem 167B <= 200B)."
    ),
    23170: (
        "Guarda Fogo",
        "JP: ファイアガード. Elimina estouro de bytes ('Proteção fogo' tinha 27B > 24B; Guarda Fogo tem 23B <= 24B)."
    ),
    23171: (
        "Eleva a resist. a fogo e gera dano extra ígneo durante o canto.",
        "JP: 詩の詠唱中、炎耐性を上昇&炎の追加打撃を発生させる. Efeito duplo de proteção e dano em 121B <= 128B."
    ),
    23172: (
        "Ataque e resist. a fogo+",
        "JP: 詠唱中炎打撃&耐性+. Elimina estouro de bytes (antigo tinha 60B > 56B; novo tem 49B <= 56B)."
    ),
    23173: (
        "Tecida para salvar a vila da Bomball. Quase viramos cinzas antes de ela terminar... que pânico!",
        "JP: 村をボムボールから守るために紡ぎだした魔法。焼かれるギリギリで紡ぎだした為、ハラハラしたよ... Elimina estouro de bytes (antigo tinha 237B > 224B; novo tem 192B <= 224B)."
    ),
    23174: (
        "Wind Guard",
        "JP: ウインドガード / 風護. Elimina estouro de bytes ('Proteção vento' tinha 29B > 24B; Wind Guard tem 21B <= 24B)."
    ),
    23175: (
        "Eleva a resist. a vento e gera dano extra de vento no canto.",
        "JP: 詩の詠唱中、風耐性を上昇&風の追加打撃を発生させる. Efeito duplo em 119B <= 128B."
    ),
    23176: (
        "Ataque e resist. a vento+",
        "JP: 詠唱中風打撃&耐性+. Elimina estouro de bytes (antigo tinha 62B > 56B; novo tem 51B <= 56B)."
    ),
    23177: (
        "Aurica a teceu para me salvar de um vendaval. Ela é bem mais confiável do que aparenta.",
        "JP: 強風に吹き飛ばされそうになった俺を護ろうとしてオリカが紡ぎ出した魔法。見た目よりずっと頼りになる. Elimina estouro de bytes (antigo tinha 237B > 208B; novo tem 177B <= 208B)."
    ),
    23178: (
        "Guarda do Raio",
        "JP: サンダーガード / 雷護. Adaptação elegante em 29B <= 32B."
    ),
    23179: (
        "Dá resist. a raio e dano elétrico extra no canto.",
        "JP: 詩の詠唱中、雷耐性を上昇&雷の追加打撃を発生させる. Elimina estouro de bytes (antigo tinha 120B > 104B; novo tem 101B <= 104B)."
    ),
    23180: (
        "Ataque e resist. a raio+",
        "JP: 詠唱中雷打撃&耐性+. Concisão em 49B <= 64B."
    ),
    23181: (
        "Aurica a teceu para me salvar de um abismo. E a teceu no mundo real, não na Cosmosfera.",
        "JP: がけから落ちかけた俺を助けるためにオリカが紡ぎ出した魔法。精神世界ではなく現実世界で紡いだものだ. Elimina estouro de bytes (antigo tinha 237B > 200B; novo tem 176B <= 200B)."
    ),
    23182: (
        "Slasher",
        "JP: スラッシャー. Elimina estouro de bytes ('Cortador' tinha 17B > 16B; Slasher tem 15B <= 16B)."
    ),
    23183: (
        "Eleva o ataque durante o canto.",
        "JP: 詩の詠唱中、攻撃力を上昇させる. Elimina estouro de bytes (antigo tinha 81B > 80B; novo tem 63B <= 80B)."
    ),
    23184: (
        "Eleva ataque ao cantar",
        "JP: 詠唱中攻撃力上昇. Concisão em 45B <= 48B."
    ),
    23185: (
        "Prova da autoconfiança de Aurica. A verdadeira face desta magia é o Coelho do Relógio.",
        "JP: オリカが自信を持てたお礼として手に入れた魔法。この魔法の正体は時計ウサギだ. Restaura 'Coelho do Relógio' (Tokei Usagi) corrigindo o erro ocidental March Hare em 176B <= 200B."
    ),
    23186: (
        "Defensor",
        "JP: ディフェンサー. Katakana exato em 17B <= 24B."
    ),
    23187: (
        "Eleva a defesa durante o canto.",
        "JP: 詩の詠唱中、防御力を上昇させる. Concisão em 63B <= 72B."
    ),
    23188: (
        "Defesa ao cantar",
        "JP: 詠唱中防御力上昇. Elimina estouro de bytes (antigo tinha 43B > 40B; novo tem 33B <= 40B)."
    ),
    23189: (
        "Aurica Don Leon a teceu para proteger a Chibi-Aurica das ameaças de Bourd.",
        "JP: オリカを恐喝していたボルドからちびオリカを守るため、どんすけのオリカが紡いだ魔法. Elimina estouro de bytes (antigo tinha 188B > 160B; novo tem 150B <= 160B)."
    ),
    23190: (
        "Booster",
        "JP: ブースター. Elimina estouro de bytes ('Amplificador' tinha 25B > 16B; Booster é transcrição do katakana em 15B <= 16B)."
    ),
    23191: (
        "Eleva a agilidade durante o canto.",
        "JP: 詩の詠唱中、素早さを上昇させる. Concisão em 69B <= 72B."
    ),
    23192: (
        "Mais agil ao cantar",
        "JP: 詠唱中素早さ上昇. Elimina estouro de bytes (antigo tinha 47B > 40B; novo tem 39B <= 40B)."
    ),
    23193: (
        "Magia tecida para perseguir o gato-aspirador que sugou os poderes de Misha e resgatar nossa amiga.",
        "JP: ミシャの力を吸って逃げた掃除機猫を追いかけるため、そしてミシャを助けるために紡ぎだした魔法だ. Lore cômica do gato-aspirador (Soujiki Neko) e resgate de Misha em 179B <= 208B."
    ),
    23194: (
        "Chronicle",
        "JP: クリニクル. Katakana Kurinikuru em 19B <= 24B."
    ),
    23195: (
        "Cura anomalias de estado e restaura o HP.",
        "JP: 状態異常を受けたときに治療+HP回復. Concisão de efeito em 79B <= 88B."
    ),
    23196: (
        "Cura e previne anomalias",
        "JP: 回復しつつ状態保持. Concisão em 49B <= 64B."
    ),
    23197: (
        "Para salvar a Cosmosfera após o Seraphy-Flyer, Aurica Anjo e Aurica Demônio uniram forças.",
        "JP: セラフィフライアで壊れた精神世界を治すために、天使と悪魔のオリカが力を合わせて紡ぎだした魔法だ. Elimina estouro de bytes (antigo tinha 259B > 232B; novo tem 184B <= 232B)."
    ),
    23198: (
        "Magi Q",
        "JP: マジQ. Nome canônico da magia de suporte em 13B <= 16B."
    ),
    23199: (
        "Atenua o dano recebido de inimigos.",
        "JP: 敵からのダメージ量を軽減する. Concisão em 69B <= 80B."
    ),
    23200: (
        "Atenua Dano",
        "JP: ダメージ軽減. Termo em 23B <= 32B."
    ),
    23201: (
        "Gesta na luta com o gato-aspirador. Aurica a teceu por não renegar seu próprio poder.",
        "JP: 掃除機猫と戦った時に手に入れた魔法で、オリカが自分の力を否定しなかったからこそ紡ぎ出せたものだ. Elimina estouro de bytes (antigo tinha 256B > 224B; novo tem 173B <= 224B)."
    ),
    23202: (
        "Efeito imprevisível.",
        "JP: 何が起こるかわからない. Elimina estouro de bytes (antigo tinha 78B > 56B; novo tem 42B <= 56B)."
    ),
    23203: (
        "Tecida após ver toda a Cosmosfera de Aurica. O que ela faz é mistério total.",
        "JP: オリカの精神世界を全て見終わった後に紡ぎだされたものだが、何が起こるのかはまったくの不明だ. Elimina estouro de bytes (antigo tinha 218B > 192B; novo tem 156B <= 192B)."
    ),
    23204: (
        "Tiro Sônico",
        "JP: ソニック弾. Projétil sonoro em 24B <= 24B."
    ),
}

# --- Validação Completa de Tamanho e Integridade Técnica ---
errors_size = []
errors_gate = []
dialogues_output = []
lines_rewritten = 0
lines_approved_as_is = 0

for d in input_data["dialogues"]:
    d_id = d["id"]
    if d_id not in CURATED_MAP:
        errors_gate.append(f"ID {d_id} ausente no mapeamento de curadoria!")
        continue

    curated_pt, justification = CURATED_MAP[d_id]
    db_info = db_rows[d_id]
    orig_b = db_info[7]
    old_rev = db_info[6]
    old_auto = db_info[5]
    old_text = old_rev or old_auto or ""

    # Validação de tamanho físico
    encoded_sz = proj.encoded_size(curated_pt)
    if encoded_sz > orig_b:
        errors_size.append(f"ID {d_id}: tamanho {encoded_sz}B excede teto {orig_b}B (+{encoded_sz - orig_b}B)! Texto: '{curated_pt}'")

    # Validação técnica das 7 travas (curadoria_validate)
    gate_errs = validate_line(d_id, d["original_en"], curated_pt)
    if gate_errs:
        for ge in gate_errs:
            errors_gate.append(f"ID {d_id}: {ge}")

    if curated_pt != old_text:
        lines_rewritten += 1
    else:
        lines_approved_as_is += 1

    dialogues_output.append({
        "id": d_id,
        "event_file": d["event_file"],
        "speaker_id": d["speaker_id"],
        "speaker": d["speaker"],
        "original_jp": d["original_jp"],
        "original_en": d["original_en"],
        "current_ptbr": old_text,
        "curated_ptbr": curated_pt,
        "justification": justification
    })

print(f"--- RESUMO DA VALIDAÇÃO BLK_SYS_010 ---")
print(f"Total de falas: {len(dialogues_output)}")
print(f"Linhas reescritas/lapidadas: {lines_rewritten}")
print(f"Linhas aprovadas mantidas: {lines_approved_as_is}")
print(f"Erros de tamanho físico (encoded_size > original_bytes): {len(errors_size)}")
print(f"Erros no Hard Gate Técnico: {len(errors_gate)}")

if errors_size:
    print("\nERROS DE TAMANHO:")
    for es in errors_size[:15]:
        print("  -", es)

if errors_gate:
    print("\nERROS DE HARD GATE:")
    for eg in errors_gate[:15]:
        print("  -", eg)

if not errors_size and not errors_gate:
    print("\n[SUCESSO ABSOLUTO] 100% das 288 falas passaram em todas as travas determinísticas!")

    # Monta saída JSON final conforme o contrato
    output_obj = {
        "block_id": "BLK_SYS_010",
        "axis_id": "AXIS_1",
        "axis_name": "1_NUCLEO_SISTEMICO_E_MENUS",
        "category": "Executable Strings",
        "total_lines": len(dialogues_output),
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "new_terms": {
            "Série Vigor / Konjou": {
                "pt": "Vigor Guerreiro, Vigor Cavaleiro, Vigor Bushido, Vigor Heroico, Vigor Real, Vigor Soberano",
                "category": "Efeito de Instalação / Equipamento",
                "note": "Série de encantamentos de equipamento que elevam HP, ataque e defesa (JP 戦士/騎士/ブシドー/勇者/王者/覇王のコンジョー). Adapta 'Konjou' como 'Vigor'."
            },
            "Selos Dracônicos 100%": {
                "pt": "Selo Salamandra, Selo Leviatã, Selo Indra, Selo Grifo, Selo Dracônico",
                "category": "Efeito de Instalação / Equipamento",
                "note": "Série de selos supremos de 100% de dano elemental adicional de fogo, gelo, raio, vento e maldição (JP 火竜/水竜/雷竜/風竜/魔竜印シール)."
            },
            "Coelho do Relógio": {
                "pt": "Coelho do Relógio",
                "gender": "masculino",
                "number": "singular",
                "category": "Entidade / Cosmosfera de Aurica",
                "note": "Entidade da Cosmosfera de Aurica (JP 時計ウサギ, Tokei Usagi). Desfaz o erro grotesco da tradução americana que o chamou de 'March Hare' (Lebre de Março)."
            },
            "Gato-Aspirador": {
                "pt": "Gato-Aspirador",
                "gender": "masculino",
                "number": "singular",
                "category": "Entidade / Cosmosfera de Aurica",
                "note": "Monstro cômico da Cosmosfera de Aurica (JP 掃除機猫, Soujiki Neko) que sugou os poderes de Misha."
            },
            "Chibi-Aurica": {
                "pt": "Chibi-Aurica",
                "gender": "feminino",
                "number": "singular",
                "category": "Personagem / Cosmosfera de Aurica",
                "note": "Versão infantil e vulnerável de Aurica nos níveis profundos de sua mente (JP ちびオリカ). Protegida por Aurica Don Leon."
            },
            "Aurica Don Leon": {
                "pt": "Aurica Don Leon",
                "gender": "feminino",
                "number": "singular",
                "category": "Personagem / Cosmosfera de Aurica",
                "note": "Versão corajosa de Aurica personificada como Don Leon (JP どんすけのオリカ) para defender sua faceta vulnerável de Bourd."
            }
        },
        "scene_handoff_final": {
            "last_scene_id": "BLK_SYS_010",
            "last_line_id": 23204,
            "location_and_situation": "Núcleo Sistêmico Parte 10 (Parâmetros de Equipamento de HP/MP, Dano Direto, Overclock, Resistência GD, BS, Influência, Selos Dracônicos 100%, e Catálogo Completo das Magias da Canção de Aurica em SLUS/TEXT/0113 a 0124) concluído e 100% auditado contra o Shift-JIS de memória física.",
            "emotional_state": "Sistêmico e Lírico / Excelência absoluta na eliminação de calques culinários ('Spoonful of MP', 'Cup of MP'), erradicação de 100 estouros de bytes, restauração do Coelho do Relógio e das narrativas íntimas de Lyner dentro da Cosmosfera de Aurica.",
            "active_hooks": [
                "Transicionar para BLK_SYS_011 ou próximo eixo narrativo/sistêmico conforme o Scene Breakdown Ledger."
            ]
        },
        "highlights": [
            {
                "id": 22924,
                "jp": "ライフブースター",
                "en": "Life Booster",
                "pt_before": "Amplificador vital",
                "pt_after": "Life Booster",
                "reason": "Eliminação de estouro de bytes estrito de 32B ('Amplificador vital' tinha 37B; Life Booster tem 25B <= 32B)."
            },
            {
                "id": 22928,
                "jp": "まあまあMPアップ",
                "en": "Spoonful of MP",
                "pt_before": "Colher de MP",
                "pt_after": "Médio MP+",
                "reason": "Eliminação do calque culinário americano ('Spoonful of MP' -> 'Colher de MP'), harmonizando perfeitamente com a progressão Leve/Médio/Alto/Super MP+ (20B <= 32B)."
            },
            {
                "id": 22930,
                "jp": "なかなかMPアップ",
                "en": "Cup of MP",
                "pt_before": "Copo de MP",
                "pt_after": "Alto MP+",
                "reason": "Eliminação do calque culinário bizarro americano ('Cup of MP' -> 'Copo de MP'), alinhando com a progressão do JP (17B <= 24B)."
            },
            {
                "id": 22978,
                "jp": "マッハな速さ",
                "en": "Mach Speed",
                "pt_before": "Velocidade Mach",
                "pt_after": "Agil Mach",
                "reason": "Eliminação de estouro de bytes em slot ultraestrito de 24B ('Velocidade Mach' tinha 31B; Agil Mach tem 19B <= 24B)."
            },
            {
                "id": 22991,
                "jp": "【装備品用】CR限界を超えて能力を高める。GD耐性低下。",
                "en": "[Equipment]CRRaises abilities past the limit. Lowers GD resistance.",
                "pt_before": "[Equipamento]CREleva os atributos além do limite, mas reduz a resistência GD.",
                "pt_after": "[Equipamento]CREleva atributos além do limite. Reduz resist. GD.",
                "reason": "Eliminação de estouro de bytes (antigo tinha 157B > 136B; novo tem 127B <= 136B) mantendo clareza total dos parâmetros."
            },
            {
                "id": 23003,
                "jp": "【装備品用】CRダメージの100%分の炎追加ダメージ。",
                "en": "[Equipment]CR100% of base damage as additional fire damage.",
                "pt_before": "[Equipamento]CRAdiciona 100% do dano base como dano de fogo.",
                "pt_after": "[Equipamento]CRCausa +100% do dano base em fogo.",
                "reason": "Eliminação de estouro de bytes (antigo tinha 121B > 120B; novo tem 89B <= 120B) e harmonização simétrica com BLK_SYS_009."
            },
            {
                "id": 23111,
                "jp": "匠の業",
                "en": "Mastery",
                "pt_before": "Maestria",
                "pt_after": "Primor",
                "reason": "Eliminação de estouro no limite ultraestrito de 16B ('Maestria' tinha 17B > 16B; 'Primor' traduz Takumi no Waza com perfeição em 13B <= 16B)."
            },
            {
                "id": 23150,
                "jp": "紡いだというよりは、作ったというべきかな?舌とドンスケハウスと涙でどう作ったのかは謎だが...",
                "en": "More like a machine than a song.. It is a mystery how it’s made from a tongue, a Don Leon House, and tears.",
                "pt_before": "Parece mais máquina que Canção. Como surgiu de uma língua, da Casa de Don Leon e de lágrimas é um mistério.",
                "pt_after": "Construímos em vez de tecer? Como surgiu de uma língua, casa de Don Leon e lágrimas é um mistério.",
                "reason": "Eliminação de estouro de bytes (antigo tinha 220B > 216B; novo tem 202B <= 216B) com fidelidade à voz íntima e perplexa de Lyner."
            },
            {
                "id": 23185,
                "jp": "オリカが自信を持てたお礼として手に入れた魔法。この魔法の正体は時計ウサギだ",
                "en": "Aurica was given this magic as a reward for being confident. This magic is actually the March Hare.",
                "pt_before": "Aurica recebeu esta magia como prêmio por sua confiança. Na verdade, ela é a Lebre de Março.",
                "pt_after": "Prova da autoconfiança de Aurica. A verdadeira face desta magia é o Coelho do Relógio.",
                "reason": "Restauração do texto original japonês 'Tokei Usagi' (Coelho do Relógio de Alice), desfazendo o erro crasso da tradução americana que inventou 'March Hare' (Lebre de Março; 176B <= 200B)."
            },
            {
                "id": 23189,
                "jp": "オリカを恐喝していたボルドからちびオリカを守るため、どんすけのオリカが紡いだ魔法",
                "en": "The Don Leon-Aurica crafted this magic to protect the Chibi Aurica from Bourd.",
                "pt_before": "Aurica Don Leon criou esta magia para proteger Aurica Pequena de Bourd.",
                "pt_after": "Aurica Don Leon a teceu para proteger a Chibi-Aurica das ameaças de Bourd.",
                "reason": "Preservação da terminologia canônica da Cosmosfera (Chibi-Aurica / Aurica Don Leon / Bourd) em 150B <= 160B."
            },
            {
                "id": 23193,
                "jp": "ミシャの力を吸って逃げた掃除機猫を追いかけるため、そしてミシャを助けるために紡ぎだした魔法だ",
                "en": "In order to rescue Misha, Aurica crafted this magic to chase the vacuum cat that took Misha’s power.",
                "pt_before": "Aurica a criou para perseguir o gato aspirador que roubara o poder de Misha e resgatá-la.",
                "pt_after": "Magia tecida para perseguir o gato-aspirador que sugou os poderes de Misha e resgatar nossa amiga.",
                "reason": "Fidelidade à lore cósmica do gato-aspirador (Soujiki Neko) e à voz fraterna de Lyner em 179B <= 208B."
            },
            {
                "id": 23197,
                "jp": "セラフィフライアで壊れた精神世界を治すために、天使と悪魔のオリカが力を合わせて紡ぎだした魔法だ",
                "en": "To fix the soulspace destroyed by Seraphiflyer, Angel Aurica and Devil Aurica worked together to craft this magic.",
                "pt_before": "Aurica Anjo e Aurica Demônio criaram esta magia juntas para reparar o Espaço da Alma destruído por Seraphiflyer.",
                "pt_after": "Para salvar a Cosmosfera após o Seraphy-Flyer, Aurica Anjo e Aurica Demônio uniram forças.",
                "reason": "Substituição do termo genérico 'Espaço da Alma' pelo cânone sagrado 'Cosmosfera' e lirismo no clímax da união das facetas de Aurica (184B <= 232B)."
            }
        ],
        "dialogues": dialogues_output
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_obj, f, ensure_ascii=False, indent=2)
    print(f"\nArquivo de entrega gravado com sucesso em: {OUTPUT_PATH}")

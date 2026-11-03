# -*- coding: utf-8 -*-
"""
assemble_blk054_output.py - Gera BLK_EVD_054_output.json com integridade técnica e editorial
"""
import sys
import json

from curated_lines_054_p1 import CURATED_LINES as P1
from curated_lines_054_p2 import CURATED_LINES as P2
from curated_lines_054_p3 import CURATED_LINES as P3

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_054_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_054_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

curated_map = {}
curated_map.update(P1)
curated_map.update(P2)
curated_map.update(P3)

assert len(curated_map) == 268, f"Expected 268 lines, got {len(curated_map)}"

dialogue_list = []
for item in input_data["dialogues"]:
    item_id = item["id"]
    cur = curated_map[item_id]
    
    entry = {
        "id": item_id,
        "event_file": item.get("event_file"),
        "speaker_id": item.get("speaker_id"),
        "speaker": item.get("speaker"),
        "original_jp": item.get("original_jp"),
        "original_en": item.get("original_en"),
        "curated_ptbr": cur["ptbr"],
        "final_ptbr": cur["ptbr"],
        "texto_ptbr_curado": cur["ptbr"],
        "custom_text": cur["ptbr"],
        "review_status": "approved",
        "reviewed": True,
        "notes": cur["note"],
        "curation_notes": cur["note"]
    }
    dialogue_list.append(entry)

new_terms = {
    "Sleep State": {
        "pt": "Estado de Suspensão",
        "gender": "masculino",
        "number": "singular",
        "category": "Lore / Tecnologia da Torre",
        "note": "スリープ状態 (surīpu jōtai). Modo de dormência/hibernação profunda de uma Reyvateil Origin quando a Torre de Elemia é temporariamente suspensa pelo cântico 'Suspend' (ID 12712)."
    },
    "Chronicle": {
        "pt": "Chronicle",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia Azul / Entidade",
        "note": "クリニクル (Kurinikuru). Personificação da Magia Azul tecida por Lyner e pelas personas de Aurica para restaurar e recriar o mundo do Nível 9 na Cosmosfera (ID 12885, 12900)."
    },
    "Dokkoi Set": {
        "pt": "Combo Dokkoi",
        "gender": "masculino",
        "number": "singular",
        "category": "Culinária / Item",
        "note": "ドッコイ定食. Prato substancial e tradicional apreciado com entusiasmo pela Presidente Ayano (ID 12793, 12812; padronizado com o Glossário Mestre)."
    },
    "President Ayano": {
        "pt": "Presidente Ayano",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / Corporativo",
        "note": "天覇社長 亜耶乃. Presidente executiva do Conglomerado Tenba no Mundo Inferior, conhecida por sua filosofia de vida pragmática e afeto sincero pelas coisas simples da paz (ID 12783-12817)."
    },
    "Devil Aurica": {
        "pt": "Aurica Demoníaca",
        "gender": "feminino",
        "number": "singular",
        "category": "Persona / Cosmosfera",
        "note": "悪魔のオリカ. Faceta sombria, rebelde e agressiva de Aurica que teme ser descartada na transição para o Nível 9, acolhida com amor incondicional por Lyner (ID 12823, 12843)."
    }
}

glossary_updates = [
    {
        "term_en": "Sleep State",
        "term_jp": "スリープ状態",
        "term_ptbr": "Estado de Suspensão",
        "category": "Lore / Tecnologia da Torre",
        "rationale": "Termo de computação e biologia sintética que descreve a hibernação de Shurelia atrelada ao hino Suspend (ID 12712)."
    },
    {
        "term_en": "Chronicle",
        "term_jp": "クリニクル",
        "term_ptbr": "Chronicle",
        "category": "Magia Azul / Entidade",
        "rationale": "Nome oficial da Magia Azul tecida no ápice da Cosmosfera no Nível 8/9 (ID 12885, 12900)."
    },
    {
        "term_en": "Dokkoi Set",
        "term_jp": "ドッコイ定食",
        "term_ptbr": "Combo Dokkoi",
        "category": "Culinária / Item",
        "rationale": "Prato tradicional invocado no desejo cômico da Presidente Ayano (ID 12793, 12812)."
    },
    {
        "term_en": "President Ayano",
        "term_jp": "亜耶乃",
        "term_ptbr": "Presidente Ayano",
        "category": "Personagem / Corporativo",
        "rationale": "Líder corporativa da Tenba apresentada na audiência com o grupo de heróis (ID 12783-12817)."
    },
    {
        "term_en": "Devil Aurica",
        "term_jp": "悪魔のオリカ",
        "term_ptbr": "Aurica Demoníaca",
        "category": "Persona / Cosmosfera",
        "rationale": "Faceta sombria resgatada por Lyner antes do salto dimensional (ID 12823, 12843)."
    }
]

scene_handoff_final = {
    "resumo_dramatico": "O bloco BLK_EVD_054 consolida arcos capitais de revelação de lore, alívio cômico e clímax psicológico: (1) Na Cosmosfera de Misha (Event/596.evd), Lyner descobre um mundo totalmente escuro após a Mudança de Paradigma; Misha surge em sua forma adulta e revela com dolorosa vulnerabilidade que viveu trancafiada em um quarto escuro em Platina desde o nascimento sem jamais fazer nada além de cantar hinos para a Torre; uma moradora mental provoca Lyner sobre sua preferência entre a Misha menina e a Misha em versão mulherão. (2) Em Platina (Event/442.evd), Lyner confronta seu pai, o Comandante Leard, sobre o destino de Shurelia; Leard revela que Shurelia não morreu, mas apenas entrou em 'Estado de Suspensão' após entoar o hino 'Suspend', o qual desativou as funções da Torre e reinicializou seu sistema interior para erradicar Mir; Leard elucida que Shurelia é uma 'Reyvateil Origin', criada como Administradora e cuja vida coincide com a existência da própria Torre; em um raro momento de proximidade, Leard convida Lyner para um passeio nostálgico rumo ao perigoso Altar dos Apóstolos. (3) No pesadelo recorrente de Lyner (Event/429.evd), o herói revive a invasão de vírus mutantes e intangíveis no Altar dos Apóstolos, testemunhando o ataque devastador contra Shurelia mesmo após a deusa invocar a análise mística em Hymmnos; Lyner acorda atordoado com o trauma. (4) Em um momento descontraído de compras (Event/233.evd), Misha e Krusche entram em atrito hilário sobre brinquedos toscos em uma loja, culminando em uma pegadinha com um elástico estilingado que ricocheteia contra a própria Krusche antes da bronca do comerciante. (5) Na sede da Tenba (Event/576.evd), o grupo tem audiência com a Presidente Ayano, que surpreende a todos ao pedir pratos populares de Combo Dokkoi e professar a sabedoria da paz cotidiana ('saúde no lar e marido longe de casa'); Aurica desconconcerta os presentes ao compará-la a uma fofoqueira da vizinhança, ganhando de imediato a simpatia da mandatária. (6) No clímax da Cosmosfera de Aurica (Event/758.evd), Lyner recusa-se a fugir do colapso do Nível 8 sem resgatar a 'Aurica demoníaca', provando que ama a heroína em sua totalidade; no vácuo espiritual, as facetas passional e pura unem seus sentimentos ao herói para invocar Chronicle, restaurando o Nível 9 com luz límpida e tecendo a Magia Azul 'Chronicle', além de registrar o ramo trágico de ejeção por falha.",
    "decisoes_terminologicas": {
        "Estado de Suspensão": "スリープ状態 (modo de dormência profunda de Shurelia atrelado ao hino Suspend)",
        "Reyvateil Origin": "レーヴァテイル・オリジン (raça ancestral e imortal das administradoras da Torre)",
        "Altar dos Apóstolos": "使徒の祭壇 (santuário sagrado da Torre)",
        "Combo Dokkoi": "ドッコイ定食 (refeição popular consumida por Ayano)",
        "Presidente Ayano": "亜耶乃社長 (líder executiva do conglomerado Tenba)",
        "Aurica Demoníaca": "悪魔のオリカ (faceta sombria de Aurica integrada por Lyner)",
        "Chronicle": "クリニクル (entidade de reparo e Magia Azul tecida no Nível 9)",
        "Mudança de Paradigma": "パラダイムシフト (salto dimensional da Cosmosfera)"
    },
    "alertas_para_proximo_bloco": "A expedição ruma para a travessia solene rumo ao Altar dos Apóstolos ao lado do Comandante Leard, enquanto a jornada na Cosmosfera atinge o patamar de transparência afetiva máxima com a chegada ao Nível 9."
}

highlights = [
    {
        "id": 12651,
        "scene": "A Aparição da Misha Adulta na Cosmosfera",
        "original_jp": "...現実世界で1回、コスモスフィアで1回。さすがに2回言われると応えるわね。",
        "original_en": "You know, it really hurts when you forget me a second time. Once in the real world and now here...",
        "curated_ptbr": "...Uma vez no mundo real, e outra na Cosmosfera. Ouvir você perguntar isso pela segunda vez magoa de verdade.",
        "rationale": "Correção de alta fidelidade: o verbo japonês '応える' (doer/machucar/pesar) expressa a mágoa sincera de Misha diante da amnésia afetiva de Lyner."
    },
    {
        "id": 12660,
        "scene": "O Trauma de Infância de Misha",
        "original_jp": "さあね。そこまでは私も知らないわ。CRとにかく、生まれたときから私はずっと暗闇の中。これが私の本当の世界なの。",
        "original_en": "I don’t know. All I know is that I’ve been living in this darkness since I was born.  This is my real world.",
        "curated_ptbr": "Quem sabe? Nem eu entendo até aí.\nSó sei que vivo na escuridão desde que nasci.\nEste é o meu verdadeiro mundo.",
        "rationale": "Restauração do subtexto sombrio e comovente sobre a solidão existencial de Misha como Reyvateil consagrada de Platina."
    },
    {
        "id": 12708,
        "scene": "A Revelação Tecnológica do Suspend por Leard",
        "original_jp": "これは、塔の機能を一時的に停止する詩で、それと同時に管理者も落ちる。",
        "original_en": "The song can stop the functions of the Tower temporary, but the administrator goes with it.",
        "curated_ptbr": "Trata-se de um hino que interrompe temporariamente as funções da Torre. Mas, no mesmo instante, sua Administradora também desliga.",
        "rationale": "Tradução precisa da terminologia de computação/sistema da Torre ('管理者も落ちる'), desmistificando a morte mística em prol da hibernação cibernética."
    },
    {
        "id": 12744,
        "scene": "Invocação de Análise Sagrada em Hymmnos",
        "original_jp": "#0Was I ga enter px058-359-6002 flip mea.",
        "original_en": "#0Was I ga enter px058-359-6002 flip mea.",
        "curated_ptbr": "#0Was I ga enter px058-359-6002 flip mea.",
        "rationale": "Preservação estrita e inegociável do código sagrado de comando Hymmnos da Administradora Shurelia, que estava vazio no arquivo preliminar."
    },
    {
        "id": 12802,
        "scene": "A Filosofia Doméstica da Presidente Ayano",
        "original_jp": "世の中安定が一番!CR無病息災家内安全亭主元気で留守がいい!",
        "original_en": "I wish the world would stabilize! I also want the world to be a happy place, with no diseases or natural disasters!",
        "curated_ptbr": "A estabilidade é o maior tesouro do mundo!\nSaúde de ferro, lar em harmonia e o marido são e longe de casa!",
        "rationale": "Resgate literário do clássico provérbio popular japonês achatado e descaracterizado pela NISA, revelando a alma bem-humorada da executiva."
    },
    {
        "id": 12843,
        "scene": "O Acolhimento Total de Aurica por Lyner",
        "original_jp": "それって、どんなオリカも分け隔て無く大切にするって事なんだ。CR悪魔の君もひっくるめて、俺はオリカを護る。",
        "original_en": "Which means, I have to care for every single piece of her, including her devilish side.",
        "curated_ptbr": "E isso significa acolher cada pedacinho dela sem distinção.\nMesmo com o seu lado demoníaco, eu protegerei a Aurica por inteiro!",
        "rationale": "Momento crucial da jornada heroica: Lyner não tenta extirpar os traumas ou o lado agressivo da amada, mas promete protegê-la por inteiro ('ひっくるめて')."
    }
]

output_data = {
    "block_id": "BLK_EVD_054",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(dialogue_list),
    "id_range": [dialogue_list[0]["id"], dialogue_list[-1]["id"]],
    "dialogues": dialogue_list,
    "curated_lines": dialogue_list,
    "new_terms": new_terms,
    "glossary_updates": glossary_updates,
    "scene_handoff_final": scene_handoff_final,
    "highlights": highlights
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Output successfully written to {output_path} with {len(dialogue_list)} dialogues.")

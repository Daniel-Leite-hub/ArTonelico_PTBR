# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_078."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Trovoada (Canção)": {
        "pt": "Canção Trovoada",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia da Canção / Vermelha",
        "note": "赤魔法【疾風迅雷】 (Akamahō Shippūjinrai / Thunderbolt). Magia Vermelha tecida por Misha no Nível 8 de sua Cosmosfera após superar o colapso e a cisão de personalidades, restaurando um mundo banhado de luz."
    },
    "Paradise Cinna": {
        "pt": "Paradise Cinna",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia da Canção / Azul",
        "note": "青魔法【極楽金丹】 (Aomahō Gokuraku Kintan / Paradise Cinna). Magia Azul tecida por Misha para proteção e cura espiritual após a reintegração de sua psique na Cosmosfera."
    },
    "Yuteroid": {
        "pt": "Espada Yuteroid",
        "gender": "feminino",
        "number": "singular",
        "category": "Equipamento / Espada",
        "note": "ユーテロイド (Yūteroido / Yuteroid). Lâmina ágil de lâmina fina usada pela Presidente Ayano em seus dias de aventureira na juventude, confiada a Lyner como prova de gratidão antes da investida a Nemo."
    },
    "Tokoyo no Kuni": {
        "pt": "Terra da Eternidade",
        "gender": "feminino",
        "number": "singular",
        "category": "Lore / Mitologia de Sol Ciel",
        "note": "常世の国 (Tokoyo no Kuni). O reino ancestral lendário erguido sob a bênção do Trio de Elemia, livre de decadência, cuja visão idealizada inspirou a vocação de Aurica para ingressar na Igreja."
    },
    "Ambivalência e Dissociação": {
        "pt": "Ambivalência e Dissociação",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Psique",
        "note": "アンヴィバレンツ / 解離. Fenômenos psíquicos fundamentais que culminaram na fratura da identidade de Misha no Nível 8 entre o anseio de liberdade e a obrigação do dever como Cantora das Estrelas."
    },
    "Hama (Origem da Ocarina)": {
        "pt": "Hama (Espírito da Ocarina)",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Lore de Vínculo",
        "note": "ハマ (Hama / オカリナ). Revelação de que Hama foi tecida pelo subconsciente de Misha como Guardiã Mental a partir do amor e da dedicação entalhados por Lyner na ocarina que lhe deu de presente de despedida na infância."
    }
}

for term, data in new_terms.items():
    glossary.setdefault("terms", {})[term] = data

glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/275.evd",
    "last_line_id": 17834,
    "resumo_dramatico": (
        "O bloco BLK_EVD_078 consolida três momentos capitais de desenvolvimento dramático, psicológico e político na narrativa de Ar tonelico: "
        "(1) Em Event/659.evd, no clímax do Nível 8 da Cosmosfera de Misha, ocorre a dramática batalha fratricida entre suas duas personas cindidas — "
        "a faceta Shinobi (desejo ardente de liberdade infantil) e a faceta de Armadura (sacerdotisa do dever cósmico de proteção do mundo). Ao tentar intervir "
        "para impedir a autodestruição da mente de Misha, Lyner é alvejado pelo contra-ataque conjunto das duas metades, momento em que Hama se joga heroicamente "
        "como escudo humano para salvá-lo da morte permanente. Antes de desvanecer, Hama revela sua verdadeira natureza: ela é o espírito encarnado da ocarina "
        "que Lyner esculpiu na infância com amor artesanal e deu de presente a Misha antes de sua partida forçada para Em Pheyna, razão pela qual Hama considerava "
        "Lyner seu 'pai'. A perda trágica de Hama quebra as defesas de Misha, desencadeando um colapso completo que reduz a Cosmosfera ao Vazio primordial. "
        "Ao perceber que apenas o amor e as lembranças com Lyner sobreviveram como uma tábua de salvação em meio ao nada, Misha supera sua contradição interna "
        "e unifica suas duas personas em uma única mulher madura. Juntos, decidem não mais viver nas sombras do poço de selamento e convocam o Construtor onírico "
        "para recriar um novo mundo transbordando de luz, tecendo as magias [Canção Trovoada] e [Paradise Cinna], além de desbloquear o vindouro Nível 9 de Cosmosphere. "
        "(2) Em Event/213.evd, nas varandas de Platina, Lyner encontra Aurica imersa em melancolia diante de sua partida de volta ao Mundo Inferior. Confrontada "
        "com seu complexo crônico de inutilidade e estigmatizada como uma Reyvateil Classe D sem parceiro sacerdotal para a missão do Advento do Trio de Elemia, "
        "Aurica relembra a lenda de Tokoyo no Kuni (a terra da eternidade sob o Trio de Elemia) que a inspirou a ingressar na Igreja, contrastando seus sonhos "
        "puros com a desilusão do trabalho doméstico subalterno. Quando Lyner tenta confortá-la e insinua que pode acompanhá-la, Aurica pede que ele não alimente "
        "esperanças impossíveis e despede-se com o coração partido. "
        "(3) Em Event/275.evd, Misha desperta no mundo real já em seu belo corpo adulto restaurado e com a capacidade plena de tecer canções devolvida ao seu coração. "
        "O reencontro é marcado por momentos cômicos de alívio entre Jack (Maninho Harm) e Krusche (que cobram apostas antigas de Combo Dokkoi), contrastados com a "
        "clássica lentidão e insensibilidade romântica de Lyner, que leva um merecido pisão de Misha. Em seguida, a Presidente Ayano de Tenba (antiga aventureira "
        "lendária) presenteia Lyner com sua espada de juventude [Yuteroid], perdoa Misha pela fuga e liberta-a de qualquer vínculo corporativo com palavras afetuosas "
        "de emancipação. Na sequência, a Venerável Tastiella proclama um discurso inflamado aos Cavaleiros de Elemia convocando a reconquista da Terra Santa e do "
        "Altar dos Apóstolos contra os heréticos, enquanto o grupo embarca na nau voadora rumo à Aerocidade Nemo para deter a conspiração de Bourd e o despertar de Mir."
    ),
    "decisoes_terminologicas": {
        "Thunderbolt / Thunderclap": "赤魔法【疾風迅雷】 / [Canção Trovoada] (Magia Vermelha de dano tecida no clímax de reconciliação de Misha)",
        "Paradise Cinna": "青魔法【極楽金丹】 / [Paradise Cinna] (Magia Azul de cura tecida após a catarse da Cosmosfera de Misha)",
        "Yuteroid": "ユーテロイド / [Espada Yuteroid] (lâmina ágil de lâmina fina de Ayano, concedida a Lyner)",
        "Tokoyo no Kuni": "常世の国 / Terra da Eternidade (reino mitológico paradisíaco do Trio de Elemia)",
        "Harm": "アル兄ぃ / Maninho Harm (tratamento carinhoso usado por Misha para se dirigir a Jack Hamilton)",
        "Ambivalence / Dissociation": "アンヴィバレンツ / 解離 (Ambivalência e Dissociação; terminologia psicológica restaurada na cisão de Misha)",
        "Hama Ocarina Origin": "オカリナ (Hama; espírito da ocarina de infância esculpida por Lyner e dada a Misha)",
        "Dokkoi Set": "ドッコイ定食 / Combo Dokkoi (refeição popular canônica de Sol Ciel)",
        "Altar of Apostles": "使徒の祭壇 / Altar dos Apóstolos (santuário sagrado herético a ser reconquistado pelos cavaleiros de Tastiella)"
    },
    "alertas_para_proximo_bloco": (
        "Nos blocos subsequentes (BLK_EVD_079 em diante), atentar para a chegada e confrontos na Aerocidade Nemo, "
        "a invasão do Altar dos Apóstolos liderada por Tastiella e os cavaleiros, o confronto decisivo contra Bourd, "
        "os planos de contenção da ressurreição de Mir e o avanço de Misha rumo ao Nível 9 de Cosmosphere."
    )
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print(f"Glossary successfully updated with {len(new_terms)} terms and scene handoff for BLK_EVD_078.")

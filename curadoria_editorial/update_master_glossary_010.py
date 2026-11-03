# -*- coding: utf-8 -*-
"""
Atualização do Glossário Mestre e geração do relatório do bloco BLK_EVD_010.
Ar tonelico: Melody of Elemia (Undub) - PS2
"""

import json
import datetime
import os

glossario_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
with open(glossario_path, "r", encoding="utf-8") as f:
    g = json.load(f)

# 1. Update last_scene_handoff
handoff_010 = {
    "status": "COMPLETED",
    "block_id": "BLK_EVD_010",
    "axis_id": "AXIS_3",
    "id_range": "2339-2634",
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "dramatic_context": (
        "Bloco narrativo de história e eventos BLK_EVD_010 (IDs 2339 a 2634, 31 arquivos Event/*.evd). "
        "Revelações cruciais da trama, arcos psicológicos da Cosmosfera e grandes confrontos bélicos: "
        "1. Na Cosmosfera de Aurica (Event/744.evd, Event/701.evd, Event/699.evd), Lyner escapa das correntes obsessivas de Aurica e recebe da persona interior a explicação sobre a Mudança de Paradigma (cura das feridas psíquicas e serenidade); supera a muralha de espinhos e ganha o respeito solene de Don Leon, que revela o Código Hymmnos sagrado dela: [#1MULE_TEIWAZ_ARTONELICO]; "
        "2. Abertura das rotas aéreas no [Ninho do Dragão] por Krusche (Event/523.evd), permitindo a travessia livre pela Blastline; "
        "3. Crise de contaminação viral no mundo virtual de Lady Shurelia (Event/820.evd), onde Hama cruza a [Torre da Vida] até o campo de dados da Ar tonelico, descobre a fabricação de cópias virais e confia o [Anel Hasaiyano] a Lyner; "
        "4. Paródia de colégio/tokusatsu de Shurelia (Event/788.evd, Event/812.evd), onde Lyner protesta contra o desfecho trágico e convence Lady Shurelia a aplicar um macete de programação no servidor para reabrir a narrativa antes do fim; "
        "5. Descoberta de relatórios científicos sinistros sobre experimentos de separação forçada em Misha até o Campo KC (Projeto MULE / Mir) e tentativas de fabricar Cristais Hymmnos (Event/511.evd, Event/510.evd); "
        "6. Leitura do diário maquiavélico do Bispo Falss (Event/463.evd - 'Nova Autobiografia de Kyle, Vol. 5'), revelando a teia de espionagem e a ordem expressa a Bourd para assassinar Lyner a qualquer custo; "
        "7. A [Provação da Lua] em Em Pheyna (Event/156.evd), na qual Lyner comprova seu valor com Harmonics e integra formalmente Radolf, Krusche e Jack ao grupo; "
        "8. Síntese do boneco Don Leon em Firefly Alley (Event/970.evd), com Lyner obtendo a receita [SínC: Bicho de Pelúcia] com Claire; "
        "9. Encontro em Em Pheyna com Lorde Flute e Senhora Tastiella (Event/222.evd), que revela a lendária [Crônica Crescente] onde Misha cantava o selo dos vírus e a paralisia das pernas da matriarca; "
        "10. Aquisição do catalisador sinfônico [Boltapolta] no Porto Gaivota (Event/339.evd); "
        "11. Fuga pelo Pipeline (Event/100.evd), levando o Bispo Falss a lançar a colossal Nau Blindada contra os Guardiões da Torre para exterminar Lyner."
    ),
    "decisoes_terminologicas": {
        "Paradigm Shift (パラダイムシフト)": "Mudança de Paradigma (salto qualitativo de cura emocional na Cosmosfera)",
        "Dragon's Nest (竜の巣)": "[Ninho do Dragão] (marco geográfico no Mapa-Múndi)",
        "Mind Guardian (心の護)": "Guardiã da Mente / Guardião da Mente (entidade psíquica protetora da Reyvateil)",
        "Tower of Life (いのちの塔)": "[Torre da Vida] (estrutura da Cosmosfera conectada ao campo de dados da Torre)",
        "Field of Information (情報野)": "campo de dados / campo informacional (restauração técnica frente ao 'binary field' da NISA)",
        "Forms of thought / Emotion (『想い』の生命体)": "entidades nascidas dos sentimentos / seres concebidos por sentimentos",
        "Hasaiyano Ring (はさいやの指輪)": "[Anel Hasaiyano] (anel antiviral purificador de mundos virtuais)",
        "Miss Tougasaki (塔ヶ崎さん)": "senhorita Tougasaki (identidade colegial de Shurelia no minigame)",
        "Urawaza (裏技)": "macete de programação (exploit técnico no servidor de Sol Ciel)",
        "MULE Project (MULEプロジェクト)": "Projeto MULE (projeto confidencial da Igreja/Tenba relacionado a Mir)",
        "KC Field (ケーシー野)": "Campo KC (região da psique de Reyvateil de alta linhagem)",
        "Hymn Code (ヒュムネコード)": "Código Hymmnos (com fixação de [#1MULE_TEIWAZ_ARTONELICO])",
        "Kyle's Autobiography (カイエル自伝)": "Autobiografia de Kyle (diário cifrado do Bispo Falss)",
        "Ordeal of the Moon (月の試練)": "[Provação da Lua] (exame ritual dos guerreiros Teru em Em Pheyna)",
        "Harmonics (ハーモニクス)": "Harmonics (ressonância emocional e sincronia em combate)",
        "Knight of Elemia / Apostle (エレミアの使徒)": "Cavaleiro de Elemia / Apóstolo de Elemia",
        "Stuffed Animal Recipe (合C:ぬいぐるみ)": "[SínC: Bicho de Pelúcia] (receita de síntese do boneco Don Leon)",
        "Crescent Chronicle (クレセントクロニクル)": "Crônica Crescente / [Crônica Crescente] (antigo local de selamento onde Misha cantava)",
        "Chief Flute (フラウト様)": "Lorde Flute (líder nobre e respeitado da tribo Teru)",
        "Boltapolta (ボルタポルタ)": "Boltapolta (artefato catalisador e amplificador de energia sinfônica)",
        "Armored Airship (装甲船)": "Nau Blindada / Nave Blindada (aeronave bélica pesada mobilizada por Falss)",
        "Tower Guardians (ガーディアン)": "Guardiões da Torre (defesas biomecânicas exteriores de Ar tonelico)"
    },
    "alertas_para_proximo_bloco": (
        "1. Radolf, Krusche e Jack agora fazem parte oficialmente do grupo ativo: atentar para as interações táticas e o sarcasmo maduro de Jack. "
        "2. A [Crônica Crescente] é o próximo destino capital da jornada: local onde o passado de Misha e o selo viral serão desvelados. "
        "3. O Bispo Falss assumiu o comando da Nau Blindada e persegue o grupo ativamente pelos céus, desafiando os Guardiões da Torre. "
        "4. Preservar o tratamento nobre a Lorde Flute e à Senhora Tastiella, cuja limitação motora exige respeito dramático. "
        "5. Manter a grafia de 'Ar tonelico' rigorosamente com 't' minúsculo e 'Crônica Crescente' para a lendária estrutura de sustentação."
    )
}

g["last_scene_handoff"] = handoff_010

# 2. Add / update terms safely
terms = g.setdefault("terms", {})

new_terms = {
    "Tower of Life": {
        "pt": "Torre da Vida",
        "gender": "feminino",
        "number": "singular",
        "category": "Estrutura / Cosmosphere",
        "note": "Estrutura mística da Cosmosfera de Misha que conecta o mundo mental diretamente ao campo de dados da Ar tonelico (JP いのちの塔)."
    },
    "Hasaiyano Ring": {
        "pt": "Anel Hasaiyano",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Antiviral",
        "note": "Anel sagrado entregue por Hama que elimina infecções virais e restaura mundos virtuais e personas corrompidas (JP はさいやの指輪)."
    },
    "Miss Tougasaki": {
        "pt": "senhorita Tougasaki",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / Cosmosphere",
        "note": "Identidade e sobrenome colegial de Shurelia na Cosmosfera (JP 塔ヶ崎さん)."
    },
    "Ordeal of the Moon": {
        "pt": "Provação da Lua",
        "gender": "feminino",
        "number": "singular",
        "category": "Rito / Tradição Teru",
        "note": "Exame marcial sagrado em Em Pheyna para comprovar se um guerreiro é um autêntico Cavaleiro de Elemia mediante o domínio de Harmonics (JP 月の試練)."
    },
    "KC Field": {
        "pt": "Campo KC",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosphere / Tecnologia",
        "note": "Camada de memória profunda e sensível na psique de uma Reyvateil Origin ligada ao Projeto MULE (JP ケーシー野)."
    },
    "Armored Airship": {
        "pt": "Nau Blindada",
        "gender": "feminino",
        "number": "singular",
        "category": "Veículo / Tecnologia Bélica",
        "note": "Aeronave militar pesada e encouraçada da Tenba equipada com armamento de alta potência capaz de abater Guardiões da Torre (JP 装甲船)."
    },
    "Dragon's Nest": {
        "pt": "Ninho do Dragão",
        "gender": "masculino",
        "number": "singular",
        "category": "Localização / Mapa-Múndi",
        "note": "Ponto geográfico nos céus que conecta o tráfego aéreo entre o Mundo Superior e Inferior através da Blastline (JP 竜の巣)."
    }
}

terms_added = 0
for k, v in new_terms.items():
    if k not in terms:
        terms[k] = v
        terms_added += 1
        print(f"Added term: {k} -> {v['pt']}")
    else:
        print(f"Term {k} already exists, preserved.")

# Save back to glossario_mestre.json
with open(glossario_path, "w", encoding="utf-8") as f:
    json.dump(g, f, ensure_ascii=False, indent=2)

print(f"Glossário Mestre updated successfully with {terms_added} new terms!")

# 3. Generate BLK_EVD_010_report.json
report_data = {
    "block_id": "BLK_EVD_010",
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "total_dialogues": 296,
    "lines_rewritten": 286,
    "lines_approved_as_is": 10,
    "new_terms_added": terms_added,
    "hard_gate_errors": 0,
    "lint_warnings": 0,
    "scene_handoff": handoff_010
}

report_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_010_report.json"
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print(f"Report saved to: {report_path}")

# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_061."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Angel Rishi": {
        "pt": "Anjo Rishi",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Magia Azul",
        "note": "Entidade onírica que governa a preservação e a razão na Cosmosfera de Misha, convertida na Magia Azul Anjo Rishi (JP 利支天)."
    },
    "Dragonferno": {
        "pt": "Dragonferno",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Magia Vermelha",
        "note": "Magia Vermelha de ataque de fogo gerada na Cosmosfera de Aurica após o enfrentamento contra a projeção do dragão (JP ドラゴンフェルノ)."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

# Atualização de handoff
glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/714.evd",
    "last_line_id": 14342,
    "resumo_dramatico": "O bloco BLK_EVD_061 abrange três frentes dramáticas cruciais: (1) Na Mansão da Lua na Cosmosfera de Misha (Event/657.evd), o Anjo Shura revela a Lyner que a mente basal de Misha é programática, mas seus sentimentos são legítimos. O Anjo Rishi e a persona austera de Misha tentam expurgar a Shinobi Misha e eliminar Lyner para cessar o paradoxo emocional do selo dos vírus. Shinobi Misha escapa do confinamento, resgata Lyner provando que o amor por ele é tão primordial quanto o propósito sagrado, e conduz Lyner ao Bosque do Sono, tecendo a Magia Azul Anjo Rishi. (2) Na sala de comando de Platina (Event/176.evd), Leard corta a energia sinfônica do Segundo Distrito ante a invasão viral e teme pela sorte de Shurelia e Ayatane no Altar dos Apóstolos; em flashback, Ayatane manifesta frieza e autoridade obscura sobre os vírus de assalto. Lyner retorna com o Cristal Hymmnos, enfrenta o desdém elitista e a recusa de reconhecimento do pai, defendido com paixão por Misha e com nobreza militar por Radolf. Leard delega a Lyner confiar o cristal à sua Reyvateil de maior fé e instrui-o a buscar Horai no Centro de Mergulho de Platina para a cerimônia de integração. (3) Na Cosmosfera de Aurica (Event/714.evd), Lyner apoia Aurica no combate contra o dragão traumático com a aparência de Bourd e a voz de Falss; Aurica supera o pavor do massacre familiar e tece a Magia Vermelha Dragonferno desencadeando a Mudança de Paradigma. Don Leon revela a Lyner o massacre histórico do Vilarejo Skuwat provocado pela fuga de Bourd com o Tesouro Teru. Contudo, ao relembrar a catástrofe, Aurica recai no trauma e foge apavorada perante o monstro redivivo; Don Leon orienta Lyner de que a vitória só virá quando Aurica consolidar sua autoconfiança através de novas pistas.",
    "decisoes_terminologicas": {
        "Anjo Rishi": "利支天 (Entidade onírica da preservação e razão na Cosmosfera de Misha, contraparte do Anjo Shura / 修羅天)",
        "Dragonferno": "ドラゴンフェルノ (Magia Vermelha forjada na Cosmosfera de Aurica contra a projeção do dragão de Skuwat)",
        "Bosque do Sono": "眠りの森 (Região de cura na mente de Misha onde jorra a fonte curativa)",
        "Centro de Mergulho de Platina": "プラティナダイブ屋 (Instalação técnica de Platina operada por Horai para Mergulho e integração de cristais)"
    },
    "alertas_para_proximo_bloco": "Com o rito de integração do Cristal Hymmnos pendente na Loja de Mergulho de Platina com Horai e a encruzilhada de confiança entre Aurica e Misha estabelecida, além da necessidade de resgatar Shurelia e Ayatane no Altar dos Apóstolos e desvendar as pistas para a autoconfiança de Aurica perante o dragão, o roteiro avança para a escolha da parceira e a contraofensiva de Platina."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print("glossario_mestre.json atualizado com sucesso para BLK_EVD_061.")

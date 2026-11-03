# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_065."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Ambience Field": {
        "pt": "Campo de Ambiência",
        "gender": "masculino",
        "number": "singular",
        "category": "Combate / Magia da Canção",
        "note": "Campo sônico de ressonância projetado pela Reyvateil sobre os inimigos antes do desencadeamento da Magia da Canção (JP アンビエンスフィールド)."
    },
    "Symphonic Power Line": {
        "pt": "Linha de Condução de Doryoku",
        "gender": "feminino",
        "number": "singular",
        "category": "Tecnologia / Infraestrutura da Torre",
        "note": "Malha condutora de energia sônica e mágica (doryoku) que percorre a superestrutura da Torre e sustenta o funcionamento de Platina (JP 導力ライン)."
    },
    "Sealed Airship": {
        "pt": "Aeronave Selada",
        "gender": "feminino",
        "number": "singular",
        "category": "Veículo / Lore",
        "note": "Veículo voador sagrado e proibido, guardado em Platina atrás de anteparas seladas, concedido por Shurelia a Lyner em estado de emergência para atravessar a Blastline rumo ao Mundo Inferior (JP 封印されし飛空挺)."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/1.evd",
    "last_line_id": 15095,
    "resumo_dramatico": "O bloco BLK_EVD_065 cobre integralmente o Prólogo de abertura cinematográfica e narrativa de Ar tonelico (Event/1.evd): (1) A lenda das Duas Grandes Catástrofes da antiguidade, a criação das formas de vida virais na Torre e o surgimento das Reyvateils e dos Cristais Hymmnos, culminando no selamento do Vírus-Mãe, na consagração dos Apóstolos de Elemia e na fundação da Cidade Celestial de Platina. (2) O despertar da Terceira Crise no Ano 3770 d.C.: um terremoto sem precedentes abala Platina enquanto vírus desconhecidos e intangíveis proliferam no Altar dos Apóstolos. Leard assume o comando e repreende o ímpeto infantil de Lyner. A Senhora Shurelia convoca Lyner como sua escolta direta. (3) No Altar dos Apóstolos, a tentativa de análise via Hymmnos revela que a cepa não possui precedentes. Os vírus entram em estado de desmaterialização energética, tornando os ataques físicos inócuos e repelindo o grupo com ferocidade. Shurelia ordena retirada tática. (4) O choque rompe as linhas de condução de doryoku, paralisando a infraestrutura vital de Platina. Ayatane se sacrifica heroicamente na retaguarda para conter a perseguição viral e permitir a fuga de Lyner e Shurelia. (5) Shurelia revela a Lyner que a única esperança reside no Cristal Hymmnos Purger, localizado no continente flutuante Asas de Hórus, milhares de stons abaixo, no tabu do Mundo Inferior. Em rara explosão emocional e vulnerabilidade, Shurelia concede a lendária Aeronave Selada e o Broche Hymmnos com os diagramas tridimensionais, rogando a Lyner que salve o mundo. Lyner jura solenemente retornar com o cristal purificador enquanto Shurelia projeta o Campo de Ambiência e assume posição de combate para tecer sua Canção e conter a horda.",
    "decisoes_terminologicas": {
        "Ambience Field": "アンビエンスフィールド (Campo de Ambiência)",
        "Symphonic Power Line": "導力ライン (Linha de Condução de Doryoku)",
        "Sealed Airship": "封印されし飛空挺 (Aeronave Selada)",
        "Hymn Brooch": "ヒュムネブローチ (Broche Hymmnos)",
        "Purger": "パージャ (Cristal Hymmnos Purger)"
    },
    "alertas_para_proximo_bloco": "Com Lyner decolando na Aeronave Selada rumo às Asas de Hórus para cruzar a Blastline e Shurelia em vigília de combate em Platina, o prólogo da Primeira Torre é consolidado com êxito."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"Glossário Mestre atualizado com sucesso! Total de termos: {len(glossary['terms'])}")

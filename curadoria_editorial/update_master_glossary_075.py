# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_075."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Songstress and Guardian": {
        "pt": "A Cantora e o Guardião",
        "gender": "feminino / masculino",
        "number": "singular",
        "category": "Lore / Religião de Elemia",
        "note": "謳姫と守護者 (Utahime to Shugosha). Estátua sacra e poema clássico de El Elemia que retrata a devoção sacrificial do guardião em proteger a donzela cantora e o nascimento do vento curador da harmonia."
    },
    "Wind Guard": {
        "pt": "Guarda do Vento",
        "gender": "feminino",
        "number": "singular",
        "category": "Combate / Magia Azul",
        "note": "青魔法【ウインドガード】 (Aomahō: Uindo Gādo). Magia Azul tecida por Aurica no nível onírico de sua Cosmosfera para resguardar Lyner das rajadas mortais do Dragão (padronizado com BLK_EVD_023)."
    },
    "Fortress-Class Guardians": {
        "pt": "Guardiões da Classe Fortaleza",
        "gender": "masculino",
        "number": "plural",
        "category": "Inimigo / Autômatos",
        "note": "要塞クラスのガーディアン (Yōsai-kurasu no gādian). Autômatos sentinelas colossais que patrulham os cais externos da Torre e possuem protocolos de convocação de reforços contínuos."
    },
    "Prism Garden": {
        "pt": "Jardim de Prisma",
        "gender": "masculino",
        "number": "singular",
        "category": "Toponímia / Mundo Superior",
        "note": "プリズムガーデン. Instalação e setor tecnológico de alto nível localizado acima da tempestade da Blastline para onde o Comandante Leard foi transferido após a invasão."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/117.evd",
    "last_line_id": 17205,
    "resumo_dramatico": (
        "O bloco BLK_EVD_075 reúne quatro arcos dramáticos e fundamentais da saga de Sol Ciel: "
        "(1) Em Event/378.evd, logo após o sequestro e o sumiço simultâneo de Shurelia, Ayatane e do Comandante Supremo Leard, "
        "Lyner é tomado por um vazio existencial e desnorteante. Radolf intervém com sabedoria paternal e conduz o jovem diante da "
        "estátua de 'A Cantora e o Guardião' (謳姫と守護者), onde Aurica recita de cor a milenar lenda de Elemia sobre a proteção incondicional "
        "e o vento curador gerado pela mútua confiança. Inspirado pela camaradagem, Lyner decide romper a Blastline para salvar seus entes "
        "queridos, idealizando recuperar e consertar sua aeronave de Platina caída na Floresta de Viola com o suporte técnico de Krusche. "
        "(2) Em Event/713.evd, no mergulho da Cosmosfera de Aurica, revive-se o trauma primal da destruição do Vilarejo de Skuwat pelo Dragão "
        "(personificado na figura odiosa de Bourd e Falss). Lyner finca os pés contra o vendaval e recusa-se a fugir, despertando em Aurica o ímpeto "
        "sagrado de salvá-lo, o que materializa a tecitura da Magia Azul [Guarda do Vento] (青魔法【ウインドガード】). Don Leon explica que a Magia Azul "
        "só floresce pelo desejo altruísta de proteger outrem, e mesmo com a fuga temporária do Dragão e o arremesso de Lyner ao fim do mundo, "
        "Aurica descobre que ao lado dele poderá vencer seus traumas. "
        "(3) Em Event/255.evd, nos meandros internos da Torre Ar tonelico, Misha entra em pânico e quase sucumbe à loucura ao se deparar com uma "
        "antepara selada. Krusche analisa os esquemas e descobre uma colossal linha de doryoku alimentando o local com uma frequência sônica "
        "destrutiva exclusiva para Reyvateils; Lyner e Jack decidem avançar a vanguarda e investigar o mistério a portas fechadas, poupando Misha em repouso. "
        "(4) Em Event/117.evd, nas imediações do Cais Flutuante (滞空岸壁), Lyner e Misha socorrem Radolf em combate contra guardiões da Classe Fortaleza. "
        "Radolf oferece carona na nau eclesiástica de regresso a Nemo, enquanto Krusche revela ser uma talentosa Grathmelder especializada em aeronaves "
        "com três veículos já construídos. Impressionado, Lyner propõe a reforma de sua nave de Platina acidentada; Krusche aceita o desafio "
        "com pragmatismo comercial, marcando reencontro no Aeroporto de Nemo."
    ),
    "decisoes_terminologicas": {
        "Songstress and Guardian": "謳姫と守護者 (A Cantora e o Guardião / Donzela da Canção e Guardião; estátua e poema sagrado)",
        "Wind Guard": "青魔法【ウインドガード】 / [Guarda do Vento] (Magia Azul tecida por Aurica)",
        "Fire Guard": "青魔法【ファイアーガード】 / Guarda de Fogo (Magia Azul defensiva prévia)",
        "Prism Garden": "プリズムガーデン (Jardim de Prisma / setor superior onde Leard é mantido)",
        "Fortress-Class Guardians": "要塞クラスのガーディアン (Guardiões da Classe Fortaleza)",
        "Symphonic Power Line": "導力ライン (Linha condutora de doryoku / linha de condução de energia sinfônica)",
        "Melder": "メルク (Grathmelder / artesã de síntese especializada em aeronaves)",
        "Viola Forest": "ヴィオラの森 (Floresta de Viola / local da queda da aeronave de Platina)"
    },
    "alertas_para_proximo_bloco": (
        "Nos blocos seguintes (BLK_EVD_076 em diante), manter a simetria terminológica quanto à engenharia de aeronaves de Krusche, "
        "as etapas do conserto na Floresta de Viola, a audiência com o Bispo Falss na Catedral de Nemo e a exploração de setores profundos da Torre."
    )
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"Glossário Mestre atualizado com sucesso! Total de termos: {len(glossary['terms'])}")

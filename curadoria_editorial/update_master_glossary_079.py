# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_079."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Guarda Gelo": {
        "pt": "Guarda Gelo",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia da Canção / Azul",
        "note": "青魔法【氷護】 (Aomahō Hyōgo / Ice Guardian). Magia Azul tecida por Misha no Nível 3 de sua Cosmosfera para aquecer e proteger Aurica do frio intenso da nevasca onírica."
    },
    "Yakuan (Eremita)": {
        "pt": "Yakuan",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Personagem Lendário",
        "note": "薬庵 (Yakuan). Sábio eremita recluso nas montanhas da Cosmosfera de Misha, possuidor do elixir supremo capaz de curar qualquer mal e realizar o anseio de humanidade da Fada da Canção."
    },
    "Fada da Canção": {
        "pt": "Fada da Canção",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Conceito Psicológico",
        "note": "詩の精 (Uta no Sei / Song Fairy). Personificação onírica assumida por Misha no Nível 3, simbolizando sua alienação e o trauma de ser tratada como mera máquina utilitária destinada a se sacrificar pelas vontades humanas."
    }
}

for term, data in new_terms.items():
    glossary.setdefault("terms", {})[term] = data

glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/116.evd",
    "last_line_id": 18019,
    "resumo_dramatico": (
        "O bloco BLK_EVD_079 abrange quatro momentos capitais da trama de Ar tonelico: "
        "(1) Em Event/147.evd, nas instalações secretas de experimentos em Reyvateils da Tenba na Placa Hexagonal, "
        "Radolf e Bourd quase duelam até a morte antes da intervenção solene da Presidente Ayano Raizer Elduke, "
        "que decreta trégua mútua diante da tragédia comum da queda. Jack Hamilton reencontra sua antiga protegida "
        "Misha e revela a verdade estarrecedora: Misha tem 18 anos, mas seu corpo não envelheceu um único dia "
        "nos últimos seis anos. Diante da ameaça crescente dos vírus e do descontrole da Torre, Lyner decide subir "
        "imediatamente com o cristal Purger para Platina, despedindo-se da Igreja de Elemia. "
        "(2) Em Event/603.evd, no Nível 3 da Cosmosfera de Misha, Lyner explora uma cidade onírica sob a neve onde "
        "Misha encarna a 'Fada da Canção', tecendo a Magia Azul [Guarda Gelo] para aquecer Aurica. Misha expressa sua "
        "dor e trauma por ser tratada como mera máquina utilitária para servir humanos e suplica a ajuda de Lyner "
        "para tornar-se humana através do remédio do eremita Yakuan das montanhas. "
        "(3) Em Event/228.evd, no altar da Crônica Crescente, Tastiella revela sua verdadeira natureza como a alma fundida "
        "ao colossal mecanismo de contenção e narra a Grande Guerra onde Mir derrubou metade do Continente Flutuante. "
        "Misha revela ser a 31ª da Linhagem Lünn (Misha Arsellec Lünn) encarregada de cantar perpetuamente o Chronicle Key "
        "como vacina. Misha confessa seu pavor de crescer e voltar ao corpo adulto para não herdar o fardo eterno de "
        "confinamento. O grupo conecta os delírios de Bourd à reativação de Mir pela Tenba e parte rumo ao Beco Vagalume. "
        "(4) Em Event/116.evd, o grupo chega ao Cais Flutuante, onde uma aeronave dos Cavaleiros de Elemia é emboscada "
        "por Guardiões voadores da Torre. Radolf reencontra Lyner, Misha oferece suporte com sua Magia da Canção e Radolf "
        "junta-se oficialmente ao grupo em combate."
    ),
    "decisoes_terminologicas": {
        "Crônica Crescente": "クレセントクロニクル / Crescent Chronicle (altar sagrado e relíquia ancestral de selamento de Mir)",
        "Chave da Crônica": "クロニクルキー / Chronicle Key (Cristal Hymmnos que serve de canção-vacina para o selamento)",
        "Guarda Gelo": "青魔法【氷護】 / Magia Azul Guarda Gelo (Magia Azul tecida no Nível 3 da Cosmosfera de Misha)",
        "Yakuan": "薬庵 / Yakuan (eremita lendário das montanhas possuidor do elixir supremo)",
        "Presidente Ayano": "亜耶乃・ライザー・エルデューク / Presidente Ayano Raizer Elduke (líder máxima do Conglomerado Tenba)",
        "Maninho Harm": "アル兄ぃ / Maninho Harm (tratamento carinhoso de Misha para Jack Hamilton)",
        "Linhagem Lünn": "リューンの系譜 / Linhagem Lünn (linhagem sagrada das 31 sacerdotisas do selamento)",
        "Misha Arsellec Lünn": "彌紗・アルトセルク・リューン / Misha Arsellec Lünn (verdadeiro nome canônico de Misha)",
        "Cais Flutuante": "滞空岸壁 / Floating Wharf (doca e porto de aeronaves em Sol Ciel)",
        "Vírus-Mãe": "母なるウイルス体「ミュール」 / Mother Virus Mir (forma primordial e desincorporada de Mir)"
    },
    "alertas_para_proximo_bloco": (
        "Para os blocos seguintes (BLK_EVD_080 em diante), atentar para as investigações e confrontos no Beco Vagalume (Firefly Alley), "
        "a busca pelo Cristal Hymmnos Chronicle Key e o desenvolvimento das tensões entre Tenba, Igreja e a libertação de Mir."
    )
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print(f"Glossary successfully updated with {len(new_terms)} terms and scene handoff for BLK_EVD_079.")

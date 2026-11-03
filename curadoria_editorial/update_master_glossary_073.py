# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_073."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Guide of the Flow": {
        "pt": "Guia do Fluxo",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / Cosmosphere",
        "note": "ナガレの水先案内人 (Nagare no Mizusaki Annai-nin). Figura mascarada misteriosa vestindo túnica ornada de olhos que atua como guia mental na Cosmosfera de Aurica."
    },
    "Potential Development Method": {
        "pt": "Método de Desenvolvimento do Potencial Oculto",
        "gender": "masculino",
        "number": "singular",
        "category": "Lore / Cosmosphere",
        "note": "「潜在能力開発法~3分で修得できる秘術~」. Livro satírico encontrado na mansão da Cosmosfera de Aurica prometendo sabedoria e notas máximas mediante roubo de energia da Torre."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/145.evd",
    "last_line_id": 16766,
    "resumo_dramatico": "O bloco BLK_EVD_073 articula três passagens dramáticas de altíssimo impacto narrativo e revelações canônicas capitais: (1) Em Event/232.evd, no parque urbano de Karff durante um intervalo da tempestade, Misha percebe o estresse e a afobação de Lyner em querer resgatar Claire e chegar ao Beco Vagalume. Com carinho e cumplicidade de infância, Misha o convence a arejar a cabeça e ir às compras para relaxar, antes que o esgotamento o faça perder o controle; Jack intervém ironizando a despreocupação dos dois ('Harm-da!') e parte sozinho para colher informações. (2) Em Event/730.evd, na mansão onírica da Cosmosfera de Aurica, a garota busca desesperadamente o livro 'Método de Desenvolvimento do Potencial Oculto' para ficar inteligente e não ser descartada. O misterioso 'Guia do Fluxo' surge e adverte que sugar energia da Torre é prejudicial, orientando-a a derrotar o gato parasita diante da Torre — um constructo mental imposto por ela mesma. Ao tentar reler o livro, Lyner é impedido pela rejeição inconsciente de Aurica, que tem um colapso de raiva, o acusa de falso e o abandona na escuridão sob o olhar cínico de Don Leon. (3) Em Event/145.evd, Aurica e Lyner conversam ao entardecer; tomada por complexo de inferioridade perante Claire e estigmatizada como Reyvateil Classe D, Aurica revela que sua única alegria fora ser convocada pelo Bispo Falss para a missão na Colina do Canto, momento em que Lyner a reafirma como indispensável e relembra como ela salvou sua vida no desabamento. Subitamente, a cena corta para o santuário do Altar dos Apóstolos em Platina: o enxame viral rompe as defesas e a voz espectral de Mir manifesta-se através de uma barreira tóxica. Mir proclama seu ódio à humanidade ('o verdadeiro vírus') e purga violentamente o Corredor Musical (彩音回廊), provocando abalos sísmicos que ecoam até o Mundo Inferior e deixam o clima global em colapso. Nos escombros sagrados, Ayatane contempla a Senhora Shurelia desacordada e faz um juramento ambíguo de proteção como Cavaleiro de Elemia... e por sua 'Mãe' (Mir), revelando sua condição de vírus infiltrado. Na taverna de Karff, Krusche noticia que destroços da Torre caíram sobre um complexo da Tenba onde estavam reunidos Bourd e Ayano; temendo pela vida de Misha mantida cativa, Lyner mobiliza o grupo, momento em que Jack perde o controle e revela que Misha é a única razão de sua viagem. O acesso à Placa Hexagonal é desbloqueado no Mapa-Múndi.",
    "decisoes_terminologicas": {
        "Musical Corridor": "彩音回廊 (Corredor Musical / complexo de regulação climática purgado por Mir)",
        "Hexagonal Plate": "六角板 (Placa Hexagonal / setor suspenso da Torre derrubado sobre as instalações da Tenba)",
        "Altar of Apostles": "使徒の祭壇 (Altar dos Apóstolos / santuário sagrado de Platina corrompido por Mir)",
        "Guide of the Flow": "ナガレの水先案内人 (Guia do Fluxo / entidade tutelar onírica da Cosmosfera de Aurica)",
        "Singing Hill": "謳う丘 (Colina do Canto / sítio ancestral onde repousavam os cristais)",
        "Potential Development Method": "「潜在能力開発法~3分で修得できる秘術~」 (Método de Desenvolvimento do Potencial Oculto / livro onírico)",
        "Mother": "『母さん』 (Mãe / título filial com que Ayatane se refere a Mir)",
        "Harm-da": "アル兄ぃ (Harm-da / diminutivo carinhoso infantil de Misha para Jack)"
    },
    "alertas_para_proximo_bloco": "Nos blocos subsequentes (BLK_EVD_074 em diante), acompanhar o avanço urgente do grupo rumo à Placa Hexagonal para resgatar Misha dos escombros da Tenba, a tensão crescente sobre o passado Teru de Jack e os desdobramentos da sabotagem de Mir e da infiltração de Ayatane após o colapso climático do Corredor Musical."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"Glossário Mestre atualizado com sucesso! Total de termos: {len(glossary['terms'])}")

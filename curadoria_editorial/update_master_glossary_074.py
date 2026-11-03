# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_074."""

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
        "note": "Campo sônico de ressonância projetado pela Reyvateil sobre os inimigos antes do desencadeamento da Magia da Canção (JP アンビエンスフィールド). Eleva o dano mágico à medida que os aliados de vanguarda atacam o alvo."
    },
    "Star Singer": {
        "pt": "Cantora das Estrelas",
        "gender": "feminino",
        "number": "singular",
        "category": "Título / Sacerdócio",
        "note": "星詠 (Hoshiyomi). Título cerimonial e sagrado da Reyvateil Origin que governa o Silvaplate e tem o fardo sacrificial supremo de manter o vírus Mir selado na Crônica Crescente entoando canções ininterruptas."
    },
    "Inferia": {
        "pt": "Inferia",
        "gender": "feminino",
        "number": "singular",
        "category": "Toponímia / Região",
        "note": "インフェリア. Região continental do Mundo Inferior sob o Mar da Morte em Sol Ciel; corrige a tradução errônea da NISA ('Inferior')."
    },
    "Frozen Eye": {
        "pt": "Olho Congelado",
        "gender": "masculino",
        "number": "singular",
        "category": "Toponímia / Estrutura da Torre",
        "note": "氷の瞳. Gigantesco portão e conjunto de semicondutores (Elemento Ardel) no centro da Torre Ar tonelico que impede o refluxo de energia sinfônica e divide os Mundos Superior e Inferior."
    },
    "Floating Wharf": {
        "pt": "Cais Flutuante",
        "gender": "masculino",
        "number": "singular",
        "category": "Toponímia / Instalação",
        "note": "滞空岸壁. Grande atracadouro suspenso construído sobre a parede externa da Torre de onde partem naves e dirigíveis."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/428.evd",
    "last_line_id": 17016,
    "resumo_dramatico": "O bloco BLK_EVD_074 articula quatro cenas capitais da narrativa e da jornada de Sol Ciel: (1) Em Event/30.evd, nas imediações florestais de um vilarejo, Lyner encontra Jack Hamilton estirado no chão, à beira da morte não por ferimentos, mas por inanição absoluta após torrar todo o dinheiro em compras secretas. Lyner o resgata e o leva à taverna suspensa no topo da coluna, bancando cinco porções inteiras de comida para o mercenário sob os protestos do velho avô e os olhares atônitos da atendente. Após Jack constatar o sumiço de sua preciosa encomenda (furtada por feras azuis imunes a armas comuns), ele convoca Lyner para ajudá-lo na busca, unindo-se oficialmente ao grupo. (2) Em Event/289.evd, na câmara do Plugue Sinfônico da Crônica Crescente, Bourd encurrala Tastiella e tenta apressar o Advento de Mir. Lyner e Misha intervêm; em sua forma adulta desperta, Misha canta para restaurar o selo sagrado enquanto Lyner derrota Bourd em um embate de pura obstinação. Mir é resselada com sucesso, mas o custo emocional é avassalador: Misha deve permanecer em canto ininterrupto no casulo eterno. Lyner jura visitá-la e contar-lhe sobre o mundo lá fora, enquanto o grupo retorna melancólico a Platina com novos setores desbloqueados no Mapa-Múndi (Placa Íon, Inferia, Olho Congelado, Altar dos Apóstolos, Platina) sob o olhar atônito de Ayatane. (3) Em Event/102.evd, na perigosa muralha externa da Torre rumo ao Cais Flutuante, Lyner e Misha socorrem Krusche Elendiek, encurralada por um guardião mecânico regenerativo enquanto buscava por seu irmão desaparecido, Luke. Com atitude tsundere e arrogante, Krusche revela estar a pé por causa da suspensão dos voos no Beco Vagalume após invadir setores restritos da Tenba para furtar peças aeronáuticas. Ela aceita a escolta de Lyner (despertando o ciúme cômico de Misha), junta-se à equipe e o grupo aprende na prática o funcionamento do Campo de Ambiência (アンビエンスフィールド), sincronizando ataques físicos para multiplicar o poder da Magia da Canção até o limiar crítico. (4) Em Event/428.evd, vive-se o grande epílogo e desfecho da saga de Sol Ciel: após a derrota definitiva de Mir e o fim da missão, Radolf e Aurica preparam o retorno a Nemo com a Igreja; Jack parte em busca de aventuras e mulheres; e Krusche retorna à sua oficina no Beco Vagalume para construir sua própria aeronave. Leard surpreende Lyner ao nomear Misha como a nova bibliotecária da Catedral de Platina, dispensando-a do sacerdócio perpétuo e devolvendo-lhe sua cidade natal. Meses depois, em um dia de folga dos Cavaleiros, Misha arrasta Lyner pelas lojas de departamentos de Platina em um 'encontro' romântico e comovente, confessando que após doze anos de reclusão em uma cela escura cantando sem parar, foi ele quem libertou o pássaro da gaiola e curou suas dores — exigindo com carinho que ele permaneça ao seu lado por toda a vida para recuperar cada instante perdido.",
    "decisoes_terminologicas": {
        "Ambience Field": "アンビエンスフィールド (Campo de Ambiência / mecânica harmônica de batalha)",
        "Star Singer": "星詠 (Cantora das Estrelas / título cerimonial de Misha na Crônica Crescente)",
        "Symphonic Plug": "導力プラグ (Plugue Sinfônico / Plugue de Condução energética de contenção de Mir)",
        "Inferia": "インフェリア (Inferia / continente do Mundo Inferior; corrige erro da NISA 'Inferior')",
        "Frozen Eye": "氷の瞳 (Olho Congelado / gigantesco portão semicondutor central da Torre)",
        "Floating Wharf": "滞空岸壁 (Cais Flutuante / atracadouro de aeronaves no paredão externo)",
        "Blue Beasts": "青い獣 (feras azuis / monstros imunes a armas normais que roubaram Jack)",
        "Ion Plate": "イオンプレート (Placa Íon / setor intermediário envolto em nuvens)"
    },
    "alertas_para_proximo_bloco": "Nos blocos posteriores (BLK_EVD_075 em diante), atentar para as consequências da consolidação da paz no Mundo Inferior e Superior, o desenvolvimento dos laços com Misha e Aurica nas rotas de Cosmosphere e eventos adicionais de final de jogo e sidequests de Sol Ciel."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"Glossário Mestre atualizado com sucesso! Total de termos: {len(glossary['terms'])}")

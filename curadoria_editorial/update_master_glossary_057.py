# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_057."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

# Novos termos do bloco
new_terms = {
    "Three Magi": {
        "pt": "Três Sábios",
        "gender": "masculino",
        "number": "plural",
        "category": "Lore / Platina",
        "note": "3賢者 (Sankenja). Antigo triunvirato governamental e científico supremo de Platina formado por Shurelia, Kyle Clancy e Leard Barsett (ID 13435; corrigindo a conotação de magos de Three Magi na NISA)."
    },
    "Três Sábios": {
        "pt": "Três Sábios",
        "gender": "masculino",
        "number": "plural",
        "category": "Lore / Platina",
        "note": "3賢者 (Sankenja). O triunvirato de fundação e liderança de Platina (Shurelia, Kyle e Leard) responsável pela manutenção da Primeira Torre."
    },
    "RE Nation": {
        "pt": "RE Nation",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Hymmnos",
        "note": "リ・ネイション / EXEC_RE-NATION/.. Cristal Hymmnos ancestral primordial capaz de reiniciar os sistemas vitais da Primeira Torre e despertar Shurelia da suspensão criogênica (ID 13443)."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

# Atualização de nuances de personagens
if "characters" in glossary:
    if "Leard" in glossary["characters"]:
        glossary["characters"]["Leard"]["address_matrix"]["Kyle Clancy (Passado)"] = "Dor fraternal pela traição do antigo melhor amigo de infância e ex-membro dos Três Sábios que quebrou o Juramento de Elemia."
        glossary["characters"]["Leard"]["address_matrix"]["Aurica (Reparação)"] = "Nobreza e humildade patriarcal ao pedir desculpas formais pelo sofrimento que a negligência de Platina causou à jovem."
    if "Don_Leon" in glossary["characters"]:
        glossary["characters"]["Don_Leon"]["address_matrix"]["Aurica (Independência)"] = "Recusa samurai em respaldar a autocomiseração e infantilização da mestra: exige que ela cresça e lute pela própria felicidade."

# Atualização de handoff
glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/444.evd",
    "last_line_id": 13497,
    "resumo_dramatico": "O bloco BLK_EVD_057 consolida arcos capitais de desenvolvimento emocional, revelações de lore ancestral e a grande virada de transição para a Fase 2 do roteiro: (1) Na cozinha de Claire em Nemo (Event/297.evd), Aurica protagoniza um interlúdio hilário e caloroso ao insistir em cozinhar para Lyner como agradecimento pelo seu esforço contínuo; apesar da técnica desastrada que quase decepa seus dedos e aterroriza Claire e Radolf com ingredientes atirados a esmo, a refeição resulta em uma alquimia caótica e viciante que Lyner devora no desespero e Radolf qualifica como 'sorte de outro mundo'. (2) No teste espiritual de Silvaplate (Event/542.evd), Hama confronta Lyner sobre a causa seminal de todos os conflitos humanos; perante a firmeza do cavaleiro em lutar pelo mundo, a guardiã se desfaz revelando-se como a sacerdotisa ancestral Tastiella, que profere seu conselho derradeiro sob o pranto dilacerado de Shurelia. No ramo hesitante, Hama repreende Lyner com severidade cirúrgica, denunciando que fugir do confronto não é bondade, mas fraqueza de convicção. (3) Na Cosmosfera de Aurica (Event/739.evd), Claire revela que o samurai Don Leon nasceu de uma pelúcia dada à heroína na infância em Skuwat para aplacar sua solidão; em um confronto dramático entre a projeção infantil de Aurica e a defensora onírica, desvenda-se o trauma central da garota: o medo de crescer e curar suas feridas, temendo que Don Leon deixe de existir se ela não for eternamente indefesa. O próprio Don Leon manifesta-se em sua glória samurai, recusando-se a respaldar a infantilização e partindo em protesto ético para ensinar à mestra a verdadeira coragem. (4) Nos subterrâneos tecnológicos de Platina (Event/444.evd), o Governador Leard revela a Lyner e Aurica a história esquecida dos 'Três Sábios' (Shurelia, Leard e Kyle Clancy); Leard expõe a dor de ver seu melhor amigo de infância corromper-se em arrogância científica contra o Juramento de Elemia, aliando-se a Mir e forjando seu falso suicídio para renascer no Mundo Inferior como o Bispo Falss. Com a Torre silenciada pelo Cântico Suspend para conter a proliferação viral, a única salvação reside no Cristal Hymmnos 'RE Nation', ocultado por Kyle no Mundo Inferior. Leard pede desculpas a Aurica pelo sofrimento infligido pela Igreja, e a jovem heroína o perdoa com serenidade lírica ao reconhecer que, sem aquela dor, jamais teria encontrado Lyner. Sentindo a Magia da Canção adormecer em suas veias com a suspensão da Torre, Aurica confessa seu desamparo, mas é reconfortada pelo juramento incondicional de proteção de Lyner, liberando a partida da comitiva para o Mapa-Múndi.",
    "decisoes_terminologicas": {
        "Três Sábios": "3賢者 (triunvirato histórico de Platina formado por Shurelia, Leard e Kyle; expurga a conotação mágica de Three Magi)",
        "RE Nation": "リ・ネイション (Cristal Hymmnos ancestral vital para reativar a Torre e acordar Shurelia)",
        "Suspend": "サスペンド (Cântico mestre de congelamento criogênico de sistema entoado por Shurelia)",
        "Juramento de Elemia": "エレミア誓約書 (tratado ancestral de segurança tecnológica que baniu experimentos com Mir)",
        "Comandante-Geral Radolf": "ラードルフ総司 (título canônico de Radolf perante a hierarquia militar dos Cavaleiros)",
        "Don Leon": "どんすけ (a pelúcia da infância de Aurica que se converteu em guardião samurai onírico)",
        "Mapa-Múndi": "ワールドマップ (área de navegação global desbloqueada após o diálogo com Leard)"
    },
    "alertas_para_proximo_bloco": "Com a Torre em suspensão de sistema, a Magia da Canção enfraquecida e o Mapa-Múndi liberado, a expedição parte para o Mundo Inferior em busca dos aliados dispersos (Radolf em Nemo, Krusche no Beco Vagalume, Jack e Misha rumo a Em Pheyna) para rastrear o Cristal Hymmnos RE Nation deixado por Kyle Clancy."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"[SUCESSO] Glossário mestre atualizado em {GLOSSARY_PATH}")

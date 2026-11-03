# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_083."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Febre de Tatoolist": {
        "pt": "Febre de Tatoolist",
        "gender": "feminino",
        "number": "singular",
        "category": "Doença / Fisiologia Reyvateil",
        "note": "タトゥリスタ病 (Taturista-byō / Tatoolist Disease). Síndrome febril crítica e letal decorrente da escassez severa do Agente Prolongador de Vida (延命剤) no organismo de Reyvateils da Terceira Geração."
    },
    "Espírito do gelo": {
        "pt": "Espírito do gelo",
        "gender": "masculino",
        "number": "singular",
        "category": "Entidade Cósmica / Cosmosfera",
        "note": "氷の精 (Kōri no sei / Ice Fairy). Criatura elemental que habita as alturas do Monte das Geadas na Cosmosfera de Misha, responsável por soprar a neve regeneradora sobre as cidades imersas em trevas."
    },
    "Monte das Geadas": {
        "pt": "Monte das Geadas",
        "gender": "masculino",
        "number": "singular",
        "category": "Cenário / Cosmosfera",
        "note": "樹氷山 (Juhyōzan / Mount Frost). Montanha gélida na Cosmosfera de Misha onde residem os espíritos do gelo e de onde descendem os ventos invernais."
    },
    "Silfa": {
        "pt": "Silfa",
        "gender": "feminino",
        "number": "singular",
        "category": "Arquétipo / Cosmosfera",
        "note": "シルフ (Shirufu / Sylph). Personificação arquetípica da liberdade e da autossuficiência no Nível 8 da Cosmosfera de Aurica, que rouba o vestido nupcial para confrontar a donzela sobre o medo do compromisso amoroso."
    },
    "Dança da Silfa": {
        "pt": "Dança da Silfa",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia Vermelha / Canção",
        "note": "赤魔法【シルフのダンス】 (Sylphan Dance). Magia de ataque tecida por Aurica no Nível 8 de sua Cosmosfera após superar o dilema de entrega emocional perante a Silfa."
    }
}

for term, data in new_terms.items():
    glossary.setdefault("terms", {})[term] = data

glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/766.evd",
    "last_line_id": 18912,
    "resumo_dramatico": (
        "O bloco BLK_EVD_083 abrange quatro sequências cruciais de conflito fisiológico, exploração psíquica e provação amorosa: "
        "(1) Em Event/323.evd, logo após o resgate de Misha e a despedida da equipe de Jack, Aurica sofre um colapso repentino de febre alta. "
        "Claire intervém em prantos e desculpa-se por suas palavras duras anteriores, diagnosticando que Aurica foi acometida pela temida "
        "febre de Tatoolist (タトゥリスタ病) — a pane fisiológica mortal que assola Reyvateils da Terceira Geração privadas de seu agente prolongador de vida (延命剤). "
        "Radolf e Claire deduzem que o organismo dela está consumindo o composto em ritmo anormalmente acelerado, e Shurelia instrui Lyner a mergulhar "
        "urgentemente na Cosmosfera de Aurica pelo Centro de Mergulho para salvar sua vida. "
        "(2) Em Event/598.evd, no interior da Cosmosfera de Misha imersa em trevas sufocantes, Lyner e Misha encontram um pequeno espírito do gelo (氷の精) "
        "que derreteu por ter se perdido na escuridão rumo ao Monte das Geadas (樹氷山). Misha relembra com saudade nostálgica as neves de outrora que clareavam o mundo. "
        "Na ramificação de sucesso, estimulada pela confiança inabalável de Lyner e pelos ensinamentos do Nível 1, Misha dialoga com seu mundo e tece a Magia Verde [Análise] (緑魔法【アナライザ】), "
        "desvendando a rota até o topo da montanha. Na ramificação de falha, Misha desiste consumida pelo medo do breu, o espírito se dissolve e Lyner é expulso da Cosmosfera pela Moradora do Mundo Inferior. "
        "(3) Em Event/953.evd, os atendentes do Centro de Mergulho e o Operador de Portão revelam com espanto que Lyner e Aurica alcançaram profundidades incomuns na Cosmosfera sem terem realizado a Instalação (インストール). "
        "Aurica cora intensamente confessando que nunca passou por isso e não sabia como propor o rito. O atendente explica a gravidade física da técnica: a inserção direta de Cristais Grathnode na carne da Reyvateil amplia a força da Magia da Canção, mas atua como veneno tóxico ao organismo da donzela. Lyner, estarrecido, recusa-se a machucá-la, e o atendente sugere que o casal vá a uma pousada conversar a sós e decidir com o coração. "
        "(4) Em Event/766.evd, no Nível 8 da Cosmosfera de Aurica, o casal confronta a Silfa (シルフ), espírito livre que roubou o vestido cerimonial nupcial para impedir o enlace matrimonial com Lyner, "
        "alertando Aurica sobre a renúncia da solidão autossuficiente e a perda da liberdade individual. Na ramificação vitoriosa, Aurica amadurece e declara com nobreza que o amor compartilhado expande a vida em vez de aprisioná-la; "
        "a Silfa devolve o vestido abençoando o casal, Aurica veste o traje para deslumbre de Lyner, convida-o para a cerimônia na Catedral e tece a Magia Vermelha [Dança da Silfa] (赤魔法【シルフのダンス】). "
        "Na ramificação de recusa, Aurica recua atemorizada pelo compromisso e a Silfa despacha o vestido e Lyner com um golpe tempestuoso pelos ares."
    ),
    "decisoes_terminologicas": {
        "Febre de Tatoolist": "タトゥリスタ病 / Tatoolist Disease",
        "Agente prolongador de vida": "延命剤 / Life Extending Agent (DDP)",
        "Espírito do gelo": "氷の精 / Ice Fairy",
        "Monte das Geadas": "樹氷山 / Mount Frost",
        "Magia Verde [Análise]": "緑魔法【アナライザ】 / Green Magic [Analyzer]",
        "Instalação": "インストール / Install",
        "Cristal Grathnode": "グラスノ結晶 / Grathnode Crystal",
        "Silfa": "シルフ / Sylph",
        "Dança da Silfa": "赤魔法【シルフのダンス】 / Red Magic [Sylph's Dance]",
        "Catedral": "正教会 / Cathedral"
    },
    "alertas_para_proximo_bloco": "Para os blocos seguintes (BLK_EVD_084 em diante), manter a continuidade das ramificações de eventos e finais, a estabilidade das Cosmosferas de Aurica e Misha no pós-jogo ou eventos paralelos, e a preservação rigorosa da Tríade de Idiomas e paridade técnica."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print("Glossario mestre atualizado com sucesso com os termos de BLK_EVD_083!")

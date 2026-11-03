# -*- coding: utf-8 -*-
"""
update_master_glossary_084.py - Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_084.
"""
import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Provação da Lua": {
        "pt": "Provação da Lua",
        "gender": "feminino",
        "number": "singular",
        "category": "Rito / Tradição Teru",
        "note": "月の試練 (Tsuki no Shiren / Ordeal of the Moon). Exame sagrado em Em Pheyna para comprovar se um guerreiro é um autêntico Cavaleiro de Elemia mediante o domínio de Harmonics."
    },
    "Harmonica": {
        "pt": "Harmonica",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / Lore Teru",
        "note": "アルモニカ (Harmonica). Nome ancestral de batismo de Jack Hamilton entre o povo Teru de Em Pheyna, evocado por Flute e Tastiella."
    },
    "Ponto de Instalação": {
        "pt": "Ponto de Instalação",
        "gender": "masculino",
        "number": "singular",
        "category": "Fisiologia Reyvateil / Mecânica",
        "note": "インストールポイント (Install Point). Região dérmica especializada no corpo da Reyvateil onde os Cristais Grathnode são absorvidos e fundidos à carne."
    },
    "Canção +10%": {
        "pt": "Canção +10%",
        "gender": "masculino",
        "number": "singular",
        "category": "Cristal Grathnode / Efeito",
        "note": "詩1割増サービス (Uta Ichiwarimashi Sābisu / 10% Song Increase). Cristal Grathnode introdutório que amplia o efeito base de Magias da Canção em 10% com desgaste físico mínimo."
    },
    "Cristal Hymmnos Linker": {
        "pt": "Cristal Hymmnos Linker",
        "gender": "masculino",
        "number": "singular",
        "category": "Item Sagrado / Lore",
        "note": "ヒュムネクリスタル「リンカ」 (Hymn Crystal Linker). Relíquia ancestral da Deusa Tyria guardada no Ninho dos Dragões e concedida a Aurica para entoar EXEC_LINKER/."
    },
    "Garzburn": {
        "pt": "Garzburn",
        "gender": "masculino",
        "number": "singular",
        "category": "NPC / Dragão Ancião",
        "note": "ガルツベルン (Garzburn). Senhor ancestral do Ninho dos Dragões e guardião de relíquias da civilização antiga em sua Loja de Antiguidades."
    },
    "Loja de Antiguidades": {
        "pt": "Loja de Antiguidades",
        "gender": "feminino",
        "number": "singular",
        "category": "Comércio / Instalação",
        "note": "古代屋 (Kodaiya / Antique Shop). Estabelecimento comercial gerido por Garzburn no Ninho dos Dragões que vende artefatos e ferramentas raras de civilizações antigas."
    },
    "Magia Azul Booster": {
        "pt": "Magia Azul Booster",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia da Canção / Cosmosfera",
        "note": "青魔法【ブースター】 (Blue Magic Booster). Magia de suporte forjada por Aurica na superação de seus sentimentos de inferioridade e inveja, multiplicando a potência interna das canções."
    }
}

for term, data in new_terms.items():
    glossary.setdefault("terms", {})[term] = data

handoff_history = glossary.setdefault("metadata", {}).setdefault("handoff_history", [])
if "last_scene_handoff" in glossary:
    handoff_history.append(glossary["last_scene_handoff"])

glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/731.evd",
    "last_line_id": 19131,
    "resumo_dramatico": (
        "O bloco BLK_EVD_084 abrange cinco sequências dramáticas cruciais de revelação de linhagem, intimidade somática, redenção de autoestima e conflito psicológico profundo: "
        "(1) Em Event/154.evd, ao chegarem à cidade oculta de Em Pheyna, Lyner, Jack e Misha são confrontados pelo ancião Teru, Flute Ross Loria, que exige a [Provação da Lua] para comprovar se Lyner é um legítimo Apóstolo de Elemia. Flute reconhece Jack pelo seu nome ancestral de batismo, Harmonica, repreendendo-o por ter abandonado seu povo. Misha anuncia seu retorno cerimonial como Cantora das Estrelas, mas Flute e a Grande Anciã Tastiella constatam com choque que ela perdeu a capacidade de entoar a Chronicle Key devido à sua regressão física. Tastiella adverte sobre a astúcia humana e a necessidade do teste no Templo, que Lyner aceita com coragem resoluta enquanto Misha permanece retida. "
        "(2) Em Event/956.evd, na privacidade de um quarto de estalagem, Misha propõe a realização da primeira Instalação em seu corpo para fortalecer a Magia da Canção e proteger Lyner. Ela confessa o receio da dor e pede que Lyner seja gentil e cuidadoso. Após um momento de pudor cômico ao mostrar a tatuagem de seu Ponto de Instalação acima dos seios, Lyner realiza o procedimento com o Cristal Grathnode [Canção +10%], consolidando um pacto de confiança mútua e dedicação heroica. "
        "(3) Em Event/345.evd, no Ninho dos Dragões Alados, Lyner, Radolf, Ayatane e Aurica derrotam a criatura e encontram o sagrado Cristal Hymmnos «Linker», relíquia eclesiástica há muito buscada pela Igreja de Elemia. Tomada pelo trauma do massacre de Skuwat, Aurica teme tocar no cristal e atrair infortúnio, mas é sustentada pelo afeto inabalável de Lyner e pela bênção de Radolf, vertendo lágrimas de alívio e proclamando com imensa gratidão sua alegria por estar viva. "
        "(4) Em Event/525.evd, no covil vulcânico do Ninho dos Dragões, o grupo encontra Garzburn, o dragão ancestral soberano da ilha. Garzburn entrega a Krusche a preciosa caixa de ferramentas deixada por seu antigo companheiro, Luke, confirmando que o engenheiro prateado sobreviveu e alçou voo rumo ao topo da Torre, deixando Krusche profundamente comovida a sós. Ao saber que Lyner abateu seu arqui-rival secular Sleipnir, Garzburn comemora e abre sua Loja de Antiguidades com relíquias da civilização antiga. "
        "(5) Em Event/731.evd, na Cosmosfera de Aurica, o casal persegue um gato espiritual que drena suas forças. Surge a persona de Misha como presidente do grêmio estudantil destilando ofensas arrogantes, seguida pela persona das sombras de Aurica, que utiliza o gato para drenar a vitalidade de Misha. A sombra desmascara a inveja, o rancor e o ciúme que Aurica reprime em relação à amiga de infância de Lyner. Em vez de desprezá-la, Lyner abraça a humanidade e as fraquezas da jovem, conferindo-lhe a coragem necessária para rejeitar o poder ilícito e tecer a Magia Azul «Booster». Na ramificação alternativa de recusa, Aurica sucumbe ao ódio e drena o próprio Lyner até o colapso sensorial e a expulsão do mergulho."
    ),
    "decisoes_terminologicas": {
        "Provação da Lua": "月の試練 / Ordeal of the Moon",
        "Harmonica": "アルモニカ / Harmonica (Nome ancestral de Jack Hamilton)",
        "Flute Ross Loria": "フラウト・ロス・ロリア / Flute Ross Loria (Ancião de Em Pheyna)",
        "Tastiella": "タスティエーラ / Tastiella (Grande Anciã Teru)",
        "Instalação": "インストール / Install",
        "Ponto de Instalação": "インストールポイント / Install Point",
        "Canção +10%": "詩1割増サービス / 10% Song Increase",
        "Cristal Hymmnos Linker": "ヒュムネクリスタル「リンカ」 / Hymn Crystal Linker",
        "Garzburn": "ガルツベルン / Garzburn (Senhor soberano do Ninho dos Dragões)",
        "Loja de Antiguidades": "古代屋 / Antique Shop",
        "Sleipnir": "スレイプニル / Sleipnir",
        "Magia Azul Booster": "青魔法【ブースター】 / Blue Magic Booster"
    },
    "alertas_para_proximo_bloco": (
        "Para os blocos seguintes (BLK_EVD_085 em diante), manter a paridade estrita de variáveis e controles, "
        "o rigor nas quebras de linha (zero fraturas sintáticas e pontuações órfãs), a coerência com a linhagem Teru de Jack e as ramificações cósmicas de Aurica e Misha."
    )
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print("Glossario mestre atualizado com sucesso com os termos de BLK_EVD_084!")

# -*- coding: utf-8 -*-
import json
import datetime
import os

glossario_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
with open(glossario_path, "r", encoding="utf-8") as f:
    g = json.load(f)

# 1. Update last_scene_handoff
handoff_009 = {
    "status": "COMPLETED",
    "block_id": "BLK_EVD_009",
    "axis_id": "AXIS_3",
    "id_range": "2115-2338",
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "dramatic_context": (
        "Bloco narrativo de história e eventos BLK_EVD_009 (IDs 2115 a 2338, 20 arquivos Event/*.evd). "
        "Consagra momentos decisivos e cenas de ouro: 1. A criação da Magia Vermelha [Esfera de Gelo] com o Espírito do Gelo e a consulta ao eremita Yakuan na Cosmosfera de Misha, "
        "onde Misha desabafa seu ressentimento contra o fardo de cantar forçada como um robô sem sentimentos; "
        "2. A cena íntima de acampamento em que Aurica escreve uma carta secreta sob as provocações adoráveis de Lyner; "
        "3. A nobreza de Radolf liderando a reconstrução dos edifícios danificados; "
        "4. A queda da noite escura na Cosmosfera de Misha e a cobrança de sinceridade pela guardiã mental; "
        "5. O dia triunfal de celebração na Cosmosfera de Aurica; "
        "6. A memorável cena de culinária da meia-noite em que Lady Shurelia prepara o viscoso 'Suco de Comida' (Food Juice), Lyner quase se engasga com grãos de arroz e ganha a receita [SínC: Suco de Comida]; "
        "7. A revelação de worldbuilding no mirante do Rinkernator onde Shurelia expõe o Plug Sinfônico como a carótida da Torre e o santuário da sucessão e transmigração dos Administradores, revelando seu fardo secular solitário; "
        "8. O alarme popular com a marcha fanática da Igreja de Falss rumo ao topo da Torre pela Terra Santa e pelo Trio de Elemia; "
        "9. A paródia sentai/tokusatsu de Singer Angel Shurelia com o herbicida da justiça contra a vilã Claire e o monstro ELMA na Cosmosfera; "
        "10. O trauma de infância de Misha sendo pressionada a virar adulta e fugir da floresta proibida; "
        "11. A reunião de despedida no sopé da Torre rumo ao Mundo Superior através da Blastline, com Jack deixando seu aviso enigmático; "
        "12. A consulta sobre o componente Power Sourcer no Centro de Mergulho; "
        "13. E o resgate de Lyner e do Cristal Hymmnos [Purger] nos escombros por Jack, culminando na entrada do mercenário no grupo e na corrida para salvar Aurica."
    ),
    "decisoes_terminologicas": {
        "Glacial Ball (樹氷玉)": "[Esfera de Gelo] (Magia Vermelha de Misha padronizada com BLK_SYS_011; verbo 'teceu')",
        "Yakuan / Shaman (薬庵 / 仙人)": "Yakuan / eremita Yakuan (restauração do nome japonês original do sábio e correção do erro crasso de tradução 'I'll die')",
        "Song Fairy (詩の精)": "Fada das Canções (entidade espiritual ligada à canção)",
        "Food Juice (メシジュース)": "[Suco de Comida] / [SínC: Suco de Comida] (alinhado rigorosamente ao Glossário Mestre e síntese)",
        "Rinkernator (リンカーネイション)": "”Rinkernator” (Plug Sinfônico e santuário de transmigração e sucessão dos Administradores da Torre)",
        "Trio of Elemia (エレミア三謳神)": "Trio de Elemia (as três Deusas do Canto de Elemia: Eoria, Frelia e Tilia)",
        "Singer Angel Shurelia (シンガーエンジェル・シュレリア)": "Singer Angel Shurelia (bordão heroico do minigame na Cosmosfera)",
        "Harase-kun (原瀬君)": "Harase-kun (papel dramático de Lyner no minigame de Shurelia, corrigindo a corruptela 'Harasett')",
        "ELMA (エルマ)": "ELMA (guardião mecânico original da Torre Ar tonelico)",
        "Power Sourcer (パワーソーサー)": "Power Sourcer (componente gerador de baixa intensidade de energia sinfônica da máquina de Mergulho)",
        "Purger (パージャ)": "Cristal Hymmnos [Purger] (cristal sagrado purificador de vírus de Mir)"
    },
    "alertas_para_proximo_bloco": (
        "1. Jack ingressou na equipe ao final de Event/134.evd: manter seu tom experiente, descontraído e cínico. "
        "2. A conquista do Cristal Hymmnos [Purger] prepara a grande transição de purificação e ascensão rumo ao Mundo Superior. "
        "3. Manter a paridade terminológica de 'Plug Sinfônico', 'Rinkernator' e 'Trio de Elemia'."
    )
}

g["last_scene_handoff"] = handoff_009

# 2. Add / update terms safely
terms = g.setdefault("terms", {})

new_terms = {
    "Glacial Ball": {
        "pt": "Esfera de Gelo",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia Vermelha / Cosmosphere",
        "note": "Magia Vermelha tecida por Misha na montanha gélida de sua Cosmosfera (JP 樹氷玉 / Glacial Ball)."
    },
    "Yakuan": {
        "pt": "Yakuan",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / Cosmosphere",
        "note": "Eremita excêntrico da montanha gelada na Cosmosfera de Misha que distribui o remédio para transformação humana (JP 薬庵)."
    },
    "Power Sourcer": {
        "pt": "Power Sourcer",
        "gender": "masculino",
        "number": "singular",
        "category": "Mecanismo / Dive Machine",
        "note": "Componente que gera uma saída modesta de energia sinfônica para a máquina de Mergulho (JP パワーソーサー)."
    },
    "Rinkernator": {
        "pt": "Rinkernator",
        "gender": "masculino",
        "number": "singular",
        "category": "Instalação / Lore",
        "note": "Instalação vital da Torre onde se localiza o Plug Sinfônico e onde ocorre a sucessão e transmigração (輪廻転生) dos Administradores da Torre (JP リンカーネイション)."
    },
    "Singer Angel Shurelia": {
        "pt": "Singer Angel Shurelia",
        "gender": "feminino",
        "number": "singular",
        "category": "Alter-ego / Cosmosphere",
        "note": "Personagem de heroína mágica/tokusatsu encarnada por Shurelia em minigame na Cosmosfera armada com o herbicida da justiça (JP シンガーエンジェル・シュレリア)."
    },
    "Harase-kun": {
        "pt": "Harase-kun",
        "gender": "masculino",
        "number": "singular",
        "category": "Papel Dramático / Cosmosphere",
        "note": "Papel dramático de herói de tokusatsu assumido por Lyner no minigame de Shurelia (JP 原瀬君 / EN corrupto 'Harasett')."
    }
}

for k, v in new_terms.items():
    if k not in terms:
        terms[k] = v
        print(f"Added term: {k} -> {v['pt']}")
    else:
        print(f"Term {k} already exists, preserved.")

# Save back to glossario_mestre.json
with open(glossario_path, "w", encoding="utf-8") as f:
    json.dump(g, f, ensure_ascii=False, indent=2)

print("Glossário Mestre updated successfully!")

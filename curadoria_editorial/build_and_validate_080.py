# -*- coding: utf-8 -*-
"""
build_and_validate_080.py - Constrói, valida e salva BLK_EVD_080_output.json
"""
import sys
import json
import os
import re
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

sys.path.insert(0, r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial")
from curated_evd_630 import CURATED_630
from curated_evd_363 import CURATED_363
from curated_evd_392 import CURATED_392
from curated_evd_707 import CURATED_707

input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_080_input.json")
output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_080_output.json")

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Unifica os dicionários das quatro cenas
curated_dict = {}
curated_dict.update(CURATED_630)
curated_dict.update(CURATED_363)
curated_dict.update(CURATED_392)
curated_dict.update(CURATED_707)

print(f"Total de falas curadas carregadas: {len(curated_dict)}")
assert len(curated_dict) == 202, f"Esperado 202 falas, obtido {len(curated_dict)}"

# Validação linha a linha contra o validador editorial
hard_errors = []
soft_warnings = []

for item in input_data["dialogues"]:
    item_id = item["id"]
    if item_id not in curated_dict:
        hard_errors.append(f"ID {item_id} ausente no dicionário de curadoria!")
        continue
    
    cur_info = curated_dict[item_id]
    prop_text = cur_info["text"]
    orig_text = item["original_jp"]
    orig_en = item["original_en"]

    # 1. Paridade de controles e Hard Gates
    ok_hg, errs_hg = validador_editorial.validar_hard_gate(orig_text, prop_text, ignorar_quebras=True)
    if not ok_hg:
        for err in errs_hg:
            hard_errors.append(f"ID {item_id} Hard Gate: {err}")

    # 2. Soft gates (lint editorial, prosódia, fraturas sintáticas, etc.)
    sg_warns = validador_editorial.auditar_estilo_editorial(prop_text)
    if sg_warns:
        for warn in sg_warns:
            soft_warnings.append(f"ID {item_id} Soft Gate: {warn}")

print("\n=== RESULTADO DA VALIDAÇÃO ===")
print(f"Erros de Hard Gate: {len(hard_errors)}")
for err in hard_errors:
    print(f"  [ERRO] {err}")

print(f"Avisos de Soft Gate: {len(soft_warnings)}")
for warn in soft_warnings:
    print(f"  [AVISO] {warn}")

if hard_errors:
    print("\n[FALHA] Corrija os erros de Hard Gate antes de gerar o arquivo final!")
    sys.exit(1)

# Monta estrutura de saída
output_dialogues = []
output_curated_lines = []

for item in input_data["dialogues"]:
    item_id = item["id"]
    curated_info = curated_dict[item_id]
    trad_text = curated_info["text"]
    notes_text = curated_info["notes"]

    curated_line = {
        "id": item_id,
        "text": trad_text,
        "ptbr_text": trad_text,
        "ptbr_curated": trad_text,
        "status": "approved",
        "origin": "curadoria_editorial",
        "notes": notes_text,
        "rationale": notes_text
    }
    output_curated_lines.append(curated_line)

    d_out = dict(item)
    d_out["review_status"] = "approved"
    d_out["ptbr_text"] = trad_text
    d_out["text_ptbr"] = trad_text
    d_out["curated_ptbr"] = trad_text
    d_out["final_ptbr"] = trad_text
    d_out["texto_ptbr_curado"] = trad_text
    d_out["custom_text"] = trad_text
    d_out["reviewed"] = True
    d_out["notes"] = notes_text
    d_out["curation_notes"] = notes_text
    d_out["curadoria_notes"] = notes_text
    output_dialogues.append(d_out)

scene_handoff = {
    "last_scene_id": "Event/707.evd",
    "last_line_id": 18221,
    "resumo_dramatico": "O bloco BLK_EVD_080 consolida quatro momentos marcantes de Ar tonelico: (1) Em Event/630.evd, no Nível 4 da Cosmosfera de Misha, Lyner e Misha enfrentam o clima polar e o desafio etílico do Espírito da Flor. Misha concebe o ardil do guaxinim absorvente (Tanuki) dotado de enzimas de fermentação que expandem e murcham instantaneamente, derrotando o Espírito da Flor e tecendo a Magia Azul [Balão Absorvente] (青魔法【吸収風船】). Misha revela sua amargura contra a figura paterna autoritária (avatar de Leard), enquanto Lyner reflete sobre a semelhança com o seu próprio pai e o passado dos dois em Platina. (2) Em Event/363.evd, Lyner e Radolf alcançam o Altar dos Apóstolos (Altar do Advento) para resgatar Aurica. Lyner atinge uma revelação crucial ao perceber que proteger alguém vai muito além de brandir uma espada à sua frente. No altar, o Bispo Falss confirma com Tastiella que o cristal foi transferido para Aurica antes de se retirar. Tastiella força Aurica a consagrar sua alma e despertar a Deusa Tyeria, subjugando-a em transe enquanto o Cântico ressoa. (3) Em Event/392.evd, a reconstrução da aeronave Silver Horn é finalizada com a Nadadeira (Flutuador) ou o Núcleo Compartilhado forjado por Lyner via Grathmeld. A Presidente Ayano e todos os aliados celebram um marco sem precedentes na história de Sol Ciel: a união entre a Tribo Teru, os Humanos, a Igreja, a Tenba, os Apóstolos de Elemia e o Povo de Hórus. Krusche adverte que, após a decolagem, dificilmente poderão retornar ao Mundo Inferior. (4) Em Event/707.evd, na Cosmosfera de Aurica, Lyner e a sacerdotisa alcançam a Torre dos Espinhos e o Portão Inviolável, onde enfrentam o Demônio das Chamas, personificação do trauma do massacre de Skuwat. Aliando a espada de Lyner à Magia Azul Guarda de Fogo, derrotam a entidade e tecem a Magia Vermelha Flamia (赤魔法【フレイメア】). Don Leon surge anunciando a Mudança de Paradigma e incita a marcha para Stonehenge, ensinando que a abertura do coração de uma Reyvateil na Cosmosfera é fruto direto da retidão e do cavalheirismo no mundo real.",
    "decisoes_terminologicas": {
        "Balão Absorvente": "青魔法【吸収風船】 / Absorbing Balloon (Magia Azul tecida por Misha na Cosmosfera para suporte)",
        "Flamia": "赤魔法【フレイメア】 / Flamia (Magia Vermelha tecida por Aurica na Cosmosfera após derrotar o Demônio das Chamas)",
        "Demônio das Chamas": "炎の悪魔 / Fire Demon (manifestação do trauma de Aurica relativo à destruição de Skuwat)",
        "Portão Inviolável": "開かずの門 / Unopenable Gate / Door that never opens (entrada da Torre dos Espinhos na mente de Aurica)",
        "Torre dos Espinhos": "イバラの塔 / Thorn Tower (marco onírico que cerca o inconsciente profundo de Aurica)",
        "Deusa Tyeria": "ティリア神 / Goddess Tyeria (terceira Deusa Originária de Sol Ciel)",
        "Nadadeira (Flutuador)": "フリッパー / Flipper (módulo giroscópico essencial para sustentação da aeronave)",
        "Núcleo Compartilhado": "シェアリングコア / Sharing Core (componente sônico de propulsão para transpor a Blastline)"
    },
    "alertas_para_proximo_bloco": "Para os blocos seguintes (BLK_EVD_081 em diante), manter a coerência das relações de Lyner com Aurica e Misha tanto no mundo desperto quanto na Cosmosfera, a prontidão para o voo final na Silver Horn através da Blastline, a iminência do confronto com Mir e os desdobramentos da conspiração do Bispo Falss."
}

glossary_additions = {
    "Balão Absorvente": {
        "pt": "Balão Absorvente",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia da Canção / Azul",
        "note": "青魔法【吸収風船】 (Aomahō Kyūshū Fūsen / Absorbing Balloon). Magia Azul tecida por Misha no Nível 4 de sua Cosmosfera para suporte, inspirada no guaxinim que absorve e metaboliza saquê sem limites."
    },
    "Flamia": {
        "pt": "Flamia",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia da Canção / Vermelha",
        "note": "赤魔法【フレイメア】 (Akamahō Fureimea / Flamia). Magia Vermelha tecida por Aurica na Torre dos Espinhos após superar o terror do Demônio das Chamas com a ajuda de Lyner."
    },
    "Demônio das Chamas": {
        "pt": "Demônio das Chamas",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Inimigo Mental",
        "note": "炎の悪魔 (Honō no Akuma / Fire Demon). Entidade onírica que encarna o trauma devastador do incêndio do vilarejo de Skuwat na mente de Aurica."
    },
    "Portão Inviolável": {
        "pt": "Portão Inviolável",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Marco",
        "note": "開かずの門 (Akazu no Mon). Portão colossal selado na base da Torre dos Espinhos que resguarda o limiar para o inconsciente profundo e o mundo exterior na mente de Aurica."
    },
    "Deusa Tyeria": {
        "pt": "Deusa Tyeria",
        "gender": "feminino",
        "number": "singular",
        "category": "Divindade / Lore de Sol Ciel",
        "note": "ティリア神 (Tyeria-shin / Goddess Tyeria). A terceira Reyvateil Originária e deusa venerada na cosmologia de Sol Ciel, cuja alma é cobiçada pela Igreja de Elemia para o despertar divino."
    }
}

output_payload = {
    "block_id": "BLK_EVD_080",
    "axis_id": input_data.get("axis_id", "AXIS_3"),
    "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
    "category": input_data.get("category", "Event Dialogue"),
    "line_count": len(output_dialogues),
    "id_range": [output_dialogues[0]["id"], output_dialogues[-1]["id"]],
    "stats": {
        "total_lines": len(output_dialogues),
        "lines_rewritten": len(output_dialogues),
        "lines_approved_as_is": 0,
        "new_terms_added": len(glossary_additions)
    },
    "curated_lines": output_curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": output_dialogues,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_payload, f, indent=2, ensure_ascii=False)

print(f"\n[OUTPUT SALVO COM SUCESSO] {output_path}")
print(f"Total de falas no arquivo final: {len(output_dialogues)}")

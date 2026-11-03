# -*- coding: utf-8 -*-
"""
build_output_089.py - Geração canônica de BLK_EVD_089_output.json
"""
import sys
import json
from pathlib import Path

from curate_blk089 import curated_data

input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_089_input.json")
output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_089_output.json")

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_dialogues = input_data["dialogues"]
print(f"Loaded {len(input_dialogues)} input dialogues.")

dialogues_out = []
for d in input_dialogues:
    item_id = d["id"]
    curated_text, note = curated_data[item_id]

    entry = {
        "id": item_id,
        "event_file": d.get("event_file"),
        "speaker_id": d.get("speaker_id"),
        "speaker": d.get("speaker"),
        "original_jp": d.get("original_jp"),
        "original_en": d.get("original_en"),
        "current_ptbr": d.get("current_ptbr"),
        "review_status": "approved",
        "ptbr_text": curated_text,
        "text_ptbr": curated_text,
        "curated_ptbr": curated_text,
        "final_ptbr": curated_text,
        "texto_ptbr_curado": curated_text,
        "custom_text": curated_text,
        "reviewed": True,
        "notes": note,
        "curation_notes": note,
        "curadoria_notes": note
    }
    dialogues_out.append(entry)

scene_handoff = {
    "last_scene_id": "Event/890.evd",
    "last_line_id": 20209,
    "resumo_dramatico": (
        "O bloco BLK_EVD_089 abrange cinco sequências dramáticas e mecânicas cruciais: "
        "(1) Em Event/864.evd, Jack indaga com ironia se um Cavaleiro de Elemia luta apenas com uma espada pura. "
        "Ao descobrir que Lyner desconhece totalmente a arte do Aprimoramento (パワード / Powered), Jack o conduz até a loja de armas. "
        "A vendedora reconhece os salvadores da cidade e presenteia o grupo com o raríssimo Cristal Grathnode «Ataque Duplo» (ダブルアタック). "
        "Jack instrui Lyner sobre a infusão de cristais em armas e é exibido o tutorial detalhado do sistema de Aprimoramento. "
        "(2) Em Event/809.evd, Lyner vivencia uma simulação narrativa cômica e paródica de romance/tokusatsu da Cosmosfera de Shurelia. "
        "Assumindo o papel de Raina Harase (原瀬頼奈) ao lado de Misha (彌紗), ele está prestes a desposar Leila Togasaki (塔ヶ崎澪羅 / Shurelia). "
        "O falso padre revela-se uma encarnação viral do Bispo Falss, e Claire invade a cerimônia em busca de vingança. "
        "Para lutar sem esgotar sua vida, Leila canaliza os Harmonics de Lyner e transforma-se na heroína mágica «Singer Angel Shurelia» (シンガーエンジェル・シュレリア). "
        "O vírus Falss liberta seu poder aterrador e a simulação termina em Game Over. "
        "Shurelia acolhe Lyner de volta à realidade com sua costumeira calma, encorajando-o a tentar novamente. "
        "(3) Em Event/375.evd, na Catedral de Platina, ocorre a reviravolta capital da invasão viral: "
        "Shurelia, sob possessão do vírus de Mir, declara a revolução apocalíptica para extirpar a humanidade e instaurar uma utopia de Reyvateils. "
        "Ela ataca e captura o Comandante Leard como detentor de segredos de Nível Especial A, sentenciando-o ao confinamento no Jardim de Prisma (プリズムガーデン). "
        "Trasladando-se com o código sagrado Hymmnos (#0Wee i ga flip 0x1011001101 enter ARTONELICO), Shurelia desaparece com Leard. "
        "Radolf questiona o surto viral e Jack ordena marcha urgente ao altar biomecânico Crescent Chronicle (クレセントクロニクル), onde Misha mantém Mir confinada. "
        "(4) Em Event/959.evd, o grupo invade instalações clandestinas da corporação Tenba e flagra cientistas replicando os experimentos ilegais de Bourd. "
        "Desesperados para não serem denunciados à Presidente Ayano, os pesquisadores oferecem o maquinário ao grupo. "
        "Misha lembra que o dispositivo permite separar cristais e pede para usá-lo para voltar a ser pequena, flertando e deixando Lyner completamente sem graça. "
        "Com isso, desbloqueia-se a função de alternância cosmética da aparência de Misha. "
        "(5) Em Event/890.evd, Shurelia desaparece subitamente nos corredores da Torre entre Misha e Aurica. "
        "O grupo é surpreendido por uma chamada pública oficial no interfone da Torre: a atendente Mei Mei convoca Lyner Barsett ao balcão. "
        "Ao chegarem lá, Mei Mei dá uma bronca centenária em Shurelia por acordá-la direto por ter se perdido de novo pela enésima vez em centenas de anos. "
        "Aurica cai na gargalhada ao constatar que a deusa de Platina é uma perdida incurável sem o menor senso de direção. "
        "Shurelia aceita a ajuda de Aurica com elegância e tenta salvar a dignidade perante Radolf e Jack alegando que estava apenas 'fazendo a manutenção do observatório'."
    ),
    "decisoes_terminologicas": {
        "Aprimoramento": "パワード (Powered / Enhancing - sistema de fixação de Cristais Grathnode em armas e armaduras)",
        "Ataque Duplo": "ダブルアタック (Double Attack - Cristal Grathnode de ataque duplo)",
        "Raina Harase": "原瀬頼奈 (Raina Harase - identidade escolar fictícia paródica de Lyner Barsett na simulação de Shurelia)",
        "Leila Togasaki": "塔ヶ崎澪羅 (Leila Togasaki - identidade fictícia de noiva/colegial de Shurelia na simulação)",
        "Singer Angel Shurelia": "シンガーエンジェル・シュレリア (Singer Angel Shurelia - alter-ego heroico mágico de Shurelia)",
        "Jardim de Prisma": "プリズムガーデン (Prism Garden - setor superior de segurança máxima da Torre)",
        "Crescent Chronicle": "クレセントクロニクル (Crescent Chronicle - monumental altar biomecânico de contenção de Mir)",
        "Alternância de Aparência de Misha": "ミシャの姿変更 (Misha Costume / Appearance change)",
        "Interfone da Torre / Anúncio Interno": "塔内放送 (Tower PA system / anúncio público operado por Mei Mei)",
        "Desligada Nata / Avoada": "生粋 / 天然 (Kissui / Tennen - traço cômico canônico de Shurelia como avoada incurável)"
    },
    "alertas_para_proximo_bloco": (
        "Para os blocos seguintes (BLK_EVD_090 em diante), atentar para as consequências da invasão viral em Platina, "
        "a rota até o Jardim de Prisma para resgate do Comandante Leard e o confronto iminente no Crescent Chronicle."
    )
}

glossary_additions = {
    "Aprimoramento": {
        "pt": "Aprimoramento",
        "gender": "masculino",
        "number": "singular",
        "category": "Sistema de Batalha / Customização",
        "note": "パワード (Powered / Enhancing). Mecânica de engaste e infusão de Cristais Grathnode em compartimentos de armas e armaduras dos personagens de combate."
    },
    "Ataque Duplo": {
        "pt": "Cristal Grathnode: «Ataque Duplo»",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Cristal Grathnode",
        "note": "ダブルアタック (Double Attack). Cristal Grathnode valioso que concede probabilidade de acerto físico duplo aos golpes da arma."
    },
    "Raina Harase": {
        "pt": "Raina Harase",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / Simulação Cósmica",
        "note": "原瀬頼奈 (Raina Harase). Papel dramático e identidade colegial paródica de Lyner Barsett na simulação urbana e minigame de Shurelia."
    },
    "Alternância de Aparência": {
        "pt": "Alternância de Aparência",
        "gender": "feminino",
        "number": "singular",
        "category": "Sistema / Recurso Cosmético",
        "note": "ミシャの姿変更. Funcionalidade desbloqueada nos laboratórios da Tenba que permite alternar o modelo físico e estético de Misha entre suas formas infantil e adulta."
    }
}

output_data = {
    "block_id": "BLK_EVD_089",
    "axis_id": input_data.get("axis_id", "AXIS_MAIN_EVENT"),
    "axis_name": input_data.get("axis_name", "Eventos Principais e Cenas de História"),
    "category": input_data.get("category", "main_events"),
    "line_count": len(dialogues_out),
    "id_range": [dialogues_out[0]["id"], dialogues_out[-1]["id"]],
    "stats": {
        "total_lines": len(dialogues_out),
        "lines_rewritten": len(dialogues_out),
        "lines_approved_as_is": 0,
        "new_terms_added": len(glossary_additions)
    },
    "curated_lines": dialogues_out,
    "glossary_additions": glossary_additions,
    "dialogues": dialogues_out,
    "scene_handoff": scene_handoff,
    "entries": dialogues_out,
    "block_entries": dialogues_out
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {output_path} with {len(dialogues_out)} lines.")

# -*- coding: utf-8 -*-
"""
assemble_and_validate_081.py - Montagem e validação determinística de BLK_EVD_081_output.json
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

sys.path.insert(0, r"C:\Users\Daniel\.gemini\antigravity\brain\1dcbd210-958c-46bf-985a-65eb160b811f\scratch")
from draft_scene1 import scene1
from draft_scene2 import scene2
from draft_scene3 import scene3
from draft_scene4 import scene4
from draft_scene5 import scene5
from draft_scene6 import scene6
from draft_scene7 import scene7

all_curated = {}
all_curated.update(scene1)
all_curated.update(scene2)
all_curated.update(scene3)
all_curated.update(scene4)
all_curated.update(scene5)
all_curated.update(scene6)
all_curated.update(scene7)

input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_081_input.json")
output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_081_output.json")

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_dialogues = input_data["dialogues"]
print(f"Total lines in input: {len(input_dialogues)}")

dialogues = []
curated_lines = []

for item in input_dialogues:
    item_id = item["id"]
    curated_info = all_curated[item_id]
    c_text = curated_info["ptbr"]
    c_note = curated_info["notes"]

    dialogue_entry = {
        "id": item_id,
        "event_file": item.get("event_file", ""),
        "speaker_id": item.get("speaker_id", 0),
        "speaker": item.get("speaker", ""),
        "original_jp": item.get("original_jp", ""),
        "original_en": item.get("original_en", ""),
        "current_ptbr": item.get("current_ptbr", ""),
        "review_status": "approved",
        "ptbr_text": c_text,
        "text_ptbr": c_text,
        "curated_ptbr": c_text,
        "final_ptbr": c_text,
        "texto_ptbr_curado": c_text,
        "custom_text": c_text,
        "reviewed": True,
        "notes": c_note,
        "curation_notes": c_note,
        "curadoria_notes": c_note
    }
    dialogues.append(dialogue_entry)

    curated_entry = {
        "id": item_id,
        "text": c_text,
        "ptbr_text": c_text,
        "ptbr_curated": c_text,
        "status": "approved",
        "origin": "curadoria_editorial",
        "notes": c_note,
        "rationale": c_note
    }
    curated_lines.append(curated_entry)

glossary_additions = {
    "Circular de Inversão de Fase": {
        "pt": "Circular de Inversão de Fase",
        "gender": "feminino",
        "number": "singular",
        "category": "Artefato Sagrado / Grathmeld",
        "note": "相転換サーキュラ (Sōtenkan Sākyura / Circula Teleporter). Artefato sagrado indispensável para a realização do Batismo de Circula no Olho Congelado. Também apelidado carinhosamente por Krusche de [Tigela do Gatinho] (猫どんぶり)."
    },
    "Lamento de Deus": {
        "pt": "Lamento de Deus",
        "gender": "masculino",
        "number": "singular",
        "category": "Fenômeno Fônico / Torre",
        "note": "神の叫び (Kami no Sakebi / Wail of God). Corrente fônica ascendente e tempestuosa que flui na região do Olho Congelado, impedindo qualquer descida e tornando a ascensão uma via de mão única."
    },
    "ELMA-DS": {
        "pt": "ELMA-DS",
        "gender": "masculino",
        "number": "singular",
        "category": "Entidade Viral / Inimigo",
        "note": "ELMA-DS (ELMAーDS). Variante viral malévola e negra que corrompe e replica o guardião autônomo ELMA criado por Shurelia. Ao ser derrotado com o Purger, refugia-se forçadamente na Cosmosfera da parceira de Lyner."
    },
    "Purger": {
        "pt": "Purger",
        "gender": "masculino",
        "number": "singular",
        "category": "Hymn Crystal / Lore",
        "note": "パージャ (Pāja / Purger). Cristal Hymmnos sagrado de purificação capaz de anular a desmaterialização de formas virais em energia pura."
    },
    "Corredor Musical": {
        "pt": "Corredor Musical",
        "gender": "masculino",
        "number": "singular",
        "category": "Cenário / Estrutura da Torre",
        "note": "彩音回廊 (Saion Kairō / Musical Corridor). Instalação acústica e prismática no interior da Torre cujas luzes e frequências fônicas regulam as seis Placas Hexagonais."
    },
    "Funbun em conserva no vinagre": {
        "pt": "Funbun em conserva no vinagre",
        "gender": "masculino",
        "number": "singular",
        "category": "Culinária / Item Cômico",
        "note": "オボンヌのビネガー漬け (Obonnu no binegā-zuke / Pickled Funbun). Criação culinária vanguardista e peculiar elaborada por Aurica para o almoço com Lyner em Platina durante o epílogo."
    }
}

scene_handoff = {
    "last_scene_id": "Event/782.evd",
    "last_line_id": 18504,
    "resumo_dramatico": "O bloco BLK_EVD_081 consolida momentos de máxima densidade dramática, romântica e de encerramento em Ar tonelico: (1) Em Event/165.evd, Lyner entrega a Circular de Inversão de Fase (相転換サーキュラ, apelidada de Tigela do Gatinho) a Hama, que confirma a prontidão para o Batismo de Circula no Olho Congelado e adverte que a travessia é uma via de mão única rumo ao Mundo Superior devido ao Lamento de Deus (神の叫び). Flute abençoa a partida e despede-se com pesar de Harmonica (Jack), que parte com Misha sem prometer retorno. (2) Em Event/188.evd (rota Misha) e Event/187.evd (rota Aurica), a equipe confronta o ELMA-DS; encurralado pelo efeito do Purger que o impede de voltar ao Campo Binário, o vírus realiza um Mergulho violento e forçado na Cosmosfera da sacerdotisa, deixando-a em coma profundo. Lyner jura solenemente que dedicará a vida inteira a curá-la e Shurelia os instrui a irem ao Centro de Mergulho. (3) Em Event/272.evd, diante dos tanques de incubação de Reyvateils, Misha entra em crise de pânico ao encarar a iminente perda de seu corpo infantil e a recuperação de sua Canção, suplicando para que Lyner prometa amá-la incondicionalmente mesmo se sua forma física mudar; Lyner a acolhe com ternura inquebrantável. (4) Em Event/305.evd, Ayatane e Lyner auxiliam Aurica na sala de controle do Corredor Musical para equilibrar as Placas Hexagonais, onde Lyner intervém carinhosamente para resgatar a autoestima frágil da sacerdotisa. (5) Em Event/427.evd, testemunha-se o Epílogo e Final da Rota de Aurica: a paz raia sobre Sol Ciel, os companheiros se dispersam (Radolf regressa a Nemo, Jack vaga pelo mundo com Misha, Krusche retorna à oficina de aeronaves no Beco Vagalume), mas Aurica permanece em Platina nomeada arquivista da Catedral por Leard com a bênção de Radolf. Meses depois, Aurica e Lyner compartilham o almoço no Gather, onde Aurica desabafa com comovente maturidade como o amor puro, constante e sem julgamentos de Lyner derreteu o gelo de seu coração e devolveu-lhe a vontade de viver, selando a união eterna do casal. (6) Em Event/782.evd, Shurelia e Lyner descobrem no Campo Binário programas antigos de simulação narrativa do cotidiano comum, conduzindo um diálogo bem-humorado e metalinguístico com o jogador.",
    "decisoes_terminologicas": {
        "Circular de Inversão de Fase": "相転換サーキュラ / Circula Teleporter (padronizado com os blocos canônicos de síntese)",
        "Tigela do Gatinho": "猫どんぶり / Kitty Bowl (alcunha carinhosa dada por Krusche)",
        "Lamento de Deus": "神の叫び / Wail of God (corrente sônica ascendente da Torre)",
        "Batismo de Circula": "サーキュラの洗礼 / Circula Baptism (rito de transição de fase)",
        "Olho Congelado": "氷の瞳 / Frozen Eye (fronteira física e fônica entre os mundos)",
        "Purger": "パージャ / Purger (Hymn Crystal sagrado)",
        "ELMA-DS": "ELMA-DS / ELMAーDS (entidade viral invasora)",
        "Campo Binário": "バイナリ野 / Binary Field (dimensão de dados e controle da Torre)",
        "Corredor Musical": "彩音回廊 / Musical Corridor (complexo fônico das Placas Hexagonais)",
        "Placas Hexagonais": "六角板 / Hexagon Plates (estruturas reguladoras atmosféricas)",
        "Funbun em conserva no vinagre": "オボンヌのビネガー漬け / Pickled Funbun (iguaria vanguardista de Aurica)"
    },
    "alertas_para_proximo_bloco": "Para os blocos seguintes (BLK_EVD_082 em diante), manter a continuidade das ramificações de eventos e finais, a estabilidade das Cosmosferas de Aurica e Misha no pós-jogo ou eventos paralelos, e a preservação rigorosa da Tríade de Idiomas e paridade técnica."
}

output_obj = {
    "block_id": "BLK_EVD_081",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(dialogues),
    "id_range": [dialogues[0]["id"], dialogues[-1]["id"]],
    "stats": {
        "total_lines": len(dialogues),
        "lines_rewritten": len(dialogues),
        "lines_approved_as_is": 0,
        "new_terms_added": len(glossary_additions)
    },
    "curated_lines": curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": dialogues,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_obj, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {output_path} with {len(dialogues)} dialogues.")

# Validação do arquivo gerado
with open(output_path, "r", encoding="utf-8") as f:
    data = json.load(f)

assert data["block_id"] == "BLK_EVD_081"
assert "stats" in data
assert "curated_lines" in data
assert "dialogues" in data
assert "scene_handoff" in data
assert "glossary_additions" in data

lines = data["dialogues"]
curated_l = data["curated_lines"]
assert len(lines) == 283
assert len(curated_l) == 283

required_fields = [
    "id", "event_file", "speaker_id", "speaker", "original_jp", "original_en",
    "curated_ptbr", "review_status", "reviewed"
]

missing_field_errors = 0
for d in lines:
    for field in required_fields:
        if field not in d:
            print(f"[SCHEMA ERROR] ID {d.get('id')}: Missing field '{field}'")
            missing_field_errors += 1

hard_gate_errors = 0
lint_warnings = 0
cr_errors = 0
orphan_errors = 0
fracture_errors = 0

for item in lines:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    trad = item["curated_ptbr"]

    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=trad,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {item_id}: {e}")

    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        cr_errors += 1

    parts = trad.split("\n")
    for line_part in parts[1:]:
        line_strip = line_part.strip()
        if line_strip.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            orphan_errors += 1
        if line_part.startswith("..."):
            print(f"[ERROR] ID {item_id}: Line starts with reticências after newline: {line_part!r}")
            orphan_errors += 1

    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r} in text: {trad!r}")
        fracture_errors += 1

print(f"\nValidation Summary for BLK_EVD_081:")
print(f"Total lines evaluated: {len(lines)}")
print(f"Missing Field Errors: {missing_field_errors}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")
print(f"CR Errors: {cr_errors}")
print(f"Orphan Errors: {orphan_errors}")
print(f"Fracture Errors: {fracture_errors}")

if missing_field_errors == 0 and hard_gate_errors == 0 and lint_warnings == 0 and cr_errors == 0 and orphan_errors == 0 and fracture_errors == 0:
    print("\n[PERFECTION] All 283 lines passed all technical and editorial checks with ZERO errors and ZERO warnings!")
else:
    print(f"\n[FAILURE] Validation detected errors.")
    sys.exit(1)

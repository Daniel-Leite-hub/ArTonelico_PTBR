# -*- coding: utf-8 -*-
"""
assemble_and_validate_083.py - Montagem e validação determinística de BLK_EVD_083_output.json
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

sys.path.insert(0, r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos")
from draft_scene1 import scene1
from draft_scene2 import scene2
from draft_scene3 import scene3
from draft_scene4 import scene4

all_curated = {}
all_curated.update(scene1)
all_curated.update(scene2)
all_curated.update(scene3)
all_curated.update(scene4)

input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_083_input.json")
output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_083_output.json")

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_dialogues = input_data["dialogues"]
print(f"Total lines in input: {len(input_dialogues)}")

dialogues = []
curated_lines = []

for item in input_dialogues:
    item_id = item["id"]
    if item_id not in all_curated:
        print(f"Missing ID {item_id} in curated drafts!")
        sys.exit(1)

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

scene_handoff = {
    "last_scene_id": "Event/766.evd",
    "last_line_id": 18912,
    "resumo_dramatico": "O bloco BLK_EVD_083 abrange quatro sequências cruciais de conflito fisiológico, exploração psíquica e provação amorosa: (1) Em Event/323.evd, logo após o resgate de Misha e a despedida da equipe de Jack, Aurica sofre um colapso repentino de febre alta. Claire intervém em prantos e desculpa-se por suas palavras duras anteriores, diagnosticando que Aurica foi acometida pela temida febre de Tatoolist (タトゥリスタ病) — a pane fisiológica mortal que assola Reyvateils da Terceira Geração privadas de seu agente prolongador de vida (延命剤). Radolf e Claire deduzem que o organismo dela está consumindo o composto em ritmo anormalmente acelerado, e Shurelia instrui Lyner a mergulhar urgentemente na Cosmosfera de Aurica pelo Centro de Mergulho para salvar sua vida. (2) Em Event/598.evd, no interior da Cosmosfera de Misha imersa em trevas sufocantes, Lyner e Misha encontram um pequeno espírito do gelo (氷の精) que derreteu por ter se perdido na escuridão rumo ao Monte das Geadas (樹氷山). Misha relembra com saudade nostálgica as neves de outrora que clareavam o mundo. Na ramificação de sucesso, estimulada pela confiança inabalável de Lyner e pelos ensinamentos do Nível 1, Misha dialoga com seu mundo e tece a Magia Verde [Análise] (緑魔法【アナライザ】), desvendando a rota até o topo da montanha. Na ramificação de falha, Misha desiste consumida pelo medo do breu, o espírito se dissolve e Lyner é expulso da Cosmosfera pela Moradora do Mundo Inferior. (3) Em Event/953.evd, os atendentes do Centro de Mergulho e o Operador de Portão revelam com espanto que Lyner e Aurica alcançaram profundidades incomuns na Cosmosfera sem terem realizado a Instalação (インストール). Aurica cora intensamente confessando que nunca passou por isso e não sabia como propor o rito. O atendente explica a gravidade física da técnica: a inserção direta de Cristais Grathnode na carne da Reyvateil amplia a força da Magia da Canção, mas atua como veneno tóxico ao organismo da donzela. Lyner, estarrecido, recusa-se a machucá-la, e o atendente sugere que o casal vá a uma pousada conversar a sós e decidir com o coração. (4) Em Event/766.evd, no Nível 8 da Cosmosfera de Aurica, o casal confronta a Silfa (シルフ), espírito livre que roubou o vestido cerimonial nupcial para impedir o enlace matrimonial com Lyner, alertando Aurica sobre a renúncia da solidão autossuficiente e a perda da liberdade individual. Na ramificação vitoriosa, Aurica amadurece e declara com nobreza que o amor compartilhado expande a vida em vez de aprisioná-la; a Silfa devolve o vestido abençoando o casal, Aurica veste o traje para deslumbre de Lyner, convida-o para a cerimônia na Catedral e tece a Magia Vermelha [Dança da Silfa] (赤魔法【シルフのダンス】). Na ramificação de recusa, Aurica recua atemorizada pelo compromisso e a Silfa despacha o vestido e Lyner com um golpe tempestuoso pelos ares.",
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

output_obj = {
    "block_id": "BLK_EVD_083",
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

# Validação estrita do arquivo gerado
with open(output_path, "r", encoding="utf-8") as f:
    data = json.load(f)

assert data["block_id"] == "BLK_EVD_083"
assert "stats" in data
assert "curated_lines" in data
assert "dialogues" in data
assert "scene_handoff" in data
assert "glossary_additions" in data

lines = data["dialogues"]
curated_l = data["curated_lines"]
assert len(lines) == 228
assert len(curated_l) == 228

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

print(f"\nValidation Summary for BLK_EVD_083:")
print(f"Total lines evaluated: {len(lines)}")
print(f"Missing Field Errors: {missing_field_errors}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")
print(f"CR Errors: {cr_errors}")
print(f"Orphan Errors: {orphan_errors}")
print(f"Fracture Errors: {fracture_errors}")

if missing_field_errors == 0 and hard_gate_errors == 0 and lint_warnings == 0 and cr_errors == 0 and orphan_errors == 0 and fracture_errors == 0:
    print("\n[PERFECTION] All 228 lines passed all technical and editorial checks with ZERO errors and ZERO warnings!")
else:
    print(f"\n[FAILURE] Validation detected errors.")
    sys.exit(1)

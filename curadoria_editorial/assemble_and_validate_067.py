# -*- coding: utf-8 -*-
"""
assemble_and_validate_067.py - Validação determinística e geração de BLK_EVD_067_output.json
"""
import sys
import json
import os
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_067_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_067_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Carrega módulos de dados
import data_067_batch1 as b1
import data_067_batch2 as b2
import data_067_batch3 as b3

curated_dict = {}
curated_dict.update(b1.curated_dict)
curated_dict.update(b2.curated_dict)
curated_dict.update(b3.curated_dict)

print(f"Total curated entries loaded: {len(curated_dict)}")
assert len(curated_dict) == 223, f"Expected 223 entries, got {len(curated_dict)}"

curated_lines = []
dialogues_out = []

for item in input_data["dialogues"]:
    item_id = item["id"]
    if item_id not in curated_dict:
        raise KeyError(f"Missing curation for ID {item_id}")
    cur_info = curated_dict[item_id]
    pt_text = cur_info["pt"]
    rat = cur_info["rationale"]

    curated_lines.append({
        "id": item_id,
        "ptbr_curated": pt_text,
        "rationale": rat
    })

    d_entry = dict(item)
    d_entry["review_status"] = "approved"
    d_entry["curated_ptbr"] = pt_text
    d_entry["final_ptbr"] = pt_text
    d_entry["texto_ptbr_curado"] = pt_text
    d_entry["custom_text"] = pt_text
    d_entry["ptbr_curated"] = pt_text
    d_entry["reviewed"] = True
    d_entry["notes"] = rat
    d_entry["curation_notes"] = rat

    dialogues_out.append(d_entry)

glossary_additions = {
    "Falcon's Claw": {
        "pt": "Garra do Falcão",
        "gender": "feminino",
        "number": "singular",
        "category": "Toponímia / Localização",
        "note": "たかのつめあと. Ilhota rochosa isolada e ninho de serpes aladas, completamente apartada da estrutura principal das Asas de Hórus."
    },
    "Tragic Heroine": {
        "pt": "Heroína Trágica",
        "gender": "feminino",
        "number": "singular",
        "category": "Conceito Psicológico / Cosmosfera",
        "note": "悲劇のヒロイン. Arquétipo central da neurose de abandono de Misha na Cosmosfera, distorcido pejorativamente pela NISA como 'drama queen'."
    },
    "Paradox Trap": {
        "pt": "Armadilha da Eternidade",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Sistema",
        "note": "永遠の罠. Laço mental patológico na Cosmosfera de Misha capaz de induzir mergulhadores a um coma perpétuo."
    },
    "Self-Paradox": {
        "pt": "Paradoxo Interno",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Sistema",
        "note": "自己パラドックス. Ruptura na estrutura lógica de um nível da Cosmosfera causada por desejos irreconciliáveis da Reyvateil."
    }
}

scene_handoff = {
    "last_scene_id": "Event/642.evd",
    "last_line_id": 15522,
    "resumo_dramatico": "O bloco BLK_EVD_067 abrange três sequências cruciais de alta intensidade narrativa: (1) Em Event/118.evd, Radolf transporta Lyner e Misha na aeronave clerical, revelando a busca pelo Cristal Hymmnos e orientando Lyner a consultar o Bispo Falss. Durante a travessia, Misha desabafa sobre sua acrofobia e seu passado em Platina, mas são emboscados por Bourd (antagonista da Tenba), que faz Aurica de refém sobre o abismo. Misha se sacrifica caminhando sozinha pela prancha para poupar Aurica. Bourd descarta Aurica no precipício; Lyner salta e se recusa a soltar sua mão. Ambos são salvos em manobra acrobática por Krusche, que colide e pousa na isolada Garra do Falcão (たかのつめあと), um ninho de serpes voadoras fora das Asas de Hórus, alfinetando o 'luxo' de Lyner cercado de Reyvateils. (2) Em Event/294.evd, malandros abordam Aurica com intimidações e assédio verbal no Baixo Mundo. Lyner intervém tomado por fúria cega e espanca os agressores quase até a morte. Claire intervém e admoesta Lyner: a verdadeira proteção não nasce de brandir a espada a esmo nem de espalhar terror nos olhos de quem se ama, oferecendo uma Canção para serenar os ânimos. (3) Em Event/642.evd, na Cosmosfera de Misha, a persona tirânica da amiga de infância exige posse absoluta sobre Lyner sob pena de morte ou exílio. Lyner recusa o cativeiro afetivo e a desafia a matá-lo ela mesma. A recusa colapsa as defesas de Misha, que confessa seu desespero de ser esquecida e sua necessidade de ser a 'heroína trágica' (悲劇のヒロイン, corrigindo a deturpação 'drama queen' da NISA) para ser amada eternamente. O autoconflito gera um paradoxo interno e aciona a Mudança de Paradigma rumo a Stonehenge, culminando no resgate de Lyner da armadilha da eternidade (永遠の罠) antes de um coma irreversível.",
    "decisoes_terminologicas": {
        "Hymn Crystal": "ヒュムネクリスタル (Cristal Hymmnos)",
        "Falcon's Claw": "たかのつめあと (Garra do Falcão)",
        "Wings of Horus": "ホルスの翼 (Asas de Hórus)",
        "Dokkoi Set": "ドッコイ定食 (Combo Dokkoi)",
        "Tragic Heroine": "悲劇のヒロイン (Heroína Trágica)",
        "Paradigm Shift": "パラダイムシフト (Mudança de Paradigma)",
        "Stonehenge": "ストーンヘンジ (Stonehenge)",
        "Paradox Trap": "永遠の罠 (Armadilha da Eternidade)",
        "Self-Paradox": "自己パラドックス (Paradoxo Interno)"
    },
    "alertas_para_proximo_bloco": "Com a Garra do Falcão consolidada como enclave isolado e a Mudança de Paradigma de Misha ativada em direção a Stonehenge na Cosmosfera, o próximo bloco deve acompanhar a progressão dos níveis mentais e a travessia das ilhas flutuantes."
}

output_data = {
    "block_id": "BLK_EVD_067",
    "axis_id": input_data.get("axis_id"),
    "axis_name": input_data.get("axis_name"),
    "category": input_data.get("category"),
    "line_count": len(dialogues_out),
    "id_range": [dialogues_out[0]["id"], dialogues_out[-1]["id"]],
    "curated_lines": curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": dialogues_out,
    "scene_handoff": scene_handoff
}

# Validações determinísticas
hard_gate_errors = 0
lint_warnings = 0

for item in dialogues_out:
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

    # Check for \r
    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1

    # Check orphan line start with punctuation after \n
    parts = trad.split("\n")
    for line_part in parts[1:]:
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1

    # Check syntactic fracture before \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

print(f"\nValidation Summary for BLK_EVD_067:")
print(f"Total lines evaluated: {len(dialogues_out)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"\n[SUCCESS] BLK_EVD_067_output.json written successfully with 0 errors and 0 warnings!")
else:
    print(f"\n[FAILURE] Cannot save output JSON until all errors and warnings are resolved.")
    sys.exit(1)

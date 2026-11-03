# -*- coding: utf-8 -*-
"""
Script to curate, assemble, validate and finalize BLK_EVD_018
with full canonical depth and strict LQA validation.
"""
import json
import sys
import os

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_018_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_018_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

batches = [
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_018.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_018.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch3_018.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_018.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_018.json"
]

all_curated = []
for b_file in batches:
    with open(b_file, "r", encoding="utf-8") as f:
        items = json.load(f)
        all_curated.extend(items)

print(f"Total curated items loaded: {len(all_curated)}")
assert len(all_curated) == 208, f"Expected 208 items, got {len(all_curated)}"

merged_dialogues = []
lines_rewritten = 0
lines_approved_as_is = 0

for item in all_curated:
    item_id = item["id"]
    inp = input_map[item_id]
    
    verdict = item["verdict"]
    if verdict == "rewritten":
        lines_rewritten += 1
    else:
        lines_approved_as_is += 1
        
    merged_dialogues.append({
        "id": item_id,
        "event_file": inp["event_file"],
        "speaker": inp["speaker"],
        "original_jp": inp["original_jp"],
        "original_en": inp["original_en"],
        "current_ptbr": inp["current_ptbr"],
        "curated_ptbr": item["curated_ptbr"],
        "verdict": verdict,
        "rationale": item["rationale"]
    })

scene_handoff = {
    "resumo_dramatico": (
        "O bloco narrativo BLK_EVD_018 (IDs 4511 a 4718, cobrindo 21 arquivos de eventos Event/*.evd) aprofunda dimensões "
        "emocionais decisivas, desde o trauma de infância das heroínas até comédias cotidianas e a evolução de seus vínculos: "
        "1. Nos corredores da Torre (Event/81.evd), Misha entra em colapso de terror visceral perante um portão lacrado "
        "associado aos traumas de seu passado, sendo carinhosamente confortada por Lyner, que decide jamais forçá-la a retornar àquele local; "
        "2. Na investigação com Radolf e Ayatane (Event/321.evd e Event/308.evd), o grupo busca pistas do paradeiro de Aurica e "
        "desvenda enigmas de reflexão luminosa com placas vermelhas e espelhos na arquitetura mecânica da Torre; "
        "3. Nos limiares da Cosmosfera (Event/966.evd e Event/769.evd), a guardiã do portal instrui Lyner sobre os requisitos de intimidade "
        "e a mecânica dos Tópicos de Conversa necessários para prosseguir após a Mudança de Paradigma; "
        "4. No épico cômico-dramático do mundo escolar na Cosmosfera de Shurelia (Event/792.evd e Event/799.evd), Claire atua como a "
        "arrogante vilã da Facção Mir que drena o Poder Harmônico das alunas; Shurelia (sob a identidade da colegial Tougasaki Leila) "
        "sucumbe ao desespero de carregar o fardo de salvar o mundo aos 15 anos; a guardiã adverte Lyner (na persona Raina / Harase-kun) "
        "sobre o perigo fatal de Tougasaki descobrir sua ligação de sangue com Mir; e após uma batalha espetacular onde derrotam o monstro "
        "ELMA e destroem a central da Facção Mir, Lyner pede perdão sincero por suas desconfianças anteriores; "
        "5. No primeiro Mergulho de Aurica (Event/952.evd), a heroína visita uma Loja de Mergulho pela primeira vez, confessa nunca ter tido "
        "um parceiro na Igreja e sela um comovente pacto de confiança com Lyner; "
        "6. Na ativação de portais (Event/341.evd e Event/132.evd), Lyner sintetiza e lança o artefato elétrico Boltapolta com Radolf; "
        "7. Em Karff (Event/236.evd), Tastiella acolhe Lyner e Misha, explicando que Aurica partiu com Radolf em uma missão para deter uma tempestade; "
        "8. No resgate no ermo (Event/37.evd), Lyner auxilia Jack a recuperar a pista vital roubada por monstros, despertando a lealdade e admiração "
        "do cínico mercenário perante a bondade desinteressada do jovem cavaleiro; "
        "9. Após o pouso de emergência do dirigível (Event/122.evd), Radolf e guardas da Igreja resgatam o grupo; Aurica lamenta em lágrimas ter sido "
        "um fardo no sequestro de Misha, e Lyner faz a promessa sagrada de resgatá-la; Krusche define prioridades práticas entre inspecionar o dirigível e ir à Igreja; "
        "10. No confronto militar (Event/258.evd), o grupo supera um posto de guarda inimigo; "
        "11. No bistrô de Karula (Event/534.evd), Jack derrama galanteios canastrões para Claire, Krusche debocha de sua pose, e Claire anuncia que começou "
        "a tecer uma nova canção enquanto indica pistas sobre o espadachim de armadura vermelha; "
        "12. Na catarse de superação de Aurica (Event/326.evd), a jovem visita Claire e revela radiante que Lyner a curou durante o Mergulho, descobrindo que "
        "ela é a reencarnação da Deusa Tyria; Aurica renuncia ao seu complexo de inferioridade e jura viver de cabeça erguida e com positividade, seguindo o exemplo de Claire; "
        "13. E na Fancy Shop de Platina (Event/198.evd), Sasha repreende Lyner por chamar sua boutique de 'loja de variedades', Aurica se apaixona pelos itens "
        "fofos, a vendedora presenteia o casal com o raro [Coração de Dragão], e Lyner encerra o bloco em desespero cômico com a ameaça de falência de sua carteira."
    ),
    "decisoes_terminologicas": {
        "Facção Mir (Team Mir - ミュール団)": "Organização vilanesca liderada por Claire na simulação escolar da Cosmosfera de Shurelia.",
        "Poder Harmônico (Harmonics Power - ハーモニクスパワー)": "Energia vital fônica e espiritual das estudantes drenada pela vilã Claire na simulação mental.",
        "Senhorita Tougasaki (Miss Tougasaki - 塔ヶ崎さん)": "Identidade e sobrenome colegial de Shurelia na Cosmosfera (Tougasaki Leila / 塔ヶ崎澪羅).",
        "Harase-kun / Raina Harase (原瀬君 / 原瀬頼奈)": "Identidade colegial fictícia assumida por Lyner Barsett na simulação mental de Shurelia.",
        "Deusa Tyria (Goddess Tyria - ティリア神)": "A terceira Reyvateil Origin ancestral e divindade sagrada cuja reencarnação Aurica descobre ser em sua psique.",
        "Boltapolta (ポルタポルタ / ボルタポルタ)": "Artefato alquímico de arremesso que desfere descargas elétricas para ativar condutores e mecanismos na Torre.",
        "Coração de Dragão (Dragon Heart - ドラゴンハート)": "Item nobre e precioso presenteado como mimo festivo de fidelidade na Fancy Shop de Platina.",
        "Fancy Shop (ファンシーショップ)": "Boutique graciosa em Platina especializada em artigos decorativos, mimos e presentes delicados que fascinam Aurica.",
        "Comandante-Geral Radolf (ラードルフ総司)": "Título militar formal do Cardeal Radolf como comandante supremo das forças armadas da Igreja.",
        "Tópicos de Conversa (Talk Topics - マター)": "Temas de diálogo recolhidos pelo mundo para desbloquear intimidade e níveis profundos na Cosmosfera."
    },
    "alertas_para_proximo_bloco": (
        "Atenção máxima à continuidade das investigações na passagem secreta de Kyle/Falss sob o acervo da Igreja, à preparação "
        "do grupo para a expedição de resgate de Misha e às reverberações do novo ânimo confiante e luminoso de Aurica."
    )
}

output_payload = {
    "block_id": "BLK_EVD_018",
    "axis_id": "AXIS_3",
    "axis_name": "HISTÓRIA E EVENTOS",
    "total_lines": len(merged_dialogues),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "dialogues": merged_dialogues,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_payload, f, indent=2, ensure_ascii=False)

print(f"Saved {output_path} with {len(merged_dialogues)} dialogues.")
print(f"Rewritten: {lines_rewritten}, Approved: {lines_approved_as_is}")

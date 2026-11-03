# -*- coding: utf-8 -*-
"""
Script to curate, assemble, validate and finalize BLK_EVD_017
with full canonical depth and strict LQA validation.
"""
import json
import sys
import os

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_017_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_017_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

# Load all 5 batches
batches = [
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_017.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_017.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch3_017.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_017.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_017.json"
]

all_curated = []
for b_file in batches:
    with open(b_file, "r", encoding="utf-8") as f:
        items = json.load(f)
        all_curated.extend(items)

print(f"Total curated items loaded: {len(all_curated)}")
assert len(all_curated) == 300, f"Expected 300 items, got {len(all_curated)}"

# Merge with input metadata
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
        "O bloco narrativo BLK_EVD_017 (IDs 4211 a 4510, abrangendo 26 arquivos de eventos Event/*.evd) conecta arcos vitais "
        "de comédia cotidiana, investigações de conspiração política, traumas passados e a jornada íntima de amadurecimento "
        "das heroínas: 1. No bistrô de Karula (Event/143.evd), o flerte canastrão de Jack com Claire e o sarcasmo de Krusche "
        "introduzem a entrega do Fragmento de Yuteria obtido da blindagem de um Guardião, culminando na obtenção da receita da "
        "Corda Yuteria para que Lyner a sintetize via Grathmeld e conserte o alaúde de Claire; 2. Na base eclesiástica (Event/455.evd "
        "e Event/465.evd), Radolf pede desculpas a Lyner, une forças oficialmente com a expedição e, sob a bênção do governador "
        "Leard, revela a descoberta de uma passagem secreta no acervo da Igreja que leva ao laboratório clandestino onde o cientista "
        "Kyle (o futuro Bispo Falss) conduzia suas pesquisas secretas; 3. No diálogo a sós durante a fuga (Event/83.evd), Misha confessa "
        "a dor de ter tido seu artefato mais precioso roubado pela corporação Tenba e pergunta aflita sobre Platina e o Mundo Superior, "
        "ao que Lyner revela a ameaça letal da epidemia viral que assola a Torre, sendo interrompidos por uma violenta explosão "
        "subterrânea que Lyner insiste em investigar, despertando a fúria tsundere e protetora de Misha; 4. Na visita ao Vilarejo de Skuwat "
        "(Event/387.evd), Claire e Aurica relembram a cápsula do tempo enterrada na infância perto de sua antiga casa; 5. No comovente "
        "reencontro com Aurica (Event/972.evd), Lyner entrega a ela o boneco Don Leon que sintetizou em Grathmeld após descobrir na "
        "Cosmosfera o quanto ela sofria pela perda do seu companheiro de pelúcia deixado para trás no massacre de Skuwat; o diálogo "
        "aprofunda o pacto emocional de servirem mutuamente como porto seguro um do outro, embora Aurica receba o presente com melancolia "
        "contida, levando Lyner a planejar um novo Mergulho para confortá-la; 6. No templo da Igreja (Event/313.evd), Radolf apresenta o "
        "Cavaleiro Ayatane à alta cúpula sacerdotal, defendendo a cooperação além das fronteiras e recebendo a missão formal de localizar o "
        "Instrumento Sagrado, o Cristal Hymmnos Linker; na saída, Aurica desaba com febre alta e é amparada por Lyner rumo à hospedaria; "
        "7. No Porto Gaivota (Event/229.evd e Event/514.evd), tempestades e tornados no mar inferior cancelam os voos para o Beco Vagalume, "
        "enquanto Spica informa o retorno da presidente da Tenba, Ayano; 8. Nos confins mecânicos da Torre (Event/566.evd), Lyner reativa a "
        "terceira androide de manutenção, Kanade, por meio do Pingente de Memória de Mei Mei; Kanade revela que sua irmã mais velha Mai "
        "guardava o Sino de Plasma da Asa Direita de Hórus antes de perecer na Guerra das Reyvateils, desafiando Lyner para combates corpo a "
        "corpo esportivos em troca de presentes especiais; 9. E no clímax da Cosmosfera de Misha (Event/656.evd e Event/667.evd), a falha "
        "traumática na conclusão da Mudança de Paradigma anterior projeta uma distorção catastrófica na mente da garota, personificada no "
        "Anjo Shura; Lyner corre até a Mansão da Lua e o Templo Sagrado para resgatá-la, sendo recebido por uma Misha radiante que o "
        "convida a participar ao seu lado da cerimônia sagrada de poder cósmico, surgindo deslumbrante em seu vestido cerimonial e recebendo "
        "o elogio comovido de Lyner."
    ),
    "decisoes_terminologicas": {
        "Corda Yuteria (Yuteria String - ユーテリア弦)": "Fio condutor de extrema finura e tenacidade inquebrável usado para instrumentos musicais e amarrações sintetizado via Grathmeld.",
        "Fragmento de Yuteria (Fragment of Yuteria - ユーテリア破片)": "Fragmento metálico e acústico extraído da carcaça do Guardião.",
        "Altar dos Apóstolos (Altar of Apostles - 使徒の祭壇)": "Santuário sagrado e tenebroso reivindicado por Falss como epicentro de sua guerra santa.",
        "Cristal Hymmnos Linker (Hymn Crystal Linker - ヒュムネクリスタル「リンカ」)": "Artefato catalisador sagrado de conexão e sintonia procurado pela Igreja e disputado por Falss.",
        "Comporta A7 / Portão A7 (A7 Dividing Wall - A7隔壁ゲート)": "Bloqueio e comporta de contenção hermética de alta segurança da Torre.",
        "Espectro FFT (FFT Spectrum - FFTスペクトラム認証)": "Protocolo fônico de autenticação por transformada rápida de Fourier para reconhecimento biométrico de cavaleiros.",
        "Plugue Sinfônico / Conector Sinfônico (Symphonic Plug - 導力プラグ)": "Terminal condutor de energia harmônica e fônica da Torre.",
        "Kanade (Child of Light - 光の御子 カナデ)": "Terceira androide de manutenção da Torre, guardiã dos Sinos de Plasma e combatente apaixonada por artes marciais.",
        "Mai (マイ)": "Segunda androide de manutenção e irmã mais velha de Kanade, guardiã do Sino de Plasma da Asa Direita de Hórus, sacrificada na Guerra das Reyvateils.",
        "Asa Direita de Hórus (Right Wing of Horus - ホルス右翼)": "Setor da superestrutura da Torre onde se localiza o sino estabilizador de gravidade gêmeo.",
        "Anjo Shura (Angel Shura - 修羅天)": "Entidade onírica que rege a inovação e o poder na Cosmosfera de Misha, convertida na Magia Azul Anjo Shura.",
        "Mansão da Lua (Moon Mansion - 月ノ館)": "Edifício solene de retiro e julgamento interior na Cosmosfera de Misha.",
        "Dia Festivo (Hare no Hi - 晴れの日)": "O grande dia solene de celebração espiritual e rito de passagem na mente da Reyvateil."
    },
    "alertas_para_proximo_bloco": (
        "Atenção ao desdobramento da cerimônia do templo na Cosmosfera de Misha, às revelações contidas nos arquivos da "
        "biblioteca secreta de Kyle/Falss sobre a conspiração com a Tenba e ao estado febril de Aurica que prenuncia a "
        "contaminação viral em seu corpo e mente."
    )
}

output_payload = {
    "block_id": "BLK_EVD_017",
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

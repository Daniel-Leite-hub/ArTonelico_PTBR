# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

# Adiciona o diretório ao sys.path para importar os segmentos
cur_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(cur_dir))

from seg1 import segment1
from seg2 import segment2
from seg3 import segment3
from seg4 import segment4
from seg5 import segment5
from seg6 import segment6

all_segments = segment1 + segment2 + segment3 + segment4 + segment5 + segment6

print(f"Total curated lines assembled: {len(all_segments)}")

input_path = cur_dir / "blocos" / "BLK_EVD_045_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_dialogues = input_data["dialogues"]
print(f"Total input lines: {len(input_dialogues)}")

assert len(all_segments) == len(input_dialogues), f"Mismatch: {len(all_segments)} vs {len(input_dialogues)}"

output_dialogues = []
for cur, inp in zip(all_segments, input_dialogues):
    assert cur["id"] == inp["id"], f"ID mismatch: {cur['id']} vs {inp['id']}"
    
    text = cur["curated_ptbr"]
    notes = cur["curation_notes"]
    orig_en = inp.get("original_en", cur.get("original_en", ""))
    
    d_out = {
        "id": cur["id"],
        "original_en": orig_en,
        "custom_text": text,
        "pt_curated": text,
        "curated_ptbr": text,
        "review_status": "approved",
        "notes": notes,
        "curation_notes": notes
    }
    output_dialogues.append(d_out)

scene_handoff_final = {
    "resumo_dramatico": "O bloco BLK_EVD_045 articula três sequências de impacto decisivo: primeiro, no laboratório clandestino da Tenba, Bourd revela ter sobrevivido a Silvaplate e detalha seu plano eugênico de criar Reyvateils artificiais que funcionam como bonecas dóceis e sem sono. Ayano (Presidente da Tenba) intervém com autoridade soberana, condenando os experimentos em Reyvateils como tabu inaceitável e prometendo aliança plena a Lyner após Bourd fugir jurando ressuscitar Mir. Krusche identifica a instalação como um Sistema de Mergulho capaz de transferir matéria para dentro e fora de Reyvateils, explicando a cristalização da Chronicle Key. Em seguida, na Crônica Crescente, Hama revela a história trágica de Mir (a Reyvateil β Pura mais poderosa da história, selada por Shurelia num caixão sagrado). O despertar de Shurelia exige que Misha permaneça cantando a Chronicle Key perpetuamente para conter Mir. Diante da dor e do desabafo dilacerante de Misha ('Me abraça... Dói tanto ficar sozinha... Eu não quero isso...'), Lyner abraça a amiga e questiona para quem, afinal, foi feita aquela canção de sacrifício. Misha reafirma sua coragem, parte do grupo e assume seu posto sagrado, enquanto o grupo parte rumo ao Rinkernator. Por fim, na simulação colegial da Cosmosfera, Raina (Lyner) encontra Leila (Shurelia) amedrontada com suas memórias e seu papel como Anjo Cantor. Ele a conforta dizendo que apenas ama ver seu sorriso, leva-a ao seu humilde quarto de solteiro de tatame (onde ela abate uma barata/biohazard e cozinha para ele), combinando um encontro no Festival de Verão para ensiná-la a nadar e ver fogos de artifício, até serem interrompidos pela chegada surpresa de Orika (Aurica). Ao despertar, Shurelia envergonhada concede a Magia Vermelha [Apóstolo de Mir].",
    "decisoes_terminologicas": {
        "Cristal Hymmnos": "ヒュムネクリスタル (preservado como Cristal Hymmnos em conformidade com o glossário mestre)",
        "β Pura": "β純血種 (linhagem de sangue puro das Reyvateils)",
        "Crônica Crescente": "クレセントクロニクル (sarcófago sagrado e altar de Hama onde Mir repousa)",
        "Chronicle Key": "クロニクルキー (o Hino sagrado de selamento entoado por Misha)",
        "Vírus-Mãe Mir": "母なるウイルス「ミュール」 (matriz primordial dos vírus que ameaça a Torre)",
        "Sistema de Mergulho": "ダイブシステム (tecnologia ancestral de extração/inserção biológica e psicológica)",
        "Cantora das Estrelas": "星詠 (título cerimonioso de Misha em Platina e no templo)",
        "Raina Harase / Leila Togasaki": "原瀬頼奈 / 塔ヶ崎澪羅 (personas da simulação colegial na Cosmosfera de Shurelia)",
        "Orika": "織香 (persona colegial de Aurica na simulação de Shurelia)",
        "Anjo Cantor": "シンガーエンジェル (identidade de combate de Leila na Cosmosfera)",
        "Facção Mir": "ミュール団 (antagonistas da simulação na Cosmosfera)",
        "Tecer Magia Vermelha": "赤魔法を紡ぎ出した (verbo litúrgico canônico 'tecer')",
        "Apóstolo de Mir": "ミュールの使徒 (Magia Vermelha de invocação obtida na Cosmosfera)"
    },
    "alertas_para_proximo_bloco": "Com Misha estabelecida na Crônica Crescente cantando a Chronicle Key para manter o selo de Mir estável, o grupo de Lyner agora segue em direção ao Rinkernator para ressuscitar a Senhora Shurelia e reativar a Torre. Ao mesmo tempo, Bourd encontra-se em fuga tramando o colapso civilizatório e a liberação total da matriz viral."
}

new_terms = {
    "Apostle of Mir": {
        "pt": "Apóstolo de Mir",
        "category": "Magia da Canção / Invocação",
        "note": "Magia Vermelha (赤魔法【ミュールの使徒】) obtida na Cosmosfera de Shurelia após o evento romântico escolar."
    }
}

highlights = [
    "Confronto definitivo com Bourd no laboratório clandestino: desmascaramento do projeto da 'Próxima Geração de Reyvateils' e aliança formal com Ayano da Tenba.",
    "A revelação de Hama sobre a natureza de Mir como a maior Reyvateil β Pura da história e o sarcófago da Crônica Crescente.",
    "O clímax emocional de Misha na Crônica Crescente: o desabafo vulnerável ('Me abraça... Dói tanto ficar sozinha...'), o abraço de Lyner e o questionamento sobre o propósito da Chronicle Key.",
    "Saída de Misha do grupo e início da jornada em direção ao Rinkernator.",
    "Simulação colegial da Cosmosfera: encontro de Raina e Leila, a cena cômica e terna no apartamento com a barata/biohazard, o jantar caseiro, a promessa do festival de fogos de artifício e o flagra de Orika.",
    "Criação canônica da Magia Vermelha [Apóstolo de Mir] através do verbo 'tecer' (紡ぎ出した)."
]

output_data = {
    "block_id": "BLK_EVD_045",
    "axis_id": input_data.get("axis_id", "3_HISTORIA_E_EVENTOS"),
    "axis_name": input_data.get("axis_name", "História e Eventos"),
    "category": input_data.get("category", "História"),
    "line_count": len(output_dialogues),
    "dialogues": output_dialogues,
    "scene_handoff": scene_handoff_final,
    "scene_handoff_final": scene_handoff_final,
    "new_terms": new_terms,
    "highlights": highlights
}

output_path = cur_dir / "blocos" / "BLK_EVD_045_output.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Sucesso! Arquivo gravado em: {output_path}")

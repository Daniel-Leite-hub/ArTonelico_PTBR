# -*- coding: utf-8 -*-
"""
build_output_087.py - Geração de BLK_EVD_087_output.json e BLK_EVD_087_report.json
"""
import json
import datetime
from pathlib import Path

from data_blk087_part1 import LINES_PART1
from data_blk087_part2 import LINES_PART2

input_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_087_input.json")
output_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_087_output.json")
report_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_087_report.json")

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

all_curated = {}
all_curated.update(LINES_PART1)
all_curated.update(LINES_PART2)

assert len(all_curated) == 291, f"Expected 291, got {len(all_curated)}"

dialogues_out = []
for item in input_data["dialogues"]:
    item_id = item["id"]
    assert item_id in all_curated, f"Missing item {item_id}"
    curated_text, curation_note = all_curated[item_id]

    entry = {
        "id": item_id,
        "event_file": item["event_file"],
        "speaker_id": item["speaker_id"],
        "speaker": item["speaker"],
        "original_jp": item["original_jp"],
        "original_en": item["original_en"],
        "current_ptbr": item["current_ptbr"],
        "review_status": "approved",
        "ptbr_text": curated_text,
        "text_ptbr": curated_text,
        "curated_ptbr": curated_text,
        "final_ptbr": curated_text,
        "texto_ptbr_curado": curated_text,
        "custom_text": curated_text,
        "reviewed": True,
        "notes": curation_note,
        "curation_notes": curation_note,
        "curadoria_notes": curation_note
    }
    dialogues_out.append(entry)

scene_handoff = {
    "last_scene_id": "Event/803.evd",
    "last_line_id": 19807,
    "resumo_dramatico": (
        "O bloco BLK_EVD_087 consolida duas sequências dramáticas magistrais da mente e da Cosmosfera de Shurelia "
        "(Campo Binário/Linker), estruturadas sob a forma de uma comédia romântica/anime colegial que funciona como metáfora "
        "arquetípica de sua solidão milenar, de seu desejo de vivenciar a juventude humana e de seu amor transcendental por Lyner: "
        "(1) Em Event/785.evd, Lyner vagueia pela cidade da simulação em seu dia de folga e desiste de ir ao cinema ao ver o "
        "cartaz bizarro de «Teatro da Esposa Apaixonada». É interceptado por Aurica Motomiya, sua vizinha e amiga de infância grudenta "
        "e sem gosto estético, que tenta arrastá-lo para a sessão ou para compras no «Paraíso dos 100 Ienes». Após despachá-la com bom humor, "
        "Lyner decide tomar um chá sofisticado num café recém-inaugurado. Lá, ele é atendido pela desastrada garçonete Leila Togasaki "
        "(a persona de Shurelia), por quem se encanta à primeira vista. Enquanto ela serve o «Conjunto de Chá Dokkoi», Lyner tem uma crise "
        "de espirro incontrolável, assustando Leila e fazendo com que ela derrube o chá escaldante em sua calça. A gerente severa do café "
        "repreende Leila duramente e a obriga a acompanhar Lyner até a loja «UNI-Q» para comprar-lhe uma calça nova. Na caminhada, Leila resmunga "
        "do domingo arruinado, mas os dois trocam confidências sobre o propósito da vida («ikigai»), momento em que Leila menciona com melancolia "
        "que sua 'missão' consome sua existência. De repente, a cidade é atacada por um robô viral ELMA, cujo raio laser nocauteia todos os "
        "cidadãos. Aurica tenta fugir com Lyner, mas ele corre de volta para resgatar Leila no café destruído. Encurralados pelo robô que identifica "
        "'Shurelia' e aciona o Dispersor Sônico e o absorvedor harmônico, Leila pede para Lyner segurar sua mão em segredo. Ao tocarem as mãos, "
        "ambos se transformam em guerreiros cósmicos trajados para a batalha. O evento culmina num 'Game Over' simulado, devolvendo Lyner e a verdadeira "
        "Shurelia ao santuário do Mergulho, onde ela comenta divertida sobre os combates reais da simulação. "
        "(2) Em Event/803.evd, Lyner e Leila encontram-se para o festival noturno de verão (Nouryou-sai). Leila surge deslumbrante vestindo "
        "um yukata tradicional e revela que é a primeira vez que vai a uma celebração daquelas. Juntos, eles assistem maravilhados aos fogos "
        "de artifício que desenham cogumelos e planetas no céu. Em meio ao espetáculo, Leila faz uma confissão dilacerante: revela que não é humana, "
        "mas uma forma de vida programada — um vírus idêntico aos que o mundo odeia. Temendo que Lyner a rejeite e desejando que ele tenha um romance "
        "comum com uma garota normal, pede apenas que fiquem juntos até o final daquela noite feliz. Lyner aceita com ternura. Eles visitam as feirinhas "
        "da noite, comem algodão-doce e jogam pescaria de peixinho dourado (Kingyo-sukui), na qual Leila fracassa 28 vezes seguidas sem encostar em um "
        "único peixe por falta total de coordenação motora, para a comoção e consolo do dono da barraca. No caminho de volta, à margem da floresta, "
        "Leila pede a resposta final de Lyner. O jovem revela que já sabia de tudo através de Misha e faz uma declaração de amor eterna: o fato de ela "
        "não conhecer o mundo é uma bênção, pois ele quer descobrir cada alegria da vida ao lado dela, vendo-a rir, chorar de alegria e se apaixonar "
        "pelas pequenas coisas. Lyner jura que a salvará quantas vezes forem necessárias, mesmo que ela volte a ser um vírus. Comovida, Leila o chama "
        "carinhosamente de 'grande bobo' e sela seu pacto eterno («continue cuidando de mim»). Ao acordarem no santuário, Shurelia vincula os dados "
        "bélicos do autômato purificado, concedendo a Lyner a Magia Vermelha «ELMA-DS»."
    ),
    "decisoes_terminologicas": {
        "ELMA-DS": "赤魔法【ELMA-DS】 (Magia Vermelha ofensiva de Shurelia purificada)",
        "Leila Togasaki": "塔ヶ崎澪羅 (Togasaki Reira - Persona colegial de Shurelia na Cosmosfera)",
        "Lyner Harasett": "原瀬頼奈 (Harase Raina - Persona colegial de Lyner na Cosmosfera)",
        "Aurica Motomiya": "本宮織香 (Motomiya Orika - Persona vizinha e colega de Aurica na Cosmosfera)",
        "Festival de Verão": "納涼祭 (Nouryousai - festival noturno tradicional de verão com fogos e barracas)",
        "Pescaria de Peixinhos Dourados": "金魚すくい (Kingyo-sukui - tradicional jogo de festival com rede de papel poi)",
        "Dispersor Sônico": "ソニックバスター (Sonic Buster - disparo sônico do robô ELMA, corrigindo o erro da NISA 'Sonic scrambler')",
        "Conjunto de Chá Dokkoi": "ドッコイ紅茶セット (Dokkoi Koucha Set - serviço cerimonioso de chá da cafeteria)",
        "Paraíso dos 100 Ienes": "100えんパラダイス (Loja popular de variedades, adaptada pela NISA como Dollar-Rama)",
        "UNI-Q": "UNI-Q (Paródia da loja de departamentos japonesa UNIQLO)",
        "Ikigai": "生き甲斐 (Propósito e razão de viver, corrigindo o desvio da NISA sobre namorado)",
        "Raio Laser Paralisante": "ロボットの光線 (Raio emitido pelo robô, corrigindo a gafe bizarra da NISA 'beam that collapsed')",
        "Voltar": "戻らなきゃ (Preciso voltar, corrigindo o erro da NISA 'go round back')"
    },
    "alertas_para_proximo_bloco": (
        "Para os blocos seguintes (BLK_EVD_088 em diante), atentar para o episódio final da Cosmosfera de Shurelia "
        "(Nível 5 / Nível 6), a progressão do vínculo afetivo transcendente com Lyner, o retorno à realidade de Sol Ciel "
        "e a reinicialização da Torre via RE Nation."
    )
}

glossary_additions = {
    "ELMA-DS": {
        "pt": "Magia Vermelha «ELMA-DS»",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia Vermelha / Sistema de Batalha",
        "note": "赤魔法【ELMA-DS】 (Red Magic ELMA-DS). Magia de ataque obtida por Lyner na Cosmosfera de Shurelia ao purificar os dados bélicos do robô ELMA."
    },
    "Leila Togasaki": {
        "pt": "Leila Togasaki",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / Cosmosfera de Shurelia",
        "note": "塔ヶ崎澪羅 (Togasaki Reira). Persona estudantil e romântica de Shurelia em seu drama simulado da Cosmosfera."
    },
    "Lyner Harasett": {
        "pt": "Lyner Harasett",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / Cosmosfera de Shurelia",
        "note": "原瀬頼奈 (Harase Raina). Persona de colegial de Lyner no drama simulado da Cosmosfera de Shurelia."
    },
    "Aurica Motomiya": {
        "pt": "Aurica Motomiya",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / Cosmosfera de Shurelia",
        "note": "本宮織香 (Motomiya Orika). Persona vizinha e colega de infância de Aurica no drama da Cosmosfera de Shurelia."
    },
    "Festival de Verão (Nouryou-sai)": {
        "pt": "Festival de Verão",
        "gender": "masculino",
        "number": "singular",
        "category": "Cultura / Evento Festivo",
        "note": "納涼祭 (Nouryousai). Tradicional festival noturno japonês de verão com queima de fogos, barracas de comidas e jogos típicos."
    },
    "Pescaria de Peixinhos Dourados (Kingyo-sukui)": {
        "pt": "Pescaria de peixinho dourado",
        "gender": "feminino",
        "number": "singular",
        "category": "Costume / Minigame Cultural",
        "note": "金魚すくい (Kingyo-sukui). Brincadeira folclórica de festivais em que peixinhos dourados são recolhidos usando uma frágil redinha de papel chamada poi."
    },
    "Dispersor Sônico": {
        "pt": "Dispersor Sônico",
        "gender": "masculino",
        "number": "singular",
        "category": "Armamento / Habilidade Mecânica",
        "note": "ソニックバスター (Sonic Buster). Canhão sônico de alta frequência acoplado ao robô ELMA; NISA traduziu erroneamente como 'Sonic scrambler'."
    },
    "Conjunto de Chá Dokkoi": {
        "pt": "Conjunto de Chá Dokkoi",
        "gender": "masculino",
        "number": "singular",
        "category": "Culinária / Item da Cosmosfera",
        "note": "ドッコイ紅茶セット (Dokkoi Koucha Set). Serviço cerimonioso de chá da tarde servido no café da Cosmosfera de Shurelia."
    }
}

output_data = {
    "block_id": "BLK_EVD_087",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
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

print(f"Generated {output_path} with {len(dialogues_out)} lines.")

# Gerar report
now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
report_data = {
    "block_id": "BLK_EVD_087",
    "completed_at": now_iso,
    "total_dialogues": len(dialogues_out),
    "lines_rewritten": len(dialogues_out),
    "lines_approved_as_is": 0,
    "new_terms_added": len(glossary_additions),
    "scene_handoff": scene_handoff,
    "highlights": []
}

with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print(f"Generated {report_path}.")

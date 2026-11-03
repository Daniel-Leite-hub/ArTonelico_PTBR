import json
from datetime import datetime, timezone
from pathlib import Path

report_data = {
    "block_id": "BLK_SYS_041",
    "completed_at": datetime.now(timezone.utc).isoformat(),
    "total_dialogues": 288,
    "lines_rewritten": 285,
    "lines_approved_as_is": 3,
    "initial_overflows": 150,
    "final_overflows": 0,
    "hard_gate_status": "PASSED (100% OK)",
    "new_terms_added": 25,
    "scene_handoff": {
        "last_scene_id": "BLK_SYS_041",
        "last_line_id": 32132,
        "location_and_situation": "Núcleo Sistêmico Parte 41 (SLUS/TEXT/0505 a 0516: Conclusão das sessões de síntese e batismos de itens de oficina entre Lyner e Misha, e inauguração das sessões completas de síntese de Grathmeld com Lady Shurelia, cobrindo remédios arcaicos da Primeira Era, bombas de pressão e fragmentação, tecnologia ancestral da Torre e comédia refinada de deusa antiga) concluído com soberania do japonês, erradicação total dos 150 estouros de buffer legados (0 estouros restantes, 100% encoded_size <= original_bytes) e validação 100% limpa no Hard Gate Técnico.",
        "emotional_state": "Comédia de Oficina Encantadora, Transição Perfeita entre a Espontaneidade de Misha e a Dignidade Científica Serena de Shurelia, Eufonia e Rigor Técnico Impecáveis.",
        "active_hooks": [
            "Conclusão integral do bloco BLK_SYS_041 (IDs 31845 a 32132).",
            "Consolidação completa das sínteses de transição de Misha para Shurelia, preparando o terreno para os blocos subsequentes de síntese avançada de Shurelia e sistemas finais da Torre."
        ]
    },
    "highlights": [
        {
            "id": 31850,
            "theme": "Joia Ardel vs Cristal Científico (Misha & Lyner)",
            "jp": "いいじゃない。あと名前も「結晶体」なんて科学用語っぽいのじゃなくて「アーデルジュエリ」とかいかにも宝石っぽいのにしようよ。",
            "revised_ptbr": "E daí? Sem termos técnicos comoCR\"Cristal\". Vamos botar um nomeCRde joia, tipo \"Joias Ardel\"!"
        },
        {
            "id": 31908,
            "theme": "Pó de Polimento 'Pikarino' (Misha & Lyner)",
            "jp": "ねえねえ!CR「ピカリーノ」って名前にしない?お店に置いたら絶対売れる!売れそうな名前だもの!",
            "revised_ptbr": "Ei, ei! Que tal \"Pikarino\"?CRSe botar na loja, vende na hora!CRÉ nome que vende!"
        },
        {
            "id": 31973,
            "theme": "Ocarina Hama - Vínculo Afetivo de Infância e Protetora da Cosmosfera",
            "jp": "あ...「波摩」。",
            "revised_ptbr": "Ah... 'Hama'."
        },
        {
            "id": 31984,
            "theme": "Reconhecimento da Evolução de Lyner como Alquimista de Grathmeld",
            "jp": "ライナーもメルクとして成長したのよ。CR正直、出逢ったときは私の方が上だと思ったけど、今じゃ全然太刀打ちできないもの。",
            "revised_ptbr": "Você cresceu como Melk, Lyner!CRAgora não te alcanço mais!"
        },
        {
            "id": 32057,
            "theme": "Fullhealin D proibido na Primeira Era com Lyner de cobaia (Shurelia & Lyner)",
            "jp": "って、ちがーう!CRいや、身体に有害かどうかは昔の話とか、CRそういうのは関係ないじゃないですか!",
            "revised_ptbr": "Espera, NADA DISSO!CRFazer mal pro corpo não tem nadaCRa ver com ser coisa antiga!"
        },
        {
            "id": 32095,
            "theme": "Cata-vento Baku e Teoria CCP de Onda de Choque de Pressão",
            "jp": "これは「CCP風圧制御弾」と言って、気圧を極端に変化させて身体を膨張させて破裂させたりする武器ですよ。",
            "revised_ptbr": "É a \"Bomba Pressórica CCP\".CREla altera brutalmente a pressão do ar,CRfazendo o corpo inchar até estourar."
        },
        {
            "id": 32121,
            "theme": "Incensário Suíno de Mosquito - Humor Deadpan de Shurelia",
            "jp": "無駄ですよ。CRブタは取り払ってください。",
            "revised_ptbr": "Inútil. Por favor, removaCRa parte do porco."
        }
    ]
}

report_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_041_report.json")
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print(f"Wrote {report_path}")

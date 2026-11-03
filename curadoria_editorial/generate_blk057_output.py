# -*- coding: utf-8 -*-
"""
generate_blk057_output.py - Gera BLK_EVD_057_output.json com esquema integral e metadados.
"""
import json
import sys
import os

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_057_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_057_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Import curadoria de build_blk057
import build_blk057
curated = build_blk057.curated

dialogues_out = []
for item in input_data["dialogues"]:
    item_id = item["id"]
    pt_text, note = curated[item_id]
    
    entry = {
        "id": item_id,
        "event_file": item["event_file"],
        "speaker_id": item.get("speaker_id"),
        "speaker": item["speaker"],
        "original_jp": item["original_jp"],
        "original_en": item["original_en"],
        "curated_ptbr": pt_text,
        "final_ptbr": pt_text,
        "texto_ptbr_curado": pt_text,
        "custom_text": pt_text,
        "review_status": "approved",
        "reviewed": True,
        "notes": note,
        "curation_notes": note
    }
    dialogues_out.append(entry)

new_terms = {
    "Três Sábios": {
        "pt": "Três Sábios",
        "gender": "masculino",
        "number": "plural",
        "category": "Lore / Platina",
        "note": "3賢者 (Sankenja). Antigo triunvirato governamental e científico supremo de Platina formado por Shurelia, Kyle Clancy e Leard Barsett (ID 13435; traduzido na NISA como Three Magi)."
    },
    "RE Nation": {
        "pt": "RE Nation",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Hymmnos",
        "note": "リ・ネイション / EXEC_RE-NATION/.. Cristal Hymmnos ancestral primordial capaz de reiniciar os sistemas vitais da Primeira Torre e despertar Shurelia da suspensão criogênica (ID 13443)."
    },
    "Juramento de Elemia": {
        "pt": "Juramento de Elemia",
        "gender": "masculino",
        "number": "singular",
        "category": "Lore / Religião e Leis",
        "note": "エレミア誓約書 (Covenant of Elemia / Elemia Oath). Tratado solene ancestral firmado entre os povos de Sol Ciel que proíbe expressamente a ativação de tecnologia armamentista pesada e experimentos com Mir (ID 13452, 13459)."
    },
    "Comandante-Geral Radolf": {
        "pt": "Comandante-Geral Radolf",
        "gender": "masculino",
        "number": "singular",
        "category": "Título / Clero Militar",
        "note": "ラードルフ総司. Título militar máximo e formal do Cardeal Radolf como líder supremo dos Cavaleiros da Igreja de Elemia (ID 13488)."
    },
    "Don Leon": {
        "pt": "Don Leon",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / Cosmosphere",
        "note": "どんすけ (Donsuke). O bichinho de pelúcia dado por Claire a Aurica na infância que assumiu o papel de Guardião samurai de sua mente na Cosmosfera (ID 13366, 13408)."
    }
}

glossary_updates = {
    "terms_added": list(new_terms.keys()),
    "character_nuances": {
        "Kyle_Clancy": "Antigo terceiro membro dos Três Sábios de Platina, amigo de infância de Leard e cientista brilhante que cometeu o tabu supremo ao conspirar com Mir para deter a estagnação tecnológica do mundo.",
        "Leard_Barsett": "Revela sua faceta mais humana e vulnerável: a dor da traição de seu melhor amigo de infância (Kyle) e a nobreza de pedir perdão a Aurica pelas culpas negligentes de Platina.",
        "Don_Leon": "Guardião samurai pomposo e dedicado que recusa a subserviência cega e adverte Aurica de que estagnar na fraqueza infantil para não perdê-lo não é amor verdadeiro.",
        "Aurica": "Atinge maturidade emocional comovente: ressignifica seus traumas passados e a carência de infância, acolhendo seu amor incondicional por Lyner mesmo perante a perda temporária de sua Magia da Canção."
    }
}

scene_handoff_final = {
    "last_scene_id": "Event/444.evd",
    "last_line_id": 13497,
    "resumo_dramatico": "O bloco BLK_EVD_057 consolida arcos capitais de desenvolvimento emocional, revelações de lore ancestral e a grande virada de transição para a Fase 2 do roteiro: (1) Na cozinha de Claire em Nemo (Event/297.evd), Aurica protagoniza um interlúdio hilário e caloroso ao insistir em cozinhar para Lyner como agradecimento pelo seu esforço contínuo; apesar da técnica desastrada que quase decepa seus dedos e aterroriza Claire e Radolf com ingredientes atirados a esmo, a refeição resulta em uma alquimia caótica e viciante que Lyner devora no desespero e Radolf qualifica como 'sorte de outro mundo'. (2) No teste espiritual de Silvaplate (Event/542.evd), Hama confronta Lyner sobre a causa seminal de todos os conflitos humanos; perante a firmeza do cavaleiro em lutar pelo mundo, a guardiã se desfaz revelando-se como a sacerdotisa ancestral Tastiella, que profere seu conselho derradeiro sob o pranto dilacerado de Shurelia. No ramo hesitante, Hama repreende Lyner com severidade cirúrgica, denunciando que fugir do confronto não é bondade, mas fraqueza de convicção. (3) Na Cosmosfera de Aurica (Event/778 / Event/739.evd), Claire revela que o samurai Don Leon nasceu de uma pelúcia dada à heroína na infância em Skuwat para aplacar sua solidão; em um confronto dramático entre a projeção infantil de Aurica e a defensora onírica, desvenda-se o trauma central da garota: o medo de crescer e curar suas feridas, temendo que Don Leon deixe de existir se ela não for eternamente indefesa. O próprio Don Leon manifesta-se em sua glória samurai, recusando-se a respaldar a infantilização e partindo em protesto ético para ensinar à mestra a verdadeira coragem. (4) Nos subterrâneos tecnológicos de Platina (Event/444.evd), o Governador Leard revela a Lyner e Aurica a história esquecida dos 'Três Sábios' (Shurelia, Leard e Kyle Clancy); Leard expõe a dor de ver seu melhor amigo de infância corromper-se em arrogância científica contra o Juramento de Elemia, aliando-se a Mir e forjando seu falso suicídio para renascer no Mundo Inferior como o Bispo Falss. Com a Torre silenciada pelo Cântico Suspend para conter a proliferação viral, a única salvação reside no Cristal Hymmnos 'RE Nation', ocultado por Kyle no Mundo Inferior. Leard pede desculpas a Aurica pelo sofrimento infligido pela Igreja, e a jovem heroína o perdoa com serenidade lírica ao reconhecer que, sem aquela dor, jamais teria encontrado Lyner. Sentindo a Magia da Canção adormecer em suas veias com a suspensão da Torre, Aurica confessa seu desamparo, mas é reconfortada pelo juramento incondicional de proteção de Lyner, liberando a partida da comitiva para o Mapa-Múndi.",
    "decisoes_terminologicas": {
        "Três Sábios": "3賢者 (triunvirato histórico de Platina formado por Shurelia, Leard e Kyle; expurga a conotação mágica de Three Magi)",
        "RE Nation": "リ・ネイション (Cristal Hymmnos ancestral vital para reativar a Torre e acordar Shurelia)",
        "Suspend": "サスペンド (Cântico mestre de congelamento criogênico de sistema entoado por Shurelia)",
        "Juramento de Elemia": "エレミア誓約書 (tratado ancestral de segurança tecnológica que baniu experimentos com Mir)",
        "Comandante-Geral Radolf": "ラードルフ総司 (título canônico de Radolf perante a hierarquia militar dos Cavaleiros)",
        "Don Leon": "どんすけ (a pelúcia da infância de Aurica que se converteu em guardião samurai onírico)",
        "Mapa-Múndi": "ワールドマップ (área de navegação global desbloqueada após o diálogo com Leard)"
    },
    "alertas_para_proximo_bloco": "Com a Torre em suspensão de sistema, a Magia da Canção enfraquecida e o Mapa-Múndi liberado, a expedição parte para o Mundo Inferior em busca dos aliados dispersos (Radolf em Nemo, Krusche no Beco Vagalume, Jack e Misha rumo a Em Pheyna) para rastrear o Cristal Hymmnos RE Nation deixado por Kyle Clancy."
}

highlights = [
    {
        "id": 13321,
        "scene": "A Comédia Culinária de Aurica e a Coragem Desesperada de Lyner",
        "original_jp": "えーい!CRこうなりゃヤケクソだ!CRいただきます!!",
        "original_en": "Okay! Okay! I’ll eat it!",
        "curated_ptbr": "Ah, que seja! Agora vai no desespero!\nBom apetite!!",
        "rationale": "Resgate da oralidade vibrante e da impulsividade juvenil de Lyner. O japonês 'ヤケクソ' denota o desespero resignado de quem se atira ao perigo sem volta, achatado pela NISA em um insosso 'I’ll eat it'."
    },
    {
        "id": 13346,
        "scene": "A Despedida Espiritual e Fragmentada de Tastiella",
        "original_jp": "それが、私からあなたへの...最後の...アドバ...ス...",
        "original_en": "That is my final advice for you...",
        "curated_ptbr": "Este é... o meu último con... se... lho... para você...",
        "rationale": "Restauração da quebra vocal expressiva original (アドバ...ス... -> con... se... lho...), em que a guardiã ancestral se desfaz em partículas espirituais no instante em que pronuncia suas últimas palavras, totalmente ignorada pela NISA."
    },
    {
        "id": 13393,
        "scene": "Correção de Erro Crasso e Invenção da NISA na Hesitação de Aurica",
        "original_jp": "...ライナー。CRどうして止めるの?ライナーに止められたらあたし、迷いが出るじゃない...。",
        "original_en": "What are you doing? If you try to stop me, I’ll have to punish you first.",
        "curated_ptbr": "...Lyner.\nPor que está me impedindo? Se você ficar no meu caminho... eu vou acabar hesitando...",
        "rationale": "Correção de uma das maiores distorções da NISA: inventaram que Aurica queria 'punir Lyner primeiro' ('I'll have to punish you first'), quando o original expressa a fragilidade enternecedora da donzela, cuja convicção cega se desfaz em dúvidas e hesitação perante a presença amada de Lyner."
    },
    {
        "id": 13408,
        "scene": "A Nobreza Samurai de Don Leon e a Ética da Proteção Real",
        "original_jp": "そんなどんすけ...拙者ではない!!",
        "original_en": "What is the meaning of this?",
        "curated_ptbr": "Esse tal de Don Leon... em nada se parece com este humilde guerreiro!!",
        "rationale": "Restauração da persona épica e da dicção samurai de Don Leon (sessha / 拙者 / este humilde guerreiro), que a NISA achatou em um genérico 'What is the meaning of this?'. Don Leon questiona a infantilização de Aurica e recusa-se a ser cúmplice de sua fuga do amadurecimento."
    },
    {
        "id": 13435,
        "scene": "A Revelação Canônica dos Três Sábios de Platina",
        "original_jp": "シュレリア様、カイエル、CRそして私の3人は、その昔CR「3賢者」と呼ばれていた。",
        "original_en": "Lady Shurelia, Kyle, and I used to be called the [Three Magi].",
        "curated_ptbr": "A Senhora Shurelia, Kyle e eu\néramos chamados, outrora, de os 'Três Sábios'.",
        "rationale": "Estabelecimento canônico do triunvirato governamental e científico de Platina (3賢者), expurgando a conotação de magos arcanos da versão inglesa ('Three Magi') em um universo de ficção científica onde homens não manipulam magia, restrita às Reyvateils."
    },
    {
        "id": 13442,
        "scene": "O Equilíbrio Cósmico entre Suspend e RE Nation",
        "original_jp": "1つは私が持っていたCR「サスペンド」。CR塔を沈黙させる詩。CRそれが「リ・ネイション」と言われるもの。塔を再起動CRさせるクリスタルだ。",
        "original_en": "The one that I had was [Suspend]... There is another one called [RE Nation].",
        "curated_ptbr": "Um deles era o \"Suspend\", sob minha guarda:\no Cântico capaz de silenciar a Torre.\nO outro era o chamado \"RE Nation\":\no cristal capaz de reativar a Torre.",
        "rationale": "Alinhamento terminológico sagrado dos dois Cristais Hymmnos mestres que regem a vida e o sono criogênico da Primeira Torre Ar tonelico."
    },
    {
        "id": 13460,
        "scene": "O Credo Transumanista Radical e a Queda de Kyle Clancy",
        "original_jp": "進歩を諦めたら終わりです。文明が停滞した時点でそのCR世界の終焉です。",
        "original_en": "We should always strive toward progress. The world ends when a civilization stops advancing.",
        "curated_ptbr": "Renunciar ao progresso é o fim.\nNo instante em que uma civilização estagna, seu mundo caminha para a ruína.",
        "rationale": "Construção da densidade filosófica do antagonista, cuja justificativa para o pacto com Mir decorre do desprezo visceral pela tecnofobia e pelo estancamento civilizatório imposto pelo Juramento de Elemia."
    },
    {
        "id": 13493,
        "scene": "A Fragilidade de Aurica e o Voto de Companheirismo de Lyner",
        "original_jp": "ライナー。詩魔法の力...CRもう殆ど使えないから...CRあたし...CR...何言ってるんだよ。CR俺がついてるだろ。",
        "original_en": "My Song Magic hardly works at all now... / ...Don’t worry. I’m here with you.",
        "curated_ptbr": "Lyner... A força da Magia da Canção...\nquase não consigo mais usá-la... Eu...\n...Do que você está falando?\nEu estou com você, não estou?",
        "rationale": "O clímax afetivo do bloco: Aurica desmorona ao sentir a dormência de sua Magia da Canção após o desligamento da Torre, temendo ser um peso inútil; Lyner dissipa sua angústia afirmando seu afeto incondicional como protetor e parceiro."
    }
]

output_data = {
    "block_id": "BLK_EVD_057",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(dialogues_out),
    "id_range": [dialogues_out[0]["id"], dialogues_out[-1]["id"]],
    "dialogues": dialogues_out,
    "curated_lines": dialogues_out,
    "new_terms": new_terms,
    "glossary_updates": glossary_updates,
    "scene_handoff_final": scene_handoff_final,
    "highlights": highlights
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"[SUCESSO] BLK_EVD_057_output.json gerado com {len(dialogues_out)} falas em {output_path}!")

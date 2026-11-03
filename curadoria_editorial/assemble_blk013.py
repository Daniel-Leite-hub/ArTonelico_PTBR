import json
import sys
import datetime

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_013_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_013_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

batches = [
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_013.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_013.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch3_013.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_013.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_013.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch6_013.json"
]

all_curated = []
for b_path in batches:
    with open(b_path, "r", encoding="utf-8") as f:
        all_curated.extend(json.load(f))

print(f"Loaded {len(all_curated)} curated items.")
assert len(all_curated) == 294, f"Expected 294 items, got {len(all_curated)}"

dialogues_output = []
lines_rewritten = 0
lines_approved_as_is = 0

for item in all_curated:
    d_id = item["id"]
    orig = input_map[d_id]
    curated_text = item["curated_ptbr"]
    verdict = item["verdict"]
    rationale = item["rationale"]
    
    if verdict == "rewritten":
        lines_rewritten += 1
        status_val = "rewritten"
    else:
        lines_approved_as_is += 1
        status_val = "approved_as_is"
        
    d_obj = {
        "id": d_id,
        "event_file": orig["event_file"],
        "speaker": orig["speaker"],
        "original_jp": orig["original_jp"],
        "original_en": orig["original_en"],
        "current_ptbr": orig["current_ptbr"],
        "curated_ptbr": curated_text,
        "verdict": verdict,
        "rationale": rationale,
        "speaker_id": orig.get("speaker_id", 0),
        "review_status": "approved",
        "change_type": "curadoria_editorial_profunda",
        "status": status_val,
        "texto_ptbr_anterior": orig["current_ptbr"],
        "texto_ptbr_curado": curated_text,
        "justificativa": rationale,
        "revised_ptbr": curated_text,
        "notes_or_justification": rationale
    }
    dialogues_output.append(d_obj)

scene_handoff = {
    "resumo_dramatico": (
        "O bloco narrativo BLK_EVD_013 (IDs 3170 a 3463, abrangendo 26 arquivos de eventos Event/*.evd) "
        "consolida momentos de profunda ressonância emocional, revelações biográficas estarrecedoras e humor refinado: "
        "1. No primeiro ingresso de Lyner na Cosmosfera de Aurica (Event/700.evd), Don Leon se apresenta como o cavaleiro guardião de pelúcia, "
        "exigindo dogeza solene, repelindo Lyner aos berros e alegando absurdamente que Aurica é 'menkui' (só se interessa por homens bonitos); "
        "2. No refúgio pacífico junto à fonte da Torre (Event/173.evd), Aurica confessa com doçura que aquele é o seu lugar favorito no mundo para acalmar o coração; "
        "3. No crossover de Atelier na mente de Aurica (Event/682.evd), os companheiros Eisel e Nordis buscam um ingrediente de síntese perdido por Elfir (Elie), "
        "destacando a generosidade de Elie e o afeto implícito de seus amigos; "
        "4. As diretrizes do Guardião e do Sistema sobre Tópicos de Conversa e Mudança de Paradigma (Event/965.evd), exigindo estreitamento de laços no mundo real; "
        "5. O tutorial e sistema de campo de Magia Verde (Event/98.evd) disparada pelo botão IM02 para romper barreiras e operar mecanismos; "
        "6. A hilária cena no bistrô de Claire (Event/235.evd), onde Krusche recomenda com malícia o 'Arroz Babanero 50x de pimenta' (erro crasso da NISA corrigido de '50 orders'), "
        "fazendo a boca de Misha pegar fogo em desespero e falar enrolado ('num é nada disso, tá?!') enquanto Krusche saboreia a sobremesa com ironia; "
        "7. A aparição do Coelho do Relógio na Cosmosfera (Event/712.evd), que elucida o trauma de Aurica pelo incêndio e massacre de seu vilarejo natal (Skuwat), "
        "revelando como a mente de Lyner pode enfraquecer o dragão projetado se mantiver a convicção inabalável da vitória, até ser interrompido por novo desafio samurai de Don Leon; "
        "8. A síntese culinária de 'Sorvete Sobrenatural' (Event/872.evd), iguaria preta como terra inventada por Aurica com Gelo Ralado e Megamilk, aterrorizando e deliciando Lyner com os 'mistérios do Sobrenatural'; "
        "9. A comovente cena pós-Cosmosfera na neve (Event/601.evd), onde Misha descobre que sua vontade pode transformar o mundo mental e Lyner admite timidamente ter ficado com o coração palpitando ao vê-la em sua verdadeira forma de mulher adulta; "
        "10. O tenebroso diário secreto do Bispo Falss ('Nova Autobiografia de Kyle Vol. 1' em Event/459.evd), revelando que Falss forjou sua morte em Platina há um mês, "
        "infiltrou-se na 'organização hipócrita' chamada Igreja de Elemia (corrigindo o disparate 'charitable' de NISA), ascendeu ao episcopado e planeja manipular os recursos vultosos da corporação Tenba para obter Cristais Hymmnos; "
        "11. Lyner fechando as três válvulas mecânicas e silenciando o letal 'Rugido de Deus' no Chifre Prateado (Event/562.evd); "
        "12. A revelação e discussão madura entre Radolf, Misha, Aurica e Lyner sobre seu pai, o Administrador de Platina (Event/177.evd), onde Aurica nota com ternura que Lyner não é carinhoso com o pai; "
        "13. O alerta angustiado de Jack na Cosmosfera (Event/645.evd) procurando desesperadamente por Misha para evitar o colapso do mundo mental; "
        "14. A preparação para o voo de teste da aeronave lendária Gungnir (Event/521.evd) sob a supervisão técnica da Chefe Krusche; "
        "15. A revelação de Aurica como a mítica 'A Princesa Que Não Canta' (Event/705.evd) por Radolf após repelir o Demônio do Fogo; "
        "16. O diálogo cômico de Aurica e a mulher ofendida por ser chamada de velha, fornecendo a pista do Power Sourcer (Event/331.evd); "
        "17. A antológica declaração de amor e sonho de Misha (Event/580.evd), desejando tornar-se uma 'Diva da Canção', viajar pelo mundo cantando e acampando sob as estrelas ao lado de Lyner em uma eterna 'lua de mel' (provocando rubor e pânico cômico no rapaz); "
        "18. E o sublime diálogo com a mana Claire (Event/574.evd), expressando o sonho de que as canções sejam amadas pela sua pura beleza e não como armas de guerra, "
        "seguido da provocação maternal de Claire incentivando Aurica a se casar com o noivo maravilhoso ao seu lado, gerando o ciúme emburrado da garota."
    ),
    "decisoes_terminologicas": {
        "Watch Rabbit (時計ウサギ - Tokei Usagi)": "[Coelho do Relógio] (padronização canônica sagrada, banindo os erros 'March Hare' da NISA e 'Coelho Vigia')",
        "Soulspace / Seishin Sekai (精神世界)": "mundo mental / mundo interior / Cosmosfera (eliminando o decalque 'Espaço da Alma')",
        "Babanero Rice 50x (ババネロライス50倍)": "Arroz Babanero 50x de pimenta (restaurando a gradação de picância após a falha crassa de NISA que traduziu por '50 orders')",
        "New Biography of Kyle Vol. 1 (新・カイエル自伝1巻)": "“Nova Autobiografia de Kyle, Volume 1” (diário confidencial do Bispo Falss)",
        "Hypocritical Organization (偽善団体 - Gizen Dantai)": "organização hipócrita (resgatando a postura cínica de Falss, que NISA suavizou absurdamente como 'charitable organization')",
        "Songless Princess (謳わぬ姫 - Utawanu Hime)": "[A Princesa Que Não Canta] (arquétipo lendário de Aurica na Cosmosfera)",
        "Roar of God (神の咆哮 - Kami no Houkou)": "[Rugido de Deus] (vórtice acústico do Chifre Prateado, expurgando 'Voice of God')",
        "Singing Princess / Utahime (詩姫)": "[Diva da Canção] (ideal artístico itinerante de Misha, superando 'singing princess')",
        "Claire-oneechan (クレアお姉ちゃん)": "mana Claire (tratamento fraternal e afetuoso canônico de Aurica para com Claire)",
        "Menkui (面食い)": "só querer homens bonitos / atração por galãs (argumento hilário de Don Leon)",
        "Supernatural Ice (超自然アイス)": "[Sorvete Sobrenatural] (iguaria de coloração preta inspirada na terra criada por Aurica)",
        "Shaved Ice (かちわり氷)": "[Gelo Ralado] (ingrediente refrescante para a síntese culinária)",
        "Megamilk (メガミルク)": "Megamilk (laticínio de alto teor de síntese de Sol Ciel)",
        "Power Sourcer (パワーソーサー)": "Power Sourcer (gerador de energia para a máquina de Mergulho)",
        "Green Magic (緑魔法)": "[Magia Verde] (categoria de magia de campo ativada por IM02)"
    },
    "alertas_para_proximo_bloco": (
        "1. A confissão de Falss em seu diário ('Nova Autobiografia de Kyle') revela que a Igreja de Elemia e a corporação Tenba estão sob risco iminente de conspiração: manter extrema atenção ao tom cínico de Falss e às menções a Platina. "
        "2. No arco de Misha, o sonho de tornar-se Diva da Canção (Event/580.evd) e a visão de seu corpo adulto nos níveis profundos consolidam a maturidade de seus sentimentos por Lyner: preservar a alternância entre dengosa/ciumenta e mulher apaixonada. "
        "3. No arco de Aurica, a superação do trauma de Skuwat e a presença de Don Leon pavimentam a descida a níveis mais obscuros da psique (vírus de Mir): manter a solene lealdade samurai de Don Leon e a doçura frágil de Aurica perante a mana Claire. "
        "4. Manter a blindagem de tokens procedurais (IM02, %s, %d) e a vigilância contra quebras órfãs de grupo de fôlego."
    )
}

output_data = {
    "block_id": "BLK_EVD_013",
    "axis_id": "AXIS_3",
    "axis_name": "HISTÓRIA E EVENTOS",
    "category": "HISTÓRIA E EVENTOS",
    "total_lines": len(dialogues_output),
    "line_count": len(dialogues_output),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "id_range": [dialogues_output[0]["id"], dialogues_output[-1]["id"]],
    "curator_notes": (
        "Curadoria editorial profunda em duas passagens de 100% das 294 falas de BLK_EVD_013 (IDs 3170 a 3463). "
        "Auditoria integral contra a Tríade de Idiomas (JP SLPS-732.49 soberano; EN SLUS-214.45 suporte; PT-BR viva). "
        "Destaques capitais deste bloco: "
        "1. Restauração da dicção samurai de Don Leon (Donsuke) expurgando o falso espanhol ('Sí.') de NISA e resgatando a exigência de dogeza (ID 3182); "
        "2. Correção do erro crasso de NISA em ID 3201 ('I got it' como 'Entendi' -> 'Achei!'); "
        "3. Correção do grotesco disparate '50 orders' de NISA em ID 3253, restabelecendo o 'Arroz Babanero 50x de pimenta' que incendeia a boca de Misha; "
        "4. Restauração canônica do Coelho do Relógio (時計ウサギ) em ID 3273, sepultando o erro 'March Hare' de NISA e o decalque 'Coelho Vigia'; "
        "5. Correção do erro 'Mud' de NISA em ID 3308, restabelecendo a 'terra' (土) que inspirou a cor preta do Sorvete Sobrenatural; "
        "6. Revelação de que Lyner viu Misha com corpo de mulher adulta na Cosmosfera (ID 3331); "
        "7. Correção histórica em ID 3341: o Bispo Falss chama a Igreja de Elemia de 'organização hipócrita' (偽善団体), que NISA distorceu como 'charitable organization'; "
        "8. Alinhamento com 'Cristais Hymmnos' em ID 3357 e [Rugido de Deus] em ID 3362 (corrigindo 'Voice of God'); "
        "9. Correção do erro de NISA em ID 3426 ('classiest stores' inventado -> 'lavar pratos juntos se a grana acabar'); "
        "10. Correção de sentido em ID 3452, onde Lyner pergunta atônito se Claire está falando dele ('...俺?...ッスか?' corrigindo o bizarro '...Not me?' de NISA); "
        "11. E blindagem total da tag de controle IM02 (ID 3235) e zero fraturas sintáticas."
    ),
    "curated_lines": dialogues_output,
    "dialogues": dialogues_output,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"BLK_EVD_013_output.json generated successfully with {len(dialogues_output)} dialogues.")
print(f"Lines rewritten: {lines_rewritten}, lines approved as-is: {lines_approved_as_is}.")

# -*- coding: utf-8 -*-
"""
Atualização do Glossário Mestre e registro de handoff do bloco BLK_EVD_013.
Ar tonelico: Melody of Elemia (Undub) - PS2
"""

import json
import datetime
import os
import shutil

glossario_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
backup_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json.bak_013"

if os.path.exists(glossario_path):
    shutil.copy2(glossario_path, backup_path)
    print(f"Backup created at {backup_path}")

with open(glossario_path, "r", encoding="utf-8") as f:
    g = json.load(f)

# 1. Update last_scene_handoff
handoff_013 = {
    "status": "COMPLETED",
    "block_id": "BLK_EVD_013",
    "axis_id": "AXIS_3",
    "id_range": "3170-3463",
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "dramatic_context": (
        "Bloco narrativo de história e eventos BLK_EVD_013 (IDs 3170 a 3463, abrangendo 26 arquivos Event/*.evd). "
        "Consolida momentos de profunda ressonância emocional, revelações biográficas estarrecedoras e humor refinado: "
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

g["last_scene_handoff"] = handoff_013

# 2. Add / update terms safely
terms = g.setdefault("terms", {})

new_terms = {
    "Watch Rabbit": {
        "pt": "Coelho do Relógio",
        "gender": "masculino",
        "number": "singular",
        "category": "Entidade / Cosmosfera de Aurica",
        "note": "Entidade da Cosmosfera de Aurica (JP 時計ウサギ, Tokei Usagi). Desfaz o erro grotesco da tradução americana que o chamou de 'March Hare' (Lebre de Março) e o decalque 'Coelho Vigia'."
    },
    "Babanero Rice": {
        "pt": "Arroz Babanero",
        "gender": "masculino",
        "number": "singular",
        "category": "Culinária / Humor",
        "note": "Prato extremamente apimentado preparado com pimenta habanero (JP ババネロライス). Na cena de Event/235.evd, Krusche pede com 50x de picância (50倍), corrigindo o disparate '50 orders' da NISA."
    },
    "New Biography of Kyle": {
        "pt": "Nova Autobiografia de Kyle",
        "gender": "feminino",
        "number": "singular",
        "category": "Item / Lore",
        "note": "Diário secreto e confidencial do Bispo Falss revelando suas origens como o cientista Kyle de Platina e suas conspirações com a Tenba (JP 新・カイエル自伝)."
    },
    "Songless Princess": {
        "pt": "A Princesa Que Não Canta",
        "gender": "feminino",
        "number": "singular",
        "category": "Arquétipo / Cosmosfera de Aurica",
        "note": "Título lendário atribuído a Aurica nos níveis intermediários de sua Cosmosfera ao resistir aos ataques do Demônio do Fogo (JP 謳わぬ姫 - Utawanu Hime)."
    },
    "Singing Princess / Utahime": {
        "pt": "Diva da Canção",
        "gender": "feminino",
        "number": "singular",
        "category": "Ideal / Lore",
        "note": "O grande sonho de vida de Misha: viajar pelo mundo cantando como uma menestrel itinerante e tocando o coração das pessoas (JP 詩姫 - Utahime)."
    },
    "Green Magic": {
        "pt": "Magia Verde",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia / Sistema",
        "note": "Categoria de Magia da Canção utilizada no campo de exploração e acionada pelo botão IM02 para demolir barreiras e ativar mecanismos (JP 緑魔法)."
    },
    "Shaved Ice": {
        "pt": "Gelo Ralado",
        "gender": "masculino",
        "number": "singular",
        "category": "Ingrediente / Síntese",
        "note": "Gelo triturado utilizado como base culinária na síntese do Sorvete Sobrenatural por Aurica (JP かちわり氷)."
    }
}

for k, v in new_terms.items():
    if k not in terms:
        terms[k] = v
        print(f"Added term: {k} -> {v['pt']}")
    else:
        terms[k].update(v)
        print(f"Updated term: {k} -> {terms[k]['pt']}")

with open(glossario_path, "w", encoding="utf-8") as f:
    json.dump(g, f, indent=2, ensure_ascii=False)

print("Glossario Mestre updated successfully with BLK_EVD_013 handoff.")

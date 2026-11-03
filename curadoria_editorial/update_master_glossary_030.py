import json

GLOSSARY_PATH = "Ferramentas_Traducao/curadoria_editorial/glossario_mestre.json"

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

# Atualiza termos
new_terms = {
    "Altar of Apostles": {
        "pt": "Altar dos Apóstolos",
        "gender": "masculino",
        "number": "singular",
        "category": "Localização / Lore da Igreja",
        "note": "使徒の祭壇. Santuário sagrado ocupado pelos vírus onde Shurelia e Ayatane lutam exaustivamente para conter a dispersão energética."
    },
    "Purger": {
        "pt": "Purger",
        "gender": "masculino",
        "number": "singular",
        "category": "Hymn Crystal / Lore",
        "note": "パージャ. Cristal Hymmnos sagrado de purificação capaz de impedir a desmaterialização dos vírus em energia e erradicá-los."
    },
    "Demon Shadow": {
        "pt": "Demônio Sombra / Magia Vermelha [Sombra]",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia Vermelha / Invocação",
        "note": "魔神シャドウ / 赤魔法【魔神シャドウ】. Invocação mágica ofensiva tecida na conclusão do drama de Shurelia na Cosmosfera."
    },
    "Memory Pendant": {
        "pt": "Pingente de Memória",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Simulação Cósmica",
        "note": "メモリペンダント. Artefato simbólico que guardava a cópia do programa de Leila Togasaki na simulação escolar."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

# Atualiza address_matrix
if "Lyner" in glossary["characters"]:
    glossary["characters"]["Lyner"]["address_matrix"]["Leard"] = "Respeito filial firme, porém contestando vigorosamente a frieza e o tom intimidador do pai diante da vulnerabilidade das Reyvateils ('Pai!! Por que tem que intimidar a garota?!')."
    glossary["characters"]["Lyner"]["address_matrix"]["Shurelia (Leila)"] = "Vínculo romântico e transcendente na Cosmosfera ('eu só queria... passar mais um minuto, mais um segundo que fosse ao lado da Leila...'), valorizando os sentimentos vivos e a memória do coração acima de réplicas digitais."

if "Leard" in glossary["characters"]:
    glossary["characters"]["Leard"]["address_matrix"]["Lyner"] = "Tom austero, exigindo rigor militar supremo sem afrouxar a disciplina paternal ('O destino do mundo repousa sobre vocês. Não baixe a guarda nem por um instante')."
    glossary["characters"]["Leard"]["address_matrix"]["Aurica"] = "Autoridade de líder de estado, transferindo o peso esmagador da sobrevivência de Platina e do mundo ('O fracasso é inadmissível. Cante com toda a gravidade de seu coração')."
    glossary["characters"]["Leard"]["address_matrix"]["Misha"] = "Confiança estrita na Reyvateil Origin de Platina, exigindo prontidão absoluta sem espaço para deslizes ('Misha... Sendo você, tenho certeza de que cumprirá o dever')."

# Atualiza handoff
glossary["last_scene_handoff"] = {
    "resumo_dramatico": "A batalha de alta tensão no Altar dos Apóstolos, onde Lyner entrega o Purger para socorrer a Senhora Shurelia e Ayatane, culminando na purificação que encurrala os vírus e força uma invasão violenta na mente da heroína receptora (Aurica ou Misha), mergulhando-a em estado de coma; a reunião estratégica no gabinete de Platina com o Governador Leard Barsett, que cobra rigor implacável e designa uma das heroínas para a defesa da cidade; e a comovente conclusão do drama escolar na Cosmosfera de Shurelia, onde o sacrifício de Leila Togasaki contra Claire imortaliza a pureza do 'Omoi' (sentimento verdadeiro), levando Lyner ao luto profundo e à recusa filosófica do pingente de memória em prol das lembranças vivas do coração, culminando no despertar e na aquisição da Magia Vermelha [Sombra].",
    "decisoes_terminologicas": {
        "Altar dos Apóstolos": "[Altar dos Apóstolos] (使徒の祭壇, local sagrado de contenção dos vírus)",
        "Purger": "[Purger] (パージャ, cristal Hymmnos ancestral de erradicação viral)",
        "Sombra": "Magia Vermelha [Sombra] / Demônio Sombra (魔神シャドウ / 赤魔法【魔神シャドウ】)",
        "Pingente de Memória": "Pingente de Memória (メモリペンダント, suporte de backup de Leila)",
        "Omoi": "Sentimento / Anseio (想い, conceito filosófico de sentimentos vivos irredutíveis a programas)"
    },
    "alertas_para_proximo_bloco": "Atenção máxima ao deslocamento urgente para o Centro de Mergulho (Dive Shop) para adentrar a Cosmosfera da heroína em coma, expurgar o vírus invasor entranhado em seu âmago psíquico e estabilizar as defesas de Platina rumo ao desfecho."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print("Glossário Mestre atualizado com sucesso com os dados do bloco BLK_EVD_030!")

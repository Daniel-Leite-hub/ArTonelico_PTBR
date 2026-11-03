# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_058."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Espada Cortante": {
        "pt": "Espada Cortante",
        "category": "Magia da Canção / Combate",
        "note": "スラッシュソード (Sword Slash). Magia Vermelha de combate de Aurica que faz chover lâminas colossais sobre os inimigos, conjurada pelo monarca sombrio do Nível 7 e tecida após a vitória por Lyner (ID 13675, 13701)."
    },
    "Avenida Karakola": {
        "pt": "Avenida Karakola",
        "gender": "feminino",
        "number": "singular",
        "category": "Toponímia / Beco Vagalume",
        "note": "カラコラ通り (Karakola Ave.). Via urbana do Beco Vagalume por onde se desce para alcançar o ponto fraco estrutural no setor de força da cidade (ID 13592)."
    },
    "Símbolo da Razão": {
        "pt": "Símbolo da Razão",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosphere / Arquétipo",
        "note": "理性の象徴 (Symbol of Rationality). Título cerimonial e papel psíquico da personificação consciente de Aurica no Nível 7 de sua Cosmosfera (ID 13673)."
    },
    "Última Consciência": {
        "pt": "Última Consciência",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosphere / Estrutura Psíquica",
        "note": "最後の良心 (Final Conscience). O Nível 7 da Cosmosfera de Aurica, bastião final de sua sanidade moral antes do domínio total da faceta niilista (ID 13655)."
    },
    "Castelo do Rei Demônio": {
        "pt": "Castelo do Rei Demônio",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosphere / Localização",
        "note": "魔王城. Cidadela hostil erguida no Nível 7 da Cosmosfera de Aurica pela influência da Aurica Maligna com o objetivo de remodelar seu mundo psíquico (ID 13650)."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

# Atualização de nuances de personagens
if "characters" in glossary:
    if "Don_Leon" in glossary["characters"]:
        glossary["characters"]["Don_Leon"]["address_matrix"]["Lyner (Nível 7)"] = "Reconhecimento da maturidade e valor de Lyner após o duelo supremo, confiando-lhe fraternalmente a vida e o futuro de Aurica ('Lyner... você lutou muito bem... Cuide da Senhorita Aurica até o fim...')."
        glossary["characters"]["Don_Leon"]["address_matrix"]["Aurica (Sacrifício)"] = "Quebra do interdito mental supremo para interpor-se perante a Espada Cortante e salvar Aurica com o próprio corpo, jurando residir eternamente em seu coração."
    if "Lyner" in glossary["characters"]:
        glossary["characters"]["Lyner"]["address_matrix"]["Igreja de Hórus (Gratidão)"] = "Determinação moral e lealdade heroica ao recusar a busca geral para descer ao lado de Aurica e saldar sua dívida de honra com o Bispo Falss."

# Atualização de handoff
glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/748.evd",
    "last_line_id": 13701,
    "resumo_dramatico": "O bloco BLK_EVD_058 consolida a grande bifurcação de rotas da Fase 2 e momentos cruciais de desenvolvimento emocional e psicológico: (1) Em Platina (Event/214.evd), Shurelia convoca o grupo para definir os papéis na expedição ao Mundo Inferior. Ayatane decide permanecer lealmente ao lado de Shurelia para resguardar a Torre. Krusche junta-se à jornada oferecendo sua perícia como mecânica e piloto. Lyner então se depara com a grande encruzilhada: no Ramo A, opta por integrar a busca geral pelo Cristal Hymmnos RE Nation ao lado de Misha, recebendo o apoio compreensivo de Aurica; no Ramo B, honra a promessa de gratidão feita ao Bispo Falss, optando por descer ao lado de Aurica e Radolf para servir à Igreja que o acolheu ferido nas Asas de Hórus, sendo abençoado com serenidade por Shurelia e recebendo a aprovação sincera e comovida de Misha. Leard despede-se do filho com sua habitual rispidez paternal austera ('Trate de não morrer pelo caminho'). (2) No Beco Vagalume (Event/95.evd), Misha e Lyner procuram a comerciante Spica após o cancelamento de todos os voos de dirigível para Nemo. Mediante a senha secreta ('O preço não importa, eu quero é comer um balde inteiro'), Spica revela sua identidade como negociante do mercado clandestino de Cristais Grathnode e indica a vulnerabilidade estrutural oculta no setor de força descendo pela Avenida Karakola, onde uma parede remendada pode ser dinamitada para dar acesso aos dutos principais, cadastrando Lyner em seu circuito secreto de compradores. (3) Nos corredores da Torre (Event/109.evd), Krusche fascina-se com as ligas ancestrais de Yuteria e Airmetal, engajando-se em uma hilária e mordaz disputa com Misha por ciúmes de Lyner; o grupo é emboscado por Guardiões da Torre corrompidos por uma nova cepa viral do Campo Binário, levando Lyner a esclarecer a Krusche a ameaça em termos diretos enquanto as garotas trocam alfinetadas cômicas sobre capacidade explicativa e 'língua venenosa'. (4) Na Cosmosfera de Aurica (Event/748.evd), Lyner alcança o Nível 7 ('Última Consciência'), o bastião final da razão da heroína sob ataque do Castelo do Rei Demônio. A guia racional de Aurica revela que sua psique vem sendo corrompida pela Aurica Maligna. No confronto contra o lorde sombrio do castelo, o ataque de Aurica falha e ela está prestes a ser aniquilada pelo ataque 'Espada Cortante', quando o leal samurai Don Leon se interpõe com o próprio corpo, quebrando as regras da mente para cumprir seu juramento eterno de proteger Aurica. Don Leon comanda o contra-ataque de Lyner, que derrota o monarca demoníaco. Ferido de morte, Don Leon reconhece a nobreza de Lyner, confia-lhe a proteção definitiva de Aurica e consola sua chorosa criadora com serenidade antes de ser conduzido pelo grupo para descansar em uma pousada mental, tecendo para Aurica a Magia Vermelha definitiva [Espada Cortante].",
    "decisoes_terminologicas": {
        "Espada Cortante": "スラッシュソード (Canção mágica de combate de Aurica que invoca lâminas celestes; expurga a tradução genérica Golpe de Espada)",
        "Símbolo da Razão": "理性の象徴 (Título do arquétipo de racionalidade de Aurica no Nível 7)",
        "Última Consciência": "最後の良心 (O Nível 7 da Cosmosfera de Aurica, salvaguarda de sua sanidade)",
        "Avenida Karakola": "カラコラ通り (Via urbana do Beco Vagalume onde se localiza o acesso ao setor de força)",
        "Bala de Gato": "猫飴 (Guloseima e código de mercado clandestino de Spica)",
        "Yuteria e Airmetal": "ユーテリア / エアメタル (Materiais nobres ancestrais da arquitetura da Torre)"
    },
    "alertas_para_proximo_bloco": "Com a superação do Nível 7 da Cosmosfera de Aurica e o sacrifício heróico de Don Leon, a psique de Aurica consolida o vínculo protetor com Lyner; na realidade física, a rota pelo duto do setor de força no Beco Vagalume está desbloqueada rumo a Nemo e à busca do Cristal Hymmnos RE Nation."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"[SUCESSO] Glossário mestre atualizado em {GLOSSARY_PATH}")

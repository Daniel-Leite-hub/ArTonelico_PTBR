# -*- coding: utf-8 -*-
"""
generate_blk058_output.py - Gera o arquivo final BLK_EVD_058_output.json
"""
import json
from pathlib import Path
from scene1_data import scene1
from scene2_data import scene2
from scene3_data import scene3
from scene4_data import scene4

all_scenes = {}
all_scenes.update(scene1)
all_scenes.update(scene2)
all_scenes.update(scene3)
all_scenes.update(scene4)

input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_058_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_lines = input_data["dialogues"]
output_dialogues = []

for item in input_lines:
    item_id = item["id"]
    curated_text, curation_note = all_scenes[item_id]
    entry = {
        "id": item_id,
        "event_file": item["event_file"],
        "speaker_id": item.get("speaker_id"),
        "speaker": item.get("speaker"),
        "original_jp": item["original_jp"],
        "original_en": item["original_en"],
        "curated_ptbr": curated_text,
        "final_ptbr": curated_text,
        "texto_ptbr_curado": curated_text,
        "custom_text": curated_text,
        "review_status": "approved",
        "reviewed": True,
        "notes": curation_note,
        "curation_notes": curation_note
    }
    output_dialogues.append(entry)

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

glossary_updates = {
    "terms_added": list(new_terms.keys()),
    "character_nuances": {
        "Don_Leon": {
            "sacrificio_samurai": "Quebra as interdições psíquicas da mente e bloqueia com o próprio corpo a Espada Cortante para proteger Aurica, confiando-a solenemente aos cuidados de Lyner no Nível 7."
        },
        "Spica": {
            "fachada_e_submundo": "Vendedora de Balas de Gato do Beco Vagalume cuja verdadeira face é o tráfico de Cristais Grathnode raros e informações confidenciais acionadas por código secreto."
        }
    }
}

scene_handoff_final = {
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

highlights = [
    "Expurgo e correção dos erros crassos da NISA nas linhas 13517/13518 e 13551/13552, onde as saudações mútuas de parceria e cumplicidade ('よろしく') foram vertidas grotescamente como 'I owe you one' e 'Now we'll be even'.",
    "Correção de erro bizarro da NISA em 13684, onde Don Leon comanda o contra-ataque decisivo de Lyner ('貴様の出番だ! とっとと倒してこい!') e a NISA traduziu erroneamente como 'Run for your life' (fuga covarde).",
    "Resgate dramático da dor autêntica de Lyner em 13693 perante a agonia de Don Leon, corrigindo a frieza absurda da NISA ('Stop, you're embarrassing me').",
    "Correção de 13510, onde Shurelia acolhe Krusche com cordialidade e gratidão (corrigindo o disparate 'Please act responsibly' da NISA).",
    "Padronização canônica da Magia Vermelha [Espada Cortante] tecida por Aurica (ID 13701).",
    "Preservação integral da Tríade Canônica, ritmo cômico refinado nos bate-bocas entre Misha e Krusche, e blindagem sintática absoluta contra quebras de grupo de fôlego e pontuação órfã."
]

output_payload = {
    "block_id": "BLK_EVD_058",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(output_dialogues),
    "id_range": [13498, 13701],
    "dialogues": output_dialogues,
    "curated_lines": output_dialogues,
    "new_terms": new_terms,
    "glossary_updates": glossary_updates,
    "scene_handoff_final": scene_handoff_final,
    "highlights": highlights
}

output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_058_output.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_payload, f, indent=2, ensure_ascii=False)

print(f"[SUCESSO] BLK_EVD_058_output.json gerado com sucesso com {len(output_dialogues)} linhas!")

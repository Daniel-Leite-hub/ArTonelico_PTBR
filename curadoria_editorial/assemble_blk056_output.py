# -*- coding: utf-8 -*-
"""
assemble_blk056_output.py - Gera BLK_EVD_056_output.json e BLK_EVD_056_report.json com rigor técnico e editorial.
"""
import sys
import json
from datetime import datetime, timezone

sys.path.insert(0, r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial")
from curate_blk056 import CURATED

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_056_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_056_output.json"
report_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_056_report.json"
glossary_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

dialogue_list = []
rewritten_count = 0
as_is_count = 0

for item in input_data["dialogues"]:
    item_id = item["id"]
    cur_text, cur_note = CURATED[item_id]

    if cur_text.strip() == item.get("current_ptbr", "").strip():
        as_is_count += 1
    else:
        rewritten_count += 1

    entry = {
        "id": item_id,
        "event_file": item.get("event_file"),
        "speaker_id": item.get("speaker_id"),
        "speaker": item.get("speaker"),
        "original_jp": item.get("original_jp"),
        "original_en": item.get("original_en"),
        "curated_ptbr": cur_text,
        "final_ptbr": cur_text,
        "texto_ptbr_curado": cur_text,
        "custom_text": cur_text,
        "review_status": "approved",
        "reviewed": True,
        "notes": cur_note,
        "curation_notes": cur_note
    }
    dialogue_list.append(entry)

assert len(dialogue_list) == 198, f"Expected 198 dialogues, got {len(dialogue_list)}"

new_terms = {
    "Descent of Mir": {
        "pt": "Advento de Mir",
        "gender": "masculino",
        "number": "singular",
        "category": "Religião / Conspiração",
        "note": "ミュール光臨 (Myūru kōrin). Rito apocalíptico manipulado pelo Bispo Falss para ressuscitar a Rainha Viral Mir (ID 13183)."
    },
    "Technical Administrator": {
        "pt": "Administrador Técnico / Oficial Técnico",
        "gender": "masculino",
        "number": "singular",
        "category": "Cargo / Governo de Platina",
        "note": "技術政官 (Gijutsu seikan). Cargo de alto escalão do departamento científico de Platina exercido por Kyle Clancy antes de forjar a própria morte e adotar a identidade de Falss (ID 13188)."
    },
    "Exclusive Guardian": {
        "pt": "Guardião Pessoal / Guardião Dedicado",
        "gender": "masculino",
        "number": "singular",
        "category": "Mecânico / Torre",
        "note": "専属ガーディアン (Senzoku gādian). Autômatos de elite programados especificamente para a proteção individual da Senhora Shurelia e das instalações da Torre, como ELMA (ID 13166)."
    },
    "Grathnode Toxicity": {
        "pt": "Toxicidade dos Cristais Grathnode",
        "gender": "feminino",
        "number": "singular",
        "category": "Lore / Biologia de Reyvateil",
        "note": "グラスノ結晶の有害性 (Gurasuno kesshō no yūgai-sei). Condição fisiológica pela qual Cristais Grathnode causam dano e sobrecarga ao organismo da Reyvateil quando inseridos na Porta de Instalação, analogamente à ingestão de veneno para amplificar poder (ID 13252)."
    }
}

glossary_updates = [
    {
        "term_en": "Descent of Mir",
        "term_jp": "ミュール光臨",
        "term_ptbr": "Advento de Mir",
        "category": "Religião / Conspiração",
        "rationale": "Harmonização canônica com 'Advento do Trio de Elemia' (エレミア三謳神光臨), resgatando a manipulação eclesiástica de Falss (ID 13183)."
    },
    {
        "term_en": "Technical Administrator",
        "term_jp": "技術政官",
        "term_ptbr": "Administrador Técnico",
        "category": "Cargo / Governo de Platina",
        "rationale": "Denominação institucional exata do cargo exercido por Kyle Clancy em Platina, corrigindo o genérico 'official in the technical department' da NISA (ID 13188)."
    },
    {
        "term_en": "Exclusive Guardian",
        "term_jp": "専属ガーディアン",
        "term_ptbr": "Guardião Pessoal",
        "category": "Mecânico / Torre",
        "rationale": "Especificação da função de segurança autônoma dedicada à Senhora Shurelia (ID 13166)."
    },
    {
        "term_en": "Grathnode Toxicity",
        "term_jp": "グラスノ結晶は有害",
        "term_ptbr": "Toxicidade dos Cristais Grathnode",
        "category": "Lore / Biologia de Reyvateil",
        "rationale": "Conceito biológico fundamental que rege o dilema ético da mecânica de Instalação nas Reyvateils (ID 13252)."
    }
]

scene_handoff_final = {
    "resumo_dramatico": "O bloco BLK_EVD_056 atinge viradas decisivas na narrativa principal e no desenvolvimento afetivo dos protagonistas: (1) Diante da barreira intransponível que sela o Divisor FFT (Event/404.evd), Lyner demonstra bravura ao decidir atravessar o escudo letal suportando a descarga contínua com base exclusivamente na sua fé em Aurica. Aurica, superando seu complexo de inferioridade ao ouvir de Lyner que ele confia nela por ser quem é ('É por ser você, Aurica... que posso confiar com o coração tranquilo'), entoa a invocação de cura sagrada (#0Was yant ga exec heas lyner.) e regenera Lyner a cada segundo de agonia enquanto ele recupera o artefato. Logo em seguida, o guardião pessoal de Shurelia, ELMA, manifesta-se corrompido; após subjugá-lo, o grupo descobre que Mir moldou seus vírus em zombaria irônica à forma de ELMA. Lyner reafirma sua promessa de usar o Divisor FFT para arrancar Mir de Shurelia, partindo com os companheiros rumo ao topo da Torre. (2) Na chegada triunfal à Cidade Alta de Platina (Event/292.evd), Radolf prostra-se solenemente diante de Shurelia e do Governador Leard Barsett, oferecendo sua própria vida em expiação pela agressão desferida pelos fiéis corrompidos da Igreja. Leard ordena com firmeza paterna que Radolf erga a cabeça, revelando que o mentor da invasão foi o falso Bispo Falss — cuja verdadeira identidade é Kyle Clancy, um antigo administrador técnico de Platina tido como morto que conspirou nas Asas de Hórus. Leard e Shurelia absolvem a Igreja, louvando o grupo pela recuperação da Chave da Crônica. Enquanto Ayatane e Lyner celebram o reencontro e Leard mantém sua rigidez austera contra a vaidade do filho, Shurelia expressa sua gratidão mais profunda e reverente a Lyner. Aurica celebra o sacrifício de Misha em Em Pheyna e jura visitá-la como sua salvadora. Radolf mobiliza os cavaleiros para a reconstrução, mas Shurelia sucumbe à exaustão extrema da batalha anterior e pede licença para se retirar com o apoio de Ayatane. Aurica reintegra-se ao grupo. (3) No Dive Shop / Portão (Event/955.evd), o atendente fica impressionado com a profundidade do Mergulho alcançada por Lyner na mente de Misha e questiona se já realizaram a 'Instalação'. A pergunta deixa Misha em pânico pudico e envergonhada, repreendendo Lyner por sua ingenuidade. Ao ouvir a explicação técnica de que a Instalação consiste em introduzir Cristais Grathnode diretamente no corpo da Reyvateil — o que potencializa seus hinos mas a fere por ser uma substância nociva comparável à ingestão de veneno —, Lyner recusa-se categoricamente a machucar Misha de forma tão cruel, comovendo a parceira em silêncio antes de seguirem o conselho de conversar com calma na estalagem.",
    "decisoes_terminologicas": {
        "Divisor FFT": "FFTディバイダ (componente tecnológico fundamental recuperado do santuário sob o campo de força)",
        "ELMA": "エルマ / ELMA (guardião mecânico autônomo de base branca pessoalmente concebido por Shurelia)",
        "Kyle Clancy": "カイエル・クランシー / カイエル (identidade real do falso Bispo Falss, antigo administrador técnico de Platina)",
        "Administrador Técnico": "技術政官 (cargo de liderança científica outrora ocupado por Kyle em Platina)",
        "Advento de Mir": "ミュール光臨 (termo sacrílego forjado por Falss para a ressurreição da Rainha Viral)",
        "Asas de Hórus": "ホルスの翼 (setor estrutural suspenso da Torre onde Kyle se refugiou em segredo)",
        "Instalação": "インストール (procedimento de inserção de Cristais Grathnode na Porta de Instalação da Reyvateil)",
        "Chave da Crônica": "クロニクルキー (Cristal Hymmnos ancestral recuperado pela expedição de Lyner)"
    },
    "alertas_para_proximo_bloco": "Com o Divisor FFT recuperado e a autorização formal do Governador Leard obtida em Platina, a expedição prepara-se para a ofensiva decisiva de libertação de Shurelia e aprofundamento das camadas íntimas da Cosmosfera, enquanto a decisão sobre a realização da Instalação fica pendente de conversa na estalagem."
}

highlights = [
    {
        "id": 13128,
        "scene": "A Cura e a Confiança Incondicional de Lyner em Aurica",
        "original_jp": "オリカだから...CR安心して頼めるんだ。",
        "original_en": "I trust you. That’s why I’m asking you to do this.",
        "curated_ptbr": "É por ser você, Aurica...\nque posso confiar com o coração tranquilo.",
        "rationale": "Resgate dramático essencial sobre a versão genérica da NISA ('I trust you'). O japonês 'オリカだから...' expressa que a confiança de Lyner nasce do valor único e intrínseco de Aurica, curando a sensação constante de inferioridade da jovem."
    },
    {
        "id": 13129,
        "scene": "A Epifania Emocional de Aurica",
        "original_jp": "あたし...だから?",
        "original_en": "You...trust me?",
        "curated_ptbr": "Por ser... eu?...",
        "rationale": "Restauração da resposta espelhada de Aurica ('あたし...だから?'), achatada pela NISA. A surpresa enternecida de Aurica vem do fato de ser escolhida e valorizada por sua própria identidade."
    },
    {
        "id": 13133,
        "scene": "Invocação Sagrada de Cura em Hymmnos",
        "original_jp": "#0Was yant ga exec heas lyner.",
        "original_en": "#0Was yant ga exec heas lyner.",
        "curated_ptbr": "#0Was yant ga exec heas lyner.",
        "rationale": "Restauração inegociável do verso de Hymmnos executado por Aurica para curar o corpo de Lyner enquanto ele é consumido pelo campo de força, que estava totalmente em branco no arquivo de entrada preliminar."
    },
    {
        "id": 13142,
        "scene": "Correção de Erro Crasso da NISA na Fuga do Escudo",
        "original_jp": "今...出る...",
        "original_en": "I’m...leaving now...",
        "curated_ptbr": "Já... estou saindo...",
        "rationale": "Correção da tradução risível da NISA ('I’m leaving now' -> 'vou embora agora'): Lyner está escapando e saindo de dentro da redoma elétrica do escudo, não 'partindo para uma viagem'."
    },
    {
        "id": 13166,
        "scene": "A Revelação Canônica do Guardião ELMA",
        "original_jp": "確か、シュレリア様専属のCRガーディアン。CR『ELMA』っていうの。",
        "original_en": "I think it’s called [ELMA], one of Lady Shurelia’s guardians.",
        "curated_ptbr": "Se não me engano, é o guardião pessoal\nda Senhora Shurelia. O nome dele é ELMA.",
        "rationale": "Preservação da lore canônica de Sol Ciel: identificação de ELMA como autômato sagrado de Shurelia, alinhando a grafia sem acionar falso positivo de controle procedurais."
    },
    {
        "id": 13175,
        "scene": "A Nobreza Trágica e Expiação de Radolf",
        "original_jp": "多数の怪我人、CRそして甚大なる被害、CRこの詫びは私の命をもって...",
        "original_en": "They hurt many people and damaged Platina severely. To atone for their sins, I must offer you my life...",
        "curated_ptbr": "Com tantos feridos e tamanha devastação material...\nofereço minha própria vida em expiação a esse pecado...",
        "rationale": "Elevação solene da dicção cavaleiresca de Radolf diante do líder de Platina, expurgando simplificações coloquiais da localização ocidental."
    },
    {
        "id": 13187,
        "scene": "O Desmascaramento de Falss como Kyle Clancy",
        "original_jp": "ファルスと名乗っていた男の本名はカイエル。",
        "original_en": "Falss wasn’t his real name. His real name is Kyle Clancy.",
        "curated_ptbr": "O indivíduo que atendia por Falss\nse chama na verdade Kyle.",
        "rationale": "Revelação do plot twist político de Sol Ciel: Leard desmascara a farsa do falso bispo, conectando sua trajetória ao governo tecnológico de Platina."
    },
    {
        "id": 13242,
        "scene": "A Provocação do Dive Shop sobre o Pudor de Misha",
        "original_jp": "おや、CRまだやってなかったのか?CR意外とガード堅いんだねぇ。",
        "original_en": "Oh, you haven’t? Why don’t you give him a chance?",
        "curated_ptbr": "Ora essa...\nAinda não fizeram?\nQuem diria que você mantinha uma guarda tão firme, mocinha!",
        "rationale": "Correção do erro interpretativo da NISA ('Why don’t you give him a chance?'): o japonês 'ガード堅い' refere-se explicitamente ao recato, prudência e reserva defensiva de Misha diante de procedimentos íntimos."
    },
    {
        "id": 13253,
        "scene": "A Metáfora Visceral da Instalação e o Dilema de Lyner",
        "original_jp": "毒を喰らってパワーアップCRするようなモノだ。",
        "original_en": "It’s kind of like increasing your power by taking poison.",
        "curated_ptbr": "É basicamente como se fortalecer\ningerindo veneno.",
        "rationale": "Impacto dramático da biologia das Reyvateils: a cristalização como um fardo tóxico que Lyner recusa terminantemente a impor à amiga de infância."
    }
]

output_data = {
    "block_id": "BLK_EVD_056",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(dialogue_list),
    "id_range": [dialogue_list[0]["id"], dialogue_list[-1]["id"]],
    "dialogues": dialogue_list,
    "curated_lines": dialogue_list,
    "new_terms": new_terms,
    "glossary_updates": glossary_updates,
    "scene_handoff_final": scene_handoff_final,
    "highlights": highlights
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Output successfully written to {output_path} with {len(dialogue_list)} dialogues.")

# Gerar relatório de curadoria
report = {
    "block_id": "BLK_EVD_056",
    "completed_at": datetime.now(timezone.utc).isoformat(),
    "total_dialogues": len(dialogue_list),
    "lines_rewritten": rewritten_count,
    "lines_approved_as_is": as_is_count,
    "new_terms_added": len(new_terms),
    "scene_handoff": scene_handoff_final,
    "highlights": highlights
}

with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(f"Report successfully written to {report_path}.")

# Atualizar o Glossário Mestre
with open(glossary_path, "r", encoding="utf-8") as f:
    glossary = json.load(f)

for term, data in new_terms.items():
    glossary.setdefault("terms", {})[term] = data

glossary["last_scene_handoff"] = scene_handoff_final

with open(glossary_path, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print(f"Glossary successfully updated with BLK_EVD_056 handoff and terms in {glossary_path}.")

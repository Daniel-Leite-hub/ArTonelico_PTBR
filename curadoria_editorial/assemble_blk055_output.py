# -*- coding: utf-8 -*-
"""
assemble_blk055_output.py - Gera BLK_EVD_055_output.json e BLK_EVD_055_report.json com rigor técnico e editorial.
"""
import sys
import json
from datetime import datetime, timezone

sys.path.insert(0, r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial")
from curate_blk055 import CURATED

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_055_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_055_output.json"
report_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_055_report.json"
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

assert len(dialogue_list) == 190, f"Expected 190 dialogues, got {len(dialogue_list)}"

new_terms = {
    "Circula Baptism": {
        "pt": "Batismo de Circula",
        "gender": "masculino",
        "number": "singular",
        "category": "Rito / Tecnologia da Torre",
        "note": "サーキュラの洗礼 (Sākyura no senrei). Ritual sagrado de transição de fase onde os corpos são temporariamente convertidos em dados/alma para ascender à região superior da Torre (Platina) através do artefato Circular (ID 12924)."
    },
    "Upper Realm of the Tower": {
        "pt": "Topo da Torre / Parte Superior da Torre",
        "gender": "masculino",
        "number": "singular",
        "category": "Localização / Geografia da Torre",
        "note": "塔の上側 (Tō no uegawa). O platô e as estruturas sagradas suspensas no alto da atmosfera onde repousam a cidade de Platina e o Altar dos Apóstolos (ID 12960)."
    },
    "Chains of the Heart": {
        "pt": "Correntes do coração",
        "gender": "feminino",
        "number": "plural",
        "category": "Cosmosfera / Psicologia",
        "note": "心のクサリ (Kokoro no kusari). Barreira psicológica inconsciente que restringe a autonomia afetiva de uma Reyvateil quando ela suprime repetidamente seus verdadeiros anseios íntimos (ID 13084)."
    },
    "Singing Doll": {
        "pt": "Boneca de cantar",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Lore de Reyvateil",
        "note": "謳う人形 (Utau ningyō). Metáfora de desumanização e sofrimento usada por Misha ao lamentar o confinamento forçado desde a infância para entoar hinos ininterruptamente (ID 13061)."
    },
    "Spirit of Song": {
        "pt": "Ninfa dos hinos / Fada dos hinos",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Mitologia",
        "note": "詩の精 (Uta no sei). Entidade e arquétipo mítico de Reyvateil que personifica a magia cantada e o sacrifício pela vida alheia (ID 13064)."
    }
}

glossary_updates = [
    {
        "term_en": "Circula Baptism",
        "term_jp": "サーキュラの洗礼",
        "term_ptbr": "Batismo de Circula",
        "category": "Rito / Tecnologia da Torre",
        "rationale": "Ritual de ascensão da Torre padronizado canonicamente como [Batismo de Circula] (ID 12924)."
    },
    {
        "term_en": "Upper Realm of the Tower",
        "term_jp": "塔の上側",
        "term_ptbr": "Topo da Torre",
        "category": "Localização / Geografia da Torre",
        "rationale": "Designação geográfica exata do destino do portal de Tastiella em direção a Platina (ID 12960)."
    },
    {
        "term_en": "Chains of the Heart",
        "term_jp": "心のクサリ",
        "term_ptbr": "Correntes do coração",
        "category": "Cosmosfera / Psicologia",
        "rationale": "Conceito estrutural da psique de Misha sobre os bloqueios do inconsciente (ID 13084)."
    },
    {
        "term_en": "Singing Doll",
        "term_jp": "謳う人形",
        "term_ptbr": "Boneca de cantar",
        "category": "Cosmosfera / Lore de Reyvateil",
        "rationale": "Expressão dramática do trauma de isolamento institucional de Misha em Platina (ID 13061)."
    },
    {
        "term_en": "Spirit of Song",
        "term_jp": "詩の精",
        "term_ptbr": "Ninfa dos hinos",
        "category": "Cosmosfera / Mitologia",
        "rationale": "Arquétipo poético resgatado do texto japonês e omitido na localização da NISA (ID 13064)."
    }
]

scene_handoff_final = {
    "resumo_dramatico": "O bloco BLK_EVD_055 atinge pontos culminantes na narrativa de amadurecimento coletivo, libertação psicológica e purificação espiritual: (1) Em Karff / Templo de Tastiella (Event/170.evd), a expedição se reúne diante de Tastiella para realizar o solene 'Batismo de Circula' rumo à parte superior da Torre e a Platina. Lyner, atormentado pelo medo de colocar os amigos em perigo mortal num caminho sem volta, tenta seguir sozinho. O grupo reage com maturidade e firmeza: Radolf repreende sua falta de fé nos laços da equipe, Jack condena a soberba protetora e Misha, às lágrimas, confronta o altruísmo unilateral de Lyner, cobrando empatia real e lembrando como ele hesitou em convidá-la para o Mergulho. Jack ministra a lição definitiva: cuidar de alguém exige respeitar aquilo que a pessoa preza mais que a própria vida. Lyner aceita a lição, e Tastiella entoa o comando Hymmnos sagrado (#0Ma nam ra flip...) que abre o portal de luz. Em confidência solene a sós, Jack jura a Tastiella que recuperará o Hino perdido de Misha. (2) Na Cosmosfera de Aurica (Event/191.evd), o grupo adentra um cenário de desolação absoluta deixado pelos vírus. Don Leon alerta em pânico que Aurica foi cristalizada por um monstro alienígena. Ao alcançarem a estrutura, os heróis deparam-se com Aurica possuída: os vírus proclamam que os humanos são a verdadeira praga e que eles são os guardiões das Reyvateils. A consciência pura de Aurica quebra o transe em prantos de terror antes de ser sufocada de novo. No limite do desespero, a Senhora Shurelia intervém diretamente dos núcleos da Torre, entoando Hymmnos ancestral (#0Wee i ga flip...) para romper o vínculo com o hospedeiro. Lyner e o grupo aniquilam os vírus, o mundo mental renasce em verde exuberante e Aurica expressa o calor inédito de ter companheiros ao seu lado. (3) Na Cosmosfera de Misha (Event/606.evd), Misha enfrenta sua angústia existencial sobre o confinamento eterno em Platina e o fardo de ser apenas um autômato de cantar. Ela decide com nobreza abrir mão de sua liberdade imediata para salvar a vida de Krusche. Sua manifestação psicológica inconsciente surge das sombras para tentá-la a tomar o remédio de Yakuan e tornar-se humana. Enquanto o ramo virtuoso solidifica a compaixão de Misha (embora alertando para as 'correntes do coração' reprimidas), o ramo de falha expõe o desfecho trágico em que Misha sucumbe ao cinismo e à amargura, expulsando Lyner para a escuridão do abismo mental por sua falta de empatia no cotidiano.",
    "decisoes_terminologicas": {
        "Batismo de Circula": "サーキュラの洗礼 (ritual sagrado de transição de fase com o artefato Circular para cruzar para Platina)",
        "Yakuan": "薬庵 (eremita e boticário excêntrico da Cosmosfera de Misha que produz o remédio para transformação humana, desmistificando o erro 'shaman' da NISA)",
        "Correntes do coração": "心のクサリ (amarras e travas do inconsciente de uma Reyvateil na Cosmosfera)",
        "Senhora Shurelia": "シュレリア様 (tratamento respeitoso e solene do protagonista à deusa/administradora)",
        "Topo da Torre": "塔の上側 (região superior da Torre acima do mar de nuvens onde Platina está situada)",
        "Ninfa dos hinos": "詩の精 (entidade mística associada à dádiva de cantar hinos)"
    },
    "alertas_para_proximo_bloco": "Com a travessia pelo Batismo de Circula concluída e o vírus na mente de Aurica completamente erradicado com auxílio de Shurelia, a narrativa avança para a chegada decisiva a Platina e a continuidade das camadas mais profundas da Cosmosfera de Misha, lidando com a administração do remédio de Yakuan e a cura de Krusche."
}

highlights = [
    {
        "id": 12933,
        "scene": "O Confronto de Misha contra o Heroísmo Solitário de Lyner",
        "original_jp": "わからないの?CRみんながっかりしてるのよ...。",
        "original_en": "Don’t you get it? You’re pissing everybody off!",
        "curated_ptbr": "Você não percebe?!\nTá todo mundo decepcionado com você!...",
        "rationale": "Correção do decalque agressivo e vulgarizado da NISA ('pissing everybody off'). O original japonês 'みんながっかりしてるのよ' expressa a mágoa e a decepção profunda dos companheiros com a falta de confiança de Lyner no grupo."
    },
    {
        "id": 12951,
        "scene": "A Sabedoria Afetiva de Jack sobre Cuidar de Alguém",
        "original_jp": "ホントに相手のことを考えるってのはな、一方的に心配CRするだけじゃダメなんだぜ。",
        "original_en": "If you really care about someone, you can’t just worry about them. You have to consider their feelings, too.",
        "curated_ptbr": "Pensar de verdade no outro, moleque,\nnão é só ficar se preocupando de forma unilateral.",
        "rationale": "Momento de ouro de mentoria emocional de Jack: ensina a Lyner que amar e respeitar alguém exige reconhecer a autonomia e os valores sagrados do outro, em vez de tratá-lo com paternalismo protetor cego."
    },
    {
        "id": 12959,
        "scene": "Abertura do Portal do Batismo de Circula em Hymmnos",
        "original_jp": "#0Ma nam ra flip 0x1011001101##CR#0yor enter ARTONELICO.",
        "original_en": "#0Ma nam ra flip 0x1011001101##CR#0yor enter ARTONELICO.",
        "curated_ptbr": "#0Ma nam ra flip 0x1011001101##\n#0yor enter ARTONELICO.",
        "rationale": "Restauração canônica inegociável do comando místico de sistema entoado pela Anciã Tastiella, que estava completamente em branco no arquivo de entrada preliminar."
    },
    {
        "id": 12991,
        "scene": "O Vírus Apodera-se da Voz de Aurica",
        "original_jp": "オロカナルモノヨ...レーヴァテイルヲCRキズツケル オロカナ ニンゲンヨ...",
        "original_en": "Stupid humans...hurting Reyvateils...",
        "curated_ptbr": "CRIATURAS TOLAS...\nHUMANOS INSENSATOS QUE FEREM AS REYVATEILS...",
        "rationale": "Construção em caixa alta solene e cadência alienígena, refletindo a dicção em katakana do vírus e a dialética do antagonista, que se autoproclama o verdadeiro protetor das Reyvateils contra os humanos predadores."
    },
    {
        "id": 13021,
        "scene": "Intervenção Cibernética Divina de Shurelia",
        "original_jp": "#0Wee i ga flip 0x1011001101 enter ARTONELICO...",
        "original_en": "#0Vey ga flip 0x1011001101 enter AR TONELICO...",
        "curated_ptbr": "#0Wee i ga flip 0x1011001101 enter ARTONELICO...",
        "rationale": "Restauração da invocação Hymmnos ancestral executada por Shurelia para desconectar a mente de Aurica do parasita digital, preservando o prefixo canônico japonês (#0Wee vs #0Vey da NISA) e resgatando a linha vazia do input preliminar."
    },
    {
        "id": 13078,
        "scene": "O Dilema Existencial de Misha e o Remédio de Yakuan",
        "original_jp": "ミシャ。その薬庵の薬は貴方が飲むべきよ。そして、人間になって...貴方の生きたい生き方をすればいい。",
        "original_en": "Misha, take the medicine the shaman gave you. Then, you can enjoy the life you deserve.",
        "curated_ptbr": "Misha. É você quem deve tomar esse remédio do Yakuan.\nE então, tornar-se humana...\npara viver a vida do jeito que sempre quis.",
        "rationale": "Fidelidade estrita ao Glossário Mestre: restauração do nome próprio do eremita da Cosmosfera (Yakuan / 薬庵) achatado erroneamente pela NISA como 'o xamã' (the shaman), e preservação do cerne dramático do dilema entre a liberdade individual e a salvação de Krusche."
    }
]

output_data = {
    "block_id": "BLK_EVD_055",
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
    "block_id": "BLK_EVD_055",
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

print(f"Glossary successfully updated with BLK_EVD_055 handoff and terms in {glossary_path}.")

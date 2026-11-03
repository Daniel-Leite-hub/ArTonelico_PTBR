# -*- coding: utf-8 -*-
"""
Script de consolidação, validação e emissão do bloco BLK_EVD_010.
Ar tonelico: Melody of Elemia (Undub) - PS2
Curadoria Editorial e LQA Sênior
"""

import json
import re
import os
import sys

sys.path.insert(0, r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial")
sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")

from build_blk010_batch1 import batch1
from build_blk010_batch2 import batch2
from build_blk010_batch3 import batch3
from build_blk010_batch4 import batch4

all_dialogues = batch1 + batch2 + batch3 + batch4

print(f"Total curated dialogues: {len(all_dialogues)}")

# 1. Contiguity check
ids = [x['id'] for x in all_dialogues]
expected_ids = list(range(2339, 2635))
assert ids == expected_ids, f"IDs mismatch! Missing: {set(expected_ids) - set(ids)}"
print("Contiguity check passed: exactly IDs 2339 to 2634 (296 dialogues).")

# Load input json to grab speaker_ids and context
input_path = r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_010_input.json'
with open(input_path, 'r', encoding='utf-8') as f:
    input_data = json.load(f)

input_map = {x['id']: x for x in input_data['dialogues']}

for d in all_dialogues:
    inp = input_map[d['id']]
    # Compatibility fields
    d['speaker_id'] = inp.get('speaker_id', 0)
    d['review_status'] = 'approved'
    d['change_type'] = 'curadoria_editorial_profunda'
    d['status'] = d['verdict']
    d['texto_ptbr_anterior'] = d['current_ptbr']
    d['texto_ptbr_curado'] = d['curated_ptbr']
    d['justificativa'] = d['rationale']
    d['revised_ptbr'] = d['curated_ptbr']
    d['notes_or_justification'] = d['rationale']

# 2. Key completeness check
required_keys = ['id', 'event_file', 'speaker', 'original_jp', 'original_en', 'current_ptbr', 'curated_ptbr', 'verdict', 'rationale']
for item in all_dialogues:
    for k in required_keys:
        assert k in item, f"Missing key {k} in item {item['id']}"
    assert item['verdict'] in ('rewritten', 'approved_as_is'), f"Invalid verdict {item['verdict']} in item {item['id']}"
    assert len(item['curated_ptbr'].strip()) > 0, f"Empty text in item {item['id']}"
    assert len(item['rationale'].strip()) > 0, f"Empty rationale in item {item['id']}"
print("Key completeness check passed.")

# 3. Status count
rewritten = sum(1 for x in all_dialogues if x['verdict'] == 'rewritten')
approved = sum(1 for x in all_dialogues if x['verdict'] == 'approved_as_is')
print(f"Rewritten: {rewritten}, Approved as is: {approved}, Total: {len(all_dialogues)}")

# 4. Rubricas check
rubrica_pattern = re.compile(r'(\*[\w\s]+\*|\(.*suspiro.*\)|\(.*risos.*\)|Suspiro\.\.\.|\*cough\*|\*tosse\*)', re.IGNORECASE)
for item in all_dialogues:
    m = rubrica_pattern.search(item['curated_ptbr'])
    if m:
        raise ValueError(f"[ERRO RUBRICA] ID {item['id']}: {m.group(0)} in '{item['curated_ptbr']}'")
print("Rubrica check passed: zero stage directions found.")

# 5. Token shielding and formatting check
for item in all_dialogues:
    t = item['curated_ptbr']
    assert '\r' not in t, f"[ERRO \\r] ID {item['id']} contains \\r"
    if item['id'] == 2346:
        assert 'Mudança de Paradigma' in t, f"Missing Mudança de Paradigma in {item['id']}"
    elif item['id'] == 2374:
        assert '[Ninho do Dragão]' in t, f"Missing [Ninho do Dragão] in {item['id']}"
    elif item['id'] == 2383:
        assert 'Magia ○' in t and '[○○○]' in t, f"Missing placeholders in {item['id']}"
    elif item['id'] == 2402:
        assert '[Torre da Vida]' in t, f"Missing [Torre da Vida] in {item['id']}"
    elif item['id'] == 2404:
        assert 'Ar tonelico' in t, f"Missing Ar tonelico in {item['id']}"
    elif item['id'] == 2426:
        assert '[Anel Hasaiyano]' in t, f"Missing [Anel Hasaiyano] in {item['id']}"
    elif item['id'] == 2479:
        assert '#1MULE_TEIWAZ_ARTONELICO' in t, f"Missing Hymn Code in {item['id']}"
    elif item['id'] == 2508:
        assert '[Provação da Lua]' in t, f"Missing [Provação da Lua] in {item['id']}"
    elif item['id'] == 2514:
        assert 'Harmonics' in t and 'Cavaleiro de Elemia' in t, f"Missing Harmonics / Cavaleiro in {item['id']}"
    elif item['id'] == 2524:
        assert 'Radolf entrou para o grupo' in t, f"Missing Radolf in {item['id']}"
    elif item['id'] == 2525:
        assert 'Krusche entrou para o grupo' in t, f"Missing Krusche in {item['id']}"
    elif item['id'] == 2526:
        assert 'Jack entrou para o grupo' in t, f"Missing Jack in {item['id']}"
    elif item['id'] == 2530:
        assert 'Chronicle Key' in t, f"Missing Chronicle Key in {item['id']}"
    elif item['id'] == 2552:
        assert '[SínC: Bicho de Pelúcia]' in t, f"Missing [SínC: Bicho de Pelúcia] in {item['id']}"
    elif item['id'] == 2586:
        assert 'Crônica Crescente' in t, f"Missing Crônica Crescente in {item['id']}"
    elif item['id'] == 2596:
        assert '[Crônica Crescente]' in t, f"Missing [Crônica Crescente] in {item['id']}"
    elif item['id'] == 2605:
        assert 'Boltapolta' in t, f"Missing Boltapolta in {item['id']}"
    elif item['id'] == 2625:
        assert 'Nau Blindada' in t, f"Missing Nau Blindada in {item['id']}"

print("Token shielding check passed.")

# 6. Build final JSON structure
scene_handoff = {
    "resumo_dramatico": (
        "O bloco BLK_EVD_010 (IDs 2339 a 2634, abrangendo 31 arquivos de eventos Event/*.evd) descortina momentos cruciais da trama principal, revelações de bastidores e arcos psicológicos de extrema sensibilidade: "
        "1. Na Cosmosfera de Aurica (Event/744.evd, Event/701.evd, Event/699.evd), Lyner escapa das correntes obsessivas da donzela e recebe da persona interior a explicação canônica sobre o que é uma 'Mudança de Paradigma' (a cura das feridas e apegos que traz serenidade mental para vislumbrar níveis mais profundos); confronta a barricada de espinhos erguida por Aurica para se isolar do mundo e conquista o respeito solene de Don Leon, que revela o Código Hymmnos sagrado dela: [#1MULE_TEIWAZ_ARTONELICO]; "
        "2. A libertação das rotas aéreas (Event/523.evd), onde Krusche e a equipe do hangar desbloqueiam o [Ninho do Dragão] e o trânsito livre pela barreira de plasma da Blastline; "
        "3. O santuário de Magia da Canção de Aurica (Event/771.evd), expandindo os limites de conjuração mágica; "
        "4. A crise de corrupção viral no mundo virtual de Lady Shurelia (Event/820.evd), na qual Lyner consulta Hama na Cosmosfera de Misha, descobrindo que os vírus da Torre forjam cópias de seres concebidos a partir de sentimentos para corromper a simulação; Hama cruza a [Torre da Vida] até o campo de dados da Ar tonelico e confia a Lyner o [Anel Hasaiyano] para erradicar os vírus e restaurar o mundo virtual; "
        "5. O impagável minigame colegial e tokusatsu de Shurelia (Event/788.evd, Event/812.evd), onde Lyner vive a rotina de estudante com sua colega de classe, debate a identidade heróica da senhorita Tougasaki, recusa-se a aceitar o final trágico ('de tragédia já basta o mundo real!') e convence Lady Shurelia a usar um macete de programação no servidor para reabrir a narrativa antes do desfecho amargo; "
        "6. As terríveis revelações secretas em laboratórios (Event/511.evd, Event/510.evd), com relatórios de experimentos de separação forçada de Misha até o 'Campo KC' no âmbito do Projeto MULE (Mir), provocando a cólera vingativa de Jack, além de relatórios de tentativas de falsificação de Cristais Hymmnos através da Chronicle Key; "
        "7. A leitura secreta do diário do Bispo Falss (Event/463.evd - 'Nova Autobiografia de Kyle, Vol. 5'), expondo toda a teia maquiavélica do clérigo: o uso de Radolf e Aurica como espiões involuntários, a ordem explícita a Bourd para assassinar Lyner na Blastline mesmo em ataque suicida, a fúria pelo fracasso de Bourd e o decreto de emergência em toda a Igreja; "
        "8. A solene [Provação da Lua] em Em Pheyna (Event/156.evd), onde Lyner prova ser um verdadeiro [Cavaleiro de Elemia] dominando o poder de [Harmonics], selando a entrada oficial de Radolf, Krusche e Jack no grupo; "
        "9. O comovente episódio artesanal em Firefly Alley (Event/970.evd), onde Lyner pede a Claire a receita para costurar o boneco de tigre original de Aurica, obtendo o Cartão de Receita [SínC: Bicho de Pelúcia] (Don Leon); "
        "10. O reencontro em Em Pheyna (Event/222.evd) com Lorde Flute e a venerável Tastiella, que revela a existência da [Crônica Crescente] (onde Misha cantou por anos a fio para sustentar o selo dos vírus), revelando-se a paralisia das pernas de Tastiella; "
        "11. A aquisição do catalisador de energia sinfônica [Boltapolta] no Porto Gaivota (Event/339.evd); "
        "12. E a eletrizante fuga pelo Pipeline (Event/100.evd), que enfurece o Bispo Falss a ponto de ele atropelar as ordens do Diretor-Presidente da Tenba e mobilizar a colossal Nau Blindada contra os Guardiões da Torre para abater Lyner e Misha."
    ),
    "decisoes_terminologicas": {
        "Paradigm Shift (パラダイムシフト)": "Mudança de Paradigma (salto qualitativo de cura emocional na Cosmosfera)",
        "Dragon's Nest (竜の巣)": "[Ninho do Dragão] (marco geográfico de navegação aérea no Mapa-Múndi)",
        "Mind Guardian (心の護)": "Guardiã da Mente / Guardião da Mente (entidade psíquica protetora da Reyvateil)",
        "Tower of Life (いのちの塔)": "[Torre da Vida] (estrutura da Cosmosfera que se conecta ao campo de dados da Torre)",
        "Field of Information (情報野)": "campo de dados / campo informacional (corrigindo o errôneo 'binary field' da NISA)",
        "Forms of thought / Emotion (『想い』の生命体)": "entidades concebidas a partir de sentimentos / nascidas dos sentimentos",
        "Hasaiyano Ring (はさいやの指輪)": "[Anel Hasaiyano] (anel antiviral purificador de simulações)",
        "Miss Tougasaki (塔ヶ崎さん)": "senhorita Tougasaki (identidade colegial de Shurelia no minigame)",
        "Urawaza (裏技)": "macete de programação (truque técnico/exploit do servidor da Torre)",
        "MULE Project (MULEプロジェクト)": "Projeto MULE (projeto confidencial da Igreja/Tenba relacionado a Mir)",
        "KC Field (ケーシー野)": "Campo KC (região da psique de Reyvateil de alta linhagem)",
        "Hymn Code (ヒュムネコード)": "Código Hymmnos (com fixação de [#1MULE_TEIWAZ_ARTONELICO])",
        "Kyle's Autobiography (カイエル自伝)": "Autobiografia de Kyle (diário cifrado do Bispo Falss)",
        "Ordeal of the Moon (月の試練)": "[Provação da Lua] (exame ritual dos guerreiros Teru em Em Pheyna)",
        "Harmonics (ハーモニクス)": "[Harmonics] (ressonância emocional e sincronia em combate)",
        "Knight of Elemia / Apostle (エレミアの使徒)": "[Cavaleiro de Elemia] / Apóstolo de Elemia",
        "Stuffed Animal Recipe (合C:ぬいぐるみ)": "[SínC: Bicho de Pelúcia] (receita de síntese do boneco Don Leon)",
        "Crescent Chronicle (クレセントクロニクル)": "Crônica Crescente / [Crônica Crescente] (antigo local de selamento onde Misha cantava)",
        "Chief Flute (フラウト様)": "Lorde Flute (líder nobre e respeitado da tribo Teru)",
        "Boltapolta (ボルタポルタ)": "[Boltapolta] (artefato catalisador e amplificador de energia sinfônica)",
        "Armored Airship (装甲船)": "Nau Blindada / Nave Blindada (aeronave bélica pesada mobilizada por Falss)",
        "Tower Guardians (ガーディアン)": "Guardiões da Torre (defesas biomecânicas exteriores de Ar tonelico)"
    },
    "alertas_para_proximo_bloco": (
        "1. Radolf, Krusche e Jack agora fazem parte oficialmente do grupo: atentar para as interações táticas, provocações de acampamento e alinhamento de liderança de Radolf com o cinismo de Jack. "
        "2. A [Crônica Crescente] (Crescent Chronicle) é o próximo destino capital da jornada: local onde o passado de Misha e a natureza do selo viral serão desvelados. "
        "3. O Bispo Falss assumiu o comando da Nau Blindada e persegue o grupo ativamente pelos céus, quebrando a jurisdição da Tenba e desafiando os Guardiões da Torre. "
        "4. Preservar o tratamento nobre a Lorde Flute e à Senhora Tastiella, cuja limitação motora é segredo revelado que exige respeito dramático. "
        "5. Manter a grafia de 'Ar tonelico' rigorosamente com 't' minúsculo e 'Crônica Crescente' para a lendária estrutura de sustentação."
    )
}

output_data = {
    "block_id": "BLK_EVD_010",
    "axis_id": "AXIS_3",
    "axis_name": "HISTÓRIA E EVENTOS",
    "category": "HISTÓRIA E EVENTOS",
    "total_lines": len(all_dialogues),
    "line_count": len(all_dialogues),
    "lines_rewritten": rewritten,
    "lines_approved_as_is": approved,
    "id_range": [2339, 2634],
    "curator_notes": (
        "Curadoria editorial profunda em duas passagens de 100% das 296 falas de BLK_EVD_010 (IDs 2339 a 2634). "
        "Auditoria integral contra a Tríade de Idiomas (JP SLPS-732.49 soberano; EN SLUS-214.45 suporte; PT-BR viva). "
        "Correção do histórico erro de inversão de autoria viral em ID 2428 (NISA alegava que Shurelia reescrevia o mundo, "
        "quando foram os vírus que o corromperam), erradicação do erro de gênero em IDs 2471 e 2571 onde Shurelia era tratada no masculino, "
        "restauração do nome colegial Tougasaki-san em ID 2446, fidelidade terminológica a 'campo de dados' (情報野) em vez de 'binary field', "
        "harmonização de 'Mudança de Paradigma', 'Provação da Lua', 'Harmonics', 'Código Hymmnos', 'Crônica Crescente' e 'Nau Blindada'."
    ),
    "dialogues": all_dialogues,
    "curated_lines": all_dialogues,
    "scene_handoff": scene_handoff
}

output_path = r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_010_output.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"File successfully written to: {output_path}")
print(f"Total size: {os.path.getsize(output_path)} bytes.")

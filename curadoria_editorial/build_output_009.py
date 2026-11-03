# -*- coding: utf-8 -*-
import json
import re
import os

from build_blk009_batch1 import batch1
from build_blk009_batch2 import batch2
from build_blk009_batch3 import batch3
from build_blk009_batch4 import batch4

all_dialogues = batch1 + batch2 + batch3 + batch4

print(f"Total curated dialogues: {len(all_dialogues)}")

# 1. Contiguity check
ids = [x['id'] for x in all_dialogues]
expected_ids = list(range(2115, 2339))
assert ids == expected_ids, f"IDs mismatch! Missing: {set(expected_ids) - set(ids)}"
print("Contiguity check passed: exactly IDs 2115 to 2338 (224 dialogues).")

# Load input json to grab speaker_ids
input_path = r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_009_input.json'
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
    # Check carriage return
    assert '\r' not in t, f"[ERRO \\r] ID {item['id']} contains \\r"
    # Check brackets in key lines
    if item['id'] == 2126:
        assert '[Esfera de Gelo]' in t, f"Missing [Esfera de Gelo] in {item['id']}"
    elif item['id'] == 2190:
        assert '[Cantar Hino]' in t, f"Missing [Cantar Hino] in {item['id']}"
    elif item['id'] == 2228:
        assert '[Suco de Comida]' in t and '[SínC: Suco de Comida]' in t, f"Missing items in {item['id']}"
    elif item['id'] == 2338:
        assert '[Purger]' in t and 'Cristal Hymmnos' in t, f"Missing Purger / Cristal Hymmnos in {item['id']}"

print("Token shielding check passed.")

# 6. Build final JSON structure
scene_handoff = {
    "resumo_dramatico": (
        "O bloco BLK_EVD_009 (IDs 2115 a 2338, 20 arquivos de eventos Event/*.evd) percorre arcos dramáticos cruciais e momentos de ouro de Ar tonelico: Melody of Elemia: "
        "1. Na Cosmosfera de Misha (Event/604.evd), o encontro com o Espírito do Gelo e a criação da Magia Vermelha [Esfera de Gelo], culminando no encontro com o eremita Yakuan (薬庵), onde Misha pede um elixir para se tornar humana e desabafa com Lyner sobre a injustiça e o trauma de viver como um robô sem sentimentos forçada a cantar para sustentar o mundo; "
        "2. O doce e íntimo diálogo no acampamento (Event/891.evd) em que Lyner flagra Aurica escrevendo uma misteriosa carta secreta e brinca sobre ser uma carta de amor, deixando-a adoravelmente envergonhada; "
        "3. A nobreza de espírito de Radolf comandando a reconstrução dos edifícios danificados pelo confronto (Event/373.evd, Event/417.evd); "
        "4. A alternância de suporte em combate entre Misha e Aurica (Event/184.evd, Event/71.evd) e o recolhimento melancólico de Claire em Firefly Alley (Event/718.evd); "
        "5. O pesadelo sombrio na Cosmosfera de Misha (Event/594.evd), onde o mundo mergulha em trevas totais e a guardiã psíquica exige que Lyner assuma a responsabilidade de acolher as feridas abertas de Misha; "
        "6. O grande dia de celebração nupcial/triunfal na Cosmosfera de Aurica (Event/762.evd, Event/52.evd); "
        "7. A icônica e hilária cena culinária da meia-noite (Event/883.evd), na qual Lady Shurelia prepara o temido 'Suco de Comida' (Food Juice / メシジュース), Lyner se surpreende com o sabor viscoso, quase se engasga com grãos de arroz não dissolvidos e obtém a receita [SínC: Suco de Comida]; "
        "8. A solene revelação cósmica no mirante do Plug Sinfônico / Rinkernator (Event/502.evd), onde Shurelia revela a carótida da Torre e explica que este é o local de sucessão onde a Torre renasce e passa por sua transmigração (輪廻転生), confessando que até hoje nunca houve uma substituição de Administradora e que ela carrega o fardo sozinha desde a gênese de Sol Ciel; "
        "9. A comoção popular diante da marcha fanática das tropas do Bispo Falss rumo ao topo da Torre em busca da Terra Santa e do advento do Trio de Elemia (Event/352.evd); "
        "10. O impagável minigame de paródia de tokusatsu e garota mágica na Cosmosfera (Event/800.evd), com Shurelia encarnando 'Singer Angel Shurelia' empunhando o herbicida da justiça contra a vilã Claire e o monstro ELMA; "
        "11. O trauma de infância de Misha (Event/616.evd), onde uma figura materna rígida (com traços de Shurelia) a proíbe de brincar, exige que ela vire adulta à força e a ameaça com a floresta proibida; "
        "12. A solene despedida no sopé da Torre antes da travessia da Blastline rumo ao Mundo Superior (Event/149.evd), onde Radolf, Krusche, Aurica e Jack renovam seus laços, com Jack alertando Lyner para não se espantar com o que encontrar lá em cima; "
        "13. A consulta técnica no Centro de Mergulho sobre a alimentação por Power Sourcer (Event/332.evd); "
        "14. E o salvamento providencial de Lyner nos escombros por Jack (Event/134.evd), que resgata o lendário Cristal Hymmnos [Purger] lembrando-se do broche anterior, selando a entrada de Jack no grupo e partindo em socorro de Aurica."
    ),
    "decisoes_terminologicas": {
        "Glacial Ball (樹氷玉)": "[Esfera de Gelo] (Magia Vermelha de Misha padronizada com BLK_SYS_011; verbo 'teceu')",
        "Yakuan / Shaman (薬庵 / 仙人)": "Yakuan / eremita Yakuan (restauração do nome japonês original do sábio e correção do erro crasso de tradução 'I'll die')",
        "Song Fairy (詩の精)": "Fada das Canções (entidade espiritual ligada à canção)",
        "Food Juice (メシジュース)": "[Suco de Comida] / [SínC: Suco de Comida] (alinhado rigorosamente ao Glossário Mestre e síntese)",
        "Rinkernator (リンカーネイション)": "”Rinkernator” (Plug Sinfônico e santuário de transmigração e sucessão dos Administradores da Torre)",
        "Trio of Elemia (エレミア三謳神)": "Trio de Elemia (as três Deusas do Canto de Elemia: Eoria, Frelia e Tilia)",
        "Singer Angel Shurelia (シンガーエンジェル・シュレリア)": "Singer Angel Shurelia (bordão heroico do minigame na Cosmosfera)",
        "Harase-kun (原瀬君)": "Harase-kun (papel dramático de Lyner no minigame de Shurelia, corrigindo a corruptela 'Harasett')",
        "ELMA (エルマ)": "ELMA (guardião mecânico original da Torre Ar tonelico)",
        "Power Sourcer (パワーソーサー)": "Power Sourcer (componente gerador de baixa intensidade de energia sinfônica da máquina de Mergulho)",
        "Purger (パージャ)": "Cristal Hymmnos [Purger] (cristal sagrado purificador de vírus de Mir)",
        "Reyvateil Position (レーヴァテイルポジション)": "posição de Reyvateil (posto tático de suporte no combate)"
    },
    "alertas_para_proximo_bloco": (
        "1. Jack se juntou oficialmente ao grupo no fim de Event/134.evd: atentar para a dicção cínica, madura, leal e pragmática do mercenário em combate e eventos de acampamento. "
        "2. A posse do Cristal Hymmnos [Purger] é o gatilho narrativo para a purificação dos vírus de Mir e o avanço rumo ao Mundo Superior / Platina. "
        "3. Manter a paridade terminológica de 'Plug Sinfônico' (導力プラグ), 'Rinkernator' (リンカーネイション) e 'Trio de Elemia' (エレミア三謳神). "
        "4. Preservar o respeito reverente inicial de Lyner chamando Shurelia por 'Lady Shurelia' (シュレリア様) e 'a senhora', contrastando com o afeto que floresce nas cenas íntimas e na Cosmosfera."
    )
}

output_data = {
    "block_id": "BLK_EVD_009",
    "axis_id": "AXIS_3",
    "axis_name": "HISTÓRIA E EVENTOS",
    "category": "HISTÓRIA E EVENTOS",
    "total_lines": len(all_dialogues),
    "line_count": len(all_dialogues),
    "lines_rewritten": rewritten,
    "lines_approved_as_is": approved,
    "id_range": [2115, 2338],
    "curator_notes": (
        "Curadoria editorial profunda em duas passagens de 100% das 224 falas de BLK_EVD_009 (IDs 2115 a 2338). "
        "Auditoria integral contra a Tríade de Idiomas (JP SLPS-732.49 soberano; EN SLUS-214.45 apoio; PT-BR viva). "
        "Erradicação do histórico erro crasso em ID 2135 ('I'll die' gerado pela confusão entre o sufixo 'desu yo' e 'morte'), "
        "correção de gravíssimas inversões de gênero em IDs 2119 e 2125, restauração do bordão sentai de Singer Angel Shurelia, "
        "harmonização de [Suco de Comida] e recepção do Cristal Hymmnos [Purger]."
    ),
    "dialogues": all_dialogues,
    "curated_lines": all_dialogues,
    "scene_handoff": scene_handoff
}

output_path = r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_009_output.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"File successfully written to: {output_path}")
print(f"Total size: {os.path.getsize(output_path)} bytes.")

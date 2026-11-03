# -*- coding: utf-8 -*-
"""
Montagem final e geração determinística de BLK_EVD_022_output.json.
"""

import json
import sys
from pathlib import Path

# Carregar o dicionário de curadorias
from build_blk022 import CURATIONS, INPUT_PATH, OUTPUT_PATH

def generate_output():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    dialogues = input_data["dialogues"]
    output_dialogues = []

    lines_rewritten = 0
    lines_approved_as_is = 0

    for d in dialogues:
        d_id = d["id"]
        if d_id not in CURATIONS:
            raise ValueError(f"Falta curadoria para ID {d_id}!")

        curated_text, verdict, rationale = CURATIONS[d_id]

        if verdict == "rewritten":
            lines_rewritten += 1
        elif verdict == "approved_as_is":
            lines_approved_as_is += 1
        else:
            raise ValueError(f"Veredito inválido para ID {d_id}: {verdict}")

        output_dialogues.append({
            "id": d_id,
            "event_file": d["event_file"],
            "speaker_id": d["speaker_id"],
            "speaker": d["speaker"],
            "original_jp": d["original_jp"],
            "original_en": d["original_en"],
            "current_ptbr": d["current_ptbr"],
            "curated_ptbr": curated_text,
            "verdict": verdict,
            "rationale": rationale
        })

    highlights = [
        {
            "id": 5577,
            "speaker": "Personagem [75]",
            "description": "Humor e duplo sentido inocente: Kanade oferecendo a si mesma como presente de vitória ('Por favor, fique com a Kanade!'), provocando engasgo atônito em Lyner e desconfiança vigilante em Shurelia."
        },
        {
            "id": 5589,
            "speaker": "Sistema / Caixa Narrativa / Tutorial",
            "description": "Fidelidade terminológica e litúrgica: Shurelia 'tecendo' (紡ぎ出した) a Magia Vermelha com o título canônico sagrado [Criança da Luz] (光の御子)."
        },
        {
            "id": 5590,
            "speaker": "Aurica",
            "description": "Correção gramatical canônica de gênero: 'Muito obrigada' dito por Aurica corrigido do erro crasso 'Obrigado' masculino herdado da tradução automática preliminar."
        },
        {
            "id": 5603,
            "speaker": "Lyner",
            "description": "Restauração de código executável ancestral em Hymmnos: resgate integral de '#0Ma paks ga exec guol A8 al noes.' que constava completamente vazio no banco de dados."
        },
        {
            "id": 5623,
            "speaker": "Krusche",
            "description": "Oralidade nostálgica e fidelidade culinária: a lista cômica de dívidas de infância entre Krusche e Misha com [Combos Dokkoi], [Gelo Ralado], [Megaleite], peixes secos ao mirin e [Balas de Gato]."
        },
        {
            "id": 5646,
            "speaker": "Shurelia",
            "description": "Clímax afetivo e nobreza da Deusa: Shurelia declarando diante de Leard que Lyner é o esteio do seu coração (心の支え), dissipando as dúvidas paternas sobre a expedição a Em Pheyna."
        },
        {
            "id": 5658,
            "speaker": "Sistema / Caixa Narrativa / Tutorial",
            "description": "Correção geográfica canônica de toponímia: fixação no Mapa-Múndi de [Asa da Reminiscência] (追憶の尾翼) e [Ruínas de Skuwat] (スクワート廃墟), expurgando invenções da NISA."
        },
        {
            "id": 5672,
            "speaker": "Cientista / Pesquisador",
            "description": "Revelação estarrecedora do diário de Kyle/Falss: o plano de falsa bandeira contra a Tenba e a ordem de assassinato da [Cantora das Estrelas] (星詠) Misha como artifício para reviver Mir."
        },
        {
            "id": 5700,
            "speaker": "Jack",
            "description": "Lapidação tática de combate: Jack instruindo o uso obrigatório de [Ataque de Fogo] (炎打撃) e o suporte ofensivo dos [Mísseis] (メッソー) sintetizados via Grathmeld."
        },
        {
            "id": 5781,
            "speaker": "Sistema / Caixa Narrativa / Tutorial",
            "description": "Superação psicológica no Nível 5 de Aurica: a heroína adulta protegendo sua criança interior da covardia de Bourd, sarando seus traumas de infância e tecendo a Magia Vermelha [Erupção de Don Leon]."
        },
        {
            "id": 5798,
            "speaker": "Misha",
            "description": "Diretriz tática de batalha: instrução sonora sobre a expansão obrigatória do [Campo de Ambiente] (アンビエンスフィールド) até o ponto de ressonância crítica."
        },
        {
            "id": 5801,
            "speaker": "Estudante da Cosmosfera",
            "description": "Tragédia e lirismo existencial: a memória escolar de infância de Lyner confrontada com a curta e dolorosa expectativa de vida das Reyvateils."
        }
    ]

    scene_handoff = {
        "resumo_dramatico": "Vitória cômica no minigame retro e concessão da Chave de Análise de Kanade para invocação de batalha, com Shurelia tecendo a Magia Vermelha [Criança da Luz]; conclusão do Nível 4 da Cosmosfera de Aurica e advertência marcial de Don Leon; liberação do Anteparo A8 via Espectro FFT com restauração do verso executável em Hymmnos ancestral; chegada e primeiras impressões do vibrante Mundo Inferior por Lyner; recordação nostálgica das brigas de infância na Gôndola de Traslado entre Krusche e Misha por Combos Dokkoi e guloseimas; conselho de emergência em Platina sobre os 50% de ressurreição de Mir, a confissão comovente de Shurelia elegendo Lyner como o esteio do seu coração e a rota para Em Pheyna e Tastiella; descoberta da Pedra Soleil na Asa da Reminiscência e abertura das Ruínas de Skuwat; revelação sombria do Volume 2 da Nova Autobiografia de Kyle, detalhando a manipulação de Bourd pela Igreja e a trama de assassinato da Cantora das Estrelas Misha; batalha com Jack exigindo Ataque de Fogo e Mísseis na Floresta de Viola; abertura do portal de realidade virtual no Stonehenge na mente de Aurica; fuga apressada de Krusche escalando a Torre antes do grupo; choque de Lyner com o uniforme colegial de Misha no Nível 5 de sua Cosmosfera e o enigma da miragem central; redenção de Aurica no Nível 5 protegendo sua criança interior das garras de Bourd e tecendo a Magia Vermelha [Erupção de Don Leon]; a correria colegial cômica de Aurica atrasada para o colégio; instrução do Campo de Ambiente em combate; e o eco trágico da finitude de vida das Reyvateils nas memórias do passado.",
        "decisoes_terminologicas": {
            "Criança da Luz": "[Criança da Luz] (光の御子 / Child of Light, título sagrado e Magia Vermelha de Kanade)",
            "Chave de Análise": "[Chave de Análise] (解析キー / Analysis Key, parâmetro fônico de invocação)",
            "Anteparo A8": "[Anteparo A8] (A8隔壁 - A8 Kakuheki, comporta militar da Torre alinhada com Anteparo A1, A2 e A6)",
            "Espectro FFT": "[Espectro FFT] (FFTスペクトラム認証, protocolo fônico/biométrico de autenticação)",
            "Gôndola de Traslado": "Gôndola de Traslado (シャトルゴンドラ, transporte mecânico entre setores da Torre)",
            "Combo Dokkoi": "[Combo Dokkoi] (ドッコイ定食 / Dokkoi Set, refeição tradicional disputada na infância)",
            "Gelo Ralado": "[Gelo Ralado] (かち割り氷 / Shaved Ice, ingrediente/iguaria)",
            "Megaleite": "[Megaleite] (メガミルク / Megamilk, bebida tradicional de Sol Ciel)",
            "Balas de Gato": "[Balas de Gato] (猫飴 / Kitty Candies, doces favoritos de Misha)",
            "Bomba de Raio": "[Bomba de Raio] (雷弾 / Thunder Bomb, projétil elétrico de ignição)",
            "Esteio do meu coração": "Esteio do meu coração (心の支え, declaração comovente de Shurelia sobre Lyner)",
            "Pedra Soleil": "[Pedra Soleil] (ソレイユストン / Soleil Stone, ingrediente de síntese)",
            "Asa da Reminiscência": "[Asa da Reminiscência] (追憶の尾翼 / Tail of Reminiscence, colina memorial)",
            "Ruínas de Skuwat": "[Ruínas de Skuwat] (スクワート廃墟, localidade desolada corrigida do termo vago 'Skuwat Village')",
            "Nova Autobiografia de Kyle": "[Nova Autobiografia de Kyle] (新・カイエル自伝, diário secreto de Kyle/Bispo Falss)",
            "Cantora das Estrelas": "[Cantora das Estrelas] (星詠 / Star Singer, título sagrado sacerdotal de Misha em Sol Ciel)",
            "Ataque de Fogo": "[Ataque de Fogo] (炎打撃 / Fire Attack, propriedade elemental ofensiva de Jack)",
            "Míssil": "[Míssil] / [Mísseis] (メッソー / Missile, item explosivo do Grathmeld)",
            "Erupção de Don Leon": "[Erupção de Don Leon] (赤魔法・ドン助大噴火, Magia Vermelha tecida pela autodefesa de Aurica)",
            "Campo de Ambiente": "[Campo de Ambiente] (アンビエンスフィールド / Ambience Field, ressonância harmônica de suporte tático)",
            "Setor de força": "Setor de força (動力部 / Power Department, departamento motriz da nave e da Torre)"
        },
        "alertas_para_proximo_bloco": "Atenção especial à escalada da Torre rumo ao encontro de Krusche, às revelações subsequentes em Em Pheyna junto a Tastiella para a liberação de Mir, e aos desdobramentos psicológicos do Nível 5 das Cosmosferas de Misha e Aurica."
    }

    output_data = {
        "block_id": input_data.get("block_id", "BLK_EVD_022"),
        "axis_id": input_data.get("axis_id", "AXIS_3"),
        "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
        "total_lines": len(output_dialogues),
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "highlights": highlights,
        "scene_handoff": scene_handoff,
        "dialogues": output_dialogues
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Sucesso: Gerado {OUTPUT_PATH} com {len(output_dialogues)} falas ({lines_rewritten} reescritas, {lines_approved_as_is} aprovadas as-is).")

if __name__ == "__main__":
    generate_output()

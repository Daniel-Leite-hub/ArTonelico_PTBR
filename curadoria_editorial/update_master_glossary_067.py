# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_067."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Falcon's Claw": {
        "pt": "Garra do Falcão",
        "gender": "feminino",
        "number": "singular",
        "category": "Toponímia / Localização",
        "note": "たかのつめあと. Ilhota rochosa isolada e ninho de serpes aladas, completamente apartada da estrutura principal das Asas de Hórus."
    },
    "Tragic Heroine": {
        "pt": "Heroína Trágica",
        "gender": "feminino",
        "number": "singular",
        "category": "Conceito Psicológico / Cosmosfera",
        "note": "悲劇のヒロイン. Arquétipo central da neurose de abandono de Misha na Cosmosfera, distorcido pejorativamente pela NISA como 'drama queen'."
    },
    "Paradox Trap": {
        "pt": "Armadilha da Eternidade",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Sistema",
        "note": "永遠の罠. Laço mental patológico na Cosmosfera de Misha capaz de induzir mergulhadores a um coma perpétuo."
    },
    "Self-Paradox": {
        "pt": "Paradoxo Interno",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Sistema",
        "note": "自己パラドックス. Ruptura na estrutura lógica de um nível da Cosmosfera causada por desejos irreconciliáveis da Reyvateil."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/642.evd",
    "last_line_id": 15522,
    "resumo_dramatico": "O bloco BLK_EVD_067 abrange três sequências cruciais de alta intensidade narrativa: (1) Em Event/118.evd, Radolf transporta Lyner e Misha na aeronave clerical, revelando a busca pelo Cristal Hymmnos e orientando Lyner a consultar o Bispo Falss. Durante a travessia, Misha desabafa sobre sua acrofobia e seu passado em Platina, mas são emboscados por Bourd (antagonista da Tenba), que faz Aurica de refém sobre o abismo. Misha se sacrifica caminhando sozinha pela prancha para poupar Aurica. Bourd descarta Aurica no precipício; Lyner salta e se recusa a soltar sua mão. Ambos são salvos em manobra acrobática por Krusche, que colide e pousa na isolada Garra do Falcão (たかのつめあと), um ninho de serpes voadoras fora das Asas de Hórus, alfinetando o 'luxo' de Lyner cercado de Reyvateils. (2) Em Event/294.evd, malandros abordam Aurica com intimidações e assédio verbal no Baixo Mundo. Lyner intervém tomado por fúria cega e espanca os agressores quase até a morte. Claire intervém e admoesta Lyner: a verdadeira proteção não nasce de brandir a espada a esmo nem de espalhar terror nos olhos de quem se ama, oferecendo uma Canção para serenar os ânimos. (3) Em Event/642.evd, na Cosmosfera de Misha, a persona tirânica da amiga de infância exige posse absoluta sobre Lyner sob pena de morte ou exílio. Lyner recusa o cativeiro afetivo e a desafia a matá-lo ela mesma. A recusa colapsa as defesas de Misha, que confessa seu desespero de ser esquecida e sua necessidade de ser a 'heroína trágica' (悲劇のヒロイン, corrigindo a deturpação 'drama queen' da NISA) para ser amada eternamente. O autoconflito gera um paradoxo interno e aciona a Mudança de Paradigma rumo a Stonehenge, culminando no resgate de Lyner da armadilha da eternidade (永遠の罠) antes de um coma irreversível.",
    "decisoes_terminologicas": {
        "Hymn Crystal": "ヒュムネクリスタル (Cristal Hymmnos)",
        "Falcon's Claw": "たかのつめあと (Garra do Falcão)",
        "Wings of Horus": "ホルスの翼 (Asas de Hórus)",
        "Dokkoi Set": "ドッコイ定食 (Combo Dokkoi)",
        "Tragic Heroine": "悲劇のヒロイン (Heroína Trágica)",
        "Paradigm Shift": "パラダイムシフト (Mudança de Paradigma)",
        "Stonehenge": "ストーンヘンジ (Stonehenge)",
        "Paradox Trap": "永遠の罠 (Armadilha da Eternidade)",
        "Self-Paradox": "自己パラドックス (Paradoxo Interno)"
    },
    "alertas_para_proximo_bloco": "Com a Garra do Falcão consolidada como enclave isolado e a Mudança de Paradigma de Misha ativada em direção a Stonehenge na Cosmosfera, o próximo bloco deve acompanhar a progressão dos níveis mentais e a travessia das ilhas flutuantes."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"Glossário Mestre atualizado com sucesso! Total de termos: {len(glossary['terms'])}")

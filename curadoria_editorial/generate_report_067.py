import json
from datetime import datetime, timezone

report = {
    "block_id": "BLK_EVD_067",
    "completed_at": datetime.now(timezone.utc).isoformat(),
    "backup_created": None,
    "total_dialogues": 223,
    "lines_rewritten": 216,
    "lines_approved_as_is": 7,
    "new_terms_added": 4,
    "scene_handoff": {
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
    },
    "highlights": [
        "Restauração do termo conceitual 'Heroína Trágica' (悲劇のヒロイン) em Event/642.evd (IDs 15498 e 15499), corrigindo a distorção degradante da NISA ('drama queen') que esvaziava a gravidade existencial do trauma de Misha.",
        "Restauração da autêntica fala da Moradora do Mundo Inferior em Event/642.evd (ID 15505: '...こんな形でもパラダイムシフトが起こる事って...あるのね。びっくりなのよ...'), corrigindo a invenção da NISA ('I don't think she can pass through the Paradigm Shift').",
        "Restauração do perigo psicológico real em Event/642.evd (ID 15513: '気がおかしくなってしまう' / 'vou perder o juízo de vez'), corrigindo o abrandamento indevido da NISA ('get upset').",
        "Restauração do conceito 'Armadilha da Eternidade' (永遠の罠) em Event/642.evd (ID 15518), substituindo o anacrônico 'paradox loop' da NISA.",
        "Restauração da dicção áspera e agressiva de Bourd em Event/118.evd (IDs 15340 a 15387), restaurando a expressão idiomática '煮え湯を飲まされる' (ID 15341) e o humor cínico de Krusche (IDs 15405 a 15434), padronizando Combo Dokkoi, Garra do Falcão e Asas de Hórus.",
        "Trabalho de decupagem e ritmo com ZERO erros de Hard Gate e ZERO advertências de estilo/lint no validador editorial determinístico v4.5.0."
    ]
}

with open("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_067_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print("Report saved successfully.")

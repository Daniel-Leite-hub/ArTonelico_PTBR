import json
from datetime import datetime, timezone

report = {
    "block_id": "BLK_EVD_083",
    "completed_at": datetime.now(timezone.utc).isoformat(),
    "backup_created": "G:\\JOGO\\PS2\\Ar tonelico - Melody of Elemia (Undub)\\Ferramentas_Traducao\\backups\\curadoria\\ArTonelico_backup_pre_BLK_EVD_083.atproj",
    "total_dialogues": 228,
    "lines_rewritten": 228,
    "lines_approved_as_is": 0,
    "new_terms_added": 5,
    "scene_handoff": {
        "last_scene_id": "Event/766.evd",
        "last_line_id": 18912,
        "resumo_dramatico": "O bloco BLK_EVD_083 abrange quatro sequências cruciais de conflito fisiológico, exploração psíquica e provação amorosa: (1) Em Event/323.evd, logo após o resgate de Misha e a despedida da equipe de Jack, Aurica sofre um colapso repentino de febre alta. Claire intervém em prantos e desculpa-se por suas palavras duras anteriores, diagnosticando que Aurica foi acometida pela temida febre de Tatoolist (タトゥリスタ病) — a pane fisiológica mortal que assola Reyvateils da Terceira Geração privadas de seu agente prolongador de vida (延命剤). Radolf e Claire deduzem que o organismo dela está consumindo o composto em ritmo anormalmente acelerado, e Shurelia instrui Lyner a mergulhar urgentemente na Cosmosfera de Aurica pelo Centro de Mergulho para salvar sua vida. (2) Em Event/598.evd, no interior da Cosmosfera de Misha imersa em trevas sufocantes, Lyner e Misha encontram um pequeno espírito do gelo (氷の精) que derreteu por ter se perdido na escuridão rumo ao Monte das Geadas (樹氷山). Misha relembra com saudade nostálgica as neves de outrora que clareavam o mundo. Na ramificação de sucesso, estimulada pela confiança inabalável de Lyner e pelos ensinamentos do Nível 1, Misha dialoga com seu mundo e tece a Magia Verde [Análise] (緑魔法【アナライザ】), desvendando a rota até o topo da montanha. Na ramificação de falha, Misha desiste consumida pelo medo do breu, o espírito se dissolve e Lyner é expulso da Cosmosfera pela Moradora do Mundo Inferior. (3) Em Event/953.evd, os atendentes do Centro de Mergulho e o Operador de Portão revelam com espanto que Lyner e Aurica alcançaram profundidades incomuns na Cosmosfera sem terem realizado a Instalação (インストール). Aurica cora intensamente confessando que nunca passou por isso e não sabia como propor o rito. O atendente explica a gravidade física da técnica: a inserção direta de Cristais Grathnode na carne da Reyvateil amplia a força da Magia da Canção, mas atua como veneno tóxico ao organismo da donzela. Lyner, estarrecido, recusa-se a machucá-la, e o atendente sugere que o casal vá a uma pousada conversar a sós e decidir com o coração. (4) Em Event/766.evd, no Nível 8 da Cosmosfera de Aurica, o casal confronta a Silfa (シルフ), espírito livre que roubou o vestido cerimonial nupcial para impedir o enlace matrimonial com Lyner, alertando Aurica sobre a renúncia da solidão autossuficiente e a perda da liberdade individual. Na ramificação vitoriosa, Aurica amadurece e declara com nobreza que o amor compartilhado expande a vida em vez de aprisioná-la; a Silfa devolve o vestido abençoando o casal, Aurica veste o traje para deslumbre de Lyner, convida-o para a cerimônia na Catedral e tece a Magia Vermelha [Dança da Silfa] (赤魔法【シルフのダンス】). Na ramificação de recusa, Aurica recua atemorizada pelo compromisso e a Silfa despacha o vestido e Lyner com um golpe tempestuoso pelos ares.",
        "decisoes_terminologicas": {
            "Febre de Tatoolist": "タトゥリスタ病 / Tatoolist Disease",
            "Agente prolongador de vida": "延命剤 / Life Extending Agent (DDP)",
            "Espírito do gelo": "氷の精 / Ice Fairy",
            "Monte das Geadas": "樹氷山 / Mount Frost",
            "Magia Verde [Análise]": "緑魔法【アナライザ】 / Green Magic [Analyzer]",
            "Instalação": "インストール / Install",
            "Cristal Grathnode": "グラスノ結晶 / Grathnode Crystal",
            "Silfa": "シルフ / Sylph",
            "Dança da Silfa": "赤魔法【シルフのダンス】 / Red Magic [Sylph's Dance]",
            "Catedral": "正教会 / Cathedral"
        },
        "alertas_para_proximo_bloco": "Para os blocos seguintes (BLK_EVD_084 em diante), manter a continuidade das ramificações de eventos e finais, a estabilidade das Cosmosferas de Aurica e Misha no pós-jogo ou eventos paralelos, e a preservação rigorosa da Tríade de Idiomas e paridade técnica."
    },
    "highlights": [
        {
            "id": 18707,
            "speaker": "Claire",
            "original_jp": "オリカ...あなたすごい熱...CRこれってもしかして...CRタトゥリスタ病じゃない!?",
            "curated_ptbr": "Aurica... você está ardendo em febre!\nSerá possível que... seja a febre de Tatoolist?!",
            "nota": "Diagnóstico do colapso febril agudo de Terceira Geração privada de prolongador."
        },
        {
            "id": 18709,
            "speaker": "Claire",
            "original_jp": "体の延命剤の量が不足すると発生する病気。放っておくと、高熱を出して死ぬわよ。",
            "curated_ptbr": "É um mal que ataca quando a dose do agente prolongador de vida fica baixa demais.\nSe não for tratada a tempo, a febre consome o corpo até levar à morte!",
            "nota": "Explicação clínica da mortalidade da deficiência de DDP."
        },
        {
            "id": 18742,
            "speaker": "Personagem [145]",
            "original_jp": "オレは氷の精だ。山へ帰りたいんだが、世界が真っ暗になっちまって...帰る道がわかんなくなっちゃってな...。",
            "curated_ptbr": "Eu sou um espírito do gelo.\nQueria voltar para a minha montanha, mas o mundo virou esse breu... e perdi o rumo de casa.",
            "nota": "Apresentação comovente do elemental gélido na Cosmosfera de Misha."
        },
        {
            "id": 18773,
            "speaker": "Sistema / Caixa Narrativa / Tutorial",
            "original_jp": "緑魔法【アナライザ】を紡ぎ出した!",
            "curated_ptbr": "Você teceu a Magia Verde [Análise]!",
            "nota": "Aquisição canônica da Magia Verde de percepção exploratória de Misha."
        },
        {
            "id": 18803,
            "speaker": "Atendente do Dive Shop",
            "original_jp": "インストールってのは、レーヴァテイルの身体にグラスノ結晶を直接差し込む技だ。",
            "curated_ptbr": "A Instalação é a técnica de inserir Cristais Grathnode diretamente no corpo de uma Reyvateil.",
            "nota": "Definição do implante de Cristais Grathnode na Porta de Instalação."
        },
        {
            "id": 18808,
            "speaker": "Atendente do Dive Shop",
            "original_jp": "毒を喰らってパワーアップCRするようなモノだ。",
            "curated_ptbr": "É exatamente como tomar veneno para aumentar a própria força.",
            "nota": "Metáfora visceral do desgaste biológico suportado pela donzela."
        },
        {
            "id": 18867,
            "speaker": "Personagem [110]",
            "original_jp": "これから行う儀式ってのは、オリカとライナーが共に永遠を誓う儀式なのよ。",
            "curated_ptbr": "Essa cerimônia que pretendem fazer é um rito onde você e o Lyner juram eternidade um ao outro!",
            "nota": "Silfa confronta Aurica sobre os votos nupciais no Nível 8 da Cosmosfera."
        },
        {
            "id": 18878,
            "speaker": "Aurica",
            "original_jp": "確かに自由はきかなくなるかもしれないけど...でも、なにも出来なくなるわけじゃない。",
            "curated_ptbr": "É verdade que posso perder um pouco da minha liberdade...\nmas isso não quer dizer que não poderei mais fazer nada.",
            "nota": "Maturação emocional e transcendência do medo do compromisso amoroso."
        },
        {
            "id": 18903,
            "speaker": "Sistema / Caixa Narrativa / Tutorial",
            "original_jp": "赤魔法【シルフのダンス】を紡ぎ出した!",
            "curated_ptbr": "Você teceu a Magia Vermelha [Dança da Silfa]!",
            "nota": "Consagração lírica da Magia Vermelha de Aurica após vencer a provação nupcial."
        }
    ]
}

report_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_083_report.json"
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(f"Report successfully saved to {report_path}")

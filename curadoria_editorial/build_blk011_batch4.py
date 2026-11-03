import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

batch4_data = [
    {
        "id": 2762,
        "event_file": "Event/401.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Este cabo aqui\nparece incrivelmente intrincado...",
        "verdict": "rewritten",
        "rationale": "Dêixis proximal precisa ('これは') e vocabulário técnico expressivo ('intrincado')."
    },
    {
        "id": 2763,
        "event_file": "Event/401.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Parece bem diferente dos outros cabos do elevador.",
        "verdict": "rewritten",
        "rationale": "Observação atenta do mecanismo de elevação."
    },
    {
        "id": 2764,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Misha!",
        "verdict": "approved_as_is",
        "rationale": "Chamado urgente e aflito de Lyner alcançando a parceira."
    },
    {
        "id": 2765,
        "event_file": "Event/618.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Lyner... Eu finalmente descobri...\num jeito de destruir o meu eu adulto.",
        "verdict": "rewritten",
        "rationale": "Tensão dramática e obsessão dolorosa de Misha em sua mente ('大きな自分を壊す方法')."
    },
    {
        "id": 2766,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Para com isso!\nSe fizer uma loucura dessas, você mesma vai morrer!",
        "verdict": "rewritten",
        "rationale": "Desespero protetor de Lyner tentando impedi-la do suicídio psicológico."
    },
    {
        "id": 2767,
        "event_file": "Event/618.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Antes morrer do que virar adulta!\nAdeus, Lyner!",
        "verdict": "rewritten",
        "rationale": "Rejeição visceral do amadurecimento e despedida dramática ('私、もう行くね')."
    },
    {
        "id": 2768,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Misha, não!!",
        "verdict": "rewritten",
        "rationale": "Grito desesperado no momento do ataque ('ミシャ!!')."
    },
    {
        "id": 2769,
        "event_file": "Event/618.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Por que você está me segurando?!",
        "verdict": "rewritten",
        "rationale": "Incompreensão e dor de Misha tentando se desvencilhar."
    },
    {
        "id": 2770,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Mas é óbvio!\nSe você morrer, acabou tudo, entende?!",
        "verdict": "rewritten",
        "rationale": "Apelo urgente à razão ('死んだら全てが終わるんだぞ!?')."
    },
    {
        "id": 2771,
        "event_file": "Event/618.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Mas se eu não fizer nada, uma hora eu vou crescer!\nE aí você vai me odiar para sempre!!",
        "verdict": "rewritten",
        "rationale": "Revelação do trauma central de Misha: o pavor de perder o amor de Lyner ao se tornar adulta."
    },
    {
        "id": 2772,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "O quê?!... Eu?!",
        "verdict": "rewritten",
        "rationale": "Incredulidade absoluta de Lyner diante da acusação ('俺が!?')."
    },
    {
        "id": 2773,
        "event_file": "Event/618.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Por isso... sai da minha frenteee!!",
        "verdict": "rewritten",
        "rationale": "Grito histérico e violento de fuga ('どいてーっ!!')."
    },
    {
        "id": 2774,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Guaaargh!!",
        "verdict": "rewritten",
        "rationale": "Vocalização do impacto físico violento do golpe sofrido por Lyner."
    },
    {
        "id": 2775,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Que pancada... violenta...",
        "verdict": "rewritten",
        "rationale": "Gemido atordoado de Lyner no chão ('強烈...だ...')."
    },
    {
        "id": 2776,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "...!! Droga!\nOnde foi parar a Misha?!",
        "verdict": "rewritten",
        "rationale": "Recobrando os sentidos em alerta imediato."
    },
    {
        "id": 2777,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Ela correu para o bosque...\nSe eu não for depressa, a vida dela corre perigo!\nPreciso correr para lá agora mesmo!",
        "verdict": "rewritten",
        "rationale": "Urgência máxima e resolução de perseguição protetora."
    },
    {
        "id": 2778,
        "event_file": "Event/618.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Que pancada... violenta...",
        "verdict": "rewritten",
        "rationale": "Eco da dor física enquanto se levanta."
    },
    {
        "id": 2779,
        "event_file": "Event/618.evd",
        "speaker": "Moradora do Mundo Inferior",
        "speaker_id": 13,
        "curated_ptbr": "Ora, ora... levou uma surra e tanto, hein?\nTalvez ela tenha achado melhor apagar você do mapa\ndo que conviver com o seu desprezo.",
        "verdict": "rewritten",
        "rationale": "Ironia cínica e perspicácia psicológica de Hama analisando a mente de Misha."
    },
    {
        "id": 2780,
        "event_file": "Event/618.evd",
        "speaker": "Moradora do Mundo Inferior",
        "speaker_id": 13,
        "curated_ptbr": "Bem, a verdade só a própria Misha sabe...\nembora você já não possa mais perguntar a ela, não é mesmo?",
        "verdict": "rewritten",
        "rationale": "Tom provocador e frio da guardiã das profundezas."
    },
    {
        "id": 2781,
        "event_file": "Event/618.evd",
        "speaker": "Moradora do Mundo Inferior",
        "speaker_id": 13,
        "curated_ptbr": "Mas tenho cá comigo que,\nse os sentimentos da Misha por você fossem mais intensos,\no destino poderia ter sido bem diferente.",
        "verdict": "rewritten",
        "rationale": "Reflexão afiada sobre o peso dos sentimentos na estabilidade da Cosmosfera."
    },
    {
        "id": 2782,
        "event_file": "Event/655.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Nível 8...",
        "verdict": "rewritten",
        "rationale": "Constatação solene da profundidade atingida na mente de Misha."
    },
    {
        "id": 2783,
        "event_file": "Event/655.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Será que a Misha conseguiu concluir\na Mudança de Paradigma em segurança...?",
        "verdict": "rewritten",
        "rationale": "Terminologia canônica 'Mudança de Paradigma' e preocupação protetora."
    },
    {
        "id": 2784,
        "event_file": "Event/655.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Q-que arrepio medonho no ar...\nNão me diga que deu tudo errado...?",
        "verdict": "rewritten",
        "rationale": "Pressentimento sinistro e calafrio diante do desastre mental ('激しくイヤな雰囲気')."
    },
    {
        "id": 2785,
        "event_file": "Event/655.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Não, não pode ser...\nVamos lá para fora conferir...",
        "verdict": "rewritten",
        "rationale": "Negação angustiada e impulso de verificar a realidade."
    },
    {
        "id": 2786,
        "event_file": "Event/655.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "M-mas o que... o que significa isso tudo...?! O mundo virou cinzas!\nE esta névoa... está sumindo...?!",
        "verdict": "rewritten",
        "rationale": "Choque visual estarrecedor diante da aniquilação do cenário da Cosmosfera ('灰になってる')."
    },
    {
        "id": 2787,
        "event_file": "Event/655.evd",
        "speaker": "Moradora do Mundo Inferior",
        "speaker_id": 13,
        "curated_ptbr": "Eu jamais imaginei que você faria uma proeza dessas...\nNem em pesadelo eu conceberia um estrago tão grande...",
        "verdict": "rewritten",
        "rationale": "Sarcasmo amargo e reprovação severa de Hama ('まさかここまでやってくれるとはね')."
    },
    {
        "id": 2788,
        "event_file": "Event/655.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Mas o que foi que aconteceu afinal?!\nA Misha está bem?!",
        "verdict": "rewritten",
        "rationale": "Desespero puro de Lyner pela segurança e integridade de Misha."
    },
    {
        "id": 2789,
        "event_file": "Event/655.evd",
        "speaker": "Moradora do Mundo Inferior",
        "speaker_id": 13,
        "curated_ptbr": "Por conta dessa última Mudança de Paradigma,\na psique profunda da Misha ruiu por completo.",
        "verdict": "rewritten",
        "rationale": "Diagnóstico psicológico estarrecedor do colapso da Cosmosfera ('深層心理は大きく崩壊した')."
    },
    {
        "id": 2790,
        "event_file": "Event/655.evd",
        "speaker": "Moradora do Mundo Inferior",
        "speaker_id": 13,
        "curated_ptbr": "É exatamente isto que acontece quando se força\numa Mudança de Paradigma sem o devido preparo emocional.\nOlha o que você fez... Francamente, que desastre absurdo...",
        "verdict": "rewritten",
        "rationale": "Condenação implacável da negligência emocional no Mergulho ('完全に準備が整っていない状態で')."
    },
    {
        "id": 2791,
        "event_file": "Event/655.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "E a culpa é minha?!",
        "verdict": "rewritten",
        "rationale": "Indignação defensiva e choque de Lyner ao ser culpado ('俺かよ!')."
    },
    {
        "id": 2792,
        "event_file": "Event/655.evd",
        "speaker": "Moradora do Mundo Inferior",
        "speaker_id": 13,
        "curated_ptbr": "Você... acha mesmo que não teve nada a ver com isso?!\nSe pensa assim, nunca mais ouse colocar os pés neste mundo!",
        "verdict": "rewritten",
        "rationale": "Fúria vingativa e expulsão categórica da guardiã ('二度とこの世界に足を踏み入れないで')."
    },
    {
        "id": 2793,
        "event_file": "Event/655.evd",
        "speaker": "Moradora do Mundo Inferior",
        "speaker_id": 13,
        "curated_ptbr": "Eu não pretendo dar as caras aqui nunca mais\naté que este mundo se restabeleça...",
        "verdict": "rewritten",
        "rationale": "Retirada definitiva da guardiã até a redenção do mundo interior."
    },
    {
        "id": 2794,
        "event_file": "Event/655.evd",
        "speaker": "Moradora do Mundo Inferior",
        "speaker_id": 13,
        "curated_ptbr": "Passar bem.",
        "verdict": "rewritten",
        "rationale": "Corte seco e desdém gélido de despedida ('それじゃ')."
    },
    {
        "id": 2795,
        "event_file": "Event/655.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Hama!!",
        "verdict": "approved_as_is",
        "rationale": "Chamado desesperado pelo nome da Guardiã da Mente de Misha."
    },
    {
        "id": 2796,
        "event_file": "Event/655.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "De qualquer forma...\npreciso achar a Misha antes de qualquer coisa...!!",
        "verdict": "rewritten",
        "rationale": "Determinação imediata em meio ao cenário devastado."
    },
    {
        "id": 2797,
        "event_file": "Event/951.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "...E-então...",
        "verdict": "rewritten",
        "rationale": "Gagueira tímida e embaraçada de Aurica no limiar do primeiro Mergulho."
    },
    {
        "id": 2798,
        "event_file": "Event/951.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "A gente... precisa mesmo mergulhar...?",
        "verdict": "rewritten",
        "rationale": "Hesitação vulnerável e insegurança característica de Aurica."
    },
    {
        "id": 2799,
        "event_file": "Event/951.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Hã? Não, eu não pretendo forçar você a nada, mas...",
        "verdict": "rewritten",
        "rationale": "Gentileza respeitosa e cavalheirismo protetor de Lyner."
    },
    {
        "id": 2800,
        "event_file": "Event/951.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Não é que eu ache uma péssima ideia nem nada...\né só que...",
        "verdict": "rewritten",
        "rationale": "Dilema interno de Aurica querendo e temendo a intimidade da Cosmosfera."
    },
    {
        "id": 2801,
        "event_file": "Event/951.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "É que é a minha primeira vez entrando numa Loja de Mergulho,\naí o nervosismo bateu forte...",
        "verdict": "rewritten",
        "rationale": "Correção crítica de gênero ('nervoso' -> 'o nervosismo bateu forte') e menção canônica à [Loja de Mergulho]."
    },
    {
        "id": 2802,
        "event_file": "Event/951.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "É mesmo? Não me diga que você...",
        "verdict": "rewritten",
        "rationale": "Surpresa compassiva de Lyner compreendendo a situação."
    },
    {
        "id": 2803,
        "event_file": "Event/951.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "É o meu primeiro Mergulho.\nEu nunca tive um parceiro nos meus tempos de Igreja.",
        "verdict": "rewritten",
        "rationale": "Histórico comovente da solidão e isolamento de Aurica na Igreja dos Santos."
    },
    {
        "id": 2804,
        "event_file": "Event/951.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Se você mergulhar comigo, Lyner...\nvai ser a minha primeira vez.",
        "verdict": "rewritten",
        "rationale": "Carga emocional e intimidade sagrada do vínculo entre Reyvateil e Cavaleiro ('あたしの初ダイブ')."
    },
    {
        "id": 2805,
        "event_file": "Event/951.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "...E-entendi...",
        "verdict": "rewritten",
        "rationale": "Tímida reação de Lyner sentindo o peso e a honra da confiança depositada nele."
    },
    {
        "id": 2806,
        "event_file": "Event/951.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "......",
        "verdict": "approved_as_is",
        "rationale": "Pausa carregada de emoção e silêncio cúmplice entre os dois."
    },
    {
        "id": 2807,
        "event_file": "Event/951.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "...Quer saber? É melhor deixarmos para outra hora.",
        "verdict": "rewritten",
        "rationale": "Delicadeza de Lyner oferecendo uma saída honrosa caso ela esteja desconfortável."
    },
    {
        "id": 2808,
        "event_file": "Event/951.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Não... eu quero ir!\nQuero ficar mais forte, nem que seja um pouquinho...\nEntão, por favor, cuide bem de mim.",
        "verdict": "rewritten",
        "rationale": "Determinação comovente de Aurica e fórmula de confiança mútua ('よろしくお願いします')."
    },
    {
        "id": 2809,
        "event_file": "Event/951.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Mas o meu mundo interior deve ser esquisito demais...\nentão, se você achar horrível, pode sair na mesma hora, tá...?",
        "verdict": "rewritten",
        "rationale": "Humildade e receio pueril de Aurica em expor suas fragilidades na Cosmosfera."
    }
]

# Validation
input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

hard_gate_errors = 0
lint_warnings = 0

for item in batch4_data:
    orig = input_map[item["id"]]
    trad = item["curated_ptbr"]
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig["original_jp"],
        traduzido=trad,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {item['id']}: {e}")

    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item['id']}: {a}")

print(f"Batch 4 ({len(batch4_data)} lines): Hard Gate Errors = {hard_gate_errors}, Lint Warnings = {lint_warnings}")
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_curated.json", "w", encoding="utf-8") as out:
    json.dump(batch4_data, out, ensure_ascii=False, indent=2)
print("Batch 4 saved successfully.")

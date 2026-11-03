import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

batch5_data = [
    {
        "id": 2810,
        "event_file": "Event/644.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Finalmente cheguei ao Nível 7...\nJá estou penetrando bem fundo na mente dela.",
        "verdict": "rewritten",
        "rationale": "Tom reflexivo de Lyner avaliando a profundidade psíquica na Cosmosfera ('随分深くなってきた')."
    },
    {
        "id": 2811,
        "event_file": "Event/644.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Mas... que calor sufocante é esse...?\nE nem parece calor de verão,\nparece o bafejo de uma fornalha ardente...",
        "verdict": "rewritten",
        "rationale": "Sensação física de calor opressivo com adjetivação expressiva ('炎の熱さ')."
    },
    {
        "id": 2812,
        "event_file": "Event/644.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Vou dar uma olhada lá fora...",
        "verdict": "rewritten",
        "rationale": "Decisão imediata de checar o exterior do santuário."
    },
    {
        "id": 2813,
        "event_file": "Event/644.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Uaaah!! O mundo inteiro está em chamas!!",
        "verdict": "rewritten",
        "rationale": "Choque visual estarrecedor diante do horizonte em chamas ('世界が燃えてるぞ')."
    },
    {
        "id": 2814,
        "event_file": "Event/644.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Mas que loucura...\no que significa tudo isso...?!",
        "verdict": "rewritten",
        "rationale": "Perplexidade diante do inferno interior."
    },
    {
        "id": 2815,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Finalmente encurralamos a fera.",
        "verdict": "rewritten",
        "rationale": "Dicção rude e caçadora de Jack cercando o monstro ('ようやく追い詰めたぜ')."
    },
    {
        "id": 2816,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Muito bem, sossega aí...\nSeja bonzinho e desista de uma vez.",
        "verdict": "rewritten",
        "rationale": "Comando autoritário e desdenhoso de Jack ('さあ、観念しな')."
    },
    {
        "id": 2817,
        "event_file": "Event/41.evd",
        "speaker": "Personagem [35]",
        "speaker_id": 35,
        "curated_ptbr": "Grrrrrr...",
        "verdict": "approved_as_is",
        "rationale": "Rosnado bestial ameaçador do monstro encurralado."
    },
    {
        "id": 2818,
        "event_file": "Event/41.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "E-ei, Jack... Pensando bem,\na gente veio até aqui sem nenhum plano de combate...",
        "verdict": "rewritten",
        "rationale": "Insegurança tardia de Lyner percebendo a imprudência da missão ('何も準備せずに')."
    },
    {
        "id": 2819,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "O tempo ruge, rapaz!\nNão temos folga para ficar de frescura!",
        "verdict": "rewritten",
        "rationale": "Impaciência pragmática de Jack acelerando o combate ('準備なんてしてられるかよ')."
    },
    {
        "id": 2820,
        "event_file": "Event/41.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Mas não teria sido bem melhor planejar\nconforme as fraquezas dele...?",
        "verdict": "rewritten",
        "rationale": "Argumento tático de Lyner questionando a abordagem direta."
    },
    {
        "id": 2821,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "...E aí? Vai querer dar meia-volta?",
        "verdict": "rewritten",
        "rationale": "Provocação irônica de Jack testando a fibra de Lyner."
    },
    {
        "id": 2822,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Paciência, bater em retirada por ora!",
        "verdict": "rewritten",
        "rationale": "Comando militar seco de recuo tático ('しゃーねえ、一旦退却だ')."
    },
    {
        "id": 2823,
        "event_file": "Event/41.evd",
        "speaker": "Sistema / Narração",
        "speaker_id": 14,
        "curated_ptbr": "Obteve o item [Pedaço de Papel]!",
        "verdict": "rewritten",
        "rationale": "Fórmula canônica de aquisição de item pelo jogador com colchetes de inventário."
    },
    {
        "id": 2824,
        "event_file": "Event/41.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "D-demos conta no sufoco...",
        "verdict": "rewritten",
        "rationale": "Alívio ofegante de Lyner após o confronto acirrado ('な、なんとか倒せたな')."
    },
    {
        "id": 2825,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Será que nós dois... no fim das contas...\nnão somos fortes pra caramba?!",
        "verdict": "rewritten",
        "rationale": "Correção crucial do desvio histórico da NISA (que inventou 'relieved or disappointed'), restaurando o entusiasmo gabola de Jack sobre a própria força."
    },
    {
        "id": 2826,
        "event_file": "Event/41.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Sei lá... Mas e aí, encontrou o que estava procurando?",
        "verdict": "rewritten",
        "rationale": "Desdém bem-humorado de Lyner trazendo o foco de volta ao item buscado."
    },
    {
        "id": 2827,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Que alívio. É isto aqui mesmo.",
        "verdict": "rewritten",
        "rationale": "Satisfação genuína de Jack encontrando o papel."
    },
    {
        "id": 2828,
        "event_file": "Event/41.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "...Um pedaço de papel rasgado...?\nNão me diga que você torrou todo o seu dinheiro com isso?!",
        "verdict": "rewritten",
        "rationale": "Perplexidade indignada de Lyner diante do gasto absurdo do mercenário ('全財産かけたのか')."
    },
    {
        "id": 2829,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Pedaço de papel rasgado?! Que disparate!\nVocê faz ideia de quanto eu paguei por isso?!",
        "verdict": "rewritten",
        "rationale": "Reação ofendida de Jack repelindo a simplificação de Lyner, expurgando o xingamento inventado pela NISA."
    },
    {
        "id": 2830,
        "event_file": "Event/41.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Sinceramente...\nQue tremenda idiotice.",
        "verdict": "rewritten",
        "rationale": "Julgamento seco e desbocado de Lyner sobre a tolice de Jack ('アホだな')."
    },
    {
        "id": 2831,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Espera lá!\nTem um segredo de Estado da maior importância escrito aqui, tá?!",
        "verdict": "rewritten",
        "rationale": "Defesa inflamada de Jack alegando a importância militar/estratégica do documento ('大変な機密')."
    },
    {
        "id": 2832,
        "event_file": "Event/41.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Tá, tá bom, sei...",
        "verdict": "rewritten",
        "rationale": "Desdém irônico e conformismo debochado de Lyner ('ああ、はいはい')."
    },
    {
        "id": 2833,
        "event_file": "Event/41.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Escuta o que eu estou dizendo!",
        "verdict": "rewritten",
        "rationale": "Protesto irritado de Jack exigindo ser ouvido ('聞けよ!')."
    },
    {
        "id": 2834,
        "event_file": "Event/41.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "O cansaço desabou de vez.\nVamos logo para Nemo.",
        "verdict": "rewritten",
        "rationale": "Fadiga cômica de Lyner querendo rumar direto para a estalagem de Nemo."
    },
    {
        "id": 2835,
        "event_file": "Event/784.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "...",
        "verdict": "approved_as_is",
        "rationale": "Despertar gradual em meio ao sono."
    },
    {
        "id": 2836,
        "event_file": "Event/784.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "......",
        "verdict": "approved_as_is",
        "rationale": "Pausa sensorial recobrando a consciência."
    },
    {
        "id": 2837,
        "event_file": "Event/784.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": ".........!!",
        "verdict": "rewritten",
        "rationale": "Susto súbito ao acordar do transe."
    },
    {
        "id": 2838,
        "event_file": "Event/784.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "Hah!!!",
        "verdict": "rewritten",
        "rationale": "Respiração entrecortada e espanto ao saltar da cama ('はっ!!!')."
    },
    {
        "id": 2839,
        "event_file": "Event/784.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "...Foi só um sonho...\nUfa...",
        "verdict": "rewritten",
        "rationale": "Alívio respiratório ('ふぅ...') ao perceber que tudo não passava de um pesadelo."
    },
    {
        "id": 2840,
        "event_file": "Event/784.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "...Que sonho mais esquisito.\nAlguém falava de um tal... 'campo de dados'...?\nAh, droga... já estou esquecendo os detalhes...",
        "verdict": "rewritten",
        "rationale": "Harmonização terminológica com 'campo de dados' (バイナリ野 / 情報野), superando o errôneo 'campo binário' da NISA."
    },
    {
        "id": 2841,
        "event_file": "Event/784.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "Hoje... é domingo.\nMas nem tenho nada para fazer, não tenho namorada...\nQue tédio medonho...",
        "verdict": "rewritten",
        "rationale": "Lamento existencial cômico do adolescente comum na simulação colegial."
    },
    {
        "id": 2842,
        "event_file": "Event/784.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "......",
        "verdict": "approved_as_is",
        "rationale": "Silêncio reflexivo contemplando o vazio da manhã de domingo."
    },
    {
        "id": 2843,
        "event_file": "Event/784.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "Mas ficar mofando aqui não adianta nada.\nQuem sabe eu não vou ao cinema ver um filme...?",
        "verdict": "rewritten",
        "rationale": "Resolução ativa do estudante saindo do marasmo ('こんな事していても仕方ない')."
    },
    {
        "id": 2844,
        "event_file": "Event/784.evd",
        "speaker": "Sistema / Caixa Narrativa / Tutorial",
        "speaker_id": 14,
        "curated_ptbr": "Esta é a cidade onde eu moro: Ciel.\nUm lugarejo pacato do interior,\ncom apenas algumas dezenas de milhares de habitantes.",
        "verdict": "rewritten",
        "rationale": "Apresentação clássica de prólogo de light novel / visual novel colegial ('詩恵留市' -> Ciel)."
    },
    {
        "id": 2845,
        "event_file": "Event/784.evd",
        "speaker": "Sistema / Caixa Narrativa / Tutorial",
        "speaker_id": 14,
        "curated_ptbr": "Pode ser pequena, mas não falta nada para viver bem.\nE o melhor de tudo: o ar é puro e a água é fresquinha!",
        "verdict": "rewritten",
        "rationale": "Orgulho suburbano e entusiasmo juvenil descrevendo o vilarejo ('空気がいい!水が美味い!')."
    },
    {
        "id": 2846,
        "event_file": "Event/784.evd",
        "speaker": "Sistema / Caixa Narrativa / Tutorial",
        "speaker_id": 14,
        "curated_ptbr": "...Bem, chega de conversa fiada\ne vamos ao que interessa: deixa eu me apresentar.",
        "verdict": "rewritten",
        "rationale": "Transição narrativa fluida e bem-humorada quebrando a quarta parede ('強がりはこれくらいにしておいて')."
    },
    {
        "id": 2847,
        "event_file": "Event/784.evd",
        "speaker": "Sistema / Caixa Narrativa / Tutorial",
        "speaker_id": 14,
        "curated_ptbr": "Eu sou Raina Harase.\nTenho 16 anos, sou aluno do primeiro ano do ensino médio\ne estou em plena fase de crescimento.",
        "verdict": "rewritten",
        "rationale": "Restauração do nome canônico da identidade simulada de Lyner no minigame colegial (原瀬頼奈 - Raina Harase)."
    },
    {
        "id": 2848,
        "event_file": "Event/784.evd",
        "speaker": "Sistema / Caixa Narrativa / Tutorial",
        "speaker_id": 14,
        "curated_ptbr": "E, para o meu desespero em plena flor da idade,\neu não tenho nem uma namoradinha sequer.\nVivia prometendo que este ano seria diferente...\nmas namoro não se arranja sozinho, né?",
        "verdict": "rewritten",
        "rationale": "Dramatização calorosa da angústia romântica adolescente ('多感な時期に', '一人で創れるものじゃないしな')."
    },
    {
        "id": 2849,
        "event_file": "Event/784.evd",
        "speaker": "Sistema / Caixa Narrativa / Tutorial",
        "speaker_id": 14,
        "curated_ptbr": "Sendo assim, cá estou eu neste domingo desolado e no mais absoluto tédio.\nO jeito é bater perna pela cidade afora para matar o tempo.",
        "verdict": "rewritten",
        "rationale": "Fechamento descontraído e coloquial de abertura de cena ('ブラブラと街に出かけよう')."
    }
]

# Validation
input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

hard_gate_errors = 0
lint_warnings = 0

for item in batch5_data:
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

print(f"Batch 5 ({len(batch5_data)} lines): Hard Gate Errors = {hard_gate_errors}, Lint Warnings = {lint_warnings}")
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_curated.json", "w", encoding="utf-8") as out:
    json.dump(batch5_data, out, ensure_ascii=False, indent=2)
print("Batch 5 saved successfully.")

import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

batch6_data = [
    {
        "id": 2850,
        "event_file": "Event/961.evd",
        "speaker": "Personagem [89]",
        "speaker_id": 89,
        "curated_ptbr": "Ora, se não é a senhorita Misha!\nVeio aqui para encolher de novo?",
        "verdict": "rewritten",
        "rationale": "Recepção animada e cortês do operador do Reator Três ('あ!これはミシャさん')."
    },
    {
        "id": 2851,
        "event_file": "Event/961.evd",
        "speaker": "Personagem [89]",
        "speaker_id": 89,
        "curated_ptbr": "Entendido!\nVamos começar imediatamente!",
        "verdict": "rewritten",
        "rationale": "Prontidão e presteza técnica ('早速行きますよ')."
    },
    {
        "id": 2852,
        "event_file": "Event/961.evd",
        "speaker": "Personagem [89]",
        "speaker_id": 89,
        "curated_ptbr": "Muito bem, lá vamos nós!\nReator Três, acionar!",
        "verdict": "rewritten",
        "rationale": "Comando operacional enérgico ativando o maquinário ('三号炉、起動!')."
    },
    {
        "id": 2853,
        "event_file": "Event/961.evd",
        "speaker": "Personagem [89]",
        "speaker_id": 89,
        "curated_ptbr": "Se quiser voltar ao tamanho adulto de novo,\né só aparecer quando quiser! Hehehe.",
        "verdict": "rewritten",
        "rationale": "Simpatia e risinho característico ('へへへ' -> 'Hehehe'), mantendo a vocalização natural."
    },
    {
        "id": 2854,
        "event_file": "Event/54.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "A Magia Vermelha é uma Canção\nvoltada para o ataque aos inimigos.",
        "verdict": "rewritten",
        "rationale": "Explicação canônica de combate de Aurica sobre a 'Magia Vermelha' (赤魔法)."
    },
    {
        "id": 2855,
        "event_file": "Event/54.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Quanto mais você acumular energia antes de descarregá-la,\nmais devastador será o seu poder.",
        "verdict": "rewritten",
        "rationale": "Mecânica de carregamento de Burst da Magia da Canção ('力を溜めれば溜めるほど')."
    },
    {
        "id": 2856,
        "event_file": "Event/54.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Muito bem, vou entoar o meu canto.",
        "verdict": "rewritten",
        "rationale": "Postura dedicada e solene de Aurica preparando-se para cantar ('謳ってみる')."
    },
    {
        "id": 2857,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Lyner!\nVocê... fez o Don Leon para mim, não foi?\nMuito obrigada...",
        "verdict": "rewritten",
        "rationale": "Gratidão comovida de Aurica recebendo seu mascote Don Leon (どんすけ) feito à mão."
    },
    {
        "id": 2858,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Graças a você, uma mudança maravilhosa começou a acontecer.\nO equilíbrio entre este mundo e o domínio da Aurica Maligna\nestá oscilando aos poucos.",
        "verdict": "rewritten",
        "rationale": "Terminologia canônica para a persona sombria de Aurica: 'Aurica Maligna' (悪魔オリカ)."
    },
    {
        "id": 2859,
        "event_file": "Event/751.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Hã? Quer dizer que...",
        "verdict": "rewritten",
        "rationale": "Curiosidade atenta de Lyner acompanhando o raciocínio dela ('それって...')."
    },
    {
        "id": 2860,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Quer dizer que a consciência da Aurica está florescendo como nunca.\nA vontade de confiar em alguém... o desejo de fazer o bem...\nsentimentos assim estão ganhando força nela.",
        "verdict": "rewritten",
        "rationale": "Explicação profunda do florescimento moral e emocional de Aurica na Cosmosfera ('良心', '誰かを信じてみよう')."
    },
    {
        "id": 2861,
        "event_file": "Event/751.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Que alívio... fico muito feliz por isso.",
        "verdict": "rewritten",
        "rationale": "Calor humano sincero e reconfortante de Lyner."
    },
    {
        "id": 2862,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Sabe, Lyner...\nQue tal irmos até Stonehenge?\nAcho que podemos alcançar a Mudança de Paradigma agora.",
        "verdict": "rewritten",
        "rationale": "Convite carinhoso e solene rumo ao marco ritual de Stonehenge para a Mudança de Paradigma."
    },
    {
        "id": 2863,
        "event_file": "Event/751.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "A sério?!",
        "verdict": "rewritten",
        "rationale": "Surpresa vibrante diante do anúncio inesperado ('え!?')."
    },
    {
        "id": 2864,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Eu... não conseguia confiar na Aurica do mundo real...\nNão conseguia acreditar em mim mesma.",
        "verdict": "rewritten",
        "rationale": "Confissão dilacerante da persona interior sobre a falta de auto-estima da Aurica real."
    },
    {
        "id": 2865,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Quando este mundo da 'Razão'\nfoi subjugado pelo domínio da Aurica Maligna...\ncheguei a pensar que talvez uma consciência nem me fizesse mais falta...",
        "verdict": "rewritten",
        "rationale": "Dramatização poética do conflito psíquico entre a 'Razão' (理性), a Aurica Maligna e a Consciência (良心)."
    },
    {
        "id": 2866,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Mas você costurou o Don Leon... e deu de presente para ela...\nE foi graças a isso que uma centelha de esperança\nrenasceu no coração da Aurica.",
        "verdict": "rewritten",
        "rationale": "Ponto de virada dramático onde o ato de amor de Lyner restaura a esperança despedaçada."
    },
    {
        "id": 2867,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Foi aí que me dei conta de como eu estava sendo tola...\nNão conseguir confiar em si mesma é a coisa mais dolorosa que existe.",
        "verdict": "rewritten",
        "rationale": "Auto-análise sincera e dolorosa ('自分自身が信じられないのって、最悪だよね')."
    },
    {
        "id": 2868,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "A Aurica do mundo real me devolveu a esperança.\nEla me mostrou que eu ainda sou indispensável para ela.",
        "verdict": "rewritten",
        "rationale": "Reconciliação entre o ego e a persona interior da heroína."
    },
    {
        "id": 2869,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Por isso mesmo,\nsinto que uma Mudança de Paradigma pode acontecer a qualquer instante.",
        "verdict": "rewritten",
        "rationale": "Presságio radiante da cura e avanço para níveis mais profundos da mente."
    },
    {
        "id": 2870,
        "event_file": "Event/751.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Então era isso...\nMas é impressionante como você mesma consegue pressentir\na chegada da Mudança de Paradigma.",
        "verdict": "rewritten",
        "rationale": "Admiração de Lyner perante a lucidez e maturidade alcançada por Aurica."
    },
    {
        "id": 2871,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Afinal de contas, quando se alcança uma profundidade dessas,\na gente passa a compreender muito mais coisas.",
        "verdict": "rewritten",
        "rationale": "Sabedoria das camadas profundas da Cosmosfera ('これくらいまで深くなってくると')."
    },
    {
        "id": 2872,
        "event_file": "Event/751.evd",
        "speaker": "Aurica",
        "speaker_id": 11,
        "curated_ptbr": "Vem, vamos lá!",
        "verdict": "rewritten",
        "rationale": "Espontaneidade luminosa e afetuosa chamando o parceiro pela mão."
    },
    {
        "id": 2873,
        "event_file": "Event/751.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Caramba!! Já começou a acontecer!!",
        "verdict": "rewritten",
        "rationale": "Entusiasmo e surpresa com o desencadeamento imediato do fenômeno da Mudança de Paradigma ('さっそく発生したぞ')."
    }
]

# Validation
input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

hard_gate_errors = 0
lint_warnings = 0

for item in batch6_data:
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

print(f"Batch 6 ({len(batch6_data)} lines): Hard Gate Errors = {hard_gate_errors}, Lint Warnings = {lint_warnings}")
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch6_curated.json", "w", encoding="utf-8") as out:
    json.dump(batch6_data, out, ensure_ascii=False, indent=2)
print("Batch 6 saved successfully.")

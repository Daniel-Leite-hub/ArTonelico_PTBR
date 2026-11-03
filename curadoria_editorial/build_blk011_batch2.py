import sys
import json

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

batch2_data = [
    {
        "id": 2678,
        "event_file": "Event/251.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Ué? Consertaram esta parede aqui.",
        "verdict": "rewritten",
        "rationale": "Espanto espontâneo de Misha com dêixis proximal ('ここの壁')."
    },
    {
        "id": 2679,
        "event_file": "Event/251.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Também, com o rombo daquele tamanho,\né claro que iam tapar.",
        "verdict": "rewritten",
        "rationale": "Tom pragmático de Lyner comentando o rombo anterior ('アレだけデカイ穴')."
    },
    {
        "id": 2680,
        "event_file": "Event/251.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Sendo assim,\nvamos ter que procurar outro caminho.",
        "verdict": "rewritten",
        "rationale": "Conclusão natural com quebra rítmica sem partículas órfãs."
    },
    {
        "id": 2681,
        "event_file": "Event/234.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Pensando bem, como eu só vivo cantando,\nnunca segurei uma arma na vida.",
        "verdict": "rewritten",
        "rationale": "Reflexão íntima de Misha sobre seu papel como Reyvateil ('謳ってばかり')."
    },
    {
        "id": 2682,
        "event_file": "Event/234.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "O Lyner até vai lá, mas fico boba de ver\ncomo a Krusche consegue empunhar um trambolho daquele tamanho.",
        "verdict": "rewritten",
        "rationale": "Espanto bem-humorado de Misha diante do porte da motosserra de Krusche."
    },
    {
        "id": 2683,
        "event_file": "Event/234.evd",
        "speaker": "Krusche",
        "speaker_id": 6,
        "curated_ptbr": "Aquilo ali tem todo um macete na pegada, sabia?",
        "verdict": "rewritten",
        "rationale": "Cacoete técnico de Krusche explicando a empunhadura ('持ち方にコツがある')."
    },
    {
        "id": 2684,
        "event_file": "Event/234.evd",
        "speaker": "Krusche",
        "speaker_id": 6,
        "curated_ptbr": "Eu praticamente balanço aquilo na base do recuo.\nSe fosse na força bruta, meus braços não aguentariam uma batalha sequer.",
        "verdict": "rewritten",
        "rationale": "Explicação física da inércia mecânica na empunhadura da motosserra."
    },
    {
        "id": 2685,
        "event_file": "Event/234.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Pois é. Até eu ficaria moído se tentasse empunhar aquilo.",
        "verdict": "rewritten",
        "rationale": "Concordância honesta de Lyner sobre o peso descomunal da ferramenta."
    },
    {
        "id": 2686,
        "event_file": "Event/234.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Falando nisso, Krusche...\npor que raios você usa uma motosserra como arma?",
        "verdict": "rewritten",
        "rationale": "Curiosidade descontraída de Misha interrogando a mecânica ('何でチェーンソウを')."
    },
    {
        "id": 2687,
        "event_file": "Event/234.evd",
        "speaker": "Krusche",
        "speaker_id": 6,
        "curated_ptbr": "Ué? Serve para o trabalho e para a batalha,\ndois coelhos de uma vez só.\nAlém do mais, que preguiça de aprender outra arma.",
        "verdict": "rewritten",
        "rationale": "Pragmatismo despojado de Krusche unindo utilidade e preguiça ('一石二鳥', '面倒')."
    },
    {
        "id": 2688,
        "event_file": "Event/234.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Dois coelhos com uma motosserra...?\nQue criatura sinistra você é.",
        "verdict": "rewritten",
        "rationale": "Reação cômica de choque de Misha ('怖い人だね')."
    },
    {
        "id": 2689,
        "event_file": "Event/234.evd",
        "speaker": "Krusche",
        "speaker_id": 6,
        "curated_ptbr": "Que petulância!\nSinistra é você, Misha,\nque vive invocando coisas bizarras do além!",
        "verdict": "rewritten",
        "rationale": "Contra-ataque mordaz de Krusche aludindo às invocações excêntricas de Misha ('得体の知れないモノ')."
    },
    {
        "id": 2690,
        "event_file": "Event/234.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Sinistra, eu?! Quis dizer adorável, né?!\nQuer que eu cante aqui mesmo para você ver?!",
        "verdict": "rewritten",
        "rationale": "Orgulho ferido e provocação inflamada de Misha ameaçando soltar Magia da Canção dentro da loja."
    },
    {
        "id": 2691,
        "event_file": "Event/234.evd",
        "speaker": "Krusche",
        "speaker_id": 6,
        "curated_ptbr": "Pois cai dentro!",
        "verdict": "rewritten",
        "rationale": "Desafio provocativo e audacioso de Krusche ('望むところよ!')."
    },
    {
        "id": 2692,
        "event_file": "Event/234.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Pelo amor de Deus!\nParem com isso, as duas!!",
        "verdict": "rewritten",
        "rationale": "Pânico e desespero cômico de Lyner no papel de apaziguador ('頼む!やめてくれー!!')."
    },
    {
        "id": 2693,
        "event_file": "Event/234.evd",
        "speaker": "Personagem [82]",
        "speaker_id": 82,
        "curated_ptbr": "Ei, vocês aí!\nNada de vandalismo dentro do meu estabelecimento!!",
        "verdict": "rewritten",
        "rationale": "Grito de autoridade furiosa do dono da loja ('店内で暴れるなー!')."
    },
    {
        "id": 2694,
        "event_file": "Event/234.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "P-perdão, mil desculpas!",
        "verdict": "rewritten",
        "rationale": "Gagueira constrangida e pedido de desculpas atropelado de Lyner."
    },
    {
        "id": 2695,
        "event_file": "Event/234.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Francamente...\nTenham piedade de mim...",
        "verdict": "rewritten",
        "rationale": "Desabafo exausto de Lyner com suas companheiras briguentas ('勘弁してくれよ')."
    },
    {
        "id": 2696,
        "event_file": "Event/611.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Ah, não! Já é hora de ir dormir?!\nNão quero, eu quero brincar mais!",
        "verdict": "rewritten",
        "rationale": "Manha e birra infantil adorável de Misha na Cosmosfera ('えーっ!もう寝るの?')."
    },
    {
        "id": 2697,
        "event_file": "Event/611.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Vamos passear em algum outro lugar!",
        "verdict": "rewritten",
        "rationale": "Entusiasmo infantil e apelo aventureiro ('もっと他のところへ')."
    },
    {
        "id": 2698,
        "event_file": "Event/285.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Como é que a gente abre esta porta?",
        "verdict": "rewritten",
        "rationale": "Dêixis proximal precisa ('この扉' -> esta porta) e oralidade natural."
    },
    {
        "id": 2699,
        "event_file": "Event/285.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Esta aqui...\nsó a Senhora Tastiella tem autorização para abrir.",
        "verdict": "rewritten",
        "rationale": "Tratamento respeitoso à anciã e guardiã Teru Tastiella."
    },
    {
        "id": 2700,
        "event_file": "Event/285.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "...O quê?!\nEntão não tem outro jeito: vamos ter que arrombar!",
        "verdict": "rewritten",
        "rationale": "Impulsividade típica de Lyner querendo derrubar obstáculos à força."
    },
    {
        "id": 2701,
        "event_file": "Event/285.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Isso se conseguir, rapaz.\nEssa blindagem parece dura feito pedra.",
        "verdict": "rewritten",
        "rationale": "Ceticismo calejado e provocador do mercenário Jack ('結構固そうだぜ')."
    },
    {
        "id": 2702,
        "event_file": "Event/285.evd",
        "speaker": "Jack",
        "speaker_id": 4,
        "curated_ptbr": "Bem, se a marreta falhar,\no jeito é procurar algum caminho alternativo.",
        "verdict": "rewritten",
        "rationale": "Pragmatismo expedicionário de Jack ('回り道')."
    },
    {
        "id": 2703,
        "event_file": "Event/248.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Ué? Parou de funcionar.",
        "verdict": "rewritten",
        "rationale": "Percepção espontânea de Lyner diante do mecanismo travado."
    },
    {
        "id": 2704,
        "event_file": "Event/248.evd",
        "speaker": "Misha",
        "speaker_id": 2,
        "curated_ptbr": "Mas é claro. Ainda não ativamos o sistema de controle\ncom uma Bomba de Raio.",
        "verdict": "rewritten",
        "rationale": "Terminologia canônica padronizada 'Bomba de Raio' (雷弾) e explicação técnica precisa de Misha."
    },
    {
        "id": 2705,
        "event_file": "Event/347.evd",
        "speaker": "Radolf",
        "speaker_id": 7,
        "curated_ptbr": "Chegamos até aqui,\nmas a Colina do Canto é uma ruína vastíssima.",
        "verdict": "rewritten",
        "rationale": "Fixação do topônimo canônico 'Colina do Canto' (謳う丘 - Utau Oka) no singular e dicção nobre de Radolf."
    },
    {
        "id": 2706,
        "event_file": "Event/347.evd",
        "speaker": "Radolf",
        "speaker_id": 7,
        "curated_ptbr": "Se procurarmos às cegas,\ndificilmente encontraremos o que buscamos...",
        "verdict": "rewritten",
        "rationale": "Raciocínio sóbrio e prudente do Cavaleiro Sagrado ('闇雲に探しても')."
    },
    {
        "id": 2707,
        "event_file": "Event/347.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Mesmo assim, não temos pista alguma e o tempo ruge...\nO jeito é vasculhar tudo.",
        "verdict": "rewritten",
        "rationale": "Contraste dramático: o pragmatismo impaciente de Lyner perante a cautela de Radolf."
    },
    {
        "id": 2708,
        "event_file": "Event/347.evd",
        "speaker": "Radolf",
        "speaker_id": 7,
        "curated_ptbr": "Quanta leviandade...",
        "verdict": "rewritten",
        "rationale": "Desconforto moral e choque de temperamentos de Radolf diante do improviso de Lyner ('いい加減すぎる')."
    },
    {
        "id": 2709,
        "event_file": "Event/347.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "...Radolf?",
        "verdict": "approved_as_is",
        "rationale": "Interrogação cautelosa de Lyner percebendo a desolação do companheiro."
    },
    {
        "id": 2710,
        "event_file": "Event/347.evd",
        "speaker": "Radolf",
        "speaker_id": 7,
        "curated_ptbr": "Não, é que, por mais incerto que fosse o local,\nlimitar a diretriz a 'Colina do Canto'...",
        "verdict": "rewritten",
        "rationale": "Desilusão de Radolf com a falta de rigor da Igreja dos Santos, mantendo 'Colina do Canto'."
    },
    {
        "id": 2711,
        "event_file": "Event/347.evd",
        "speaker": "Radolf",
        "speaker_id": 7,
        "curated_ptbr": "...No passado,\na Igreja demonstrava um mínimo de zelo e retidão...",
        "verdict": "rewritten",
        "rationale": "Nostalgia amarga e crítica moral de Radolf à decadência institucional da Igreja ('誠意があったものなのだが')."
    },
    {
        "id": 2712,
        "event_file": "Event/798.evd",
        "speaker": "Reyvateil da Cosmosfera",
        "speaker_id": 12,
        "curated_ptbr": "Raina! Você voltou para me ajudar!",
        "verdict": "rewritten",
        "rationale": "Preservação da persona colegial de Shurelia no minigame chamando Lyner pelo seu alter ego 'Raina' (頼奈)."
    },
    {
        "id": 2713,
        "event_file": "Event/798.evd",
        "speaker": "Reyvateil da Cosmosfera",
        "speaker_id": 12,
        "curated_ptbr": "Sendo assim, vamos nessa!",
        "verdict": "rewritten",
        "rationale": "Disposição enérgica de heroína tokusatsu entrando em batalha."
    },
    {
        "id": 2714,
        "event_file": "Event/798.evd",
        "speaker": "Reyvateil da Cosmosfera",
        "speaker_id": 12,
        "curated_ptbr": "...Vejam só!\nRaina! A lavagem cerebral da Leila ainda não terminou!",
        "verdict": "rewritten",
        "rationale": "Alerta tático dramático identificando os nomes da simulação (Raina e Leila) e a brecha no controle mental."
    },
    {
        "id": 2715,
        "event_file": "Event/798.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "É sério?!",
        "verdict": "rewritten",
        "rationale": "Reação vibrante e instantânea de esperança do protagonista."
    },
    {
        "id": 2716,
        "event_file": "Event/798.evd",
        "speaker": "Reyvateil da Cosmosfera",
        "speaker_id": 12,
        "curated_ptbr": "Sim! São aquelas três esferas diante da Leila\nque estão mantendo o transe pelo lado de fora!",
        "verdict": "rewritten",
        "rationale": "Esclarecimento da mecânica de combate do minigame com linguagem natural e dramática."
    },
    {
        "id": 2717,
        "event_file": "Event/798.evd",
        "speaker": "Lyner (Voz Interior / Memória na Cosmosfera)",
        "speaker_id": 1,
        "curated_ptbr": "Quer dizer que,\nse destruirmos apenas essas três esferas...?",
        "verdict": "rewritten",
        "rationale": "Dedução tática de Lyner alinhada ao objetivo da missão."
    },
    {
        "id": 2718,
        "event_file": "Event/798.evd",
        "speaker": "Reyvateil da Cosmosfera",
        "speaker_id": 12,
        "curated_ptbr": "Exato... A Leila se libertará dessa maldição!",
        "verdict": "rewritten",
        "rationale": "Conclusão épica de Shurelia em seu papel de Singer Angel ('呪縛から解き放たれる')."
    },
    {
        "id": 2719,
        "event_file": "Event/798.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "...Ué? Onde é que eu estou...?",
        "verdict": "rewritten",
        "rationale": "Desorientação cômica de Lyner ao ser ejetado do minigame após a derrota."
    },
    {
        "id": 2720,
        "event_file": "Event/798.evd",
        "speaker": "Shurelia",
        "speaker_id": 3,
        "curated_ptbr": "Seja bem-vindo de volta.\nParece que deu Game Over para nós.",
        "verdict": "rewritten",
        "rationale": "Polidez impassível e amável de Lady Shurelia acolhendo Lyner na tela de Game Over ('ゲームオーバー')."
    },
    {
        "id": 2721,
        "event_file": "Event/798.evd",
        "speaker": "Lyner",
        "speaker_id": 1,
        "curated_ptbr": "Puxa vida... de novo...?",
        "verdict": "rewritten",
        "rationale": "Frustração bem-humorada de Lyner diante da repetição da derrota ('ありゃりゃ...またか')."
    },
    {
        "id": 2722,
        "event_file": "Event/798.evd",
        "speaker": "Shurelia",
        "speaker_id": 3,
        "curated_ptbr": "Como podemos tentar quantas vezes quisermos,\nquem sabe não vale a pena encararmos de novo daqui a pouco?",
        "verdict": "rewritten",
        "rationale": "Incentivo paciente e sereno de Shurelia com perspectiva de jogabilidade ilimitada ('何度でも挑戦出来る')."
    }
]

# Validation
input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

hard_gate_errors = 0
lint_warnings = 0

for item in batch2_data:
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

print(f"Batch 2 ({len(batch2_data)} lines): Hard Gate Errors = {hard_gate_errors}, Lint Warnings = {lint_warnings}")
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_curated.json", "w", encoding="utf-8") as out:
    json.dump(batch2_data, out, ensure_ascii=False, indent=2)
print("Batch 2 saved successfully.")

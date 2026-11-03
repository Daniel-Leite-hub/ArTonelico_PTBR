import json

batch4 = [
    {
        "id": 3041,
        "curated_ptbr": "Lyner...\nPor favor, cuide da Aurica e proteja ela.",
        "verdict": "rewritten",
        "rationale": "Apelo carinhoso e comovente de Misha ('オリカを護ってあげて'), superando a cobrança ríspida da tradução preliminar."
    },
    {
        "id": 3042,
        "curated_ptbr": "Porque ter você ao lado dela é a única coisa que a Aurica mais deseja neste momento.",
        "verdict": "rewritten",
        "rationale": "Percepção sensível de Misha sobre a necessidade afetiva de Aurica."
    },
    {
        "id": 3043,
        "curated_ptbr": "Diz uma coisa, Misha...\nO que realmente significa... \"proteger\" alguém?",
        "verdict": "rewritten",
        "rationale": "Indagação profunda de Lyner sobre a natureza do dever de guardião ('「護る」って...どういう事なんだろう')."
    },
    {
        "id": 3044,
        "curated_ptbr": "...O quê?",
        "verdict": "rewritten",
        "rationale": "Surpresa de Misha diante do questionamento filosófico inesperado de Lyner."
    },
    {
        "id": 3045,
        "curated_ptbr": "Lyner... Você acha que proteger alguém se resume a defender o corpo dos ataques inimigos, não é?",
        "verdict": "rewritten",
        "rationale": "Distinção canônica entre defesa física (守る) e resguardo espiritual/afetivo (護る)."
    },
    {
        "id": 3046,
        "curated_ptbr": "Ué, e não é isso?",
        "verdict": "rewritten",
        "rationale": "Inocência pragmática do jovem cavaleiro diante do conceito ampliado de proteção."
    },
    {
        "id": 3047,
        "curated_ptbr": "Se você pensar só assim, jamais conseguirá resguardar a Aurica de verdade.",
        "verdict": "rewritten",
        "rationale": "Alerta maduro de Misha sobre a vulnerabilidade emocional da amiga."
    },
    {
        "id": 3048,
        "curated_ptbr": "Será...?",
        "verdict": "rewritten",
        "rationale": "Dúvida sincera instigando o amadurecimento interior de Lyner."
    },
    {
        "id": 3049,
        "curated_ptbr": "...Tenho certeza.",
        "verdict": "rewritten",
        "rationale": "Afirmação categórica e carinhosa de Misha ('...ええ')."
    },
    {
        "id": 3050,
        "curated_ptbr": "Então me diz: como é que eu faço pra proteger ela direito?",
        "verdict": "rewritten",
        "rationale": "Vontade sincera de aprender a agir como um verdadeiro parceiro."
    },
    {
        "id": 3051,
        "curated_ptbr": "Essa resposta você vai ter que descobrir por conta própria, senhor Lyner.",
        "verdict": "rewritten",
        "rationale": "Provocação afetuosa de Misha usando o tratamento carinhoso 'ライナーくん'."
    },
    {
        "id": 3052,
        "curated_ptbr": "......\nTsc... Não precisava ser tão maldosa.",
        "verdict": "rewritten",
        "rationale": "Resmungo mimado e infantil de Lyner ('ちぇっ...意地悪いな')."
    },
    {
        "id": 3053,
        "curated_ptbr": "Ah... Pensando bem, aquela receita da ocarina que me pediram na Cosmosfera outro dia... Preciso perguntar sobre ela pra Misha.",
        "verdict": "rewritten",
        "rationale": "Monólogo de Lyner conectando os eventos da mente com a realidade física."
    },
    {
        "id": 3054,
        "curated_ptbr": "Misha, você tem um minutinho?",
        "verdict": "rewritten",
        "rationale": "Abordagem casual e amigável ('ミシャ。ちょっといいか?')."
    },
    {
        "id": 3055,
        "curated_ptbr": "Ah, Lyner! Que foi?",
        "verdict": "rewritten",
        "rationale": "Recepção animada e luminosa de Misha."
    },
    {
        "id": 3056,
        "curated_ptbr": "Vim aqui porque queria te pedir um favor. Por acaso você ainda tem o Cartão de Receita daquela ocarina que eu fiz pra você no passado?",
        "verdict": "rewritten",
        "rationale": "Pedido nostálgico evocando a memória do artesanato de infância."
    },
    {
        "id": 3057,
        "curated_ptbr": "O quê?!... Mas por que você tá querendo isso agora...?",
        "verdict": "rewritten",
        "rationale": "Reação sobressaltada de Misha ao ouvir sobre a relíquia esquecida."
    },
    {
        "id": 3058,
        "curated_ptbr": "É que, lá dentro da sua Cosmosfera, uma ocarina chamada Hama acabou quebrando... e eu queria muito consertar ela.",
        "verdict": "rewritten",
        "rationale": "Explicação afetuosa de Lyner desejando curar a ferida da mente de Misha."
    },
    {
        "id": 3059,
        "curated_ptbr": "......",
        "verdict": "approved_as_is",
        "rationale": "Choque silencioso e culpa acumulada no coração de Misha preservados."
    },
    {
        "id": 3060,
        "curated_ptbr": "Pensando bem, já que fui eu mesmo quem inventou ela, é até meio esquisito vir pedir a receita pra você, mas...",
        "verdict": "rewritten",
        "rationale": "Descontração embaraçada de Lyner amenizando o clima ('おかしな話だけど...')."
    },
    {
        "id": 3061,
        "curated_ptbr": "Não... quem tem que pedir desculpas sou eu. Tem uma coisa que eu passei todo esse tempo sem coragem de te confessar...",
        "verdict": "rewritten",
        "rationale": "Início da dolorosa confissão reprimida por anos no peito da heroína."
    },
    {
        "id": 3062,
        "curated_ptbr": "Aquela ocarina que você me deu de presente de despedida na infância... ela quebrou quando o Bourd me sequestrou...",
        "verdict": "rewritten",
        "rationale": "Revelação do trauma capital de Misha e a origem da perda de seu tesouro."
    },
    {
        "id": 3063,
        "curated_ptbr": "E eu cuidava dela com tanto carinho... Tinha até batizado ela com o nome de Hama...",
        "verdict": "rewritten",
        "rationale": "Tradução comovente e exata de '大切にしてたのに' e a conexão com a persona psíquica [Hama]."
    },
    {
        "id": 3064,
        "curated_ptbr": "Mesmo sabendo que você dedicou todo o seu coração pra fazer ela pra mim... Me perdoa, de verdade...",
        "verdict": "rewritten",
        "rationale": "Lágrimas e culpa sincera de Misha ('一生懸命創ってくれたものなのに... 本当にごめんなさい')."
    },
    {
        "id": 3065,
        "curated_ptbr": "...Então era isso? Não se preocupe com isso! Eu faço outra novinha pra você. Com todo o meu afeto, exatamente como fiz daquela vez.",
        "verdict": "rewritten",
        "rationale": "Compreensão calorosa e reconfortante de Lyner renovando a promessa de carinho."
    },
    {
        "id": 3066,
        "curated_ptbr": "...Lyner... muito obrigada... Então eu posso mesmo ficar esperando por ela?",
        "verdict": "rewritten",
        "rationale": "Sorriso entre lágrimas de Misha recuperando a esperança ('お願いしちゃっていい?')."
    },
    {
        "id": 3067,
        "curated_ptbr": "Você obteve o Cartão de Receita:\n\"Ocarina\"!",
        "verdict": "rewritten",
        "rationale": "Notificação formal de obtenção do item de síntese sem colisão de colchetes."
    },
    {
        "id": 3068,
        "curated_ptbr": "O botão foi pressionado.",
        "verdict": "rewritten",
        "rationale": "Registro neutro e direto de ação de acionamento mecânico no cenário."
    },
    {
        "id": 3069,
        "curated_ptbr": "Lyner, olha esta sala!\nQue saudade me dá!",
        "verdict": "rewritten",
        "rationale": "Exclamação nostálgica de Misha ao revisitar a câmara onde se reencontraram."
    },
    {
        "id": 3070,
        "curated_ptbr": "É... Embora eu preferisse nem me lembrar muito daquela situação...",
        "verdict": "rewritten",
        "rationale": "Ironia sutil de Lyner relembrando o cárcere desconfortável ('あまり思い出したくないけどな')."
    },
    {
        "id": 3071,
        "curated_ptbr": "Mas foi aqui que a gente se reencontrou!",
        "verdict": "rewritten",
        "rationale": "Insistência romântica e animada de Misha valorizando o marco afetivo da dupla."
    },
    {
        "id": 3072,
        "curated_ptbr": "Será que vai ser assim? Na hora do nosso casamento, vão apresentar este lugar pros convidados e dizer...",
        "verdict": "rewritten",
        "rationale": "Devaneio matrimonial divertido e travesso de Misha ('お式の時には')."
    },
    {
        "id": 3073,
        "curated_ptbr": "\"O noivo em cativeiro foi resgatado pela noiva, e a primeira obra em conjunto do casal teve início exatamente aqui!\"",
        "verdict": "rewritten",
        "rationale": "Paródia cômica do cerimonial clássico de matrimônio japonês ('二人の共同作業')."
    },
    {
        "id": 3074,
        "curated_ptbr": "Já imaginou se falarem uma coisa dessas?!",
        "verdict": "rewritten",
        "rationale": "Gargalhada cúmplice de Misha imaginando a reação de todos ('なーんて言われるのかしら!')."
    },
    {
        "id": 3075,
        "curated_ptbr": "...De onde você tirou essa loucura?",
        "verdict": "rewritten",
        "rationale": "Embaraço cômico e desconcertado de Lyner tentando conter as fantasias da amiga."
    },
    {
        "id": 3076,
        "curated_ptbr": "Hehehe! Mas, falando sério, bate uma saudade tão gostosa...",
        "verdict": "rewritten",
        "rationale": "Transição suave de Misha da brincadeira para o sentimento terno genuíno."
    },
    {
        "id": 3077,
        "curated_ptbr": "Se você não tivesse sido arrastado pra cá, talvez a gente nem tivesse se reencontrado de novo.",
        "verdict": "rewritten",
        "rationale": "Reflexão sensível sobre o destino entrelaçado dos dois companheiros."
    },
    {
        "id": 3078,
        "curated_ptbr": "...É, pode ser.",
        "verdict": "rewritten",
        "rationale": "Concordância afetuosa e reflexiva de Lyner acolhendo a ideia ('...そうだな')."
    },
    {
        "id": 3079,
        "curated_ptbr": "M-mas o que é isso...?!",
        "verdict": "rewritten",
        "rationale": "Espanto diante da arquitetura ancestral colossal na profundeza da Torre."
    },
    {
        "id": 3080,
        "curated_ptbr": "Que foi? É a primeira vez que você põe os pés por aqui também, Lyner?",
        "verdict": "rewritten",
        "rationale": "Indagação prática de Jack percebendo a hesitação do cavaleiro."
    },
    {
        "id": 3081,
        "curated_ptbr": "Nunca vi nada parecido com isto na vida. Devemos estar muito próximos do núcleo central.",
        "verdict": "rewritten",
        "rationale": "Avaliação topográfica de Lyner estimando a proximidade com o reator principal."
    },
    {
        "id": 3082,
        "curated_ptbr": "Incrível... Você tá me proporcionando uma experiência verdadeiramente impagável, Lyner.",
        "verdict": "rewritten",
        "rationale": "Fascínio científico da prodígio mecânica Krusche desbravando ruínas míticas."
    },
    {
        "id": 3083,
        "curated_ptbr": "Nossa, que demais!! Já desidratou tudo?!",
        "verdict": "rewritten",
        "rationale": "Entusiasmo infantil da garota admirando a velocidade da desidratação ('もう乾いちゃったの!?')."
    },
    {
        "id": 3084,
        "curated_ptbr": "Muito obrigada! Vou te dar uma também, moço!",
        "verdict": "rewritten",
        "rationale": "Correção de gênero: agradecimento no feminino por ser uma menina ('ありがとう! お兄さんにも1つあげるわ')."
    },
    {
        "id": 3085,
        "curated_ptbr": "Você obteve o item:\n\"Fruta Seca\"!",
        "verdict": "rewritten",
        "rationale": "Mensagem padronizada de recompensa com aspas e quebra natural."
    }
]

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_012.json", "w", encoding="utf-8") as f:
    json.dump(batch4, f, indent=2, ensure_ascii=False)

print(f"Batch 4 written: {len(batch4)} items.")

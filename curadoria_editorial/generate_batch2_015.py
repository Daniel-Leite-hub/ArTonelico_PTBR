import json

batch2 = [
    {
        "id": 3801,
        "curated_ptbr": "Narl... Belo nome.\nTem uma sonoridade doce e inebriante, como um feitiço de amor.",
        "verdict": "rewritten",
        "rationale": "Jack destila galanteio experiente (媚薬のような魔力) com charme e sem decalque."
    },
    {
        "id": 3802,
        "curated_ptbr": "Ai, moço... Não fala assim que eu fico toda sem jeito...",
        "verdict": "rewritten",
        "rationale": "Narl reage com timidez graciosa e espontânea (照れちゃいますー)."
    },
    {
        "id": 3803,
        "curated_ptbr": "A-A... Aaaatchim!!",
        "verdict": "rewritten",
        "rationale": "Vocalização cômica do espirro estrondoso de Mestre Pochoma cortando o clima (ヘッブシッ!!)."
    },
    {
        "id": 3804,
        "curated_ptbr": "...",
        "verdict": "rewritten",
        "rationale": "Pausa atônita de Jack após o espirro do velho."
    },
    {
        "id": 3805,
        "curated_ptbr": "Ei, Lyner!\nO que você está arrumando aí parado?",
        "verdict": "rewritten",
        "rationale": "Jack desconversa disfarçando a vergonha e puxa a orelha de Lyner."
    },
    {
        "id": 3806,
        "curated_ptbr": "Larga de ficar plantado com cara de pastel e vai pedir para o velho te ensinar o Grathmeld.",
        "verdict": "rewritten",
        "rationale": "Jack incisivo e direto (ボケッとしてねぇで) empurrando Lyner para a síntese."
    },
    {
        "id": 3807,
        "curated_ptbr": "A-Ah... Certo...",
        "verdict": "rewritten",
        "rationale": "Lyner é pego de surpresa e concorda sem jeito."
    },
    {
        "id": 3808,
        "curated_ptbr": "Escuta, ouvi dizer que o seu avô é um Melder famoso. É verdade?",
        "verdict": "rewritten",
        "rationale": "Lyner pergunta a Narl sobre o ofício lendário de Mestre Pochoma (高名なメルク)."
    },
    {
        "id": 3809,
        "curated_ptbr": "Sim, é verdade!\nEle pode não aparentar grande coisa, mas no passado era uma lenda viva.",
        "verdict": "rewritten",
        "rationale": "Narl confirma o prestígio lendário do avô com carinho bem-humorado."
    },
    {
        "id": 3810,
        "curated_ptbr": "Será que ele ainda aceitaria ensinar as técnicas de Grathmeld?",
        "verdict": "rewritten",
        "rationale": "Lyner indaga educadamente sobre a disposição do mestre para ensinar."
    },
    {
        "id": 3811,
        "curated_ptbr": "Com certeza! Ele vai adorar.\nO vovô vive entediado sem ter o que fazer mesmo.",
        "verdict": "rewritten",
        "rationale": "Narl encoraja Lyner ressaltando o tédio cômico do ancião (暇を持てあましてる)."
    },
    {
        "id": 3812,
        "curated_ptbr": "Pode ir falar com ele sem medo.",
        "verdict": "rewritten",
        "rationale": "Narl instrui Lyner a abordar o avô diretamente."
    },
    {
        "id": 3813,
        "curated_ptbr": "Entendi, vou fazer isso.",
        "verdict": "rewritten",
        "rationale": "Lyner aceita o conselho e se prepara para falar com o ancião."
    },
    {
        "id": 3814,
        "curated_ptbr": "Jack deixou o grupo.",
        "verdict": "rewritten",
        "rationale": "Mensagem determinística de sistema limpa e concisa."
    },
    {
        "id": 3815,
        "curated_ptbr": "O sistema voltou a operar...",
        "verdict": "rewritten",
        "rationale": "Lyner constata a restauração das funções energéticas (状態が復帰したか)."
    },
    {
        "id": 3816,
        "curated_ptbr": "E quais são os materiais necessários?",
        "verdict": "rewritten",
        "rationale": "Misha pergunta pragmática sobre a lista de síntese."
    },
    {
        "id": 3817,
        "curated_ptbr": "Vejamos... Um Yulastrino e um Gancho Invertido...",
        "verdict": "rewritten",
        "rationale": "Terminologia canônica fixada do Glossário Mestre: Yulastrino e Gancho Invertido (インバートフック)."
    },
    {
        "id": 3818,
        "curated_ptbr": "...",
        "verdict": "rewritten",
        "rationale": "Silêncio cético e desconfiado de Misha."
    },
    {
        "id": 3819,
        "curated_ptbr": "Lyner... Você por acaso sabe\no que são essas coisas?",
        "verdict": "rewritten",
        "rationale": "Misha questiona a ignorância de Lyner com quebra de linha natural."
    },
    {
        "id": 3820,
        "curated_ptbr": "Bem... Para falar a verdade, nunca ouvi falar de nenhum dos dois.",
        "verdict": "rewritten",
        "rationale": "Lyner admite sem rodeios que não faz ideia do que são os itens."
    },
    {
        "id": 3821,
        "curated_ptbr": "Puxa vida! Você sempre aceita tudo sem pensar!\nVê se pesquisa antes de prometer as coisas!",
        "verdict": "rewritten",
        "rationale": "Misha dá uma bronca cheia de atitude na impulsividade crônica de Lyner (また安請け合いして!)."
    },
    {
        "id": 3822,
        "curated_ptbr": "Calma aí!... Esse tal de Yulastrino... Acho que sei do que se trata.",
        "verdict": "rewritten",
        "rationale": "Jack intervém com sua experiência de mundo lembrando-se do artefato sagrado."
    },
    {
        "id": 3823,
        "curated_ptbr": "Que tal darmos um pulo no templo de Em Pheyna?\nQuase certo que encontramos por lá.",
        "verdict": "rewritten",
        "rationale": "Jack orienta o grupo rumo ao santuário sagrado dos Teru em Em Pheyna."
    },
    {
        "id": 3824,
        "curated_ptbr": "Certo. Então vamos primeiro ao templo.",
        "verdict": "rewritten",
        "rationale": "Lyner toma a decisão da rota com objetividade."
    },
    {
        "id": 3825,
        "curated_ptbr": "Quanto ao Gancho Invertido, eu conheço bem.",
        "verdict": "rewritten",
        "rationale": "Krusche anuncia que tem a resposta para a outra metade da receita, evitando cacófatos."
    },
    {
        "id": 3826,
        "curated_ptbr": "Por pura coincidência, estou com o Cartão de Receita dele.",
        "verdict": "rewritten",
        "rationale": "Krusche explica que possui a receita rara por acaso (ちょっとした縁があってね)."
    },
    {
        "id": 3827,
        "curated_ptbr": "Não brinca! Você é demais, Krusche!",
        "verdict": "rewritten",
        "rationale": "Lyner empolgado com a revelação da amiga inventora."
    },
    {
        "id": 3828,
        "curated_ptbr": "Então só precisamos sintetizar esse gancho, não é?",
        "verdict": "rewritten",
        "rationale": "Lyner resume a tarefa com entusiasmo prático."
    },
    {
        "id": 3829,
        "curated_ptbr": "Mas olha... A receita é dificílima. Nem eu consegui fabricar.\n...Vai encarar mesmo assim?",
        "verdict": "rewritten",
        "rationale": "Krusche desafia a habilidade de Lyner com seriedade e orgulho ferido de artesã."
    },
    {
        "id": 3830,
        "curated_ptbr": "Você acha mesmo que eu fugiria do desafio?",
        "verdict": "rewritten",
        "rationale": "Resposta audaciosa e heroica de Lyner (俺が『やらない』って言うと思うか?)."
    },
    {
        "id": 3831,
        "curated_ptbr": "Tudo bem. Fique com este cartão por enquanto.",
        "verdict": "rewritten",
        "rationale": "Krusche cede e confia o cartão nas mãos dele."
    },
    {
        "id": 3832,
        "curated_ptbr": "Mas fique avisado! Cuide muito bem dele!\nSe você sujar ou amassar, eu acabo com a sua raça!",
        "verdict": "rewritten",
        "rationale": "Krusche ameaça Lyner com seu temperamento explosivo e possessivo por tecnologia."
    },
    {
        "id": 3833,
        "curated_ptbr": "Você obteve o Cartão de Receita:\n[SínC: Herança da Supercivilização?]!",
        "verdict": "rewritten",
        "rationale": "Mensagem do sistema com terminologia canônica e alinhamento de tags com BLK_EVD_010."
    },
    {
        "id": 3834,
        "curated_ptbr": "N-Nossa, que agressividade...",
        "verdict": "rewritten",
        "rationale": "Lyner estremece com o tom intimidador de Krusche."
    },
    {
        "id": 3835,
        "curated_ptbr": "Não podemos perder tempo voltando à cidade. Vamos direto para a entrada do laboratório!",
        "verdict": "rewritten",
        "rationale": "Lyner comanda a urgência da missão em Event/268."
    },
    {
        "id": 3836,
        "curated_ptbr": "Lyner, posso entrar?",
        "verdict": "rewritten",
        "rationale": "Misha bate à porta do quarto pedindo permissão de forma tímida e delicada."
    },
    {
        "id": 3837,
        "curated_ptbr": "Sabe aquele negócio da instalação...? Que tal experimentarmos agora?",
        "verdict": "rewritten",
        "rationale": "Misha introduz o tema íntimo da Instalação com hesitação disfarçada de casualidade."
    },
    {
        "id": 3838,
        "curated_ptbr": "H-Hã?! Como assim, do nada...?",
        "verdict": "rewritten",
        "rationale": "Lyner é pego totalmente desprevenido com a proposta repentina."
    },
    {
        "id": 3839,
        "curated_ptbr": "Dizem que com a instalação a Magia da Canção fica muito mais poderosa. Eu quero ficar forte para proteger você, Lyner.",
        "verdict": "rewritten",
        "rationale": "Misha expressa sua motivação genuína e amorosa de fortalecer seu canto para proteger Lyner."
    },
    {
        "id": 3840,
        "curated_ptbr": "Assim nós vamos conseguir alcançar lugares que antes estavam fora do nosso alcance.",
        "verdict": "rewritten",
        "rationale": "Misha argumenta a utilidade prática para a jornada do grupo."
    },
    {
        "id": 3841,
        "curated_ptbr": "Bem, você tem razão nisso, mas...",
        "verdict": "rewritten",
        "rationale": "Lyner pondera relutante sabendo que o processo é desconfortável para a Reyvateil."
    },
    {
        "id": 3842,
        "curated_ptbr": "Eu quero estar ao seu lado, Lyner!\nQuero ficar muito mais forte para te ajudar.\nPor favor, faça a instalação em mim.",
        "verdict": "rewritten",
        "rationale": "Declaração tocante de Misha implorando pela conexão física e fônica da instalação."
    },
    {
        "id": 3843,
        "curated_ptbr": "T-Tudo bem, eu faço...\nMas você tem certeza absoluta? Não está fazendo isso contra a sua vontade?",
        "verdict": "rewritten",
        "rationale": "Lyner se preocupa com os sentimentos de Misha antes de aceitar."
    },
    {
        "id": 3844,
        "curated_ptbr": "De jeito nenhum! Pelo contrário, estou até animada.\nAfinal, a canção ganha vários efeitos especiais.",
        "verdict": "rewritten",
        "rationale": "Misha tenta esconder o medo demonstrando empolgação infantil."
    },
    {
        "id": 3845,
        "curated_ptbr": "Só que... Ouvi dizer que dói um pouquinho na hora da inserção, então mentiria se dissesse que não estou com medo.\nSeja gentil comigo...",
        "verdict": "rewritten",
        "rationale": "Misha revela sua vulnerabilidade feminina e pede carinho e suavidade (優しくしてね...)."
    },
    {
        "id": 3846,
        "curated_ptbr": "C-Certo. Vou ser o mais cuidadoso possível.",
        "verdict": "rewritten",
        "rationale": "Lyner assume o compromisso solene de não machucá-la."
    },
    {
        "id": 3847,
        "curated_ptbr": "Obrigada...\nVocê sempre foi atencioso desse jeito.",
        "verdict": "rewritten",
        "rationale": "Misha agradece comovida pela consideração de infância de Lyner."
    },
    {
        "id": 3848,
        "curated_ptbr": "Se você não estiver com nenhum Cristal Grathnode,\npode usar este aqui.\nO efeito não é grande coisa, mas o choque da inserção é bem menor.",
        "verdict": "rewritten",
        "rationale": "Misha entrega o cristal básico para minimizar o impacto fônico da primeira vez."
    },
    {
        "id": 3849,
        "curated_ptbr": "Obteve o Cristal Grathnode [Canção +10%]!",
        "verdict": "rewritten",
        "rationale": "Terminologia canônica consagrada em BLK_EVD_014 ID 3529 para 詩1割増サービス."
    },
    {
        "id": 3850,
        "curated_ptbr": "A minha Porta de Instalação fica bem no alto do meu colo.",
        "verdict": "rewritten",
        "rationale": "Consistência terminológica canônica de 'Porta de Instalação' (インストールポイント)."
    }
]

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_015.json', 'w', encoding='utf-8') as f:
    json.dump(batch2, f, ensure_ascii=False, indent=2)

print(f"Batch 2 generated with {len(batch2)} dialogues.")

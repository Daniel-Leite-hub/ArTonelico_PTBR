import json

batch4 = [
    {
        "id": 3901,
        "curated_ptbr": "Este lugar...\nTem um ar incrivelmente nostálgico...",
        "verdict": "rewritten",
        "rationale": "Lyner reflete sobre a atmosfera acolhedora e nostálgica do nível da Cosmosfera em Event/734."
    },
    {
        "id": 3902,
        "curated_ptbr": "O cenário deixou de ser uma escola e virou uma cidadezinha comum... O que será que nos aguarda desta vez?",
        "verdict": "rewritten",
        "rationale": "Lyner observa a mutação do cenário psíquico de Aurica de escola para vilarejo."
    },
    {
        "id": 3903,
        "curated_ptbr": "Ei, patife.\nTem certeza de que deseja perambular por este nível?",
        "verdict": "rewritten",
        "rationale": "Don Leon usa seu vocativo arcaico e austero (貴様) alertando Lyner solenemente."
    },
    {
        "id": 3904,
        "curated_ptbr": "Mas é claro.\nDe onde veio essa pergunta, assim do nada...?",
        "verdict": "rewritten",
        "rationale": "Lyner estranha a hesitação misteriosa do guardião samurai."
    },
    {
        "id": 3905,
        "curated_ptbr": "Não é nada. Apenas não se assuste com o que quer que seus olhos testemunhem.",
        "verdict": "rewritten",
        "rationale": "Aviso profético de Don Leon sobre as revelações que estão por vir na mente de Aurica."
    },
    {
        "id": 3906,
        "curated_ptbr": "Lyner, hoje tenho algo especial que gostaria de lhe entregar.",
        "verdict": "rewritten",
        "rationale": "Shurelia se dirige a Lyner com elegância régia e afeto sincero em Event/884."
    },
    {
        "id": 3907,
        "curated_ptbr": "Hã? O que seria?",
        "verdict": "rewritten",
        "rationale": "Lyner curioso e atento à deusa da Torre."
    },
    {
        "id": 3908,
        "curated_ptbr": "Pensei que pudesse ser útil em combate.\nTome, aqui está.",
        "verdict": "rewritten",
        "rationale": "Shurelia entrega o presente com simplicidade carinhosa."
    },
    {
        "id": 3909,
        "curated_ptbr": "Uma fita? É de uma tonalidade linda.",
        "verdict": "rewritten",
        "rationale": "Lyner elogia a cor bonita da fita sem ainda desconfiar do propósito dela."
    },
    {
        "id": 3910,
        "curated_ptbr": "Chama-se Fita de Topologia.\nComo fazia muito tempo que eu não criava nada, acabei ficando exausta.",
        "verdict": "rewritten",
        "rationale": "Shurelia batiza o item com seu nome técnico canônico (トポロジーリボン) e confessa a fadiga."
    },
    {
        "id": 3911,
        "curated_ptbr": "Obrigado pelo esforço.\nE como exatamente esse item deve ser usado?",
        "verdict": "rewritten",
        "rationale": "Lyner agradece educadamente e busca entender a função prática."
    },
    {
        "id": 3912,
        "curated_ptbr": "É um artefato que aprimora drasticamente o poder de uma Reyvateil.",
        "verdict": "rewritten",
        "rationale": "Shurelia explica a amplificação mágica proporcionada pela fita de fônica."
    },
    {
        "id": 3913,
        "curated_ptbr": "Não apenas amplifica a resistência física e mental, como também eleva a velocidade de Burst.",
        "verdict": "rewritten",
        "rationale": "Consistência terminológica canônica de mecânicas de combate: velocidade de Burst (バーストスピード)."
    },
    {
        "id": 3914,
        "curated_ptbr": "E deve permitir que ela suporte instalações arriscadas sem maiores danos.",
        "verdict": "rewritten",
        "rationale": "Shurelia destaca a proteção oferecida durante instalações complexas."
    },
    {
        "id": 3915,
        "curated_ptbr": "Puxa, isso é fantástico!",
        "verdict": "rewritten",
        "rationale": "Reação entusiasmada e positiva de Lyner."
    },
    {
        "id": 3916,
        "curated_ptbr": "Bem, fazia tanto tempo que eu não praticava o Grathmeld que fiquei um pouco insegura com o resultado.",
        "verdict": "rewritten",
        "rationale": "Shurelia demonstra sua modéstia tocante em relação à sua perícia ancestral de síntese."
    },
    {
        "id": 3917,
        "curated_ptbr": "Pode confiar no seu talento!\nVou usar com muito carinho.",
        "verdict": "rewritten",
        "rationale": "Lyner encoraja Shurelia com gentileza e entusiasmo sincero."
    },
    {
        "id": 3918,
        "curated_ptbr": "Fico feliz... Só que, a rigor, minha intenção era criar algo que o próprio Lyner pudesse equipar.",
        "verdict": "rewritten",
        "rationale": "Shurelia revela o propósito original da criação com ingenuidade doce."
    },
    {
        "id": 3919,
        "curated_ptbr": "Mas quando terminei a síntese, percebi que ela não surte o menor efeito em quem não for uma Reyvateil...",
        "verdict": "rewritten",
        "rationale": "Shurelia lamenta que o acessório só sirva para Reyvateils."
    },
    {
        "id": 3920,
        "curated_ptbr": "Ah, entendi...",
        "verdict": "rewritten",
        "rationale": "Lyner assimila a informação com simpatia."
    },
    {
        "id": 3921,
        "curated_ptbr": "Peraí... Então quer dizer que a sua ideia original era fazer com que EU usasse essa fita?!",
        "verdict": "rewritten",
        "rationale": "A ficha de Lyner cai com hilaridade cômica perfeita ao perceber o que ela planejava."
    },
    {
        "id": 3922,
        "curated_ptbr": "Sim. Haveria algum problema nisso?",
        "verdict": "rewritten",
        "rationale": "Shurelia responde com total inocência e serenidade divina (何か問題あった?)."
    },
    {
        "id": 3923,
        "curated_ptbr": "É óbvio que há um problema!\nOnde já se viu um homem amarrar uma fita no cabelo?!",
        "verdict": "rewritten",
        "rationale": "Lyner entra em choque machucado em seu orgulho juvenil (男がリボンつけてどうするんですか!?)."
    },
    {
        "id": 3924,
        "curated_ptbr": "Diremos que é a vanguarda da alta moda. Ninguém vai achar estranho... Provavelmente.",
        "verdict": "rewritten",
        "rationale": "Shurelia tenta justificar com moda de vanguarda e hesita com graça (きっと)."
    },
    {
        "id": 3925,
        "curated_ptbr": "Mas EU acho estranho!",
        "verdict": "rewritten",
        "rationale": "Lyner protesta enfático defendendo sua dignidade."
    },
    {
        "id": 3926,
        "curated_ptbr": "...E eu tinha certeza de que combinaria tanto com você...",
        "verdict": "rewritten",
        "rationale": "Shurelia murmura com um biquinho desapontado adorável (結構似合うと思ったのに)."
    },
    {
        "id": 3927,
        "curated_ptbr": "Obteve o item [Fita de Topologia]!",
        "verdict": "rewritten",
        "rationale": "Mensagem determinística de obtenção do item-chave."
    },
    {
        "id": 3928,
        "curated_ptbr": "Lyner, posso entrar no seu quarto?",
        "verdict": "rewritten",
        "rationale": "Shurelia pede permissão para entrar nos aposentos de Lyner."
    },
    {
        "id": 3929,
        "curated_ptbr": "Uma cidade inteira?! Que lugar é este...?",
        "verdict": "rewritten",
        "rationale": "Lyner se surpreende ao descobrir uma metrópole inteira nas entranhas da Torre em Event/87."
    },
    {
        "id": 3930,
        "curated_ptbr": "Este lugar se chama Beco Vagalume.",
        "verdict": "rewritten",
        "rationale": "Misha apresenta a cidade pelo nome canônico estabelecido 'Beco Vagalume' (ほたる横丁)."
    },
    {
        "id": 3931,
        "curated_ptbr": "Entendi... Então não é apenas uma fortaleza da Tenba.",
        "verdict": "rewritten",
        "rationale": "Lyner percebe que não se trata apenas de uma base militar da corporação."
    },
    {
        "id": 3932,
        "curated_ptbr": "Não se engane: é uma fortaleza da Tenba também.",
        "verdict": "rewritten",
        "rationale": "Misha pontua a dupla natureza da localidade com autoridade."
    },
    {
        "id": 3933,
        "curated_ptbr": "De fato, é uma vila onde moram pessoas comuns, mas a cidade inteira é um produto da Tenba.",
        "verdict": "rewritten",
        "rationale": "Misha explica o modelo corporativo totalitário de moradia da Tenba."
    },
    {
        "id": 3934,
        "curated_ptbr": "Uma ilha completamente artificial.\nAté o último parafuso... Tudo foi fabricado pela Tenba.",
        "verdict": "rewritten",
        "rationale": "Misha detalha a engenharia integralmente fabricada pela corporação monopolista."
    },
    {
        "id": 3935,
        "curated_ptbr": "Aquele setor onde você lutou há pouco fica logo abaixo daqui: é o gerador de força.",
        "verdict": "rewritten",
        "rationale": "Misha mapeia a geografia vertical da estrutura mecânica (動力部)."
    },
    {
        "id": 3936,
        "curated_ptbr": "E aqui em cima é a parte residencial.",
        "verdict": "rewritten",
        "rationale": "Divisão urbana clara entre maquinário e habitação."
    },
    {
        "id": 3937,
        "curated_ptbr": "Surpreendente, não é?",
        "verdict": "rewritten",
        "rationale": "Misha busca a reação de Lyner com sorriso orgulhoso de quem conhece a tecnologia."
    },
    {
        "id": 3938,
        "curated_ptbr": "Eu fiquei de queixo caído quando vi pela primeira vez.",
        "verdict": "rewritten",
        "rationale": "Misha relembra seu próprio espanto infantil ao contemplar a cidade pela primeira vez."
    },
    {
        "id": 3939,
        "curated_ptbr": "Esta é a verdadeira força dos habitantes do Mundo Inferior.",
        "verdict": "rewritten",
        "rationale": "Exaltação antropológica da tenacidade humana sob o Mar de Morte (下の世界に住む人達の力)."
    },
    {
        "id": 3940,
        "curated_ptbr": "Uma energia colossal aliada a um espírito pioneiro insaciável... E mais...",
        "verdict": "rewritten",
        "rationale": "Misha descreve a vitalidade voraz dos povos terrenos (どん欲なまでのフロンティア精神)."
    },
    {
        "id": 3941,
        "curated_ptbr": "Uma busca por inovação que não mede meios nem limites.",
        "verdict": "rewritten",
        "rationale": "Síntese filosófica da ambição científica da Tenba (手段を選ばない技術革新)."
    },
    {
        "id": 3942,
        "curated_ptbr": "Em outras palavras: uma terra habitada por pessoas que almejam o progresso a qualquer custo.",
        "verdict": "rewritten",
        "rationale": "Misha equilibra o juízo de valor com maturidade analítica."
    },
    {
        "id": 3943,
        "curated_ptbr": "O oposto absoluto da calmaria de Platina...",
        "verdict": "rewritten",
        "rationale": "Contraste dramático profundo com o isolacionismo estagnado e aristocrático de Platina."
    },
    {
        "id": 3944,
        "curated_ptbr": "...Então este é o poder dos povos lá de baixo...",
        "verdict": "rewritten",
        "rationale": "Lyner comovido ao romper com os preconceitos ensinados pelos nobres da Torre."
    },
    {
        "id": 3945,
        "curated_ptbr": "Venha, precisamos ir depressa até o porto.",
        "verdict": "rewritten",
        "rationale": "Misha apressa os passos retomando o objetivo imediato."
    },
    {
        "id": 3946,
        "curated_ptbr": "Lyner!\nQuais são as notícias?!",
        "verdict": "rewritten",
        "rationale": "Radolf indaga ansioso com dicção de cavaleiro honrado em Event/368."
    },
    {
        "id": 3947,
        "curated_ptbr": "Conseguimos resgatar a Aurica, mas o Bispo Falss...",
        "verdict": "rewritten",
        "rationale": "Lyner relata o resgate de Aurica e a tragédia com o clérigo maior da Igreja."
    },
    {
        "id": 3948,
        "curated_ptbr": "Foi contaminado pelo vírus.",
        "verdict": "rewritten",
        "rationale": "Ayatane completa a frase com sua calma fria e cirúrgica (ウイルスに汚染されたよ)."
    },
    {
        "id": 3949,
        "curated_ptbr": "O quê?!",
        "verdict": "rewritten",
        "rationale": "Radolf em choque devastador com o destino sombrio de seu superior espiritual."
    },
    {
        "id": 3950,
        "curated_ptbr": "De todo modo, vamos recompor as forças e tentar outra investida.",
        "verdict": "rewritten",
        "rationale": "Lyner focado na missão traça o plano de reagrupamento tático (体勢を立て直して)."
    }
]

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_015.json', 'w', encoding='utf-8') as f:
    json.dump(batch4, f, ensure_ascii=False, indent=2)

print(f"Batch 4 generated with {len(batch4)} dialogues.")

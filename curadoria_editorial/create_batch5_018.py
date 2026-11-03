# -*- coding: utf-8 -*-
import json

batch5 = [
    {
        "id": 4681,
        "curated_ptbr": "Armadura vermelha... Deixe-me ver.\nNão me recordo de ter visto ninguém assim por aqui...",
        "verdict": "rewritten",
        "rationale": "Ponderação atenciosa de Claire em 2 linhas balanceadas sem pontuação órfã."
    },
    {
        "id": 4682,
        "curated_ptbr": "Entendo...",
        "verdict": "rewritten",
        "rationale": "Reação desapontada, porém educada de Lyner."
    },
    {
        "id": 4683,
        "curated_ptbr": "Se for um guerreiro desse tipo... talvez valha a pena perguntar na Igreja.",
        "verdict": "rewritten",
        "rationale": "Sugestão lógica de Claire indicando a instituição militar e religiosa da Igreja."
    },
    {
        "id": 4684,
        "curated_ptbr": "Desculpe não ter sido\nde grande ajuda...",
        "verdict": "rewritten",
        "rationale": "Gentileza polida de Claire com quebra sem fratura sintática."
    },
    {
        "id": 4685,
        "curated_ptbr": "De forma alguma. Eu é que peço desculpas por chegar perguntando tão de repente.",
        "verdict": "rewritten",
        "rationale": "Modéstia cortês de Lyner ao responder à dona do bistrô (こちらこそ唐突ですみません)."
    },
    {
        "id": 4686,
        "curated_ptbr": "Ah, a propósito, Lyner.\nDesde aquela ocasião,\ncomecei a tecer uma canção nova.",
        "verdict": "rewritten",
        "rationale": "Uso poético do verbo 'tecer canção' (曲を紡ぎ始めてる) típico do universo e da arte das Reyvateils."
    },
    {
        "id": 4687,
        "curated_ptbr": "Isso sim é algo pelo qual vale a pena esperar! Ah, como anseio me embriagar ao som da sua voz um segundo mais cedo!",
        "verdict": "rewritten",
        "rationale": "Expressão dramática e canastrã de Jack (一秒でも早く貴方に酔いしれたい), superando o simplório 'I can't wait to hear it'."
    },
    {
        "id": 4688,
        "curated_ptbr": "Hehe, obrigada.\nVenha ouvir de novo quando eu terminar de compor.",
        "verdict": "rewritten",
        "rationale": "Convite afetuoso de Claire em 2 linhas límpidas."
    },
    {
        "id": 4689,
        "curated_ptbr": "Mana Claire...",
        "verdict": "rewritten",
        "rationale": "Tratamento carinhoso canônico 'Mana Claire...' (クレアお姉ちゃん) consagrado na relação entre as duas desde a infância."
    },
    {
        "id": 4690,
        "curated_ptbr": "Aurica! Você está bem?!\nJá está se sentindo melhor?",
        "verdict": "rewritten",
        "rationale": "Acolhida maternal e aliviada de Claire ao ver a irmãzinha recuperada da febre."
    },
    {
        "id": 4691,
        "curated_ptbr": "Sim. O Lyner fez um Mergulho e me curou por completo...",
        "verdict": "rewritten",
        "rationale": "Uso canônico do termo 'Mergulho' (ダイブ) e gratidão sincera de Aurica."
    },
    {
        "id": 4692,
        "curated_ptbr": "E tem mais: descobri uma coisa\nsimplesmente incrível!",
        "verdict": "rewritten",
        "rationale": "Entusiasmo infantil e radiante de Aurica compartilhando a grande revelação."
    },
    {
        "id": 4693,
        "curated_ptbr": "Eu sou a reencarnação\nda Deusa Tyria!",
        "verdict": "rewritten",
        "rationale": "Termo canônico sagrado 'Deusa Tyria' (ティリア神) com quebra harmônica."
    },
    {
        "id": 4694,
        "curated_ptbr": "Como é que é?!\nÉ sério mesmo?!",
        "verdict": "rewritten",
        "rationale": "Espanto atônito de Claire (ええ!? 本当に?) com expressividade brasileira viva."
    },
    {
        "id": 4695,
        "curated_ptbr": "Sim. Pelo que parece, o Lyner testemunhou isso com os próprios olhos durante o Mergulho.",
        "verdict": "rewritten",
        "rationale": "Confirmação convicta de Aurica respaldada no testemunho de Lyner na Cosmosfera."
    },
    {
        "id": 4696,
        "curated_ptbr": "Não... Não pode ser...\nEu mal consigo acreditar...",
        "verdict": "rewritten",
        "rationale": "Incredulidade profunda de Claire em 2 linhas sem pontuação solta."
    },
    {
        "id": 4697,
        "curated_ptbr": "Ehehe...\nPara falar a verdade, nem eu mesma\nconsigo acreditar direito nisso até agora.",
        "verdict": "rewritten",
        "rationale": "Risinho tímido característico de Aurica (えへへ...) em 3 versos balanceados perfeitamente."
    },
    {
        "id": 4698,
        "curated_ptbr": "E além disso... mana Claire, me perdoa.",
        "verdict": "rewritten",
        "rationale": "Pedido de desculpas humilde e afetuoso com o vocativo 'mana Claire'."
    },
    {
        "id": 4699,
        "curated_ptbr": "Eu vivia me rebaixando com tanto complexo de inferioridade,\ne acho que acabei causando\ntantos incômodos a você...",
        "verdict": "rewritten",
        "rationale": "Tradução precisa de '卑屈になって' (agir com subserviência/complexo de inferioridade), refletindo o trauma psicológico de Aurica."
    },
    {
        "id": 4700,
        "curated_ptbr": "Mas com tudo o que aconteceu desta vez, eu percebi uma coisa.",
        "verdict": "rewritten",
        "rationale": "Transição de maturidade emocional no arco de Aurica."
    },
    {
        "id": 4701,
        "curated_ptbr": "Mesmo que aconteçam tantos problemas e tragédias no mundo,\na vida não é feita só de sofrimento.",
        "verdict": "rewritten",
        "rationale": "Superação do niilismo de Aurica (世の中辛い事ばかりでもない), fluindo com beleza eufônica."
    },
    {
        "id": 4702,
        "curated_ptbr": "Por isso...\nvou encarar a vida de cabeça erguida!\nDecidi viver de forma muito mais positiva daqui em diante.",
        "verdict": "rewritten",
        "rationale": "Resolução de vida luminosa e comovente de Aurica em 3 versos, eliminando pontuações órfãs iniciais."
    },
    {
        "id": 4703,
        "curated_ptbr": "Aurica...",
        "verdict": "approved_as_is",
        "rationale": "Comoção silenciosa e maternal de Claire."
    },
    {
        "id": 4704,
        "curated_ptbr": "Então, daqui para a frente...\nvou dar o meu melhor para ser positiva,\nassim como você sempre foi, mana Claire!",
        "verdict": "rewritten",
        "rationale": "Voto sincero de imitar o exemplo de força de Claire, com quebra tripartite elegante."
    },
    {
        "id": 4705,
        "curated_ptbr": "Com certeza. Estou torcendo com todo o coração por você!",
        "verdict": "rewritten",
        "rationale": "Apoio vibrante e encorajador da irmã de criação (ええ。頑張ってね!)."
    },
    {
        "id": 4706,
        "curated_ptbr": "Este lugar é uma loja de variedades.\nSó que...",
        "verdict": "rewritten",
        "rationale": "Constatação de Lyner preparando a piada recorrente com a dona da loja."
    },
    {
        "id": 4707,
        "curated_ptbr": "Não chame de loja de variedades!\nAqui é uma Fancy Shop!",
        "verdict": "rewritten",
        "rationale": "Uso canônico do termo de cenário 'Fancy Shop' (ファンシーショップ) defendido com indignação cômica pela dona da boutique."
    },
    {
        "id": 4708,
        "curated_ptbr": "Se eu chamar de loja de variedades, ela fica uma fera comigo.",
        "verdict": "rewritten",
        "rationale": "Comentário resignado e bem-humorado de Lyner para Aurica."
    },
    {
        "id": 4709,
        "curated_ptbr": "Nossa, aqui tem tantas coisinhas fofas!\nDá vontade de levar todas para casa.",
        "verdict": "rewritten",
        "rationale": "Fascínio genuíno de Aurica diante dos artigos delicados da Fancy Shop."
    },
    {
        "id": 4710,
        "curated_ptbr": "Pois então convença o rapaz aí do seu lado a comprar um monte de mimos para você na próxima!",
        "verdict": "rewritten",
        "rationale": "Sugestão marota e comercial da lojista incentivando o cavalheirismo de Lyner."
    },
    {
        "id": 4711,
        "curated_ptbr": "Eba...\nAcho que vou pedir mesmo...",
        "verdict": "rewritten",
        "rationale": "Concordância travessa e meiga de Aurica (うん。そうしてもらおうかな...). Entrada da segunda linha limpa sem reticências órfãs."
    },
    {
        "id": 4712,
        "curated_ptbr": "Ei, espera um pouco!",
        "verdict": "rewritten",
        "rationale": "Sobressalto atônito de Lyner vendo o plano tramado contra a sua carteira."
    },
    {
        "id": 4713,
        "curated_ptbr": "Pois bem, como cortesia de cliente fiel, vou dar este mimo especial para vocês!",
        "verdict": "rewritten",
        "rationale": "Generosidade astuta da vendedora fidelizando o casal com um brinde de luxo."
    },
    {
        "id": 4714,
        "curated_ptbr": "Obteve o item [Coração de Dragão]!",
        "verdict": "rewritten",
        "rationale": "Notificação formal com o item canônico 'Coração de Dragão' (ドラゴンハート / Dragon Heart) entre colchetes blindados."
    },
    {
        "id": 4715,
        "curated_ptbr": "Tem certeza de verdade?!\nUma coisa que parece tão cara...",
        "verdict": "rewritten",
        "rationale": "Choque de Lyner ao receber de graça um artefato de tamanho valor."
    },
    {
        "id": 4716,
        "curated_ptbr": "Não tem problema. Afinal de contas, hoje é dia de festival! E sem falar que vocês ainda vão comprar um montão de coisas aqui comigo mais tarde!",
        "verdict": "rewritten",
        "rationale": "Lógica comercial esperta e festiva da comerciante de Platina."
    },
    {
        "id": 4717,
        "curated_ptbr": "Ehehe...",
        "verdict": "rewritten",
        "rationale": "Risinho cúmplice e deleitado de Aurica diante da cena."
    },
    {
        "id": 4718,
        "curated_ptbr": "Tenham piedade da minha carteira...",
        "verdict": "rewritten",
        "rationale": "Lamento derrotado e cômico de Lyner Barsett (勘弁してくれ), fechando o bloco com humor brilhante."
    }
]

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_018.json", "w", encoding="utf-8") as f:
    json.dump(batch5, f, indent=2, ensure_ascii=False)

print(f"Batch 5 saved with {len(batch5)} items.")

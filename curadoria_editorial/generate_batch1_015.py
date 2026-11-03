import json

batch1 = [
    {
        "id": 3751,
        "curated_ptbr": "Ora, boa noite.\nO que vocês procuram por aqui?",
        "verdict": "rewritten",
        "rationale": "Espírito da Flor tem tom acolhedor e gracioso; elimina o coloquialismo moderno 'E aí, tudo bem?' e quebra a linha sem órfãs."
    },
    {
        "id": 3752,
        "curated_ptbr": "Disseram que um grande carregamento de bebida\nfoi importado para cá...",
        "verdict": "rewritten",
        "rationale": "Lyner expressa com naturalidade e tom investigativo, ajustando a quebra de linha após o substantivo composto."
    },
    {
        "id": 3753,
        "curated_ptbr": "Sim, temos de sobra.\nFaço um preço especial: dez mil Leaf a garrafa.",
        "verdict": "rewritten",
        "rationale": "Espírito da Flor em tom mercante e provocador, escrevendo o numeral por extenso para eufonia em diálogo oral."
    },
    {
        "id": 3754,
        "curated_ptbr": "D-Dez mil Leaf?!\nÉ claro que a gente não tem tanto dinheiro!",
        "verdict": "rewritten",
        "rationale": "Misha em choque tsundere genuíno com gagueira inicial expressiva em vez de 'I,いちまん'."
    },
    {
        "id": 3755,
        "curated_ptbr": "É... compreendo.\nEntão que tal um duelo de copos?\nSe ganhar de mim na bebida, dou uma de graça.",
        "verdict": "rewritten",
        "rationale": "Propõe o desafio de bebida com naturalidade e ritmo teatral sem quebras órfãs."
    },
    {
        "id": 3756,
        "curated_ptbr": "Como é que é?! Eu nem tenho idade para beber!",
        "verdict": "rewritten",
        "rationale": "Misha indignada com a proposta absurda de beber saquê, capturando a indignação original de não ter idade/estômago para isso."
    },
    {
        "id": 3757,
        "curated_ptbr": "Não precisa ser você.\nPode ser o rapaz ou a moça ao seu lado,\nou qualquer amigo que quiserem trazer.",
        "verdict": "rewritten",
        "rationale": "Espírito da Flor oferece alternativas aos companheiros com fluidez e prosódia limpa."
    },
    {
        "id": 3758,
        "curated_ptbr": "Eu estou fora. Sou fraca para bebida.\nE você, Lyner?",
        "verdict": "rewritten",
        "rationale": "Personagem feminina da mente de Misha declina educadamente por ter baixa tolerância ao álcool (お酒は弱くて)."
    },
    {
        "id": 3759,
        "curated_ptbr": "E-Eu não bebo um único pingo!",
        "verdict": "rewritten",
        "rationale": "Lyner gagueja envergonhado com o sufixo 'ッス' casual juvenil, enfatizando que não bebe nada."
    },
    {
        "id": 3760,
        "curated_ptbr": "Assim nem temos como começar a disputa.",
        "verdict": "rewritten",
        "rationale": "Misha constata a falta de competidores sem decalque do inglês."
    },
    {
        "id": 3761,
        "curated_ptbr": "A gente não conhece ninguém que seja bom de copo?",
        "verdict": "rewritten",
        "rationale": "Lyner busca uma solução em tom coloquial brasileiro natural ('bom de copo' para 酒に強い)."
    },
    {
        "id": 3762,
        "curated_ptbr": "Bem... até onde eu me lembre,\nnão há ninguém assim...",
        "verdict": "rewritten",
        "rationale": "Resposta hesitante e reflexiva da interlocutora."
    },
    {
        "id": 3763,
        "curated_ptbr": "Hum... Vamos procurar por aí e falar com todo mundo que pareça aguentar o tranco.",
        "verdict": "rewritten",
        "rationale": "Lyner decide investigar de forma proativa (片っ端から探してみよう) sem pontuação órfã inicial."
    },
    {
        "id": 3764,
        "curated_ptbr": "A Hama não parece daquelas que aguentam muita bebida...",
        "verdict": "rewritten",
        "rationale": "Lyner pondera sobre Hama, guardiã da mente de Misha, preservando o nome canônico e ritmo de fala."
    },
    {
        "id": 3765,
        "curated_ptbr": "Para começar, eu nem bebo álcool, seu tonto!",
        "verdict": "rewritten",
        "rationale": "Moradora do Mundo Inferior (Hama) reage irritada à suposição absurda (そもそも飲まないわよ!)."
    },
    {
        "id": 3766,
        "curated_ptbr": "É verdade... Mas que mundo mais esquisito.\nA família da Misha era mesmo assim?",
        "verdict": "rewritten",
        "rationale": "Lyner reflete sobre a estranheza do lar simbólico de Misha na Cosmosfera sem calque."
    },
    {
        "id": 3767,
        "curated_ptbr": "Escuta aqui... você acha mesmo que o pai da Misha era um bêbado de verdade?\nÉ óbvio que se trata de uma substituição simbólica.",
        "verdict": "rewritten",
        "rationale": "Hama esclarece o conceito de '代替' (substituição mental/simbólica na psique) com precisão pedagógica e tom ríspido."
    },
    {
        "id": 3768,
        "curated_ptbr": "Substituição simbólica...?",
        "verdict": "rewritten",
        "rationale": "Eco interrogativo de Lyner correspondendo ao termo estabelecido."
    },
    {
        "id": 3769,
        "curated_ptbr": "É quando a mente troca fatos do passado por metáforas mais fáceis de assimilar.\nAqui ele parece um beberrão, mas na realidade o trauma foi completamente diferente.",
        "verdict": "rewritten",
        "rationale": "Explicação clínica e psicológica de como a psique da Reyvateil reescreve traumas do mundo real em arquétipos na Cosmosfera."
    },
    {
        "id": 3770,
        "curated_ptbr": "Hum... Será que aconteceu alguma coisa\nentre o meu pai e a Misha...?",
        "verdict": "rewritten",
        "rationale": "Lyner liga os pontos sobre o passado encoberto entre seu pai (Leard) e Misha em Platina."
    },
    {
        "id": 3771,
        "curated_ptbr": "Ora, ora... Até que você não é tão tapado...",
        "verdict": "rewritten",
        "rationale": "Hama admite com sarcasmo a dedução precisa de Lyner (意外と鋭いのね)."
    },
    {
        "id": 3772,
        "curated_ptbr": "Então esta é a Cosmosfera da Senhora Shurelia...",
        "verdict": "rewritten",
        "rationale": "Lyner contempla solenemente o vasto espaço da divindade da Torre."
    },
    {
        "id": 3773,
        "curated_ptbr": "É completamente diferente das outras duas.",
        "verdict": "rewritten",
        "rationale": "Constatação natural de Lyner ao comparar com as mentes de Aurica e Misha."
    },
    {
        "id": 3774,
        "curated_ptbr": "Lyner.",
        "verdict": "approved_as_is",
        "rationale": "Vocativo canônico perfeito da sacerdotisa suprema."
    },
    {
        "id": 3775,
        "curated_ptbr": "Então esta é a sua Cosmosfera, Senhora Shurelia.\nÉ um lugar bem desolado... não tem quase nada.",
        "verdict": "rewritten",
        "rationale": "Lyner expressa sua surpresa inocente diante do vazio do Campo Binário mantendo o tratamento respeitoso 'Senhora Shurelia'."
    },
    {
        "id": 3776,
        "curated_ptbr": "Pois é...\nPara dizer a verdade, nem sei se podemos chamar este lugar de Cosmosfera...",
        "verdict": "rewritten",
        "rationale": "Shurelia expressa hesitação modesta sobre a natureza técnica do seu domínio mental."
    },
    {
        "id": 3777,
        "curated_ptbr": "A rigor, a Cosmosfera é o reino onde reside a psique mortal e humana de uma Reyvateil.",
        "verdict": "rewritten",
        "rationale": "Shurelia conceitua '生身の精神' como psique mortal e humana, definindo a biologia das Reyvateils."
    },
    {
        "id": 3778,
        "curated_ptbr": "Contudo, como eu não possuo essa psique humana, este mundo é, em termos estritos, o Campo Binário.",
        "verdict": "rewritten",
        "rationale": "Fixação terminológica de 'Campo Binário' (バイナリ野) e explicação da sua natureza como Origin."
    },
    {
        "id": 3779,
        "curated_ptbr": "O Campo Binário...? Aquele mundo de dados\nonde os vírus costumavam se refugiar?!",
        "verdict": "rewritten",
        "rationale": "Lyner reconhece chocado o ambiente digital dos vírus sem afetações sintáticas."
    },
    {
        "id": 3780,
        "curated_ptbr": "Exatamente.",
        "verdict": "rewritten",
        "rationale": "Confirmação serena e refinada de Shurelia."
    },
    {
        "id": 3781,
        "curated_ptbr": "E como deve saber se viajou pela mente das outras duas, este lugar fica além daquela porta da Torre que existe no íntimo delas.",
        "verdict": "rewritten",
        "rationale": "Shurelia conecta a cosmologia das mentes e a porta dimensional da Torre de forma elegante e precisa."
    },
    {
        "id": 3782,
        "curated_ptbr": "Hã?!\nEra isso que havia do outro lado...?",
        "verdict": "rewritten",
        "rationale": "Reação atônita de Lyner ao desvendar o mistério das portas da Torre na Cosmosfera."
    },
    {
        "id": 3783,
        "curated_ptbr": "Sim. A Cosmosfera e o Campo Binário estão separados por uma linha tênue. Por isso os vírus conseguem mergulhar tão facilmente.",
        "verdict": "rewritten",
        "rationale": "Shurelia elucida o mecanismo de invasão dos vírus com precisão e clareza conceitual."
    },
    {
        "id": 3784,
        "curated_ptbr": "Compreendo...",
        "verdict": "rewritten",
        "rationale": "Lyner assimila a revelação em tom meditativo."
    },
    {
        "id": 3785,
        "curated_ptbr": "Peço desculpas...\nSe ao menos eu tivesse um mundo mais interessante... Ficou decepcionado, não ficou?",
        "verdict": "rewritten",
        "rationale": "Shurelia demonstra sua fragilidade e timidez feminina tocante ao temer ter desapontado Lyner."
    },
    {
        "id": 3786,
        "curated_ptbr": "Ah, não, de jeito nenhum!\nSó de poder contemplar este lugar, já fico muito contente.",
        "verdict": "rewritten",
        "rationale": "Lyner a tranquiliza com calor humano e gentileza sincera."
    },
    {
        "id": 3787,
        "curated_ptbr": "É mesmo...? Fico aliviada...",
        "verdict": "rewritten",
        "rationale": "Shurelia suspira de alívio com meiguice doce."
    },
    {
        "id": 3788,
        "curated_ptbr": "Bem, que tal voltarmos...?",
        "verdict": "rewritten",
        "rationale": "Lyner sugere a saída com delicadeza e respeito."
    },
    {
        "id": 3789,
        "curated_ptbr": "Ah, sim.",
        "verdict": "rewritten",
        "rationale": "Concordância afável de Shurelia."
    },
    {
        "id": 3790,
        "curated_ptbr": "Aqui é o Anteparo A1.\nO responsável pela autenticação deve dar um passo à frente.",
        "verdict": "rewritten",
        "rationale": "Consistência militar absoluta com 'Anteparo A2' de BLK_EVD_014 para A1隔壁 e comando formal do sistema."
    },
    {
        "id": 3791,
        "curated_ptbr": "Autenticação por Espectro FFT: Lyner Barsett. Aguardando instruções.",
        "verdict": "rewritten",
        "rationale": "Consistência canônica do sistema de segurança com 'Espectro FFT'."
    },
    {
        "id": 3792,
        "curated_ptbr": "Abrir o Anteparo A1.",
        "verdict": "rewritten",
        "rationale": "Ordem militar firme e concisa de Lyner."
    },
    {
        "id": 3793,
        "curated_ptbr": "#0Ma paks ga exec guol A1 al noes.",
        "verdict": "rewritten",
        "rationale": "Restauração obrigatória do código sagrado ancestral em Hymmnos que havia sido apagado na tradução preliminar."
    },
    {
        "id": 3794,
        "curated_ptbr": "Código de fônica autenticado.",
        "verdict": "rewritten",
        "rationale": "Notificação técnica concisa de confirmação do código sonoro."
    },
    {
        "id": 3795,
        "curated_ptbr": "Dois segundos para a abertura do anteparo.\nAutorização de passagem concedida.",
        "verdict": "rewritten",
        "rationale": "Anúncio determinístico da comporta de alta segurança."
    },
    {
        "id": 3796,
        "curated_ptbr": "Sejam muito bem-vindos!\nEsta é a loja Guardião da Torre!",
        "verdict": "rewritten",
        "rationale": "Narl atende os clientes com entusiasmo jovial característico e tom hospitaleiro."
    },
    {
        "id": 3797,
        "curated_ptbr": "Então é você a garota que veio da capital?",
        "verdict": "rewritten",
        "rationale": "Jack puxa assunto com seu estilo de veterano galanteador e perspicaz."
    },
    {
        "id": 3798,
        "curated_ptbr": "Uau! Como o senhor ficou sabendo disso?!",
        "verdict": "rewritten",
        "rationale": "Narl reage boquiaberta e inocente à dedução de Jack."
    },
    {
        "id": 3799,
        "curated_ptbr": "Ora, basta bater o olho numa moça bonita para saber tudo sobre ela.\nUma belezinha como você... Qual é o seu nome?",
        "verdict": "rewritten",
        "rationale": "Jack destila seu charme despojado e autoconfiante sem afetações."
    },
    {
        "id": 3800,
        "curated_ptbr": "Ah... Bem, eu me chamo Narl.",
        "verdict": "rewritten",
        "rationale": "Narl se apresenta com timidez lisonjeada, preservando o nome original canônico japonês estabelecido em BLK_EVD_003 (ナール)."
    }
]

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_015.json', 'w', encoding='utf-8') as f:
    json.dump(batch1, f, ensure_ascii=False, indent=2)

print(f"Batch 1 generated with {len(batch1)} dialogues.")

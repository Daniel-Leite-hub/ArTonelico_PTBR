import json

batch3 = [
    {
        "id": 3851,
        "curated_ptbr": "Dá para ver...? Tem uma espécie de tatuagem entre os meus seios...",
        "verdict": "rewritten",
        "rationale": "Misha mostra seu conector com timidez provocativa fofa."
    },
    {
        "id": 3852,
        "curated_ptbr": "O-O quê?! M-Mas... Será que eu posso ficar olhando para aí?!",
        "verdict": "rewritten",
        "rationale": "Lyner fica em pânico virginal ao se deparar com a visão do decote dela."
    },
    {
        "id": 3853,
        "curated_ptbr": "Seu tarado! Eu não estou te mostrando o peito de propósito!\n...Francamente...",
        "verdict": "rewritten",
        "rationale": "Misha se irrita e finge braveza chamando-o de pervertido (もう!スケベ!)."
    },
    {
        "id": 3854,
        "curated_ptbr": "D-Desculpa...",
        "verdict": "rewritten",
        "rationale": "Lyner pede desculpas sem jeito."
    },
    {
        "id": 3855,
        "curated_ptbr": "Vê este desenho no meu colo? Tem um círculo bem no centro, não tem?\nÉ exatamente ali a minha Porta de Instalação.",
        "verdict": "rewritten",
        "rationale": "Misha orienta Lyner para localizar o ponto exato da inserção fônica."
    },
    {
        "id": 3856,
        "curated_ptbr": "A Instalação permite adicionar propriedades especiais à Magia da Canção.",
        "verdict": "rewritten",
        "rationale": "Explicação determinística e elegante do tutorial de sistema."
    },
    {
        "id": 3857,
        "curated_ptbr": "Por exemplo, ao instalar um Cristal Grathnode com o efeito de Veneno em uma magia de dano básico, o feitiço causará dano tóxico aos inimigos.",
        "verdict": "rewritten",
        "rationale": "Exemplo didático do sistema de batalha com redação limpa e culta."
    },
    {
        "id": 3858,
        "curated_ptbr": "Realize a Instalação e teste a nova Magia da Canção em combate.",
        "verdict": "rewritten",
        "rationale": "Instrução objetiva do tutorial para o jogador."
    },
    {
        "id": 3859,
        "curated_ptbr": "Nossa... Foi bem mais intenso do que eu imaginava...\nFiquei exausta.",
        "verdict": "rewritten",
        "rationale": "Misha desabafa sobre o cansaço pós-instalação fônica com respiração pesada."
    },
    {
        "id": 3860,
        "curated_ptbr": "Você está bem?\nNão precisa se forçar além da conta.",
        "verdict": "rewritten",
        "rationale": "Lyner acolhedor e protetor cuidando do bem-estar dela."
    },
    {
        "id": 3861,
        "curated_ptbr": "Não, estou bem. Foi uma escolha minha...\ne se for você quem estiver instalando, eu aguento firme.\nContinuo contando com você daqui para frente.",
        "verdict": "rewritten",
        "rationale": "Misha reafirma sua confiança inabalável em Lyner com doçura e afeto."
    },
    {
        "id": 3862,
        "curated_ptbr": "Agora você pode realizar a Instalação em Misha!",
        "verdict": "rewritten",
        "rationale": "Mensagem oficial de desbloqueio mecânico."
    },
    {
        "id": 3863,
        "curated_ptbr": "O tópico de Instalação foi adicionado ao menu de Ajuda.",
        "verdict": "rewritten",
        "rationale": "Atualização das instruções do sistema."
    },
    {
        "id": 3864,
        "curated_ptbr": "Este tópico de ajuda pode ser consultado a qualquer momento no menu.",
        "verdict": "rewritten",
        "rationale": "Nota explicativa para consulta do menu."
    },
    {
        "id": 3865,
        "curated_ptbr": "A tal academia deve ser por aqui...",
        "verdict": "rewritten",
        "rationale": "Lyner chega ao cenário do crossover de Atelier Marie na Cosmosfera."
    },
    {
        "id": 3866,
        "curated_ptbr": "Ora, vejo um rosto desconhecido por aqui.\nE, a julgar pelas feições, desprovido de qualquer intelecto...",
        "verdict": "rewritten",
        "rationale": "Kreis se apresenta com sua arrogância erudita cômica e petulância clássica."
    },
    {
        "id": 3867,
        "curated_ptbr": "Não se meta onde não foi chamado.\nEu sou o Lyner. E você, quem é?",
        "verdict": "rewritten",
        "rationale": "Lyner rebate a petulância do aluno com firmeza direta."
    },
    {
        "id": 3868,
        "curated_ptbr": "Chamo-me Kreis. Sou o eterno primeiro colocado da Academia.",
        "verdict": "rewritten",
        "rationale": "Kreis proclama seu status acadêmico com orgulho enfatuado (万年主席)."
    },
    {
        "id": 3869,
        "curated_ptbr": "Ao contrário de certa pessoa em uma oficina que ocupa a lanterna perpétua de notas, sou a personificação da excelência acadêmica.",
        "verdict": "rewritten",
        "rationale": "Kreis desdenha de Marie (Aurica) e sua oficina de alquimia."
    },
    {
        "id": 3870,
        "curated_ptbr": "Essa pessoa seria... A Aurica... Digo, a Marie?",
        "verdict": "rewritten",
        "rationale": "Lyner quase se confunde com o papel desempenhado por Aurica na mente dela."
    },
    {
        "id": 3871,
        "curated_ptbr": "O quê?! Por acaso conhece a senhorita Marlone?!",
        "verdict": "rewritten",
        "rationale": "Kreis fica alarmado ao ouvir que o forasteiro conhece o nome formal de Marie (マルローネさん)."
    },
    {
        "id": 3872,
        "curated_ptbr": "Bem, mais ou menos...",
        "verdict": "rewritten",
        "rationale": "Lyner responde de forma evasiva."
    },
    {
        "id": 3873,
        "curated_ptbr": "Que tipo de relacionamento você tem com a senhorita Marlone?!",
        "verdict": "rewritten",
        "rationale": "Kreis exige explicações tomado de ciúme intelectual e romântico."
    },
    {
        "id": 3874,
        "curated_ptbr": "Ela é alguém muito especial para mim...",
        "verdict": "rewritten",
        "rationale": "Lyner confessa seus sentimentos profundos por Aurica/Marie."
    },
    {
        "id": 3875,
        "curated_ptbr": "Inacreditável!!\nN-Não pode ser... Como pode existir um cavalheiro atraído por aquela desastrada, desleixada e eterna reprovada...?!",
        "verdict": "rewritten",
        "rationale": "Kreis entra em choque cômico diante da revelação amorosa (ガサツでズボラで万年落ちこぼれ)."
    },
    {
        "id": 3876,
        "curated_ptbr": "A propósito, essa tal de Marie me pediu para vir buscar uma Língua Insuportável com você...",
        "verdict": "rewritten",
        "rationale": "Consistência terminológica canônica estrita com BLK_EVD_007 para [Língua Insuportável] (憎たらしい舌)."
    },
    {
        "id": 3877,
        "curated_ptbr": "L-Língua Insuportável, ela disse?!\nKyaaa! Como ela ousa repetir essa audácia?!",
        "verdict": "rewritten",
        "rationale": "Kreis se enfurece com a audácia do apelido sarcástico de Marie."
    },
    {
        "id": 3878,
        "curated_ptbr": "Para começo de conversa, já é humilhação bastante ter de ouvir desaforos de um sujeito obtuso como você exigindo a minha língua!",
        "verdict": "rewritten",
        "rationale": "Discurso empolado de Kreis atacando a falta de refinamento de Lyner."
    },
    {
        "id": 3879,
        "curated_ptbr": "E para piorar, insinua intimidades com a senhorita Marlone! Aaaah... Pela honra do aluno mais brilhante da Academia de Alquimia de Salburg...",
        "verdict": "rewritten",
        "rationale": "Menção canônica à Academia de Alquimia de Salburg (ザールブルグ錬金術アカデミー)."
    },
    {
        "id": 3880,
        "curated_ptbr": "Não terei sossego até colocar este indivíduo em seu devido lugar! E que petulância da senhorita Marlone! Onde já se viu me pedir uma Língua Insuportável?!",
        "verdict": "rewritten",
        "rationale": "Kreis discursa sem parar em tom melodramático e histriônico."
    },
    {
        "id": 3881,
        "curated_ptbr": "Se ela queria uma língua insuportável, que arrancasse da própria boca! Ter o descaramento de exigir logo a minha?!",
        "verdict": "rewritten",
        "rationale": "Kreis esbraveja indignado com a ironia do trocadilho da língua afiada."
    },
    {
        "id": 3882,
        "curated_ptbr": "Quanta falta de decoro! Bem, essa insolência é a cara dela, mas isso não diminui a minha indignação! E digo mais!",
        "verdict": "rewritten",
        "rationale": "Kreis perde o fôlego tentando manter a pose de gênio ofendido."
    },
    {
        "id": 3883,
        "curated_ptbr": "N-Não, chega, já chega!\nJá me deu desaforo mais do que suficiente, obrigado...",
        "verdict": "rewritten",
        "rationale": "Lyner interrompe o monólogo interminável dando a quest por encerrada."
    },
    {
        "id": 3884,
        "curated_ptbr": "Pode ser o bastante para você, mas não para mim!",
        "verdict": "rewritten",
        "rationale": "Kreis protesta querendo continuar sua preleção."
    },
    {
        "id": 3885,
        "curated_ptbr": "Mas me diz uma coisa... Você por acaso gosta da Marie?",
        "verdict": "rewritten",
        "rationale": "Lyner faz a pergunta fatal que desmonta toda a farsa de Kreis."
    },
    {
        "id": 3886,
        "curated_ptbr": "O quê?! De onde tirou esse disparate?!\nE-Eu apaixonado pelo maior fiasco e estorvo de toda a história desta instituição?!",
        "verdict": "rewritten",
        "rationale": "Kreis tem um ataque de nervos negando com veemência desesperada."
    },
    {
        "id": 3887,
        "curated_ptbr": "É essa a calúnia que tem coragem de pronunciar?!",
        "verdict": "rewritten",
        "rationale": "Acusação ofendida e histérica de Kreis."
    },
    {
        "id": 3888,
        "curated_ptbr": "T-Tá bom, já entendi, não precisava berrar...",
        "verdict": "rewritten",
        "rationale": "Lyner recua para não ensurdecer com os gritos dele."
    },
    {
        "id": 3889,
        "curated_ptbr": "Que bom que reconheceu o erro.\n...A propósito...",
        "verdict": "rewritten",
        "rationale": "Kreis recupera a pose e muda de assunto para demonstrar sua preocupação real."
    },
    {
        "id": 3890,
        "curated_ptbr": "Como tem passado a senhorita Marlone ultimamente?\nSe ela estiver com dificuldades, diga que procure por este Kreis.",
        "verdict": "rewritten",
        "rationale": "Kreis se trai completamente revelando o quanto se importa com o bem-estar de Marie."
    },
    {
        "id": 3891,
        "curated_ptbr": "Terei o prazer de inculcar nela os fundamentos da alquimia, detalhe por detalhe, desde o princípio.",
        "verdict": "rewritten",
        "rationale": "Kreis oferece sua tutoria pedagógica como desculpa para passar tempo com ela."
    },
    {
        "id": 3892,
        "curated_ptbr": "(Ele é caidinho por ela e não admite...\nMelhor cair fora antes que ele comece a falar de novo.)",
        "verdict": "rewritten",
        "rationale": "Lyner em pensamento sarcástico percebe a paixão evidente de Kreis."
    },
    {
        "id": 3893,
        "curated_ptbr": "Bom, até mais ver.",
        "verdict": "rewritten",
        "rationale": "Despedida rápida e casual de Lyner."
    },
    {
        "id": 3894,
        "curated_ptbr": "E-Ei! Espere!\nAinda tenho um sem-número de coisas para expor...",
        "verdict": "rewritten",
        "rationale": "Kreis tenta em vão reter Lyner para continuar palestrando."
    },
    {
        "id": 3895,
        "curated_ptbr": "Você obteve a [Língua Insuportável]!",
        "verdict": "rewritten",
        "rationale": "Mensagem determinística de recompensa do item com paridade estrita a BLK_EVD_007."
    },
    {
        "id": 3896,
        "curated_ptbr": "Amarelo...\nEntão temos que virar o espelho da placa laranja para cá... Ué?",
        "verdict": "rewritten",
        "rationale": "Lyner raciocina sobre o quebra-cabeça de reflexão de feixes luminosos em Event/309."
    },
    {
        "id": 3897,
        "curated_ptbr": "Mas nesse caso a luz segue direto, então não precisamos do espelho, precisamos?",
        "verdict": "rewritten",
        "rationale": "Aurica observa a física óptica do enigma com delicadeza e lógica."
    },
    {
        "id": 3898,
        "curated_ptbr": "Em situações assim, não há saída:\nprecisamos estilhaçar o espelho com uma bomba de fogo.",
        "verdict": "rewritten",
        "rationale": "Ayatane propõe a solução tática de demolição (火炎弾)."
    },
    {
        "id": 3899,
        "curated_ptbr": "Uma das placas hexagonais despencou.\nIncidentes fora do padrão acontecem de vez em quando.",
        "verdict": "rewritten",
        "rationale": "Ayatane analisa a anomalia estrutural com serenidade matemática (アブノーマルな事)."
    },
    {
        "id": 3900,
        "curated_ptbr": "Não adianta ficar mofando do lado de fora!\nTemos que correr para o porto...",
        "verdict": "rewritten",
        "rationale": "Jack expressa a urgência militar em Event/261."
    }
]

with open(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch3_015.json', 'w', encoding='utf-8') as f:
    json.dump(batch3, f, ensure_ascii=False, indent=2)

print(f"Batch 3 generated with {len(batch3)} dialogues.")

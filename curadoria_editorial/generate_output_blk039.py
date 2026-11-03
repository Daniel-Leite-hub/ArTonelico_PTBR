# -*- coding: utf-8 -*-
import sys
import json
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Load input
input_path = 'Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_039_input.json'
with open(input_path, 'r', encoding='utf-8') as f:
    input_data = json.load(f)

input_map = {d['id']: d for d in input_data['dialogues']}

curated = {}

# Part 1: Event/541.evd (9345 - 9405)
curated[9345] = {
    "pt_curated": "Lorde Flute, seria possível\nme encontrar com a Tastiella?",
    "curation_notes": "Lyner dirigindo-se com deferência respeitosa ao líder Teru, solicitando audiência com Tastiella."
}
curated[9346] = {
    "pt_curated": "Preciso muito falar com ela.",
    "curation_notes": "Expressão de necessidade sincera e urgente de Lyner."
}
curated[9347] = {
    "pt_curated": "Lamento, mas ela não está em condições\nde receber ninguém agora.",
    "curation_notes": "Flute explicando com gravidade a impossibilidade da audiência."
}
curated[9348] = {
    "pt_curated": "Ela esgotou até a última gota de suas forças\npara manter Mir sob controle.",
    "curation_notes": "Flute demonstrando reverência ao sacrifício extenuante de Tastiella para conter Mir."
}
curated[9349] = {
    "pt_curated": "Não se preocupe, Flute, estou bem.\nSe for por pouco tempo, não há problema algum.",
    "curation_notes": "Intervenção serena e afável de Tastiella tranquilizando Flute."
}
curated[9350] = {
    "pt_curated": "...Grande Anciã!",
    "curation_notes": "Flute expressando espanto e reverência pelo título canônico 'Obaba-sama' (Grande Anciã), motivando a réplica seguinte."
}
curated[9351] = {
    "pt_curated": "Já disse para não me chamar de Anciã.",
    "curation_notes": "Repreensão espirituosa e afetuosa de Tastiella recusando o epíteto envelhecido de 'Obaba-sama', corrigindo o erro da NISA."
}
curated[9352] = {
    "pt_curated": "Tastiella!!",
    "curation_notes": "Alívio e surpresa de Shurelia ao rever a amiga de séculos."
}
curated[9353] = {
    "pt_curated": "...Shurelia!?\nHá quanto tempo, minha querida.",
    "curation_notes": "Saudação calorosa e emotiva de Tastiella à Administradora da Torre."
}
curated[9354] = {
    "pt_curated": "Você está bem!?\nSuas forças parecem tão profundamente esgotadas...",
    "curation_notes": "Preocupação empática de Shurelia com o estado debilitado de Tastiella."
}
curated[9355] = {
    "pt_curated": "Estou bem.\nSe for só isso, ainda consigo aguentar.",
    "curation_notes": "Tastiella minimizando o próprio sofrimento para não alarmar Shurelia."
}
curated[9356] = {
    "pt_curated": "Ainda assim, sinto que a idade me alcançou.\nUltimamente, meu poder mágico tem decaído tanto...",
    "curation_notes": "Reflexão melancólica sobre o declínio de suas faculdades mágicas após quatro séculos."
}
curated[9357] = {
    "pt_curated": "É porque você tem se forçado além da conta!\nE tudo por minha culpa...",
    "curation_notes": "Remorso doloroso de Shurelia assumindo a responsabilidade pela sobrecarga de Tastiella."
}
curated[9358] = {
    "pt_curated": "...Nós prometemos não falar sobre isso, não foi?",
    "curation_notes": "Tastiella lembrando o pacto de amizade entre ambas, resgatando '約束' suprimido pela NISA."
}
curated[9359] = {
    "pt_curated": "...",
    "curation_notes": "Silêncio carregado de culpa e emoção contida."
}
curated[9360] = {
    "pt_curated": "E então, Lyner?\nO que gostaria de conversar comigo?",
    "curation_notes": "Transição graciosa de foco para o jovem cavaleiro."
}
curated[9361] = {
    "pt_curated": "Por favor, liberte a Crônica Crescente.",
    "curation_notes": "Pedido direto e solene de Lyner para liberar o repositório da Crônica Crescente."
}
curated[9362] = {
    "pt_curated": "...",
    "curation_notes": "Pausa avaliativa de Tastiella medindo a gravidade do pedido."
}
curated[9363] = {
    "pt_curated": "E depois de abri-la... o que pretende fazer?",
    "curation_notes": "Pergunta investigativa de Tastiella sondando as reais intenções e maturidade de Lyner."
}
curated[9364] = {
    "pt_curated": "Vou derrotar a Mir!",
    "curation_notes": "Declaração impetuosa e decidida de Lyner."
}
curated[9365] = {
    "pt_curated": "...",
    "curation_notes": "Tastiella percebendo a perigosa sede de combate do rapaz."
}
curated[9366] = {
    "pt_curated": "Compreendo.\nNesse caso, venha comigo.",
    "curation_notes": "Tastiella aceitando conduzi-lo ao teste de maturidade."
}
curated[9367] = {
    "pt_curated": "Vou lhe fazer algumas perguntas.",
    "curation_notes": "Tom pedagógico e sereno iniciando o questionamento socrático."
}
curated[9368] = {
    "pt_curated": "Primeira pergunta.\nO quanto você realmente... conhece sobre a Mir?",
    "curation_notes": "Primeira sondagem desestabilizando a visão maniqueísta de Lyner."
}
curated[9369] = {
    "pt_curated": "Hã? Sobre a Mir...?",
    "curation_notes": "Hesitação surpresa de Lyner diante da pergunta inesperada."
}
curated[9370] = {
    "pt_curated": "Que tipo de vida ela levou até os dias de hoje...",
    "curation_notes": "Tastiella evocando a tragédia pessoal e o sofrimento histórico de Mir."
}
curated[9371] = {
    "pt_curated": "Por quais motivos ela ataca\nos seres humanos...",
    "curation_notes": "Questionamento sobre as origens do ódio e da revolta viral de Mir."
}
curated[9372] = {
    "pt_curated": "O que é que Mir verdadeiramente\ndeseja no fundo do coração...",
    "curation_notes": "Sondagem sobre os anseios profundos da alma de Mir."
}
curated[9373] = {
    "pt_curated": "Isso... eu não tenho como saber...",
    "curation_notes": "Admissão involuntária de ignorância por parte de Lyner."
}
curated[9374] = {
    "pt_curated": "...Compreendo.\nEntão, a segunda pergunta.",
    "curation_notes": "Tastiella constatando o despreparo e avançando com serenidade."
}
curated[9375] = {
    "pt_curated": "Por que você luta contra a Mir?\nPor que quer derrotá-la?",
    "curation_notes": "Duplo questionamento desnudando a motivação superficial de combate."
}
curated[9376] = {
    "pt_curated": "Ora, porque este mundo corre perigo!\nQue outro motivo haveria?!",
    "curation_notes": "Resposta inflamada e defensiva de Lyner expressando senso comum impulsivo."
}
curated[9377] = {
    "pt_curated": "E o que você sente pela Mir agora?",
    "curation_notes": "Tastiella sondando a temperatura afetiva real no peito dele."
}
curated[9378] = {
    "pt_curated": "Como assim, o que eu sinto...?",
    "curation_notes": "Desconforto de Lyner ao ser obrigado a olhar para as próprias emoções."
}
curated[9379] = {
    "pt_curated": "Você nutre ódio... e uma profunda hostilidade.",
    "curation_notes": "Diagnóstico certeiro de Tastiella sobre os sentimentos destrutivos de Lyner."
}
curated[9380] = {
    "pt_curated": "E tem como ser diferente?!\nEla brinca com vidas humanas como se não fossem nada...",
    "curation_notes": "Indignação moral legítima, porém desprovida de empatia transcendente."
}
curated[9381] = {
    "pt_curated": "...",
    "curation_notes": "Silêncio solene de quem anteviu o desfecho do teste."
}
curated[9382] = {
    "pt_curated": "Como imaginei...\nNão posso permitir que passe por aqui.",
    "curation_notes": "Veredito negativo pronunciado com firmeza serena."
}
curated[9383] = {
    "pt_curated": "Mas por que não?!",
    "curation_notes": "Protesto inconformado de Lyner."
}
curated[9384] = {
    "pt_curated": "Porque concluí que você... jamais será capaz de salvar este mundo.",
    "curation_notes": "Golpe de realidade de Tastiella apontando a falha de visão."
}
curated[9385] = {
    "pt_curated": "O que você disse...?",
    "curation_notes": "Choque de Lyner ao ser desqualificado como salvador."
}
curated[9386] = {
    "pt_curated": "No seu estado atual, você só está agindo por pressa e desespero cego.\nEsfrie a cabeça.",
    "curation_notes": "Crítica lúcida ao estado mental desordenado ('ヤケクソ') do cavaleiro."
}
curated[9387] = {
    "pt_curated": "...\nO que eu preciso fazer para você me deixar passar?",
    "curation_notes": "Lyner engolindo o orgulho e perguntando pragmaticamente a condição de passagem."
}
curated[9388] = {
    "pt_curated": "Se responder com sabedoria à pergunta\nque vou lhe fazer agora, eu permitirei sua passagem.",
    "curation_notes": "Tastiella estipulando a condição filosófica do desafio."
}
curated[9389] = {
    "pt_curated": "Qual é a razão mais elementar,\ne ao mesmo tempo mais crucial, para que os conflitos surjam?",
    "curation_notes": "O enigma nuclear de Ar tonelico: a raiz de todas as guerras e discórdias entre humanos e Reyvateils."
}
curated[9390] = {
    "pt_curated": "Essa razão...",
    "curation_notes": "Hesitação reflexiva diante da profundidade do mistério."
}
curated[9391] = {
    "pt_curated": "Não precisa se forçar. Essa não é uma resposta que você consiga formular agora.",
    "curation_notes": "Compreensão compassiva de que a resposta só virá pela experiência no mundo."
}
curated[9392] = {
    "pt_curated": "Percorra o mundo afora e encontre essa resposta.",
    "curation_notes": "Instrução que dá início à peregrinação reflexiva de Lyner."
}
curated[9393] = {
    "pt_curated": "Mas... Tastiella!\nNão temos tempo para isso, a sua vida já está...",
    "curation_notes": "Angústia de Shurelia temendo que a amiga faleça antes do retorno de Lyner."
}
curated[9394] = {
    "pt_curated": "Tem razão. É como Shurelia disse. Sendo sincera, meu tempo de vida já não é longo.",
    "curation_notes": "Aceitação serena e estoica de sua finitude biológica."
}
curated[9395] = {
    "pt_curated": "Não foi nesse sentido que eu quis dizer...!",
    "curation_notes": "Desespero carinhoso de Shurelia por ter tocado na iminência da morte da amiga."
}
curated[9396] = {
    "pt_curated": "...Tudo bem, Shurelia.",
    "curation_notes": "Conforto maternal e terno para a Administradora da Torre."
}
curated[9397] = {
    "pt_curated": "Depois de sofrer um golpe tão devastador...\nseria impossível me recuperar por completo.",
    "curation_notes": "Explicação lúcida sobre as sequelas irreversíveis da batalha contra Mir."
}
curated[9398] = {
    "pt_curated": "Mas acredite em mim nisto: não sinto nenhum arrependimento em partir.",
    "curation_notes": "Paz de espírito e plenitude espiritual de quem cumpriu seu dever."
}
curated[9399] = {
    "pt_curated": "Afinal, já vivi por mais de quatrocentos anos.\nJá era hora de desejar um descanso tranquilo.",
    "curation_notes": "Poética constatação de cansaço após quatro séculos de vigília."
}
curated[9400] = {
    "pt_curated": "No entanto, com a Mir nesse estado,\neu jamais poderia me recolher ao sono eterno com tamanha irresponsabilidade.",
    "curation_notes": "Alto senso de dever e amor protetor impedindo seu repouso prematuro."
}
curated[9401] = {
    "pt_curated": "Por isso, Lyner, quero que encontre por si mesmo a resposta para aquela pergunta.",
    "curation_notes": "Transmissão de responsabilidade e confiança no potencial do rapaz."
}
curated[9402] = {
    "pt_curated": "Ao ouvir o que tem a dizer, se eu julgar que você é alguém a quem se pode confiar o futuro deste mundo...",
    "curation_notes": "Condição para a sucessão espiritual e passagem de bastão."
}
curated[9403] = {
    "pt_curated": "Eu libertarei a Mir... e confiarei todo o resto em suas mãos.",
    "curation_notes": "Compromisso sagrado de entrega do destino do mundo a Lyner."
}
curated[9404] = {
    "pt_curated": "...Entendido.\nEu vou encontrar essa resposta e trazer para você.",
    "curation_notes": "Aceitação firme e madura da missão filosófica e existencial."
}
curated[9405] = {
    "pt_curated": "...Muito bem. Obrigada.\nEstou contando com você.",
    "curation_notes": "Bênção serena de encerramento da cena em Pheyna Gate."
}

# Part 2: Event/453.evd (9406 - 9453)
curated[9406] = {
    "pt_curated": "Vila de Karulu... hein.",
    "curation_notes": "Chegada nostálgica de Lyner à Vila de Karulu nas Asas de Hórus."
}
curated[9407] = {
    "pt_curated": "Se bem me lembro, foi aqui que você caiu nas Asas de Hórus pela primeira vez, não foi?",
    "curation_notes": "Misha rememorando a queda canônica do prólogo ('落ちてきた')."
}
curated[9408] = {
    "pt_curated": "O quêêê?! É sério isso?!",
    "curation_notes": "Berro indignado de Jack ao longe discutindo no mercado."
}
curated[9409] = {
    "pt_curated": "Ué!? ...Essa voz é do...!",
    "curation_notes": "Reconhecimento imediato do timbre inconfundível do amigo veterano."
}
curated[9410] = {
    "pt_curated": "Harm!?",
    "curation_notes": "Misha reagindo com surpresa e afeto ao nome do amigo de infância."
}
curated[9411] = {
    "pt_curated": "Jack!!",
    "curation_notes": "Lyner chamando pelo apelido público do aventureiro."
}
curated[9412] = {
    "pt_curated": "Lyner! Misha!\nChegaram na hora certa!",
    "curation_notes": "Alívio exuberante de Jack ao ver os companheiros chegarem."
}
curated[9413] = {
    "pt_curated": "Dá só uma olhada! Esse coroa tá botando defeito\nno tesouro que me custou o maior suor pra descolar!",
    "curation_notes": "Linguagem coloquial e fanfarrona de Jack reclamando do comerciante mesquinho."
}
curated[9414] = {
    "pt_curated": "...Você não muda nunca, Harm...",
    "curation_notes": "Comentário afetuoso e resignado de Misha sobre a imaturidade crônica dele."
}
curated[9415] = {
    "pt_curated": "...Pois é, o mesmo de sempre.",
    "curation_notes": "Lyner sorrindo cúmplice, concordando com a observação."
}
curated[9416] = {
    "pt_curated": "Mas já faz um tempão, hein.\nNunca imaginei te encontrar aqui\nna Vila de Karulu.",
    "curation_notes": "Reencontro amistoso e surpresa por vê-lo em Karulu."
}
curated[9417] = {
    "pt_curated": "Pois é... Fazia tanto tempo que a gente não se via,\ne eu acabo dando esse vexame logo de cara.",
    "curation_notes": "Jack sem jeito ('みっともないところ'), coçando a nuca pelo papelão em público."
}
curated[9418] = {
    "pt_curated": "Francamente...\nO Harm continua agindo feito criança,\nnão importa quanto tempo passe...",
    "curation_notes": "Provocação carinhosa e idioleto maternal da amiga de infância."
}
curated[9419] = {
    "pt_curated": "Já fazia tempo que eu não presenciava o bom e velho 'estilo Jack'.",
    "curation_notes": "Referência humorística a 'ジャック節' (o estilo inconfundível do Jack), resgatado do original."
}
curated[9420] = {
    "pt_curated": "Qual é, não começa...\nDá um tempo, vai...",
    "curation_notes": "Desconforto cômico de Jack resmungando."
}
curated[9421] = {
    "pt_curated": "Mas sério, que bom ver que você tá bem.",
    "curation_notes": "Afeto genuíno e caloroso de Lyner."
}
curated[9422] = {
    "pt_curated": "Digo o mesmo de vocês.",
    "curation_notes": "Reciprocidade seca e leal de veterano."
}
curated[9423] = {
    "pt_curated": "...Lyner. Aquela conversa...",
    "curation_notes": "Misha cutucando discretamente o protagonista para introduzir o assunto sério."
}
curated[9424] = {
    "pt_curated": "Ué? Que conversa é essa?...\nNão me digam que vocês dois...",
    "curation_notes": "Jack insinuando maliciosamente um romance iminente."
}
curated[9425] = {
    "pt_curated": "SC50Claro que não!!1X",
    "curation_notes": "Preservação estrita das tags de controle SC50 e 1X; explosão de indignação tsundere envergonhada."
}
curated[9426] = {
    "pt_curated": "Q-Que susto, caramba!\nPra que gritar do nada...?",
    "curation_notes": "Reação cômica assustada de Jack após o grito estridente."
}
curated[9427] = {
    "pt_curated": "Ninguém aqui vai se casar coisa nenhuma!",
    "curation_notes": "Misha entregando o próprio subtexto e pensamentos secretos ao negar casamento com veemência."
}
curated[9428] = {
    "pt_curated": "Hã?... Ué, eu só achei que vocês tinham descoberto alguma ruína nova...",
    "curation_notes": "Jack genuinamente confuso com a interpretação precipitada dela."
}
curated[9429] = {
    "pt_curated": "...Hã?",
    "curation_notes": "Misha congelando de vergonha ao perceber que falou demais."
}
curated[9430] = {
    "pt_curated": "Misha... Fala sério. Por acaso sua cabeça só vive cheia desse tipo de bobagem?",
    "curation_notes": "Provocação impagável de Jack expondo a obsessão romântica da garota."
}
curated[9431] = {
    "pt_curated": "N-Não tem nada a ver!... Caramba...",
    "curation_notes": "Defesa gaguejada e envergonhada de Misha, bico emburrado."
}
curated[9432] = {
    "pt_curated": "...Então, podemos voltar ao assunto principal?",
    "curation_notes": "Lyner, alheio à tensão romântica, cortando a conversa fiada."
}
curated[9433] = {
    "pt_curated": "Você...\nrealmente não se toca pra essas coisas, né...",
    "curation_notes": "Jack perplexo e desiludido com a insensibilidade romântica de Lyner."
}
curated[9434] = {
    "pt_curated": "Na verdade...\né sobre a Senhora Shurelia.",
    "curation_notes": "Mudança repentina de tom para a solenidade da missão divina."
}
curated[9435] = {
    "pt_curated": "...O que foi que disse?",
    "curation_notes": "Mudança drástica no semblante de Jack; choque inicial."
}
curated[9436] = {
    "pt_curated": "...E por isso, talvez dê para trazê-la de volta à vida.",
    "curation_notes": "Lyner explicando a possibilidade de restauração de Shurelia."
}
curated[9437] = {
    "pt_curated": "Por favor, Jack.\nNão poderia nos ajudar\nna busca pelo «Re-Nation»?",
    "curation_notes": "Pedido de auxílio para rastrear o Cristal Hymmnos «Re-Nation»."
}
curated[9438] = {
    "pt_curated": "...",
    "curation_notes": "Silêncio pesado e sombrio de Jack confrontado com traumas do passado."
}
curated[9439] = {
    "pt_curated": "...Foi mal, mas recuso.",
    "curation_notes": "Recusa taxativa e gélida de Jack."
}
curated[9440] = {
    "pt_curated": "O quê...!? Jack!?\nQual é o problema...?",
    "curation_notes": "Incompreensão dolorosa de Lyner diante da reação inesperada do amigo."
}
curated[9441] = {
    "pt_curated": "Quando o assunto é a Senhora Shurelia...\neu não quero nem mais ouvir falar.",
    "curation_notes": "Revelação da ferida aberta no coração de Jack em relação ao passado com a deusa Teru/Shurelia."
}
curated[9442] = {
    "pt_curated": "Harm! O que deu em você!?",
    "curation_notes": "Aflição de Misha vendo a frieza atípica do irmão de consideração."
}
curated[9443] = {
    "pt_curated": "Foi mal. Até mais...",
    "curation_notes": "Fuga evasiva de Jack virando as costas."
}
curated[9444] = {
    "pt_curated": "Espera aí, Harm!!",
    "curation_notes": "Tentativa desesperada de contê-lo."
}
curated[9445] = {
    "pt_curated": "...Lyner.",
    "curation_notes": "Olhar cabisbaixo e desolado de Misha."
}
curated[9446] = {
    "pt_curated": "...Não tem jeito. O Jack deve ter os motivos dele.",
    "curation_notes": "Maturidade compreensiva de Lyner respeitando a dor alheia."
}
curated[9447] = {
    "pt_curated": "No fim das contas, levamos um fora de todo mundo, né?",
    "curation_notes": "Autoironia leve ('全員フラレちゃった') para aliviar o peso da frustração acumulada."
}
curated[9448] = {
    "pt_curated": "...É.",
    "curation_notes": "Tristeza suave assentindo ao comentário."
}
curated[9449] = {
    "pt_curated": "Ei, não faz essa cara de choro.",
    "curation_notes": "Conforto afetuoso e íntimo de Lyner para a amiga de infância."
}
curated[9450] = {
    "pt_curated": "Se eu tiver você ao meu lado, Misha,\ntenho certeza de que vamos dar um jeito.",
    "curation_notes": "Declaração de confiança inabalável na parceria de ambos."
}
curated[9451] = {
    "pt_curated": "Lyner...",
    "curation_notes": "Comovida com as palavras calorosas do companheiro."
}
curated[9452] = {
    "pt_curated": "Vamos voltar para Platina.\nA gente bola uma nova estratégia por lá.",
    "curation_notes": "Determinação renovada retornando à base na cidade alta."
}
curated[9453] = {
    "pt_curated": "...Tem razão.",
    "curation_notes": "Concordância esperançosa encerrando o evento em Karulu."
}

# Part 3: Event/671.evd (9454 - 9528)
curated[9454] = {
    "pt_curated": "Lyner... Você esculpiu uma ocarina pra mim! Muito obrigada...",
    "curation_notes": "Misha radiante de felicidade ao receber a ocarina esculpida por Lyner."
}
curated[9455] = {
    "pt_curated": "Parabéns, Misha.\nVocê realmente cresceu tanto para chegar até aqui...",
    "curation_notes": "Hama parabenizando Misha com carinho maternal de guardiã mental."
}
curated[9456] = {
    "pt_curated": "Hama... obrigada.\nEu nunca tinha conseguido preencher o vazio que ficou quando você se foi...\ne isso sempre me pesou no coração.",
    "curation_notes": "Confissão de vulnerabilidade de Misha sobre a ferida de infância, resgatando o original suprimido pela NISA."
}
curated[9457] = {
    "pt_curated": "Mas ver o Lyner esculpindo você de novo para mim... me deixa tão feliz.\nAgora, de verdade, já não resta nenhuma mágoa ou inquietação.",
    "curation_notes": "Alívio pleno e encerramento do trauma infantil que bloqueava a psique de Misha."
}
curated[9458] = {
    "pt_curated": "Mesmo depois que a Hama verdadeira quebrou,\neu continuei o tempo todo no seu coração...\ndando umas boas cutucadas nas costas do Lyner!",
    "curation_notes": "Humor afiado e carinhoso de Hama, admitindo que continuou instigando Lyner de dentro da mente dela."
}
curated[9459] = {
    "pt_curated": "É, é, tá bom...",
    "curation_notes": "Lyner aceitando a provocação com humor seco e conformismo cômico."
}
curated[9460] = {
    "pt_curated": "Misha... Mesmo se esta ocarina voltar a quebrar algum dia, jamais se abata.\nEu estarei sempre viva no seu coração.",
    "curation_notes": "Promessa imortal de proteção e presença espiritual da Guardiã da Mente."
}
curated[9461] = {
    "pt_curated": "...Sim.",
    "curation_notes": "Assentimento emocionado de Misha."
}
curated[9462] = {
    "pt_curated": "E se ainda assim bater saudade, mande esse sujeito aqui esculpir outra para você.",
    "curation_notes": "Provocação afetuosa ('この男') delegando a responsabilidade eterna a Lyner."
}
curated[9463] = {
    "pt_curated": "'Esse sujeito'...? Fala sério...",
    "curation_notes": "Reação cômica de Lyner fingindo indignação."
}
curated[9464] = {
    "pt_curated": "Ahaha... Pode deixar, farei isso mesmo!",
    "curation_notes": "Risada cristalina e desanuviada de Misha."
}
curated[9465] = {
    "pt_curated": "Pois bem, já estão prontos?",
    "curation_notes": "Guia da Cosmosfera assumindo a condução cerimonial."
}
curated[9466] = {
    "pt_curated": "Sim...",
    "curation_notes": "Prontidão serena de Misha."
}
curated[9467] = {
    "pt_curated": "Superando inúmeros obstáculos e atravessando sucessivas Mudanças de Paradigma, Misha finalmente alcançou este patamar.",
    "curation_notes": "Reconhecimento solene da jornada psíquica percorrida através dos níveis da Cosmosfera."
}
curated[9468] = {
    "pt_curated": "E atingiu, enfim, as profundezas mais recônditas: o ponto de conexão com a nossa grande Torre, a «Ar tonelico»...",
    "curation_notes": "Revelação da interface fundamental entre a psique da Reyvateil e a Primeira Torre."
}
curated[9469] = {
    "pt_curated": "...Ponto de conexão com a Torre!?",
    "curation_notes": "Espanto de Lyner diante da magnitude do que está presenciando."
}
curated[9470] = {
    "pt_curated": "Exato. Suponho que já saibam que a Cosmosfera de uma Reyvateil está entrelaçada ao Campo Binário da Torre...",
    "curation_notes": "Explicação técnica diegética sobre a arquitetura neural e de fônica da Torre."
}
curated[9471] = {
    "pt_curated": "Mas onde essa união se dá, afinal? Pois bem: ela ocorre justamente neste patamar... no Nível 9.",
    "curation_notes": "Confirmação de que o Nível 9 é a fronteira direta com o Campo Binário, lapidado para eufonia sem eco."
}
curated[9472] = {
    "pt_curated": "Se Misha se conectar diretamente à Torre, poderá obter um poder antes inimaginável.",
    "curation_notes": "Anúncio do salto quântico de potência mágica proporcionado pela união."
}
curated[9473] = {
    "pt_curated": "Um poder que permitirá a Misha intervir diretamente na própria Torre...!",
    "curation_notes": "Definição do poder supremo da Reyvateil Origin."
}
curated[9474] = {
    "pt_curated": "...",
    "curation_notes": "Silêncio atônito de Lyner."
}
curated[9475] = {
    "pt_curated": "...",
    "curation_notes": "Misha compenetrada na gravidade do momento."
}
curated[9476] = {
    "pt_curated": "Muito bem, daremos início à cerimônia.",
    "curation_notes": "Abertura solene do ritual dos votos eternos."
}
curated[9477] = {
    "pt_curated": "...Aham.",
    "curation_notes": "Pigarro cerimonial legítimo, eliminando a rubrica teatral de acordo com o Critério 4."
}
curated[9478] = {
    "pt_curated": "Misha Arsellec Lünn.",
    "curation_notes": "Invocação pelo nome de batismo canônico completo da heroína."
}
curated[9479] = {
    "pt_curated": "Sim.",
    "curation_notes": "Resposta clara e dedicada de Misha."
}
curated[9480] = {
    "pt_curated": "Promete amar por toda a vida aquele que a guiou até aqui, Lyner, tornando-se o esteio do coração dele e incentivando-se mutuamente em perfeito companheirismo?",
    "curation_notes": "Formula dos votos canônicos matrimoniais da Cosmosfera ('一生愛し、その心の支えとしてお互いを切磋琢磨し合う')."
}
curated[9481] = {
    "pt_curated": "...Hã!?",
    "curation_notes": "Reação tímida e sobressaltada diante do teor matrimonial explícito dos votos."
}
curated[9482] = {
    "pt_curated": "...",
    "curation_notes": "Lyner pego de surpresa pelo compromisso sagrado."
}
curated[9483] = {
    "pt_curated": "...Eu juro.",
    "curation_notes": "Entrega definitiva e corajosa de seu amor a Lyner."
}
curated[9484] = {
    "pt_curated": "Lyner Barsett.",
    "curation_notes": "Invocação solene do cavaleiro."
}
curated[9485] = {
    "pt_curated": "Eu também tenho que jurar?!",
    "curation_notes": "Espanto e espontaneidade jovial de Lyner ao ser colocado no altar."
}
curated[9486] = {
    "pt_curated": "Promete ser o apoio emocional eterno de Misha, cuja mente desbravou, dedicando-se por toda a vida a preservar a serenidade desta Cosmosfera?",
    "curation_notes": "Voto do Diver assumindo a guarda perpétua da estabilidade mental da parceira."
}
curated[9487] = {
    "pt_curated": "...S-Sim...",
    "curation_notes": "Consentimento tímido e embaraçado de Lyner, corrigindo a resposta desinteressada inventada pela NISA."
}
curated[9488] = {
    "pt_curated": "...",
    "curation_notes": "Misha contemplando Lyner com infinito carinho."
}
curated[9489] = {
    "pt_curated": "Muito bem. Agora, como prova do pacto,\nconcedam-se o abraço sagrado dos votos.",
    "curation_notes": "Instrução cerimonial exigindo o selo corporal do juramento ('誓いの抱擁')."
}
curated[9490] = {
    "pt_curated": "O quê!?... O que um abraço tem a ver com isso?!",
    "curation_notes": "Desconcerto pueril de Lyner diante da exigência do abraço íntimo."
}
curated[9491] = {
    "pt_curated": "Mas é claro que tem! Tem tudo a ver!",
    "curation_notes": "Entusiasmo enfático do Guia comprovando a necessidade do gesto afetivo."
}
curated[9492] = {
    "pt_curated": "A Cosmosfera é uma estrutura frágil. E após ser desbravada a tal profundidade, qualquer abalo deixará feridas ainda mais fundas na alma dela.",
    "curation_notes": "Fundamento psicológico e diegético sobre a extrema sensibilidade da mente da Reyvateil."
}
curated[9493] = {
    "pt_curated": "Por este motivo, o laço com aquele que desbravou seu mundo interior deve ser eterno.",
    "curation_notes": "A necessidade de segurança emocional perpétua entre Diver e parceira."
}
curated[9494] = {
    "pt_curated": "Você por ela, e ela por você...\nUm vínculo onde ambos se apoiam, servem de refúgio perpétuo e reconhecem o valor um do outro...",
    "curation_notes": "Poética definição do amor mútuo e reciprocidade espiritual."
}
curated[9495] = {
    "pt_curated": "Afinal, é apenas nisso que reside o verdadeiro laço...",
    "curation_notes": "Conclusão sublime da doutrina da Cosmosfera."
}
curated[9496] = {
    "pt_curated": "...Lyner...",
    "curation_notes": "Sussurro tímido e apaixonado de Misha."
}
curated[9497] = {
    "pt_curated": "S-Sim...",
    "curation_notes": "Lyner acolhendo-a com ternura desajeitada, mas protetora."
}
curated[9498] = {
    "pt_curated": "...Parece... que até agora a ficha não caiu...\nEu revelei tudo, absolutamente tudo de mim para você...",
    "curation_notes": "Vulnerabilidade absoluta de Misha aconchegada no abraço dele."
}
curated[9499] = {
    "pt_curated": "É mesmo...?",
    "curation_notes": "Lyner absorvendo com serenidade o peso sagrado da confissão."
}
curated[9500] = {
    "pt_curated": "Afinal, este é o ponto mais profundo do meu mundo interior. Se você está aqui comigo... significa que já conhece tudo o que sou.",
    "curation_notes": "A comunhão total de almas que o Nível 9 representa."
}
curated[9501] = {
    "pt_curated": "...É... parando para pensar, é verdade...",
    "curation_notes": "Compreensão humilde e reverente de Lyner."
}
curated[9502] = {
    "pt_curated": "Sabe, Lyner...\nEu queria ficar assim para sempre...",
    "curation_notes": "Desejo puro de eternizar o aconchego do abraço."
}
curated[9503] = {
    "pt_curated": "Estar em seus braços me traz tanta paz...\nVocê me envolve com ternura como um berço,\nme protegendo de qualquer perigo...",
    "curation_notes": "Metáfora poética do berço ('揺りかご') simbolizando abrigo e redenção após anos de solidão no Rinkernator."
}
curated[9504] = {
    "pt_curated": "Daqui em diante... para sempre juntos...",
    "curation_notes": "O leitmotiv sagrado de amor eterno compartilhado entre eles."
}
curated[9505] = {
    "pt_curated": "Pois bem. Agora que a cerimônia dos votos se concluiu, vamos receber o poder propriamente dito.",
    "curation_notes": "Guia interrompendo com delicadeza o momento para avançar à sintonização final."
}
curated[9506] = {
    "pt_curated": "Ué? O poder não vinha com a cerimônia?",
    "curation_notes": "Espanto cândido de Lyner."
}
curated[9507] = {
    "pt_curated": "Mas é evidente!\nComo pretendia obter o poder sem antes tocar a Torre?\nVamos, venham comigo.",
    "curation_notes": "Explicação prática com bom humor cerimonial."
}
curated[9508] = {
    "pt_curated": "Chegamos ao destino.",
    "curation_notes": "Chegada ao portal de comunhão da Torre."
}
curated[9509] = {
    "pt_curated": "Este lugar... por acaso não é...",
    "curation_notes": "Pressentimento de Lyner diante da arquitetura transcendental."
}
curated[9510] = {
    "pt_curated": "Exato. Este pilar é o «cordão umbilical» que une a Torre Ar tonelico às Reyvateils. Basta dar um único passo além para adentrar o Campo Binário.",
    "curation_notes": "Definição técnica visceral de 'へその緒' (cordão umbilical) que ancora as Reyvateils à Primeira Torre."
}
curated[9511] = {
    "pt_curated": "É-É mesmo...!?\nMas esta torre sempre esteve erguida aqui\ndesde os níveis anteriores...",
    "curation_notes": "Dúvida legítima de Lyner observando a presença constante da torre na paisagem mental."
}
curated[9512] = {
    "pt_curated": "De fato, ela era visível. Mesmo em níveis mais baixos podia ser avistada, mas interferir nela era impossível.",
    "curation_notes": "Esclarecimento sobre a inacessibilidade prévia da interface."
}
curated[9513] = {
    "pt_curated": "Era uma presença tão próxima e ao mesmo tempo tão distante.\nContudo... agora tudo mudou!",
    "curation_notes": "Paradoxo poético ('近くて遠い') quebrado pelo avanço dos laços espirituais."
}
curated[9514] = {
    "pt_curated": "Basta que Misha toque neste pilar para despertar um poder antes inimaginável.",
    "curation_notes": "Ação física necessária para o despertar cósmico."
}
curated[9515] = {
    "pt_curated": "O poder de intervir diretamente na própria Torre...!",
    "curation_notes": "A revelação do acesso de baixo nível / privilégio de Origem."
}
curated[9516] = {
    "pt_curated": "...Intervir diretamente?",
    "curation_notes": "Misha assimilando a amplitude de sua nova capacidade."
}
curated[9517] = {
    "pt_curated": "Exatamente!\nAté então, Misha apenas recebia forças da Torre para materializar suas próprias magias.",
    "curation_notes": "Contraste entre a recepção passiva e a intervenção ativa."
}
curated[9518] = {
    "pt_curated": "Mas de agora em diante... tecendo seus sentimentos em canção, ela será capaz até de mobilizar a própria Torre!",
    "curation_notes": "Uso do verbo canônico 'tecer' ('想い紡げば') ligando sentimento e Magia da Canção."
}
curated[9519] = {
    "pt_curated": "...Inacreditável...",
    "curation_notes": "Lyner abalado com a imensidão do que acabou de ouvir, resgatando 'マジか'."
}
curated[9520] = {
    "pt_curated": "Vamos, Misha. Toque na Torre.",
    "curation_notes": "Convite ao toque de comunhão."
}
curated[9521] = {
    "pt_curated": "...Sim.",
    "curation_notes": "Passo firme em direção ao pilar."
}
curated[9522] = {
    "pt_curated": "Lyner... Eu estou conectada à Torre...\nÉ incrível...\nNunca experimentei uma sensação assim em toda a minha vida...",
    "curation_notes": "Êxtase e deslumbramento cósmico ao sintonizar a rede neural da Primeira Torre."
}
curated[9523] = {
    "pt_curated": "Misha... Meus parabéns!",
    "curation_notes": "Comemoração fraterna e amorosa pela conquista épica dela."
}
curated[9524] = {
    "pt_curated": "Lyner... Muito obrigada por ter ficado comigo até o fim deste caminho.",
    "curation_notes": "Gratidão eterna ao seu Diver e parceiro de vida."
}
curated[9525] = {
    "pt_curated": "...Ainda não é o fim.\nNossa verdadeira jornada começa agora, não é?",
    "curation_notes": "Esperança vibrante no futuro conjunto que os aguarda."
}
curated[9526] = {
    "pt_curated": "Sim... é verdade.",
    "curation_notes": "Sorriso compartilhado e alinhamento espiritual."
}
curated[9527] = {
    "pt_curated": "Daqui em diante... para sempre juntos...",
    "curation_notes": "Reafirmação do juramento eterno ('これからも、ずっと一緒'), corrigindo a omissão da NISA."
}
curated[9528] = {
    "pt_curated": "Você teceu a Magia Vermelha [Conexão da Torre]!",
    "curation_notes": "Mensagem de sistema utilizando o verbo canônico 'tecer' ('紡ぎ出した') para a Magia Vermelha obtida no Nível 9."
}

# Validation run
hard_gate_errors = 0
lint_warnings = 0
orphan_errors = 0

for item_id in range(9345, 9529):
    inp = input_map[item_id]
    orig_jp = inp['original_jp']
    orig_en = inp['original_en']
    cur = curated[item_id]
    trad = cur['pt_curated']
    
    # Check for orphan punctuation: line starting with \n followed by punctuation
    # \n followed by . , ; : ? ! -
    for part in trad.split('\n')[1:]:
        if part and part[0] in '.,;:?!':
            print(f"[ORPHAN ERROR] ID {item_id}: line starts with orphan punctuation! '{trad}'")
            orphan_errors += 1
            
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=trad,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {item_id}: {e}")

    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

print(f"\n--- AUDIT SUMMARY ---")
print(f"Total evaluated: {len(curated)}")
print(f"Orphan Punctuation Errors: {orphan_errors}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0 and orphan_errors == 0:
    print("\nPERFECT: All 184 lines passed cleanly with ZERO errors and ZERO warnings!")
    
    # Prepare output dictionary
    output_dialogues = []
    for item_id in range(9345, 9529):
        inp = input_map[item_id]
        cur = curated[item_id]
        output_dialogues.append({
            "id": item_id,
            "pt_curated": cur["pt_curated"],
            "curation_notes": cur["curation_notes"],
            "curated_ptbr": cur["pt_curated"],
            "justificativa": cur["curation_notes"],
            "original_en": inp["original_en"],
            "original_jp": inp["original_jp"]
        })
    
    output_obj = {
        "block_id": "BLK_EVD_039",
        "dialogues": output_dialogues,
        "curated_lines": output_dialogues
    }
    
    output_file = 'Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_039_output.json'
    with open(output_file, 'w', encoding='utf-8') as out_f:
        json.dump(output_obj, out_f, ensure_ascii=False, indent=2)
    print(f"Output successfully written to {output_file}")
else:
    print("Fixes required before writing output.")
    sys.exit(1)

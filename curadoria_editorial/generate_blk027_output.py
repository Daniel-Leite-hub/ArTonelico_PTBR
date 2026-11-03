# -*- coding: utf-8 -*-
"""Script gerador e validador da curadoria editorial do bloco BLK_EVD_027."""

import json
import sys
from pathlib import Path

# Adiciona o diretório de ferramentas ao sys.path para importar o validador oficial
sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\tools")
from curadoria_validate import validate_batch, validate_line

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_027_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_027_output.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

raw_dialogues = input_data["dialogues"]
assert len(raw_dialogues) == 281, f"Esperado 281 falas, obtido {len(raw_dialogues)}"

curations = {
    # =========================================================================
    # EVENT: Event/136.evd (IDs 6781 - 6811) [31 falas] - Saída das ruínas perigosas
    # =========================================================================
    6781: (
        "Uff... De alguma forma,\nconseguimos sair vivos de lá.",
        "rewritten",
        "Radolf aliviado após escapar por um triz dos perigos da ruína."
    ),
    6782: (
        "Tenho que admitir, dessa vez foi\nadrenalina até demais da conta.",
        "rewritten",
        "Tom irônico e despojado de Krusche sobre o perigo excessivo da expedição."
    ),
    6783: (
        "Não dá mais para ficar nestas ruínas.\nEstá perigoso demais para continuar explorando.",
        "rewritten",
        "Avaliação tática austera de Radolf sobre a instabilidade do local."
    ),
    6784: (
        "De qualquer forma, cumprimos nosso objetivo sãos e salvos.\nVamos voltar para Nemo.",
        "rewritten",
        "Conclusão resoluta de Radolf liderando o retorno à base."
    ),
    6785: (
        "Jack...",
        "approved_as_is",
        "Chamado simples e direto de Lyner ao veterano."
    ),
    6786: (
        "Muito obrigado por antes.\nVocê salvou a minha pele de verdade.",
        "rewritten",
        "Gratidão franca e calorosa de Lyner a Jack pelo socorro providencial."
    ),
    6787: (
        "...Deixa disso, garoto. Não foi nada.",
        "rewritten",
        "Jack desconversa com sua fala mansa e despojada de veterano."
    ),
    6788: (
        "Mais importante... se já achou o cristal,\nquer dizer que finalmente vai subir de volta, não é?",
        "rewritten",
        "Jack indagando sobre os próximos passos de Lyner rumo ao Mundo Superior."
    ),
    6789: (
        "Sim... Preciso voltar o quanto antes...\nEnquanto estou aqui parado, Platina pode...",
        "rewritten",
        "Angústia e urgência patriótica de Lyner pelo destino de sua terra natal."
    ),
    6790: (
        "E aí, encontrou algum meio viável de subir?",
        "rewritten",
        "Pragmatismo de Jack questionando a logística da travessia."
    ),
    6791: (
        "Nada ainda... Pedi para a Krusche examinar\na minha aeronave, mas ela disse que não tem conserto.",
        "rewritten",
        "Frustração de Lyner ao constatar a perda irreparável de sua aeronave."
    ),
    6792: (
        "Compreendo...",
        "rewritten",
        "Jack absorvendo a gravidade da situação com murmúrio pensativo."
    ),
    6793: (
        "Ei, aquilo que você comentou outro dia,\nsobre escalar a Torre... Será que não dá para tentar?",
        "rewritten",
        "Lyner cogitando a perigosa escalada vertical da Torre."
    ),
    6794: (
        "Ei, então será que não dá para subir até lá\nescalando a Torre a pé?",
        "rewritten",
        "Variante de Lyner insistindo na subida direta pela estrutura."
    ),
    6795: (
        "O... o quê?!\nEscalar... a Torre?!",
        "rewritten",
        "Choque incrédulo de Jack diante da audácia insensata de Lyner."
    ),
    6796: (
        "...É loucura demais, afinal?",
        "rewritten",
        "Lyner hesita e recua um passo diante da reação atônita de Jack."
    ),
    6797: (
        "Não, impossível não é.",
        "rewritten",
        "Jack admite contrariado a viabilidade física da subida."
    ),
    6798: (
        "O quê?! C-cê tá falando sério...?!",
        "rewritten",
        "Reação de sobressalto de Jack à teimosia temerária do jovem cavaleiro."
    ),
    6799: (
        "Como já te avisei antes, no meio do caminho mora a [Tribo Teru],\ne eles caçam qualquer humano que tente subir a Torre...",
        "rewritten",
        "Jack adverte sobre o território hostil dos Teru no meio da estrutura."
    ),
    6800: (
        "Eu sei.",
        "rewritten",
        "Resposta monossilábica e firme de Lyner que não se intimida."
    ),
    6801: (
        "......",
        "approved_as_is",
        "Pausa dramática cênica de Jack encarando a determinação de Lyner."
    ),
    6802: (
        "A Tribo Teru vive no meio da Torre justamente\npara impedir que os humanos alcancem o topo.",
        "rewritten",
        "Explicação da função territorial dos guardiões Teru."
    ),
    6803: (
        "Eles nunca deixariam a gente passar!",
        "rewritten",
        "Ênfase categórica de Jack na impossibilidade diplomática de passagem."
    ),
    6804: (
        "Mas... não temos mais nenhuma outra alternativa.",
        "rewritten",
        "Resignação resoluta de Lyner assumindo o risco mortal."
    ),
    6805: (
        "...Eu não recomendo. É muito mais prudente\npensar em outro caminho.",
        "rewritten",
        "Conselho de cautela experiente do mercenário veterano."
    ),
    6806: (
        "......",
        "approved_as_is",
        "Silêncio reflexivo de Lyner pesando o perigo."
    ),
    6807: (
        "Falando nisso, Lyner.\nNão precisa mais que eu dê uma olhada na sua aeronave?",
        "rewritten",
        "Krusche quebrando o clima tenso com seu pragmatismo de mecânica."
    ),
    6808: (
        "Ah! Puts... tinha me esquecido completamente!",
        "rewritten",
        "Trapalhada jovial de Lyner levando a mão à cabeça por ter esquecido o plano inicial."
    ),
    6809: (
        "Por mim, tanto faz como tanto fez.",
        "rewritten",
        "Desdém cômico característico de Krusche com seu bico indiferente."
    ),
    6810: (
        "Não, não, não! Vamos lá, com certeza!",
        "rewritten",
        "Desespero bem-humorado de Lyner implorando pela vistoria técnica."
    ),
    6811: (
        "A aeronave caiu na [Floresta de Viola].\nDesculpe o incômodo, mas conto com você até lá.",
        "rewritten",
        "Lyner orientando o destino para as coordenadas da queda com tag canônica."
    ),

    # =========================================================================
    # EVENT: Event/467.evd (IDs 6812 - 6814) [3 falas] - Enigma Hymmnos nos arquivos
    # =========================================================================
    6812: (
        "Tem caracteres de Hymmnos grafados aqui.",
        "rewritten",
        "Identificação precisa do alfabeto ancestral, expurgando o decalque 'Hino'."
    ),
    6813: (
        "Pode ser a chave de liberação do baú que estava no arquivo.",
        "rewritten",
        "Dedução perspicaz de Radolf relacionando os caracteres ao cofre."
    ),
    6814: (
        "Certo, vamos voltar ao arquivo!",
        "rewritten",
        "Lyner animado com a descoberta propondo retornar para abrir o cofre."
    ),

    # =========================================================================
    # EVENT: Event/46.evd (IDs 6815 - 6821) [7 falas] - Passeio no parque de Nemo
    # =========================================================================
    6815: (
        "Bela vista, não é?\nEste é o maior parque de Nemo.",
        "rewritten",
        "Jack apresentando a grandiosidade arborizada do parque metropolitano."
    ),
    6816: (
        "Dizem por aí que o desenvolvimento deste mundo\nse deve inteiramente ao Grathmeld...",
        "rewritten",
        "Lore alquímica de Sol Ciel narrada no tom descompromissado de Jack."
    ),
    6817: (
        "E contam que colocaram aqui, como monumento comemorativo,\na [Pedra da Canção], considerada a própria origem do Grathmeld.",
        "rewritten",
        "Apresentação da Pedra da Canção com terminologia canônica."
    ),
    6818: (
        "Bom, eu mesmo não entendo quase nada disso.",
        "rewritten",
        "Cinismo prático de Jack admitindo sua ignorância acadêmica."
    ),
    6819: (
        "Mas veja bem!\nNada disso tem a menor importância!",
        "rewritten",
        "Transição teatral de Jack mudando o foco para o que realmente lhe interessa."
    ),
    6820: (
        "O que realmente importa é que este parque é\no lugar perfeito para marcar um encontro com uma garota!",
        "rewritten",
        "Espirituosidade maliciosa de Jack recomendando o parque como recanto de namoro."
    ),
    6821: (
        "Você também vai bater ponto aqui direto num futuro próximo,\nescreve o que estou dizendo.",
        "rewritten",
        "Jack provocando Lyner sobre seus futuros passeios românticos com as Reyvateils."
    ),

    # =========================================================================
    # EVENT: Event/182.evd (IDs 6822 - 6839) [18 falas] - Comporta A7 e Batalha em Platina
    # =========================================================================
    6822: (
        "Aqui é a Comporta A7.\nO operador de autenticação deve dar um passo à frente.",
        "rewritten",
        "Mensagem automatizada e impessoal do terminal de segurança da Torre."
    ),
    6823: (
        "Autenticação por Espectro FFT concluída.\nLyner Barsett. Favor emitir comando.",
        "rewritten",
        "Reconhecimento fônico biométrico ancestral da Torre."
    ),
    6824: (
        "Liberar Comporta A7.",
        "rewritten",
        "Ordem militar direta e concisa de Lyner."
    ),
    6825: (
        "#0Ma paks ga exec guol A7 al noes.",
        "approved_as_is",
        "Preservação estrita e inviolável do código de comando ancestral em língua Hymmnos."
    ),
    6826: (
        "Código autenticado.",
        "rewritten",
        "Confirmação sintética do sistema operacional da Torre."
    ),
    6827: (
        "Abertura da comporta em 2 segundos.\nStatus: permissão de passagem concedida.",
        "rewritten",
        "Contagem regressiva técnica com precisão militar."
    ),
    6828: (
        "Senhora Shurelia... Ayatane...\nJá estou a caminho!",
        "rewritten",
        "Tratamento respeitoso canônico ('Senhora Shurelia') e lealdade aos companheiros em apuros."
    ),
    6829: (
        "Uaaagh!!",
        "rewritten",
        "Sobressalto e impacto ao ser emboscado por guardiões corrompidos."
    ),
    6830: (
        "Senhora Shurelia!\nAyatane!",
        "rewritten",
        "Clamor aflito de Lyner procurando pelos protetores de Platina."
    ),
    6831: (
        "!!\nGuardiões sob lavagem cerebral?!",
        "rewritten",
        "Reconhecimento instantâneo da corrupção dos soldados aliados pelo vírus."
    ),
    6832: (
        "Cavaleiro Lyner!\nVocê conseguiu voltar?!",
        "rewritten",
        "Tratamento honroso de 'Lyner-dono' por companheiro de armas em meio ao caos."
    ),
    6833: (
        "Sim, agorinha mesmo!\nOnde está a Senhora Shurelia?!",
        "rewritten",
        "Lyner focado na integridade da administradora sagrada da Torre."
    ),
    6834: (
        "Ela está combatendo os vírus\nno [Altar dos Apóstolos]!",
        "rewritten",
        "Localização do confronto crucial com preservação da tag do santuário."
    ),
    6835: (
        "Então temos que liquidar esses caras primeiro!",
        "rewritten",
        "Determinação aguerrida de Lyner desembainhando a lâmina."
    ),
    6836: (
        "Vocês estão lutando sem parar há horas, não é?\nPodem recuar e descansar!",
        "rewritten",
        "Cavalheirismo e compaixão protetora de Lyner para com os guardas exaustos."
    ),
    6837: (
        "Perdão! Ficamos te devendo essa!",
        "rewritten",
        "Agradecimento visceral e aliviado do soldado ferido."
    ),
    6838: (
        "Saiam do caminho!\nPara trás!",
        "rewritten",
        "Grito de comando firme de Lyner partindo para o combate (revertendo o erro de tradução do EN)."
    ),
    6839: (
        "Certo! Vamos avançar!",
        "rewritten",
        "Ímpeto ofensivo de investida corrigindo o erro da localização inglesa ('get outta here')."
    ),

    # =========================================================================
    # EVENT: Event/269.evd (ID 6840) [1 fala] - Entrada do Laboratório
    # =========================================================================
    6840: (
        "Não é hora de ficar zanzando lá fora.\nVamos depressa até a porta do laboratório!",
        "rewritten",
        "Lyner mantendo o foco na urgência da missão de infiltração."
    ),

    # =========================================================================
    # EVENT: Event/535.evd (IDs 6841 - 6845) [5 falas] - Pista da Garra do Falcão
    # =========================================================================
    6841: (
        "Vou tentar me informar por aqui por desencargo de consciência...\nEsperem um instante.",
        "rewritten",
        "Postura metódica do bispo investigando rumores locais."
    ),
    6842: (
        "Sem chance, ninguém sabe de nada...",
        "rewritten",
        "Radolf retornando frustrado da sondagem com moradores."
    ),
    6843: (
        "Mas enquanto estava na igreja, me lembrei de algo...\nQue tal tentarmos o [Templo de Elemia], na [Garra do Falcão]?",
        "rewritten",
        "Sugestão perspicaz de Radolf com termos canônicos precisos."
    ),
    6844: (
        "É verdade... Lá também são ruínas antigas,\nentão talvez encontremos alguma pista.",
        "rewritten",
        "Concordância entusiasmada de Lyner com a dedução histórica."
    ),
    6845: (
        "Fechado!\nEntão vamos para lá sem perder tempo.",
        "rewritten",
        "Jack aprovando a rota com agilidade prática de mercenário."
    ),

    # =========================================================================
    # EVENT: Event/537.evd (IDs 6846 - 6850) [5 falas] - Chegada ao Templo de Elemia
    # =========================================================================
    6846: (
        "Este lugar...",
        "approved_as_is",
        "Sussurro etéreo de Shurelia reconhecendo reminiscências do passado."
    ),
    6847: (
        "É o lugar conhecido como o [Templo de Elemia].",
        "rewritten",
        "Lyner apresentando o santuário com respeito solene à administradora."
    ),
    6848: (
        "Entendo... O Templo de Elemia...",
        "rewritten",
        "Eco contemplativo de Shurelia processando as memórias da Primeira Era."
    ),
    6849: (
        "Esta edificação me é familiar.\nTalvez possamos descobrir alguma coisa lá dentro.",
        "rewritten",
        "Serenidade prudente de Shurelia antecipando segredos guardados no templo."
    ),
    6850: (
        "Parece que acertamos na mosca.\nVamos entrar de uma vez.",
        "rewritten",
        "Confiança sóbria de Radolf liderando a incursão ao interior sagrado."
    ),

    # =========================================================================
    # EVENT: Event/220.evd (ID 6851) [1 fala] - Parada em Em Pheyna
    # =========================================================================
    6851: (
        "Ei, ei! Dê uma passada\nem Em Pheyna primeiro, por favor.",
        "rewritten",
        "Reclamação típica de Jack cobrando seu desvio obrigatório para Em Pheyna."
    ),

    # =========================================================================
    # EVENT: Event/612.evd (IDs 6852 - 6856) [5 falas] - Guerra de bolas de neve
    # =========================================================================
    6852: (
        "Lyyyner! Por aqui, vem!",
        "rewritten",
        "Chamado travesso e cantarolado de Misha puxando Lyner para a neve."
    ),
    6853: (
        "U-u-u-ui... Que frio, que frio, que frio...",
        "rewritten",
        "Tremedeira cômica de Lyner batendo os dentes na nevasca."
    ),
    6854: (
        "Puxa, Lyner, você é friorento demais!\nOlha só, vamos fazer guerra de neve! Vai esquentar o corpo rapidinho!",
        "rewritten",
        "Impertinência afetuosa de Misha provocando o amigo de infância."
    ),
    6855: (
        "A-antes disso, as minhas mãos vão congelar!",
        "rewritten",
        "Protesto desesperado e divertido de Lyner contra o plano gelado de Misha."
    ),
    6856: (
        "Aaah... Que sem graça!\nEntão vamos para outro canto!",
        "rewritten",
        "Biquinho manhoso de Misha desistindo e procurando outra distração."
    ),

    # =========================================================================
    # EVENT: Event/346.evd (IDs 6857 - 6880) [24 falas] - Audiência com Tastiella
    # =========================================================================
    6857: (
        "Cardeal Radolf, Aurica, Lyner e Ayatane:\nretornamos de nossa missão.",
        "rewritten",
        "Relatório militar e clerical austero do Cardeal Radolf diante da liderança sagrada."
    ),
    6858: (
        "Oh, então retornaram!\nE quanto ao Cristal Hymmnos...?",
        "rewritten",
        "Expectativa reverente e solene de Tastiella pelo artefato ancestral."
    ),
    6859: (
        "Aurica.",
        "approved_as_is",
        "Radolf dando a deixa para Aurica apresentar o cristal sagrado."
    ),
    6860: (
        "Está aqui...",
        "rewritten",
        "Aurica humilde e tímida entregando a relíquia fônica."
    ),
    6861: (
        "E-este é... sem sombra de dúvida,\no autêntico Cristal Hymmnos [Linker]...",
        "rewritten",
        "Comoção extasiada de Tastiella contemplando a pureza sonora do Cristal Linker."
    ),
    6862: (
        "Benditos sejais...\nFizestes uma proeza monumental ao encontrá-lo!",
        "rewritten",
        "Gratidão sublime e louvor pastoral aos cavaleiros."
    ),
    6863: (
        "Donzela Sagrada Aurica, e vós, distintos cavaleiros.\nVossa conquista é de uma grandeza sem igual!",
        "rewritten",
        "Consagração solene do mérito sagrado do grupo."
    ),
    6864: (
        "Muito obrigada!",
        "rewritten",
        "Correção de gênero (obrigada) e reverência graciosa de Aurica."
    ),
    6865: (
        "O momento enfim se cumpriu em plenitude.\nChegou a hora de partirmos rumo à Terra Santa.",
        "rewritten",
        "Proclamação profética e litúrgica de Tastiella."
    ),
    6866: (
        "Aurica, minha filha. Dirija-se aos aposentos interiores\ne inicie os preparativos para a jornada à Terra Santa.",
        "rewritten",
        "Tom maternal e cerimonioso orientando o recolhimento ritual da Donzela."
    ),
    6867: (
        "Sim, senhora.",
        "rewritten",
        "Submissão respeitosa e serena de Aurica à guardiã do templo."
    ),
    6868: (
        "Nobre Lyner,\ne vós, distintos cavaleiros...",
        "rewritten",
        "Vocativo formal e cerimonioso reverenciando a ordem dos cavaleiros."
    ),
    6869: (
        "Resta a vós uma última e crucial missão.",
        "rewritten",
        "Enunciado solene anunciando o encargo derradeiro."
    ),
    6870: (
        "Trata-se de encontrar e resgatar o artefato sagrado\n[Cálice de Eoria], que repousa na [Colina do Canto].",
        "rewritten",
        "Resgate terminológico canônico de [Cálice de Eoria] e [Colina do Canto]."
    ),
    6871: (
        "Este instrumento sagrado é absolutamente indispensável\npara a Cerimônia de Advento das Três Deusas.",
        "rewritten",
        "Justificativa teológica da relíquia para a manifestação divina."
    ),
    6872: (
        "Para cavaleiros que resgataram o lendário cristal,\ntalvez soe como uma incumbência modesta demais, mas...",
        "rewritten",
        "Elogio sutil e polido à estatura heroica da comitiva."
    ),
    6873: (
        "...Poderia confiar em vossa nobre dedicação?",
        "rewritten",
        "Pedido cerimonioso e confiante da líder espiritual."
    ),
    6874: (
        "Sim!",
        "approved_as_is",
        "Prontidão convicta e espontânea de Lyner."
    ),
    6875: (
        "Será uma honra!",
        "rewritten",
        "Polidez refinada e cortesia cavalheiresca de Ayatane."
    ),
    6876: (
        "...Às vossas ordens.",
        "rewritten",
        "Aceite marcial disciplinado e solene de Radolf."
    ),
    6877: (
        "Lyner...",
        "approved_as_is",
        "Olhar afetuoso e preocupado de Aurica antes da separação."
    ),
    6878: (
        "Você tem seus preparativos, Aurica.\nVoltaremos num piscar de olhos, espere por mim.",
        "rewritten",
        "Promessa carinhosa e reconfortante de Lyner à sua donzela."
    ),
    6879: (
        "...Sim.\nBoa sorte na jornada.",
        "rewritten",
        "Despedida dócil e cheia de fé de Aurica."
    ),
    6880: (
        "Aurica deixou o grupo temporariamente.",
        "rewritten",
        "Notificação de sistema do jogo lapidada e clara."
    ),

    # =========================================================================
    # EVENT: Event/625.evd (IDs 6881 - 6893) [13 falas] - Competição de bebida na Cosmosfera
    # =========================================================================
    6881: (
        "Pois bem, preciso achar alguém bom de copo\npara derrotar a Misha do Cais numa disputa de bebida...",
        "rewritten",
        "Lyner maquinando a estratégia para o desafio etílico da Cosmosfera."
    ),
    6882: (
        "Ora, veja só quem está aí. É você, Lyner.",
        "rewritten",
        "Saudação amigável e descontraída de Radolf surgindo na hora certa."
    ),
    6883: (
        "Radolf! Chegou na hora perfeita.\nPor um acaso você é resistente na bebida?",
        "rewritten",
        "Lyner farejando a oportunidade de recrutar o bispo como campeão de copos."
    ),
    6884: (
        "Bebida? Deixe comigo!\nBebo feito uma sucuri de garganta seca!",
        "rewritten",
        "Vangloria estrondosa e cômica de Radolf adaptando a expressão nipônica de bebedeira 'uwabami'."
    ),
    6885: (
        "(...Que linguajar digno de um cardeal, hein...\nBom, estamos dentro da mente da Misha mesmo...)",
        "rewritten",
        "Comentário mental irônico de Lyner estranhando a conduta mundana da projeção de Radolf."
    ),
    6886: (
        "Então vem comigo, conheço um lugar ali\nonde dá para entornar o caneco à vontade.",
        "rewritten",
        "Lyner guiando o cardeal esfomeado por trago para o ringue."
    ),
    6887: (
        "Ora, seja bem-vindo de volta.\nQuem é o cavalheiro?",
        "rewritten",
        "Recepcionista misteriosa do cais com ar sedutor e elegante."
    ),
    6888: (
        "É o desafiante para a nossa disputa de copos.",
        "rewritten",
        "Apresentação formal de Lyner colocando Radolf na berlinda."
    ),
    6889: (
        "Muito bem, prazer em conhecê-lo.\nNão espere que eu vá pegar leve.",
        "rewritten",
        "Provocação confiante do espírito avisando que não terá piedade."
    ),
    6890: (
        "Digo o mesmo, era tudo o que eu queria!\nQue comece o duelo!",
        "rewritten",
        "Entusiasmo guerreiro de Radolf brindando à contenda alcoólica."
    ),
    6891: (
        "N-não aguento... nem mais... uma gota...",
        "rewritten",
        "Balbucio arrastado de Radolf derrotado pelo pileque monumental."
    ),
    6892: (
        "Ora, ora... Mas que decepção.\nAchei que aguentaria muito mais.",
        "rewritten",
        "Ironia zombeteira do espírito lamentando a fraqueza do desafiante."
    ),
    6893: (
        "Não teve jeito...",
        "rewritten",
        "Suspiro derrotado de Lyner vendo seu campeão estirado no balcão."
    ),

    # =========================================================================
    # EVENT: Event/728.evd (ID 6894) [1 fala] - Gato no aspirador de pó
    # =========================================================================
    6894: (
        "...Tem um gato ali.\nUm gato esquisito... montado no que parece um aspirador de pó.",
        "rewritten",
        "Assombro genuíno e cômico de Lyner com a bizarrice surreal da Cosmosfera."
    ),

    # =========================================================================
    # EVENT: Event/602.evd (IDs 6895 - 6921) [27 falas] - O Cais da mente de Misha
    # =========================================================================
    6895: (
        "Nossa... Um manto branco de neve por todo lado.\nO mundo com certeza parece um pouco mais luminoso...",
        "rewritten",
        "Lyner contemplando o clareamento gradual da mente de Misha."
    ),
    6896: (
        "É a prova de que a Misha está aprendendo\na gostar do próprio mundo, pouco a pouco.",
        "rewritten",
        "Explicação psicológica profunda da moradora sobre a autoaceitação da Reyvateil."
    ),
    6897: (
        "É mesmo...?\nSe é assim, podemos ficar mais tranquilos com ela.",
        "rewritten",
        "Otimismo ingênuo e aliviado de Lyner achando que a crise acabou."
    ),
    6898: (
        "Eu preferiria que você só dissesse isso depois de enxergá-la com seus próprios olhos.\nAs raízes daquela menina vão muito mais fundo do que você imagina.",
        "rewritten",
        "Advertência lúcida da moradora contra o julgamento superficial do trauma de Misha."
    ),
    6899: (
        "Veja bem, este mundo está imerso na noite... não, nas trevas.\nContinua em trevas até agora. Já parou para pensar no significado disso?",
        "rewritten",
        "Questionamento desconfortável sobre a escuridão persistente no subconsciente."
    ),
    6900: (
        "A Misha ainda trava uma batalha diária contra amarras e limitações sem fim.\nGostaria que você se esforçasse para compreendê-la.",
        "rewritten",
        "Apelo empático para que Lyner enxergue o fardo que Misha carrega como Cantora das Estrelas."
    ),
    6901: (
        "É... você tem toda razão.",
        "rewritten",
        "Lyner tocado pela reprimenda, assumindo a seriedade do desafio."
    ),
    6902: (
        "Mudando de assunto, surgiu neste mundo\num lugar chamado [Cais].",
        "rewritten",
        "Revelação do novo ponto geográfico desbloqueado na mente."
    ),
    6903: (
        "O Cais é um lugar extremamente precioso para a Misha.\nRecomendo que vá até lá ao menos uma vez.",
        "rewritten",
        "Indicação de rumo emocional essencial para o progresso do mergulho."
    ),
    6904: (
        "Entendi.\nEntão vou dar um pulo lá agora mesmo.",
        "rewritten",
        "Decisão imediata de Lyner em seguir a orientação da moradora."
    ),
    6905: (
        "Aqui é... um lugar tão enigmático.\nNunca vi uma paisagem como essa. Lembra um aeroporto, mas não parece com um...",
        "rewritten",
        "Estranhamento de Lyner diante da arquitetura naval desconhecida para os povos do céu."
    ),
    6906: (
        "Este é o ancoradouro onde atracam embarcações que cruzam a água.",
        "rewritten",
        "Definição arcaica de navios marítimos para quem só conhece aeronaves de plasma."
    ),
    6907: (
        "Q-quem é você?!",
        "rewritten",
        "Surpresa de Lyner ao deparar-se com o habitante misterioso do cais."
    ),
    6908: (
        "Eu estou aqui esperando o navio chegar.\nPor mais que eu espere, espere e espere... ele nunca vem.",
        "rewritten",
        "Melancolia poética do arquétipo de Misha fadada à solidão no cais."
    ),
    6909: (
        "Você vai embarcar nele?",
        "rewritten",
        "Pergunta ingênua buscando compreender o anseio da figura."
    ),
    6910: (
        "Sim...\nOu melhor, embarcar... ou talvez voltar para dentro dele...\nDe qualquer modo, preciso dele para retornar à minha terra natal.",
        "rewritten",
        "Confissão enigmática de saudade e pertencimento ancestral."
    ),
    6911: (
        "É mesmo...?",
        "rewritten",
        "Sensibilidade de Lyner respeitando a tristeza da guardiã."
    ),
    6912: (
        "Mas como é entediante...\nFicar aqui todos os dias, só olhando para o nada e esperando.",
        "rewritten",
        "Desabafo solitário sobre o vazio dos dias imóveis."
    ),
    6913: (
        "Já faz muito tempo que você está esperando...?",
        "rewritten",
        "Lyner investigando a duração daquele tormento interior."
    ),
    6914: (
        "Vejamos...\nAcho que já faz quase quatro anos.",
        "rewritten",
        "Conexão direta com os quatro anos em que Misha foi confinada em Tenba como Cantora das Estrelas."
    ),
    6915: (
        "Quatro anos?!...\nÉ de perder a noção do tempo...",
        "rewritten",
        "Assombro compassivo de Lyner calculando o peso daquele cativeiro temporal."
    ),
    6916: (
        "Mesmo assim, não posso desistir de esperar pelo navio.\nÉ algo precioso demais para mim...",
        "rewritten",
        "Fidelidade inabalável ao pacto original de infância."
    ),
    6917: (
        "Por que será que existe um cais num lugar como este?",
        "rewritten",
        "Lyner buscando o nexo causal entre a memória física e a metáfora mental."
    ),
    6918: (
        "Isso é algo que você mesmo terá de descobrir.",
        "rewritten",
        "Papel maiêutico dos moradores da Cosmosfera forçando o mergulhador a refletir."
    ),
    6919: (
        "Será que esse navio chega quando?",
        "rewritten",
        "Impaciência juvenil de Lyner querendo resolver o sofrimento alheio."
    ),
    6920: (
        "Quem sabe?\nTalvez dependa apenas de você.",
        "rewritten",
        "O navio é a salvação prometida por Lyner; a chegada depende de suas escolhas."
    ),
    6921: (
        "Droga... De novo essa resposta.",
        "rewritten",
        "Beicinho frustrado de Lyner ouvindo o enigma padrão da mente."
    ),

    # =========================================================================
    # EVENT: Event/813.evd (IDs 6922 - 6926) [5 falas] - Diálogo de recusa com Shurelia
    # =========================================================================
    6922: (
        "Lyner.\nNão encontrará mais nada por aqui, sabia?",
        "rewritten",
        "Shurelia surpresa e carinhosa com a insistência de Lyner em visitá-la sem motivo de serviço."
    ),
    6923: (
        "A-ah... é verdade, né...\nJá imaginei que fosse isso...",
        "rewritten",
        "Lyner sem graça, sem jeito por ter subido até o santuário só para vê-la."
    ),
    6924: (
        "...?",
        "approved_as_is",
        "Ponto de interrogação ingênuo de Shurelia sem entender a timidez dele."
    ),
    6925: (
        "A-ah, não, não é nada!\nPeço desculpas pelo incômodo.",
        "rewritten",
        "Lyner gaguejando e dando meia-volta todo desconcertado."
    ),
    6926: (
        "...Compreendo.",
        "rewritten",
        "Resposta polida e sutilmente intrigada de Shurelia com a atitude do jovem."
    ),

    # =========================================================================
    # EVENT: Event/647.evd (IDs 6927 - 6931) [5 falas] - Krusche procura Misha
    # =========================================================================
    6927: (
        "Lyner!\nEi, você não viu a Misha por aí?",
        "rewritten",
        "Agitação repentina de Krusche procurando desesperada pela parceira."
    ),
    6928: (
        "A Misha?\nEla apostou com você de novo e deu no pé?",
        "rewritten",
        "Lyner achando que se trata de mais uma das habituais apostas fraudulentas de Krusche."
    ),
    6929: (
        "Não é nada disso! Estou falando muito sério!\nSe não acharmos a Misha depressa, este mundo pode acabar colapsando!",
        "rewritten",
        "Pânico genuíno de Krusche alertando sobre o risco iminente de colapso psicológico."
    ),
    6930: (
        "Por favor, Lyner, me ajude a procurá-la!",
        "rewritten",
        "Súplica urgente demandando ação rápida do cavaleiro."
    ),
    6931: (
        "T-tudo bem...",
        "rewritten",
        "Lyner engolindo em seco e aceitando a gravidade do alerta."
    ),

    # =========================================================================
    # EVENT: Event/497.evd (IDs 6932 - 6947) [16 falas] - Regulação ambiental de Platina
    # =========================================================================
    6932: (
        "Desde aquele incidente...\nnão tivemos mais nenhuma anormalidade.",
        "rewritten",
        "Shurelia conferindo a telemetria ambiental com alívio sereno."
    ),
    6933: (
        "Senhorita Aurica, todos vocês foram de grande ajuda durante a tempestade.",
        "rewritten",
        "Agradecimento caloroso e gentil de Shurelia à comitiva."
    ),
    6934: (
        "Imagina! Nós também estávamos com problemas naquela hora...\nFoi graças à Senhora Shurelia que nos salvamos.",
        "rewritten",
        "Humildade graciosa de Aurica retribuindo a gratidão divina."
    ),
    6935: (
        "Aquela tempestade foi assustadora...\nA coisa deve ter ficado realmente feia por aqui, não foi?",
        "rewritten",
        "Curiosidade direta de Lyner sobre a vulnerabilidade física da cúpula de Platina."
    ),
    6936: (
        "Não.\nFoi apenas uma leve oscilação em nosso equilíbrio.",
        "rewritten",
        "Esclarecimento técnico de Shurelia minimizando o drama com frieza científica."
    ),
    6937: (
        "...Nossa... É mesmo?",
        "rewritten",
        "Lyner surpreso com a dimensão colateral de um mero desvio milimétrico."
    ),
    6938: (
        "Sim. Se as funções deste núcleo fossem verdadeiramente comprometidas...\nninguém mais seria capaz de sobreviver neste mundo.",
        "rewritten",
        "Gravidade soturna da revelação ecológica sobre a dependência vital da Torre."
    ),
    6939: (
        "É... é sério mesmo...?!",
        "rewritten",
        "Espanto estupefato de Lyner diante da fragilidade da vida em Sol Ciel."
    ),
    6940: (
        "Esta altitude, originalmente,\nnão comporta a vida humana...",
        "rewritten",
        "Constatação física sobre a estratosfera inóspita de Platina."
    ),
    6941: (
        "Pressão atmosférica, temperatura, precipitação, umidade e radiação...\nTodas as variáveis são neutralizadas e reguladas a partir daqui.",
        "rewritten",
        "Enumeração magistral das funções vitais de suporte de vida da Torre."
    ),
    6942: (
        "Poderíamos dizer que as funções vitais deste planeta\nsão todas simuladas artificialmente neste centro.",
        "rewritten",
        "Síntese de Shurelia resumindo Ar tonelico como o pulmão artificial do planeta."
    ),
    6943: (
        "Nossa... Então este lugar é ainda mais colossal do que eu pensava.",
        "rewritten",
        "Admiração genuína da mecânica genial perante a megaengenharia de Primeira Era."
    ),
    6944: (
        "Quer dizer que a nossa própria existência é preservada por este lugar...",
        "rewritten",
        "Reflexão teológica e existencial de Radolf sobre a providência da Torre."
    ),
    6945: (
        "É uma forma perfeitamente justa de descrever.",
        "rewritten",
        "Concordância afável e graciosa de Shurelia."
    ),
    6946: (
        "Mudando em miúdos, quer dizer que as nossas vidas\nestão todas na palma das mãos desta máquina.",
        "rewritten",
        "O cinismo cortante de Jack desnudando a terrível vulnerabilidade da humanidade."
    ),
    6947: (
        "...Também não deixa... de ser verdade.",
        "rewritten",
        "Shurelia baixando o olhar com melancolia silenciosa, admitindo a terrível responsabilidade que carrega."
    ),

    # =========================================================================
    # EVENT: Event/804.evd (IDs 6948 - 7061) [114 falas] - Simulador Escolar de Shurelia
    # =========================================================================
    6948: (
        "Enfim chegamos ao episódio final.\nGostaria de jogar a continuação da história anterior?",
        "rewritten",
        "Shurelia convidando Lyner com afabilidade e expectativa para a conclusão de sua história interativa."
    ),
    6949: (
        "Muito bem.\nVamos retomar a partida imediatamente.",
        "rewritten",
        "Shurelia iniciando a execução do programa simulado."
    ),
    6950: (
        "Meu nome é Lyner Harasett.",
        "approved_as_is",
        "Apresentação canônica do protagonista do jogo escolar de Shurelia."
    ),
    6951: (
        "Por um capricho do destino, conheci uma garota enigmática chamada Leila Togasaki, e esse encontro virou minha vida de ponta-cabeça.",
        "rewritten",
        "Narrativa literária fluida do romance escolar."
    ),
    6952: (
        "Repelimos os ataques da maligna Facção Mir e minha relação com Leila vai de vento em popa. Desde aquele dia, a monotonia foi banida da minha rotina.",
        "rewritten",
        "Aplicação canônica do termo 'Facção Mir' (ミュール団) e prosa vibrante."
    ),
    6953: (
        "Uma semana se passou desde então...\ne chegava o dia que marcaria um divisor de águas em minha vida...",
        "rewritten",
        "Construção de suspense cênico dramático para o clímax."
    ),
    6954: (
        "......",
        "rewritten",
        "Pontuação completa de reticências no sono profundo."
    ),
    6955: (
        ".........",
        "rewritten",
        "Prolongamento do sono inconsciente."
    ),
    6956: (
        "...Lyner, acorda...",
        "rewritten",
        "Sussurro meigo de Leila chamando pelo namorado na cama."
    ),
    6957: (
        ".........",
        "rewritten",
        "Preguiça matinal persistente."
    ),
    6958: (
        "Lyner, vamos!... Acorda!",
        "rewritten",
        "Chacoalhão amoroso com insistência crescente."
    ),
    6959: (
        "...Hum...?",
        "rewritten",
        "Balbucio sonolento de despertar."
    ),
    6960: (
        "Bom dia. Até que enfim resolveu acordar!\nVocê é um dorminhoco de marca maior, sabia?",
        "rewritten",
        "Provocação carinhosa e doce de Leila no quarto."
    ),
    6961: (
        "...Foi mal... Deixa eu dormir mais cinco minutinhos...",
        "rewritten",
        "Clássico pedido de dengo matinal juvenil."
    ),
    6962: (
        "Nada de dormir!\nA gente vai se atrasar pra aula!",
        "rewritten",
        "Puxão de cobertor enérgico de Leila alertando sobre o relógio."
    ),
    6963: (
        "Hã...? Quê...?",
        "rewritten",
        "Reação aparvalhada de Lyner recobrando a consciência."
    ),
    6964: (
        "Uou! Ferrou!\nJá é essa hora toda?!",
        "rewritten",
        "Pânico hilário ao ver os ponteiros do despertador."
    ),
    6965: (
        "Como é que você consegue repetir esse mesmo drama todo santo dia sem enjoar?",
        "rewritten",
        "Ironia espirituosa de Leila diante do hábito incorrigível de Lyner."
    ),
    6966: (
        "Não é que eu faça de propósito, ué!",
        "rewritten",
        "Defesa indignada e cômica enquanto veste o uniforme às pressas."
    ),
    6967: (
        "Pronto! Finalmente me arrumei!\nBora lá, Leila!",
        "rewritten",
        "Lyner pronto para a corrida até o colégio."
    ),
    6968: (
        "Vamos!",
        "rewritten",
        "Prontidão alegre disparando ao lado dele."
    ),
    6969: (
        "Ufa... Conseguimos chegar no último segundo!\nMas você já me salvou de cair duas vezes no caminho...",
        "rewritten",
        "Respiração ofegante natural sem rubricas proibidas, corrigindo o sentido do salvamento."
    ),
    6970: (
        "Ai, ai... Fala sério...\nEm vez da correria, o que me cansa de verdade\né ter que te agarrar toda vez que você tropeça...",
        "rewritten",
        "Eliminação total das rubricas proibidas (*huff*, *uf*), capturando o cansaço na literatura da fala."
    ),
    6971: (
        "Desculpa...\nMas a sala fica logo ali, força!\nSe a gente chegar atrasado depois de correr tanto...",
        "rewritten",
        "Leila encorajando Lyner no corredor da escola."
    ),
    6972: (
        "Não vai ter adiantado... de na... da... Ué... o que...?",
        "rewritten",
        "Hesitação fônica e desmaio súbito de Leila com perda de sustentação vocal."
    ),
    6973: (
        "Leila...?! Leila!\nEi, aguenta firme! Leila!",
        "rewritten",
        "Desespero de Lyner correndo para ampará-la no chão."
    ),
    6974: (
        "......",
        "rewritten",
        "Inconsciência súbita de Leila."
    ),
    6975: (
        "Leila?!",
        "rewritten",
        "Grito atônito de Misha entrando correndo na enfermaria."
    ),
    6976: (
        "Ouvi dizer que você desmaiou e vim correndo...\nO que aconteceu?!",
        "rewritten",
        "Preocupação aflita de Misha checando o estado de saúde da amiga."
    ),
    6977: (
        "A gente estava quase atrasado e veio correndo.\nAí, assim que pisamos na escola, a Leila...",
        "rewritten",
        "Lyner relatando angustiado a dinâmica do ocorrido."
    ),
    6978: (
        "Entendi...\nSe for só uma tontura passageira ou anemia, menos mal...",
        "rewritten",
        "Ponderação médica atenta de Misha avaliando as possibilidades."
    ),
    6979: (
        "...Isso acontece mesmo?\nAté com um programa...?",
        "rewritten",
        "Suspeita e confusão de Lyner lembrando-se da natureza digital do mundo."
    ),
    6980: (
        "É apenas uma emulação, mas pode acontecer.\nSe for só isso, não há motivo para alarme.",
        "rewritten",
        "Misha explicando o funcionamento das rotinas biossimuladas."
    ),
    6981: (
        "...Ugh... hum...",
        "rewritten",
        "Leila recobrando a consciência lentamente na maca."
    ),
    6982: (
        "Leila?!\nVocê tá bem?! Firmeza aí!",
        "rewritten",
        "Alívio imediato e apoio afetuoso de Lyner."
    ),
    6983: (
        "...Lyner...\nEu... cheguei a desmaiar...?",
        "rewritten",
        "Voz frágil e desorientada de Leila sem lembrar de nada."
    ),
    6984: (
        "Sim, desmaiou.\nComo tá se sentindo? Não tá enjoada nem nada?",
        "rewritten",
        "Cuidado atencioso de Lyner verificando se ela tem náusea ou dores."
    ),
    6985: (
        "...Sim, estou melhor...",
        "rewritten",
        "Resposta reconfortante de Leila tentando acalmá-lo."
    ),
    6986: (
        "Bem, não faça esforço hoje.\nFique deitada descansando um pouco.",
        "rewritten",
        "Conselho protetor de Misha zelando pela recuperação dela."
    ),
    6987: (
        "Tem razão.\nVou descansar um pouco.",
        "rewritten",
        "Leila assentindo obediente."
    ),
    6988: (
        "......",
        "rewritten",
        "Olhar atento e pensativo de Lyner."
    ),
    6989: (
        "Vamos, Lyner, você tem aula agora, não tem?\nNada de usar a visita de desculpa para matar aula, ouviu bem?",
        "rewritten",
        "Misha botando ordem e empurrando Lyner de volta à sala de aula."
    ),
    6990: (
        "Tá, tá bom...\nLeila, eu volto para te ver mais tarde.",
        "rewritten",
        "Despedida dócil de Lyner com promessa de retorno rápido."
    ),
    6991: (
        "...Uhum.",
        "rewritten",
        "Sorriso tímido de Leila concordando."
    ),
    6992: (
        "......",
        "rewritten",
        "Expressão sombria de Misha assim que Leila se acomoda."
    ),
    6993: (
        "O que deu em você?\nPor que essa cara tão séria?",
        "rewritten",
        "Lyner notando a mudança brusca no semblante de Misha."
    ),
    6994: (
        "...Não, não é nada...",
        "rewritten",
        "Esquiva nervosa de Misha escondendo uma terrível suspeita."
    ),
    6995: (
        "...?",
        "rewritten",
        "Lyner intrigado com o segredo."
    ),
    6996: (
        "Preciso averiguar uma coisa.\nJá volto.",
        "rewritten",
        "Misha saindo apressada para consultar os registros do sistema."
    ),
    6997: (
        "Ah, eu vou com...",
        "rewritten",
        "Lyner tentando segui-la por curiosidade."
    ),
    6998: (
        "Você fica aí!\nVá estudar como deve ser!",
        "rewritten",
        "Bronca categórica cortando o avanço dele."
    ),
    6999: (
        "Droga... Fui despachado rapidinho.",
        "rewritten",
        "Resmungo bem-humorado de Lyner coçando a nuca."
    ),
    7000: (
        "Uff...\nFinalmente as aulas acabaram.\nMuito bem, hora de visitar a Leila.",
        "rewritten",
        "Alívio ao bater o sinal e entusiasmo para voltar à enfermaria."
    ),
    7001: (
        "Lyner.",
        "rewritten",
        "Aurica em trajes escolares chamando o colega no corredor."
    ),
    7002: (
        "Aurica. O que houve?",
        "rewritten",
        "Lyner parando para conversar com ela."
    ),
    7003: (
        "Fiquei sabendo que a Leila desmaiou...\nSerá que ela tá bem...?",
        "rewritten",
        "Compaixão genuína e preocupação afetuosa de Aurica."
    ),
    7004: (
        "Você estava preocupada com ela...?",
        "rewritten",
        "Lyner sensibilizado com o carinho da amiga."
    ),
    7005: (
        "Mas é claro que fico!\nSó de ver a sua cara de enterro já dá aflição.",
        "rewritten",
        "Franqueza carinhosa de Aurica alfinetando a feição desolada de Lyner."
    ),
    7006: (
        "...A m-minha cara?!",
        "rewritten",
        "Sobressalto envergonhado de Lyner sem saber que estava tão transparente."
    ),
    7007: (
        "Você passou o dia todo cabisbaixo.\nQuando falavam com você, só respondia coisas sem nexo.\nNão me diga que nem percebeu?",
        "rewritten",
        "Aurica descrevendo a distração angustiada de Lyner durante o dia."
    ),
    7008: (
        "...Nadinha...",
        "rewritten",
        "Confissão constrangida de Lyner baixando a cabeça."
    ),
    7009: (
        "De qualquer forma, estou torcendo para que ela melhore logo.\nManda essa mensagem pra ela, tá?\nAté mais.",
        "rewritten",
        "Desejo sincero de melhoras e despedida carinhosa."
    ),
    7010: (
        "Ué?\nVocê não vai lá visitá-la?",
        "rewritten",
        "Surpresa ingênua de Lyner por ela não entrar com ele."
    ),
    7011: (
        "Olha só...\nAté parece que eu seria sem-noção a esse ponto.\nFique ao lado dela e cuide bem dela, ouviu?",
        "rewritten",
        "Delicadeza de Aurica recusando segurar vela para deixar o casal a sós."
    ),
    7012: (
        "Aurica...\nObrigado por se importar.",
        "rewritten",
        "Agradecimento caloroso e sincero de Lyner pela generosidade da amiga."
    ),
    7013: (
        "Leila!\nVocê já pode ficar sentada assim?\nEstá se sentindo melhor?",
        "rewritten",
        "Cuidado solícito de Lyner ao entrar e vê-la erguida."
    ),
    7014: (
        "Sim, estou bem melhor.\nDesculpa ter te preocupado.",
        "rewritten",
        "Meiguice reconfortante de Leila com sorriso tranquilo."
    ),
    7015: (
        "É mesmo...? Que alívio...\nSe você não melhorasse, eu nem saberia o que fazer...\nFiquei com o coração na mão.",
        "rewritten",
        "Confissão apaixonada de Lyner demonstrando a profundidade do seu afeto."
    ),
    7016: (
        "Huuuum.\nE por isso passou a aula inteira no mundo da lua, né?",
        "rewritten",
        "Provocação doce de Leila pegando-o no pulo."
    ),
    7017: (
        "Ugh!... Não começa...\nEu aqui me descabelando de preocupação e você...",
        "rewritten",
        "Protesto tímido e acanhado de Lyner fingindo estar zangado."
    ),
    7018: (
        "Hahaha! É brincadeira!\nDesculpa de verdade. A matéria da aula que você perdeu,\neu te explico tudinho mais tarde.",
        "rewritten",
        "Risada cristalina e afetuosa sem rubricas, prometendo aulas particulares."
    ),
    7019: (
        "...É, n-não sei se fico feliz\nou chateado com isso...",
        "rewritten",
        "Dilema cômico de Lyner adorando a ideia de estudar juntinho mas temendo as broncas."
    ),
    7020: (
        "Bom, vou descansar mais um pouquinho aqui na enfermaria.",
        "rewritten",
        "Leila ajeitando o travesseiro para repousar mais."
    ),
    7021: (
        "Beleza.\nNada de forçar a barra hoje, tá?",
        "rewritten",
        "Recomendação protetora de namorado zeloso."
    ),
    7022: (
        "Tudo beeem.",
        "rewritten",
        "Resposta manhosa e cantada de Leila."
    ),
    7023: (
        "Uff...\nAinda bem que não era nada sério com a Leila.",
        "rewritten",
        "Suspiro de alívio puro no corredor da escola."
    ),
    7024: (
        "Lyner!",
        "approved_as_is",
        "Misha irrompendo no corredor com pavor na voz."
    ),
    7025: (
        "Misha?... O que foi?\nPor que está tão apavorada?",
        "rewritten",
        "Lyner assustado com a palidez cadavérica de Misha."
    ),
    7026: (
        "É um assunto muito sério...",
        "rewritten",
        "Tensão extrema antecipando uma tragédia iminente."
    ),
    7027: (
        "O-o que foi...?\nPor que essa formalidade toda aqui...?",
        "rewritten",
        "Nervosismo de Lyner sentindo o peso do presságio."
    ),
    7028: (
        "Lyner... me perdoa...\nEu... cometi um erro irreparável...",
        "rewritten",
        "Desespero angustiante de Misha confessando sua falha colossal."
    ),
    7029: (
        "...Diz logo de uma vez!\nEstá me assustando, sabia? ...É sobre a Leila?",
        "rewritten",
        "O coração de Lyner dispara ao ligar os pontos com o desmaio."
    ),
    7030: (
        "...É.",
        "rewritten",
        "Confirmação sombria que sela o pesadelo."
    ),
    7031: (
        "O quê?!",
        "rewritten",
        "Choque brutal exigindo respostas."
    ),
    7032: (
        "......",
        "rewritten",
        "Misha engolindo o pranto antes de contar a verdade."
    ),
    7033: (
        "Por favor, desembucha!",
        "rewritten",
        "Lyner suplicando no limite do desespero."
    ),
    7034: (
        "...Tudo bem...",
        "rewritten",
        "Misha cedendo para relatar os fatos técnicos."
    ),
    7035: (
        "No dia do festival de verão, nós nos infiltramos no esconderijo da Facção Mir.\nE resgatamos a Leila, que estava aprisionada lá...",
        "rewritten",
        "Contextualização da operação de infiltração na Facção Mir."
    ),
    7036: (
        "Sim... E o que tem de errado nisso?",
        "rewritten",
        "Lyner não enxergando erro em terem salvado a garota."
    ),
    7037: (
        "E depois, destruímos o [Depósito de Programas de Vírus],\nque servia como o arsenal de armas deles.",
        "rewritten",
        "Misha detalhando a demolição do storage central dos vírus."
    ),
    7038: (
        "...Sim, destruímos.\nE graças a isso nenhum vírus voltou a aparecer desde então.",
        "rewritten",
        "Lyner relembrando o resultado vitorioso da missão."
    ),
    7039: (
        "......",
        "rewritten",
        "Silêncio esmagador de Misha diante da ironia cruel daquele triunfo."
    ),
    7040: (
        "...E-ei...",
        "rewritten",
        "Voz vacilante de Lyner percebendo o horror por trás daquele silêncio."
    ),
    7041: (
        ".........",
        "rewritten",
        "Pausa dramática cortante."
    ),
    7042: (
        "Não me diga que... aquilo tem alguma relação\ncom o desmaio da Leila hoje...?",
        "rewritten",
        "A verdade aterrorizante começa a se desenhar na mente de Lyner."
    ),
    7043: (
        "Ao que parece, o depósito executava um processo de renovação\numa vez por semana para todos os vírus despachados em campo.",
        "rewritten",
        "Revelação do ciclo de manutenção periódica da matriz viral."
    ),
    7044: (
        "Trata-se de uma reconstrução necessária para manter os vírus materializados neste mundo.\nSe esse ciclo for interrompido... os vírus...",
        "rewritten",
        "A mecânica de persistência quântica do código viral."
    ),
    7045: (
        "E-espera um pouco aí...",
        "rewritten",
        "Lyner tentando frear o raciocínio antes da conclusão letal."
    ),
    7046: (
        "Esgotam suas energias... e desaparecem para sempre...",
        "rewritten",
        "A sentença de morte digital pronunciada com dor profunda."
    ),
    7047: (
        "...Tá brincando, né?!\nAquela engenhoca não foi você mesma quem construiu?!\nComo é que você não sabia de algo tão crucial...?!",
        "rewritten",
        "Revolta desesperada de Lyner voltando-se contra a criadora da máquina."
    ),
    7048: (
        "Não adianta gritar comigo! Nem eu mesma...\nNem eu consigo acreditar que não sabia de uma coisa tão vital até agora!",
        "rewritten",
        "Mágoa e autocrítica dilacerante de Misha em prantos."
    ),
    7049: (
        "Se eu soubesse, jamais teria destruído aquele depósito...\nSe ao menos eu soubesse...",
        "rewritten",
        "Remorso lancinante por ter condenado a própria amiga por acidente."
    ),
    7050: (
        "......",
        "rewritten",
        "Paralisia atônita de Lyner assimilando a tragédia."
    ),
    7051: (
        "Misha... Não tem nenhum jeito de consertar isso?!\nFaz alguma coisa, por favor... igual você sempre faz...",
        "rewritten",
        "Desespero infantil de Lyner implorando pela inteligência genial da companheira."
    ),
    7052: (
        "Me perdoa...\nDesta vez... eu não tenho o menor conhecimento sobre esse processo,\nnão há absolutamente nada que eu possa fazer...",
        "rewritten",
        "Confissão de impotência absoluta que destrói as últimas esperanças."
    ),
    7053: (
        "...Leila!!",
        "approved_as_is",
        "Lyner correndo desesperado de volta à enfermaria."
    ),
    7054: (
        "Ela sumiu!\nSerá que... já foi para casa...?",
        "rewritten",
        "Pânico ao encontrar a maca deserta."
    ),
    7055: (
        "...Ou será que...",
        "rewritten",
        "O pressentimento sinistro cruzando sua mente."
    ),
    7056: (
        ".........",
        "rewritten",
        "O vazio silencioso do quarto da enfermaria."
    ),
    7057: (
        "...Não pode ser...",
        "rewritten",
        "A recusa em aceitar o pior."
    ),
    7058: (
        "A Leila... desaparecendo?\nNão pode ser verdade...",
        "rewritten",
        "A dor do luto antecipado da amada."
    ),
    7059: (
        "A Leila vai desaparecer...\ne justo agora... eu não posso fazer nada por ela...?",
        "rewritten",
        "Sentimento de impotência esmagador do herói impotente."
    ),
    7060: (
        "Absolutamente nada...",
        "rewritten",
        "Queda das cortinas do drama com solidão absoluta."
    ),
    7061: (
        "Compreendo...\nNesse caso, fica para uma próxima oportunidade.",
        "rewritten",
        "Resposta polida e serena de Shurelia caso o jogador recuse iniciar a cena final do simulador."
    )
}

assert len(curations) == 281, f"Curations len = {len(curations)}"

curated_dialogues = []
translations_list = []
lines_rewritten = 0
lines_approved_as_is = 0

for d in raw_dialogues:
    d_id = d["id"]
    assert d_id in curations, f"ID {d_id} ausente em curations!"
    cur_text, verdict, rationale = curations[d_id]
    
    if verdict == "rewritten":
        lines_rewritten += 1
    else:
        lines_approved_as_is += 1

    item = {
        "id": d_id,
        "event_file": d["event_file"],
        "speaker_id": d["speaker_id"],
        "speaker": d["speaker"],
        "original_jp": d["original_jp"],
        "original_en": d["original_en"],
        "current_ptbr": d["current_ptbr"],
        "curated_ptbr": cur_text,
        "text": cur_text,
        "verdict": verdict,
        "rationale": rationale
    }
    curated_dialogues.append(item)
    translations_list.append({"id": d_id, "text": cur_text})

# Teste da Trava Técnica Determinística (Fail-Fast)
mock_batch = {"dialogues": curated_dialogues}
is_valid, errors = validate_batch(mock_batch)
if not is_valid:
    print(f"ERRO DE VALIDAÇÃO TÉCNICA ({len(errors)} falhas detectadas):")
    for d_id, errs in errors.items():
        print(f"  ID {d_id}: {errs}")
    sys.exit(1)
else:
    print("[VALIDAÇÃO OK] Todas as 281 falas passaram com nota 10 nas 7 Travas Técnicas de Integridade Canônica!")

highlights = [
    {
        "id": 6782,
        "speaker": "Krusche / Jack / Lyner",
        "description": "Krusche aliviada com ironia mordaz sobre a expedição perigosa e Jack advertindo severamente Lyner sobre a impossibilidade diplomática de cruzar o território hostil da Tribo Teru na subida vertical da Torre."
    },
    {
        "id": 6825,
        "speaker": "Lyner / Sistema / Guarda",
        "description": "Execução com precisão ritual do comando ancestral em idioma Hymmnos (#0Ma paks ga exec guol A7 al noes.) liberando a Comporta A7 e investida corajosa para combater os guardiões corrompidos no Altar dos Apóstolos."
    },
    {
        "id": 6861,
        "speaker": "Tastiella / Aurica / Radolf / Lyner",
        "description": "Audiência solene na Catedral de Platina onde Tastiella consagra a recuperação do autêntico Cristal Hymmnos Linker e outorga a Lyner e aos cavaleiros a missão sagrada de recuperar o artefato sagrado [Cálice de Eoria] na [Colina do Canto]."
    },
    {
        "id": 6884,
        "speaker": "Radolf / Lyner / Espírito da Flor",
        "description": "Concurso etílico tragicômico na Cosmosfera de Misha onde Radolf promete beber feito uma sucuri de garganta seca e acaba estirado de pileque sob o olhar desapontado da guardiã do cais."
    },
    {
        "id": 6908,
        "speaker": "Espírito da Flor / Moradora / Lyner",
        "description": "Revelação comovente no Cais da mente de Misha onde o Espírito da Flor aguarda há quatro anos o navio ancestral que a levará de volta para casa, espelhando os anos de cativeiro e solidão em Tenba."
    },
    {
        "id": 6941,
        "speaker": "Shurelia / Jack / Krusche / Radolf",
        "description": "Diálogo de revelação cosmológica no núcleo ambiental de Platina onde Shurelia expõe a fragilidade da biosfera artificial e Jack crava com cinismo cirúrgico que a máquina segura a vida de todos na palma de suas mãos."
    },
    {
        "id": 7035,
        "speaker": "Misha / Lyner",
        "description": "Clímax trágico do simulador escolar da Cosmosfera de Shurelia onde Misha revela aterrorizada que ao destruir o depósito de vírus da Facção Mir acabou condenando Leila à extinção iminente por falta do ciclo de renovação."
    }
]

new_terms = {
    "Grail of Eoria": {
        "pt": "Cálice de Eoria",
        "gender": "masculino",
        "number": "singular",
        "category": "Artefato Sagrado / Mitologia de Sol Ciel",
        "note": "エオリアの杯. Instrumento e artefato sagrado ancestral de Eoria repousado na Colina do Canto, imprescindível para a Cerimônia de Advento das Três Deusas."
    },
    "Virus Program Storage": {
        "pt": "Depósito de Programas de Vírus",
        "gender": "masculino",
        "number": "singular",
        "category": "Tecnologia / Simulação da Cosmosfera",
        "note": "ウイルスプログラムストレージ. Repositório central de manutenção e renovação periódica de vírus na simulação da Cosmosfera de Shurelia."
    },
    "Refresh": {
        "pt": "Renovação / processo de renovação",
        "gender": "masculino",
        "number": "singular",
        "category": "Tecnologia / Simulação de Vírus",
        "note": "リフレッシュ. Ciclo semanal executado pelo repositório para reestruturar e manter os vírus materializados no mundo da Cosmosfera."
    }
}

updated_address_matrix = {
    "Radolf": {
        "Lyner": "Camarada de armas respeitado e parceiro em missões confidenciais ('Lyner', 'você'), revelando com bom humor seu lado profano bom de copo durante as peripécias da Cosmosfera."
    },
    "Shurelia": {
        "Lyner": "Guardiã sagrada paciente e compreensiva ('Lyner', 'você'), acolhendo com carinho suas visitas tímidas e compartilhando os fardos existenciais da Torre."
    },
    "Aurica": {
        "Lyner": "Companheirismo amoroso e maduro na escola simulada ('Lyner'), abrindo mão de visitas para deixá-lo cuidar de Leila sem ser inconveniente."
    },
    "Misha": {
        "Lyner": "Amiga inseparável e confidente leal ('Lyner'), dilacerada pela culpa e implorando perdão por seu erro de cálculo na destruição do depósito."
    }
}

scene_handoff = {
    "resumo_dramatico": "A decisão temerária de Lyner de encarar a escalada da Torre cruzando o território hostil da Tribo Teru; a entrada triunfal e o confronto com guardiões corrompidos na Comporta A7 em Platina até o Altar dos Apóstolos com o código ancestral Hymmnos; a consagração na Catedral de Platina onde Tastiella celebra a posse do autêntico Cristal Hymmnos Linker e incumbe a comitiva de recuperar o sagrado [Cálice de Eoria] na [Colina do Canto]; a hilária bebedeira de Radolf derrotado no cais mental de Misha; a tocante metáfora dos quatro anos de espera pelo navio libertador no Cais da Cosmosfera; a revelação cósmica dos sistemas ecológicos da Torre que sustentam a vida humana em Platina; e a catarse trágica no simulador colegial de Shurelia, onde a vitória sobre a Facção Mir condena a doce Leila ao desaparecimento definitivo por falta do ciclo de renovação.",
    "decisoes_terminologicas": {
        "Cálice de Eoria": "[Cálice de Eoria] (エオリアの杯, artefato sagrado indispensável à Cerimônia de Advento)",
        "Colina do Canto": "[Colina do Canto] (謳う丘, santuário ancestral de repouso dos cristais)",
        "Tribo Teru": "[Tribo Teru] (テル族, guardiões do setor intermediário da Torre)",
        "Depósito de Programas de Vírus": "[Depósito de Programas de Vírus] (ウイルスプログラムストレージ, matriz de renovação de vírus)",
        "Facção Mir": "Facção Mir (ミュール団, organização antagônica na Cosmosfera de Shurelia)"
    },
    "alertas_para_proximo_bloco": "Atenção ao resgate e consequências do desaparecimento de Leila na Cosmosfera de Shurelia, à jornada em direção à Colina do Canto para a recuperação do Cálice de Eoria e aos preparativos para a Cerimônia de Advento das Deusas com Aurica."
}

output_data = {
    "block_id": "BLK_EVD_027",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "total_lines": len(curated_dialogues),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "highlights": highlights,
    "new_terms": new_terms,
    "updated_address_matrix": updated_address_matrix,
    "scene_handoff": scene_handoff,
    "dialogues": curated_dialogues,
    "entries": curated_dialogues,
    "translations": translations_list
}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Sucesso absoluto! Gravado {OUTPUT_PATH.name} com {len(curated_dialogues)} falas ({lines_rewritten} reescritas, {lines_approved_as_is} aprovadas).")

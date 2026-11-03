# -*- coding: utf-8 -*-
"""
Script de geração e refinamento editorial do bloco BLK_EVD_024
Ar tonelico: Melody of Elemia (Undub)
"""

import json
from pathlib import Path

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_024_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_024_output.json")

def get_curated_data():
    return {
        # 6105 - 6110 (Event/172.evd)
        6105: {
            "curated_ptbr": "Por aqui não vai para a cidade de Platina.",
            "rationale": "Dêixis espacial (こっち) e constatação de orientação geográfica de Lyner."
        },
        6106: {
            "curated_ptbr": "De qualquer forma, preciso voltar para Platina logo.",
            "rationale": "Urgência dramática (とにかくまずは) e foco na missão prioritária."
        },
        6107: {
            "curated_ptbr": "Enquanto não baixarmos o Purger, não teremos como derrotar os vírus.",
            "rationale": "Termo canônico 'Purger' e precisão condicional contra a ameaça dos vírus."
        },
        6108: {
            "curated_ptbr": "Por enquanto, nossa prioridade é baixar o Purger...",
            "rationale": "Foco mental e urgência estratégica de Lyner."
        },
        6109: {
            "curated_ptbr": "Primeiro preciso avisar meu pai de que conseguimos baixá-lo...",
            "rationale": "Dever filial de Lyner em relação ao Comandante Leard Barsett."
        },
        6110: {
            "curated_ptbr": "Vamos à catedral primeiro.",
            "rationale": "Direcionamento imediato para a Catedral de Platina."
        },

        # 6111 - 6122 (Event/47.evd) - Encontro inicial e tutorial de batalha com Aurica
        6111: {
            "curated_ptbr": "O-o quê...?",
            "rationale": "Gagueira tímida e perplexidade inicial de Aurica (な、なに?)."
        },
        6112: {
            "curated_ptbr": "Isso é... Harmonics. Você é uma Reyvateil?!",
            "rationale": "Assombro e termos canônicos Harmonics e Reyvateil na primeira conexão."
        },
        6113: {
            "curated_ptbr": "......",
            "rationale": "Silêncio constrangido e insegurança de Aurica."
        },
        6114: {
            "curated_ptbr": "Então fica mais fácil! Me empresta a sua força!",
            "rationale": "Pragmatismo impulsivo e caloroso de Lyner (だったら話は早い)."
        },
        6115: {
            "curated_ptbr": "...O meu poder não serve para nada.",
            "rationale": "Subtexto de baixa autoestima e trauma de Aurica (...私の力なんて、なんの役にも立たない)."
        },
        6116: {
            "curated_ptbr": "Não se preocupa! Só preciso que você cante!",
            "rationale": "Encorajamento franco e direto de Lyner."
        },
        6117: {
            "curated_ptbr": "Eu sou uma Reyvateil Classe D... Nem sei tantas Canções assim...",
            "rationale": "Hesitação e autodepreciação técnica de Aurica (クラスD)."
        },
        6118: {
            "curated_ptbr": "Classe...? Deixa isso pra lá, não faz diferença! Canta como você sempre faz!",
            "rationale": "Desdém de Lyner por rótulos burocráticos e apelo à espontaneidade."
        },
        6119: {
            "curated_ptbr": "...Não consigo, eu... não sei... O que eu faço?",
            "rationale": "Desespero tímido e paralisia de combate de Aurica."
        },
        6120: {
            "curated_ptbr": "Hã?! Enfim, só canta uma Canção! Uma bem impressionante!",
            "rationale": "Afobação juvenil e cobrança expressiva de Lyner (すごいやつ!)."
        },
        6121: {
            "curated_ptbr": "...Qual Canção eu canto?... Escolhe para mim.",
            "rationale": "Submissão meiga e entrega de controle a Lyner (...選んで)."
        },
        6122: {
            "curated_ptbr": "Quando vir a indicação no canto inferior direito, aperte o botão IM03 para me dar ordens.",
            "rationale": "Preservação da tag de controle IM03 e instrução de combate da interface."
        },

        # 6123 - 6126 (Event/330.evd) - Radolf e Tastiella
        6123: {
            "curated_ptbr": "Senhor Bispo, gostaria de lhe perguntar uma coisa.",
            "rationale": "Dicção militar respeitosa e solene de Radolf (司祭様)."
        },
        6124: {
            "curated_ptbr": "Na verdade, durante nossa missão, surgiu a necessidade de um item capaz de canalizar poder sinfônico...",
            "rationale": "Linguagem técnica e precisa de Radolf com 'poder sinfônico' (導力)."
        },
        6125: {
            "curated_ptbr": "Compreendo... Faz sentido. Contudo... para ser sincero, sou um leigo no que tange ao Grathmeld...",
            "rationale": "Tom professoral e confissão de desconhecimento alquímico de Tastiella."
        },
        6126: {
            "curated_ptbr": "A esse respeito, creio que o pessoal da Tenba ou do Beco Vagalume entenda muito melhor do assunto.",
            "rationale": "Topônimos e facções canônicas: Tenba e Beco Vagalume (ほたる横丁)."
        },

        # 6127 (Event/377.evd)
        6127: {
            "curated_ptbr": "Não adianta, não abre. Está completamente bloqueado.",
            "rationale": "Frustração física de Lyner diante de uma passagem lacrada."
        },

        # 6128 - 6167 (Event/878.evd) - Presente de Misha: Hakama Decorada
        6128: {
            "curated_ptbr": "Lyner, Lyner! Finalmente ficou pronta!!",
            "rationale": "Entusiasmo eufórico e carinhoso de Misha (ライナーライナー!!)."
        },
        6129: {
            "curated_ptbr": "Você parece bem animada. E o que foi que ficou pronto?",
            "rationale": "Curiosidade afetuosa e descontraída de Lyner."
        },
        6130: {
            "curated_ptbr": "Um presente pra você! Deu um tra-ba-lhão danado pra fazer!",
            "rationale": "Orgulho de artífice de Misha com ênfase expressiva (すっ......ごい)."
        },
        6131: {
            "curated_ptbr": "Um presente pra mim? Poxa, valeu!",
            "rationale": "Reação alegre e calorosa de Lyner."
        },
        6132: {
            "curated_ptbr": "Fufun... Quando você vir com os próprios olhos, vai ficar centenas de vezes mais feliz!",
            "rationale": "Vocalização característica de Misha (ふふ~ん) e vaidade afetuosa."
        },
        6133: {
            "curated_ptbr": "Então toma, é todo seu! Minha grande obra-prima: a [Hakama Decorada]!",
            "rationale": "Apresentação teatral do item canônico [Hakama Decorada] (もんつきはかま)."
        },
        6134: {
            "curated_ptbr": "Ha... Hakamaaa?!",
            "rationale": "Choque cômico e desconcerto de Lyner."
        },
        6135: {
            "curated_ptbr": "Isso aí! E ainda vem com o brasão da família do Lyner estampado!",
            "rationale": "Exaltação de Misha destacando o brasão familiar (家紋)."
        },
        6136: {
            "curated_ptbr": "E-espera aí um instante! Nem eu conhecia esse brasão, como é que você sabe qual é?!",
            "rationale": "Indignação cômica de Lyner sobre seu próprio brasão de família."
        },
        6137: {
            "curated_ptbr": "Ora, como assim? Eu vi quando a gente era pequeno!",
            "rationale": "Cumplicidade e memórias de infância em Platina compartilhadas por Misha."
        },
        6138: {
            "curated_ptbr": "Um X dentro de três círculos concêntricos, é...? O brasão da minha família é bem brega, hein.",
            "rationale": "Autocrítica hilária de Lyner ao brasão Barsett (すごくダサいな)."
        },
        6139: {
            "curated_ptbr": "Brasão de família é tudo assim mesmo! Mas esquece isso, olha que incrível essa hakama!",
            "rationale": "Desdém bem-humorado de Misha redirecionando a atenção para sua criação."
        },
        6140: {
            "curated_ptbr": "É, realmente é impressionante... O tecido parece super-resistente...",
            "rationale": "Admissão sincera de qualidade de confecção por Lyner."
        },
        6141: {
            "curated_ptbr": "Não é? Eu já disse que deu o maior trabalhão!",
            "rationale": "Autoafirmação orgulhosa de Misha."
        },
        6142: {
            "curated_ptbr": "É-é claro, costurar uma hakama não deve ser nada fácil...",
            "rationale": "Concordância cautelosa de Lyner."
        },
        6143: {
            "curated_ptbr": "Por isso mesmo me esforcei tanto! Gostou dela?",
            "rationale": "Busca por aprovação e validação emocional carinhosa de Misha."
        },
        6144: {
            "curated_ptbr": "Gostei, fiquei muito feliz! Obrigado mesmo, Misha.",
            "rationale": "Gratidão genuína e doce de Lyner."
        },
        6145: {
            "curated_ptbr": "Ehehe, de nada! Agora é só vestir ela e dar tudo de si nas batalhas, viu?",
            "rationale": "Riso meigo (えへへ) seguido da pegadinha tática: usá-la em combate!"
        },
        6146: {
            "curated_ptbr": "Pode deixar!... Espera aí, o quê? Na batalha?!",
            "rationale": "Timing cômico perfeito de assimilação e espanto de Lyner."
        },
        6147: {
            "curated_ptbr": "Esqueci de avisar, mas reforcei essa hakama até o limite do possível!",
            "rationale": "Explicação técnica impetuosa de Misha."
        },
        6148: {
            "curated_ptbr": "Fiz justamente para ser útil em combate! Qualquer armadura comum passa vergonha perto dela!",
            "rationale": "Gabarito de qualidade de Misha desdenhando armaduras metálicas."
        },
        6149: {
            "curated_ptbr": "P-por que você foi fazer um negócio tão blindado assim?",
            "rationale": "Perplexidade desconfiada de Lyner."
        },
        6150: {
            "curated_ptbr": "O-ora, é claro que é... pro Lyner poder vestir o tempo todo!",
            "rationale": "Gagueira adorável e confissão velada de afeto de Misha."
        },
        6151: {
            "curated_ptbr": "E não é só defesa, não! Ela ainda concede dano extra de todos os elementos!",
            "rationale": "Atributos táticos de RPG descritos com entusiasmo."
        },
        6152: {
            "curated_ptbr": "Como eu botei todos os meus sentimentos por você nela, o seu HP também vai disparar lá em cima!",
            "rationale": "Declaração de sentimentos límpida disfarçada de bônus de atributos (思いを込めて)."
        },
        6153: {
            "curated_ptbr": "...O poder dos sentimentos é uma coisa impressionante mesmo...",
            "rationale": "Reflexão irônica e filosófica de Lyner sobre a magia emocional."
        },
        6154: {
            "curated_ptbr": "Sendo assim... você vai vestir, não vai?",
            "rationale": "Pressão carinhosa e insistente de Misha."
        },
        6155: {
            "curated_ptbr": "...É sério mesmo?",
            "rationale": "Tentativa desesperada de Lyner de verificar se é brincadeira."
        },
        6156: {
            "curated_ptbr": "Seríssimo! Eu fiz justamente pra você usar!",
            "rationale": "Determinação inabalável de Misha."
        },
        6157: {
            "curated_ptbr": "Mas, puxa... essas abas soltas esvoaçando no meio da luta vão atrapalhar meus movimentos...",
            "rationale": "Argumento tático de Lyner sobre o corte largo da hakama (ビラビラしてる)."
        },
        6158: {
            "curated_ptbr": "Parece que sim, mas planejei tudo pra você nem sentir nada!",
            "rationale": "Confiança mecânica e têxtil de Misha."
        },
        6159: {
            "curated_ptbr": "...I-isso é impressionante...",
            "rationale": "Rendição atônita de Lyner."
        },
        6160: {
            "curated_ptbr": "Ah, para de me bajular! E então, vai vestir?",
            "rationale": "Impaciência fofa e foco no ultimato."
        },
        6161: {
            "curated_ptbr": "É-é que... bem... é uma hakama, né? Eu vou ficar parecendo um peixe fora d'água...",
            "rationale": "Medo do ridículo social de Lyner (俺だけ浮いちゃうし)."
        },
        6162: {
            "curated_ptbr": "É mais resistente do que uma armadura, não tem problema nenhum! Então, vai vestir?",
            "rationale": "Reiteração de superioridade prática de Misha."
        },
        6163: {
            "curated_ptbr": "............",
            "rationale": "Pausa silenciosa de pânico absoluto de Lyner."
        },
        6164: {
            "curated_ptbr": "Vai vestir, não vai?",
            "rationale": "Olhar intimidador e fofo de Misha encurralando o herói."
        },
        6165: {
            "curated_ptbr": "...P-por favor, me deixa pensar só mais um pouquinho...",
            "rationale": "Lyner apelando à polidez defensiva para adiar o inevitável."
        },
        6166: {
            "curated_ptbr": "Obteve o item [Hakama Decorada]!",
            "rationale": "Notificação canônica de obtenção de item com colchetes balanceados."
        },
        6167: {
            "curated_ptbr": "Lyner? Posso entrar?",
            "rationale": "Misha pedindo licença antes de adentrar os aposentos."
        },

        # 6168 - 6170 (Event/709.evd) - Cosmosfera Nível 2 Aurica
        6168: {
            "curated_ptbr": "Então este é o mundo do Nível 2... Tenho a impressão de que os espinhos diminuíram um pouco.",
            "rationale": "Constatação visual de Lyner sobre a diminuição dos espinhos psíquicos."
        },
        6169: {
            "curated_ptbr": "Sim... De fato. Em suma, significa que o coração da senhorita Aurica se abriu um pouco...",
            "rationale": "Explicação afetuosa e digna do guardião Don Leon."
        },
        6170: {
            "curated_ptbr": "É mesmo? Então com certeza o lugar deve estar mais tranquilo que antes.",
            "rationale": "Otimismo de Lyner diante da evolução psicológica de Aurica."
        },

        # 6171 - 6193 (Event/776.evd) - Quest da Dor de Dente do Don Leon
        6171: {
            "curated_ptbr": "Nossa, mas que castelo esquisito... Já que o item se chama \"Dor de Dente do Don Leon\", será que é aqui que ele mora...?",
            "rationale": "Monólogo dedutivo de Lyner associando o castelo ao item de Marie."
        },
        6172: {
            "curated_ptbr": "Oh, Lyner!! Ai, ai, ai, aiii...",
            "rationale": "Gritos cômicos de agonia de Don Leon (いててて...)."
        },
        6173: {
            "curated_ptbr": "Uou!! Você tá aqui mesmo! Ei, não vai se apossando do castelo dos outros sem permissão!",
            "rationale": "Espanto cômico de Lyner repreendendo a invasão do guardião."
        },
        6174: {
            "curated_ptbr": "N-não é nada disso! Nem este guerreiro imaginava se encontrar em semelhante aperto! Ai, ai, aiii...",
            "rationale": "Dicção samurai grandiloquente de Don Leon (拙者 / アイタタタ...)."
        },
        6175: {
            "curated_ptbr": "Mas afinal, por que você tá gemendo de tanta dor?",
            "rationale": "Pergunta direta e coloquial de Lyner."
        },
        6176: {
            "curated_ptbr": "N-não é nada, ora essa!",
            "rationale": "Orgulho ferido e teimosia de Don Leon tentando disfarçar a dor."
        },
        6177: {
            "curated_ptbr": "Bom, tanto faz.",
            "rationale": "Desdém casual de Lyner."
        },
        6178: {
            "curated_ptbr": "A Aurica... quer dizer, a Marie tá querendo uma tal de [Dor de Dente do Don Leon]. Você não sabe de nada a respeito?",
            "rationale": "Correção de persona da Cosmosfera (Aurica -> Marie) e citação do item."
        },
        6179: {
            "curated_ptbr": "Nunca ouvi falar de tal disparate! Ai, ai, aiii...",
            "rationale": "Negação enfática em registro samurai de Don Leon (そんなものは知らん!)."
        },
        6180: {
            "curated_ptbr": "Don Leon... por acaso você... tá com cárie no dente?",
            "rationale": "Diagnóstico cirúrgico e desconfiado de Lyner (虫歯か?)."
        },
        6181: {
            "curated_ptbr": "Droga! Fui descoberto! A maior vergonha de toda a existência deste nobre guerreiro!!",
            "rationale": "Teatralidade épica de Don Leon admitindo sua humilhação (一生一度の不覚!!)."
        },
        6182: {
            "curated_ptbr": "Andei comendo doces em excesso ultimamente... e acabei com uma tremenda dor de dente...",
            "rationale": "Confissão desajeitada de gula infantil por doces."
        },
        6183: {
            "curated_ptbr": "Meus pêsames por você...",
            "rationale": "Ironia fúnebre zombeteira de Lyner (ご愁傷様で...)."
        },
        6184: {
            "curated_ptbr": "Hum?... Espera um pouco...",
            "rationale": "O estalo cognitivo de Lyner ligando os fatos."
        },
        6185: {
            "curated_ptbr": "Q-que foi?!",
            "rationale": "Pavor repentino de Don Leon pressentindo o perigo."
        },
        6186: {
            "curated_ptbr": "É isso!! Consegui a [Dor de Dente do Don Leon]!!!",
            "rationale": "Comemoração extasiada de Lyner pela solução do enigma (ゲットぉぉ!!!)."
        },
        6187: {
            "curated_ptbr": "Ei! Alto lá! O que pensa que vai fazer com os dentes deste nobre servo?!",
            "rationale": "Defesa de integridade física de Don Leon em registro arcaico."
        },
        6188: {
            "curated_ptbr": "Vou arrancar esse dente e levar comigo!",
            "rationale": "Decisão implacável e absurda típica da Cosmosfera."
        },
        6189: {
            "curated_ptbr": "Uou! Ficou louco?! Para com isso, larga de ser idiota!",
            "rationale": "Desespero histérico de Don Leon (バカ野郎! こら、やめろ!)."
        },
        6190: {
            "curated_ptbr": "Já é meu!!!",
            "rationale": "Triunfo físico de extração de Lyner (いただきっ!!!)."
        },
        6191: {
            "curated_ptbr": "Gyaaaaaahhh!!! Que doooor dos infernoooos!!",
            "rationale": "Urro de agonia cósmica de Don Leon (イテェェェーーー!)."
        },
        6192: {
            "curated_ptbr": "Foi mal, Don Leon! Mas aguenta firme, pensa que é tudo pelo bem da Aurica!",
            "rationale": "Pedido de desculpas cínico mas altruísta de Lyner em prol de sua heroína."
        },
        6193: {
            "curated_ptbr": "Obteve o item [Dor de Dente do Don Leon]!",
            "rationale": "Notificação canônica de item de evento obtido."
        },

        # 6194 - 6195 (Event/397.evd) - Centro de Mergulho
        6194: {
            "curated_ptbr": "Gostaria de realizar o Mergulho?",
            "rationale": "Pergunta padrão de serviço do operador de Mergulho."
        },
        6195: {
            "curated_ptbr": "Fica para uma próxima oportunidade, então.",
            "rationale": "Despedida polida do atendente do Dive Shop."
        },

        # 6196 (Event/432.evd)
        6196: {
            "curated_ptbr": "Não tem cabimento sair lá fora agora...",
            "rationale": "Constatação lógica de Lyner sobre a rota bloqueada."
        },

        # 6197 - 6214 (Event/957.evd) - Conversa noturna com Shurelia sobre Instalação
        6197: {
            "curated_ptbr": "Com licença, Senhora Shurelia... posso lhe perguntar uma coisa?",
            "rationale": "Reverência cerimoniosa de Lyner ao se dirigir à deusa de Sol Ciel."
        },
        6198: {
            "curated_ptbr": "Sim, do que se trata?",
            "rationale": "Resposta serena e cortês de Shurelia."
        },
        6199: {
            "curated_ptbr": "...E-eu sei que pode soar estranho fazer uma pergunta dessas, mas...",
            "rationale": "Hesitação tímida de Lyner tateando um assunto íntimo."
        },
        6200: {
            "curated_ptbr": "?",
            "rationale": "Ponto de interrogação original preservado denotando inocência."
        },
        6201: {
            "curated_ptbr": "A Senhora Shurelia... também pode receber uma Instalação?",
            "rationale": "A pergunta proibida: viabilidade biotecnológica de Instalar na Deusa."
        },
        6202: {
            "curated_ptbr": "...Como?",
            "rationale": "Surpresa e rubor sutil de Shurelia (...え?)."
        },
        6203: {
            "curated_ptbr": "A-ah, não, não é que eu queira fazer isso nem nada do tipo! É só curiosidade...",
            "rationale": "Pânico e retratação desesperada de Lyner para não soar desrespeitoso."
        },
        6204: {
            "curated_ptbr": "Em tese, sim... Mas faz tanto tempo que não passo por isso que não posso garantir nada.",
            "rationale": "Admissão técnica tímida de Shurelia sobre sua condição como Reyvateil Origin."
        },
        6205: {
            "curated_ptbr": "Seria mais prudente não alimentar grandes expectativas.",
            "rationale": "Advertência sutil de Shurelia (期待しない方が身のためです)."
        },
        6206: {
            "curated_ptbr": "N-não, eu não disse que pretendia fazer! Jamais ousaria fazer uma coisa dessas com a Senhora Shurelia...",
            "rationale": "Defesa de reverência de Lyner que acaba soando como rejeição involuntária."
        },
        6207: {
            "curated_ptbr": "...Compreendo.",
            "rationale": "Frieza contida e decepção velada de Shurelia (...そうですか)."
        },
        6208: {
            "curated_ptbr": "...Ué?",
            "rationale": "Perplexidade ingênua de Lyner sentindo a mudança de ar."
        },
        6209: {
            "curated_ptbr": "Não é nada. Claro, o senhor não disse em momento algum que pretendia fazer isso, não é verdade?",
            "rationale": "Ironia passivo-agressiva fofa de Shurelia emburrada."
        },
        6210: {
            "curated_ptbr": "Peço a gentileza de evitar comentários dúbios. O senhor já deve ir descansar, não? Sendo assim... uma boa noite.",
            "rationale": "Expulsão polida e orgulhosa de Shurelia encerrando a conversa."
        },
        6211: {
            "curated_ptbr": "Ah...",
            "rationale": "Vocalização atônita de Lyner deixado no vácuo."
        },
        6212: {
            "curated_ptbr": "Será que eu falei alguma besteira...?",
            "rationale": "Inocência desconcertada de Lyner sem entender a reação feminina."
        },
        6213: {
            "curated_ptbr": "Senhora Shurelia, a senhora tem um instante?",
            "rationale": "Tentativa cautelosa de reaproximação com a administradora."
        },
        6214: {
            "curated_ptbr": "Sim. Fique à vontade.",
            "rationale": "Hospitalidade régia e serena de Shurelia concedendo audiência."
        },

        # 6215 - 6220 (Event/115.evd) - Portão do Anteparo B2 e Verso Hymmnos
        6215: {
            "curated_ptbr": "Aqui é o Portão do Anteparo B2 nº 1. Solicitante, dê um passo à frente para identificação.",
            "rationale": "Protocolo fônico e de segurança da Torre (B2隔壁ゲートNo1)."
        },
        6216: {
            "curated_ptbr": "Autenticação por Espectro FFT concluída: Lyner Barsett. Aguardando instruções.",
            "rationale": "Terminologia oficial de autenticação por Espectro FFT."
        },
        6217: {
            "curated_ptbr": "Liberar Portão do Anteparo B2 nº 1.",
            "rationale": "Comando de voz militar emitido pelo cavaleiro Lyner."
        },
        6218: {
            "curated_ptbr": "#0Ma paks ga exec guol B2-i al noes.",
            "rationale": "Restauração integral e obrigatória do verso executável em Hymmnos ancestral iniciado por #0."
        },
        6219: {
            "curated_ptbr": "Código autenticado.",
            "rationale": "Confirmação do sistema de segurança fônica da Torre."
        },
        6220: {
            "curated_ptbr": "Abertura do anteparo em dois segundos. Condição: passagem autorizada.",
            "rationale": "Contagem regressiva de despressurização e liberação de trânsito."
        },

        # 6221 - 6233 (Event/31.evd) - Boatos das Feras Azuis na Floresta Cello
        6221: {
            "curated_ptbr": "Ouvi dizer que surgiram umas Feras Azuis na Floresta Cello atacando as pessoas. Que pavor...",
            "rationale": "Topônimo Floresta Cello e monstros canônicos Feras Azuis (青い獣)."
        },
        6222: {
            "curated_ptbr": "Dizem que essas Feras Azuis reviram as bagagens dos viajantes e roubam tudo o que encontram.",
            "rationale": "Detalhe de comportamento de pilhagem dos monstros."
        },
        6223: {
            "curated_ptbr": "Parece que as Feras Azuis da Floresta Cello não sofrem um arranhão sequer com espadas ou tiros, sabia?",
            "rationale": "Imunidade física a armas comuns mencionada no original (剣や銃じゃ倒せない)."
        },
        6224: {
            "curated_ptbr": "Fiquei sabendo que lá no Mercado ao Ar Livre tem um cartão de receita para criar algo capaz de derrotar as feras.",
            "rationale": "Localização Mercado ao Ar Livre (青空市場) e cartão de receita."
        },
        6225: {
            "curated_ptbr": "Se não me engano, o nome é [Cartão A067]...",
            "rationale": "Nome do item de síntese [Cartão A067]."
        },
        6226: {
            "curated_ptbr": "Estou prestes a atravessar a Floresta Cello.",
            "rationale": "Declaração de rota de viajante."
        },
        6227: {
            "curated_ptbr": "Para me precaver contra as Feras Azuis, pretendo comprar o [Cartão A067] nesta loja.",
            "rationale": "Prevenção tática citando o [Cartão A067] e as Feras Azuis."
        },
        6228: {
            "curated_ptbr": "Ainda bem que sou um Melder.",
            "rationale": "Orgulho de classe artesanal (メルク / Melder)."
        },
        6229: {
            "curated_ptbr": "Dizem que o velhinho do Mercado ao Ar Livre é um Melder de grande renome.",
            "rationale": "Referência a Pombad como Melder consagrado."
        },
        6230: {
            "curated_ptbr": "Quem diria, as aparências realmente enganam.",
            "rationale": "Reflexão sobre a simplicidade de Pombad."
        },
        6231: {
            "curated_ptbr": "Graças àquelas Feras Azuis empesteando a Floresta Cello, fiquei totalmente encurralado aqui.",
            "rationale": "Frustração de caravaneiro ilhado."
        },
        6232: {
            "curated_ptbr": "Ouvi dizer que elas pilham toda a carga dos viajantes. Para um mercador, isso é o fim do mundo!",
            "rationale": "Perspectiva comercial e desespero de negociante."
        },
        6233: {
            "curated_ptbr": "Dizem por aí que as afamadas Feras Azuis podem ser derrotadas com uma bomba fabricada por um Melder, sabia?",
            "rationale": "Dica de síntese alquímica para superação do obstáculo de combate."
        },

        # 6234 - 6257 (Event/36.evd) - Teste de Melder com Pombad e Noelle
        6234: {
            "curated_ptbr": "Oho! Finalmente conseguiu forjar! Um item legítimo através do Grathmeld!",
            "rationale": "Exaltação de mestre de Pombad celebrando a síntese de Lyner."
        },
        6235: {
            "curated_ptbr": "E aí, o que achou? Tenho bastante confiança no resultado!",
            "rationale": "Orgulho jovem de Lyner apresentando sua criação."
        },
        6236: {
            "curated_ptbr": "Muito bem! Está aprovado!",
            "rationale": "Certificação oficial expedida pelo mestre (合格じゃ!)."
        },
        6237: {
            "curated_ptbr": "Agora você é um Melder oficial! Toda síntese de itens daqui em diante é uma aplicação prática disso.",
            "rationale": "Reconhecimento de status como Melder."
        },
        6238: {
            "curated_ptbr": "Com perseverança, você será capaz de criar os artefatos mais complexos que existem.",
            "rationale": "Ensinamento filosófico e artesanal de Pombad."
        },
        6239: {
            "curated_ptbr": "Aí, velhote, e cadê o prêmio prometido?",
            "rationale": "Cobrança mercenária despojada de Jack."
        },
        6240: {
            "curated_ptbr": "Oho, é mesmo, quase me esquecia!",
            "rationale": "Memória dispersa do ancião Pombad."
        },
        6241: {
            "curated_ptbr": "Ô Noelle! Vem cá, Noelle!",
            "rationale": "Chamado à neta Noelle (ナール / Naal)."
        },
        6242: {
            "curated_ptbr": "Já vou, já vou! Que foi, vovô?",
            "rationale": "Entrada animada e prestativa de Noelle."
        },
        6243: {
            "curated_ptbr": "Vou te conceder a minha preciosa neta Noelle como recompensa!",
            "rationale": "A pegadinha clássica do avô oferecendo a neta como prêmio."
        },
        6244: {
            "curated_ptbr": "...Hã?!",
            "rationale": "Choque paralisante de Lyner (...は?)."
        },
        6245: {
            "curated_ptbr": "Quê?!",
            "rationale": "Reação atordoada de Noelle (へ?)."
        },
        6246: {
            "curated_ptbr": "Vovôôô!!!!",
            "rationale": "Grito de indignação e vergonha filial de Noelle."
        },
        6247: {
            "curated_ptbr": "É b-brincadeira, gente! Céus, a juventude de hoje não sabe distinguir uma piadinha esperta da realidade?!",
            "rationale": "Gargalhada de Pombad zombando da falta de malícia dos jovens."
        },
        6248: {
            "curated_ptbr": "E então?! O que você quer, afinal?!",
            "rationale": "Noelle impaciente e emburrada com a piada do avô."
        },
        6249: {
            "curated_ptbr": "Entregue aquela encomenda ao nosso estimado hóspede.",
            "rationale": "Instrução formal de entrega do prêmio real."
        },
        6250: {
            "curated_ptbr": "Quer dizer que... você conseguiu realizar o Grathmeld! Meus parabéns!!",
            "rationale": "Alegria contagiante de Noelle parabenizando Lyner."
        },
        6251: {
            "curated_ptbr": "Espera só um instantinho, tá?",
            "rationale": "Simpatia e prontidão da atendente."
        },
        6252: {
            "curated_ptbr": "Tcharããã! Aqui está o seu prêmio! Parabéns pra você!",
            "rationale": "Onomatopeia festiva (ぱんぱかぱーん!) de entrega."
        },
        6253: {
            "curated_ptbr": "Obteve 10 [Pedras Azuis]!",
            "rationale": "Notificação canônica do item básico [Pedras Azuis]."
        },
        6254: {
            "curated_ptbr": "Obteve 10 [Pedras Vermelhas]!",
            "rationale": "Notificação canônica do item básico [Pedras Vermelhas]."
        },
        6255: {
            "curated_ptbr": "P-pedras?!",
            "rationale": "Desapontamento cômico de Lyner esperando algo lendário."
        },
        6256: {
            "curated_ptbr": "São a matéria-prima elementar de todo o Grathmeld, meu jovem!",
            "rationale": "Lição de pragmatismo químico de Pombad."
        },
        6257: {
            "curated_ptbr": "Continue se esforçando bastante nas sínteses, ouviu?",
            "rationale": "Incentivo doce e carinhoso de Noelle."
        },

        # 6258 - 6262 (Event/509.evd) - Documentos confidenciais
        6258: {
            "curated_ptbr": "Estes documentos...",
            "rationale": "Tensão investigativa de Lyner ao encontrar arquivos secretos."
        },
        6259: {
            "curated_ptbr": "\"[Quando o projeto for concluído... o próprio Falss se tornará descartável...]\"",
            "rationale": "Leitura textual do plano de traição de Bourd contra o Bispo Falss."
        },
        6260: {
            "curated_ptbr": "\"[Nessa ocasião... aproveitando para realizar um teste prático, farei com que as Reyvateils o ataquem...]\"",
            "rationale": "Crueldade maquiavélica planejando usar Reyvateils como armas descartáveis."
        },
        6261: {
            "curated_ptbr": "...Não havia a menor ponta de confiança entre eles...",
            "rationale": "Repulsa moral de Lyner diante da baixeza dos conspiradores."
        },
        6262: {
            "curated_ptbr": "No fundo, não passava de uma aliança de conveniência.",
            "rationale": "Avaliação estóica e experiente do cavaleiro Radolf."
        },

        # 6263 - 6271 (Event/586.evd) - Hama e o Código Hymmnos de Misha
        6263: {
            "curated_ptbr": "Hama! Ô Hama! Cheguei ao Nível 4! Me conta o Código Hymmnos!",
            "rationale": "Cobrança energética e empolgada de Lyner a Hama na Cosmosfera."
        },
        6264: {
            "curated_ptbr": "......",
            "rationale": "Pausa avaliadora e relutante de Hama."
        },
        6265: {
            "curated_ptbr": "Tsc, tudo bem. Afinal de contas, promessa é promessa... Embora eu ainda não confie totalmente em você.",
            "rationale": "Resignação cética da Guardiã da Mente (ま、いいわ)."
        },
        6266: {
            "curated_ptbr": "Mas olha lá: não vá abrir o bico pra ninguém! Essa é a chave de acesso pessoal da Misha!",
            "rationale": "Advertência estrita de sigilo sobre a intimidade de Misha."
        },
        6267: {
            "curated_ptbr": "Só estou te revelando isso porque decidi colocar minha confiança em você!",
            "rationale": "Ato de fé e responsabilidade depositado em Lyner."
        },
        6268: {
            "curated_ptbr": "Sim, com certeza. Pode confiar.",
            "rationale": "Compromisso firme e solene de Lyner."
        },
        6269: {
            "curated_ptbr": "O Código Hymmnos da Misha é: [#1MISYA_FEHU_EOLIA_ARTONELICO]",
            "rationale": "Preservação integral do código ancestral Hymmnos com tag e colchetes."
        },
        6270: {
            "curated_ptbr": "Vê se não deixa vazar por nada deste mundo!",
            "rationale": "Último aviso severo e protetor de Hama."
        },
        6271: {
            "curated_ptbr": "Obrigado! Fico te devendo essa!",
            "rationale": "Gratidão efusiva e lealdade de Lyner."
        },

        # 6272 - 6273 (Event/814.evd) - Shurelia e a reprogramação do mundo virtual
        6272: {
            "curated_ptbr": "Gostaria de se aventurar novamente no mundo virtual com o programa que reescrevi outro dia?",
            "rationale": "Convite gracioso e divino de Shurelia para adentrar sua simulação."
        },
        6273: {
            "curated_ptbr": "Compreendo. Já está tudo preparado, venha quando desejar.",
            "rationale": "Prontidão serena e acolhedora da administradora."
        },

        # 6274 - 6276 (Event/249.evd) - Vendaval na Torre
        6274: {
            "curated_ptbr": "Uouuu!! Que vendaval absurdo!",
            "rationale": "Impacto corporal do vento avassalador nas alturas da Torre."
        },
        6275: {
            "curated_ptbr": "Com essa ventania, não há dirigível no mundo que consiga decolar.",
            "rationale": "Constatação técnica e cínica do veterano Jack sobre os dirigíveis."
        },
        6276: {
            "curated_ptbr": "É melhor a gente voltar para dentro da Torre...",
            "rationale": "Prudência de Lyner buscando abrigo nos corredores."
        },

        # 6277 - 6290 (Event/738.evd) - Memórias de Aurica no Orfanato de Skuwat
        6277: {
            "curated_ptbr": "Don Leon! Eu tô com fome!",
            "rationale": "Grito infantil ingênuo clamando pelo protetor de pelúcia."
        },
        6278: {
            "curated_ptbr": "Calma, calma, já vou preparar a comida, tá bom?",
            "rationale": "Voz maternal, terna e abnegada de Aurica cuidando das crianças."
        },
        6279: {
            "curated_ptbr": "Aqui é a casa da Aurica...?",
            "rationale": "Lyner reconhecendo o cenário das memórias de Aurica na Cosmosfera."
        },
        6280: {
            "curated_ptbr": "A comida ainda não tá pronta?",
            "rationale": "Impaciência típica de criança faminta."
        },
        6281: {
            "curated_ptbr": "Já tá quase saindo! Espera só mais um pouquinho!",
            "rationale": "Doçura e dedicação incansável de Aurica."
        },
        6282: {
            "curated_ptbr": "Don Leooon! Quero ir ao banheirooo!",
            "rationale": "Apelo infantil dramático chamando pelo boneco."
        },
        6283: {
            "curated_ptbr": "Tá bom, tá bom, vem cá que eu te levo ao banheiro.",
            "rationale": "Paciência infinita de Aurica atendendo a criança."
        },
        6284: {
            "curated_ptbr": "Mas o que é isso...? O Don Leon afinal de contas é...?",
            "rationale": "Perplexidade de Lyner ao ver o papel de Don Leon na mente de Aurica."
        },
        6285: {
            "curated_ptbr": "Don Leon... você era o faz-tudo da Aurica?",
            "rationale": "Pergunta inquisitiva e bem-humorada de Lyner (お手伝いさん)."
        },
        6286: {
            "curated_ptbr": "Não!",
            "rationale": "Indignação categórica do samurai Don Leon."
        },
        6287: {
            "curated_ptbr": "Então era o guarda-costas dela?",
            "rationale": "Tentativa honrosa de adivinhação de Lyner."
        },
        6288: {
            "curated_ptbr": "Não!!",
            "rationale": "Rejeição veemente de Don Leon."
        },
        6289: {
            "curated_ptbr": "Então o que você é afinal? Pelo que tô vendo, não consigo imaginar mais nada...",
            "rationale": "Lógica direta de Lyner apontando as evidências visuais."
        },
        6290: {
            "curated_ptbr": "......",
            "rationale": "Silêncio embaraçado e derrotado de Don Leon."
        },

        # 6291 - 6292 (Event/660.evd) - Cosmosfera Nível 9 Misha
        6291: {
            "curated_ptbr": "Finalmente o Nível 9...",
            "rationale": "Marco emocional de profundidade máxima no coração de Misha."
        },
        6292: {
            "curated_ptbr": "A Misha tá me esperando por lá... né? É hora de ir.",
            "rationale": "Determinação amorosa de Lyner para alcançar o núcleo da psique de Misha."
        },

        # 6293 (Event/476.evd)
        6293: {
            "curated_ptbr": "Preciso encontrar meu pai e levar a Senhora Shurelia conosco... Primeiro, rumo à catedral.",
            "rationale": "Planejamento tático de Lyner priorizando o encontro na Catedral de Platina."
        },

        # 6294 - 6319 (Event/166.evd) - Apresentação da fada Lyra e reações do grupo
        6294: {
            "curated_ptbr": "Mano Harm!",
            "rationale": "Saudação infantil e calorosa de Lyra a Jack (アル兄ぃ!)."
        },
        6295: {
            "curated_ptbr": "Opa! L-Lyra, é você?!",
            "rationale": "Desconcerto imediato do durão mercenário Jack."
        },
        6296: {
            "curated_ptbr": "Mano Harm! Onde é que você tava? A Lyra tava morrendo de saudade!",
            "rationale": "Dengo infantil e afeto efusivo da garota mercante."
        },
        6297: {
            "curated_ptbr": "E-ei, calma lá...!",
            "rationale": "Constrangeamento de Jack perante os companheiros."
        },
        6298: {
            "curated_ptbr": "Ora, ora... Então a praia do Jack é esse tipo de coisa.",
            "rationale": "Provocação maliciosa e sarcástica da engenheira Krusche."
        },
        6299: {
            "curated_ptbr": "E-espera aí, não viaja! Não tem nada a ver!",
            "rationale": "Pânico defensivo de Jack tentando abafar os mal-entendidos."
        },
        6300: {
            "curated_ptbr": "Mano Harm♪",
            "rationale": "Carinho melódico e inocente de Lyra agravando a situação."
        },
        6301: {
            "curated_ptbr": "As aparências realmente enganam...",
            "rationale": "Julgamento estóico e solene de Radolf abalando ainda mais Jack."
        },
        6302: {
            "curated_ptbr": "Lolicon.",
            "rationale": "Estocada cirúrgica, fulminante e canônica de Krusche (ロリコン)."
        },
        6303: {
            "curated_ptbr": "Tô falando que não é nada disso, droga!",
            "rationale": "Desespero total de Jack diante do veredito da equipe."
        },
        6304: {
            "curated_ptbr": "O nome dela é Lyra.",
            "rationale": "Apresentação formal forçada para tentar retomar a seriedade."
        },
        6305: {
            "curated_ptbr": "Sou a Lyra, e pronto!",
            "rationale": "Bordão verbal característico de Lyra adaptando ~なのだ ('...e pronto!')."
        },
        6306: {
            "curated_ptbr": "Ela trabalha encontrando e fornecendo itens.",
            "rationale": "Explicação da função mercantil da fada."
        },
        6307: {
            "curated_ptbr": "Fornecendo itens, e pronto!",
            "rationale": "Eco rítmico com bordão característico (~なのだ)."
        },
        6308: {
            "curated_ptbr": "Se você encomendar com ela, ela dá um jeito de descolar os itens.",
            "rationale": "Descrição do serviço de busca sob encomenda."
        },
        6309: {
            "curated_ptbr": "Vou descolar tudinho, e pronto!",
            "rationale": "Reafirmação energética infantil com bordão (~なのだ)."
        },
        6310: {
            "curated_ptbr": "Claro que o serviço dela tem um preço.",
            "rationale": "Alerta pragmático de mercenário sobre os custos."
        },
        6311: {
            "curated_ptbr": "Tem preço sim, e pronto!",
            "rationale": "Concordância comercial de Lyra (~なのだ)."
        },
        6312: {
            "curated_ptbr": "B-bom... prazer em conhecê-la.",
            "rationale": "Polidez desconcertada de Lyner diante da dinâmica inusitada."
        },
        6313: {
            "curated_ptbr": "Prazer em conhecer, e pronto!",
            "rationale": "Cumprimento simpático com bordão (~なのだ)."
        },
        6314: {
            "curated_ptbr": "Até que ela é uma gracinha.",
            "rationale": "Krusche amolecendo e achando a menina fofa (かわいいかも)."
        },
        6315: {
            "curated_ptbr": "E era isso.",
            "rationale": "Encerramento seco de Jack querendo mudar de assunto."
        },
        6316: {
            "curated_ptbr": "Era isso sim, e pronto!",
            "rationale": "Finalização triunfante de Lyra (~なのだ)."
        },
        6317: {
            "curated_ptbr": "Ao conversar com Lyra, você poderá encomendar a busca e o fornecimento de itens.",
            "rationale": "Tutorial de sistema do mecanismo de procura de itens."
        },
        6318: {
            "curated_ptbr": "Para encomendar itens, você precisará de Cristais Grathnode. Quanto maior for a qualidade do cristal entregue, melhores serão os itens obtidos.",
            "rationale": "Explicação do custo em Cristais Grathnode e correlação com a qualidade."
        },
        6319: {
            "curated_ptbr": "Experimente fazer encomendas com ela em diversos locais diferentes.",
            "rationale": "Incentivo à exploração em variados cenários do mapa."
        },

        # 6320 - 6321 (Event/211.evd) - Busca por Aurica em Platina
        6320: {
            "curated_ptbr": "Falando nisso, para onde terá ido a Aurica?",
            "rationale": "Preocupação de Lyner com o paradeiro de sua companheira."
        },
        6321: {
            "curated_ptbr": "Ela não teria ido lá para fora... Será que passou pelo túnel subterrâneo e foi para o Gather...?",
            "rationale": "Dedução toponímica canônica citando a plataforma de observação [O Gather] (ギャザー)."
        },

        # 6322 - 6335 (Event/513.evd) - Informações de inteligência com Spica em Porto Gaivota
        6322: {
            "curated_ptbr": "E aí, Spica.",
            "rationale": "Cumprimento camarada de Lyner à comerciante felina."
        },
        6323: {
            "curated_ptbr": "Ora, ora... seja bem-vindo!",
            "rationale": "Acolhida calorosa e manhosa de Spica."
        },
        6324: {
            "curated_ptbr": "Vai uma Bala de Gato? Sai por apenas 12 Leaf cada uma♪",
            "rationale": "Termos canônicos [Bala de Gato] (猫飴) e moeda Leaf (12 Leaf) com nota musical."
        },
        6325: {
            "curated_ptbr": "O preço nem importa, eu queria mesmo era comer um balde inteiro delas!",
            "rationale": "Entusiasmo guloso de Lyner pelas Balas de Gato."
        },
        6326: {
            "curated_ptbr": "Pois não, ao seu dispor! Em que posso ajudar no dia de hoje?",
            "rationale": "Profissionalismo comercial de Spica mudando para o modo de atendimento."
        },
        6327: {
            "curated_ptbr": "Pode ser qualquer coisa: me passa todas as informações recentes que você conseguiu.",
            "rationale": "Lyner acionando a rede clandestina de inteligência de Spica."
        },
        6328: {
            "curated_ptbr": "...Vejamos...",
            "rationale": "Pausa reflexiva de Spica buscando as notícias mais quentes."
        },
        6329: {
            "curated_ptbr": "Ultimamente o exército da Tenba anda em polvorosa porque encontrou um novo sítio de escavação na Torre.",
            "rationale": "Informação geopolítica sobre a corporação militar Tenba operando na Torre."
        },
        6330: {
            "curated_ptbr": "Mas ouvi dizer que os Guardiões voltaram a atacar por lá e eles estão penando feio.",
            "rationale": "Dificuldades táticas enfrentadas pela Tenba contra os Guardiões."
        },
        6331: {
            "curated_ptbr": "Pouco tempo atrás diziam que os ataques tinham cessado e que a exploração estava mais fácil...",
            "rationale": "Contraste temporal de inteligência militar."
        },
        6332: {
            "curated_ptbr": "Mas agora parece que eles vão para lá exclusivamente para travar uma guerra contra os Guardiões.",
            "rationale": "Escalada para um estado de conflito bélico total."
        },
        6333: {
            "curated_ptbr": "Ah, então a Presidente Ayano também...",
            "rationale": "Intervenção preocupada de Krusche sobre sua mentora e líder da Tenba."
        },
        6334: {
            "curated_ptbr": "Parece que ela está no meio da correria com as tropas. Bem, como sempre, né?",
            "rationale": "Perfil ativo da Presidente Ayano em campo de batalha."
        },
        6335: {
            "curated_ptbr": "Sendo assim, acho que não vou conseguir falar com ela tão cedo...",
            "rationale": "Desapontamento afetuoso de Krusche por não poder rever Ayano."
        },

        # 6336 - 6348 (Event/532.evd) - Investigação do Espadachim de Vermelho na Loja de Pombad
        6336: {
            "curated_ptbr": "Sejam bem-vindos!",
            "rationale": "Saudação alegre e cortês de Noelle aos viajantes."
        },
        6337: {
            "curated_ptbr": "Olá! Na verdade, eu passei aqui porque queria perguntar uma coisa...",
            "rationale": "Introdução educada e objetiva de Lyner."
        },
        6338: {
            "curated_ptbr": "Pois não, o que seria?",
            "rationale": "Disponibilidade simpática de Noelle."
        },
        6339: {
            "curated_ptbr": "Por acaso não passou por aqui um espadachim vestindo armadura vermelha...?",
            "rationale": "Pergunta investigativa crucial sobre o espadachim de armadura vermelha."
        },
        6340: {
            "curated_ptbr": "Armadura vermelha... Hummm... Não vi ninguém assim por aqui, não.",
            "rationale": "Esforço de memória de Noelle negando o avistamento."
        },
        6341: {
            "curated_ptbr": "SC30Não veio ninguém!!1X",
            "rationale": "Preservação estrita dos códigos de engine SC30 e 1X na interrupção sonolenta de Pombad."
        },
        6342: {
            "curated_ptbr": "Vovô, você vive dormindo, como é que vai ter visto alguma coisa?!",
            "rationale": "Bronca cômica de Noelle desmascarando a soneca do avô."
        },
        6343: {
            "curated_ptbr": "Já fazia tempo que eu não via... essa discussão engraçada entre vocês dois.",
            "rationale": "Nostalgia afetuosa de Lyner diante da rotina dos amigos."
        },
        6344: {
            "curated_ptbr": "Ai, não fala isso, que vergonha! Para com isso, por favor!",
            "rationale": "Timidez graciosa de Noelle pedindo para mudar de assunto."
        },
        6345: {
            "curated_ptbr": "M-mas enfim... por estas bandas não vi ninguém com essa descrição.",
            "rationale": "Retomada do foco investigativo por Noelle."
        },
        6346: {
            "curated_ptbr": "Só que... esta cidade vive cheia de aventureiros a caminho da Colina do Canto. Pode ser que ele tenha passado despercebido...",
            "rationale": "Pista toponímica canônica apontando para a [Colina do Canto] (謳う丘)."
        },
        6347: {
            "curated_ptbr": "Colina do Canto, é...?",
            "rationale": "Reflexão pensativa de Lyner fixando o próximo destino."
        },
        6348: {
            "curated_ptbr": "Fica bem pertinho daqui, então talvez seja uma boa ideia dar uma olhada por lá!",
            "rationale": "Recomendação prestativa de Noelle encerrando o bloco com gancho dramático."
        }
    }

def main():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    curated_dict = get_curated_data()

    dialogues = []
    lines_rewritten = 0
    lines_approved_as_is = 0

    for d in input_data["dialogues"]:
        d_id = d["id"]
        if d_id not in curated_dict:
            raise KeyError(f"ID {d_id} ausente no dicionário de curadoria!")

        info = curated_dict[d_id]
        curated_text = info["curated_ptbr"]
        rationale = info["rationale"]

        # Determina o veredito comparando com o texto anterior no banco
        curr_pt = d.get("current_ptbr") or ""
        if curated_text != curr_pt:
            verdict = "rewritten"
            lines_rewritten += 1
        else:
            verdict = "approved_as_is"
            lines_approved_as_is += 1

        entry = {
            "id": d_id,
            "event_file": d.get("event_file"),
            "speaker_id": d.get("speaker_id"),
            "speaker": d.get("speaker"),
            "original_jp": d.get("original_jp"),
            "original_en": d.get("original_en"),
            "current_ptbr": curr_pt,
            "curated_ptbr": curated_text,
            "verdict": verdict,
            "rationale": rationale
        }
        dialogues.append(entry)

    highlights = [
        {
            "id": 6112,
            "speaker": "Lyner",
            "description": "Descoberta de Reyvateil e sintonia harmônica: Lyner percebe a ressonância de Harmonics com Aurica em batalha e descobre sua verdadeira natureza de donzela cantora."
        },
        {
            "id": 6133,
            "speaker": "Misha",
            "description": "Presente cômico e afetuoso de Misha: a [Hakama Decorada] bordada com o brasão familiar dos Barsett, impregnada com sentimentos juvenis para conferir bônus em todos os elementos e salto de HP."
        },
        {
            "id": 6138,
            "speaker": "Lyner",
            "description": "Autoironia familiar: Lyner descobrindo que o brasão da família Barsett (um X dentro de três círculos) é incrivelmente brega."
        },
        {
            "id": 6186,
            "speaker": "Lyner",
            "description": "Resolução hilária na Cosmosfera de Aurica: Lyner descobre que o item [Dor de Dente do Don Leon] para a boneca Marie consiste em arrancar à força o dente cariado do guardião samurai de pelúcia."
        },
        {
            "id": 6201,
            "speaker": "Lyner",
            "description": "Diálogo íntimo e embaraçoso com Shurelia: Lyner questionando a possibilidade de Instalação na deusa de Sol Ciel, gerando um clima de timidez, orgulho ferido e expulsão polida para dormir."
        },
        {
            "id": 6218,
            "speaker": "Lyner",
            "description": "Restauração canônica de verso executável em Hymmnos ancestral: resgate de '#0Ma paks ga exec guol B2-i al noes.' para liberação do [Portão do Anteparo B2 nº 1], que constava omitido no banco."
        },
        {
            "id": 6221,
            "speaker": "Personagem [64]",
            "description": "Worldbuilding e ameaça da Floresta Cello: boatos sobre as temíveis [Feras Azuis] que pilham viajantes e são imunes a lâminas e armas convencionais."
        },
        {
            "id": 6243,
            "speaker": "Pombad",
            "description": "Humor geracional no Mercado ao Ar Livre: o Mestre Pombad oferecendo sua neta Noelle como prêmio de síntese de Melder, provocando escândalo e risos antes da entrega das Pedras Azuis e Vermelhas."
        },
        {
            "id": 6260,
            "speaker": "Lyner",
            "description": "Revelação de conspiração nos arquivos confidenciais: documentos secretos provando o plano de descarte e traição contra o Bispo Falss utilizando Reyvateils como armas de ataque."
        },
        {
            "id": 6269,
            "speaker": "Moradora do Mundo Inferior (Hama)",
            "description": "Concessão sagrada de chave de acesso: Hama revelando a Lyner o Código Hymmnos pessoal de Misha '[#1MISYA_FEHU_EOLIA_ARTONELICO]' no Nível 4 de sua mente."
        },
        {
            "id": 6278,
            "speaker": "Aurica",
            "description": "Memórias do orfanato de Skuwat: Aurica acolhendo crianças famintas com paciência maternal e ternura infinita, desmistificando o papel doméstico de Don Leon."
        },
        {
            "id": 6296,
            "speaker": "Personagem [11] (Lyra)",
            "description": "Estreia da fada mercantil Lyra: saudação dengosa ao 'mano Harm' (Jack) com seu bordão verbal característico (~なのだ / '...e pronto!') e a reação fulminante de Krusche ('Lolicon.')."
        },
        {
            "id": 6324,
            "speaker": "Vendedora de Doces (Porto Gaivota) (Spica)",
            "description": "Comércio e espionagem no porto: Spica vendendo [Balas de Gato] a 12 Leaf e informando sobre a guerra da Tenba contra os Guardiões da Torre sob o comando da Presidente Ayano."
        },
        {
            "id": 6341,
            "speaker": "Pombad",
            "description": "Preservação estrita de códigos de engine: manutenção dos comandos 'SC30' e '1X' nos gritos de Pombad acordando da soneca."
        },
        {
            "id": 6346,
            "speaker": "Personagem [40] (Noelle)",
            "description": "Pista investigativa rumo à Colina do Canto: Noelle indicando o fluxo de aventureiros rumo à [Colina do Canto] (謳う丘) como provável rastro do espadachim de armadura vermelha."
        }
    ]

    new_terms = {
        "Hakama Decorada": {
            "pt": "Hakama Decorada",
            "category": "Item / Equipamento",
            "note": "もんつきはかま / Decorated Hakama. Vestimenta bordada por Misha com o brasão familiar Barsett, fortalecida com bônus elementais e de HP."
        },
        "Dor de Dente do Don Leon": {
            "pt": "Dor de Dente do Don Leon",
            "category": "Item / Evento",
            "note": "ドンスケハイタ / Don Leon's Toothache. Item de quest extraído do dente cariado de Don Leon na Cosmosfera de Aurica."
        },
        "Portão do Anteparo B2": {
            "pt": "Portão do Anteparo B2",
            "category": "Estrutura / Torre",
            "note": "B2隔壁ゲート. Comporta de segurança da Torre Ar tonelico liberada por Espectro FFT e verso executável em Hymmnos ancestral."
        },
        "Cartão A067": {
            "pt": "Cartão A067",
            "category": "Item / Receita",
            "note": "カードA067. Cartão de receita de Grathmeld vendido no Mercado ao Ar Livre para sintetizar a bomba contra as Feras Azuis."
        },
        "Pedras Azuis": {
            "pt": "Pedras Azuis",
            "category": "Item / Ingrediente",
            "note": "青い石. Minério azul básico utilizado como insumo em sínteses de Grathmeld."
        },
        "Pedras Vermelhas": {
            "pt": "Pedras Vermelhas",
            "category": "Item / Ingrediente",
            "note": "赤い石. Minério vermelho básico utilizado como insumo em sínteses de Grathmeld."
        },
        "Bala de Gato": {
            "pt": "Bala de Gato",
            "category": "Item / Alimento",
            "note": "猫飴 / Kitty Candy. Doce felino vendido por Spica em Porto Gaivota a 12 Leaf."
        },
        "Lolicon": {
            "pt": "Lolicon",
            "category": "Expressão / Diálogo",
            "note": "ロリコン. Provocação mordaz de Krusche direcionada a Jack ao ver o apego infantil de Lyra por ele."
        }
    }

    updated_address_matrix = {
        "Lyra": {
            "Jack": "Trata com devoção infantil e dengo chamando de 'Mano Harm' (アル兄ぃ) e finalizando todas as frases com seu bordão verbal característico '~なのだ' ('...e pronto!').",
            "Lyner": "Trata com simpatia comercial e espontaneidade de criança mercante."
        },
        "Jack": {
            "Lyra": "Trata como uma irmãzinha mais nova ou conhecida de trabalho que o envergonha em público, tentando manter pose de mercenário durão."
        },
        "Shurelia": {
            "Lyner": "Trata com nobreza e dignidade celestial, revelando vulnerabilidade tímida e pudor quando o assunto envolve intimidade de Instalação."
        },
        "Misha": {
            "Lyner": "Tratamento de infância com amor explícito vertido em suas sínteses, insistindo para que ele use sua [Hakama Decorada] em combate."
        },
        "Noelle": {
            "Lyner": "Tratamento hospitaleiro e animado de balconista e aprendiz de Melder.",
            "Pombad": "Tratamento de neta dedicada mas impaciente com as piadas e sonecas do avô ('Vovôôô!!!!')."
        }
    }

    scene_handoff = {
        "resumo_dramatico": "Descoberta das origens da parceria com Aurica e o primeiro despertar do Harmonics em combate; a hilária síntese da [Hakama Decorada] tecida por Misha com o brasão brega dos Barsett e impregnada de amor juvenil para infligir todos os danos elementais; a exploração do Nível 2 da Cosmosfera de Aurica com o alívio dos espinhos e o hilário roubo do dente de Don Leon [Dor de Dente do Don Leon] para a boneca Marie; o sutil e embaraçoso diálogo noturno entre Lyner e Shurelia sobre a viabilidade de uma Instalação divina em seu corpo milenar; a restauração do código executável em Hymmnos ancestral `#0Ma paks ga exec guol B2-i al noes.` para a abertura do Portão do Anteparo B2; a lenda das Feras Azuis da Floresta Cello e o teste de iniciação de Lyner como Melder sob a tutela do excêntrico Mestre Pombad e sua neta Noelle com a recompensa das Pedras Azuis e Vermelhas; os arquivos secretos revelando o plano de traição contra o Bispo Falss; a concessão solene do Código Hymmnos pessoal de Misha `[#1MISYA_FEHU_EOLIA_ARTONELICO]` por sua Guardiã Hama no Nível 4; as memórias do orfanato da igreja em Skuwat com Aurica cuidando de crianças esfomeadas; o reencontro cômico de Jack com a fada mercantil Lyra sob os olhares mordazes de Krusche ('Lolicon.') e o aprendizado sobre o comércio com Cristais Grathnode; o relato de inteligência com Spica em Porto Gaivota desvelando a guerra violenta da Tenba contra os Guardiões da Torre liderada por Ayano; e as pistas colhidas na oficina de Pombad apontando os passos do espadachim de armadura vermelha rumo à sagrada Colina do Canto.",
        "decisoes_terminologicas": {
            "Hakama Decorada": "[Hakama Decorada] (もんつきはかま / Decorated Hakama, vestimenta com o brasão familiar Barsett tecida por Misha)",
            "Dor de Dente do Don Leon": "[Dor de Dente do Don Leon] (ドンスケハイタ / Don Leon's Toothache, item de quest extraído do dente cariado do guardião)",
            "Portão do Anteparo B2": "[Portão do Anteparo B2] (B2隔壁ゲート, comporta de segurança da Torre aberta via Espectro FFT e verso Hymmnos ancestral)",
            "Feras Azuis": "[Feras Azuis] (青い獣 / Blue Wolves, criaturas imunes a lâminas e pólvora convencional na Floresta Cello)",
            "Cartão A067": "[Cartão A067] (カードA067, receita de síntese para a bomba contra as Feras Azuis)",
            "Pedras Azuis / Pedras Vermelhas": "[Pedras Azuis] / [Pedras Vermelhas] (青い石 / 赤い石, minerais básicos de Grathmeld)",
            "Código Hymmnos de Misha": "[#1MISYA_FEHU_EOLIA_ARTONELICO] (código ancestral de linhagem e chave de acesso da Origin Eolia)",
            "Lyra": "Lyra (リルラ, fada mercantil de itens com bordão verbal infantil '~のだ' / '...e pronto!')",
            "Lolicon": "Lolicon (ロリコン, acusação cômica mordaz de Krusche a Jack diante de Lyra)",
            "Bala de Gato": "[Bala de Gato] (猫飴 / Kitty Candy, guloseima vendida por Spica a 12 Leaf)",
            "Colina do Canto": "[Colina do Canto] (謳う丘 / Singing Hill, planalto sagrado onde repousam os segredos de Elemia)"
        },
        "alertas_para_proximo_bloco": "Atenção à chegada à Colina do Canto e ao confronto/encontro com o espadachim de armadura vermelha (Radolf / Ayatane), aos desdobramentos da expedição de Ayano nas escavações da Torre e às repercussões do Código Hymmnos de Misha nos níveis profundos de sua mente."
    }

    output_data = {
        "block_id": input_data.get("block_id", "BLK_EVD_024"),
        "axis_id": input_data.get("axis_id", "AXIS_3"),
        "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
        "total_lines": len(dialogues),
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "highlights": highlights,
        "new_terms": new_terms,
        "updated_address_matrix": updated_address_matrix,
        "scene_handoff": scene_handoff,
        "dialogues": dialogues
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Sucesso! Gerado {OUTPUT_PATH}")
    print(f"Total: {len(dialogues)} | Reescritas: {lines_rewritten} | Aprovadas: {lines_approved_as_is}")

if __name__ == "__main__":
    main()

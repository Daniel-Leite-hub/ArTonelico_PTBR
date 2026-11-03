# -*- coding: utf-8 -*-
"""Script para gerar BLK_EVD_051_output.json com todas as 222 falas lapidadas."""

import json
from pathlib import Path

curated_map = {
    # =========================================================================
    # EVENT/50.EVD (IDs 12010 - 12073) - 64 falas
    # Ataque de A.B.R., encontro com Aurica, tutorial de combate e convite de Radolf
    # =========================================================================
    12010: {
        "pt": "!? Que barulheira é essa por ali?",
        "notes": "Lyner nota o alvoroço repentino na cidade."
    },
    12011: {
        "pt": "Aquele ali é... o Guardião da Torre, o A.B.R.?! Por que ele está atacando as pessoas?!",
        "notes": "Lyner reconhece a máquina guardiã da Torre; fidelidade ao A.B.R."
    },
    12012: {
        "pt": "Não importa o porquê! Vamos logo ajudá-los!",
        "notes": "Jack corta divagações com urgência marcial de mercenário."
    },
    12013: {
        "pt": "!!",
        "notes": "Reação de choque diante do ataque iminente."
    },
    12014: {
        "pt": "Não...",
        "notes": "Aurica encurralada pelo guardião."
    },
    12015: {
        "pt": "Aquela garota!",
        "notes": "Lyner avista a donzela em perigo."
    },
    12016: {
        "pt": "O-O quê?",
        "notes": "Aurica surpresa com a intervenção heroica de Lyner."
    },
    12017: {
        "pt": "Isso é... Harmonics. Você é uma Reyvateil?!",
        "notes": "Lyner sente a ressonância mágica entre ambos."
    },
    12018: {
        "pt": "......",
        "notes": "Silêncio tímido e atônito de Aurica."
    },
    12019: {
        "pt": "Então fica mais fácil! Me empresta a sua força!",
        "notes": "Lyner pede suporte de canção para enfrentar o monstro."
    },
    12020: {
        "pt": "...O meu poder não serve para nada...",
        "notes": "Aurica expressa sua baixa autoestima crônica (なんの役にも立たない)."
    },
    12021: {
        "pt": "Vai dar tudo certo. Só preciso que você cante!",
        "notes": "Lyner encoraja Aurica com entusiasmo sincero."
    },
    12022: {
        "pt": "Eu sou apenas uma Reyvateil Classe D. Quase nem sei canções direito...",
        "notes": "Aurica cita sua classificação inferior (Classe D / クラスD)."
    },
    12023: {
        "pt": "Classe...? Pouco importa, isso não faz a menor diferença! Só canta como você sempre faz!",
        "notes": "Lyner desconsidera rótulos burocráticos e confia no coração dela."
    },
    12024: {
        "pt": "Lá vem ele!",
        "notes": "Avisando a investida do monstro."
    },
    12025: {
        "pt": "Não pode ser...",
        "notes": "Aurica estupefata ao ver o monstro ruir."
    },
    12026: {
        "pt": "O que foi aquilo...?! Não foi um golpe comum!",
        "notes": "Cidadão perplexo com a potência desferida."
    },
    12027: {
        "pt": "Será que ele... não é um Apóstolo de Elemia?!",
        "notes": "Especulação sagrada sobre a identidade de Lyner."
    },
    12028: {
        "pt": "Será mesmo? Ele me parece uma pessoa comum como qualquer um de nós.",
        "notes": "Outra cidadã expressa dúvida cética."
    },
    12029: {
        "pt": "Ai, ai, ai... Ei, Lyner! Você pegou pesado demais, cara!",
        "notes": "Jack repreende Lyner por se exibir em público."
    },
    12030: {
        "pt": "Eu tinha acabado de te mandar ficar na moita, e você já entrega o ouro assim?!",
        "notes": "Jack ironiza a falta de discrição (バレバレ -> entrega o ouro)."
    },
    12031: {
        "pt": "Não dava pra evitar! Olha a enrascada em que o pessoal estava!",
        "notes": "Lyner se justifica pelo impulso moral de salvar os cidadãos."
    },
    12032: {
        "pt": "...Que saco. Aconteça o que acontecer daqui pra frente, eu lavo minhas mãos, ouviu?",
        "notes": "Jack se exime de culpa no seu estilo cínico habitual."
    },
    12033: {
        "pt": "A gente conseguiu vencer graças a você. Muito obrigado!",
        "notes": "Lyner agradece com afeto e cordialidade a Aurica."
    },
    12034: {
        "pt": "Eu não fiz nada... Pelo contrário, devo ter sido só um estorvo pra você...",
        "notes": "Aurica insiste em sua pequenez (足を引っ張る -> ser um estorvo)."
    },
    12035: {
        "pt": "Não fala uma coisa dessas. Nós só conseguimos derrotá-lo porque você estava comigo.",
        "notes": "Lyner reafirma a importância vital da parceria."
    },
    12036: {
        "pt": "Se eu estivesse sozinho, com certeza teria passado um sufoco danado. Então o mérito é todo seu!",
        "notes": "Lyner valida o valor de Aurica com gentileza desarmante."
    },
    12037: {
        "pt": "......",
        "notes": "Aurica comovida pelo elogio sincero."
    },
    12038: {
        "pt": "Meus agradecimentos. Graças a vocês, o perigo que ameaçava a cidade foi contornado.",
        "notes": "Radolf intervém com solenidade militar impecável."
    },
    12039: {
        "pt": "Se bem me recordo, seu nome é Lyner... correto? Nós nos conhecemos no Vilarejo de Karulu.",
        "notes": "Radolf relembra o encontro prévio em Karulu."
    },
    12040: {
        "pt": "Ora, ora... Vocês já se conheciam?",
        "notes": "Jack percebe a conexão mútua."
    },
    12041: {
        "pt": "É, sim... Mas só tínhamos nos visto uma vez no Vilarejo de Karulu.",
        "notes": "Lyner confirma a interação prévia."
    },
    12042: {
        "pt": "Você resgatou a Aurica de um perigo iminente. Minha gratidão é incomensurável.",
        "notes": "Radolf demonstra seu apreço protetor por Aurica."
    },
    12043: {
        "pt": "Se não for pedir demais, vocês poderiam nos fazer uma visita na igreja onde servimos?",
        "notes": "Convite cerimonioso para comparecer à Igreja de Elemia."
    },
    12044: {
        "pt": "Gostaria de recompensá-los devidamente... e também há alguém que faço questão de lhe apresentar, Lyner.",
        "notes": "Correção de erro/invenção da NISA (abduct you); Radolf deseja apresentar o Bispo Falss."
    },
    12045: {
        "pt": "Está certo. Então daremos uma passada lá para uma breve visita.",
        "notes": "Lyner aceita o convite educadamente."
    },
    12046: {
        "pt": "......",
        "notes": "Aurica timidamente observando a conversa."
    },
    12047: {
        "pt": "Você ganhou acesso à [Igreja de Elemia]!",
        "notes": "Desbloqueio de destino no mapa (Elemia Church)."
    },
    12048: {
        "pt": "É possível deslocar-se até a [Igreja de Elemia] através do mapa da cidade.",
        "notes": "Instrução de navegação do mapa."
    },
    12049: {
        "pt": "...Não consigo, eu... não sei o que fazer... O que devo fazer?",
        "notes": "Aurica hesitante no tutorial em batalha."
    },
    12050: {
        "pt": "Hã?! B-Bem, apenas cante uma canção! Algo bem poderoso!",
        "notes": "Lyner comanda com pressa na batalha."
    },
    12051: {
        "pt": "...Qual canção devo cantar?... Por favor, escolha.",
        "notes": "Aurica solicita que Lyner selecione a magia."
    },
    12052: {
        "pt": "Quando o ícone aparecer no canto inferior direito, aperte o botão IM03 para me dar ordens.",
        "notes": "Preservação estrita do botão IM03."
    },
    12053: {
        "pt": "Não... Primeiro você precisa me dar a ordem. Aperte o botão IM03 para abrir os comandos.",
        "notes": "Preservação estrita do botão IM03."
    },
    12054: {
        "pt": "Em seguida, selecione [Cantar Canção] e escolha qual canção você deseja que eu cante.",
        "notes": "Paridade de colchetes com o comando [Sing a Song] / 「詩を謳う」."
    },
    12055: {
        "pt": "...Você ainda não escolheu a canção que devo cantar. Por favor, decida logo.",
        "notes": "Aurica aguarda a seleção de comando."
    },
    12056: {
        "pt": "A Magia Vermelha é uma canção destinada a atacar os inimigos.",
        "notes": "Definição canônica de Magia Vermelha (赤魔法)."
    },
    12057: {
        "pt": "Quanto mais tempo você deixar o poder se concentrar antes de disparar, maior será o efeito gerado.",
        "notes": "Mecânica de carga (Burst) de Song Magic."
    },
    12058: {
        "pt": "Sendo assim, vou começar a cantar.",
        "notes": "Início da conjuração de suporte."
    },
    12059: {
        "pt": "A Magia Azul é uma canção destinada a prestar suporte a todos nós.",
        "notes": "Definição canônica de Magia Azul (青魔法)."
    },
    12060: {
        "pt": "Enquanto eu canto, ela pode restaurar o HP e aprimorar nossos atributos.",
        "notes": "Efeitos benéficos de cura e buffs da Magia Azul."
    },
    12061: {
        "pt": "Sendo assim, vou começar a cantar.",
        "notes": "Início do canto."
    },
    12062: {
        "pt": "A canção... evoluiu?!",
        "notes": "Lyner nota a transformação energética da canção (詩が変化した)."
    },
    12063: {
        "pt": "Pensar que existia um poder desses dentro de mim...",
        "notes": "Aurica descobre seu próprio potencial latente."
    },
    12064: {
        "pt": "Você já está pronta para disparar?",
        "notes": "Lyner indaga sobre a prontidão do Burst."
    },
    12065: {
        "pt": "Sim... Já deve ser possível ativar a qualquer momento!",
        "notes": "Aurica confirma a prontidão mágica."
    },
    12066: {
        "pt": "Quando quiser disparar a Magia da Canção, aperte o botão IM03 e selecione [Ativar Canção].",
        "notes": "Preservação estrita de IM03 e colchetes [Ativar Canção]."
    },
    12067: {
        "pt": "Acho que... estou ficando um pouco cansada...",
        "notes": "Aviso prévio de queda de MP."
    },
    12068: {
        "pt": "Se o meu MP chegar a 0, a canção sofrerá uma erupção descontrolada, então fique de olho no MP restante!",
        "notes": "Conceito de erupção mágica (暴発) por esgotamento de MP."
    },
    12069: {
        "pt": "Eu... acho que estou no meu limite...",
        "notes": "Aurica prestes a esgotar suas forças."
    },
    12070: {
        "pt": "Se o meu MP chegar a 0, a canção sofrerá uma erupção descontrolada, então fique de olho no MP restante!",
        "notes": "Reiteração do aviso de erupção descontrolada de MP."
    },
    12071: {
        "pt": "Eu... não aguento mais...",
        "notes": "Colapso final de MP de Aurica."
    },
    12072: {
        "pt": "Os tópicos de ajuda [Harmonics], [Magia da Canção em Batalha] e [Magia Azul] foram adicionados!",
        "notes": "Paridade de colchetes com os três tutoriais desbloqueados."
    },
    12073: {
        "pt": "Estes tópicos podem ser consultados no menu de Ajuda, acessando [Ajuda: Como Jogar].",
        "notes": "Paridade de colchetes de menu de tutorial."
    },

    # =========================================================================
    # EVENT/590.EVD (IDs 12074 - 12106) - 33 falas
    # Cosmosfera de Misha: Criação de Magia Vermelha e rejeição pelo espírito
    # =========================================================================
    12074: {
        "pt": "Lyner, você sabe o que é essa torre?",
        "notes": "Misha pergunta sobre o pilar de energia na mente."
    },
    12075: {
        "pt": "Uma torre...? Bem, mais do que uma torre... parece um facho de luz...",
        "notes": "Lyner descreve a impressão visual do pilar condutor."
    },
    12076: {
        "pt": "Talvez a gente não descubra se não chegar mais perto. Vamos nos aproximar um pouquinho mais!",
        "notes": "Misha incita Lyner a avançar."
    },
    12077: {
        "pt": "...É mesmo uma torre... Será que dá pra entrar por essa porta?",
        "notes": "Lyner contempla a porta da estrutura condutora."
    },
    12078: {
        "pt": "Não, não dá pra entrar. Essa porta é uma via condutora de energia... um duto de transmissão, então pessoas comuns não conseguem passar.",
        "notes": "Misha explica o conceito técnico da via condutora (伝達口)."
    },
    12079: {
        "pt": "...Uma torre? Via condutora...?",
        "notes": "Lyner intrigado com os termos técnicos."
    },
    12080: {
        "pt": "...Hum, acho que ainda é um pouco cedo pro Lyner entender isso. Mais tarde eu te explico com calma, tá?",
        "notes": "Misha adia o aprofundamento com carinho fraternal."
    },
    12081: {
        "pt": "De qualquer modo, a energia por aqui é fortíssima, então fica bem mais fácil manifestar magias poderosas!",
        "notes": "Alta concentração energética da mente."
    },
    12082: {
        "pt": "Por isso, tecer as magias ofensivas, conhecidas como Magia Vermelha, é perfeito neste lugar!",
        "notes": "Associação de Magia Vermelha a feitiços de ataque."
    },
    12083: {
        "pt": "É mesmo...?",
        "notes": "Lyner compreendendo a mecânica."
    },
    12084: {
        "pt": "Então vou começar a tecer agora mesmo! Vou criar algo inacreditavelmente incrível, então vê se não vai cair de costas de tanto espanto, ouviu?",
        "notes": "Misha empolgada querendo impressionar Lyner."
    },
    12085: {
        "pt": "Lá vou eu...! Haaah!!",
        "notes": "Grito de foco espiritual de Misha."
    },
    12086: {
        "pt": "Uaaau...!!",
        "notes": "Lyner assombrado com a explosão de luz."
    },
    12087: {
        "pt": "Consegui...! Eu realmente teci a magia!",
        "notes": "Misha vibra com a manifestação do feitiço."
    },
    12088: {
        "pt": "...Foi você quem me teceu?",
        "notes": "Espírito draconiano surge questionando sua criadora."
    },
    12089: {
        "pt": "Fui eu mesma! Fui eu quem teceu você!",
        "notes": "Misha responde com orgulho ingênuo."
    },
    12090: {
        "pt": "Mera pirralha... Julga que com uma força de espírito tão medíocre é capaz de me subjugar?!",
        "notes": "Espírito desafia a fraqueza espiritual de Misha."
    },
    12091: {
        "pt": "...Hã?!",
        "notes": "Choque de Misha."
    },
    12092: {
        "pt": "Kyaaa!!",
        "notes": "Misha é arremessada pela onda de choque."
    },
    12093: {
        "pt": "Misha!",
        "notes": "Lyner grita acorrendo à amiga."
    },
    12094: {
        "pt": "Pirralha insolente, coberta num manto de falsidade! Você está dez níveis adiantada para ousar me invocar!",
        "notes": "Repreensão contundente à persona artificial de Misha (10レベル早い)."
    },
    12095: {
        "pt": "N-Não pode ser! Mas foi uma magia que eu mesma teci...!",
        "notes": "Misha inconformada com a rebelião do feitiço."
    },
    12096: {
        "pt": "O poder de tecer e a envergadura de espírito para comandar são grandezas completamente distintas. Jamais prestarei vassalagem a alguém como você, que esconde o próprio mundo e desdobra diante do próximo um reino pintado de mentiras!",
        "notes": "Revelação capital de subtexto: a farsa psicológica criada por Misha em sua mente."
    },
    12097: {
        "pt": "......",
        "notes": "Misha atingida em cheio no seu íntimo."
    },
    12098: {
        "pt": "Lave essa cara e volte quando for gente grande!",
        "notes": "Desdém final do espírito (顔を洗ってまた出直せ)."
    },
    12099: {
        "pt": "......",
        "notes": "Humilhação profunda e silêncio."
    },
    12100: {
        "pt": "Misha! Você está bem...?! Aguenta firme!",
        "notes": "Lyner ampara a amiga ferida em sua autoestima."
    },
    12101: {
        "pt": "Lyner... eu... eu não tenho mais cara pra olhar pra você...!",
        "notes": "Misha desesperada de vergonha diante de Lyner (もうライナーに顔向けできない)."
    },
    12102: {
        "pt": "Misha!!",
        "notes": "Lyner clama por ela enquanto foge em prantos."
    },
    12103: {
        "pt": "...Preciso ir atrás dela depressa!",
        "notes": "Lyner parte imediatamente em seu encalço."
    },
    12104: {
        "pt": "Pra onde a Misha foi?!",
        "notes": "Lyner procura a amiga pela mente."
    },
    12105: {
        "pt": "...Sei lá. Por que você mesmo não procura?",
        "notes": "Moradora do Mundo Inferior com sarcasmo e indiferença."
    },
    12106: {
        "pt": "Que frieza...",
        "notes": "Lyner lamenta a grosseria da guia psíquica."
    },

    # =========================================================================
    # EVENT/543.EVD (IDs 12107 - 12156) - 50 falas
    # Visita noturna de Shurelia a Lyner: Revelações sobre Tastiella e o selo de Mir
    # Duas ramificações: 12107-12131 (Formal) e 12132-12156 (Íntima/Casual)
    # =========================================================================
    # --- Ramificação Formal (12107 - 12131) ---
    12107: {
        "pt": "Lyner. Poderíamos... conversar um pouco?",
        "notes": "Shurelia formal visita o aposento de Lyner à noite."
    },
    12108: {
        "pt": "A-Ah, sim! Fique à vontade, pode entrar!!",
        "notes": "Lyner pego de surpresa pela presença divina."
    },
    12109: {
        "pt": "Perdoe-me por incomodá-lo durante o seu repouso. É que... por algum motivo, senti vontade de ver o seu rosto...",
        "notes": "Confissão meiga e serena de Shurelia."
    },
    12110: {
        "pt": "Ah, mas devo estar sendo um incômodo, não é...? Peço desculpas.",
        "notes": "Hesitação delicada e graciosa."
    },
    12111: {
        "pt": "Não, não, de jeito nenhum! A senhora não está incomodando nada!",
        "notes": "Lyner tranquiliza a Deusa com devoção respeitosa."
    },
    12112: {
        "pt": "A propósito, havia algo que eu gostaria de perguntar à Senhora Shurelia.",
        "notes": "Lyner aproveita a ocasião a sós para sanar uma dúvida de lore."
    },
    12113: {
        "pt": "Sobre a Tastiella... quem ela realmente é? Seria algo como a Mei Mei, uma espécie de inteligência artificial?",
        "notes": "Lyner pergunta se Tastiella é uma IA como Mei Mei."
    },
    12114: {
        "pt": "Ela é... uma \"alma\". A alma da sacerdotisa da Tribo Teru que viveu há 400 anos... a alma de Tastiella.",
        "notes": "Revelação da sacralidade espiritual de Tastiella."
    },
    12115: {
        "pt": "U-Uma alma?!",
        "notes": "Assombro genuíno de Lyner."
    },
    12116: {
        "pt": "Sim. Quando Mir foi selada, ela ofereceu a própria vida em sacrifício por nós.",
        "notes": "Fidelidade canônica ao sacrifício pelo selamento de Mir."
    },
    12117: {
        "pt": "A paz em que vivemos hoje... é um mundo erguido sobre 400 anos de sacrifício contínuo dela.",
        "notes": "Subtexto grave sobre o fardo sacrificial que sustenta Sol Ciel."
    },
    12118: {
        "pt": "Então era isso... Eu não fazia a menor ideia de tudo isso.",
        "notes": "Lyner compreende a dimensão trágica do mundo."
    },
    12119: {
        "pt": "Ela e eu... somos amigas desde tempos imemoriais. Desde a época em que ela vivia como uma jovem comum da Tribo Teru...",
        "notes": "Vínculo afetuoso secular entre a Deusa e a donzela Teru."
    },
    12120: {
        "pt": "E, ao mesmo tempo, ela é a salvadora da minha vida... Por isso, quero fazer tudo o que estiver ao meu alcance por ela.",
        "notes": "Sentimento eterno de dívida e amor fraterno."
    },
    12121: {
        "pt": "É justamente num momento de crise como este... Não, é somente numa hora dessas que posso fazer algo por ela...",
        "notes": "Desabafo de angústia e determinação em retribuir o sacrifício."
    },
    12122: {
        "pt": "......",
        "notes": "Lágrimas silenciosas de Shurelia."
    },
    12123: {
        "pt": "Se-Senhora Shurelia?! O-O que houve?! Eu perguntei alguma besteira sem querer?!",
        "notes": "Lyner em pânico ao ver a Deusa verter lágrimas."
    },
    12124: {
        "pt": "Não, não é isso... É que, sempre que penso nela, as lágrimas simplesmente transbordam...",
        "notes": "Dor comovente de Shurelia."
    },
    12125: {
        "pt": "Se eu tivesse sido mais forte e decidida, ela jamais precisaria ter entregado a própria vida...",
        "notes": "Sentimento dilacerante de culpa de Shurelia."
    },
    12126: {
        "pt": "Ela acabou presa a esse destino só para conseguir me salvar...",
        "notes": "Lamento pelo destino trágico de Tastiella."
    },
    12127: {
        "pt": "Ah!!",
        "notes": "Shurelia percebe que perdeu a compostura divina."
    },
    12128: {
        "pt": "Ah...! P-Perdoe-me. Vir desabafar sobre assuntos tão íntimos aqui... estou misturando o dever com questões pessoais, não é?",
        "notes": "Nuance exata de 公私混同 (misturar dever público com assuntos íntimos)."
    },
    12129: {
        "pt": "Ah, não... na verdade, fiquei muito feliz. Foi a primeira vez que vi a Senhora Shurelia se abrir sobre os seus verdadeiros sentimentos...",
        "notes": "Lyner acolhe a vulnerabilidade da Deusa com calor humano."
    },
    12130: {
        "pt": "......",
        "notes": "Shurelia ruborizada e comovida com as palavras de Lyner."
    },
    12131: {
        "pt": "Sendo assim, peço licença e me retiro por esta noite...",
        "notes": "Despedida cerimoniosa formal de Shurelia."
    },

    # --- Ramificação Íntima/Casual (12132 - 12156) ---
    12132: {
        "pt": "Lyner. Podemos... conversar um pouquinho?",
        "notes": "Variação íntima e doce na voz de Shurelia (少しお話...いい?)."
    },
    12133: {
        "pt": "A-Ah, sim! Fique à vontade, pode entrar!!",
        "notes": "Lyner acolhe prontamente a visita."
    },
    12134: {
        "pt": "Desculpa te atrapalhar enquanto descansa. É que... deu uma vontade boba de ver o seu rosto...",
        "notes": "Registro afetuoso e romântico íntimo (ごめんなさい...見たくなって)."
    },
    12135: {
        "pt": "Ah, mas estou te incomodando, não estou...?",
        "notes": "Insegurança fofa e graciosa."
    },
    12136: {
        "pt": "Não, não, de jeito nenhum! A senhora não está incomodando nada!",
        "notes": "Lyner refuta com prontidão."
    },
    12137: {
        "pt": "A propósito, tem uma coisa que eu queria perguntar à Senhora Shurelia.",
        "notes": "Lyner introduz a dúvida sobre Tastiella."
    },
    12138: {
        "pt": "Sobre a Tastiella... quem ela realmente é? Seria algo como a Mei Mei, uma espécie de inteligência artificial?",
        "notes": "Indagação sobre a verdadeira essência de Tastiella."
    },
    12139: {
        "pt": "Ela é... uma \"alma\". A alma da sacerdotisa da Tribo Teru que viveu há 400 anos... a alma de Tastiella.",
        "notes": "Explicação afetuosa no diapasão íntimo de Shurelia."
    },
    12140: {
        "pt": "U-Uma alma?!",
        "notes": "Espanto de Lyner."
    },
    12141: {
        "pt": "Sim. Quando Mir foi selada, ela ofereceu a própria vida por nós.",
        "notes": "Histórico do sacrifício em tom confidente."
    },
    12142: {
        "pt": "A paz que desfrutamos hoje... é um mundo erguido sobre 400 anos de sacrifício dela.",
        "notes": "Memória dolorosa do fardo de Tastiella."
    },
    12143: {
        "pt": "Então era isso... Eu não fazia a menor ideia de tudo isso.",
        "notes": "Compreensão atenta de Lyner."
    },
    12144: {
        "pt": "Ela e eu... éramos amigas desde tempos imemoriais. Desde quando ela ainda vivia como uma garota comum da Tribo Teru...",
        "notes": "Lembrança terna da juventude de Tastiella."
    },
    12145: {
        "pt": "E também foi a salvadora da minha vida... Por isso, quero fazer tudo o que estiver ao meu alcance por ela.",
        "notes": "Gratidão fraternal profunda."
    },
    12146: {
        "pt": "É justamente num momento de crise como este... Não, é somente numa hora dessas que consigo fazer algo por ela...",
        "notes": "Desejo sincero de redenção."
    },
    12147: {
        "pt": "......",
        "notes": "Shurelia mareja os olhos em silêncio."
    },
    12148: {
        "pt": "Se-Senhora Shurelia?! O-O que houve?! Eu perguntei alguma besteira sem querer?!",
        "notes": "Lyner aflito ao vê-la marejar os olhos."
    },
    12149: {
        "pt": "Não, não é isso... É que, sempre que penso nela, as lágrimas simplesmente transbordam...",
        "notes": "Confissão desarmada da Deusa perante o cavaleiro."
    },
    12150: {
        "pt": "Se eu tivesse sido mais forte e decidida, ela jamais precisaria ter entregado a própria vida...",
        "notes": "Culpa interior expressa abertamente."
    },
    12151: {
        "pt": "Ela acabou presa a esse destino só para conseguir me salvar...",
        "notes": "Tristeza pela amiga que se sacrificou."
    },
    12152: {
        "pt": "Ah!!",
        "notes": "Shurelia se assusta com a própria vulnerabilidade."
    },
    12153: {
        "pt": "Ah...! D-Desculpa. Vir desabafar sobre coisas tão íntimas aqui... estou misturando dever com sentimentos pessoais, né?",
        "notes": "Desculpas informais e carinhosas (公私混同よね)."
    },
    12154: {
        "pt": "Ah, não... na verdade, fiquei muito feliz. Foi a primeira vez que vi a Senhora Shurelia desabafar o que realmente sente...",
        "notes": "Lyner valida a confidência com ternura protetora."
    },
    12155: {
        "pt": "......",
        "notes": "Momento de profunda cumplicidade romântica e espiritual."
    },
    12156: {
        "pt": "Bom, então vou voltar para o meu quarto por hoje...",
        "notes": "Despedida meiga e carinhosa de Shurelia."
    },

    # =========================================================================
    # EVENT/231.EVD (IDs 12157 - 12183) - 27 falas
    # Beco Vagalume: Valentões contra Claire, fúria de Lyner e a lição moral de paz
    # =========================================================================
    12157: {
        "pt": "Se continuar de ladainha, eu acabo com você pra valer, tá ouvindo?!",
        "notes": "Capanga valentão coagindo Claire a desocupar o bar."
    },
    12158: {
        "pt": "É melhor obedecer de bico calado. Esse brutamontes não tá brincando não, viu?",
        "notes": "Comparsa reforça a coação covarde."
    },
    12159: {
        "pt": "Não importa quantas vezes me ameacem, minha resposta é a mesma. Não tenho motivo algum para sair daqui!",
        "notes": "Claire defende sua dignidade com serenidade inabalável."
    },
    12160: {
        "pt": "...Olha a audácia dessa abusada! Mera escória de Reyvateil querendo engrossar a voz?!",
        "notes": "Preconceito e desprezo descarado (レーヴァテイルの分際で)."
    },
    12161: {
        "pt": "...!!",
        "notes": "Claire sob ameaça física direta."
    },
    12162: {
        "pt": "A coisa tá feia!",
        "notes": "Jack prevê a iminência de agressão violenta."
    },
    12163: {
        "pt": "Ei! Vocês aí!!",
        "notes": "Lyner explode em fúria para proteger Claire."
    },
    12164: {
        "pt": "Q-Quem diabos são vocês?!",
        "notes": "Capanga acuado pela chegada repentina dos cavaleiros."
    },
    12165: {
        "pt": "Você é aquele canalha que já estava importunando a Claire antes...!",
        "notes": "Lyner reconhece o agressor reincidente de eventos passados."
    },
    12166: {
        "pt": "Ei, seu energúmeno! Dá cabo desse moleque insolente primeiro!",
        "notes": "デクノボウ -> energúmeno / brutamontes sem cérebro."
    },
    12167: {
        "pt": "Pode deixar!",
        "notes": "Capanga parte para a agressão física."
    },
    12168: {
        "pt": "Seu desgraçado! Tá achando que acabou?!",
        "notes": "Lyner revida com fúria implacável e desproporcional."
    },
    12169: {
        "pt": "Lyner! Chega, pare com isso!!",
        "notes": "Misha intervém aos gritos para conter o massacre."
    },
    12170: {
        "pt": "Hã...?",
        "notes": "Lyner cai em si, atordoado pelo frenesi de combate."
    },
    12171: {
        "pt": "Piedade... me... me poupe...",
        "notes": "Capanga humilhado implorando pela própria vida."
    },
    12172: {
        "pt": "......",
        "notes": "Lyner envergonhado diante do excesso de força."
    },
    12173: {
        "pt": "Lyner, você passou completamente dos limites. Mesmo que envolvesse a defesa de uma Reyvateil...",
        "notes": "Misha adverte com gravidade moral."
    },
    12174: {
        "pt": "Me desculpem. Eu perdi a cabeça de raiva... Mas aqueles covardes também...",
        "notes": "Lyner tenta se justificar pelo calor do momento."
    },
    12175: {
        "pt": "Nem \"mas\" nem meio \"mas\"! Fico grata pela ajuda, mas você passou da conta.",
        "notes": "Expressão idiomática japonesa デモもドッコイも無い -> Nem \"mas\" nem meio \"mas\"!"
    },
    12176: {
        "pt": "E além do mais... você acha mesmo que aquilo foi o certo? Ficou satisfeito com o que fez?",
        "notes": "Claire confronta a consciência moral do jovem herói."
    },
    12177: {
        "pt": "Hã? Satisfeito...?",
        "notes": "Lyner sem palavras diante do questionamento."
    },
    12178: {
        "pt": "Se você subjugar pela força, só gerará mais revolta pela força.",
        "notes": "Ensinamento ético supremo de Claire contra a violência cega."
    },
    12179: {
        "pt": "E essa espiral vai se repetir. Sem parar, uma vez após a outra...",
        "notes": "Visão lúcida do ciclo vicioso da agressão."
    },
    12180: {
        "pt": "......",
        "notes": "Lyner absorve o impacto da sabedoria de Claire."
    },
    12181: {
        "pt": "Perdoe-me... Talvez eu tenha pegado pesado demais com você?",
        "notes": "Claire suaviza o tom com carinho fraternal."
    },
    12182: {
        "pt": "Mas não tem jeito: continuo acreditando que resolver os problemas pela via pacífica é sempre o melhor caminho.",
        "notes": "Afirmação do pacifismo humanista de Claire."
    },
    12183: {
        "pt": "...Gostaria de me ouvir cantar?",
        "notes": "Convite afetuoso para uma canção de consolo."
    },

    # =========================================================================
    # EVENT/592.EVD (IDs 12184 - 12231) - 48 falas
    # Cosmosfera de Misha: Reconciliação, Mudança de Paradigma e expulsão cômica
    # =========================================================================
    12184: {
        "pt": "Misha! Você estava escondida aqui... Fiquei tão preocupado!",
        "notes": "Lyner encontra Misha reclusa na floresta psíquica."
    },
    12185: {
        "pt": "...Lyner... Eu coloquei você em perigo de verdade...",
        "notes": "Culpa sincera de Misha pelo desastre do dragão."
    },
    12186: {
        "pt": "E além do mais... Por ter bancado a sabichona, acabei passando a maior vergonha na sua frente...",
        "notes": "Misha lamenta ter tentado fingir ser forte (見栄張った)."
    },
    12187: {
        "pt": "Não acho que tenha sido vergonhoso... Mas me diz uma coisa: por que aquilo aconteceu?",
        "notes": "Lyner acolhe a fragilidade dela e investiga a causa."
    },
    12188: {
        "pt": "Provavelmente... a força deste meu mundo ainda não tinha capacidade de suportar uma criatura como aquele dragão.",
        "notes": "Misha admite a limitação de seu poder atual."
    },
    12189: {
        "pt": "Entendi... Então, para sustentar uma magia formidável daquelas, você vai precisar fortalecer seu nível mental primeiro.",
        "notes": "Lyner deduz a necessidade de crescimento espiritual."
    },
    12190: {
        "pt": "Hã?! ...Como você sabe disso?!",
        "notes": "Misha espantada com a perspicácia de Lyner."
    },
    12191: {
        "pt": "É que uma criaturinha parecida com um coelho... dizendo ser parte do seu coração, me contou tudo.",
        "notes": "Lyner menciona o conselho da Moradora do Mundo Inferior."
    },
    12192: {
        "pt": "O quêêê?! Tinha uma coisa dessas por aqui?! Ei, o que ela te disse?! Não falou nenhuma besteira sobre mim, falou?! Você não passou a me odiar, passou?!",
        "notes": "Pânico tsundere clássico de Misha temendo rejeição."
    },
    12193: {
        "pt": "De jeito nenhum! Falando nisso... ela me revelou que este mundo que você está me mostrando não é o seu verdadeiro mundo.",
        "notes": "Lyner traz à tona a revelação da farsa do cenário."
    },
    12194: {
        "pt": "...Misha... Você não quer me mostrar quem você é de verdade?",
        "notes": "Pergunta íntima e acolhedora de Lyner."
    },
    12195: {
        "pt": "...Se não quero...? Talvez seja isso. Mas não é porque não gosto de você nem nada do tipo...",
        "notes": "Misha hesitante entre o pudor e a afeição."
    },
    12196: {
        "pt": "Pelo contrário...",
        "notes": "Subtexto de intimidade e amor velado."
    },
    12197: {
        "pt": "Dentro do meu verdadeiro eu... tem tanta coisa que não quero que ninguém veja... meu passado, o que sinto lá no fundo, lembranças vergonhosas...",
        "notes": "Traumas do Clã Lune e do sacrifício como Cantora das Estrelas."
    },
    12198: {
        "pt": "Só que, quanto mais eu me despir por inteiro, mais fundo alcançamos meu subconsciente... e é aí que consigo tecer magias verdadeiramente poderosas das profundezas do coração.",
        "notes": "Mecânica psíquica do Mergulho: vulnerabilidade gera poder mágico."
    },
    12199: {
        "pt": "Acontece que isso significa... mostrar pro Lyner as minhas fraquezas mais vergonhosas... tudo o que há de horrível em mim...",
        "notes": "Medo de desiludir a imagem de heroína aos olhos dele."
    },
    12200: {
        "pt": "...Não precisa ter medo. Não importa o que eu veja, jamais vou te odiar. Seja como você for, você sempre será a minha Misha.",
        "notes": "Afirmação definidora do vínculo imutável de infância."
    },
    12201: {
        "pt": "...É sério mesmo...?",
        "notes": "Misha comovida até as lágrimas."
    },
    12202: {
        "pt": "Com certeza absoluta!",
        "notes": "Garantia incondicional de Lyner."
    },
    12203: {
        "pt": "...Está bem. Mas não vá se assustar com o que vai ver... A crueza da minha verdadeira Cosmosfera não dá nem pra comparar com aquele dragão...",
        "notes": "Aviso sobre a ferocidade de sua dor interna (壮絶さ)."
    },
    12204: {
        "pt": "É-É tão pesado assim...?",
        "notes": "Lyner assustado com a revelação."
    },
    12205: {
        "pt": "...É. Por isso... quando soube que você vinha, cobri tudo com essa camada de tinta bonitinha.",
        "notes": "Metáfora poética da fachada artificial (絵の具で塗りたくった)."
    },
    12206: {
        "pt": "Para que meu mundo real não ficasse visível... Para que o Lyner não visse...",
        "notes": "Tentativa desesperada de proteger a fantasia pueril."
    },
    12207: {
        "pt": "......",
        "notes": "Lyner comovido com a fragilidade de Misha."
    },
    12208: {
        "pt": "Mas eu já me decidi! Vou mostrar ao Lyner quem eu realmente sou!",
        "notes": "Coragem madura de Misha em aceitar a intimidade."
    },
    12209: {
        "pt": "Eu fui tão boba... O Lyner se deu ao trabalho de Mergulhar em mim, e eu aqui escondendo o meu verdadeiro eu.",
        "notes": "Uso canônico do termo Mergulhar (ダイブ)."
    },
    12210: {
        "pt": "Não vou mais fazer isso. Eu quero ficar ao seu lado para sempre, Lyner... então vou me mostrar exatamente como sou.",
        "notes": "Declaração afetuosa de fidelidade eterna."
    },
    12211: {
        "pt": "......",
        "notes": "Silêncio carregado de cumplicidade."
    },
    12212: {
        "pt": "O-O que é aquilo?!",
        "notes": "Erupção de luz sagrada anunciando o rito."
    },
    12213: {
        "pt": "Aquilo ali?! É uma Mudança de Paradigma!",
        "notes": "Termo canônico Mudança de Paradigma (パラダイムシフト)."
    },
    12214: {
        "pt": "Mudança de... Paradigma?! O que é isso, apareceu outro monstro inimigo?!",
        "notes": "Ingenuidade de guerreiro de Lyner."
    },
    12215: {
        "pt": "Idiota!! Aquilo é a prova viva de que o coração da Misha amadureceu!",
        "notes": "Moradora desdenha a lerdeza de Lyner."
    },
    12216: {
        "pt": "Mergulhando no centro daquela luz, o coração da Misha dará um salto e avançará um nível!",
        "notes": "Explicação da transição de nível mental."
    },
    12217: {
        "pt": "Vamos, depressa antes que se apague! Vão logo para Stonehenge!",
        "notes": "Stonehenge como marco da Mudança de Paradigma."
    },
    12218: {
        "pt": "...C-Claro.",
        "notes": "Micro-hesitação de Lyner no tom de voz (...もちろん)."
    },
    12219: {
        "pt": "Espera aí... por que houve essa pausa antes de responder?!",
        "notes": "Misha flagra a insegurança na resposta."
    },
    12220: {
        "pt": "Não teve pausa nenhuma!",
        "notes": "Lyner nega em desespero cômico."
    },
    12221: {
        "pt": "...Eu sabia! Quer dizer que, dependendo do que vir, você pode sim passar a me odiar!",
        "notes": "Gatilho de ciúmes e insegurança tsundere."
    },
    12222: {
        "pt": "Não, quer dizer... provavelmente vai ficar tudo bem, mas...",
        "notes": "O deslize fatal da palavra \"provavelmente\" (多分)."
    },
    12223: {
        "pt": "\"Provavelmente\"?! Eu não quero ouvir \"provavelmente\"! Tinha que ser com certeza absoluta!!",
        "notes": "Misha explode em fúria pelo capricho emocional (絶対じゃなきゃダメなの!)."
    },
    12224: {
        "pt": "Chega! Não vou mostrar mais nada do meu mundo pra você!",
        "notes": "Misha corta a conexão psíquica com Lyner."
    },
    12225: {
        "pt": "Vai embora!!",
        "notes": "Expulsão sumária do Mergulho."
    },
    12226: {
        "pt": "Pronto, tomou um belo chute pra fora.",
        "notes": "Ironia impagável da Moradora do Mundo Inferior."
    },
    12227: {
        "pt": "Ai, que droga... Não acredito nisso...",
        "notes": "Lyner lamentando seu próprio desastre verbal."
    },
    12228: {
        "pt": "Sendo assim, sinto muito, mas vou ter que proceder com a sua expulsão forçada.",
        "notes": "Procedimento canônico de expulsão forçada (強制退去)."
    },
    12229: {
        "pt": "Afinal, a Misha acabou de decretar que não quer mais você aqui dentro.",
        "notes": "Aviso da soberania do desejo da Reyvateil em sua mente."
    },
    12230: {
        "pt": "Uou! E-Espera um pouco!",
        "notes": "Lyner sendo puxado pelo portal de logout."
    },
    12231: {
        "pt": "Ei... droga...",
        "notes": "Desfecho cômico de ejeção da Cosmosfera."
    }
}

# Carregar arquivo de entrada
input_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_051_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

curated_dialogues = []
for d in input_data["dialogues"]:
    d_id = d["id"]
    if d_id not in curated_map:
        raise ValueError(f"Falta ID {d_id} no mapa de curadoria!")
    item = curated_map[d_id]
    curated_text = item["pt"]
    notes = item["notes"]
    
    entry = {
        "id": d_id,
        "event_file": d["event_file"],
        "speaker_id": d["speaker_id"],
        "speaker": d["speaker"],
        "original_jp": d["original_jp"],
        "original_en": d["original_en"],
        "curated_ptbr": curated_text,
        "final_ptbr": curated_text,
        "texto_ptbr_curado": curated_text,
        "custom_text": curated_text,
        "review_status": "approved",
        "reviewed": True,
        "notes": notes,
        "curation_notes": notes
    }
    curated_dialogues.append(entry)

# Novos termos descobertos para o Glossário Mestre
new_terms = {
    "Sacerdotisa Tastiella": {
        "pt": "Sacerdotisa Tastiella",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / Lore Ancestral",
        "note": "Título e função sacerdotal de Tastiella como sacerdotisa da Tribo Teru há 400 anos que entregou sua vida para selar Mir (JP テル族の巫女タスティエーラ)."
    },
    "Expulsão Forçada": {
        "pt": "Expulsão Forçada",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Sistema Psíquico",
        "note": "Mecanismo psíquico de ejeção involuntária do parceiro de Mergulho acionado pela guardiã quando a Reyvateil revoga seu consentimento (JP 強制退去)."
    },
    "Erupção da Canção": {
        "pt": "Erupção da Canção",
        "gender": "feminino",
        "number": "singular",
        "category": "Combate / Magia da Canção",
        "note": "Fenômeno de detonação descontrolada da Magia da Canção decorrente do esgotamento total dos Pontos de Magia (MP = 0) da Reyvateil durante a batalha (JP 詩の暴発)."
    },
    "Duto de Transmissão": {
        "pt": "Duto de Transmissão",
        "gender": "masculino",
        "number": "singular",
        "category": "Tecnologia / Ar tonelico",
        "note": "Vias condutoras e passagens técnicas lacradas da Torre por onde trafegam altíssimas densidades de Energia Sinfônica, inacessíveis a humanos comuns (JP 導力伝達口)."
    }
}

glossary_updates = [
    {
        "term_en": "High Priestess Tastiella",
        "term_jp": "テル族の巫女タスティエーラ",
        "term_ptbr": "Sacerdotisa Tastiella",
        "category": "Personagem / Lore Ancestral"
    },
    {
        "term_en": "Forced Ejection",
        "term_jp": "強制退去",
        "term_ptbr": "Expulsão Forçada",
        "category": "Cosmosfera / Sistema Psíquico"
    },
    {
        "term_en": "Song Eruption",
        "term_jp": "詩の暴発",
        "term_ptbr": "Erupção da Canção",
        "category": "Combate / Magia da Canção"
    },
    {
        "term_en": "Conductor Port",
        "term_jp": "導力伝達口",
        "term_ptbr": "Duto de Transmissão",
        "category": "Tecnologia / Ar tonelico"
    }
]

scene_handoff_final = {
    "resumo_dramatico": "O bloco BLK_EVD_051 consolida cinco arcos narrativos fundamentais de lore, comédia de relacionamentos e evolução psíquica: (1) Em praça pública, o guardião autônomo A.B.R. perde o controle e ataca a população; Lyner intervém e descobre que Aurica é uma Reyvateil Classe D atormentada por sentimentos de inutilidade; com o apoio tático de Harmonics, Magia Vermelha e Magia Azul, Lyner derrota a máquina e ganha o respeito do Comandante Radolf, que o convida para uma visita solene à Igreja de Elemia a fim de apresentá-lo a uma figura eminente do clero (Bispo Falss). (2) No Nível 1 da Cosmosfera de Misha, a jovem tenta impressionar Lyner tecendo uma Magia Vermelha junto a um duto de transmissão da Torre; ao conjurar um colossal espírito draconiano, o monstro a rejeita com fúria por seu baixo nível espiritual e escarnece de sua covardia em esconder o próprio mundo sob uma máscara de mentiras; humilhada e em prantos, Misha foge em desespero. (3) Em seu quarto durante a calada da noite, Lyner recebe a visita secreta da Administradora Shurelia em duas ramificações de intimidade (formal reverente e doce confidente); Shurelia revela que a guardiã Tastiella é na verdade a alma viva da sacerdotisa da Tribo Teru que sacrificou sua vida há 400 anos para selar a terrível Mir, desabafando em lágrimas de culpa por não ter sido forte o suficiente no passado para evitar a tragédia da amiga, enquanto Lyner acolhe sua humanidade. (4) No Beco Vagalume, capangas violentos tentam expulsar Claire de sua taverna com insultos contra as Reyvateils; Lyner intervém e espanca o agressor quase até a morte; Misha e Claire o repreendem com severidade ética, ensinando-lhe que subjugar pela força bruta apenas gera mais ódio e perpetua um ciclo infindável de violência. (5) De volta à mente de Misha, Lyner a encontra reclusa e oferece-lhe aceitação incondicional ('Seja como você for, você sempre será a minha Misha'); comovida, Misha decide revelar sua verdadeira dor, disparando a sagrada Mudança de Paradigma em direção a Stonehenge; contudo, diante de uma micro-hesitação de Lyner, o ciúme tsundere de Misha explode quando ele diz que 'provavelmente' não a odiará, resultando em sua expulsão forçada imediata da Cosmosfera.",
    "decisoes_terminologicas": {
        "A.B.R.": "Guardião mecânico autônomo da Torre de Elemia",
        "Igreja de Elemia": "エル・エレミア教会 / Elemia Church",
        "Sacerdotisa Tastiella": "テル族の巫女タスティエーラ (sacerdotisa ancestral Teru seladora de Mir)",
        "Expulsão Forçada": "強制退去 (ejeção compulsória da mente da Reyvateil)",
        "Erupção da Canção": "詩の暴発 (detonação de magia decorrente de MP zerado)",
        "Duto de Transmissão": "導力伝達口 (conduíte de energia sinfônica da Torre)",
        "Mudança de Paradigma": "パラダイムシフト (salto qualitativo de nível na Cosmosfera)",
        "Stonehenge": "ストーンヘンジ (marco megalítico de evolução na Cosmosfera)"
    },
    "alertas_para_proximo_bloco": "A trama deve avançar para o ingresso solene de Lyner na Igreja de Elemia em Platina para a audiência com o Bispo Falss; na frente da Cosmosfera, o retorno ao mundo interior de Misha exigirá a superação do trauma da rejeição e a travessia do rito em Stonehenge, enquanto na esfera das Reyvateils aprofunda-se o contraste entre a submissão insegura de Aurica e a impetuosidade vulnerável de Misha."
}

highlights = [
    {
        "id": 12020,
        "speaker": "Aurica",
        "original_jp": "...私の力なんて、なんの役にも立たない。",
        "original_en": "But...I’m useless.",
        "curated_ptbr": "...O meu poder não serve para nada...",
        "rationale": "Subtexto comovente da baixa autoestima de Aurica, contrastando sua fragilidade com a coragem que Lyner desperta nela."
    },
    {
        "id": 12044,
        "speaker": "Radolf",
        "original_jp": "礼もしたいし...ライナーに会わせたい方もいるんでね。",
        "original_en": "I’m not trying to abduct you... I want you to meet someone, and to repay you.",
        "curated_ptbr": "Gostaria de recompensá-los devidamente... e também há alguém que faço questão de lhe apresentar, Lyner.",
        "rationale": "Eliminação categórica da censura e invenção espúria da NISA ('abduct you'), restaurando a dignidade cavalheiresca de Radolf e sua menção ao Bispo Falss."
    },
    {
        "id": 12068,
        "speaker": "Aurica",
        "original_jp": "MPが0になると、詩は暴発しちゃうから、残りMPに注意してね。",
        "original_en": "When my MP reaches 0, I lose control of my song. So pay attention to my MP.",
        "curated_ptbr": "Se o meu MP chegar a 0, a canção sofrerá uma erupção descontrolada, então fique de olho no MP restante!",
        "rationale": "Fidelidade ao termo técnico de combate 暴発 (erupção mágica/colapso descontrolado)."
    },
    {
        "id": 12096,
        "speaker": "Personagem [111]",
        "original_jp": "紡ぐ力と従わせる懐は似て非なるモノ。貴様のように、自分の世界を隠し、隣人にも嘘で塗った世界を広げる奴には付き従わぬ。",
        "original_en": "You may have the power to craft, but I won’t take orders from posers like you who are afraid of showing the truth.",
        "curated_ptbr": "O poder de tecer e a envergadura de espírito para comandar são grandezas completamente distintas. Jamais prestarei vassalagem a alguém como você, que esconde o próprio mundo e desdobra diante do próximo um reino pintado de mentiras!",
        "rationale": "Texto capital de McKee sobre a fratura psicológica de Misha: a máscara infantil com que encobre seu trauma de sacrifício."
    },
    {
        "id": 12117,
        "speaker": "Shurelia",
        "original_jp": "今の平和は...400年間の彼女の犠牲の上に成り立つ世界なのです。",
        "original_en": "We owe the last 400 years of peace to her sacrifice.",
        "curated_ptbr": "A paz em que vivemos hoje... é um mundo erguido sobre 400 anos de sacrifício contínuo dela.",
        "rationale": "A solenidade pungente da lore: o preço de sangue e isolamento de Tastiella que sustenta a era de paz de Sol Ciel."
    },
    {
        "id": 12128,
        "speaker": "Shurelia",
        "original_jp": "あ!...す、すみません。こんな所でこんな話するなんて、公私混同ですよね。",
        "original_en": "I’m sorry. I shouldn’t be talking about such private matters right now.",
        "curated_ptbr": "Ah...! P-Perdoe-me. Vir desabafar sobre assuntos tão íntimos aqui... estou misturando o dever com questões pessoais, não é?",
        "rationale": "Resgate da expressão japonesa 公私混同 (confundir o ofício público de Deusa com a dor pessoal de mulher)."
    },
    {
        "id": 12175,
        "speaker": "Claire",
        "original_jp": "デモもドッコイも無いわよ。助けてくれたのは嬉しいけど、ちょっと行き過ぎね。",
        "original_en": "Thank you for saving me, but I agree. You were quite excessive.",
        "curated_ptbr": "Nem \"mas\" nem meio \"mas\"! Fico grata pela ajuda, mas você passou da conta.",
        "rationale": "Equivalência primorosa e natural em PT-BR para o provérbio japonês デモもドッコイも無い (sem desculpas nem meias palavras)."
    },
    {
        "id": 12178,
        "speaker": "Claire",
        "original_jp": "力で制すれば、また力による反抗が起こるだけよ。",
        "original_en": "You can’t force people to do things.",
        "curated_ptbr": "Se você subjugar pela força, só gerará mais revolta pela força.",
        "rationale": "Filosofia ética e dramática profunda sobre a espiral inútil da violência física."
    },
    {
        "id": 12200,
        "speaker": "Lyner",
        "original_jp": "...大丈夫。俺は何を見ても、ミシャを嫌いにはならないよ。どんなミシャでも、ミシャはミシャだから。",
        "original_en": "...Don’t worry. Nothing can change how I feel about you. Whatever I see, I won’t hold it against you.",
        "curated_ptbr": "...Não precisa ter medo. Não importa o que eu veja, jamais vou te odiar. Seja como você for, você sempre será a minha Misha.",
        "rationale": "Declaração fundamental de amor e aceitação incondicional entre Lyner e Misha."
    },
    {
        "id": 12205,
        "speaker": "Misha",
        "original_jp": "...うん。だから...ライナーが来るって言うから、こうして絵の具で塗りたくったの。",
        "original_en": "...Yeah. I heard that you were coming, so I wanted to fix up my Soulspace a little just to cover it up.",
        "curated_ptbr": "...É. Por isso... quando soube que você vinha, cobri tudo com essa camada de tinta bonitinha.",
        "rationale": "Metáfora japonesa original 絵の具で塗りたくった preservada com poesia e ternura."
    },
    {
        "id": 12223,
        "speaker": "Misha",
        "original_jp": "多分!?多分なんて言葉、聞きたくないの。絶対じゃなきゃダメなの!",
        "original_en": "”Pretty sure!?” I need to know for sure!",
        "curated_ptbr": "\"Provavelmente\"?! Eu não quero ouvir \"provavelmente\"! Tinha que ser com certeza absoluta!!",
        "rationale": "Timing cômico e oralidade perfeita da histeria tsundere de Misha exigindo 100% de devoção."
    }
]

output_data = {
    "block_id": "BLK_EVD_051",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(curated_dialogues),
    "id_range": [12010, 12231],
    "dialogues": curated_dialogues,
    "curated_lines": curated_dialogues,
    "new_terms": new_terms,
    "glossary_updates": glossary_updates,
    "scene_handoff_final": scene_handoff_final,
    "highlights": highlights
}

output_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_051_output.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Sucesso! Gerado {output_path.name} com {len(curated_dialogues)} falas lapidadas.")

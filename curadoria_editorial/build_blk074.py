# -*- coding: utf-8 -*-
"""
build_blk074.py - Script de construção e validação da curadoria editorial de BLK_EVD_074
"""
import sys
import json
import re
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Carrega arquivo de entrada
input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_074_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

curated_dict = {}

# =========================================================================
# CENA 1: Event/30.evd (IDs 16767..16811 - 45 falas)
# Encontro com Jack desmaiado de fome na floresta e refeição na loja da coluna
# =========================================================================
curated_dict[16767] = {
    "text": "Ei! Você está bem?",
    "notes": "Lyner encontra um viajante desmaiado na trilha da floresta e corre para socorrê-lo."
}
curated_dict[16768] = {
    "text": "......",
    "notes": "Jack permanece inconsciente e sem forças para articular palavras."
}
curated_dict[16769] = {
    "text": "O que houve?\nAguenta firme!",
    "notes": "Lyner tenta reanimar o estranho caído no chão."
}
curated_dict[16770] = {
    "text": "Ugh...",
    "notes": "Jack solta um gemido fraco de fraqueza e exaustão."
}
curated_dict[16771] = {
    "text": "Ha...",
    "notes": "Jack arfa fracamente sem forças nos lábios."
}
curated_dict[16772] = {
    "text": "Com... fome...",
    "notes": "Jack balbucia com esforço o motivo real do seu colapso físico."
}
curated_dict[16773] = {
    "text": "Hã? Que isso...\nNão me assusta desse jeito...",
    "notes": "Lyner reage atônito e aliviado ao descobrir que o desmaio era pura fome."
}
curated_dict[16774] = {
    "text": "Ugh... c-comida...",
    "notes": "Jack implora por alimento no limite das forças."
}
curated_dict[16775] = {
    "text": "...Não tem jeito.\nVou levar esse cara de volta àquele vilarejo.",
    "notes": "Lyner decide carregar o viajante até o povoado mais próximo para alimentá-lo."
}
curated_dict[16776] = {
    "text": "Se eu for até aquela loja no topo da coluna,\ndevem arranjar alguma coisa pra ele comer...",
    "notes": "Lyner planeja conseguir refeições na mercearia/taverna no topo da coluna."
}
curated_dict[16777] = {
    "text": "Aah, tava uma delícia!\nSinto que voltei dos mortos!",
    "notes": "Jack se empanturra na loja e celebra o retorno das energias com vigor bruto."
}
curated_dict[16778] = {
    "text": "...Incrível...\nEle devorou cinco porções inteiras...",
    "notes": "A atendente da loja fica pasma diante do apetite colossal do estranho."
}
curated_dict[16779] = {
    "text": "Ei, ei... Comer tanto assim de uma vez\nnão vai te fazer mal, não...?",
    "notes": "Lyner adverte com perplexidade sobre os perigos da indigestão após dias de jejum."
}
curated_dict[16780] = {
    "text": "Que nada, relaxa!\nFazia três dias que eu não comia nem bebia nada, sabia?!",
    "notes": "Jack descarta as preocupações com bom humor revelando o jejum forçado de três dias."
}
curated_dict[16781] = {
    "text": "Mas olha, rapaz: você é gente fina de verdade.",
    "notes": "Jack reconhece a generosidade rara do jovem que o salvou."
}
curated_dict[16782] = {
    "text": "Pagar comida pra um sujeito que você\nnunca viu na vida não é pra qualquer um.",
    "notes": "Jack elogia a hospitalidade desinteressada de Lyner."
}
curated_dict[16783] = {
    "text": "VB15SC30Inacreditável!1X",
    "notes": "O velho avô da loja esbraveja incrédulo com o apetite absurdo do cliente."
}
curated_dict[16784] = {
    "text": "Vovô! Ele é um freguês hoje, sabia...?",
    "notes": "A neta repreende o avô rabugento para manter os bons modos com a clientela."
}
curated_dict[16785] = {
    "text": "Bem, mas é verdade que uma pessoa normal\nnão bancaria cinco pratos pra alguém...",
    "notes": "A garota pondera timidamente concordando com a bizarrice da situação."
}
curated_dict[16786] = {
    "text": "Dahahaha! Nisso ela tem toda a razão!",
    "notes": "Jack cai na gargalhada diante do comentário sincero da menina."
}
curated_dict[16787] = {
    "text": "Mas falando sério: no mundo de hoje,\né raro encontrar alguém como você.",
    "notes": "Jack reafirma com respeito a admiração pelo caráter nobre e prestativo de Lyner."
}
curated_dict[16788] = {
    "text": "Eu me chamo Jack. E você?",
    "notes": "Jack estende a mão e se apresenta cordialmente."
}
curated_dict[16789] = {
    "text": "Eu sou o Lyner.",
    "notes": "Lyner retribui a apresentação amigavelmente."
}
curated_dict[16790] = {
    "text": "Mas me diz uma coisa: por que você estava\ndesmaiado no meio do nada?",
    "notes": "Lyner pergunta a razão de Jack estar caído na floresta deserta."
}
curated_dict[16791] = {
    "text": "Fiz uma compra das grandes\ne fiquei liso, sem nenhum tostão.",
    "notes": "Jack explica que torrou todas as economias num item valioso."
}
curated_dict[16792] = {
    "text": "Achei que encontraria algo pra comer na floresta...\nmas apaguei antes de achar qualquer coisa.",
    "notes": "Jack admite que tentou forragear comida na mata mas sucumbiu à fraqueza."
}
curated_dict[16793] = {
    "text": "Bom, graças a isso eu finalmente\nconsegui uma pista...",
    "notes": "Jack começa a mencionar a pista que obteve antes de se dar conta de algo."
}
curated_dict[16794] = {
    "text": "Hã? O que houve?",
    "notes": "Lyner estranha a hesitação súbita do mercenário."
}
curated_dict[16795] = {
    "text": "......",
    "notes": "Jack apalpa os bolsos em pânico silencioso."
}
curated_dict[16796] = {
    "text": "Aaaaah!! A mercadoria na qual gastei\ntodas as minhas economias...",
    "notes": "Jack grita em desespero ao notar que perdeu o item valioso."
}
curated_dict[16797] = {
    "text": "Sumiu! Não tá em lugar nenhum!\nOnde é que eu enfiei aquilo...?!",
    "notes": "Jack vasculha seus pertences em desespero cômico."
}
curated_dict[16798] = {
    "text": "Será que alguém não te roubou,\nou você deixou cair em algum lugar?",
    "notes": "Lyner sugere hipóteses racionais para o sumiço do objeto."
}
curated_dict[16799] = {
    "text": "É... bem capaz...",
    "notes": "Jack admite a possibilidade constrangido."
}
curated_dict[16800] = {
    "text": "Agora que me lembro: quando encontrei você,\ntinha umas feras azuis rondando por perto.",
    "notes": "Lyner recorda das feras que cercavam o corpo inerte de Jack na floresta."
}
curated_dict[16801] = {
    "text": "Só pode ter sido isso!",
    "notes": "Jack deduz que as feras levaram sua mercadoria preciosa."
}
curated_dict[16802] = {
    "text": "Feras azuis...?",
    "notes": "A menina da loja reconhece a menção aos monstros locais."
}
curated_dict[16803] = {
    "text": "Mal aí, Lyner, mas você não me daria uma ajuda?",
    "notes": "Jack pede a companhia de Lyner para voltar ao local do incidente."
}
curated_dict[16804] = {
    "text": "É que eu não me lembro muito bem\nde onde foi que eu caí duro.",
    "notes": "Jack confessa com desconcerto que perdeu o senso de direção."
}
curated_dict[16805] = {
    "text": "Peraí, nada disso! Alto lá!",
    "notes": "A atendente interrompe os dois alarmada com o perigo iminente."
}
curated_dict[16806] = {
    "text": "Uou! Que susto do caramba!!",
    "notes": "Jack salta com o berro repentino da garota."
}
curated_dict[16807] = {
    "text": "Essas feras azuis... Quando cheguei aqui,\no vilarejo inteiro só falava disso!",
    "notes": "A menina relata os boatos que ouviu dos aldeões sobre os monstros."
}
curated_dict[16808] = {
    "text": "Dizem que lâminas e armas de fogo\nquase não surtem efeito nelas!",
    "notes": "A atendente alerta para a imunidade quase total das criaturas a armas comuns."
}
curated_dict[16809] = {
    "text": "Talvez seja uma boa ideia vocês\nconversarem com o pessoal do vilarejo primeiro.",
    "notes": "A garota recomenda investigar mais sobre os pontos fracos das feras antes de partir."
}
curated_dict[16810] = {
    "text": "É mesmo...? Entendido.\nValeu pelo toque!",
    "notes": "Jack agradece o conselho e decide se informar na vila."
}
curated_dict[16811] = {
    "text": "Jack se juntou ao grupo!",
    "notes": "Mensagem do sistema confirmando o ingresso de Jack na equipe."
}

# =========================================================================
# CENA 2: Event/289.evd (IDs 16812..16866 - 55 falas)
# Clímax na Crônica Crescente: confronto com Bourd, sacrifício do canto de Misha e despedida
# =========================================================================
curated_dict[16812] = {
    "text": "E aí? Quanto tempo você acha\nque ainda aguenta ficar aí?",
    "notes": "Bourd zomba da resistência de Tastiella diante da câmara de selamento."
}
curated_dict[16813] = {
    "text": "......\nNão importa o que faça, eu não vou morrer.",
    "notes": "Tastiella declara sua determinação inabalável de resistir aos abusos de Bourd."
}
curated_dict[16814] = {
    "text": "Existem muitas coisas bem piores\ndo que a morte, sabia?\nNão é mesmo, gracinha...?",
    "notes": "Bourd ameaça Tastiella com sadismo e deboche repugnante."
}
curated_dict[16815] = {
    "text": "Bourd!!",
    "notes": "Lyner invade a sala gritando de indignação contra o algoz."
}
curated_dict[16816] = {
    "text": "O quê?! Você de novo, moleque...?",
    "notes": "Bourd reconhece Lyner com desdém e surpresa irritada."
}
curated_dict[16817] = {
    "text": "Não vamos deixar você\nfazer o que bem entende!!",
    "notes": "Misha confronta Bourd com determinação heroica."
}
curated_dict[16818] = {
    "text": "Tsc! Esse corpo...!\nVocê recuperou o seu canto, desgraçada...",
    "notes": "Bourd repara na transformação de Misha em sua forma adulta e no retorno do seu poder Reyvateil."
}
curated_dict[16819] = {
    "text": "Misha! ...Cante, depressa!",
    "notes": "Tastiella clama para que Misha entoe o Canto de Selamento antes que seja tarde."
}
curated_dict[16820] = {
    "text": "Nem pensar!!",
    "notes": "Bourd parte para cima para impedir a conjuração do canto."
}
curated_dict[16821] = {
    "text": "Já é tarde demais!\nMais um pouco e Mir descerá\nsobre o Plugue Sinfônico!",
    "notes": "Bourd revela triunfante a iminência da descida apocalíptica de Mir."
}
curated_dict[16822] = {
    "text": "Até lá, não vou deixar\nninguém cantar aqui dentro!",
    "notes": "Bourd promete sufocar qualquer tentativa de canto com violência."
}
curated_dict[16823] = {
    "text": "Parece que finalmente chegou a hora\ndo nosso acerto de contas, Lyner Barsett!",
    "notes": "Bourd desafia Lyner pelo nome completo para o confronto definitivo."
}
curated_dict[16824] = {
    "text": "Eu não vou parar de atacar nem se você\ncair de joelhos! Está preparado?!",
    "notes": "Bourd ameaça massacrar Lyner sem piedade no calor do duelo."
}
curated_dict[16825] = {
    "text": "Quem precisa se preparar é você!\nPor tudo o que fez contra as Reyvateils,\npor todas as suas conspirações sórdidas...",
    "notes": "Lyner devolve o desafio cobrando justiça pelos crimes e maus-tratos perpetrados por Bourd."
}
curated_dict[16826] = {
    "text": "Eu jamais vou te perdoar!!",
    "notes": "Lyner proclama seu repúdio inegociável à tirania e vilania de Bourd."
}
curated_dict[16827] = {
    "text": "Vem com tudo!!",
    "notes": "Bourd se lança na batalha com agressividade desmedida."
}
curated_dict[16828] = {
    "text": "Bourd... Que determinação assustadora...",
    "notes": "Lyner ofegante contempla o desfecho do combate e a obstinação cega do vilão derrotado."
}
curated_dict[16829] = {
    "text": "Tastiella!\nVocê está bem?!",
    "notes": "Lyner corre para acudir a Guardiã ferida na contenção de Mir."
}
curated_dict[16830] = {
    "text": "Eu estou bem.\nMais importante... a Misha...",
    "notes": "Tastiella ignora suas próprias feridas apontando para o sacrifício de Misha."
}
curated_dict[16831] = {
    "text": "...Sim.",
    "notes": "Misha responde com serenidade resignada e amorosa."
}
curated_dict[16832] = {
    "text": "Lyner... Foi por pouco tempo,\nmas... muito obrigada por tudo.",
    "notes": "Misha agradece a Lyner pelos breves dias de liberdade e companheirismo."
}
curated_dict[16833] = {
    "text": "Aquele breve instante de descanso...\nNunca vou esquecer os momentos felizes\nque passei ao seu lado, Lyner.",
    "notes": "Misha declara que guardará para sempre as lembranças do tempo compartilhado."
}
curated_dict[16834] = {
    "text": "...Misha!",
    "notes": "Lyner clama em desespero vendo a amiga assumir o fardo eterno."
}
curated_dict[16835] = {
    "text": "Agora, vou retornar ao papel de Cantora das Estrelas.\nPara tecer a felicidade de todos neste mundo...",
    "notes": "Misha assume o dever sacerdotal supremo como Cantora das Estrelas em prol da paz mundial."
}
curated_dict[16836] = {
    "text": "Os tremores... cessaram...",
    "notes": "Jack percebe que o colapso sísmico da Torre e do Silvaplate parou."
}
curated_dict[16837] = {
    "text": "O selamento de Mir...\nfoi consumado.",
    "notes": "Krusche constata o êxito do ritual de selamento da Rainha Viral."
}
curated_dict[16838] = {
    "text": "Foi por um triz.\nConseguimos no último segundo.",
    "notes": "Tastiella reconhece o triunfo dramático obtido nos momentos derradeiros."
}
curated_dict[16839] = {
    "text": "Misha...",
    "notes": "Lyner sussurra o nome da amada diante do casulo selado."
}
curated_dict[16840] = {
    "text": "Misha...!\nNão vai nem me responder?",
    "notes": "Lyner chama por ela em choque com o silêncio."
}
curated_dict[16841] = {
    "text": "Ela não pode.\nEstá cantando, então não tem como responder.",
    "notes": "Tastiella explica a natureza contínua do canto que aprisiona a voz de Misha."
}
curated_dict[16842] = {
    "text": "Misha... obrigado.\nMe perdoa... No fim das contas,\neu não pude fazer nada por você.",
    "notes": "Lyner lamenta sua impotência em libertá-la do fardo sacrificial."
}
curated_dict[16843] = {
    "text": "Na verdade, eu também queria...",
    "notes": "Lyner quase confessa seus sentimentos românticos reprimidos."
}
curated_dict[16844] = {
    "text": "......",
    "notes": "Misha permanece imóvel em canto espiritual ininterrupto."
}
curated_dict[16845] = {
    "text": "Eu vou voltar aqui.\nMesmo que não dê para vir todo dia...\neu virei de novo e de novo...",
    "notes": "Lyner promete solenemente visitá-la sem cessar ao longo da vida."
}
curated_dict[16846] = {
    "text": "Você não pode falar,\nmas ainda consegue me ouvir, não é?\nVou te contar tudo sobre o mundo lá fora.",
    "notes": "Lyner planeja mantê-la conectada à realidade trazendo novidades e histórias."
}
curated_dict[16847] = {
    "text": "Por isso... espere por mim com um sorriso,\ntá bom?... Não se esqueça.",
    "notes": "Lyner pede com ternura que ela mantenha a esperança no coração."
}
curated_dict[16848] = {
    "text": "......",
    "notes": "O casulo ressoa com o canto compassivo da Cantora das Estrelas."
}
curated_dict[16849] = {
    "text": "Vamos...\nVocês precisam ir a Platina relatar o sucesso da missão.",
    "notes": "Tastiella orienta os heróis a levarem as boas novas ao Governador de Platina."
}
curated_dict[16850] = {
    "text": "Parece que conseguiram selar Mir novamente sem baixas.",
    "notes": "A sentinela de guarda acolhe a comitiva confirmando o sucesso da operação."
}
curated_dict[16851] = {
    "text": "...Sim.",
    "notes": "Lyner responde cabisbaixo, abatido pela dor da despedida."
}
curated_dict[16852] = {
    "text": "O que foi, Lyner?",
    "notes": "O sentinela percebe a tristeza no semblante do jovem herói."
}
curated_dict[16853] = {
    "text": "Não... Não é nada.",
    "notes": "Lyner disfarça o sofrimento para manter a compostura."
}
curated_dict[16854] = {
    "text": "......",
    "notes": "Jack fita Lyner em silêncio solidário e compassivo."
}
curated_dict[16855] = {
    "text": "Beleza.\nVamos partir pra Platina!",
    "notes": "Jack quebra o clima pesado chamando o grupo para a marcha."
}
curated_dict[16856] = {
    "text": "Lyner! Firmeza aí.\nA Misha ficaria triste se te visse com essa cara.",
    "notes": "Jack encoraja o amigo lembrando que Misha deseja vê-lo forte."
}
curated_dict[16857] = {
    "text": "Pois é. Além disso,\nnão podemos baixar a guarda até vermos como Platina está.",
    "notes": "Krusche adverte prudentemente sobre os perigos remanescentes na cidade flutuante."
}
curated_dict[16858] = {
    "text": "...É verdade.\nEu preciso recompor a postura.",
    "notes": "Lyner se esforça para sacudir a melancolia e cumprir o dever."
}
curated_dict[16859] = {
    "text": "Certo, vamos voltar para Platina!",
    "notes": "Lyner assume a liderança renovada do grupo."
}
curated_dict[16860] = {
    "text": "......",
    "notes": "Krusche contempla a determinação de Lyner com respeito silencioso."
}
curated_dict[16861] = {
    "text": "O acesso à Placa Íon\nfoi liberado no Mapa-Múndi!",
    "notes": "Notificação do sistema desbloqueando o setor intermediário da Torre."
}
curated_dict[16862] = {
    "text": "O acesso a Inferia\nfoi liberado no Mapa-Múndi!",
    "notes": "Notificação do sistema desbloqueando a região do continente inferior."
}
curated_dict[16863] = {
    "text": "O acesso ao Olho Congelado\nfoi liberado no Mapa-Múndi!",
    "notes": "Notificação do sistema desbloqueando a passagem do portão glacial."
}
curated_dict[16864] = {
    "text": "O acesso ao Altar dos Apóstolos\nfoi liberado no Mapa-Múndi!",
    "notes": "Notificação do sistema desbloqueando o santuário superior de Platina."
}
curated_dict[16865] = {
    "text": "O acesso a Platina\nfoi liberado no Mapa-Múndi!",
    "notes": "Notificação do sistema desbloqueando a cidade flutuante de Platina."
}
curated_dict[16866] = {
    "text": "...!!",
    "notes": "Ayatane observa a nova conjuntura em choque silencioso com os desígnios de Mir."
}

# =========================================================================
# CENA 3: Event/102.evd (IDs 16867..16932 - 66 falas)
# Encontro com Krusche na parede externa da Torre, resgate e tutorial de Campo de Ambiência
# =========================================================================
curated_dict[16867] = {
    "text": "...Droga...",
    "notes": "Krusche pragueja ao se ver encurralada pelo monstro na parede da Torre."
}
curated_dict[16868] = {
    "text": "Não dá... Minha consciência tá...",
    "notes": "Krusche fraqueja à beira do desmaio pelo esgotamento físico."
}
curated_dict[16869] = {
    "text": "Aquilo ali é...!",
    "notes": "Lyner avista uma pessoa em perigo iminente na muralha externa."
}
curated_dict[16870] = {
    "text": "É aquela garota de antes!!",
    "notes": "Misha reconhece a jovem mecânica que viram fugindo dos guardas da Tenba."
}
curated_dict[16871] = {
    "text": "Você está bem?!",
    "notes": "Lyner se aproxima gritando preocupado."
}
curated_dict[16872] = {
    "text": "Haa... haa... Quem tá aí?\nPor acaso é... o Luke...?",
    "notes": "Krusche balbucia arfante chamando pelo irmão Luke em seu delírio."
}
curated_dict[16873] = {
    "text": "Quem é você, afinal...?\nO que tá fazendo num lugar desses?!",
    "notes": "Lyner se espanta com a presença de uma garota sozinha no paredão da Torre."
}
curated_dict[16874] = {
    "text": "Lyner!\nDeixa isso pra depois!\nPrimeiro temos que derrotar o inimigo!",
    "notes": "Misha puxa Lyner para a realidade do combate imediato."
}
curated_dict[16875] = {
    "text": "P-perdão!",
    "notes": "Lyner se desculpa desembainhando a arma com pressa."
}
curated_dict[16876] = {
    "text": "Foi por pouco, hein?",
    "notes": "Lyner respira aliviado após repelir o golpe inicial da fera."
}
curated_dict[16877] = {
    "text": "Vocês são... os de mais cedo...",
    "notes": "Krusche recupera os sentidos e identifica seus salvadores."
}
curated_dict[16878] = {
    "text": "Então não era o Luke...\nÉ claro que não seria...",
    "notes": "Krusche lamenta com tristeza a ausência do irmão desaparecido."
}
curated_dict[16879] = {
    "text": "...Luke?",
    "notes": "Lyner repete o nome intrigado com a identidade mencionada."
}
curated_dict[16880] = {
    "text": "...Obrigada.\nTô agradecendo só por educação.",
    "notes": "Krusche expressa gratidão relutante em pose tsundere."
}
curated_dict[16881] = {
    "text": "E-ei, como é que é?!\nÉ essa a consideração com quem acabou\nde salvar a sua pele?!",
    "notes": "Misha se indigna com a falta de tato e calor humano da garota."
}
curated_dict[16882] = {
    "text": "...Eu daria conta de derrotar aquele bicho\nmesmo sem a ajuda de vocês.",
    "notes": "Krusche tenta manter a pose de autossuficiência orgulhosa."
}
curated_dict[16883] = {
    "text": "Além do mais, em nenhum momento\neu pedi pra me salvarem.",
    "notes": "Krusche retruca com petulância juvenil desajeitada."
}
curated_dict[16884] = {
    "text": "...S-sua abusada...!\nComo tem coragem de falar isso depois de quase apagar...?!",
    "notes": "Misha fica boquiaberta com o cinismo da garota recém-resgatada."
}
curated_dict[16885] = {
    "text": "Calma, gente. O que importa é que todo mundo tá bem.\nNuma hora dessas, a gente tem que se ajudar, né?",
    "notes": "Lyner acalma os ânimos com seu pragmatismo conciliador."
}
curated_dict[16886] = {
    "text": "...Urrgh.",
    "notes": "Misha bufa de frustração cruzando os braços."
}
curated_dict[16887] = {
    "text": "Pensando bem, ainda não nos apresentamos.\nEu me chamo Lyner.",
    "notes": "Lyner estende a mão iniciando uma apresentação formal amigável."
}
curated_dict[16888] = {
    "text": "...Krusche.",
    "notes": "Krusche revela seu nome com timidez contida."
}
curated_dict[16889] = {
    "text": "E esta aqui é a Misha.",
    "notes": "Lyner introduz sua parceira Reyvateil."
}
curated_dict[16890] = {
    "text": "Muito prazer!",
    "notes": "Misha se apresenta com cortesia apesar da implicância inicial."
}
curated_dict[16891] = {
    "text": "Mas me diga... quem é você afinal?\nNão parece ser alguém ligado à Tenba...",
    "notes": "Lyner pergunta sobre as origens de Krusche notando o descompasso com os guardas."
}
curated_dict[16892] = {
    "text": "Você também tava fugindo dos guardas agorinha mesmo.\nAprontou alguma coisa, não aprontou?",
    "notes": "Misha indaga desconfiada sobre a perseguição policial recente."
}
curated_dict[16893] = {
    "text": "Que falta de educação!\nEu só dei uma passadinha numa área de acesso restrito, tá legal?",
    "notes": "Krusche minimiza a invasão com cinismo divertido."
}
curated_dict[16894] = {
    "text": "...Só pra recolher umas peças de aeronave...",
    "notes": "Krusche admite baixinho o furto de suprimentos mecânicos."
}
curated_dict[16895] = {
    "text": "Quêêê?!\nIsso não é encrenca séria, não...?",
    "notes": "Lyner arregala os olhos diante da confissão descarada de contravenção."
}
curated_dict[16896] = {
    "text": "Olha quem fala! Vocês também estavam\ncirculando por uma área proibida agorinha mesmo.",
    "notes": "Krusche aponta a incoerência do grupo que também invadiu o setor vedado."
}
curated_dict[16897] = {
    "text": "É... bem, isso é verdade...",
    "notes": "Lyner coça a cabeça sem argumentos defensáveis."
}
curated_dict[16898] = {
    "text": "E o que você veio fazer num lugar desses agora?",
    "notes": "Misha insiste em saber o propósito de Krusche na perigosa muralha externa."
}
curated_dict[16899] = {
    "text": "Os voos de aeronave do Beco Vagalume foram todos suspensos,\nentão tô indo a pé até o Cais Flutuante.",
    "notes": "Krusche explica que o bloqueio das linhas aéreas a obrigou a subir a pé."
}
curated_dict[16900] = {
    "text": "Pela parede externa?!",
    "notes": "Misha se assusta com a temeridade de escalar o abismo vertical da Torre."
}
curated_dict[16901] = {
    "text": "É.",
    "notes": "Krusche confirma com naturalidade imperturbável."
}
curated_dict[16902] = {
    "text": "Tá brincando, né? Com esse corpinho frágil\nquerendo escalar a muralha da Torre?!\nVocê vai acabar morrendo!",
    "notes": "Misha adverte que a compleição física franzina de Krusche é suicida para a escalada."
}
curated_dict[16903] = {
    "text": "...Olha quem fala.\nQualquer um vê que você é bem mais magricela do que eu...",
    "notes": "Krusche desdenha da estatura de Misha gerando disputa cômica de fragilidade."
}
curated_dict[16904] = {
    "text": "O quêêê?! ...Comigo é diferente!\nSe acontecer alguma coisa, o Lyner me protege...",
    "notes": "Misha se gaba da proteção física devotada de Lyner."
}
curated_dict[16905] = {
    "text": "Então eu também vou querer\no Lyner me acompanhando.",
    "notes": "Krusche provoca a rival pedindo a escolta do espadachim."
}
curated_dict[16906] = {
    "text": "Era só o que me faltava...",
    "notes": "Misha resmunga com ciúme evidente diante da audácia da recém-chegada."
}
curated_dict[16907] = {
    "text": "C-calma, meninas, sem briga...\nMas afinal, por que você precisa ir até o Cais Flutuante?",
    "notes": "Lyner aparta o bate-boca investigando o motivo de tanta pressa."
}
curated_dict[16908] = {
    "text": "Porque tem uma coisa lá que eu preciso pegar de qualquer jeito.",
    "notes": "Krusche mantém o mistério sobre o componente vital que busca no cais."
}
curated_dict[16909] = {
    "text": "Você é muito ingênua!\nO céu agora tá infestado de Guardiões\nque atacam qualquer pessoa que encontram!",
    "notes": "Misha avisa sobre a ativação agressiva dos mecanismos de defesa aéreos da Torre."
}
curated_dict[16910] = {
    "text": "Nem dá pra saber se o Cais Flutuante tá seguro!",
    "notes": "Misha enfatiza a incerteza mortal daquela rota."
}
curated_dict[16911] = {
    "text": "Mesmo assim, eu tenho que ir.\nNão posso recuar.",
    "notes": "Krusche reafirma seu compromisso inegociável em prosseguir."
}
curated_dict[16912] = {
    "text": "Parece que o assunto é sério.\nSe quiser, por que não vem com a gente?",
    "notes": "Lyner oferece acolhimento solidário convidando Krusche a se unir à marcha."
}
curated_dict[16913] = {
    "text": "E-espera aí, Lyner?!",
    "notes": "Misha protesta com a espontaneidade com que Lyner recruta desconhecidos."
}
curated_dict[16914] = {
    "text": "A gente tá indo na mesma direção de qualquer forma.\nE três pessoas podem se ajudar muito melhor\nse pintar algum aperto no caminho.",
    "notes": "Lyner expõe o argumento prático da união de forças em território hostil."
}
curated_dict[16915] = {
    "text": "Urgh... Bem, isso é verdade, mas...",
    "notes": "Misha capitula a contragosto diante da lógica irrevogável de Lyner."
}
curated_dict[16916] = {
    "text": "Beleza! Então tá combinado!\nContamos com você, Krusche.",
    "notes": "Lyner sela a aliança com entusiasmo contagiante."
}
curated_dict[16917] = {
    "text": "É. Conto com vocês.",
    "notes": "Krusche aceita a parceria formalizando a amizade."
}
curated_dict[16918] = {
    "text": "Krusche se juntou ao grupo!",
    "notes": "Mensagem do sistema confirmando a entrada de Krusche na equipe."
}
curated_dict[16919] = {
    "text": "Cuidado... Essa criatura se regenera sozinha\ntoda vez que sofre um ataque!",
    "notes": "Krusche alerta em combate sobre a habilidade regenerativa do monstro."
}
curated_dict[16920] = {
    "text": "Com os meus golpes, não importa o quanto eu bata,\nele recupera a vida na hora! Não consigo derrubar!",
    "notes": "Krusche expressa impotência com suas armas mecânicas convencionais."
}
curated_dict[16921] = {
    "text": "O quêêê?! Desse jeito essa luta não vai acabar nunca!",
    "notes": "Lyner se desespera com o ciclo perpétuo de cura do adversário."
}
curated_dict[16922] = {
    "text": "Deixa comigo, Lyner!\nVou liquidar a fatura de uma vez só com a minha Magia da Canção!",
    "notes": "Misha intervém confiante na letalidade do seu ataque mágico único."
}
curated_dict[16923] = {
    "text": "Lyner, expanda o Campo de Ambiência\npra potencializar o poder da minha Magia da Canção!",
    "notes": "Misha comanda o companheiro a coordenar a ressonância harmônica da batalha."
}
curated_dict[16924] = {
    "text": "Campo de Ambiência...?\nO que é isso mesmo?",
    "notes": "Lyner demonstra sua habitual ignorância teórica sobre a mecânica de batalha Reyvateil."
}
curated_dict[16925] = {
    "text": "Ai, não acredito!\nVocê matou todas as aulas mesmo, né?!",
    "notes": "Misha ralha carinhosamente com a negligência acadêmica de Lyner."
}
curated_dict[16926] = {
    "text": "O Campo de Ambiência é o indicador de nível (LV)\nque surge ao desferir ataques contra o inimigo.",
    "notes": "Quadro instrutivo do tutorial explicando a natureza do medidor numérico de Ambiência."
}
curated_dict[16927] = {
    "text": "Esse valor aumenta conforme você ataca;\nquanto maior o nível, mais devastador\nserá o impacto da Magia da Canção.",
    "notes": "Quadro instrutivo do tutorial detalhando o ganho de dano mágico proporcional aos golpes físicos."
}
curated_dict[16928] = {
    "text": "Os combatentes da linha de frente, a começar por Lyner,\ndevem golpear continuamente para elevar esse nível.",
    "notes": "Quadro instrutivo orientando a função tática dos atacantes de vanguarda no combate."
}
curated_dict[16929] = {
    "text": "Q-que estrago impressionante...!",
    "notes": "Lyner se maravilha com a explosão devastadora do canto potencializado."
}
curated_dict[16930] = {
    "text": "Se mais combatentes agirem juntos no fronte,\no campo de ressonância se expande ainda mais.",
    "notes": "Misha explica a ampliação tática do raio do campo pela cooperação de múltiplos aliados."
}
curated_dict[16931] = {
    "text": "Ao expandi-lo até o ponto crítico, a potência supera\naté mesmo o dobro da carga acumulada do canto!",
    "notes": "Misha revela a vantagem extrema de atingir o limiar harmônico de sobrecarga (Harmocrest)."
}
curated_dict[16932] = {
    "text": "Então trate de gravar bem\na utilidade do Campo de Ambiência, viu?",
    "notes": "Misha encerra o tutorial com um lembrete firme e orgulhoso para as próximas pelejas."
}

# =========================================================================
# CENA 4: Event/428.evd (IDs 16933..17016 - 84 falas)
# Epílogo e Despedidas: partida dos aliados, nova vida em Platina e o encontro romântico com Misha
# =========================================================================
curated_dict[16933] = {
    "text": "Pensando bem...\nEu tô um caco de cansado...",
    "notes": "Lyner sente o peso avassalador do desgaste acumulado após a vitória sobre Mir."
}
curated_dict[16934] = {
    "text": "Acho que vou pra casa descansar um pouco...",
    "notes": "Lyner decide se recolher aos aposentos para recarregar as energias."
}
curated_dict[16935] = {
    "text": "Foi mal! Acabei dormindo demais!",
    "notes": "Lyner chega esbaforido ao ponto de encontro no dia seguinte."
}
curated_dict[16936] = {
    "text": "Tá atrasado, seu dorminhoco.",
    "notes": "Misha recebe Lyner com deboche afetuoso de melhor amiga."
}
curated_dict[16937] = {
    "text": "Não tem como evitar. O Lyner se esforçou mais do que todos nós.\nÉ normal que o cansaço venha em dobro, né?",
    "notes": "Aurica acolhe Lyner com doçura e compreensão maternal."
}
curated_dict[16938] = {
    "text": "Peço desculpas por adiantar o assunto sem a sua presença, Lyner...",
    "notes": "Radolf se desculpa cerimoniosamente pela reunião prévia à chegada de Lyner."
}
curated_dict[16939] = {
    "text": "Decidi que vou retornar para Nemo hoje mesmo.",
    "notes": "Radolf comunica sua resolução de regressar à sede da Igreja de Elemia."
}
curated_dict[16940] = {
    "text": "Eu também vou voltar junto com o Comandante Radolf.",
    "notes": "Aurica anuncia que acompanhará seu líder clerical de volta a Nemo."
}
curated_dict[16941] = {
    "text": "Eu também vou me mandar. Foi mal a pressa repentina.",
    "notes": "Jack informa sua partida com o despojamento típico dos mercenários itinerantes."
}
curated_dict[16942] = {
    "text": "Paz é uma maravilha e tal... mas, como posso dizer? Meu sangue não ferve.",
    "notes": "Jack brinca que a calmaria pós-guerra não combina com seu espírito inquieto."
}
curated_dict[16943] = {
    "text": "Eu também tô voltando pro Beco Vagalume.\nDeu pra pegar todas as manhas da engenharia de aeronaves.",
    "notes": "Krusche avisa que retorna à sua oficina após assimilar a tecnologia da Torre."
}
curated_dict[16944] = {
    "text": "Agora quero voltar logo pra casa e construir minha própria aeronave.",
    "notes": "Krusche expressa entusiasmo ardente pelo seu sonho de infância."
}
curated_dict[16945] = {
    "text": "Entendi...",
    "notes": "Lyner assimila as despedidas sentindo o vazio do término da jornada."
}
curated_dict[16946] = {
    "text": "É verdade, né?\nA nossa missão finalmente terminou.",
    "notes": "Lyner aceita que o vínculo formal da missão que os uniu chegou ao fim."
}
curated_dict[16947] = {
    "text": "É assim mesmo que as coisas devem ser.",
    "notes": "Lyner tenta se conformar racionalmente com a dispersão do grupo."
}
curated_dict[16948] = {
    "text": "...Lyner.",
    "notes": "Jack percebe a dor oculta no olhar do amigo e o chama suavemente."
}
curated_dict[16949] = {
    "text": "Não é como se a gente nunca mais fosse se ver.\nNão fica com essa cara desolada.",
    "notes": "Radolf conforta o companheiro com cordialidade fraterna."
}
curated_dict[16950] = {
    "text": "Além do mais, nós fomos companheiros que salvaram o mundo lado a lado.",
    "notes": "Radolf exalta o laço indestrutível forjado na salvação da humanidade."
}
curated_dict[16951] = {
    "text": "Pois é. Não importa onde cada um esteja,\nvamos estar sempre conectados.",
    "notes": "Krusche expressa seu afeto sincero sob sua costumeira pose sarcástica."
}
curated_dict[16952] = {
    "text": "...É verdade.",
    "notes": "Lyner sorri tocado pelo calor das palavras de despedida."
}
curated_dict[16953] = {
    "text": "Vocês prestaram um serviço imensurável a Platina.",
    "notes": "O Governador Leard manifesta sua solene gratidão patriarcal aos combatentes."
}
curated_dict[16954] = {
    "text": "Não há de quê. Nós é que fomos agraciados com grandes ensinamentos nesta jornada.",
    "notes": "Radolf retribui o elogio com nobreza e humildade cavalheiresca."
}
curated_dict[16955] = {
    "text": "Quem sabe um dia eu não retorne aqui na liderança de uma delegação da Igreja?",
    "notes": "Radolf projeta futuras visitas diplomáticas entre a Igreja e Platina."
}
curated_dict[16956] = {
    "text": "Lyner...",
    "notes": "Radolf estende a mão a Lyner com olhar de admiração."
}
curated_dict[16957] = {
    "text": "...Até a próxima.",
    "notes": "Radolf se despede brevemente com honra militar."
}
curated_dict[16958] = {
    "text": "...Lyner. Muito obrigada por ter cuidado de mim de tantas formas.",
    "notes": "Aurica agradece comovida pelo carinho e resgate emocional que recebeu dele."
}
curated_dict[16959] = {
    "text": "Adeus.",
    "notes": "Aurica se despede com ternura e respeito."
}
curated_dict[16960] = {
    "text": "......",
    "notes": "Krusche hesita por um instante antes de sua despedida final."
}
curated_dict[16961] = {
    "text": "...Quem sabe um dia eu não volte pra surrupiar mais tecnologia de vocês.",
    "notes": "Krusche se despede com sua tradicional provocação de ladra de patentes."
}
curated_dict[16962] = {
    "text": "...Até mais.",
    "notes": "Krusche acena partindo com determinação rumo ao seu cais."
}
curated_dict[16963] = {
    "text": "Fique bem, Lyner.",
    "notes": "Jack se aproxima para o aperto de mão final."
}
curated_dict[16964] = {
    "text": "A viagem com você foi cheia de perrengues,\nmas foi a época mais divertida de toda a minha vida.",
    "notes": "Jack confessa com genuíno carinho fraternal o valor inestimável daquela jornada."
}
curated_dict[16965] = {
    "text": "......",
    "notes": "Jack fita o horizonte com nostalgia fugaz."
}
curated_dict[16966] = {
    "text": "Quando eu voltar por aqui, a gente vai sair junto pra paquerar umas gatas, ouviu?!",
    "notes": "Jack despede-se com sua canastrice cômica incorrigível para aliviar a tensão."
}
curated_dict[16967] = {
    "text": "...Bom, então é isso... Lyner.",
    "notes": "Jack sela a despedida com sobriedade."
}
curated_dict[16968] = {
    "text": "Se cuida, garoto.",
    "notes": "Jack vira as costas e parte pela estrada."
}
curated_dict[16969] = {
    "text": "...E lá se foram eles.",
    "notes": "Lyner contempla o salão vazio sentindo o silêncio da partida."
}
curated_dict[16970] = {
    "text": "Pois é...",
    "notes": "Misha murmura contemplativa ao lado dele."
}
curated_dict[16971] = {
    "text": "M-Misha?!\nVocê não ia voltar para Em Pheyna?!",
    "notes": "Lyner toma um susto ao ver que Misha não acompanhou a partida dos outros."
}
curated_dict[16972] = {
    "text": "Sim, eu ia.",
    "notes": "Misha responde com serenidade misteriosa."
}
curated_dict[16973] = {
    "text": "Fui eu quem a acolheu como a nova bibliotecária da Catedral.",
    "notes": "O Governador Leard surpreende o filho anunciando a nomeação oficial de Misha."
}
curated_dict[16974] = {
    "text": "P-pai?!",
    "notes": "Lyner gagueja perplexo com a atitude benevolente e astuta do pai austero."
}
curated_dict[16975] = {
    "text": "Tem alguma objeção a fazer?",
    "notes": "Leard encara Lyner com sua costumeira autoridade irrefutável."
}
curated_dict[16976] = {
    "text": "...N-não, nenhuma... Claro que não...",
    "notes": "Lyner recua desconcertado e secretamente radiante com a notícia."
}
curated_dict[16977] = {
    "text": "Agora que Mir não está mais aqui,\nnão faz sentido eu continuar cantando na Crônica Crescente.",
    "notes": "Misha explica que o dever de contenção eterna que a aprisionava deixou de existir."
}
curated_dict[16978] = {
    "text": "Além disso, a eficácia da minha Magia da Canção diminuiu bastante.",
    "notes": "Misha relata a redução do seu poder cósmico após a cessação do conflito."
}
curated_dict[16979] = {
    "text": "Por isso, resolvi que queria morar em Platina outra vez.",
    "notes": "Misha anuncia sua escolha soberana de viver livre onde seu coração reside."
}
curated_dict[16980] = {
    "text": "É verdade, né?\nAfinal de contas, Platina é a sua terra natal...",
    "notes": "Lyner relembra com carinho a infância compartilhada antes da separação."
}
curated_dict[16981] = {
    "text": "Então vamos ficar juntos daqui pra frente... Conto com você mais uma vez.",
    "notes": "Lyner acolhe a companheira com amor sereno e renovado."
}
curated_dict[16982] = {
    "text": "...Sim. Conto com você!",
    "notes": "Misha sorri radiante selando o novo capítulo de suas vidas."
}
curated_dict[16983] = {
    "text": "E foi assim que a nossa jornada chegou ao fim.",
    "notes": "Lyner narra a conclusão da épica odisseia de salvação de Sol Ciel."
}
curated_dict[16984] = {
    "text": "Uma verdadeira alvorada despontou sobre este mundo.\nUma paz autêntica, sem nada mais a temer...",
    "notes": "Lyner contempla o novo amanhecer luminoso sobre a Torre e os continentes."
}
curated_dict[16985] = {
    "text": "Sim... Uma... verdadeira paz.",
    "notes": "Lyner suspira em serenidade diante da harmonia conquistada."
}
curated_dict[16986] = {
    "text": "E então, alguns meses se passaram...",
    "notes": "Marcador temporal narrativo sinalizando o início do epílogo civil."
}
curated_dict[16987] = {
    "text": "Ah! Lyner?!",
    "notes": "Misha avista Lyner caminhando pelas ruas comerciais de Platina."
}
curated_dict[16988] = {
    "text": "Você tá de folga hoje?",
    "notes": "Misha pergunta animada sobre a escala de serviço dos Cavaleiros."
}
curated_dict[16989] = {
    "text": "Tô, sim. De vez em quando até eu preciso arejar a cabeça, né?",
    "notes": "Lyner confirma o dia livre com sorriso descontraído."
}
curated_dict[16990] = {
    "text": "Eba! Então vamos até a loja de departamentos!",
    "notes": "Misha puxa Lyner animadíssima para uma sessão de compras."
}
curated_dict[16991] = {
    "text": "Hã... De novo...?!",
    "notes": "Lyner lamenta com bom humor a perspectiva de horas carregando sacolas."
}
curated_dict[16992] = {
    "text": "Mas é claro! De novo, sim!",
    "notes": "Misha não aceita desculpas e impõe sua vontade festiva."
}
curated_dict[16993] = {
    "text": "Lyner! Olha só, olha só!\nIsto aqui não é uma gracinha?!",
    "notes": "Misha aponta vitrines encantada com os produtos expostos."
}
curated_dict[16994] = {
    "text": "É, é... Bem legal.",
    "notes": "Lyner concorda com resignação masculina típica."
}
curated_dict[16995] = {
    "text": "Ei, ei, vem cá!\nIsto aqui parece tão gostoso! Vamos provar!",
    "notes": "Misha se empolga com as guloseimas da confeitaria."
}
curated_dict[16996] = {
    "text": "M-mas... a gente acabou de comer agora há pouco...",
    "notes": "Lyner tenta frear a gula da amiga lembrando da refeição recente."
}
curated_dict[16997] = {
    "text": "Doces são uma exceção à parte!",
    "notes": "Misha aplica a clássica regra feminina de que doces vão para outro estômago."
}
curated_dict[16998] = {
    "text": "É... mas o meu estômago não concorda muito com isso, sabia...?",
    "notes": "Lyner resmunga acariciando a barriga cheia."
}
curated_dict[16999] = {
    "text": "Lyner!",
    "notes": "Misha o chama saltitante à frente."
}
curated_dict[17000] = {
    "text": "Anda logo, que lerdeza!",
    "notes": "Misha cobra pressa do rapaz com meiguice mimada."
}
curated_dict[17001] = {
    "text": "Misha, você não cansa nunca, né...?",
    "notes": "Lyner sorri impressionado com o fôlego interminável da parceira."
}
curated_dict[17002] = {
    "text": "Mas é lógico que não!\nEu nunca tive a chance de curtir um encontro de verdade até hoje!",
    "notes": "Misha revela desinibida a natureza romântica do passeio."
}
curated_dict[17003] = {
    "text": "...U-um encontro...?!",
    "notes": "Lyner engasga ruborizado e atordoado com a palavra mágica."
}
curated_dict[17004] = {
    "text": "Eu... passei a vida inteira cantando.\nDesde antes de você ter idade para entender as coisas...",
    "notes": "Misha resgata as lembranças do cárcere sacrificial de onde veio."
}
curated_dict[17005] = {
    "text": "Não saí daquele quarto escuro nem meia dúzia de vezes.",
    "notes": "Misha detalha a reclusão claustrofóbica imposta pelo seu sacerdócio."
}
curated_dict[17006] = {
    "text": "......",
    "notes": "Lyner escuta em silêncio reverente e comovido pela dor do passado dela."
}
curated_dict[17007] = {
    "text": "Mas o Lyner deu a liberdade para aquela menina.",
    "notes": "Misha agradece a salvação de sua vida e de sua alma."
}
curated_dict[17008] = {
    "text": "Você soltou o passarinho que vivia acorrentado na gaiola e o fez voar pelo vasto céu...",
    "notes": "Misha expressa com metáfora poética o renascimento proporcionado por ele."
}
curated_dict[17009] = {
    "text": "Se eu continuasse cantando daquele jeito...\nteria terminado a vida sem jamais saber a alegria de ser uma garota normal.",
    "notes": "Misha celebra a humanidade recuperada e os pequenos prazeres femininos."
}
curated_dict[17010] = {
    "text": "E não foi só isso. O Lyner curou todos os terrores que me assombravam no passado.",
    "notes": "Misha enaltece o apoio emocional com que ele sarou suas feridas mais profundas."
}
curated_dict[17011] = {
    "text": "A pessoa que sou hoje... só existe porque você estava lá por mim.",
    "notes": "Misha declara sua mais pura devoção e amor a Lyner sem artifícios ou rubricas."
}
curated_dict[17012] = {
    "text": "Misha...",
    "notes": "Lyner balbucia o nome dela com os olhos brilhando de ternura."
}
curated_dict[17013] = {
    "text": "Por isso... eu vou recuperar tudo, tudinho o que perdi!",
    "notes": "Misha sacode as lágrimas e declara seu plano audacioso de felicidade."
}
curated_dict[17014] = {
    "text": "Vou viver doze anos inteiros de alegria de uma só vez! E você vai ter que me acompanhar até o fim, ouviu bem, Lyner?",
    "notes": "Misha exige a presença amorosa de Lyner para compensar os anos de sacrifício."
}
curated_dict[17015] = {
    "text": "V-você tá falando sério...?!",
    "notes": "Lyner reage atônito e comovido com a exigência afetuosa da amiga."
}
curated_dict[17016] = {
    "text": "C-o-n-t-o c-o-m v-o-c-ê!",
    "notes": "Misha soletra com alegria triunfante selando a união eterna do casal."
}

# Verificação de cobertura total
assert len(curated_dict) == 250, f"Expected 250 curated entries, got {len(curated_dict)}"
for d in input_data["dialogues"]:
    assert d["id"] in curated_dict, f"Missing ID {d['id']} in curated_dict"

# Teste preliminar de integridade em todas as 250 linhas
hard_gate_errors = 0
lint_warnings = 0
orphan_errors = 0
fracture_errors = 0
cr_errors = 0

for d in input_data["dialogues"]:
    item_id = d["id"]
    orig_jp = d["original_jp"]
    trad = curated_dict[item_id]["text"]

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

    if "\r" in trad:
        print(f"[CR ERROR] ID {item_id}: contains \\r")
        cr_errors += 1

    parts = trad.split("\n")
    for line_part in parts[1:]:
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ORPHAN ERROR] ID {item_id}: line starts with orphan punctuation: {line_part!r}")
            orphan_errors += 1

    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[FRACTURE ERROR] ID {item_id}: syntactic fracture before newline: {match_frac.group(0)!r}")
        fracture_errors += 1

print(f"\n--- TEST REPORT ---")
print(f"Total lines: {len(curated_dict)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")
print(f"Orphan Punctuation Errors: {orphan_errors}")
print(f"Fracture Errors: {fracture_errors}")
print(f"CR Errors: {cr_errors}")

if hard_gate_errors == 0 and lint_warnings == 0 and orphan_errors == 0 and fracture_errors == 0 and cr_errors == 0:
    print("\n[PERFECTION] All 250 lines passed all gates with ZERO errors and ZERO warnings!")
else:
    print("\n[FAIL] Found issues!")
    sys.exit(1)

# Construir os objetos finais para o output JSON
curated_lines_list = []
dialogues_list = []

lines_rewritten = 0
lines_approved_as_is = 0

for d in input_data["dialogues"]:
    item_id = d["id"]
    cur_text = curated_dict[item_id]["text"]
    cur_notes = curated_dict[item_id]["notes"]
    
    if cur_text == d.get("current_ptbr"):
        lines_approved_as_is += 1
    else:
        lines_rewritten += 1

    curated_lines_list.append({
        "id": item_id,
        "text": cur_text,
        "ptbr_curated": cur_text,
        "status": "approved",
        "origin": "curadoria_editorial",
        "notes": cur_notes,
        "rationale": cur_notes
    })

    dialogue_obj = dict(d)
    dialogue_obj["review_status"] = "approved"
    dialogue_obj["text_ptbr"] = cur_text
    dialogue_obj["curated_ptbr"] = cur_text
    dialogue_obj["final_ptbr"] = cur_text
    dialogue_obj["texto_ptbr_curado"] = cur_text
    dialogue_obj["custom_text"] = cur_text
    dialogue_obj["ptbr_curated"] = cur_text
    dialogue_obj["reviewed"] = True
    dialogue_obj["notes"] = cur_notes
    dialogue_obj["curation_notes"] = cur_notes
    dialogue_obj["curadoria_notes"] = cur_notes
    dialogues_list.append(dialogue_obj)

glossary_additions = {
    "Ambience Field": {
        "pt": "Campo de Ambiência",
        "gender": "masculino",
        "number": "singular",
        "category": "Combate / Magia da Canção",
        "note": "Campo sônico de ressonância projetado pela Reyvateil sobre os inimigos antes do desencadeamento da Magia da Canção (JP アンビエンスフィールド). Eleva o dano mágico à medida que os aliados de vanguarda atacam o alvo."
    },
    "Star Singer": {
        "pt": "Cantora das Estrelas",
        "gender": "feminino",
        "number": "singular",
        "category": "Título / Sacerdócio",
        "note": "星詠 (Hoshiyomi). Título cerimonial e sagrado da Reyvateil Origin que governa o Silvaplate e tem o fardo sacrificial supremo de manter o vírus Mir selado na Crônica Crescente entoando canções ininterruptas."
    },
    "Inferia": {
        "pt": "Inferia",
        "gender": "feminino",
        "number": "singular",
        "category": "Toponímia / Região",
        "note": "インフェリア. Região continental do Mundo Inferior sob o Mar da Morte em Sol Ciel; corrige a tradução errônea da NISA ('Inferior')."
    },
    "Frozen Eye": {
        "pt": "Olho Congelado",
        "gender": "masculino",
        "number": "singular",
        "category": "Toponímia / Estrutura da Torre",
        "note": "氷の瞳. Gigantesco portão e conjunto de semicondutores (Elemento Ardel) no centro da Torre Ar tonelico que impede o refluxo de energia sinfônica e divide os Mundos Superior e Inferior."
    },
    "Floating Wharf": {
        "pt": "Cais Flutuante",
        "gender": "masculino",
        "number": "singular",
        "category": "Toponímia / Instalação",
        "note": "滞空岸壁. Grande atracadouro suspenso construído sobre a parede externa da Torre de onde partem naves e dirigíveis."
    }
}

scene_handoff = {
    "last_scene_id": "Event/428.evd",
    "last_line_id": 17016,
    "resumo_dramatico": "O bloco BLK_EVD_074 articula quatro cenas capitais da narrativa e da jornada de Sol Ciel: (1) Em Event/30.evd, nas imediações florestais de um vilarejo, Lyner encontra Jack Hamilton estirado no chão, à beira da morte não por ferimentos, mas por inanição absoluta após torrar todo o dinheiro em compras secretas. Lyner o resgata e o leva à taverna suspensa no topo da coluna, bancando cinco porções inteiras de comida para o mercenário sob os protestos do velho avô e os olhares atônitos da atendente. Após Jack constatar o sumiço de sua preciosa encomenda (furtada por feras azuis imunes a armas comuns), ele convoca Lyner para ajudá-lo na busca, unindo-se oficialmente ao grupo. (2) Em Event/289.evd, na câmara do Plugue Sinfônico da Crônica Crescente, Bourd encurrala Tastiella e tenta apressar o Advento de Mir. Lyner e Misha intervêm; em sua forma adulta desperta, Misha canta para restaurar o selo sagrado enquanto Lyner derrota Bourd em um embate de pura obstinação. Mir é resselada com sucesso, mas o custo emocional é avassalador: Misha deve permanecer em canto ininterrupto no casulo eterno. Lyner jura visitá-la e contar-lhe sobre o mundo lá fora, enquanto o grupo retorna melancólico a Platina com novos setores desbloqueados no Mapa-Múndi (Placa Íon, Inferia, Olho Congelado, Altar dos Apóstolos, Platina) sob o olhar atônito de Ayatane. (3) Em Event/102.evd, na perigosa muralha externa da Torre rumo ao Cais Flutuante, Lyner e Misha socorrem Krusche Elendiek, encurralada por um guardião mecânico regenerativo enquanto buscava por seu irmão desaparecido, Luke. Com atitude tsundere e arrogante, Krusche revela estar a pé por causa da suspensão dos voos no Beco Vagalume após invadir setores restritos da Tenba para furtar peças aeronáuticas. Ela aceita a escolta de Lyner (despertando o ciúme cômico de Misha), junta-se à equipe e o grupo aprende na prática o funcionamento do Campo de Ambiência (アンビエンスフィールド), sincronizando ataques físicos para multiplicar o poder da Magia da Canção até o limiar crítico. (4) Em Event/428.evd, vive-se o grande epílogo e desfecho da saga de Sol Ciel: após a derrota definitiva de Mir e o fim da missão, Radolf e Aurica preparam o retorno a Nemo com a Igreja; Jack parte em busca de aventuras e mulheres; e Krusche retorna à sua oficina no Beco Vagalume para construir sua própria aeronave. Leard surpreende Lyner ao nomear Misha como a nova bibliotecária da Catedral de Platina, dispensando-a do sacerdócio perpétuo e devolvendo-lhe sua cidade natal. Meses depois, em um dia de folga dos Cavaleiros, Misha arrasta Lyner pelas lojas de departamentos de Platina em um 'encontro' romântico e comovente, confessando que após doze anos de reclusão em uma cela escura cantando sem parar, foi ele quem libertou o pássaro da gaiola e curou suas dores — exigindo com carinho que ele permaneça ao seu lado por toda a vida para recuperar cada instante perdido.",
    "decisoes_terminologicas": {
        "Ambience Field": "アンビエンスフィールド (Campo de Ambiência / mecânica harmônica de batalha)",
        "Star Singer": "星詠 (Cantora das Estrelas / título cerimonial de Misha na Crônica Crescente)",
        "Symphonic Plug": "導力プラグ (Plugue Sinfônico / Plugue de Condução energética de contenção de Mir)",
        "Inferia": "インフェリア (Inferia / continente do Mundo Inferior; corrige erro da NISA 'Inferior')",
        "Frozen Eye": "氷の瞳 (Olho Congelado / gigantesco portão semicondutor central da Torre)",
        "Floating Wharf": "滞空岸壁 (Cais Flutuante / atracadouro de aeronaves no paredão externo)",
        "Blue Beasts": "青い獣 (feras azuis / monstros imunes a armas normais que roubaram Jack)",
        "Ion Plate": "イオンプレート (Placa Íon / setor intermediário envolto em nuvens)"
    },
    "alertas_para_proximo_bloco": "Nos blocos posteriores (BLK_EVD_075 em diante), atentar para as consequências da consolidação da paz no Mundo Inferior e Superior, o desenvolvimento dos laços com Misha e Aurica nas rotas de Cosmosphere e eventos adicionais de final de jogo e sidequests de Sol Ciel."
}

output_payload = {
    "block_id": "BLK_EVD_074",
    "axis_id": input_data.get("axis_id", "AXIS_3"),
    "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
    "category": input_data.get("category", "Event Dialogue"),
    "line_count": 250,
    "id_range": [16767, 17016],
    "stats": {
        "total_lines": 250,
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "new_terms_added": len(glossary_additions)
    },
    "curated_lines": curated_lines_list,
    "glossary_additions": glossary_additions,
    "dialogues": dialogues_list,
    "scene_handoff": scene_handoff
}

output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_074_output.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_payload, f, ensure_ascii=False, indent=2)

print(f"\n[SUCCESS] Wrote {len(dialogues_list)} dialogues to {output_path}")
print(f"Stats: Rewritten: {lines_rewritten}, Approved as-is: {lines_approved_as_is}")

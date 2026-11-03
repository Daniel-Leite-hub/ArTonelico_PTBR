# -*- coding: utf-8 -*-
"""Script para gerar BLK_EVD_053_output.json com todas as 190 falas lapidadas."""

import json
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

INPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_053_input.json")
OUTPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_053_output.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

curated_translations = {
    # =========================================================================
    # EVENT/658.EVD (IDs 12458 - 12545) - 88 falas
    # Cosmosfera de Misha (Nível 8/9): A armadilha da ilusão infantil, a
    # desolação de Lyner, a ruptura esquizofrênica e o retorno heroico de Hama.
    # =========================================================================
    12458: (
        "Venha, por aqui... Rápido...",
        "A persona infantil de Misha atrai Lyner para a armadilha na profundeza de sua mente."
    ),
    12459: (
        "Ah... tá...",
        "Lyner atordoado e sonolento respondendo ao chamado."
    ),
    12460: (
        "Tudo bem?\nConsegue me acompanhar?",
        "Falsa solicitude da persona infantil manipuladora."
    ),
    12461: (
        "Tô bem, já disse...",
        "Lyner tenta disfarçar a tontura e o cansaço mental."
    ),
    12462: (
        "Por aqui...",
        "Voz sussurrada guiando Lyner para a escuridão."
    ),
    12463: (
        "Ué? Misha...?!",
        "Lyner percebe que perdeu a figura de vista."
    ),
    12464: (
        "...Por aqui! Rápido...!",
        "Eco distante de Misha chamando."
    ),
    12465: (
        "Por ali, é...?",
        "Lyner tentando se orientar na penumbra."
    ),
    12466: (
        "Misha?!\nEi, Misha!!",
        "Lyner gritando aflito pelo vazio."
    ),
    12467: (
        "...Lyner... Por aqui...",
        "Sussurro ilusório atraindo Lyner para a armadilha."
    ),
    12468: (
        "Espera por mim...!",
        "Lyner correndo no encalço da voz."
    ),
    12469: (
        "Misha?!\n...... Misha?!",
        "Lyner perdido na escuridão chamando em vão."
    ),
    12470: (
        "Que lugar sinistro... Parece que vai sair algum bicho a qualquer...",
        "Lyner pressentindo o perigo iminente antes da emboscada."
    ),
    12471: (
        "Uwaaaah!!",
        "Grito de pavor de Lyner diante da aparição da criatura (correção do errôneo 'Whoa!/Uau!')."
    ),
    12472: (
        "Agyaaaaah!!",
        "Rugido gutural e aterrorizante do monstro mental."
    ),
    12473: (
        "Uou!!\nE-Espera um pouco! Não me avisaram disso!",
        "Lyner recuando em choque diante do ataque surpresa."
    ),
    12474: (
        "Vou... matar você...",
        "Ameaça assassina em fala quebrada da entidade sombria (お前...コロス...)."
    ),
    12475: (
        "Eek!!\nD-De qualquer forma... tenho que fugir...!",
        "Pânico e fuga desesperada de Lyner desarmado na mente."
    ),
    12476: (
        "Haa... haa...\nConsegui... despistar...?\nAcho que não vem mais atrás de mim...",
        "Lyner ofegante recuperando o fôlego após a corrida angustiante."
    ),
    12477: (
        "...Lyner.\nQue alívio... Eu...",
        "Aparição sinistra da cópia alucinatória de Aurica."
    ),
    12478: (
        "Aurica?!\nVocê também se perdeu...?!\nAinda bem! Eu já tava ficando apavorado sozinho aqui.",
        "Alívio ingênuo de Lyner ao ver um rosto amigo no vazio."
    ),
    12479: (
        "...Eu...\ntava com tanta vontade de matar você, Lyner...\nQue bom que a gente se encontrou!",
        "Virada aterrorizante (yandere) da projeção mental de Aurica."
    ),
    12480: (
        "Gyaaaaah!!!\nA-Aurica!! Para!\nPara com isso!!",
        "Grito de horror e dor de Lyner sob o ataque brutal e insano de Aurica."
    ),
    12481: (
        "Lyner...\nOlha só, Lyner... Você tá todo vermelhinho...\nEi... O que você quer que eu faça agora...?",
        "Sadismo perturbador da projeção banhada pelo sangue dele."
    ),
    12482: (
        "Uwaaah!",
        "Lyner arremessado ao chão em agonia (correção do 'Whoa!/Uau!')."
    ),
    12483: (
        "Haa... haa...\n...... Haa... haa...",
        "Respiração ofegante transcrita foneticamente sem rubrica teatral."
    ),
    12484: (
        "Nngh... haa...\nO que diabos... tá acontecendo aqui...?\nQue lugar é esse... E a Misha...?",
        "Desespero e confusão mental de Lyner gravemente ferido."
    ),
    12485: (
        "Minha cabeça... tá ficando turva...\n... Misha... Misha...",
        "Lyner perdendo a consciência sob o trauma psíquico."
    ),
    12486: (
        "...Lyner...",
        "Tom gélido e impiedoso da Misha sombria."
    ),
    12487: (
        "Lyner... Então estava aqui...\nVou eliminar você deste mundo...",
        "Sentença de erradicação existencial proferida pela faceta sombria."
    ),
    12488: (
        "......!!\n... ......gh...! Haa... ah......",
        "Asfixia e terror paralisante transcritos sem rubrica descritiva."
    ),
    12489: (
        "Está tão apavorado que nem consegue gritar...? Que patético...",
        "Crueldade desdenhosa da faceta sombria desmantelando a coragem de Lyner."
    ),
    12490: (
        "Guhaaah!!\n... Aah... aaah...",
        "Gemido de dor excruciante sob tortura mágica interior."
    ),
    12491: (
        "Vamos... caminhe aos poucos rumo ao abismo da morte...\nNão vou te matar de uma vez...",
        "Sadismo calculado prolongando o tormento."
    ),
    12492: (
        "Guhaaah!!",
        "Novo impacto agonizante sofrido por Lyner."
    ),
    12493: (
        "Bem devagar... saboreando cada segundo...\n......",
        "Tortura deliberada desmantelando a psique do herói."
    ),
    12494: (
        "A sua... vi... da... est... á...",
        "Voz se decompondo e falhando em fragmentos espectrais (お前の... いの... の ...が...)."
    ),
    12495: (
        "...yner...\n...Lyner...",
        "Voz real de Misha penetrando o véu da alucinação."
    ),
    12496: (
        "Hã?!",
        "Lyner despertando em solavanco do transe letal."
    ),
    12497: (
        "Você está bem...?",
        "Fingimento carinhoso da persona infantil que planejou a armadilha."
    ),
    12498: (
        "M-Misha...?",
        "Lyner trêmulo e fragilizado reconhecendo a amiga de infância."
    ),
    12499: (
        "Me perdoa... Foi tudo culpa minha por ter me separado de você... Te fiz passar por momentos tão horríveis.",
        "Chantagem emocional sutil da persona manipuladora simulando culpa."
    ),
    12500: (
        "Misha... Eu fiquei com tanto medo...",
        "Vulnerabilidade crua de Lyner buscando abrigo emocional."
    ),
    12501: (
        "Mas agora tá tudo bem...\nEu estou ao seu lado...\nPor isso, não precisa se preocupar com mais nada.",
        "Aconchego sedutor criando codependência doentia."
    ),
    12502: (
        "Que alívio... Misha...\nEu... tava tão apavorado sozinho...",
        "Confissão de desamparo infantilizado sob o trauma recente."
    ),
    12503: (
        "Me perdoa.\nMas agora nós vamos ficar juntos para sempre.",
        "Promessa possessiva selando o isolamento perpétuo."
    ),
    12504: (
        "É verdade?!\nJuntos para sempre...?",
        "Esperança desesperada em busca de segurança absoluta."
    ),
    12505: (
        "Claro que sim.\nNão acredita em mim...?",
        "Inoculação de culpa testando a devoção cega de Lyner."
    ),
    12506: (
        "Não é isso, mas...\nE se a gente se perder de novo...?",
        "Medo paralisante de novo abandono."
    ),
    12507: (
        "...Tem razão...\nEntão, é só a gente garantir que nunca mais possamos nos separar, né...?",
        "O bote da aranha fechando a gaiola mental."
    ),
    12508: (
        "Aqui nós estamos seguros.\nLá fora deste quarto só existe o nada absoluto.\nMesmo que abra a porta, ela não leva a lugar algum.",
        "Descrição arrepiante do isolamento solipsista da mente de Misha."
    ),
    12509: (
        "É sério...? Então, nem você nem eu...",
        "Lyner assimilando a ideia de reclusão mútua e eterna."
    ),
    12510: (
        "Não poderemos dar nem mais um passo para fora deste quarto.",
        "Cláusula de aprisionamento mútuo definitivo."
    ),
    12511: (
        "...Que maravilha! Misha... obrigado!\nAgora vamos ficar juntos para sempre... pra sempre...",
        "O colapso total do senso crítico de Lyner, rendendo-se à ilusão tóxica."
    ),
    12512: (
        "...Com certeza...",
        "Triunfo silencioso da persona infantil obtendo a submissão dele."
    ),
    12513: (
        "A sobrevivência do mundo não importa a mínima, né?\nMesmo que o continente caia ou uma tempestade devaste tudo,\neu sei exatamente como nos salvar...",
        "Niilismo romântico e fuga covarde da responsabilidade cósmica."
    ),
    12514: (
        "Pra mim, contanto que você e eu escapemos juntos,\né só o que importa.\nVocê pensa igual, não pensa, Lyner?",
        "Sedutora cumplicidade egoísta exigindo validação incondicional."
    ),
    12515: (
        "...É...",
        "Concordância hipnótica e dócil de Lyner."
    ),
    12516: (
        "Que bom!\nEu sabia que você diria isso!\nE olha só, eu tive uma ideia...",
        "Entusiasmo infantil revelando o plano macabro de suicídio assistido."
    ),
    12517: (
        "Nós vamos nos trancar para sempre neste quarto. Assim, nem eu nem você jamais vamos acordar... E poderemos ficar nós dois a sós por toda a eternidade.",
        "A consumação do suicídio espiritual e vigília do sono eterno (幽閉 / 一生目を醒まさない)."
    ),
    12518: (
        "...Para sempre... só nós dois...",
        "Repetição em transe antes do rompimento da ilusão."
    ),
    12519: (
        "Kyaah!!",
        "Grito estridente da persona infantil atingida pelo golpe de Misha Real."
    ),
    12520: (
        "Que truque rasteiro...\nPretender erguer um santuário inviolável\ndentro do próprio coração...!",
        "Intervenção da faceta madura de Misha quebrando a ilusão com indignação ética."
    ),
    12521: (
        "Sabe muito bem o que acontece se for erguida uma muralha intransponível na mente de um indivíduo...",
        "Advertência psicológica rigorosa sobre a cisão esquizofrênica da alma."
    ),
    12522: (
        "E para piorar... induzir alucinações, arrastar Lyner à beira do colapso psicológico só para forçá-lo a depender de você... Que baixeza deplorável.",
        "Repúdio implacável à chantagem emocional da persona infantil (卑劣きわまりない)."
    ),
    12523: (
        "Pra começo de conversa, essa distorção só nasceu porque você renegou \"tudo o que sou além do meu destino\"! Isso mesmo...\nSe você desaparecer, o problema tá resolvido!",
        "Revolta genuína da menina reprimida pelo peso do sacrifício da Canção das Crônicas."
    ),
    12524: (
        "Este mundo não parece ter forças para resistir por muito tempo... É hora de acertarmos as contas de uma vez.",
        "Reconhecimento da instabilidade terminal da Cosmosfera exigindo resolução."
    ),
    12525: (
        "Tem razão...\nEgos que se fragmentaram a esse ponto já não conseguem mais voltar a ser um só.",
        "Tragédia da cisão de identidade irreversível sem mediação externa."
    ),
    12526: (
        "E a única saída para isso...",
        "Antecipação do duelo mortal interior."
    ),
    12527: (
        "É que a mente de uma de nós... seja totalmente aniquilada...",
        "O veredito sombrio de vida ou morte entre as duas metades de Misha."
    ),
    12528: (
        "...Misha...\n...Misha... Não me deixa sozinho...\nMisha...",
        "Lyner abandonado no chão, implorando pelo retorno de Misha."
    ),
    12529: (
        "Lyner!\nAcorda! Firmeza nessa postura!!",
        "Hama esbofeteando a fraqueza de Lyner com sua autoridade protetora."
    ),
    12530: (
        "...Hama...?\nÉ você, Hama...? Mas... você disse que não ia mais aparecer...",
        "Lyner surpreso pelo retorno da guardiã que havia se despedido."
    ),
    12531: (
        "...\nVocê tava num estado tão deplorável\nque eu não tive outra escolha!",
        "Tsundere clássica disfarçando seu cuidado e afeto protetor."
    ),
    12532: (
        "Francamente, cair na lábia da Misha com essa facilidade toda... E pensar que um frouxo desses é o meu pai... É o fim da picada...",
        "Hama chama Lyner de pai por ele ter esculpido sua forma original na infância (たまんないわよ)."
    ),
    12533: (
        "...Pai...?",
        "Lyner totalmente perplexo com a revelação filial."
    ),
    12534: (
        "N-Não é nada!!\nEm vez de ficar aí com essa cara de pastel, trate de cair na real de uma vez!",
        "Embaraço e bronca enérgica para sacudir Lyner."
    ),
    12535: (
        "O coração da Misha tá um caos absoluto!\nA identidade dela se partiu completamente ao meio!",
        "Diagnóstico da cisão de identidade que ameaça a vida da Reyvateil."
    ),
    12536: (
        "Nasceram duas personalidades conflitantes dentro da mesma garota!",
        "Polarização irreconciliável entre o dever sagrado e os desejos reprimidos."
    ),
    12537: (
        "Isso não vai se manifestar no mundo real de imediato, mas, se deixar quieto, com o tempo... vai culminar no colapso existencial da própria Misha!",
        "Alerta médico-espiritual sobre o risco de colapso mental irreversível (自己崩壊)."
    ),
    12538: (
        "...O quê...?! A Misha...",
        "Choque e urgência despertando em Lyner."
    ),
    12539: (
        "As duas personas dela estão prestes a duelar na Montanha Geada! Só que, não importa quem vença ou perca, a Misha deixará de ser a Misha!",
        "Padronização terminológica canônica de Montanha Geada (樹氷山 / Juhyōzan) em harmonia com BLK_SYS_011."
    ),
    12540: (
        "Afinal de contas, a Misha só se sustenta como quem é com a coexistência de ambas!\nPor isso, você tem que impedir essa luta!",
        "A tese psicológica central do Dive: a harmonia e integração das contradições humanas."
    ),
    12541: (
        "Hama... Vou agora mesmo...",
        "Lyner assumindo seu dever de parceiro com determinação renovada."
    ),
    12542: (
        "Ai, ai, ai...",
        "Dores físicas do ataque sofrido se manifestando ao se levantar."
    ),
    12543: (
        "Olha... não se esforce além da conta, tá...? Se você morrer... eu...",
        "Revelação involuntária do afeto profundo da Guardiã pelo herói."
    ),
    12544: (
        "...Hã?",
        "Lyner percebendo a hesitação carinhosa de Hama."
    ),
    12545: (
        "N-Não é nada!!",
        "Reação envergonhada e esquiva típica de Hama fechando a cena."
    ),

    # =========================================================================
    # EVENT/778.EVD (IDs 12546 - 12620) - 75 falas
    # Cosmosfera de Aurica (Nível 9): O crossover cômico de Atelier Marie,
    # síntese da Aurica nº 1, quebra da 4ª parede e integração mística final.
    # =========================================================================
    12546: (
        "Bem-vindo de volta!\nEncontrou os itens?",
        "Acolhida alegre de Aurica encarnando Marie (Marlone) em seu ateliê."
    ),
    12547: (
        "Só não achei as [Lágrimas da Professora]...\nOnde é que essa professora fica, afinal?",
        "Busca cômica pelo item lendário de Atelier Marie; uso de colchetes canônicos."
    ),
    12548: (
        "Hãã?! Não tava lá?\nQue estranho... Ela devia estar na Academia, como sempre...",
        "Alusão direta à Academia de Salburg (ザールブルグのアカデミー)."
    ),
    12549: (
        "Marlone! Marlone!",
        "Voz severa da tutora chamando Marie à porta do ateliê."
    ),
    12550: (
        "A-Ai, lascou...!\nNão acredito que veio justo agora!\nAinda nem sintetizei o item da tarefa...!",
        "Pânico clássico de Marie por não ter cumprido a meta acadêmica."
    ),
    12551: (
        "Marlone! Eu sei que você está aí!\nAbra essa porta imediatamente!",
        "Autoridade inflexível da professora Ingrid exigindo a abertura da porta."
    ),
    12552: (
        "Foi mal, Lyner!\nVou fingir que não estou em casa! Atende você!",
        "Aurica aplicando o clássico '居留守' (fingir ausência) e empurrando Lyner para a fogueira."
    ),
    12553: (
        "E-Eu?!",
        "Espanto de Lyner ao ser colocado como escudo humano."
    ),
    12554: (
        "Marlone!\n...Ora...",
        "Ingrid entra furiosa e estranha encontrar um rapaz desconhecido."
    ),
    12555: (
        "Ah... olá... boa tarde...",
        "Cumprimento desajeitado e intimidado de Lyner."
    ),
    12556: (
        "Quem é você?\nAmigo da Marlone?",
        "Olhar desconfiado da professora examinando a visita."
    ),
    12557: (
        "É... bem, mais ou menos isso...",
        "Lyner sem jeito tentando não se comprometer."
    ),
    12558: (
        "E onde aquela menina se meteu, posso saber?",
        "Inquirição impaciente sobre o paradeiro da aluna relapsa."
    ),
    12559: (
        "Ééé... ela saiu para colher materiais... isso, colher materiais...",
        "Gagueira nervosa de Lyner sustentando o álibi improvisado."
    ),
    12560: (
        "Ora, é mesmo...?\nVim conferir se ela estava fazendo a lição de casa direitinho, que pena...",
        "Ironia afiada de Ingrid desconfiando da desculpa."
    ),
    12561: (
        "Com licença... mas a Marlone é...\ntão desastrada assim nos estudos?",
        "Curiosidade ingênua de Lyner sobre a fama acadêmica de Marie."
    ),
    12562: (
        "Se é?! Ela é a pior aluna de toda a história da Academia!\nE logo sob a minha tutela...",
        "O cânone supremo de Atelier Marie preservado com fervor: 'アカデミー史上最悪の落ちこぼれ'."
    ),
    12563: (
        "Só de pensar nisso já me dá enxaqueca! Para piorar, dei um prazo de cinco anos para ela fazer o exame de recuperação, e hoje é o 364º dia do quarto ano!",
        "Paródia exata da mecânica de tempo do primeiro Atelier, com 5 anos de prazo limite."
    ),
    12564: (
        "E o que aquela garota apresentou até agora? Absolutamente nada! Se amanhã ela aparecer de mãos abanando... vai se ver comigo...",
        "Ameaça pedagógica implacável da severa mestra."
    ),
    12565: (
        "(Misericórdia... Q-Que mulher assustadora...)",
        "Lyner apavorado nos pensamentos (ひぃぃぃぃ...。こ、怖い人だ...)."
    ),
    12566: (
        "Pensando bem, você também é digno de pena.\nSer amigo de uma garota tão problemática assim...\nMeus sinceros pêsames...",
        "Piedade condescendente da professora para com o pobre Lyner."
    ),
    12567: (
        "Ai, que horror... até me vieram lágrimas aos olhos...",
        "Lágrimas teatrais de desgosto docente abrindo a brecha cômica perfeita."
    ),
    12568: (
        "Lágrimas coletadas com sucesso!!!",
        "Timing cômico magistral de Lyner capturando as lágrimas como item de alquimia no ar."
    ),
    12569: (
        "Obteve [Lágrimas da Professora]!",
        "Caixa de sistema confirmando a obtenção do ingrediente de síntese."
    ),
    12570: (
        "......",
        "Silêncio perplexo e atônito de Ingrid diante da audácia do garoto."
    ),
    12571: (
        "Aha... haha...",
        "Risada sem graça e nervosa tentando disfarçar o roubo de lágrimas."
    ),
    12572: (
        "...Que palhaçada é essa?\nBom, não importa. Diga à Marlone o seguinte:",
        "Ingrid recompondo a postura severa sem entender nada."
    ),
    12573: (
        "Apresente os resultados amanhã, sem falta.\nE se trouxer alguma porcaria estrambólica...\nela já sabe muito bem o que a espera.",
        "Ultimato solene da mestra antes de se retirar."
    ),
    12574: (
        "...Fuuu...",
        "Suspiro de alívio puro transcrito foneticamente sem asteriscos."
    ),
    12575: (
        "Que professora barra-pesada...",
        "Lyner impressionado com a fúria da educadora."
    ),
    12576: (
        "Nem me fale!\nEla é a megera mais temida de toda a Academia!",
        "Tradução viva e enérgica para 鬼ババ教師 (bruxa/megera da academia)."
    ),
    12577: (
        "Por falar nisso, consegui as [Lágrimas da Professora]!",
        "Lyner exibe com orgulho o ingrediente recém-obtido."
    ),
    12578: (
        "Sério?! Mandou muito bem!\nObrigada! Fez um ótimo trabalho! Você é demais!",
        "Cascata de elogios entusiasmados de Aurica comemorando a vitória."
    ),
    12579: (
        "Incrível! Todos os ingredientes estão reunidos!\nAgora é só sintetizar!",
        "Termo alquímico fundamental '調合' traduzido canonicamente como sintetizar."
    ),
    12580: (
        "Muito bem! Mãos à obra!",
        "Fervor alquímico iniciando o processo de síntese no caldeirão."
    ),
    12581: (
        "Prontinhooo!",
        "Exclamação vitoriosa ao concluir a alquimia."
    ),
    12582: (
        "...O que diabos você inventou aí?",
        "Curiosidade receosa diante da engenhoca fumegante."
    ),
    12583: (
        "Olha só!",
        "Apresentação orgulhosa da invenção bizarra."
    ),
    12584: (
        "Batizada de... Aurica nº 1!",
        "Nome oficial da engenhoca cômica: Aurica nº 1 (オリカ一号)."
    ),
    12585: (
        "Aurica... nº 1...?",
        "Lyner repetindo com evidente ceticismo e medo."
    ),
    12586: (
        "Vou botar pra funcionar agora mesmo!\nAurica nº 1, decolar!!",
        "Grito de ativação empolgado acionando o robô descontrolado."
    ),
    12587: (
        "Uwaaaaah!!",
        "Pânico absoluto sob o estouro do robô desgovernado (correção do 'Wow!/Uau!')."
    ),
    12588: (
        "A-Ai, deu ruim... A professora Ingrid vai nos esfolar vivos...\nPernas pra que te querooo!!",
        "Fuga hilária temendo a punição catastrófica da mestra."
    ),
    12589: (
        "Marlone!!\nQue algazarra é essa?!\nO barulho foi ouvido até lá na Academia!",
        "Fúria de Ingrid irrompendo no laboratório em chamas."
    ),
    12590: (
        "...Ora?\nOnde a Marlone se meteu?!",
        "Espanto ao encontrar o ateliê vazio."
    ),
    12591: (
        "N-Não, é que...\nEla saiu para colher materiais!\nCom licença, fui!!",
        "Lyner fugindo às pressas antes de ser pego pela professora."
    ),
    12592: (
        "E-Espere aí, rapaz!",
        "Tentativa inútil de Ingrid de deter o cúmplice em fuga."
    ),
    12593: (
        "E assim é o jogo \"Atelier Marie: A Alquimista de Salburg\"!\nPessoal, não deixem de comprar e jogar, viu?!",
        "Quebra magistral da quarta parede divulgando o clássico da Gust."
    ),
    12594: (
        "N-Não viaja! Nada a ver!!\nO jogo não tem nada a ver com isso!!",
        "Lyner desmascarando a propaganda enganosa em ritmo cômico perfeito (全然違う!)."
    ),
    12595: (
        "Vamos para Stonehenge!\nPrecisamos escapar deste mundo!",
        "Marco sagrado Stonehenge (ストーンヘンジ) servindo de portal de saída da simulação."
    ),
    12596: (
        "...Ai, minha nossa...",
        "Expressão japonesa de derrota cômica (とほほ / tohoho) adaptada com naturalidade."
    ),
    12597: (
        "Ai, ai... Passei por um aperto dos diabos.",
        "Desabafo exausto de Lyner após o caos do mundo virtual (やれやれ、散々な目にあったな)."
    ),
    12598: (
        "Mas até que foi bem divertido, não foi?",
        "Otimismo travesso de Aurica minimizando o desastre."
    ),
    12599: (
        "Retornou à Cosmosfera de Aurica.",
        "Notificação de transição de retorno ao nível mental padrão."
    ),
    12600: (
        "Sejam muito bem-vindos de volta, jovem mestre e senhorita Aurica.",
        "Cortesia polida do espírito anfitrião acolhendo a dupla de volta."
    ),
    12601: (
        "U-Ué? Ainda estou usando essa roupa!",
        "Surpresa de Aurica ao notar que permanece trajando as vestes de Marie."
    ),
    12602: (
        "Esse traje é um presente meu para a senhorita.\nFaça bom proveito dele.",
        "Concessão graciosa do traje especial como recompensa de conclusão."
    ),
    12603: (
        "Obteve o Figurino \"Marlone\"! Ao equipá-lo, seus atributos de combate serão alterados.",
        "Obtenção de Figurino canônico com bônus de combate; harmonia com menus."
    ),
    12604: (
        "...Voltamos...",
        "Sensação de retorno pleno à sua própria psique."
    ),
    12605: (
        "Mudando de assunto, o que acharam?\nEspero que tenham aproveitado o mundo virtual ao máximo.",
        "Inquirição amável do espírito sobre a experiência imersiva."
    ),
    12606: (
        "Mais do que 'aproveitar', eu nem entendi o que raios aconteceu ali.",
        "Sinceridade cômica de Lyner resumindo o turbilhão surreal."
    ),
    12607: (
        "Isso é o mais importante.\nComo alcançaram todos os meus critérios,\ntambém tenho uma dádiva especial.",
        "Satisfação do guardião atestando a superação do desafio mental."
    ),
    12608: (
        "Rogo que entoe esta humilde entidade\ncomo parte das Canções da senhorita Aurica.",
        "A consagração da essência mística como feitiço de Canção (オリカさんの詩として奏でてください)."
    ),
    12609: (
        "Hã?",
        "Hesitação surpresa de Aurica."
    ),
    12610: (
        "Eu sou a essência que rege o \"mistério\" da senhorita Aurica.\nE agora, nos tornaremos um só.",
        "Revelação psicológica: a reintegração da faceta do mistério à psique da heroína."
    ),
    12611: (
        "Sendo assim, até o dia em que voltarmos a nos encontrar...\nPassar bem...",
        "Despedida nobre e etérea ao se dissolver no coração da cantora."
    ),
    12612: (
        "......",
        "Silêncio sagrado absorvendo a plenitude da integração."
    ),
    12613: (
        "Desapareceu...",
        "Constatação suave de Lyner presenciando a fusão cósmica."
    ),
    12614: (
        "É como se... tudo tivesse chegado ao fim, sabe?",
        "Sensação reconfortante de encerramento da jornada interior na Cosmosfera."
    ),
    12615: (
        "É assim que você sente?",
        "Lyner acolhendo o sentimento de Aurica com ternura e escuta atenta."
    ),
    12616: (
        "Sim. Não sobrou mais nada.\nEu já não tenho mais nada para te mostrar, Lyner.\nNão tenho mais nenhum segredo guardado de você.",
        "Entrega emocional definitiva de Aurica revelando sua alma desnuda ao parceiro."
    ),
    12617: (
        "Não é maravilhoso ter uma relação assim?",
        "Afirmação comovente da cumplicidade e intimidade conquistadas no Nível 9."
    ),
    12618: (
        "Com certeza.",
        "Cumplicidade mútua e selamento de afeto inabalável."
    ),
    12619: (
        "Magia Azul [???] tecida!",
        "Registro formal do feitiço azul protetor tecido no fundo da mente."
    ),
    12620: (
        "Magia Vermelha [Aurica nº 1] tecida!",
        "Registro formal da hilária e explosiva Magia Vermelha 'Aurica nº 1'."
    ),

    # =========================================================================
    # EVENT/369.EVD (IDs 12621 - 12647) - 27 falas
    # O Clímax do Bispo Falss e Consequências em Platina:
    # A morte amarga de Falss, sua maldição sobre o mundo, a lealdade inabalável
    # de Radolf sob falsa acusação e o resgate da honra de Platina.
    # =========================================================================
    12621: (
        "Meros tolos... Homens tolos...",
        "O lamento amargo de Falss sucumbindo aos efeitos do poder proibido."
    ),
    12622: (
        "Em nome... do Trio de Elemia...\nFaça-se... a luz...",
        "Liturgia ancestral distorcida proferida pelo prelado decadente (エレミア三謳神)."
    ),
    12623: (
        "Eis o fim trágico daqueles\nque cobiçaram o poder...",
        "Sentença grave e sóbria de Radolf sobre a ruína da ambição cega (なれの果て)."
    ),
    12624: (
        "Não é momento para divagações!\nLá vem ele...!",
        "Ayatane em prontidão tática alertando para a convulsão violenta do inimigo."
    ),
    12625: (
        "Radolf...\nFilho de Leard...\nEscutem bem.",
        "Falss se dirigindo a Radolf e a Lyner como o sangue do Comandante de Platina."
    ),
    12626: (
        "O poder de Mir é o poder da civilização...",
        "Filosofia de Kyle Clancy / Falss justificando seu pacto tecnológico com a vilã."
    ),
    12627: (
        "Era a última esperança... para frear o lento declínio deste mundo agonizante...",
        "Tese trágica do vilão que via em Mir a única salvação para a escassez de energia de Sol Ciel."
    ),
    12628: (
        "Contudo... essa mesma esperança...\nvocês a estraçalharam...",
        "Acusação furiosa e desesperada culpando os heróis pelo fim da civilização."
    ),
    12629: (
        "Malditos tolos...\nQue pereçam e apodreçam lentamente...\njunto deste mundo decrépito...",
        "Maldição final de Falss antes da aniquilação completa."
    ),
    12630: (
        "Guooooooh!!",
        "Rugido de destruição final de Falss ao evaporar."
    ),
    12631: (
        "Falss!!",
        "Lyner atônito diante da desintegração do bispo conspirador."
    ),
    12632: (
        "Falss...\nEle não estava agindo apenas\npor ganância própria...?",
        "Dúvida moral e choque de Lyner descobrindo que o inimigo tinha convicções próprias."
    ),
    12633: (
        "Quem pode saber...?",
        "Ponderação sóbria de Radolf recusando simplificações morais precipitadas."
    ),
    12634: (
        "Seja como for, é certo que uma catástrofe teria acontecido se o tivéssemos deixado impune.",
        "Pragmatismo marcial: independentemente dos motivos, a ameaça à população era inaceitável."
    ),
    12635: (
        "Mais importante: a situação em Platina está sob controle?",
        "Ayatane redirecionando o foco para a segurança da cidade flutuante no topo da Torre."
    ),
    12636: (
        "......",
        "Hesitação dolorosa de Radolf carregando um fardo vergonhoso."
    ),
    12637: (
        "Peço desculpas,\nLyner, Ayatane...",
        "Humildade de comandante militar pedindo perdão aos jovens subordinados."
    ),
    12638: (
        "O-O que houve?!",
        "Susto de Lyner com o abatimento repentino do líder."
    ),
    12639: (
        "Os cavaleiros da Igreja causaram estragos desmedidos sob o pretexto de uma \"Guerra Santa\".",
        "A confissão da insubordinação fanática dos cavaleiros clericais em Platina."
    ),
    12640: (
        "O-O quê?!",
        "Indignação explosiva diante da profanação e violência contra civis."
    ),
    12641: (
        "A Senhora Shurelia, os Cavaleiros de Elemia\ne eu interviemos e conseguimos conter a revolta, mas...",
        "O relato da coalizão pacificadora liderada pela deusa da Torre e pelos Cavaleiros de Elemia."
    ),
    12642: (
        "A cidade sofreu estragos terríveis. Sinto muitíssimo...",
        "Dor moral de Radolf pelos danos infligidos à capital sagrada."
    ),
    12643: (
        "Não é culpa sua, Radolf!\nNão precisa ficar tão cerimonioso comigo.",
        "Calor fraternal de Lyner aliviando a culpa do amigo e superior (そんな、かしこまらないでくれよ)."
    ),
    12644: (
        "Contudo...!",
        "O senso de dever de Radolf resistindo à absolvição fácil."
    ),
    12645: (
        "Mesmo tendo sido falsamente acusado de traição, ainda mantém sua lealdade à Igreja? É impressionante.",
        "Ayatane admirando a integridade inquebrantável de Radolf, incapaz de abandonar sua honra mesmo caluniado (謀反の濡れ衣)."
    ),
    12646: (
        "Sob qualquer circunstância,\naquele que comanda uma instituição deve assumir a responsabilidade.",
        "Filosofia de liderança ética inabalável: o dever da liderança (組織の上に立つ者は責任を取らねばならない)."
    ),
    12647: (
        "De qualquer forma, preciso ver a situação.\nVamos voltar à cidade.",
        "Decisão heroica imediata de retornar a Platina para socorrer o povo."
    ),
}

print(f"Total mapped: {len(curated_translations)} / 190 lines.")
assert len(curated_translations) == 190, f"Expected 190, got {len(curated_translations)}"

# Validar Hard Gate e Lint em cada fala
hard_gate_errors = 0
lint_warnings = 0

dialogues_out = []
curated_lines_out = []

for item in input_data["dialogues"]:
    d_id = item["id"]
    if d_id not in curated_translations:
        raise ValueError(f"Falta tradução para ID {d_id}")
    
    text, note = curated_translations[d_id]
    orig_jp = item["original_jp"]

    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=text,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {d_id}: {e}")

    avisos = validador_editorial.auditar_estilo_editorial(text)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {d_id}: {a}")

    entry = {
        "id": d_id,
        "event_file": item.get("event_file", ""),
        "speaker_id": item.get("speaker_id", 0),
        "speaker": item.get("speaker", ""),
        "original_jp": item.get("original_jp", ""),
        "original_en": item.get("original_en", ""),
        "curated_ptbr": text,
        "final_ptbr": text,
        "texto_ptbr_curado": text,
        "custom_text": text,
        "review_status": "approved",
        "reviewed": True,
        "notes": note,
        "curation_notes": note
    }
    dialogues_out.append(entry)
    curated_lines_out.append(entry)

print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors > 0:
    print("ERRO: O processo foi interrompido devido a violações de Hard Gate!")
    sys.exit(1)

new_terms = {
    "Teacher's Tears": {
        "pt": "Lágrimas da Professora",
        "gender": "feminino",
        "number": "plural",
        "category": "Item / Cosmosphere",
        "note": "先生の涙. Ingrediente lendário de alquimia coletado das lágrimas de desespero docente da professora Ingrid no crossover de Atelier Marie na Cosmosfera de Aurica (ID 12569)."
    },
    "Aurica No. 1": {
        "pt": "Aurica nº 1",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia Vermelha / Cosmosphere",
        "note": "オリカ一号. Engenhoca alquímica cômica e explosiva sintetizada por Aurica personificada como Marie, convertida em feitiço de combate de Magia Vermelha (ID 12584, 12620)."
    },
    "Frost Mountain": {
        "pt": "Montanha Geada",
        "gender": "feminino",
        "number": "singular",
        "category": "Localização / Cosmosphere",
        "note": "樹氷山 (Juhyōzan). Montanha glacial na Cosmosfera de Misha onde ocorre o duelo interior decisivo entre a faceta madura/guardiã e a persona infantil deprimida (ID 12539; padronizado com BLK_SYS_011 ID 23234)."
    },
    "Holy War": {
        "pt": "Guerra Santa",
        "gender": "feminino",
        "number": "singular",
        "category": "Lore / Religião",
        "note": "聖戦 (seisen). Pretexto fanático bradado pelos cavaleiros rebeldes e corrompidos da Igreja de Elemia para saquear e espalhar terror pelas ruas de Platina (ID 12639)."
    },
    "Atelier Marie: Alchemist of Salburg": {
        "pt": "Atelier Marie: A Alquimista de Salburg",
        "gender": "masculino",
        "number": "singular",
        "category": "Crossover / Meta",
        "note": "マリーのアトリエ・ザールブルグの錬金術士. Primeiro título clássico da franquia Atelier desenvolvido pela Gust em 1997, parodiado e divulgado com quebra de quarta parede por Aurica na Cosmosfera (ID 12593)."
    }
}

glossary_updates = [
    {
        "term_en": "Teacher's Tears",
        "term_jp": "先生の涙",
        "term_ptbr": "Lágrimas da Professora",
        "category": "Item / Cosmosphere",
        "rationale": "Ingrediente cômico obtido de Ingrid na paródia de Atelier Marie (ID 12569)."
    },
    {
        "term_en": "Aurica No. 1",
        "term_jp": "オリカ一号",
        "term_ptbr": "Aurica nº 1",
        "category": "Magia Vermelha / Cosmosphere",
        "rationale": "Nome oficial da criação mecânica de Aurica e feitiço de Magia Vermelha (ID 12584, 12620)."
    },
    {
        "term_en": "Frost Mountain",
        "term_jp": "樹氷山",
        "term_ptbr": "Montanha Geada",
        "category": "Localização / Cosmosphere",
        "rationale": "Padronização canônica com BLK_SYS_011 para o palco do duelo interior de Misha (ID 12539)."
    },
    {
        "term_en": "Holy War",
        "term_jp": "聖戦",
        "term_ptbr": "Guerra Santa",
        "category": "Lore / Religião",
        "rationale": "Pretexto eclesiástico fanático empregado no motim contra Platina (ID 12639)."
    },
    {
        "term_en": "Atelier Marie: Alchemist of Salburg",
        "term_jp": "マリーのアトリエ・ザールブルグの錬金術士",
        "term_ptbr": "Atelier Marie: A Alquimista de Salburg",
        "category": "Crossover / Meta",
        "rationale": "Título do jogo clássico citado diretamente na quebra da 4ª parede (ID 12593)."
    }
]

scene_handoff_final = {
    "resumo_dramatico": "O bloco BLK_EVD_053 consolida três momentos capitais de alta densidade psicológica, comédia metalinguística e drama ético-militar: (1) Na profundeza da Cosmosfera de Misha (Event/658.evd), Lyner é arrastado por um pesadelo sufocante onde cópias distorcidas de Aurica e Misha tentam executá-lo em meio a torturas mentais; a persona infantil e deprimida de Misha tenta seduzi-lo a um pacto suicida para trancarem-se juntos para sempre em um quarto suspenso no nada até morrerem dormindo; a faceta madura de Misha invade o local e denuncia a baixeza da chantagem psicológica; perante a impossibilidade de coexistência pacífica, as duas metades partem para a Montanha Geada para um duelo de aniquilação mútua; Hama, a Guardiã da Mente, resgata Lyner à beira do desespero e o conclama a impedir o duelo fraticida que destruiria a existência da garota. (2) Na Cosmosfera de Aurica (Event/778.evd), vive-se a paródia antológica de Atelier Marie: Aurica encarna Marie às vésperas do fim do prazo de 5 anos da Academia de Salburg; a temida professora Ingrid invade o ateliê aos berros e Lyner consegue coletar o item de síntese 'Lágrimas da Professora' diretamente do pranto de desgosto da mestra; Aurica sintetiza a caótica 'Aurica nº 1' e faz propaganda do jogo em quebra hilária da 4ª parede; de volta à Cosmosfera, o espírito do mistério se reintegra à alma de Aurica, permitindo que a heroína atinja a transparência emocional absoluta e teça suas magias finais com Lyner. (3) No rescaldo do confronto contra o Bispo Falss (Event/369.evd), o prelado conspirador desaba perante Radolf, Ayatane e Lyner, amaldiçoando-os por terem destruído a última esperança de deter o declínio do mundo através do poder civilizatório de Mir; após a morte do bispo, Radolf pede perdão a Lyner e Ayatane pela devassidão provocada pelos cavaleiros rebeldes da Igreja em Platina sob o estandarte de uma 'Guerra Santa', enquanto Ayatane contempla com respeito assombroso a integridade inabalável do comandante militar que se recusa a abandonar seu senso de responsabilidade mesmo tendo sido caluniado como traidor.",
    "decisoes_terminologicas": {
        "Montanha Geada": "樹氷山 (palco do confronto entre as facetas de Misha, padronizado com BLK_SYS_011)",
        "Lágrimas da Professora": "先生の涙 (item de síntese colhido do pranto de Ingrid)",
        "Aurica nº 1": "オリカ一号 (engenhoca alquímica e Magia Vermelha tecida no Nível 9)",
        "Figurino \"Marlone\"": "コスチューム「マルローネ」 (traje de Marie adquirido após a simulação)",
        "Guerra Santa": "聖戦 (falso estandarte religioso usado na pilhagem de Platina)",
        "Atelier Marie: A Alquimista de Salburg": "マリーのアトリエ・ザールブルグの錬金術士 (metalinguagem e 4ª parede)",
        "Falsa acusação de traição": "謀反の濡れ衣 (calúnia política imposta a Radolf)"
    },
    "alertas_para_proximo_bloco": "A narrativa avança para a chegada dos heróis a Platina devastada pelo motim religioso da Igreja e a preparação solene para o avanço em direção ao clímax cósmico, exigindo coerência sobre a dor moral de Radolf e o amadurecimento heroico de Lyner."
}

highlights = [
    {
        "id": 12471,
        "scene": "Terror e Pesadelo na Cosmosfera de Misha",
        "original_jp": "うわぁぁ!!",
        "original_en": "Whoa!",
        "curated_ptbr": "Uwaaaah!!",
        "rationale": "Correção de alta fidelidade: a NISA converteu o grito de pavor puro de Lyner diante de uma entidade assassina no frívolo 'Whoa!', desfigurando a atmosfera de horror cósmico."
    },
    {
        "id": 12479,
        "scene": "A Virada Sádica da Projeção de Aurica",
        "original_jp": "...あたし...CRライナーを殺したくてたまらなかったの...。出逢えて良かった!",
        "original_en": "I wanted to kill you so badly...and now, I finally found you!",
        "curated_ptbr": "...Eu...\ntava com tanta vontade de matar você, Lyner...\nQue bom que a gente se encontrou!",
        "rationale": "Preservação da modulação aterrorizante yandere de Aurica dentro do pesadelo, com quebra rítmica precisa."
    },
    {
        "id": 12517,
        "scene": "O Pacto Suicida da Persona Infantil de Misha",
        "original_jp": "ライナーと私をこの部屋に幽閉しちゃうの。そうすれば、私もライナーも一生目を醒まさない。ずっと2人きりでいられるわ。",
        "original_en": "You and I will be locked up in this room and we’ll never wake up. You and I can stay here together forever.",
        "curated_ptbr": "Nós vamos nos trancar para sempre neste quarto. Assim, nem eu nem você jamais vamos acordar... E poderemos ficar nós dois a sós por toda a eternidade.",
        "rationale": "Fidelidade absoluta ao vocabulário existencial de reclusão (幽閉) e sono eterno (一生目を醒まさない), evidenciando a depressão profunda da heroína."
    },
    {
        "id": 12532,
        "scene": "O Afeto e a Fúria Protetora de Hama",
        "original_jp": "ホントにもう、上手いことミシャにのせられちゃって...。これが私のお父さんだっていうんだから...たまんないわよ...",
        "original_en": "Misha seduced you... I’m ashamed to see my father like this...",
        "curated_ptbr": "Francamente, cair na lábia da Misha com essa facilidade toda... E pensar que um frouxo desses é o meu pai... É o fim da picada...",
        "rationale": "Resgate cômico e afetuoso da expressão idiomática 'たまんないわよ' e do laço de Hama com seu 'criador/pai' Lyner."
    },
    {
        "id": 12593,
        "scene": "A Quebra da Quarta Parede por Aurica",
        "original_jp": "というわけで、「マリーのアトリエ・ザールブルグの錬金術士」はこんなゲームです!CR皆さん、ぜひ買ってプレイしてみてね!",
        "original_en": "That was a preview of a game called [Atelier Marie: Alchemist of Salburg]! Please buy it and enjoy!",
        "curated_ptbr": "E assim é o jogo \"Atelier Marie: A Alquimista de Salburg\"!\nPessoal, não deixem de comprar e jogar, viu?!",
        "rationale": "Humor metalinguístico afiado com pontuação viva em português brasileiro, honrando o primeiro título da Gust."
    },
    {
        "id": 12645,
        "scene": "A Nobreza Moral Inabalável de Radolf",
        "original_jp": "謀反の濡れ衣を着せられても、まだ尚教会に忠誠を誓うのか。恐れ入るよ。",
        "original_en": "You’re still loyal to the Church, even though they branded you as a traitor.",
        "curated_ptbr": "Mesmo tendo sido falsamente acusado de traição, ainda mantém sua lealdade à Igreja? É impressionante.",
        "rationale": "Restauração da expressão jurídica ancestral '謀反の濡れ衣' (falsa acusação de traição/rebelião) e da reverência contida de Ayatane."
    }
]

output_data = {
    "block_id": "BLK_EVD_053",
    "axis_id": "AXIS_3",
    "axis_name": "3_HISTORIA_E_EVENTOS",
    "category": "Event Dialogue",
    "line_count": len(dialogues_out),
    "id_range": [12458, 12647],
    "dialogues": dialogues_out,
    "curated_lines": curated_lines_out,
    "new_terms": new_terms,
    "glossary_updates": glossary_updates,
    "scene_handoff_final": scene_handoff_final,
    "highlights": highlights
}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"[SUCESSO] Bloco BLK_EVD_053 gerado com {len(dialogues_out)} falas em {OUTPUT_PATH}")

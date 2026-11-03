# -*- coding: utf-8 -*-
"""
assemble_and_validate_062.py - Montagem e validação rigorosa de BLK_EVD_062
"""
import sys
import json
import re

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

INPUT_PATH = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_062_input.json"
OUTPUT_PATH = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_062_output.json"

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

# Base dictionary of curated lines: id -> (ptbr_curated, rationale)
curations = {}

# Section 1: Event/703.evd (14343 - 14393)
curations[14343] = (
    "Q-quem é você!?",
    "Aurica sobressalta-se ao ver Lyner pela primeira vez em sua Cosmosfera."
)
curations[14344] = (
    "Eu sou Lyner. Lyner Barsett.\nVim a este mundo na esperança\nde que você pudesse tecer uma Canção para nós.",
    "Lyner se apresenta com cordialidade e franqueza, explicando o propósito do Mergulho."
)
curations[14345] = (
    "...Uma Canção?\nEu não sirvo para isso. Jamais conseguiria tecer...\nNão tenho esse tipo de poder...",
    "Aurica expressa seu complexo crônico de inferioridade, desacreditando de sua própria capacidade."
)
curations[14346] = (
    "Não acho que seja bem assim...\nPara começar, este não é o seu mundo?\nVocê pode criar o que bem entender por aqui.",
    "Lyner incentiva Aurica, lembrando-a de que a Cosmosfera é regida pela imaginação dela."
)
curations[14347] = (
    "Para mim, não é algo tão simples assim.\nNão para quem não consegue salvar nem o próprio vilarejo...",
    "Aurica lamenta sua impotência, remoendo o trauma da destruição de seu vilarejo."
)
curations[14348] = (
    "...Este vilarejo já foi destruído inúmeras vezes\npor causa do Demônio do Fogo que surge do nada.\nRadolf, que mora aqui, diz que sou eu quem o atrai.",
    "Aurica relata as investidas do Demônio do Fogo e a acusação de Radolf dentro de sua mente."
)
curations[14349] = (
    "C-como é que é?!\nVocê, atraindo o Demônio do Fogo?!\nNão tem como uma coisa dessas ser verdade!",
    "Lyner reage indignado diante da acusação absurda de que Aurica atrairia o monstro."
)
curations[14350] = (
    "Mas deve ser verdade...\nPor causa disso, este vilarejo já virou cinzas\nincontáveis vezes no passado.",
    "Aurica assume a culpa com tristeza pelo histórico de incêndios do vilarejo."
)
curations[14351] = (
    "E... o Radolf sempre o reconstrói para nós.\nEle é um homem ríspido e inflexível,\nmas, no fundo, é alguém de bom coração.",
    "Aurica descreve a nobreza e a proteção do Radolf projetado em seu mundo interior."
)
curations[14352] = (
    "...Hum... Que estranho...\nEste lugar não é o seu mundo, Aurica?\nPor que você mesma não consegue reconstruir o vilarejo...?",
    "Lyner estranha o paradoxo de Aurica não conseguir restaurar as próprias construções mentais."
)
curations[14353] = (
    "Neste mundo, você deveria ser capaz de fazer tudo!\nNão apenas reconstruir o vilarejo,\nmas até impedir que o Demônio do Fogo invadisse...",
    "Lyner aponta o potencial ilimitado de uma Reyvateil sobre sua própria Cosmosfera."
)
curations[14354] = (
    "Eu não sou capaz disso!\nA única coisa que eu consigo...\né trazer sofrimento para este vilarejo...",
    "Aurica expressa sua angústia e culpa profunda, acreditando ser apenas uma praga destruidora."
)
curations[14355] = (
    "... (Nossa, ela se martiriza tanto...)",
    "Lyner reflete comovido sobre o nível extremo de autodepreciação demonstrado por Aurica."
)
curations[14356] = (
    "Olha, Aurica. Para começar, vamos enfrentar esse Demônio do Fogo.\nComo este mundo é seu, você deve saber\num jeito de fazê-lo desaparecer, não sabe?",
    "Lyner propõe enfrentar a manifestação hostil, apelando para o controle de Aurica sobre a Cosmosfera."
)
curations[14357] = (
    "...",
    "Aurica silencia, demonstrando hesitação e desconhecimento."
)
curations[14358] = (
    "Você não sabe?\nEntão como foi que você fez ele aparecer?",
    "Lyner se surpreende com a falta de controle de Aurica sobre o próprio mundo mental."
)
curations[14359] = (
    "Não sei...\nEle sempre surge sem que eu perceba...\ndestrói tudo e vai embora...",
    "Aurica descreve o caráter imprevisível e devastador das manifestações de seu trauma."
)
curations[14360] = (
    "Hum... Que situação complicada...\nEntão não tem jeito, teremos que lutar.\nVocê não consegue tecer alguma magia para atacar?",
    "Lyner conclui que a única saída é o confronto e sugere a criação de uma magia ofensiva."
)
curations[14361] = (
    "...Eu não quero.\nMorro de vergonha...\nTodo mundo sempre ri das coisas que eu crio...",
    "Aurica resiste por vergonha, temendo o deboche e o escárnio aos quais estava acostumada."
)
curations[14362] = (
    "...Riem? Por quê?",
    "Lyner estranha a reação e questiona o motivo dos risos alheios."
)
curations[14363] = (
    "É que eu sou boba...\nSó consigo criar coisas esquisitas...\ne sou fraca demais...",
    "Aurica verbaliza sua autodepreciação, sentindo-se incapaz e ridícula."
)
curations[14364] = (
    "Não tem o menor problema!\nTente assim mesmo, por favor.",
    "Lyner acolhe a fragilidade de Aurica com insistência calorosa."
)
curations[14365] = (
    "...Mas vai sair fraquinha de verdade, sabia?",
    "Aurica reforça sua hesitação, prevenindo-o sobre a fraqueza de suas criações."
)
curations[14366] = (
    "Eu já disse que não me importo!",
    "Lyner reafirma com convicção que não se importa com a potência da magia."
)
curations[14367] = (
    "...Você vai rir da minha cara.",
    "Aurica expressa seu medo infantil e vulnerável de ser ridicularizada."
)
curations[14368] = (
    "Eu não vou rir, já falei!",
    "Lyner assegura solenemente que jamais zombaria dela."
)
curations[14369] = (
    "Jamais teríamos chance contra o Demônio do Fogo...",
    "Aurica duvida da eficácia de suas forças contra a ameaça ameaçadora."
)
curations[14370] = (
    "Vai dar tudo certo!\nConfie em mim e tente tecer alguma coisa!",
    "Lyner transmite confiança e encoraja Aurica a dar o salto de fé."
)
curations[14371] = (
    "...T-tá bom... Eu vou tentar...",
    "Aurica cede timidamente ao incentivo e decide tentar."
)
curations[14372] = (
    "Lá vai...",
    "Aurica se concentra para iniciar a tecitura."
)
curations[14373] = (
    "Eiiih!!",
    "Grito fofo e focado de liberação de energia no instante da tecitura."
)
curations[14374] = (
    "Apareceu!",
    "Lyner comemora a manifestação visual da magia recém-nascida."
)
curations[14375] = (
    "D-desculpa...\nEu avisei que só conseguiria conjurar algo assim...",
    "Aurica se desculpa envergonhada, julgando sua criação insignificante."
)
curations[14376] = (
    "Ei, ei, ei! Depois de me tecer com tanto esforço,\nchamar de \"algo assim\" é muita maldade!\nDá um tempo, francamente...",
    "A bola de fogo ganha vida com voz tagarela e se ofende ao ser tratada com desdém."
)
curations[14377] = (
    "Ele falou?!",
    "Aurica se assusta ao perceber que sua própria magia possui consciência e fala."
)
curations[14378] = (
    "Tá surpresa por quê?\nNão foi você que pensou \"seria tão fofo se falasse\"\nquando começou a me tecer, senhorita?",
    "O ser mágico confronta Aurica, revelando que seu dom da fala nasceu dos pensamentos íntimos dela."
)
curations[14379] = (
    "É-é verdade, mas...\nEu jamais imaginei que fosse falar para valer!",
    "Aurica confessa seu espanto infantil diante da materialização literal de seu desejo."
)
curations[14380] = (
    "Incrível! Viu só como você consegue tecer direitinho?\nEu jamais conseguiria fazer algo assim.\nTenha mais orgulho de si mesma!",
    "Lyner celebra o feito com entusiasmo genuíno, ressaltando o valor único do talento dela."
)
curations[14381] = (
    "Este lugar é o seu mundo, Aurica!\nSe acreditar e mentalizar \"eu posso tecer!\",\nvocê poderá criar qualquer coisa por aqui.",
    "Lyner ensina a regra de ouro da Cosmosfera: a força criativa brota da autoconfiança."
)
curations[14382] = (
    "...É, tem razão.\nM-mas uma magia simplória dessas...",
    "Aurica hesita entre o carinho de Lyner e a vergonha pelo visual modesto da magia."
)
curations[14383] = (
    "Não venha com essa de \"magia simplória\"!!\nAgora que vim ao mundo, pretendo me esforçar\nao máximo para ser útil, sabia?!",
    "A pequena chama protesta cheia de brio, declarando sua lealdade prestativa."
)
curations[14384] = (
    "A bola de fogo tem toda razão!\nAlém disso, ela com certeza terá muita utilidade.",
    "Lyner acolhe a defesa do pequeno ser ígneo e enxerga seu lado prático."
)
curations[14385] = (
    "Dá para assar carne com ela, por exemplo!\nNem tudo na vida é poder bruto, não acha?\nAfinal, não dá para assar um bife com uma bomba.",
    "Lyner brinca com o utilitarismo doméstico da chama, fazendo sutil contraste com as bombas de Misha."
)
curations[14386] = (
    "...Ehehe, é verdade.",
    "Aurica ri de forma doce e relaxada, desarmada pelo bom humor de Lyner."
)
curations[14387] = (
    "\"Ehehe\" nada, sua...! Você concorda com isso?!\nC-carne assada?! Fala sério...",
    "O Tiro Ígneo indigna-se comicamente ao perceber que seu destino é virar churrasqueira portátil."
)
curations[14388] = (
    "Você teceu a Magia Verde [Tiro Ígneo]!",
    "Notificação de sistema confirmando a criação da primeira Magia Verde de Aurica."
)
curations[14389] = (
    "Viu só, Aurica? Você teceu a sua magia!",
    "Lyner celebra o triunfo com alegria fraterna, incentivando a parceira."
)
curations[14390] = (
    "C-como é que éeee?!\nSeu canalhaaa! O que você fez com a Senhorita Aurica?!",
    "Don Leon irrompe enfurecido e histriônico, cobrando explicações de Lyner."
)
curations[14391] = (
    "Eu não fiz nada de mal!\nAliás, por que você tá tão desesperado?\nSerá que... você não queria que ela tecesse magia?",
    "Lyner reage com estranheza ao pânico suspeito de Don Leon."
)
curations[14392] = (
    "Não diga tolices!\nÉ só que... já fazia muitos anos que a Senhorita Aurica\nnão conseguia tecer magia alguma.",
    "Don Leon revela que o bloqueio mágico de Aurica perdurava há anos desde o trauma original."
)
curations[14393] = (
    "Então era isso...",
    "Lyner compreende a gravidade do passado e a importância daquele primeiro passo."
)

# Section 2: Event/640.evd (14394 - 14483)
curations[14394] = (
    "Droga... Não adianta...\nO dragão continua me caçando, não importa para onde eu vá...",
    "Lyner foge ofegante do dragão incansável na Cosmosfera de Misha."
)
curations[14395] = (
    "Por quê?!\nPor que você continua vindo atrás de mim?!",
    "Lyner grita desesperado, sem compreender a fixação do monstro."
)
curations[14396] = (
    "...Grrr...",
    "O dragão rosna com ferocidade primal e intimidadora."
)
curations[14397] = (
    "Não tenho mais para onde fugir...\nTem que haver um jeito... uma rota de fuga...",
    "Lyner se vê encurralado e busca freneticamente uma brecha para escapar."
)
curations[14398] = (
    "Gyarrrgh!!",
    "Rugido cortante de ataque do dragão antes de desferir o bote."
)
curations[14399] = (
    "Guh...!\nDroga... Ele me acertou com as garras...",
    "Lyner é golpeado com violência e acusa o impacto das garras da fera."
)
curations[14400] = (
    "O-o que é... isto...?\nSerá que... são garras venenosas...?",
    "Lyner sente os efeitos paralisantes do veneno correndo por suas veias."
)
curations[14401] = (
    "Exato.\nE aí, que tal o gosto do veneno de dragão\npreparado especialmente por mim?",
    "A persona sombria de Misha manifesta-se com provocação sádica e doce veneno."
)
curations[14402] = (
    "...Misha... por quê...?",
    "Lyner reconhece a voz da amiga e balbucia atônito perante a traição inconcebível."
)
curations[14403] = (
    "Gyarrrgh!!",
    "O dragão ruge ferozmente sob o influxo da vontade da dona da mente."
)
curations[14404] = (
    "Gyaaaah!!\nGuh...",
    "Lyner solta um berro de agonia perante novo golpe devastador."
)
curations[14405] = (
    "Droga... Minha cabeça... tá ficando... zonza...\nSerá que... vou morrer aqui...?",
    "A consciência de Lyner esvai-se com a toxina letal."
)
curations[14406] = (
    "Fique tranquilo...\nAcha mesmo que eu mataria o meu precioso Lyner?",
    "Misha fala com doçura arrepiante e possessiva, revelando sua persona distorcida."
)
curations[14407] = (
    "Eu não suportaria ver você morrer...",
    "Misha sussurra um apego angustiado e doentio."
)
curations[14408] = (
    "Gyarrrgh!!",
    "O dragão ruge novamente para subjugar a vítima."
)
curations[14409] = (
    "Guhaaaah!\nHaa... haa... Não consigo respirar...\nO veneno se espalhou... Minha cabeça tá girando...",
    "Lyner arfa com a respiração cortada enquanto a peçonha atinge seu ápice."
)
curations[14410] = (
    "...Dói?... Está sofrendo?",
    "Misha indaga com curiosidade sussurrada e morbidez íntima."
)
curations[14411] = (
    "Por que... tá fazendo isso comigo...?",
    "Lyner suplica em agonia por uma resposta à tortura mental."
)
curations[14412] = (
    "Dói, não dói?\nA intensidade dessa dor é o tamanho do meu amor por você...\nVocê me traiu, e este é o seu merecido castigo...",
    "Misha equipara a dor física à grandeza de sua paixão ferida pela traição percebida."
)
curations[14413] = (
    "Traí você...?!\nEu... traí a Misha...?!",
    "Lyner fica atordoado e estarrecido diante da acusação que dilacera sua alma."
)
curations[14414] = (
    "...Grrr...",
    "O dragão ronda em tom de ameaça constante."
)
curations[14415] = (
    "Guh... gaaah...",
    "Gemido involuntário ante os espasmos musculares da toxina."
)
curations[14416] = (
    "Traiu...\nOu melhor, você sempre me trai, em todos os momentos.",
    "Misha generaliza seu sofrimento solitário de anos de abandono na Torre."
)
curations[14417] = (
    "M-mentira!\nEu nunca traí a Misha na minha vida...!",
    "Lyner rebate com desespero, reafirmando sua fidelidade à amiga de infância."
)
curations[14418] = (
    "Isso... é porque você nunca traiu a Misha\nque guarda aí dentro do seu próprio coração, não é?",
    "Misha desvenda a cisão psicológica entre a memória idealizada dele e a realidade dilacerada dela."
)
curations[14419] = (
    "Mas o Lyner que habita o meu peito\nme trai todos os santos dias. E nem imagina\nquantas e quantas vezes já me matou por dentro...",
    "Revelação devastadora da solidão de Misha quando prisioneira no selo de Mir."
)
curations[14420] = (
    "...!!",
    "Lyner se cala em choque absoluto diante do peso do trauma de Misha."
)
curations[14421] = (
    "Mas hoje você tá bem aqui. Não é o Lyner das minhas lembranças,\né você de carne e osso, em pessoa...\nIsso me dá até um arrepio gostoso...",
    "Misha vibra com a presença real de Lyner, mesclando afeto ardente e sadismo onírico."
)
curations[14422] = (
    "...O-o meu corpo... tá dormente...",
    "O entorpecimento neuromuscular avança sobre o corpo de Lyner."
)
curations[14423] = (
    "Ora... Lyner?! Você tá bem?\nO veneno do dragão já se espalhou, né...?\nNão quero que você morra, ouviu...?",
    "Misha finge preocupação carinhosa enquanto contempla o efeito do veneno."
)
curations[14424] = (
    "Mas, se caiu nas presas venenosas do dragão, não tem muito jeito...\nPelo menos, ficarei ao seu lado até o seu último suspiro.",
    "Promessa sombria de acompanhar a agonia do amado sem intervir para salvá-lo."
)
curations[14425] = (
    "Quando esse veneno corre pelo sangue,\nele vai trazendo uma sensação aconchegante, sabia?\nNo fim das contas, leva ao mais puro êxtase.",
    "Misha descreve as propriedades sedutoras e anestesiantes da toxina."
)
curations[14426] = (
    "Mas fique em paz. Mesmo que tenha uma morte humilhante,\neu jamais deixaria de te amar, Lyner...",
    "Declaração incondicional de afeto bizarro, prometendo amor mesmo na ruína do rapaz."
)
curations[14427] = (
    "Afinal de contas, você ficou ao meu lado até o fim...\ncom os olhos fixos em mim. Sem me abandonar,\nsem me deixar para trás...",
    "Misha expõe a raiz de seu delírio: a necessidade visceral de atenção exclusiva de Lyner."
)
curations[14428] = (
    "...Não... dá...\nMinha mente... tá apagando...\nNão consigo... pensar em nada...",
    "Lyner sucumbe ao desmaio com a perda total da clareza mental."
)
curations[14429] = (
    "Mas que situação deplorável vocês arrumaram...",
    "A consciência alternativa de Misha intervém com ironia ao presenciar o impasse."
)
curations[14430] = (
    "...Quem é você?",
    "Misha estranha a presença da intrusa em seu domínio mental."
)
curations[14431] = (
    "...Você... sou eu...?!",
    "Misha reconhece com espanto o reflexo de si mesma na outra entidade."
)
curations[14432] = (
    "Isso mesmo. Eu sou você.\nE você... passou de todos os limites desta vez...",
    "A persona autônoma adverte a Misha possessiva sobre o desmando cometido."
)
curations[14433] = (
    "...Não aguento mais... Meus sentidos...",
    "Lyner apaga completamente enquanto a cena é cortada."
)
curations[14434] = (
    "Você... passou dos limites...",
    "Fragmento de voz ouvido por Lyner no limiar da inconsciência."
)
curations[14435] = (
    "...Onde... estou...?",
    "Lyner desperta desorientado em um novo ambiente da Cosmosfera."
)
curations[14436] = (
    "No Stonehenge. Você tá bem?",
    "A garota identifica o monumento megalítico e checa a recuperação dele."
)
curations[14437] = (
    "V-você!!\nSe não me engano, foi quem manipulou a Misha no nível anterior...",
    "Lyner recorda o papel ambíguo daquela persona em patamares anteriores."
)
curations[14438] = (
    "Que falta de consideração me chamar de manipuladora.\nEssa não é forma de falar com quem acabou de salvar a sua vida.",
    "A persona cobra gratidão com elegância arrogante e altiva."
)
curations[14439] = (
    "...Afinal de contas... você é inimiga ou aliada?",
    "Lyner busca delimitar a lealdade da entidade misteriosa."
)
curations[14440] = (
    "Fufufu... Inimiga ou aliada?\nEu não sou nem sua adversária, nem sua companheira.",
    "A entidade recusa classificações simplórias com riso misterioso."
)
curations[14441] = (
    "Sou a consciência inovadora que zela pela \"alma livre\"\nno íntimo de Misha, agindo para preservá-la.",
    "Define sua identidade canônica: a manifestação do anseio de liberdade reprimido de Misha."
)
curations[14442] = (
    "...?",
    "Reação de confusão reflexiva de Lyner."
)
curations[14443] = (
    "Com o tempo você compreenderá.\nQuando alcançar o meu nível... é claro.",
    "Foreshadowing sobre os níveis mais profundos da mente de Misha."
)
curations[14444] = (
    "Mudando de assunto, se continuar zanzando por este nível,\nvocê será assassinado para valer.",
    "Alerta prático sobre a letalidade das defesas mentais descontroladas de Misha."
)
curations[14445] = (
    "Tá falando sério...? Mas por que a Misha tentaria me matar...?\nSerá que a Misha deste nível me odeia tanto assim...?",
    "Lyner teme que a aversão venha de rancor genuíno acumulado."
)
curations[14446] = (
    "Não seja tolo. Ela te valoriza mais do que a qualquer um no mundo. É esse amor profundo que está se manifestando de forma distorcida.",
    "Explica o mecanismo de defesa psicológico por trás do ímpeto assassino."
)
curations[14447] = (
    "...Não faz o menor sentido para mim.\nAfinal, ela estava tentando me matar com as próprias mãos!",
    "A lógica racional de Lyner colide com os paradoxos emocionais do inconsciente."
)
curations[14448] = (
    "...",
    "Silêncio condescendente da guardiã perante a ingenuidade masculina."
)
curations[14449] = (
    "Seja como for, se deseja continuar Mergulhando na Cosmosfera de Misha,\nterá que conduzir este mundo a um desfecho pacífico.",
    "Estabelece o requisito de cura emocional para avançar no Mergulho."
)
curations[14450] = (
    "Para conseguir isso, teremos que abater aquele dragão.\nEu darei uma força para você.",
    "Propõe aliança prática para neutralizar a fera do trauma."
)
curations[14451] = (
    "T-tá certo...",
    "Aquiescência hesitante de Lyner ante a determinação da garota."
)
curations[14452] = (
    "Vejamos... Por onde será que aquele monstro anda se escondendo...?",
    "Planejamento tático para rastrear o dragão pela mente."
)
curations[14453] = (
    "Você teceu a Magia Vermelha [Gota Divina]!",
    "Notificação canônica da tecitura da Magia Vermelha Gota Divina (JP 雫神)."
)
curations[14454] = (
    "Lyner!\nQue alívio ver que você está são e salvo.",
    "A mentora do Mundo Inferior acolhe Lyner após o rito de superação."
)
curations[14455] = (
    "Pois é...\nMas faltou bem pouco para eu bater as botas de vez.",
    "Lyner desabafa em tom coloquial sobre o risco extremo que correu."
)
curations[14456] = (
    "Nesta profundidade da mente, até os meus poderes são impotentes para te socorrer.",
    "Adverte sobre o alcance limitado de suas orientações em camadas profundas."
)
curations[14457] = (
    "Além do mais, como você já deve ter percebido,\nestamos nos aproximando do inconsciente mais profundo de Misha.",
    "Contextualiza a descida aos estratos basilares da psique."
)
curations[14458] = (
    "O inconsciente profundo frequentemente age de modo oposto\nà mente desperta, ainda que a raiz de ambos seja rigorosamente a mesma...",
    "Explica a dinâmica psicológica entre ego e sombra em Ar tonelico."
)
curations[14459] = (
    "Puxa vida...\nIsso tudo é complicado demais para a minha cabeça...",
    "Lyner expressa sua sobrecarga mental diante de conceitos psicológicos complexos."
)
curations[14460] = (
    "Em resumo: embora a Misha de sempre e a deste mundo\ntenham atitudes tão opostas,\no sentimento na raiz de ambas é exatamente o mesmo.",
    "Sintetiza de forma didática o princípio da dualidade da Cosmosfera."
)
curations[14461] = (
    "É aí que mora o perigo. Nos próximos níveis, você enfrentará mundos assim.\nNão será apenas na base do seu \"amor e esperança\"\nque conseguirá superar todos os obstáculos.",
    "Alerta firme contra o idealismo ingênuo de Lyner perante a dor reprimida."
)
curations[14462] = (
    "...Entendo...",
    "Lyner assimila a lição com maturidade sóbria."
)
curations[14463] = (
    "É por isso que dizem que o Mundo Espiritual fica assustador\nconforme você se aprofunda. Mas não desanime, mantenha a firmeza.",
    "Encerra a mentoria com incentivo vigoroso para a jornada adiante."
)
curations[14464] = (
    "Guh...!\nDroga... Fui pego pelas garras dele...",
    "Lyner é abatido pelas garras do dragão na rota de fracasso."
)
curations[14465] = (
    "O-o que é... isto...?\nSerá que... são garras venenosas...?",
    "O veneno volta a paralisar o corpo do protagonista."
)
curations[14466] = (
    "Exato.\nE aí, que tal o gosto do veneno de dragão\npreparado especialmente por mim?",
    "A persona sombria zomba da agonia iminente de Lyner."
)
curations[14467] = (
    "...Misha... por quê...?",
    "Murmúrio desesperado perante a traição inabalável."
)
curations[14468] = (
    "Gyarrrgh!!",
    "Rugido final do dragão ao golpear mortalmente."
)
curations[14469] = (
    "Gyaaaah!!\nGuh...",
    "Grito agonizante perante a derrota física irreversível."
)
curations[14470] = (
    "Ora... Lyner?! Você tá bem?\nNão quero que você morra, ouviu...?\nPor favor, não me deixe sozinha neste mundo...",
    "Misha desaba em desespero possessivo ante a morte iminente do parceiro."
)
curations[14471] = (
    "Mas, se caiu nas presas venenosas do dragão, não tem muito jeito...\nPelo menos, ficarei ao seu lado até o seu último suspiro.",
    "Resignação macabra e doentia de quem prefere vê-lo morrer a deixá-lo partir."
)
curations[14472] = (
    "Quando esse veneno corre pelo sangue,\nele vai trazendo uma sensação aconchegante, sabia?\nNo fim das contas, leva ao mais puro êxtase.",
    "Descrição hipnótica e anestésica do veneno letal."
)
curations[14473] = (
    "Mas fique em paz. Mesmo que tenha uma morte humilhante,\neu jamais deixaria de te amar, Lyner...",
    "Promessa sombria de adoração perpétua que transcende a morte."
)
curations[14474] = (
    "Afinal de contas, você ficou ao meu lado até o fim...\ncom os olhos fixos em mim. Sem me abandonar,\nsem me deixar para trás...",
    "O clímax do desvio afetivo: a morte garante que ele nunca a abandonará."
)
curations[14475] = (
    "... ......",
    "Silêncio absoluto do protagonista que perde os sentidos."
)
curations[14476] = (
    "...",
    "Silêncio grave da mentora diante da fatalidade onírica."
)
curations[14477] = (
    "Eu... morri?",
    "Lyner desperta no limiar e questiona seu próprio destino."
)
curations[14478] = (
    "Dentro deste mundo mental, sim.\nO melhor a fazer agora é retornar ao mundo real por um tempo.",
    "Esclarece que a morte mental requer a ejeção forçada para o mundo físico."
)
curations[14479] = (
    "Misha...",
    "Lyner sussurra o nome da amiga em profunda comoção."
)
curations[14480] = (
    "Esta é a dura realidade do inconsciente profundo.\nCompreendeu agora por que eu disse que era assustador?",
    "Destaca a gravidade das correntes emocionais ocultas."
)
curations[14481] = (
    "O inconsciente profundo frequentemente age de modo oposto\nà mente desperta, ainda que a raiz de ambos seja rigorosamente a mesma...",
    "Reitera a tese psicológica central da Cosmosfera."
)
curations[14482] = (
    "De todo modo, ao contrário dos níveis anteriores,\ndaqui para frente as coisas não se resolverão com tanta facilidade.",
    "Alerta para a complexidade crescente das barreiras mentais."
)
curations[14483] = (
    "Se você pretende continuar desbravando a Cosmosfera de Misha,\né bom estar preparado de corpo e alma.",
    "Conclui com advertência solene para os próximos mergulhos."
)

# Section 3: Event/238.evd (14484 - 14518)
curations[14484] = (
    "Aaaah, como foi divertido!\nEi, Lyner, vamos ao parque!",
    "Misha demonstra alegria infantil após um raro momento de lazer."
)
curations[14485] = (
    "E aí?\nDeu para relaxar um pouco?",
    "Misha indaga com afeto se o passeio aliviou o estresse dele."
)
curations[14486] = (
    "Sim, graças a você.\nEmbora eu tenha passado um baita sufoco\npor outros motivos...",
    "Lyner brinca sobre o estresse cômico de apartar as confusões dela com Krusche."
)
curations[14487] = (
    "Desculpa... No fim das contas,\neu passei quase o tempo todo implicando com a Krusche.",
    "Misha reconhece com culpa fofa que se distraiu nas birras com Krusche."
)
curations[14488] = (
    "Eu acabei usando você como pretexto só porque quem queria brincar era eu mesma.",
    "Misha admite com transparência que desejava viver momentos de infância."
)
curations[14489] = (
    "Mas isso foi ótimo!\nAcho que nunca tinha visto você tão alegre assim, Misha.",
    "Lyner celebra a felicidade autêntica da companheira de infância."
)
curations[14490] = (
    "...Ehehe.",
    "Risinho tímido e feliz de Misha."
)
curations[14491] = (
    "Eu também... Acho que foi a primeira vez que me diverti como uma criança de verdade.",
    "Lembrança agridoce de uma infância sacrificada pelo dever sagrado."
)
curations[14492] = (
    "Mas...\ntalvez esta tenha sido a última vez...",
    "A sombra do dever cai repentinamente sobre a alegria efêmera."
)
curations[14493] = (
    "Como é que é?!",
    "Lyner sobressalta-se com a mudança drástica de tom."
)
curations[14494] = (
    "Escuta, Lyner...\nPara falar a mais pura verdade...\neu não quero cantar.",
    "Confissão dilacerante de Misha: a recusa íntima do fardo de cantar eternamente."
)
curations[14495] = (
    "No fundo do peito, eu chego a desejar que a gente nunca encontre a Canção...",
    "O anseio inconsciente de que o Cristal Hymmnos permaneça perdido para que ela seja livre."
)
curations[14496] = (
    "Misha?!",
    "Espanto e preocupação com a dor oculta da amiga."
)
curations[14497] = (
    "É claro que vou procurar com tudo de mim! E... vou cantar também...",
    "Conflito interno entre o dever sagrado inegociável e seus desejos juvenis."
)
curations[14498] = (
    "Afinal de contas, as pessoas do mundo inteiro\nestão aguardando pelo meu Cântico.",
    "Consciência do fardo planetário que repousa sobre seus ombros de Reyvateil Origin."
)
curations[14499] = (
    "Lyner, muito obrigada por hoje.\nEu te dei um trabalho danado, mas me diverti demais.",
    "Agradecimento terno e comovido pela tarde de carinho compartilhado."
)
curations[14500] = (
    "Até porque este pode muito bem ser\no nosso último encontro como pessoas comuns.",
    "Misha reconhece a linha divisória entre a vida mortal e a imolação sacerdotal."
)
curations[14501] = (
    "Não diga uma bobagem dessas...",
    "Lyner se recusa a aceitar a resignação fúnebre daquela despedida."
)
curations[14502] = (
    "Não é exagero nenhum, Lyner.\nAssim que a Canção for encontrada, a partir desse instante\neu voltarei a ser a Cantora das Estrelas.",
    "Misha reafirma sua sina com o título canônico sagrado de Cantora das Estrelas."
)
curations[14503] = (
    "Por isso eu precisava te contar tudo.\nEu queria que soubesse exatamente\no que sinto aqui dentro.",
    "Declaração de amor e vulnerabilidade antes do retorno ao altar."
)
curations[14504] = (
    "No fundo, eu sou só uma garota comum como as outras.\nEu também queria passear, brincar, comer doces gostosos...",
    "O lamento humano da divindade forçada pelo sacrifício."
)
curations[14505] = (
    "Mas já coloquei a minha cabeça no lugar, então tá tudo bem!",
    "Misha recompõe seu ânimo com heroica maturidade tsundere."
)
curations[14506] = (
    "E eu...",
    "Lyner hesita perante sua própria pequenez e impotência."
)
curations[14507] = (
    "...O quê?",
    "Misha nota a aflição nos olhos do parceiro."
)
curations[14508] = (
    "Será que eu... não posso fazer nada por você,\nMisha...?",
    "Angústia cavalheiresca de Lyner ao se ver incapaz de libertar a amada de seu fardo."
)
curations[14509] = (
    "Deixa de ser bobo, Lyner...\nVocê já fez mais do que o suficiente por mim,\ne com sobras.",
    "Misha consola o cavaleiro com afeto enternecido."
)
curations[14510] = (
    "...Muito obrigada.",
    "Agradecimento sussurrado do fundo do coração."
)
curations[14511] = (
    "Ei, Lyner!\nNão é hora de ficar sonhando acordado!\nDescolei uma informação quente de primeira!",
    "Jack interrompe o clima intimista com sua veia de mercenário despachado."
)
curations[14512] = (
    "É sério?",
    "Lyner recupera o foco tático e questiona a novidade."
)
curations[14513] = (
    "Corre o boato de que há uma brecha perto do Silvaplate por onde dá para entrar no coração da Torre.",
    "Jack traz a pista do Silvaplate com terminologia canônica."
)
curations[14514] = (
    "Parece que, entrando por ali,\ndá para alcançar as imediações do Beco Vagalume.",
    "Aponta o trajeto secreto rumo ao Beco Vagalume."
)
curations[14515] = (
    "...Tem certeza disso?",
    "Lyner busca confirmar a solidez da rota."
)
curations[14516] = (
    "Bem, só vamos descobrir se formos até lá ver com os próprios olhos. É bem melhor do que ficar aqui mofando.",
    "Pragmatismo experiente de mercenário calejado que prefere ação a inércia."
)
curations[14517] = (
    "...Tens razão.\nVamos partir rumo ao Silvaplate.",
    "Lyner acata a sugestão e traça o próximo rumo da comitiva."
)
curations[14518] = (
    "Jack entrou para o grupo!",
    "Notificação canônica padronizada da entrada de Jack no grupo ativo."
)

# Section 4: Event/538.evd (14519 - 14550)
curations[14519] = (
    "Isto é...",
    "Shurelia contempla o templo com reverência solene."
)
curations[14520] = (
    "Dentre os muitos Templos de Elemia, este é o de maior magnitude...\nO Neo-Templo de Elemia...",
    "Shurelia identifica o monumento sagrado com a terminologia oficial Neo-Templo de Elemia."
)
curations[14521] = (
    "Existiam assim tantos Templos de Elemia no passado?",
    "Lyner pergunta com polidez respeitosa à Administradora."
)
curations[14522] = (
    "Sim. Os templos consagrados como Templos de Elemia no passado...\neram incontáveis.",
    "Shurelia confirma a vasta devoção pretérita em Sol Ciel."
)
curations[14523] = (
    "A fé em Elemia...\né reverenciada desde tempos imemoriais.",
    "Radolf reconhece as raízes milenares de sua própria congregação religiosa."
)
curations[14524] = (
    "E pensar que eles se aproveitaram de uma fé com tanta história\npara conspirar pela ressurreição de Mir...",
    "Radolf lamenta a profanação da Igreja pelo fanatismo pró-Mir."
)
curations[14525] = (
    "Maldito Falss...\nJamais o perdoarei por isso!",
    "Indignação santa de Radolf contra a perfídia do bispo renegado."
)
curations[14526] = (
    "A título de curiosidade... houve uma época no passado\nem que a própria Mir era venerada neste mesmo templo.",
    "Shurelia compartilha memória histórica desconhecida pelos contemporâneos."
)
curations[14527] = (
    "Era aclamada pelo povo como a \"reencarnação do Trio de Elemia\"...",
    "Revela o culto profético devotado a Mir no zênite da civilização anterior."
)
curations[14528] = (
    "Afinal de contas, naquele passado distante,\nMir proporcionou benefícios incomensuráveis à humanidade.",
    "Explica o papel vital de Mir antes da ruptura bélica."
)
curations[14529] = (
    "C-como é que é?!\nQuer dizer que a Mir nem sempre agiu pelo mal?!",
    "Lyner se choca ao saber que a vilã ancestral nem sempre fora um monstro de ódio."
)
curations[14530] = (
    "Sim. Pelo contrário...\nSem a existência de Mir, a prosperidade da civilização anterior\njamais teria existido.",
    "Shurelia elucida o protagonismo tecnológico de Mir na Primeira Era."
)
curations[14531] = (
    "A humanidade compreendia essa dívida perfeitamente,\ne por essa razão consagrou Mir no Templo de Elemia.",
    "A sacralização de Mir como deusa encarnada pelos humanos gratos."
)
curations[14532] = (
    "...Se a Mir era tão venerada pelas pessoas,\npor que ela se rebelou e cravou suas presas contra a humanidade...?",
    "Lyner busca compreender a tragédia que converteu a deusa venerada em algoz."
)
curations[14533] = (
    "Porque, enquanto era aclamada como \"deusa\" na fachada pública,\nnos bastidores sofria os mais cruéis abusos e humilhações.",
    "Shurelia expõe a hipocrisia e a crueldade da exploração humana sobre as Reyvateils."
)
curations[14534] = (
    "Você tem um coração puro e gentil, Lyner...\nTalvez seja doloroso demais para você conceber tamanha maldade.",
    "Shurelia pondera com melancolia maternal sobre a nobreza de espírito de Lyner."
)
curations[14535] = (
    "A arquitetura corrompida daquele mundo,\nforjada a partir das fraquezas e covardias do coração humano...",
    "Diagnóstico filosófico sobre o declínio moral da civilização pretérita."
)
curations[14536] = (
    "Mesmo sabendo disso... você ainda deseja ouvir o que se sucedeu na época de Mir?",
    "Shurelia oferece a verdade histórica solene, testando a determinação do jovem."
)
curations[14537] = (
    "S-sim... com certeza.",
    "Lyner reafirma sua firme disposição de conhecer as raízes da guerra."
)
curations[14538] = (
    "Houve uma era dourada em que humanos e Reyvateils coexistiam em perfeita harmonia.",
    "Prólogo da crônica histórica contada por Shurelia."
)
curations[14539] = (
    "Contudo, à medida que a população das Reyvateils florescia,\numa inquietação silenciosa começou a brotar no seio da humanidade.",
    "O despertar da paranoia e do medo existencial entre os humanos."
)
curations[14540] = (
    "O pavor de que as Reyvateils, dotadas de um poder muito superior ao dos mortais,\nse tornassem as soberanas absolutas deste mundo.",
    "A origem do preconceito de dominação baseado no medo da superioridade mágica."
)
curations[14541] = (
    "A humanidade então transformou sua postura:\nem vez de coexistência pacífica, adotou a subjugação implacável.",
    "A virada política que instituiu a escravidão e o controle das Reyvateils."
)
curations[14542] = (
    "E foi precisamente sob essa atmosfera sombria...\nque Mir veio ao mundo.",
    "O nascimento de Mir inserido no auge da opressão sistêmica."
)
curations[14543] = (
    "Projetada para agir unicamente sob o comando humano.\nUma Reyvateil sem ego, privada de senciência ou vontade própria.",
    "A especificação cibernética original de Mir como ferramenta desalmada."
)
curations[14544] = (
    "Todavia...\nMir começou a desenvolver a própria consciência.",
    "O milagre trágico do despertar do livre-arbítrio em Mir."
)
curations[14545] = (
    "Brotaram nela uma fúria ardente contra a humanidade que a escravizava\ne uma piedade imensa pelo sofrimento de suas irmãs Reyvateils.",
    "As duas forças motoras da revolta de Mir: indignação moral e empatia por sua espécie."
)
curations[14546] = (
    "Mir rompeu a submissão aos humanos\ne, conclamando as demais Reyvateils ao seu lado,\niniciou a guerra total.",
    "A deflagração da insurreição armada das Reyvateils lideradas por Mir."
)
curations[14547] = (
    "Essa tragédia monumental não foi outra senão a Guerra das Reyvateils,\nque aniquilou metade do planeta e extinguiu setenta por cento de toda a população.",
    "Fixa os números canônicos e o título do conflito: Guerra das Reyvateils (レーヴァテイル戦争)."
)
curations[14548] = (
    "A partir daquele momento, o ódio de Mir apenas se multiplicou,\naté se cristalizar na determinação de exterminar toda a raça humana.",
    "A escalada do trauma em fanatismo genocida."
)
curations[14549] = (
    "Como uma vingança inexorável contra a humanidade que a gerou daquela forma,\nque a acorrentou e a submeteu aos mais vis tormentos.",
    "A consumação do ciclo de vingança contra os criadores opressores."
)
curations[14550] = (
    "...Então foi essa a tragédia que aconteceu no passado...",
    "Lyner absorve a revelação em silêncio compenetrado, compreendendo a dimensão trágica de Mir."
)

print(f"Total curated entries defined: {len(curations)}")
assert len(curations) == 208, f"Expected 208, got {len(curations)}"

# Build output structures
curated_lines = []
enriched_dialogues = []

glossary_additions = {
    "Fire Shot": {
        "pt": "Tiro Ígneo",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia Verde / Cosmosphere",
        "note": "Primeira Magia Verde de campo tecida na mente de Aurica sob forma de uma pequena esfera falante (JP 火炎弾)."
    },
    "Water God": {
        "pt": "Gota Divina",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia Vermelha / Cosmosphere",
        "note": "Magia Vermelha ofensiva elemental aquática tecida na Cosmosfera de Misha (JP 雫神)."
    },
    "Neo Temple of Elemia": {
        "pt": "Neo-Templo de Elemia",
        "gender": "masculino",
        "number": "singular",
        "category": "Topônimo / Templo Sagrado",
        "note": "O mais monumental santuário histórico consagrado ao culto de Elemia e às suas Deusas ancestrais (JP ネオ・エレミア神殿)."
    },
    "War of the Reyvateils": {
        "pt": "Guerra das Reyvateils",
        "gender": "feminino",
        "number": "singular",
        "category": "História / Conflito Ancestral",
        "note": "Guerra deflagrada por Mir contra a humanidade que destruiu metade do mundo e dizimou 70% da população (JP レーヴァテイル戦争)."
    }
}

hard_gate_errors = 0
lint_warnings = 0

for d in input_data["dialogues"]:
    item_id = d["id"]
    orig_jp = d["original_jp"]
    orig_en = d["original_en"]
    
    if item_id not in curations:
        print(f"[MISSING ID] {item_id}")
        continue
    
    trad, rationale = curations[item_id]
    
    # Validation checks
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
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_gate_errors += 1
        
    parts = trad.split("\n")
    for line_part in parts[1:]:
        if line_part.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_gate_errors += 1
            
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1
        
    curated_lines.append({
        "id": item_id,
        "ptbr_curated": trad,
        "rationale": rationale
    })
    
    enriched_d = dict(d)
    enriched_d["curated_ptbr"] = trad
    enriched_d["final_ptbr"] = trad
    enriched_d["texto_ptbr_curado"] = trad
    enriched_d["custom_text"] = trad
    enriched_d["ptbr_curated"] = trad
    enriched_d["review_status"] = "approved"
    enriched_d["reviewed"] = True
    enriched_d["notes"] = rationale
    enriched_d["curation_notes"] = rationale
    enriched_dialogues.append(enriched_d)

print(f"\nPre-Validation Summary:")
print(f"Total lines: {len(curated_lines)}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

output_dict = {
    "block_id": "BLK_EVD_062",
    "axis_id": input_data.get("axis_id", "AXIS_3"),
    "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
    "category": input_data.get("category", "Event Dialogue"),
    "line_count": len(curated_lines),
    "id_range": [curated_lines[0]["id"], curated_lines[-1]["id"]],
    "curated_lines": curated_lines,
    "glossary_additions": glossary_additions,
    "dialogues": enriched_dialogues
}

if hard_gate_errors == 0 and lint_warnings == 0:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_dict, f, ensure_ascii=False, indent=2)
    print(f"\n[SUCCESS] Successfully written {OUTPUT_PATH}")
else:
    print("\n[FAILED] Errors/warnings detected! Correct before writing output.")
    sys.exit(1)

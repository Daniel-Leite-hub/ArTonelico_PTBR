# -*- coding: utf-8 -*-
"""
generate_blk084.py - Script de curadoria editorial de excelência para BLK_EVD_084.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

INPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_084_input.json")
OUTPUT_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_084_output.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

curated_map = {}

# Event 1: Event/154.evd (18913 - 18958)
curated_map[18913] = {
    "ptbr": "Então o dito Apóstolo de Elemia...\né você?",
    "notes": "Flute indaga Lyner com solenidade e ceticismo ancestral."
}
curated_map[18914] = {
    "ptbr": "Sim. Sou Lyner Barsett,\no Apóstolo de Elemia.",
    "notes": "Lyner se apresenta formalmente perante o ancião de Em Pheyna."
}
curated_map[18915] = {
    "ptbr": "Sou Flute Ross Loria,\no ancião de Em Pheyna.",
    "notes": "Flute se apresenta com autoridade como líder dos Teru."
}
curated_map[18916] = {
    "ptbr": "Serei direto com você.\nNão posso confiar que seja\no «Apóstolo de Elemia».",
    "notes": "Flute rejeita prontamente a reivindicação de Lyner."
}
curated_map[18917] = {
    "ptbr": "Se afirma ser mesmo o Apóstolo de Elemia,\nprove submetendo-se à [Provação da Lua].",
    "notes": "Flute impõe a Provação da Lua para validar a identidade de Lyner."
}
curated_map[18918] = {
    "ptbr": "Outra vez essa história de «provação»?\nVocê não muda esse seu jeito mesmo, Flute.",
    "notes": "Jack intervém com seu tom cínico e familiar característico."
}
curated_map[18919] = {
    "ptbr": "...Harmonica!",
    "notes": "Flute reconhece Jack pelo seu nome ancestral Teru."
}
curated_map[18920] = {
    "ptbr": "Você, que renegou a Tribo Teru...\nque veio fazer aqui depois de tanto tempo?",
    "notes": "Flute confronta Jack pelo abandono de seu povo ancestral."
}
curated_map[18921] = {
    "ptbr": "Hã?! Jack... Você é da Tribo Teru?!",
    "notes": "Lyner expressa espanto genuíno com a revelação da linhagem de Jack."
}
curated_map[18922] = {
    "ptbr": "Não estamos aqui para falar de mim.",
    "notes": "Jack corta o assunto pessoal com pragmatismo áspero."
}
curated_map[18923] = {
    "ptbr": "Mais importante... Pelo visto você nem percebeu\nque a Cantora das Estrelas retornou.",
    "notes": "Jack redireciona o foco para o retorno cerimonial de Misha."
}
curated_map[18924] = {
    "ptbr": "A Cantora das Estrelas?!",
    "notes": "Flute reage chocado com a menção à Cantora das Estrelas."
}
curated_map[18925] = {
    "ptbr": "Há quanto tempo...\nA Cantora das Estrelas, Misha, apresenta seu retorno.",
    "notes": "Misha saúda o ancião com reverência protocolar e solenidade."
}
curated_map[18926] = {
    "ptbr": "Misha...? É você mesma, Misha?!\nMas o que aconteceu com o seu corpo...?",
    "notes": "Flute percebe estarrecido que ela retornou em forma de criança."
}
curated_map[18927] = {
    "ptbr": "Seja como for, cante o Hino...\nEntoe a Chronicle Key!\nO mundo anseia pelo Cântico da Cantora das Estrelas.",
    "notes": "Flute clama com urgência desesperada pelo canto de contenção de Mir."
}
curated_map[18928] = {
    "ptbr": "Peço perdão...\nNo meu estado atual, não sou capaz\nde entoar o Cântico...",
    "notes": "Misha confessa com pesar que perdeu a capacidade de cantar a canção."
}
curated_map[18929] = {
    "ptbr": "C-como disse?!\nNão é capaz de cantar... O que significa isso?!",
    "notes": "Flute entra em desespero perante a revelação da pane vocal."
}
curated_map[18930] = {
    "ptbr": "É que...",
    "notes": "Misha hesita, envergonhada e comovida."
}
curated_map[18931] = {
    "ptbr": "Chega! Estamos com pressa!\nNão temos tempo para ficar perdendo com provações!",
    "notes": "Jack corta a burocracia dos Teru em defesa do grupo."
}
curated_map[18932] = {
    "ptbr": "As coisas não funcionam assim!",
    "notes": "Flute rebate com rigor tradicionalista inabalável."
}
curated_map[18933] = {
    "ptbr": "Tem razão. É como o Flute disse.\nVocê terá que se submeter à provação.",
    "notes": "Tastiella entra em cena ratificando a exigência ritual."
}
curated_map[18934] = {
    "ptbr": "Grande Anciã!",
    "notes": "Flute clama respeitosamente ao avistar Tastiella."
}
curated_map[18935] = {
    "ptbr": "Vovó!",
    "notes": "Jack evoca o apelido afetuoso e atrevido da anciã Teru."
}
curated_map[18936] = {
    "ptbr": "...Parem de me chamar de «vovó» na frente dos convidados.",
    "notes": "Tastiella repreende o apelido na presença de forasteiros com humor cortês."
}
curated_map[18937] = {
    "ptbr": "Misha... Bem-vinda de volta...\nVocê ficou tão pequenina e adorável.",
    "notes": "Tastiella acolhe Misha com ternura materna perante sua nova forma."
}
curated_map[18938] = {
    "ptbr": "Tastiella...\nMe perdoe... Eu...",
    "notes": "Misha expressa remorso perante sua mentora espiritual."
}
curated_map[18939] = {
    "ptbr": "Você não tem pelo que se desculpar.",
    "notes": "Tastiella isenta Misha com serenidade compassiva."
}
curated_map[18940] = {
    "ptbr": "Vejamos... Você é o Lyner, certo?\nÉ a primeira vez que nos encontramos.\nSou Tastiella.",
    "notes": "Tastiella se apresenta elegantemente ao protagonista."
}
curated_map[18941] = {
    "ptbr": "Vovó! Por que o Lyner tem\nque passar por essa provação?!\nNão faz o menor sentido!",
    "notes": "Jack contesta indignado a exigência imposta a Lyner."
}
curated_map[18942] = {
    "ptbr": "Nada de «vovó», Harmonica.\nA provação é necessária porque...\no Lyner é um ser humano.",
    "notes": "Tastiella repreende Jack e expõe a desconfiança histórica contra humanos."
}
curated_map[18943] = {
    "ptbr": "Os humanos são ardilosos e traiçoeiros.\nNão podemos descartar a possibilidade\nde que até você mesmo tenha sido enganado.",
    "notes": "Correção de gênero: Harmonica é homem ('você mesmo'). Alerta sobre a astúcia humana."
}
curated_map[18944] = {
    "ptbr": "...Não pode ser...",
    "notes": "Jack reage incrédulo perante a desconfiança da anciã."
}
curated_map[18945] = {
    "ptbr": "Eu também não aceito isso!\nO Lyner é, de corpo e alma,\no legítimo Apóstolo de Elemia!",
    "notes": "Misha defende Lyner com fervor incondicional e bravura."
}
curated_map[18946] = {
    "ptbr": "Misha... Sinto muito,\nmas no seu estado atual eu também\nnão posso confiar plenamente em você.",
    "notes": "Tastiella expressa a dolorosa cautela que deve manter como líder."
}
curated_map[18947] = {
    "ptbr": "Se não consegue entoar o Cântico,\nhá a possibilidade de você não ser\na verdadeira Misha que conhecemos...",
    "notes": "Tastiella aponta o critério ontológico da voz das Reyvateils Origins."
}
curated_map[18948] = {
    "ptbr": "...Como assim...?",
    "notes": "Misha sofre o impacto emocional de ver sua identidade questionada."
}
curated_map[18949] = {
    "ptbr": "Embora seja chamada de «provação»,\na [Provação da Lua] é bem simples.\nNão levará quase nada de tempo.",
    "notes": "Tastiella ameniza a tensão explicando a brevidade do rito."
}
curated_map[18950] = {
    "ptbr": "Isto é... desde que o Lyner seja mesmo\no verdadeiro Apóstolo de Elemia.",
    "notes": "Tastiella lança o desafio final com ironia refinada."
}
curated_map[18951] = {
    "ptbr": "Eu aceito passar por essa provação!\nPor favor, me diga o que devo fazer!",
    "notes": "Lyner demonstra coragem resoluta e prontidão heroica."
}
curated_map[18952] = {
    "ptbr": "Lyner?!",
    "notes": "Jack se espanta com a aceitação imediata do rapaz."
}
curated_map[18953] = {
    "ptbr": "Se estão dizendo que é obrigatório,\nentão não tenho escolha, né?",
    "notes": "Lyner encara o dever com naturalidade prática desarmante."
}
curated_map[18954] = {
    "ptbr": "Sendo assim, submeta-se à provação.\nDirija-se ao templo.",
    "notes": "Flute convoca o jovem guerreiro ao local sagrado do teste."
}
curated_map[18955] = {
    "ptbr": "Ah, Misha.\nVocê fica aqui.",
    "notes": "Tastiella retém Misha no posto por precaução sagrada."
}
curated_map[18956] = {
    "ptbr": "Misha deixou o grupo.",
    "notes": "Mensagem sistêmica de saída temporária de personagem."
}
curated_map[18957] = {
    "ptbr": "O acesso ao Templo foi liberado!",
    "notes": "Notificação do sistema desbloqueando nova área."
}
curated_map[18958] = {
    "ptbr": "Você pode se deslocar até o Templo\npelo mapa do vilarejo.",
    "notes": "Instrução de navegação no mapa de Em Pheyna."
}

# Event 2: Event/956.evd (18959 - 18995)
curated_map[18959] = {
    "ptbr": "Lyner... Posso entrar?",
    "notes": "Misha bate à porta do quarto de Lyner na estalagem."
}
curated_map[18960] = {
    "ptbr": "Sabe... sobre aquele rito da Instalação...\nSerá que a gente não podia tentar?",
    "notes": "Misha propõe o procedimento íntimo com timidez carinhosa."
}
curated_map[18961] = {
    "ptbr": "O-o quê?!\nDe onde veio isso tão de repente...?",
    "notes": "Lyner reage chocado e encabulado com a proposta súbita."
}
curated_map[18962] = {
    "ptbr": "Não dizem que a Instalação deixa\na Magia da Canção ainda mais poderosa?\nEu quero ficar mais forte para te ajudar!",
    "notes": "Misha justifica sua motivação heroica de apoiar Lyner."
}
curated_map[18963] = {
    "ptbr": "Com certeza vamos conseguir chegar com facilidade\naos lugares inacessíveis agora.",
    "notes": "Misha vislumbra o avanço da jornada com otimismo vibrante."
}
curated_map[18964] = {
    "ptbr": "É verdade, pode até ser, mas...",
    "notes": "Lyner hesita temendo a dor física que ela sentirá."
}
curated_map[18965] = {
    "ptbr": "Eu quero te ajudar, Lyner!\nQuero ficar muito, muito mais forte!\nPor isso... faça a Instalação em mim.",
    "notes": "Misha insiste com fervor e entrega afetuosa."
}
curated_map[18966] = {
    "ptbr": "T-tudo bem... Eu faço.\nMas... tem certeza mesmo?\nNão vai se forçar a algo que não queira?",
    "notes": "Lyner aceita zelando pelo consentimento e bem-estar dela."
}
curated_map[18967] = {
    "ptbr": "Que nada! Estou até empolgada!\nAfinal de contas, disseram que a gente ganha\ntodo tipo de efeito especial.",
    "notes": "Misha disfarça a ansiedade demonstrando entusiasmo lúdico."
}
curated_map[18968] = {
    "ptbr": "Bem... ouvi dizer que dói um pouco na hora\nde inserir, então mentiria se dissesse que não tenho medo...\nPegue leve comigo, tá?...",
    "notes": "Misha admite a vulnerabilidade pedindo delicadeza a Lyner."
}
curated_map[18969] = {
    "ptbr": "T-tá bom. Vou fazer o meu melhor.",
    "notes": "Lyner promete solenemente ter todo o cuidado do mundo."
}
curated_map[18970] = {
    "ptbr": "Obrigada...\nVocê é mesmo muito gentil, Lyner.",
    "notes": "Misha agradece comovida pela ternura do amigo de infância."
}
curated_map[18971] = {
    "ptbr": "Pensando bem...\né a sua primeira vez fazendo uma Instalação, né?\nQue tal tentarmos agora como treino?",
    "notes": "Misha sugere um primeiro teste preliminar no quarto."
}
curated_map[18972] = {
    "ptbr": "Se não tiver nenhum Cristal Grathnode com você,\nuse este aqui. O efeito não é grande coisa,\nmas o dano ao meu corpo também é mínimo.",
    "notes": "Misha entrega um cristal de baixa voltagem para o rito inicial."
}
curated_map[18973] = {
    "ptbr": "Obteve o Cristal Grathnode\n[Canção +10%]!",
    "notes": "Paridade canônica com EVD_082 ID 18519."
}
curated_map[18974] = {
    "ptbr": "Como o atendente do Centro de Mergulho explicou,\na Instalação consiste em inserir\no Cristal Grathnode no meu corpo.",
    "notes": "Misha relembra a teoria mecânica explicada no Centro de Mergulho."
}
curated_map[18975] = {
    "ptbr": "Só que não dá para inserir o cristal\nem qualquer lugar do corpo.",
    "notes": "Misha detalha a restrição fisiológica dos condutores Grathnode."
}
curated_map[18976] = {
    "ptbr": "Toda Reyvateil possui em algum lugar do corpo\num Ponto de Instalação. O cristal reage com essa área\ne se funde à nossa carne.",
    "notes": "Explicação canônica da interface de inserção somática."
}
curated_map[18977] = {
    "ptbr": "O meu fica bem ali, logo acima dos seios.",
    "notes": "Misha revela a localização anatômica de sua porta."
}
curated_map[18978] = {
    "ptbr": "Está vendo aqui...? Dá para ver a tatuagem\nno meu peito...?",
    "notes": "Misha aponta o símbolo heráldico gravado em sua pele."
}
curated_map[18979] = {
    "ptbr": "E-eeh?!\nM-mas será que eu posso ficar olhando assim...?!",
    "notes": "Lyner se atrapalha com o pudor juvenil diante do corpo dela."
}
curated_map[18980] = {
    "ptbr": "Nossa! Que tarado!\nNão é como se eu estivesse mostrando os peitos pra você!...\nFrancamente...",
    "notes": "Misha dá bronca fofa e corada no constrangimento de Lyner."
}
curated_map[18981] = {
    "ptbr": "D-desculpa...",
    "notes": "Lyner pede desculpas desajeitadas morrendo de vergonha."
}
curated_map[18982] = {
    "ptbr": "Então esta marca no peito... é a tatuagem.",
    "notes": "Lyner observa o circuito sonoro gravado na epiderme de Misha."
}
curated_map[18983] = {
    "ptbr": "Esse é o meu Ponto de Instalação.\nVê aquele círculo no centro do desenho?\nSe encostar o Cristal Grathnode ali, ele é absorvido.",
    "notes": "Misha instrui com precisão sobre o ponto de contato do cristal."
}
curated_map[18984] = {
    "ptbr": "Pode tentar.",
    "notes": "Misha encoraja Lyner a iniciar o procedimento."
}
curated_map[18985] = {
    "ptbr": "Ao realizar a Instalação,\né possível atribuir efeitos especiais à Magia da Canção.",
    "notes": "Tutorial do sistema elucidando as vantagens de combate."
}
curated_map[18986] = {
    "ptbr": "Por exemplo, ao instalar um Cristal Grathnode\nque conceda «Envenenar» em uma canção de dano simples,\nela passará a causar dano venenoso.",
    "notes": "Exemplo didático do acréscimo de propriedades elementais/status."
}
curated_map[18987] = {
    "ptbr": "Faça a Instalação e experimente utilizar\nessas Magias da Canção em combate.",
    "notes": "Recomendação tática de aplicação em batalha."
}
curated_map[18988] = {
    "ptbr": "Ufa... Foi bem mais exaustivo\ndo que eu imaginava...\nFiquei esgotada.",
    "notes": "Misha exala cansaço. Correção de gênero contra rascunho amador ('cansado' -> feminina)."
}
curated_map[18989] = {
    "ptbr": "Você está bem?\nPor acaso... doeu muito?",
    "notes": "Lyner demonstra alívio e preocupação protetora."
}
curated_map[18990] = {
    "ptbr": "B-bom... só uma pontadinha.\nMas foi a primeira vez de nós dois.\nCom o tempo a gente descobre um jeito que não doa nada.",
    "notes": "Misha conforta Lyner com cumplicidade otimista."
}
curated_map[18991] = {
    "ptbr": "Acabei te fazendo sofrer... me desculpe.",
    "notes": "Lyner lamenta com sincera compaixão o desconforto dela."
}
curated_map[18992] = {
    "ptbr": "Não, que isso! A decisão foi minha.\nSe for você quem fizer isso por mim, eu aguento firme!\nConto com você daqui para frente, tá?",
    "notes": "Misha sela a promessa mútua de confiança incondicional."
}
curated_map[18993] = {
    "ptbr": "A [Instalação] em Misha\njá está disponível!",
    "notes": "Correção canônica crucial: o script em inglês dizia erroneamente 'Aurica'; o original japonês especifica 'ミシャに'."
}
curated_map[18994] = {
    "ptbr": "O tópico [Instalação] foi adicionado ao menu de Ajuda.",
    "notes": "Aviso de novo verbete de sistema desbloqueado."
}
curated_map[18995] = {
    "ptbr": "Você pode consultar este guia a qualquer momento\nno menu Ajuda, em «Como Jogar».",
    "notes": "Orientações para revisão das regras de mecânica."
}

# Event 3: Event/345.evd (18996 - 19021)
curated_map[18996] = {
    "ptbr": "Esta câmara...!",
    "notes": "Lyner reage ao entrar no recinto secreto dos monstros alados."
}
curated_map[18997] = {
    "ptbr": "O quê?!",
    "notes": "Radolf se põe em guarda em reação ao perigo repentino."
}
curated_map[18998] = {
    "ptbr": "O que um dragão alado está fazendo num lugar desses?!",
    "notes": "Lyner se espanta com a presença da fera no ninho."
}
curated_map[18999] = {
    "ptbr": "Bem, esta ilha inteira é um ninho de dragões alados.\nNão é de surpreender que haja um aqui.",
    "notes": "Radolf analisa a ecologia local com serenidade marcial."
}
curated_map[19000] = {
    "ptbr": "Ufa... Que susto!",
    "notes": "Lyner respira aliviado após a batalha/surpresa."
}
curated_map[19001] = {
    "ptbr": "Lyner... Olha aquilo ali...",
    "notes": "Aurica avista um brilho deslumbrante no fundo do covil."
}
curated_map[19002] = {
    "ptbr": "Não pode ser...!",
    "notes": "Lyner reconhece a preciosidade reluzente diante de seus olhos."
}
curated_map[19003] = {
    "ptbr": "Então este é o Cristal Hymmnos...\n«Linker»...",
    "notes": "Radolf identifica o sagrado Cristal Hymmnos Linker procurado pela Igreja."
}
curated_map[19004] = {
    "ptbr": "O cristal que a Igreja mobilizou todas as suas forças\npara encontrar...",
    "notes": "Radolf rememora a magnitude da busca eclesiástica."
}
curated_map[19005] = {
    "ptbr": "É lindo...",
    "notes": "Aurica contempla a pureza resplandecente do cristal com fascínio."
}
curated_map[19006] = {
    "ptbr": "Dizem que os dragões alados têm o hábito de juntar coisas reluzentes.\nEle deve ter sido atraído pelo brilho do cristal.",
    "notes": "Radolf explica o instinto acumulador da fera mítica."
}
curated_map[19007] = {
    "ptbr": "Aurica...\nPegue o cristal...",
    "notes": "Lyner convida Aurica a acolher o artefato que lhe foi destinado."
}
curated_map[19008] = {
    "ptbr": "...",
    "notes": "Aurica hesita paralisada por traumas do passado."
}
curated_map[19009] = {
    "ptbr": "Se eu tocar nele... pode ser que algo terrível aconteça de novo...",
    "notes": "O pavor de atrair maldições e tragédias ressurge no coração de Aurica."
}
curated_map[19010] = {
    "ptbr": "Não se preocupe.\nNão vai acontecer nada de ruim.",
    "notes": "Lyner dissipa as sombras do medo com sua confiança reconfortante."
}
curated_map[19011] = {
    "ptbr": "Com certeza. Foi a você, Aurica,\nque este cristal foi concedido.",
    "notes": "Radolf reafirma a bênção e o direito legítimo da donzela."
}
curated_map[19012] = {
    "ptbr": "...\nÉ verdade, né?...\nVai ficar tudo bem...",
    "notes": "Aurica encontra refúgio nas palavras dos companheiros e ganha coragem."
}
curated_map[19013] = {
    "ptbr": "Lyner... Eu...\nencontrei o Cristal Hymmnos...",
    "notes": "Aurica balbucia tomada de emoção ao tocar no artefato."
}
curated_map[19014] = {
    "ptbr": "O Cristal Hymmnos que ninguém mais\nconseguiu encontrar...",
    "notes": "A superação de sua autoimagem de inutilidade se concretiza no feito."
}
curated_map[19015] = {
    "ptbr": "Parabéns, Aurica.",
    "notes": "Lyner parabeniza a jovem com ternura calorosa."
}
curated_map[19016] = {
    "ptbr": "Meus parabéns!",
    "notes": "Radolf expressa orgulho pelo triunfo de sua protegida."
}
curated_map[19017] = {
    "ptbr": "É uma grande bênção.",
    "notes": "Ayatane corrobora a celebração com elegância serena."
}
curated_map[19018] = {
    "ptbr": "Gente... muito obrigada...",
    "notes": "Aurica verte lágrimas de pura gratidão perante a afeição de todos."
}
curated_map[19019] = {
    "ptbr": "...Estou tão feliz por estar viva.\nTão feliz... de verdade...",
    "notes": "Ponto alto dramático: a redenção do valor da própria vida perante o trauma do massacre."
}
curated_map[19020] = {
    "ptbr": "Muito obrigada, Lyner...",
    "notes": "Agradecimento direto a quem devolveu a ela a esperança de existir."
}
curated_map[19021] = {
    "ptbr": "Muito bem, vamos voltar para a Igreja!",
    "notes": "Radolf comanda o retorno vitorioso à Catedral."
}

# Event 4: Event/525.evd (19022 - 19050)
curated_map[19022] = {
    "ptbr": "Quem ousa invadir a minha morada sem permissão?!",
    "notes": "Garzburn brada indignado em dialeto arcaico de dragão ancião."
}
curated_map[19023] = {
    "ptbr": "Ah, não... Eu me chamo Lyner.\nVim de uma cidade chamada Platina...",
    "notes": "Lyner tenta acalmar o anfitrião com sinceridade desajeitada."
}
curated_map[19024] = {
    "ptbr": "Meu nome é Garzburn!\nSou o senhor soberano deste «Ninho dos Dragões»!",
    "notes": "O dragão ancestral se apresenta com imponência altiva."
}
curated_map[19025] = {
    "ptbr": "Mas veja só... Ultimamente os humanos\ntêm aparecido por aqui com frequência!",
    "notes": "Garzburn constata a inusitada movimentação de viajantes no pico."
}
curated_map[19026] = {
    "ptbr": "Ainda outro dia mesmo veio um.\nUm sujeito de cabelos prateados.",
    "notes": "Garzburn menciona a visita recente do engenheiro prateado."
}
curated_map[19027] = {
    "ptbr": "Não pode ser... O Luke?!\nPor favor, senhor! O que aconteceu com aquele homem?!",
    "notes": "Krusche perde o fôlego ao reconhecer a descrição de seu amado desaparecido."
}
curated_map[19028] = {
    "ptbr": "Ele disse que a nave havia quebrado\ne ficou hospedado por alguns dias...\nDepois, alçou voo rumo às alturas.",
    "notes": "Garzburn relata a partida audaciosa de Luke em direção ao topo da Torre."
}
curated_map[19029] = {
    "ptbr": "Ah, é mesmo... Ele me pediu para entregar isto\ncaso uma donzela de cabelos alaranjados aparecesse.",
    "notes": "Garzburn entrega o legado deixado para Krusche."
}
curated_map[19030] = {
    "ptbr": "Isto é...!\nA caixa de ferramentas que o Luke guardava como um tesouro...!",
    "notes": "Krusche reconhece o objeto mais precioso de seu parceiro."
}
curated_map[19031] = {
    "ptbr": "Luke...\nQuem diria que eu encontraria os seus passos num lugar destes...",
    "notes": "Krusche expressa comoção profunda com a proximidade dos rastros de Luke."
}
curated_map[19032] = {
    "ptbr": "Lyner, se importa se eu der uma volta lá fora?\nEu queria ficar um pouco sozinha...",
    "notes": "Krusche pede privacidade para processar o impacto emocional em silêncio."
}
curated_map[19033] = {
    "ptbr": "Claro...",
    "notes": "Lyner concede espaço com respeito delicado à dor da amiga."
}
curated_map[19034] = {
    "ptbr": "Quem diria que você encontraria um rastro dele\nnum lugar tão inesperado, Krusche...",
    "notes": "Lyner reflete comovido sobre o destino dos dois inventores."
}
curated_map[19035] = {
    "ptbr": "Pois é! E ainda recentemente teve um bando\nque passou voando aqui perto numa velocidade espantosa!",
    "notes": "Garzburn comenta sobre a passagem vertiginosa de uma aeronave."
}
curated_map[19036] = {
    "ptbr": "...Provavelmente fomos nós...",
    "notes": "Lyner admite sem jeito que eram eles rasgando os céus."
}
curated_map[19037] = {
    "ptbr": "O quê?! Ora, vejam só...",
    "notes": "Garzburn se diverte com a coincidência dos fatos."
}
curated_map[19038] = {
    "ptbr": "...Por acaso vocês não deram de cara\ncom um dragão chamado Sleipnir naquela hora?",
    "notes": "Garzburn indaga sobre o arqui-rival alado."
}
curated_map[19039] = {
    "ptbr": "Ah... Sim. Acabamos derrotando ele, mas...",
    "notes": "Lyner confessa a vitória com receio de represálias."
}
curated_map[19040] = {
    "ptbr": "Como disse?!\nDerrotaram aquele dragão?! Ora, que magnífico!",
    "notes": "Garzburn explode em euforia ao saber da queda de seu adversário."
}
curated_map[19041] = {
    "ptbr": "...?!",
    "notes": "Lyner se espanta com a reação de comemoração do dragão."
}
curated_map[19042] = {
    "ptbr": "Aquele desgraçado foi meu velho rival jurado\npor centenas de anos!",
    "notes": "Garzburn explica a rivalidade de séculos entre as duas criaturas."
}
curated_map[19043] = {
    "ptbr": "E vocês deram cabo dele?!",
    "notes": "Garzburn reafirma seu assombro festivo com a proeza militar."
}
curated_map[19044] = {
    "ptbr": "Hã... rival jurado?!\nNão me diga que a gente fez besteira ao derrotá-lo...?",
    "notes": "Lyner teme ter violado algum laço de honra mística."
}
curated_map[19045] = {
    "ptbr": "Não há com que se preocupar!\nEle e eu duelamos por séculos inteiros\npelo domínio absoluto desta ilha.",
    "notes": "Garzburn tranquiliza o jovem narrando a guerra secular."
}
curated_map[19046] = {
    "ptbr": "Se não precisarei mais me desgastar com essa disputa,\nnada poderia me deixar mais satisfeito!",
    "notes": "Garzburn celebra o fim de um fardo milenar."
}
curated_map[19047] = {
    "ptbr": "...Pois bem, forasteiros.\nDesde eras remotas venho acumulando\ntodo tipo de relíquias e artefatos.",
    "notes": "Garzburn revela seu tesouro particular acumulado por eras."
}
curated_map[19048] = {
    "ptbr": "Guardo aqui heranças da civilização antiga\nque hoje em dia ninguém mais encontra no mundo.",
    "notes": "Garzburn exalta o valor inestimável de seus achados tecnológicos."
}
curated_map[19049] = {
    "ptbr": "Não chega a ser uma recompensa, mas...\nse tiverem interesse, posso lhes vender tudo por um preço justo.",
    "notes": "O dragão mercador oferece acesso ao seu empório exclusivo."
}
curated_map[19050] = {
    "ptbr": "A [Loja de Antiguidades] de Garzburn\njá está disponível!",
    "notes": "Desbloqueio do novo comércio ancestral de itens raros."
}

# Event 5: Event/731.evd (19051 - 19131)
curated_map[19051] = {
    "ptbr": "Achei! É este o gato!",
    "notes": "Aurica localiza o felino espiritual que drena suas forças na Cosmosfera."
}
curated_map[19052] = {
    "ptbr": "Entendi... Então é este gato que está drenando\na energia proveniente da Torre, a sua fonte de poder...",
    "notes": "Lyner deduz a causa da escassez energética de Aurica."
}
curated_map[19053] = {
    "ptbr": "Mas... será que fui eu mesma que criei isso?\nNão me lembro de ter feito uma coisa dessas...",
    "notes": "Aurica não reconhece as projeções involuntárias de seu subconsciente."
}
curated_map[19054] = {
    "ptbr": "(Provavelmente é mais uma daquelas emoções\nda Aurica que se materializou no subconsciente...)",
    "notes": "Lyner compreende a dinâmica psíquica dos mundos mentais."
}
curated_map[19055] = {
    "ptbr": "E como a gente faz para derrotá-lo...?",
    "notes": "Aurica pede orientação prática sobre como combater a criatura."
}
curated_map[19056] = {
    "ptbr": "Boa pergunta...\nNão chegaram a me explicar essa parte...",
    "notes": "Lyner admite sua falta de preparo com bom humor desajeitado."
}
curated_map[19057] = {
    "ptbr": "Eeeh?...\nTenha dó, né?...",
    "notes": "Aurica faz bico decepcionada com a falta de instrução dele."
}
curated_map[19058] = {
    "ptbr": "A culpa é minha agora?!",
    "notes": "Lyner devolve o protesto com indignação bem-humorada."
}
curated_map[19059] = {
    "ptbr": "Ora, vejam só... A mesma duplinha descompassada de sempre.",
    "notes": "A persona de Misha (Presidente do Grêmio) surge destilando sarcasmo."
}
curated_map[19060] = {
    "ptbr": "Você?! É a Misha, a presidente do grêmio estudantil!",
    "notes": "Aurica identifica o arquétipo disciplinar de Misha no colégio cósmico."
}
curated_map[19061] = {
    "ptbr": "Como imaginei... Esse gato foi criação sua, né?\nEle tem bem a sua cara de pamonha.\nIsso atenta contra a moral pública, então trate de dar sumiço nele já!",
    "notes": "Misha persona agride Aurica verbalmente com prepotência arrogante."
}
curated_map[19062] = {
    "ptbr": "(Ué?... A Misha do mundo real\nnão diria uma barbaridade dessas...)",
    "notes": "Lyner nota o exagero caricato e agressivo da projeção mental."
}
curated_map[19063] = {
    "ptbr": "Grrr...!\nA Misha sempre fala com tanto veneno!\nQue ódio!",
    "notes": "Aurica range os dentes frustrada com as provocações da rival."
}
curated_map[19064] = {
    "ptbr": "Não é? Pois é, pois é!\nDá nos nervos, dá nos nervos!",
    "notes": "A persona das sombras de Aurica instiga a discórdia venenosa."
}
curated_map[19065] = {
    "ptbr": "Quem é você?!",
    "notes": "Lyner se sobressalta com a aparição da misteriosa mulher sombria."
}
curated_map[19066] = {
    "ptbr": "O quê?! Quem é você nessa roupa de péssimo gosto?!\nVou ter que te punir por infração ao código escolar!",
    "notes": "A presidente do grêmio tenta enquadrar a recém-chegada nas normas da escola."
}
curated_map[19067] = {
    "ptbr": "Hum... Tem certeza de que quer falar assim comigo?\nEi, Aurica... vou te mostrar uma coisa divertida agora.",
    "notes": "A persona sombria desafia a presidente e seduz Aurica com crueldade lúdica."
}
curated_map[19068] = {
    "ptbr": "Este gato vive sugando a sua energia sem parar, não vive?\nMas o que aconteceria se apontássemos ele\npara esta pirralha arrogante?...",
    "notes": "A sombra propõe transferir o parasita felino para torturar Misha."
}
curated_map[19069] = {
    "ptbr": "Nããão!! O que é isso?! Parem!!\nTem alguma coisa... sendo arrancada de mim!...",
    "notes": "A persona de Misha grita de dor ao ter sua essência vital usurpada."
}
curated_map[19070] = {
    "ptbr": "E aí? Não é uma maravilha dependendo de como se usa?\nEle parou de sugar as suas forças e você ainda se vinga.\nDois coelhos com uma cajadada só.",
    "notes": "A sombra racionaliza o ato cruel como solução ideal de retaliação."
}
curated_map[19071] = {
    "ptbr": "P-peraí, para com isso!!\nEu não quero poder às custas de uma maldade dessas!",
    "notes": "Aurica resiste com repulsa à tentação vil de fazer o mal."
}
curated_map[19072] = {
    "ptbr": "Tem certeza de que pensa assim?\nMesmo sendo eu mesma, esse seu falso moralismo barato\nme dá ânsia de vômito a cada segundo.",
    "notes": "A sombra desmascara a hipocrisia e o puritanismo autoimposto de Aurica."
}
curated_map[19073] = {
    "ptbr": "No fundo do coração, você sempre quis exatamente isso.\nÉ por isso mesmo que o gato continua sugando\nas forças dessa garota sem parar agora.",
    "notes": "A sombra expõe a lei cósmica: a vontade reprimida governa o mundo mental."
}
curated_map[19074] = {
    "ptbr": "É mentira!!",
    "notes": "Aurica nega em desespero o próprio ódio reprimido."
}
curated_map[19075] = {
    "ptbr": "Este lugar é o seu mundo mental, sabia?\nTudo o que acontece ao seu gosto ou contra a sua vontade...\né fruto exclusivo do seu próprio querer.",
    "notes": "A sombra expõe a soberania irrefutável da mente de Aurica na Cosmosfera."
}
curated_map[19076] = {
    "ptbr": "Tudo aqui reflete o que você deseja lá no fundo, não vê?",
    "notes": "O espelho psicológico quebra as defesas de inocência da donzela."
}
curated_map[19077] = {
    "ptbr": "Não é verdade!\nSolte a Misha agora!",
    "notes": "Aurica tenta impor sua ordem consciente para cessar o tormento."
}
curated_map[19078] = {
    "ptbr": "Se você desejasse mesmo «soltar» do fundo da alma,\nele já a teria largado há muito tempo.\nMas você não quer isso de verdade.",
    "notes": "A sombra desmonta a ordem verbal demonstrando a contradição do desejo inconsciente."
}
curated_map[19079] = {
    "ptbr": "Esta pirralha insolente vive te fazendo engolir sapos\nno mundo real, não vive?",
    "notes": "A sombra evoca as mágoas acumuladas dos atritos diários com Misha."
}
curated_map[19080] = {
    "ptbr": "Como, por exemplo, ficar se esfregando e grudando\nno nosso querido Lyner...",
    "notes": "O ciúme amoroso visceral por Lyner vem à tona sem filtros."
}
curated_map[19081] = {
    "ptbr": "Por onde quer que passe, ela sempre rouba a cena\ncom a astúcia e a iniciativa dela...\nUma heroína nata. Uma garota no extremo oposto de nós...",
    "notes": "A amarga sensação de inferioridade estética e social perante a amiga de infância."
}
curated_map[19082] = {
    "ptbr": "...Não...",
    "notes": "Aurica desaba emocionalmente perante as verdades dilacerantes."
}
curated_map[19083] = {
    "ptbr": "Alguém contra quem nós, fracassadas sem talento,\nnão temos como competir... e só nos resta olhar de longe, em silêncio...\nTorcendo para que ela cometa um erro fatal algum dia.",
    "notes": "A confissão do desejo oculto de fracasso alheio, a inveja nua e crua."
}
curated_map[19084] = {
    "ptbr": "Cala a boca!\nNão diga essas coisas na frente do Lyner!!",
    "notes": "O maior pavor de Aurica: ser desmascarada como invejosa aos olhos de seu amado."
}
curated_map[19085] = {
    "ptbr": "Mesmo a essa altura do campeonato,\nvocê ainda quer posar de boazinha para o Lyner, né?\nSendo que, bastará descer mais alguns andares,\ne esconder isso será simplesmente impossível...",
    "notes": "A sombra prenuncia o desnudamento psíquico absoluto nos andares mais profundos."
}
curated_map[19086] = {
    "ptbr": "N-não...!\nLyner, por favor! Não escute mais nada disso!\nNão escute mais sobre mim!! Não olhe para mim!!",
    "notes": "Aurica implora em prantos para que Lyner tape os ouvidos e desvie os olhos de sua vergonha."
}
curated_map[19087] = {
    "ptbr": "Ora, veja só... Agora o Lyner vai te detestar.\nMas pensando bem... isso também pode ser bem divertido.",
    "notes": "A crueldade cínica da sombra regozijando-se com a ruína afetiva."
}
curated_map[19088] = {
    "ptbr": "Eu jamais odiaria você por uma coisa dessas, Aurica.\nMais do que isso... fico feliz de verdade\npor você abrir o seu coração assim para mim.",
    "notes": "Momento ápice de empatia heroica: Lyner acolhe a escuridão de Aurica sem julgamentos."
}
curated_map[19089] = {
    "ptbr": "...Hã?!... Não pode ser... Mentira...",
    "notes": "A sombra fica estarrecida com o amor incondicional demonstrado por Lyner."
}
curated_map[19090] = {
    "ptbr": "Desde o dia em que nos conhecemos,\neu vivia me perguntando sobre você. Por que vive em silêncio?\nO que será que passa pela cabeça da Aurica?... ",
    "notes": "Lyner expressa o desejo constante que sempre teve de conhecê-la por inteiro."
}
curated_map[19091] = {
    "ptbr": "Mas agora que consegui enxergar um pedacinho disso...\nsinto que nós nos aproximamos um pouco mais.",
    "notes": "A vulnerabilidade compartilhada como ponte definitiva para a intimidade afetiva."
}
curated_map[19092] = {
    "ptbr": "Mas... eu sou uma mulher que guarda podridões assim\nno fundo do peito, sabia?...\nMesmo sabendo disso... você ainda...",
    "notes": "Aurica não acredita que ainda possa ser amada e aceita com seus defeitos humanos."
}
curated_map[19093] = {
    "ptbr": "A gente quase nunca fala em voz alta,\nmas eu mesmo já tive pensamentos mesquinhos assim várias vezes...\nPor isso, não esquenta a cabeça com isso.",
    "notes": "Lyner normaliza os sentimentos sombrios com humildade fraterna."
}
curated_map[19094] = {
    "ptbr": "Na verdade, fico até aliviado ao ver que a Aurica\ntambém é uma pessoa de carne e osso,\nque chora e sorri como todo mundo.",
    "notes": "A celebração da humanidade real da donzela em vez de um pedestal inalcançável."
}
curated_map[19095] = {
    "ptbr": "...Lyner... Muito obrigada...\nSuas palavras me deram tanta coragem...",
    "notes": "Aurica renasce das cinzas da vergonha sustentada pelo carinho de Lyner."
}
curated_map[19096] = {
    "ptbr": "Muito bem. Já suguei bastante energia,\nentão toma aqui de presente para você.",
    "notes": "A sombra tenta uma cartada final oferecendo o poder ilícito drenado de Misha."
}
curated_map[19097] = {
    "ptbr": "...Eu não quero essa porcaria...",
    "notes": "Aurica rejeita o poder corrompido com firmeza e desprezo."
}
curated_map[19098] = {
    "ptbr": "...Hum. É mesmo?",
    "notes": "A sombra reage surpresa com a recusa decidida."
}
curated_map[19099] = {
    "ptbr": "Eu não preciso esmolar poder de alguém como você!\nEu mesma sou capaz de ficar mais forte por conta própria!!",
    "notes": "A proclamação triunfal de autonomia, dignidade e autoconfiança de Aurica."
}
curated_map[19100] = {
    "ptbr": "O quê?!... Isso é...!!",
    "notes": "Lyner pressente o surgimento de um fenômeno luminoso cósmico."
}
curated_map[19101] = {
    "ptbr": "Olá a todos! Nos encontramos novamente.",
    "notes": "O espírito da Magia Booster se materializa em cena."
}
curated_map[19102] = {
    "ptbr": "Você é... Aquele que conhecemos antes!!",
    "notes": "Lyner reconhece a entidade cósmica de andares anteriores."
}
curated_map[19103] = {
    "ptbr": "Exatamente, sou eu mesmo!\nContudo, o meu papel agora é bem diferente daquela ocasião.\nChegou a hora de liberar o meu poder em prol da senhorita Aurica!",
    "notes": "A entidade anuncia sua prontidão para servir ao crescimento da donzela."
}
curated_map[19104] = {
    "ptbr": "A razão da minha existência é a inovação. A ruptura dos limites.\nO motivo de eu ter me materializado agora é que a senhorita Aurica\ndecidiu do fundo da alma que vai mudar de verdade.",
    "notes": "A metafísica cósmica da Magia Booster: a superação da estagnação psíquica."
}
curated_map[19105] = {
    "ptbr": "E sou capaz de multiplicar a força da senhorita Aurica\nem várias vezes, agindo a partir do seu interior!",
    "notes": "A descrição da mecânica do Booster ampliando a potência das canções."
}
curated_map[19106] = {
    "ptbr": "...De verdade?!\nFui eu que... teci essa magia?!",
    "notes": "Aurica se maravilha com a própria capacidade de tecer algo grandioso sem atalhos vis."
}
curated_map[19107] = {
    "ptbr": "Precisamente! Porém, há um detalhe:\neu sou uma existência tão efêmera que desaparecerei\nno instante em que o seu coração vacilar.",
    "notes": "O espírito alerta sobre a vulnerabilidade intrínseca à insegurança emocional."
}
curated_map[19108] = {
    "ptbr": "Eu só consigo me manifestar quando você acreditar,\ndo fundo da alma, que é capaz e que possui força de sobra.\nTenha isso sempre em mente!",
    "notes": "A condição de manutenção do Booster: a fé inabalável em si mesma."
}
curated_map[19109] = {
    "ptbr": "...Entendido!",
    "notes": "Aurica aceita o desafio de manter a firmeza no coração."
}
curated_map[19110] = {
    "ptbr": "Quem diria que você teceria algo assim...",
    "notes": "A sombra admite com desagrado o despertar genuíno da donzela."
}
curated_map[19111] = {
    "ptbr": "Não me importa o quanto você seja uma versão superior de mim!\nA nossa maneira de pensar é fundamentalmente oposta!\nSaia já daqui!",
    "notes": "Aurica expulsa sua sombra maligna com coragem e autoridade moral."
}
curated_map[19112] = {
    "ptbr": "Ora, veja só... Bastou tecer uma única magiazinha decente\npara empinar o nariz desse jeito, né?\nQue garota interesseira.",
    "notes": "A sombra zomba da altivez recém-descoberta com veneno ressentido."
}
curated_map[19113] = {
    "ptbr": "Mas essa história de que pensamos de forma oposta...\né uma ilusão absoluta. Mais cedo ou mais tarde você vai ver.",
    "notes": "A advertência sinistra de que a escuridão ainda habita o fundo de sua alma."
}
curated_map[19114] = {
    "ptbr": "Bem, de qualquer forma, vou deixar este gato aqui.\nPode fazer o que quiser com ele agora.\nAté a próxima!",
    "notes": "A sombra se despede deixando para trás a criatura insaciável."
}
curated_map[19115] = {
    "ptbr": "U-uh... ah... As minhas forças...\nEu... não aguento mais...",
    "notes": "A persona de Misha desfalecendo pela drenagem de energia."
}
curated_map[19116] = {
    "ptbr": "Misha!!",
    "notes": "Lyner corre aflito para socorrer a amiga exausta."
}
curated_map[19117] = {
    "ptbr": "Misha!!\nMeu Deus!... O que eu faço?!",
    "notes": "Aurica se desespera com o estado crítico da rival."
}
curated_map[19118] = {
    "ptbr": "Temos que fazer este gato devolver a energia dela agora mesmo!...",
    "notes": "Lyner comanda a ação urgente de resgate das forças roubadas."
}
curated_map[19119] = {
    "ptbr": "...Carga máxima concluída!",
    "notes": "O gato felino profere sua frase de saciedade energética."
}
curated_map[19120] = {
    "ptbr": "Ah! O g-gato!!",
    "notes": "Aurica aponta a fuga iminente da criatura repleta de energia."
}
curated_map[19121] = {
    "ptbr": "Atrás dele!",
    "notes": "Lyner dispara na perseguição do animal espectral."
}
curated_map[19122] = {
    "ptbr": "Misha... me perdoe... Você ficou assim por minha culpa...\nVou recuperar as suas forças e trazer de volta, custe o que custar!",
    "notes": "Aurica faz um juramento sincero de salvação perante a Misha desmaiada."
}
curated_map[19123] = {
    "ptbr": "Você teceu a Magia Azul «Booster»!",
    "notes": "Notificação canônica de criação da Magia Azul Booster."
}
curated_map[19124] = {
    "ptbr": "E aí? Não é uma maravilha dependendo de como se usa?\nEle parou de sugar as suas forças e você ainda se vinga.\nDois coelhos com uma cajadada só.",
    "notes": "Ramificação de falha: a proposta vil é repetida seduzindo a fraqueza de Aurica."
}
curated_map[19125] = {
    "ptbr": "...É verdade.\nE a Misha vai sumir também...",
    "notes": "Aurica capitula perante a tentação mórbida da vingança egoísta."
}
curated_map[19126] = {
    "ptbr": "Espere aí! Você acha certo fazer isso?!",
    "notes": "Lyner tenta intervir em choque ao ver Aurica corrompida pela maldade."
}
curated_map[19127] = {
    "ptbr": "Aquele gato ficou sugando as minhas forças até agora!\nEu quero que a Misha sinta na pele essa mesma agonia!",
    "notes": "Aurica explode em rancor e desejo cego de retribuição sádica."
}
curated_map[19128] = {
    "ptbr": "O quê?! Mas foi você mesma que deu à luz a esse gato!\nA Misha não tem nada a ver com isso!",
    "notes": "Lyner tenta puxá-la de volta à razão com a verdade dos fatos."
}
curated_map[19129] = {
    "ptbr": "Então você está do lado da Misha, Lyner...\nTudo bem. Nesse caso... vou drenar você juntinho com ela!",
    "notes": "A fúria ciumenta de Aurica se volta contra Lyner em delírio destrutivo."
}
curated_map[19130] = {
    "ptbr": "Uaaargh!... As minhas forças... estão se esvaindo\nnuma velocidade assustadora...",
    "notes": "Lyner é atacado pelo parasita espiritual e perde sua vitalidade em agonia."
}
curated_map[19131] = {
    "ptbr": "Eu... não aguento mais...\nNão consigo enxergar nada...",
    "notes": "Fim trágico da ramificação de recusa: colapso sensorial e expulsão do mergulho."
}

print(f"Total curated lines mapped: {len(curated_map)}")
assert len(curated_map) == 219, f"Expected 219 lines, got {len(curated_map)}"

# Run through validador_editorial
hard_errors = 0
lint_warnings = 0

for item in input_data["dialogues"]:
    item_id = item["id"]
    orig_jp = item["original_jp"]
    entry = curated_map[item_id]
    trad = entry["ptbr"]
    
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig_jp,
        traduzido=trad,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {item_id}: {e}")
            
    # Check for \r
    if "\r" in trad:
        print(f"[ERROR] ID {item_id}: Contains \\r carriage return!")
        hard_errors += 1

    # Check orphan line start with punctuation after \n
    parts = trad.split("\n")
    for line_part in parts[1:]:
        line_strip = line_part.strip()
        if line_strip.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {item_id}: Line starts with orphan punctuation after newline: {line_part!r}")
            hard_errors += 1
        if line_part.startswith("..."):
            print(f"[ERROR] ID {item_id}: Line starts with reticências after newline: {line_part!r}")
            hard_errors += 1

    # Check syntactic fracture before \n
    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {item_id}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_errors += 1

    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {item_id}: {a}")

print(f"\nValidation Summary: Hard Errors = {hard_errors}, Lint Warnings = {lint_warnings}")

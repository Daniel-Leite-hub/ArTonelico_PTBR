# -*- coding: utf-8 -*-
"""Script gerador e validador da curadoria editorial do bloco BLK_EVD_026."""

import json
import sys
from pathlib import Path

# Adiciona o diretório de ferramentas ao sys.path para importar o validador oficial
sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\tools")
from curadoria_validate import validate_batch, validate_line

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_026_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_026_output.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

raw_dialogues = input_data["dialogues"]
assert len(raw_dialogues) == 215, f"Esperado 215 falas, obtido {len(raw_dialogues)}"

curations = {
    # =========================================================================
    # EVENT: Event/886.evd (IDs 6566 - 6603) - Reencontro com Spica em Porto Gaivota
    # =========================================================================
    6566: (
        "Sejam bem-vindos~!",
        "rewritten",
        "Acolhimento cantarolado e afável de Spica em sua barraca de doces."
    ),
    6567: (
        "Oi, Spica!\nComo vão os negócios?",
        "rewritten",
        "Quebra eufônica e saudação animada de Misha ao rever a comerciante."
    ),
    6568: (
        "...Ué?\nSerá que a gente já se conhece de algum lugar?",
        "rewritten",
        "Spica semicerra os olhos sem reconhecer a silhueta adulta de Misha."
    ),
    6569: (
        "Oi, Spica.",
        "approved_as_is",
        "Saudação simples, direta e casual de Lyner."
    ),
    6570: (
        "Ora, Lyner!\nJá está acompanhado de outra garota bonita de novo?",
        "rewritten",
        "Alfinetada zombeteira de Spica sugerindo que Lyner trocou de namorada."
    ),
    6571: (
        "N-não fale essas coisas...\nVão acabar achando que sou mulherengo...",
        "rewritten",
        "Lyner desconcertado e na defensiva contra a provocação de Spica."
    ),
    6572: (
        "Poxa, sou eu! Não tá me reconhecendo?\nJá se esqueceu de mim?",
        "rewritten",
        "Indignação fofa e biquinho emburrado de Misha por não ser reconhecida."
    ),
    6573: (
        "...Ué? Agora que você falou,\nparece mesmo que já te vi em algum lugar...",
        "rewritten",
        "Spica finge esforço para puxar pela memória visual."
    ),
    6574: (
        "Isso, isso! Força, faz um esforço!",
        "rewritten",
        "Incentivo empolgado de Misha torcendo pelo reconhecimento."
    ),
    6575: (
        "............",
        "rewritten",
        "Pausa cênica de ponderação com reticências completas."
    ),
    6576: (
        "...Não me diga que... a Misha?!",
        "rewritten",
        "Espanto teatral de Spica desvendando a identidade da amiga."
    ),
    6577: (
        "Na mosca! Que bom que você me reconheceu, Spica!",
        "rewritten",
        "Comemoração vitoriosa e radiante de Misha."
    ),
    6578: (
        "É você mesma, Misha?!\nMas até outro dia você era daquele tamanhinho!",
        "rewritten",
        "Contraste cômico entre a forma infantil recente e o corpo de moça."
    ),
    6579: (
        "Esta é a minha verdadeira forma!\nHehe... Ficou de queixo caído, não ficou?",
        "rewritten",
        "Misha orgulhosa inflando o peito ao exibir sua forma adulta natural."
    ),
    6580: (
        "Nossa, estou boquiaberta.\nFicou uma moça linda, viu~?",
        "rewritten",
        "Elogio afável de Spica mantendo sua pose serena de comerciante."
    ),
    6581: (
        "...S-se bem que, olhando para a sua cara,\nvocê não parece nem um pouco surpresa.",
        "rewritten",
        "Desconfiança aguçada de Misha ao notar o sorriso inabalável de Spica."
    ),
    6582: (
        "É que meu ganha-pão é o sorriso, sabe~?\nMas por dentro estou chocada de verdade.",
        "rewritten",
        "Spica justificando sua expressão com a famosa marca registrada de vendedora."
    ),
    6583: (
        "No fim das contas, parece que você\nsó demorou um pouco para espichar.",
        "rewritten",
        "Provocação de Spica atribuindo a mudança a um simples estirão tardio."
    ),
    6584: (
        "Hã?",
        "approved_as_is",
        "Reação de estranhamento imediato de Misha."
    ),
    6585: (
        "Tem gente que é assim mesmo:\no estirão da puberdade chega atrasado.",
        "rewritten",
        "Explicação pseudocientífica bem-humorada de Spica."
    ),
    6586: (
        "E-ei, espera aí!\nNão tem nada a ver com isso!",
        "rewritten",
        "Misha interrompendo o raciocínio absurdo da amiga."
    ),
    6587: (
        "E quem é assim, basta passar um tempinho sem ver\nque cresce tudo de uma vez até ficar irreconhecível~.",
        "rewritten",
        "Spica insistindo na tese da estirada repentina com tom provocativo."
    ),
    6588: (
        "Mas crescer tanto assim de repente é exagero.\nNão me parece nada saudável.",
        "rewritten",
        "Ironia descarada de Spica fingindo preocupação com a saúde de Misha."
    ),
    6589: (
        "Nada disso! Eu já disse que não tem nada a ver com estirão!\nEsta aqui é quem eu sempre fui!",
        "rewritten",
        "Explosão cômica de Misha aos berros defendendo sua natureza."
    ),
    6590: (
        "Eu não tive atraso nenhum no crescimento,\neu só tinha sido impedida de crescer!",
        "rewritten",
        "Misha esclarecendo que seu corpo havia sido selado à força."
    ),
    6591: (
        "Ora, mas travar o envelhecimento é uma mão na roda.\nFicar jovem é bem melhor.",
        "rewritten",
        "Spica comentando com sabedoria descontraída sobre as vantagens da juventude."
    ),
    6592: (
        "...É verdade. Pensando bem,\ntalvez ser jovem seja bom mesmo...",
        "rewritten",
        "Hesitação e ponderação sincera de Misha quase caindo na lábia da amiga."
    ),
    6593: (
        "Mas não me venha com essa!\nFicar empacada como criança ninguém merece!",
        "rewritten",
        "Misha sacudindo a cabeça e rejeitando a ideia de permanecer pirralha."
    ),
    6594: (
        "Estou brincando. Toma, chupa uma Bala de Gato\npara espantar esse mau humor.",
        "rewritten",
        "Fixação do termo canônico [Bala de Gato] e oferta pacificadora de Spica."
    ),
    6595: (
        "Eu já falei que não sou criança, sou adulta!\nVamos, Lyner, fala alguma coisa também!",
        "rewritten",
        "Misha rejeitando o doce infantil e cobrando apoio moral de Lyner."
    ),
    6596: (
        "F-falar o quê? Assim de repente...",
        "rewritten",
        "Lyner pego de surpresa no meio do fogo cruzado feminino."
    ),
    6597: (
        "...Bom, o corpo dela cresceu,\nmas por dentro ela continua a mesma, então pode ficar tranquila.",
        "rewritten",
        "Lyner tranquilizando Spica com sua costumeira honestidade desajeitada."
    ),
    6598: (
        "...Quer dizer que por dentro continua a mesma pirralha precoce?",
        "rewritten",
        "Spica sintetizando a personalidade sabidinha de Misha (おませさん)."
    ),
    6599: (
        "Já disse que...! Ah, chega, deixa para lá...\nNem eu mesma sei como explicar isso direito...",
        "rewritten",
        "Banimento rigoroso da rubrica *suspiro* e transposição orgânica do cansaço verbal."
    ),
    6600: (
        "E além do mais, só de ter conseguido te deixar surpresa\neu já me dou por satisfeita.",
        "rewritten",
        "Misha se conformando com o objetivo alcançado de causar espanto."
    ),
    6601: (
        "Ufufu... Seja como for,\nque bom que você recuperou a sua verdadeira forma, Misha.",
        "rewritten",
        "Vocalização refinada 'Ufufu...' e carinho genuíno de Spica desfazendo a provocação."
    ),
    6602: (
        "É, obrigada... Ei!\nQuer dizer que você já sabia de tudo esse tempo todo?!",
        "rewritten",
        "Misha caindo na real de que Spica estava apenas zombando dela desde o início."
    ),
    6603: (
        "...Essas duas se dão bem de verdade, hein.",
        "rewritten",
        "Comentário de Lyner admirando a intimidade e cumplicidade das amigas."
    ),

    # =========================================================================
    # EVENT: Event/898.evd (IDs 6604 - 6608) - Informação da Moradora sobre a Embarcação
    # =========================================================================
    6604: (
        "Ei, garoto! Por falar nisso,\ntenho uma novidade fresquinha para você.",
        "rewritten",
        "Abordagem viva e coloquial da moradora do porto (耳寄り情報)."
    ),
    6605: (
        "Novidade fresquinha? Que história é essa?",
        "rewritten",
        "Curiosidade espontânea de Lyner."
    ),
    6606: (
        "Lembra daquela embarcação que atracou no cais\nquando você recuperou o Código Hymmnos da Misha?",
        "rewritten",
        "Menção canônica ao [Código Hymmnos] e ao cais de Porto Gaivota."
    ),
    6607: (
        "Pois saiba que dá para entrar nela!\nSeria uma boa você dar uma passada lá dentro.",
        "rewritten",
        "Dica útil convidando à exploração interna da nave."
    ),
    6608: (
        "Novo destino liberado no mapa: [Interior da Embarcação]!",
        "rewritten",
        "Notificação de sistema com colchetes rigorosamente preservados."
    ),

    # =========================================================================
    # EVENT: Event/325.evd (IDs 6609 - 6626) - Audiência Solene com o Bispo Tastiella
    # =========================================================================
    6609: (
        "Ora, nobre Lyner.\nQuais foram os avanços de vossa jornada desde então?",
        "rewritten",
        "Dicção nobre e cerimoniosa do Patriarca Tastiella acolhendo o cavaleiro."
    ),
    6610: (
        "Na verdade... descobrimos algo espantoso.\nParece que Aurica é a reencarnação da Deusa Tyria.",
        "rewritten",
        "Revelação monumental sobre a identidade divina ancestral de Aurica."
    ),
    6611: (
        "O sagrado Trio de Elemia descendeu\nnas profundezas do coração dela...",
        "rewritten",
        "Terminologia sacra: [Trio de Elemia] e a descida graciosa (光臨)."
    ),
    6612: (
        "...Hã? Mas isso quer dizer...",
        "rewritten",
        "Hesitação e assombro de Aurica absorvendo o peso de sua linhagem."
    ),
    6613: (
        "Afirmaram também que ela é descendente da Deusa Tyria.\nE revelaram até mesmo o paradeiro do [Linker]...",
        "rewritten",
        "Preservação canônica da [Deusa Tyria] e do cristal [Linker]."
    ),
    6614: (
        "O que dissestes?!\nNobre Lyner, podereis me conceder mais detalhes sobre isso?",
        "rewritten",
        "Sobressalto solene do bispo com registro clerical impecável."
    ),
    6615: (
        "......",
        "rewritten",
        "Silêncio reflexivo e calculista de Ayatane em segundo plano."
    ),
    6616: (
        "Que prodígio celestial...!\nComo pode nos ser concedido testemunhar tamanha graça...?",
        "rewritten",
        "Exaltação mística do sacerdote diante do milagre anunciado."
    ),
    6617: (
        "Aurica. Meus olhos jamais me enganaram a vosso respeito.\nÉreis, desde o início, uma jovem guardiã de um poder grandioso.",
        "rewritten",
        "Paternalismo e reconhecimento sagrado do bispo para com Aurica."
    ),
    6618: (
        "Vossa Eminência...",
        "rewritten",
        "Tratamento litúrgico de Aurica ao líder supremo da Igreja de Elemia."
    ),
    6619: (
        "Eu guardava a certeza inabalável\nde que a aurora deste dia finalmente chegaria.",
        "rewritten",
        "Convencimento profético de Tastiella sobre a restauração da Igreja."
    ),
    6620: (
        "Sendo assim, providenciarei de imediato\numa aeronave rumo à [Garra do Falcão].",
        "rewritten",
        "Determinação logística militar e topônimo [Garra do Falcão] protegido."
    ),
    6621: (
        "Rogo que vos empenheis em receber a bênção\ndo Cristal Hymmnos [Linker].",
        "rewritten",
        "Padronização perfeita de [Cristal Hymmnos] e [Linker]."
    ),
    6622: (
        "Abrem-se, enfim, os portais de uma nova era!",
        "rewritten",
        "Proclamação épica e solene da alvorada de Sol Ciel."
    ),
    6623: (
        "......",
        "rewritten",
        "Postura estoica e respeitosa de Radolf ao lado do patriarca."
    ),
    6624: (
        "Nobre Lyner. Rogo que cuideis de Aurica\ncom toda a vossa honra.",
        "rewritten",
        "Incumbência de cavalaria conferida a Lyner pelo sumo sacerdote."
    ),
    6625: (
        "Iniciaremos agora os preparativos da cerimônia de partida.\nNobre Lyner, apresente-se assim que tiver concluído os vossos aprontos.",
        "rewritten",
        "Instrução protocolar para a cerimônia de envio da expedição."
    ),
    6626: (
        "Sim, senhor!",
        "rewritten",
        "Prontidão resoluta e disciplina marcial de Lyner."
    ),

    # =========================================================================
    # EVENT: Event/846.evd (IDs 6627 - 6632) - Sistema de Segurança do Portão A7
    # =========================================================================
    6627: (
        "Aqui é a Divisória de Contenção A7.\nO operador credenciado deve dar um passo à frente.",
        "rewritten",
        "Comando de voz automatizado e impessoal da infraestrutura da Torre."
    ),
    6628: (
        "Autenticação por Espectro FFT confirmada: Lyner Barsett.\nAguardando diretrizes.",
        "rewritten",
        "Terminologia tecnológica de autenticação fônica ancestral [Espectro FFT]."
    ),
    6629: (
        "Liberar a Divisória A7.",
        "rewritten",
        "Ordem operacional direta e clara de Lyner ao sistema."
    ),
    6630: (
        "#0Ma paks ga exec guol A7 al noes.",
        "rewritten",
        "Código Hymmnos sagrado de liberação com tag #0 integralmente restaurado."
    ),
    6631: (
        "Código operacional verificado.",
        "rewritten",
        "Resposta de confirmação de autorização da máquina."
    ),
    6632: (
        "Abertura da divisória em dois segundos.\nStatus: autorização de passagem concedida.",
        "rewritten",
        "Contagem regressiva de segurança da antecâmara."
    ),

    # =========================================================================
    # EVENT: Event/344.evd (IDs 6633 - 6634) - Exploração com Tiro Trovão
    # =========================================================================
    6633: (
        "Então foi aqui que o [Tiro Trovão] acertou.",
        "rewritten",
        "Constatação de Lyner mantendo o nome canônico da munição mágica."
    ),
    6634: (
        "Existem outros mecanismos iguais a este espalhados.\nSeria uma boa disparar um [Tiro Trovão] neles também.",
        "rewritten",
        "Conselho tático perspicaz e ponderado de Ayatane."
    ),

    # =========================================================================
    # EVENT: Event/759.evd (IDs 6635 - 6636) - Entrada no Nível 9 da Cosmosfera
    # =========================================================================
    6635: (
        "Nível 9...",
        "approved_as_is",
        "Contemplação do abismo psicológico mais profundo da Reyvateil."
    ),
    6636: (
        "Tem uma Aurica me esperando lá dentro, é...?\nMuito bem, hora de entrar.",
        "rewritten",
        "Resolução corajosa de Lyner para mergulhar no âmago da alma de Aurica."
    ),

    # =========================================================================
    # EVENT: Event/632.evd (IDs 6637 - 6644) - Reflexão de Misha na Cosmosfera
    # =========================================================================
    6637: (
        "Acho que desta vez acabei te mostrando\num monte de coisas vergonhosas a meu respeito...",
        "rewritten",
        "Vulnerabilidade e timidez de Misha após as provações do nível."
    ),
    6638: (
        "Não tem nada de vergonhoso nisso.\nFoi a primeira vez que te vi explodir de raiva daquele jeito,\nmas você parecia tão cheia de vida.",
        "rewritten",
        "Consolo caloroso e cavalheiresco de Lyner elogiando a vivacidade dela."
    ),
    6639: (
        "N-não sei bem se isso foi um elogio\nou se você tá tirando uma com a minha cara, mas... obrigada.",
        "rewritten",
        "Reação desconcertada e meiga de Misha acolhendo o carinho."
    ),
    6640: (
        "......",
        "rewritten",
        "Silêncio afetuoso entre os amigos de infância."
    ),
    6641: (
        "Uma Mudança de Paradigma... Esta já é a quinta, não é?\nA cada novo salto, tudo o que eu guardava em segredo\nvai transbordando sem parar...",
        "rewritten",
        "Reflexão madura sobre a superação emocional e o desnudamento da alma."
    ),
    6642: (
        "...Da próxima vez, talvez você acabe me detestando de verdade.\nAhaha...",
        "rewritten",
        "Medo latente de rejeição disfarçado sob um risinho nervoso."
    ),
    6643: (
        "Vai dar tudo certo, eu já te disse...\nPode encarar a Mudança de Paradigma de coração tranquilo.",
        "rewritten",
        "Lyner reafirmando sua aceitação incondicional à amiga."
    ),
    6644: (
        "...É verdade.\nEntão... até logo...",
        "rewritten",
        "Despedida suave antes da transição de nível mental."
    ),

    # =========================================================================
    # EVENT: Event/620.evd (IDs 6645 - 6658) - Clímax da Cosmosfera: Quebra do Eu Falso
    # =========================================================================
    6645: (
        "Misha... quando você diz destruir, o que exatamente você quer destruir?",
        "rewritten",
        "Apreensão de Lyner diante da determinação drástica da garota."
    ),
    6646: (
        "A minha versão falsa...",
        "rewritten",
        "Definição concisa e cortante do avatar infantil ilusório."
    ),
    6647: (
        "A falsa Misha...?",
        "rewritten",
        "Eco de espanto de Lyner tentando assimilar a revelação."
    ),
    6648: (
        "Sim. Acho que a mamãe já deve ter te falado...\nEsta que você vê agora, a Misha pequenina, é uma ilusão.",
        "rewritten",
        "Explicação serena e consciente sobre o bloqueio mental imposto."
    ),
    6649: (
        "A verdadeira Misha tem corpo de adulta!\nAfinal de contas, no mundo real eu já tenho dezoito anos!\nNão tem cabimento eu continuar presa nesta forma de criança!",
        "rewritten",
        "Reivindicação apaixonada de sua maturidade física e psicológica."
    ),
    6650: (
        "Por isso eu vou destruir esse meu eu falso!\nJunto com todo esse mundo ilusório que o gerou!",
        "rewritten",
        "Decisão dramática de colapsar o estrato da Cosmosfera para renascer."
    ),
    6651: (
        "E-espera um pouco, Misha!",
        "rewritten",
        "Lyner tentando conter o ímpeto perigoso da amiga."
    ),
    6652: (
        "Quando eu digo que vou destruir, eu destruo!",
        "rewritten",
        "Vontade férrea e indomável de Misha rompendo seus próprios limites."
    ),
    6653: (
        "Uoooh! Que tremor absurdo!\nEste lugar... vai desabar inteiro!",
        "rewritten",
        "Desespero físico diante do terremoto cataclísmico na simulação psíquica."
    ),
    6654: (
        "Não pode ser... Uma Mudança de Paradigma?!",
        "rewritten",
        "Compreensão súbita de que a destruição é o gatilho da evolução."
    ),
    6655: (
        "Exatamente!\nEu já decidi que vou dar adeus a este mundo postiço de uma vez!",
        "rewritten",
        "Expurgo de palavrão indevido da tradução automática, restituindo o grito heroico."
    ),
    6656: (
        "Lyner, eu... estou indo!\nMesmo quando eu me tornar a Misha adulta...\ncontinue sendo para mim o mesmo Lyner de sempre, por favor!",
        "rewritten",
        "Clímax emocional: a súplica pura para que o laço de afeto não mude com o crescimento."
    ),
    6657: (
        "Misha!!",
        "approved_as_is",
        "Grito desesperado de Lyner enquanto a realidade se desfaz."
    ),
    6658: (
        "Uooh...",
        "rewritten",
        "Gemido abafado de Lyner sendo tragado pelo colapso dimensional."
    ),

    # =========================================================================
    # EVENT: Event/108.evd (IDs 6659 - 6664) - Portão Divisor B1 nº 3
    # =========================================================================
    6659: (
        "Aqui é o Portão Divisor B1 nº 3.\nO operador credenciado deve dar um passo à frente.",
        "rewritten",
        "Protocolo formal do mecanismo de barreira da Torre."
    ),
    6660: (
        "Autenticação por Espectro FFT confirmada:\nLyner Barsett. Aguardando diretrizes.",
        "rewritten",
        "Identificação acústica de ondas harmônicas do cavaleiro."
    ),
    6661: (
        "Liberar o Portão Divisor B1 nº 3.",
        "rewritten",
        "Ordem de comando de voz de Lyner."
    ),
    6662: (
        "#0Ma paks ga exec guol B1-iii al noes.",
        "rewritten",
        "Comando de liberação na língua Hymmnos ancestral devidamente preservado."
    ),
    6663: (
        "Código operacional verificado.",
        "rewritten",
        "Validação positiva dos parâmetros fônicos."
    ),
    6664: (
        "Abertura da divisória em dois segundos.\nStatus: autorização de passagem concedida.",
        "rewritten",
        "Sinal sonoro de liberação do trânsito na divisória."
    ),

    # =========================================================================
    # EVENT: Event/423.evd (ID 6665) - Misha manhosa na pousada
    # =========================================================================
    6665: (
        "Ai, bateu um soninho tão bom...\nLyner, a gente não pode dormir juntinho como nos velhos tempos?",
        "rewritten",
        "Doçura travessa e intimidade carinhosa de Misha provocando o amigo."
    ),

    # =========================================================================
    # EVENT: Event/114.evd (IDs 6666 - 6669) - Reativação dos Sistemas e Retorno
    # =========================================================================
    6666: (
        "Funcionou!!",
        "rewritten",
        "Júbilo espontâneo de Lyner ao ver a máquina responder."
    ),
    6667: (
        "Para quem estava chutando sem rumo,\naté que a gente se saiu muito bem, né?",
        "rewritten",
        "Ironia bem-humorada de Misha celebrando o improviso bem-sucedido."
    ),
    6668: (
        "Quem sabe a gente não consiga reativar\nos outros terminais usando esse mesmo método?",
        "rewritten",
        "Otimismo prático de Lyner vislumbrando a solução geral."
    ),
    6669: (
        "De qualquer forma,\nvamos voltar até a gôndola do translado.",
        "rewritten",
        "Orientação de exploração retornando à gôndola (シャトルゴンドラ)."
    ),

    # =========================================================================
    # EVENT: Event/740.evd (IDs 6670 - 6691) - Despedida e Emancipação de Don Leon
    # =========================================================================
    6670: (
        "Achei você! Don Leon!!",
        "rewritten",
        "Lyner alcança o guardião e utiliza a nomenclatura canônica [Don Leon]."
    ),
    6671: (
        "......",
        "rewritten",
        "Silêncio estóico do guerreiro de pelúcia contemplando o horizonte."
    ),
    6672: (
        "Don Leon... Por favor, não me abandone!",
        "rewritten",
        "Desespero aflito de Aurica com medo de perder seu protetor de infância."
    ),
    6673: (
        "Senhorita Aurica... Vós vos lembrais?\nDo dia em que este humilde servo vos encontrou pela primeira vez?",
        "rewritten",
        "Dicção arcaica e nobre de samurai guardião (sessha / Senhorita Aurica)."
    ),
    6674: (
        "Quando Claire me colocou em vossas mãos,\nlembrais do que ela vos disse naquela ocasião?",
        "rewritten",
        "Evocação comovente da memória afetiva de Claire e do massacre de Skuwat."
    ),
    6675: (
        "\"Quando a solidão apertar, olhe para este bichinho de pelúcia,\npense que sou eu e crie coragem\"... Foi o que ela disse.",
        "rewritten",
        "Recordação das palavras de alento de Claire citadas em discurso direto."
    ),
    6676: (
        "Exatamente. Claire costurou este servo e o presenteou\npara servir de esteio ao vosso coração ferido...",
        "rewritten",
        "A missão original de Don Leon como bálsamo psicológico para Aurica."
    ),
    6677: (
        "...Porém, ter um apoio na alma é algo bem diferente\nde viver em dependência absoluta.",
        "rewritten",
        "Lição moral de maturidade distinguindo consolo fraterno de estagnação."
    ),
    6678: (
        "Que a senhorita se apoie cegamente neste servo\ne desista de trilhar os próprios passos...\nisso nem eu nem Claire jamais desejamos.",
        "rewritten",
        "O guardião exortando Aurica a não fugir da realidade nem se anular."
    ),
    6679: (
        "Ver a senhorita erguer a fronte e viver com altivez\npor vossas próprias forças é a única aspiração e o maior júbilo deste servo.",
        "rewritten",
        "Declaração comovente da verdadeira vocação protetora de Don Leon."
    ),
    6680: (
        "Mas... se for assim...\nSe eu aprender a andar com as minhas próprias pernas...\no Don Leon vai se afastar de mim para sempre...!",
        "rewritten",
        "O terror inconsciente de Aurica: acreditar que a cura significa o abandono."
    ),
    6681: (
        "Este servo jamais vos desamparará.\nEsse receio não passa de um fantasma criado por vossa mente.\nComo poderia eu me apartar da Senhorita Aurica...?",
        "rewritten",
        "Don Leon desarmando o fantasma do medo com carinho paterno absoluto."
    ),
    6682: (
        "Por mais independente que vos torneis, ainda que um dia\njulgueis este servo dispensável... eu sempre viverei no vosso coração.",
        "rewritten",
        "Promessa eterna de presença imaterial nos alicerces da alma de Aurica."
    ),
    6683: (
        "Don Leon... Me perdoa... Muito obrigada...",
        "rewritten",
        "Lágrimas de redenção, pedido de desculpas e gratidão de Aurica (flexão feminina)."
    ),
    6684: (
        "Acho que... eu estava me escorando demais no Don Leon.\nO que era para ser um esteio na alma virou dependência sem eu perceber...",
        "rewritten",
        "O despertar da autoconsciência curando a ferida psicológica de infância."
    ),
    6685: (
        "É a Mudança de Paradigma!",
        "rewritten",
        "Constatação eletrizante de Lyner ao ver o salto quântico da Cosmosfera."
    ),
    6686: (
        "O coração da Senhorita Aurica encontrou sua resolução... enfim.\nEla já não dependerá mais deste velho servo.",
        "rewritten",
        "Orgulho melancólico do mentor que cumpriu com bravura o seu papel."
    ),
    6687: (
        "...Bateu uma pontinha de saudade?",
        "rewritten",
        "Sensibilidade afetuosa de Lyner lendo o sentimento secreto do bichinho."
    ),
    6688: (
        "Q-que despropósito insolente!!\nEste servo... sempre permanecerá ao lado da Senhorita Aurica!",
        "rewritten",
        "Don Leon indignado na defensiva com pose épica caricata."
    ),
    6689: (
        "Continuarei a protegê-la para que velhacos atrevidos como vós\nnão inventem gracinhas, e nada mais!",
        "rewritten",
        "Ameaça samurai bem-humorada marcando território contra Lyner."
    ),
    6690: (
        "...Tá certo, tá certo.",
        "rewritten",
        "Lyner rindo e aceitando a implicância costumeira do guardião."
    ),
    6691: (
        "Concebeu a Magia Vermelha [Meu Herói]!",
        "rewritten",
        "Síntese mística de alta magia com colchetes blindados [Meu Herói]."
    ),

    # =========================================================================
    # EVENT: Event/481.evd (IDs 6692 - 6695) - Jack e Lyner diante de Painel Emperrado
    # =========================================================================
    6692: (
        "...Não parece disposto a se mexer.",
        "rewritten",
        "Avaliação cínica e experiente do mercenário veterano."
    ),
    6693: (
        "Deixa eu tentar mexer nos comandos.",
        "rewritten",
        "Iniciativa prática e disposta de Lyner."
    ),
    6694: (
        "......",
        "rewritten",
        "Pausa cênica de esforço inútil nos controles."
    ),
    6695: (
        "...Bora para o próximo.",
        "rewritten",
        "Pragmatismo seco e despojado de Jack cortando a perda de tempo."
    ),

    # =========================================================================
    # EVENT: Event/257.evd (IDs 6696 - 6698) - O Céu se Abre Após a Tempestade
    # =========================================================================
    6696: (
        "Ué? O céu...",
        "rewritten",
        "Krusche notando a mudança repentina da atmosfera lá fora."
    ),
    6697: (
        "Parece que a tempestade deu uma trégua.",
        "rewritten",
        "Jack confirmando o fim da intempérie."
    ),
    6698: (
        "Que alívio!\nAgora as aeronaves já podem decolar de novo.",
        "rewritten",
        "Misha celebrando a retomada dos voos na Torre."
    ),

    # =========================================================================
    # EVENT: Event/208.evd (IDs 6699 - 6705) - Jack nas Docas de Platina
    # =========================================================================
    6699: (
        "E aí, garoto.\nFalta pouco para darmos adeus a Platina, hein.",
        "rewritten",
        "Tom camarada e intimidade cínica de Jack chamando Lyner de garoto."
    ),
    6700: (
        "É bom gravar bem na memória esta vista espetacular...\nDaqui para a frente, o nosso assunto é com a Tenba.",
        "rewritten",
        "Contraste entre a beleza de Platina e o perigo corporativo da Tenba."
    ),
    6701: (
        "Então você vai se juntar à brigada de busca, Jack...",
        "rewritten",
        "Lyner constatando o engajamento do mercenário."
    ),
    6702: (
        "Mas é claro. Afinal de contas,\neu já estava fazendo exatamente isso por conta própria antes.",
        "rewritten",
        "Jack lembrando que sua caçada já era solitária antes de se unirem."
    ),
    6703: (
        "Eu não te disse?\nO objetivo de toda a minha viagem é a Misha.",
        "rewritten",
        "Reafirmação firme do juramento de lealdade e proteção a Misha."
    ),
    6704: (
        "E é óbvio que você também vai se voluntariar para a busca, né?\nBom, como se eu precisasse perguntar.",
        "rewritten",
        "Ironia bem-humorada de Jack reconhecendo a impulsividade heroica de Lyner."
    ),
    6705: (
        "Bom, vou dar uma esticada nas pernas por aí.",
        "rewritten",
        "Despedida casual de andarilho acostumado a bater perna."
    ),

    # =========================================================================
    # EVENT: Event/504.evd (IDs 6706 - 6711) - Barreira de Seguranças da Tenba
    # =========================================================================
    6706: (
        "Daqui em diante é propriedade privada da Tenba.",
        "rewritten",
        "Tom burocrático e intimidador da sentinela corporativa."
    ),
    6707: (
        "A entrada é terminantemente proibida sem a autorização da presidente.",
        "rewritten",
        "Menção direta ao cargo de comando supremo ocupado por Ayano."
    ),
    6708: (
        "...Sem chance por aqui.",
        "rewritten",
        "Percepção rápida de Jack sobre o bloqueio intransponível pela força."
    ),
    6709: (
        "Vamos lá pedir uma autorização direto com a presidente.",
        "rewritten",
        "Krusche propondo a via institucional aproveitando seu prestígio."
    ),
    6710: (
        "Acho que ela liberaria a nossa passagem,\nmas soube que ela vai ficar ausente por uns tempos...",
        "rewritten",
        "Obstáculo narrativo: a ausência temporária de Ayano."
    ),
    6711: (
        "Então é melhor deixar a dona presidente para depois\ne averiguar outras opções primeiro.",
        "rewritten",
        "Reorganização prática da rota de investigação por Jack."
    ),

    # =========================================================================
    # EVENT: Event/199.evd (IDs 6712 - 6714) - Pousada Pública de Platina
    # =========================================================================
    6712: (
        "Esta é a hospedaria pública de Platina.\nNesta cidade, a própria administração municipal cuida dos alojamentos.",
        "rewritten",
        "Worldbuilding detalhado: a gestão comunitária das instalações em Platina."
    ),
    6713: (
        "As construções de Platina têm um ar tão majestoso...\nSão deslumbrantes... e enormes.",
        "rewritten",
        "Deslumbramento tímido de Aurica diante da arquitetura da alta civilização."
    ),
    6714: (
        "Pois é. Se tem uma coisa que sobra aos montes por aqui\né material de construção.",
        "rewritten",
        "Orgulho nativo de Lyner comentando a fartura de recursos de sua terra natal."
    ),

    # =========================================================================
    # EVENT: Event/437.evd (ID 6715) - Exploração no Escuro
    # =========================================================================
    6715: (
        "Nossa, que breu...\nÉ melhor avançar com cuidado.",
        "rewritten",
        "Reação sensorial imediata à escuridão da masmorra."
    ),

    # =========================================================================
    # EVENT: Event/815.evd (IDs 6716 - 6724) - Missão Especial de Resgate na Cosmosfera
    # =========================================================================
    6716: (
        "Muito bem, vamos começar.\nComo a narrativa já vai se iniciar em pleno andamento,\ntome cuidado para não se desorientar, certo?",
        "rewritten",
        "Instruções técnicas de mergulho de Shurelia reconfigurando o ponto de entrada."
    ),
    6717: (
        "...!!",
        "approved_as_is",
        "Choque sensorial na transição abrupta para a mente da Reyvateil."
    ),
    6718: (
        "...Aqui é... uma cafeteria?",
        "rewritten",
        "Lyner reconhecendo o cenário urbano simulado."
    ),
    6719: (
        "Ora? Se não é o cavalheiro de outro dia...\nEm que posso ajudar? A Leila continua ausente...",
        "rewritten",
        "Atendente NPC da simulação dando a pista sobre o sumiço de Leila."
    ),
    6720: (
        "Leila...? É verdade! A Leila!!",
        "rewritten",
        "Reativação súbita da memória de missão na mente de Lyner."
    ),
    6721: (
        "Preciso salvar a Leila...\nMas... o que posso fazer...?",
        "rewritten",
        "Urgência dramática e dilema tático em busca de uma saída."
    ),
    6722: (
        "A esta hora do dia...\nela ainda devia estar em casa.",
        "rewritten",
        "Cálculo cronológico de Lyner desvendando a linha temporal do evento."
    ),
    6723: (
        "De qualquer forma, vou correr para a minha casa.",
        "rewritten",
        "Decisão de rumar ao ponto de partida para interceptar o destino."
    ),
    6724: (
        "E o melhor de tudo: desta vez eu me lembro de tudo do mundo real!\nDeve ser graças à reprogramação que a Senhora Shurelia fez...",
        "rewritten",
        "Conexão diegética: a preservação do livre-arbítrio graças à magia de Shurelia."
    ),

    # =========================================================================
    # EVENT: Event/810.evd (IDs 6725 - 6730) - Fim de Jogo na Cosmosfera (Estudante)
    # =========================================================================
    6725: (
        "Lyner! Você veio por mim...",
        "rewritten",
        "Avatar de estudante da Cosmosfera agradecendo o retorno do cavaleiro."
    ),
    6726: (
        "Não temos mais tempo!\nDepressa...!",
        "rewritten",
        "Pressão de tempo angustiante antes da falha do mergulho."
    ),
    6727: (
        "...Ué? Onde é que eu...",
        "rewritten",
        "Desorientação pós-ejeção ao despertar na cápsula de Dive."
    ),
    6728: (
        "Seja bem-vindo de volta.\nParece que deu Fim de Jogo.",
        "rewritten",
        "Acolhimento sereno e ligeiramente cômico de Shurelia anunciando o insucesso."
    ),
    6729: (
        "Puxa vida...",
        "rewritten",
        "Lamento desconcertado e coçar de cabeça de Lyner (ありゃりゃ...)."
    ),
    6730: (
        "Como você poderá continuar de onde parou da próxima vez,\ntalvez valha a pena tentar de novo quando quiser.",
        "rewritten",
        "Incentivo afável de Shurelia explicando a persistência do checkpoint."
    ),

    # =========================================================================
    # EVENT: Event/786.evd (IDs 6731 - 6736) - Segunda Tentativa e Fim de Jogo
    # =========================================================================
    6731: (
        "Lyner! Você voltou por mim... Muito obrigada!",
        "rewritten",
        "Avatar agradecendo com afeto a insistência e fidelidade de Lyner."
    ),
    6732: (
        "Então vamos lá!",
        "rewritten",
        "Entusiasmo para a nova empreitada na simulação."
    ),
    6733: (
        "...Ué? Onde é que eu...",
        "rewritten",
        "Repetição do despertar atordoado após nova ejeção."
    ),
    6734: (
        "Seja bem-vindo de volta.\nParece que deu Fim de Jogo.",
        "rewritten",
        "A mesma compostura divina de Shurelia comunicando a falha."
    ),
    6735: (
        "Puxa vida... De novo...?",
        "rewritten",
        "Cansaço bem-humorado de Lyner diante da reincidência do tropeço."
    ),
    6736: (
        "Como é possível recomeçar quantas vezes forem necessárias,\ntalvez valha a pena tentar mais uma vez.",
        "rewritten",
        "Paciência infinita da deusa motivando o herói a não desistir."
    ),

    # =========================================================================
    # EVENT: Event/899.evd (IDs 6737 - 6772) - Conversa Íntima entre Shurelia e Lyner
    # =========================================================================
    6737: (
        "Lyner... Eu vim até aqui\nporque gostaria de conversar com você.",
        "rewritten",
        "Aproximação tímida e reservada de Shurelia em busca de um momento a sós."
    ),
    6738: (
        "Senhora Shurelia? Aconteceu alguma coisa?",
        "rewritten",
        "Respeito solene de Lyner diante da administradora da Torre."
    ),
    6739: (
        "B-bem... Lyner... Será que... eu poderia lhe fazer um pedido egoísta?",
        "rewritten",
        "Hesitação e pudor de Shurelia ao ousar expressar um anseio pessoal."
    ),
    6740: (
        "S-sim... claro, pode falar.",
        "rewritten",
        "Prontidão gentil de Lyner incentivando a deusa a se abrir."
    ),
    6741: (
        "É que...",
        "rewritten",
        "A trava da timidez segurando as palavras na garganta."
    ),
    6742: (
        "......",
        "rewritten",
        "Pausa cênica de expectativa respeitosa."
    ),
    6743: (
        "Bem... eu...",
        "rewritten",
        "Nova tentativa relutante de encontrar a coragem necessária."
    ),
    6744: (
        "......",
        "rewritten",
        "Silêncio acolhedor de Lyner dando espaço ao tempo dela."
    ),
    6745: (
        "Gostaria de falar de um jeito comum...\ncomo se fôssemos simples amigos... Eu queria falar assim com você, Lyner.",
        "rewritten",
        "O pedido sincero e puro que desconstrói a barreira entre deusa e mortal."
    ),
    6746: (
        "S-Senhora Shurelia...\nMas por que isso... tão de repente...?!",
        "rewritten",
        "Surpresa estupefata de Lyner diante de uma quebra de protocolo tão íntima."
    ),
    6747: (
        "...Lyner... Você ouviria o que guardo no peito?...\nOs meus verdadeiros sentimentos...",
        "rewritten",
        "Súplica tocante de quem passou eras reprimindo a própria humanidade."
    ),
    6748: (
        "Mas é claro.",
        "rewritten",
        "Entrega leal e escuta aberta de Lyner."
    ),
    6749: (
        "...Eu...",
        "approved_as_is",
        "Suspiro contido antes do mergulho na memória."
    ),
    6750: (
        "Vivo em completa solidão...\nDesde o fim da Segunda Era, ao longo de centenas de anos...",
        "rewritten",
        "O peso cósmico dos séculos de isolamento após a Segunda Era."
    ),
    6751: (
        "Na Primeira Era, eu tinha alguém que era como um pai para mim.\nNa Segunda Era, tive valorosos companheiros que ajudaram a reconstruir o mundo.",
        "rewritten",
        "Resgate da cronologia ancestral canônica: Primeira Era e Segunda Era."
    ),
    6752: (
        "...Mas, nesta Terceira Era... vivi em solidão absoluta.\nNão havia uma só alma a quem eu pudesse abrir o meu coração...",
        "rewritten",
        "A tragédia da Terceira Era: o confinamento funcional e o vazio afetivo."
    ),
    6753: (
        "......",
        "rewritten",
        "Compaixão reverente de Lyner absorvendo o sofrimento milenar dela."
    ),
    6754: (
        "No ocaso da Segunda Era... fomos traídos pela humanidade...\ne a Grande Calamidade se abateu sobre o mundo... Desde aquele dia,\neu me tornei incapaz de voltar a confiar nas pessoas...",
        "rewritten",
        "A raiz do trauma: a traição humana e a catástrofe que selou seu coração."
    ),
    6755: (
        "Por isso, cortei qualquer contato humano que não fosse estritamente necessário.\nImpus a mim mesma a proibição absoluta de nutrir sentimentos pessoais.",
        "rewritten",
        "A disciplina de ferro autoimposta para suportar o fardo da imortalidade."
    ),
    6756: (
        "...Então era por isso.\nPor essa razão a senhora mantinha aquela postura tão rigorosamente burocrática...",
        "rewritten",
        "Compreensão iluminada de Lyner decifrando a frieza institucional de Shurelia."
    ),
    6757: (
        "...Sim.",
        "approved_as_is",
        "Confirmação sussurrada e resignada."
    ),
    6758: (
        "Mas agora... eu já não suporto mais viver assim...\nDesde que passei a viajar com você,\no peso desse jugo foi se tornando cada vez mais sufocante...",
        "rewritten",
        "O degelo afetivo provocado pela convivência calorosa e protetora de Lyner."
    ),
    6759: (
        "No fundo... eu não quero mais ficar sozinha...",
        "rewritten",
        "A verdade nua e crua: a deusa implorando pelo calor da amizade humana."
    ),
    6760: (
        "Senhora Shurelia... Eu estarei sempre ao seu lado.\nPor isso, por favor, não tenha receio.",
        "rewritten",
        "Juramento de proteção inabalável e conforto afetuoso de Lyner."
    ),
    6761: (
        "Obrigada...\nMas eu gostaria de dar mais um passo... Queria ficar só mais um pouquinho mais perto de você.",
        "rewritten",
        "Vontade delicada de encurtar a distância e transpor a hierarquia formal."
    ),
    6762: (
        "Por isso eu queria conversar como se fôssemos bons amigos...\nClaro, apenas quando estivermos a sós assim, nós dois.",
        "rewritten",
        "A proposta de cumplicidade privada: um pacto de intimidade a portas fechadas."
    ),
    6763: (
        "......",
        "rewritten",
        "Lyner ponderando o impacto e a beleza do segredo compartilhado."
    ),
    6764: (
        "Tudo bem, combinado.\nAfinal de contas, se a senhora falasse comigo sem cerimônias na frente de todos,\neu passaria por um bocado de apuros.",
        "rewritten",
        "Aceitação bem-humorada de Lyner pensando no escândalo dos cavaleiros e da Igreja."
    ),
    6765: (
        "Fica combinado só para quando estivermos a sós.\nUm segredo só nosso.",
        "rewritten",
        "Cumplicidade doce e cavalheiresca selando o pacto dos dois."
    ),
    6766: (
        "O-obrigada...",
        "rewritten",
        "Alívio tímido e felicidade transbordando nos lábios da deusa."
    ),
    6767: (
        "......",
        "rewritten",
        "Momento de respiração e preparo mental para abandonar a compostura."
    ),
    6768: (
        "Então... b-bem...\njá vou... c-começar a falar... s-sem cerimônia...",
        "rewritten",
        "Shurelia tentando articular a fala informal (ため口) e travando toda na pronúncia."
    ),
    6769: (
        "M-mas faz tanto tempo que não sei se vou acertar...\nPor favor, não vá rir de mim, está bem?",
        "rewritten",
        "Insegurança adorável de quem passou séculos falando apenas com linguagem de corte."
    ),
    6770: (
        "Eu prometo, mas...\na senhora não ia começar a falar sem formalidades?",
        "rewritten",
        "Lyner flagrando com bom humor que ela acabou de usar o polido 'くださいね'."
    ),
    6771: (
        "Ah... É-é que assim de repente... é tão difícil...!",
        "rewritten",
        "Enrubescimento e frustração fofa de Shurelia ao falhar na informalidade imediata."
    ),
    6772: (
        "Lyner... Você teria um instante?",
        "rewritten",
        "Nova tentativa hesitante ainda carregando resquícios do polido 'いいですか?'."
    ),

    # =========================================================================
    # EVENT: Event/119.evd (IDs 6773 - 6780) - Exploração das Ruínas com Krusche
    # =========================================================================
    6773: (
        "Lyner! Dá uma olhada ali!",
        "rewritten",
        "Krusche chamando a atenção com sua vivacidade e energia contagiante."
    ),
    6774: (
        "Parece algum tipo de ruína...\nBora lá investigar!",
        "rewritten",
        "Espírito explorador e audacioso da engenheira em busca de tecnologia."
    ),
    6775: (
        "Quêêê?!\nA gente não tem tempo para ficar zanzando em ruínas agora!",
        "rewritten",
        "Protesto exasperado de Lyner focado na urgência do dever."
    ),
    6776: (
        "Lyner, quanta ingenuidade!",
        "rewritten",
        "Krusche zombando da falta de visão do cavaleiro ('甘い!')."
    ),
    6777: (
        "São ruínas antigas, sabia?\nPodemos muito bem encontrar pistas para escapar deste lugar!",
        "rewritten",
        "Argumento pragmático e engenhoso demonstrando que a exploração é necessária."
    ),
    6778: (
        "B-bom...\naté pode ser, mas...",
        "rewritten",
        "Lyner desarmado pela lógica irrefutável da amiga mecânica."
    ),
    6779: (
        "Só uma olhadinha rápida!\nFicar plantado esperando não vai adiantar nada mesmo.",
        "rewritten",
        "Krusche puxando Lyner com atitude resoluta contra a inércia."
    ),
    6780: (
        "...Não tem jeito com você. Está bem, vamos lá.",
        "rewritten",
        "Rendição bem-humorada de Lyner cedendo ao comando prático de Krusche."
    ),
}

# Verificação de integridade da contagem
assert len(curations) == 215, f"Esperado 215 falas no dicionário, obtido {len(curations)}"

curated_dialogues = []
translations_list = []
lines_rewritten = 0
lines_approved_as_is = 0

all_validation_errors = {}

for d in raw_dialogues:
    d_id = d["id"]
    orig_en = d.get("original_en", "")
    orig_jp = d.get("original_jp", "")
    current_pt = d.get("current_ptbr", "")

    if d_id not in curations:
        raise ValueError(f"ID {d_id} ausente no mapeamento curations!")

    curated_text, verdict, rationale = curations[d_id]

    if verdict == "rewritten":
        lines_rewritten += 1
    elif verdict == "approved_as_is":
        lines_approved_as_is += 1
    else:
        raise ValueError(f"Veredito inválido para ID {d_id}: {verdict}")

    # Validar deterministicamente cada linha
    line_errs = validate_line(d_id, orig_en, curated_text)
    if line_errs:
        all_validation_errors[d_id] = line_errs

    curated_dialogues.append({
        "id": d_id,
        "event_file": d.get("event_file", ""),
        "speaker_id": d.get("speaker_id", 0),
        "speaker": d.get("speaker", ""),
        "original_jp": orig_jp,
        "original_en": orig_en,
        "current_ptbr": current_pt,
        "curated_ptbr": curated_text,
        "text": curated_text,  # campo redundante para máxima compatibilidade
        "verdict": verdict,
        "rationale": rationale
    })

    translations_list.append({
        "id": d_id,
        "text": curated_text
    })

if all_validation_errors:
    print(f"FALHA NA VALIDAÇÃO DE LINHAS ({len(all_validation_errors)} erros):")
    for d_id, errs in all_validation_errors.items():
        print(f"  ID {d_id}: {'; '.join(errs)}")
    sys.exit(1)

# Validação do lote completo pelo validador do projeto
is_valid, batch_errors = validate_batch({"dialogues": curated_dialogues})
if not is_valid:
    print(f"FALHA NO BATCH VALIDATOR ({len(batch_errors)} erros):")
    for d_id, errs in batch_errors.items():
        print(f"  ID {d_id}: {'; '.join(errs)}")
    sys.exit(1)

# Highlights marcantes do bloco
highlights = [
    {
        "id": 6570,
        "speaker": "Spica / Misha / Lyner",
        "description": "Reencontro cômico no Porto Gaivota onde Spica alfineta Lyner como namorador e zomba de Misha adulta sugerindo que ela só teve um estirão tardio."
    },
    {
        "id": 6610,
        "speaker": "Lyner / Tastiella / Aurica",
        "description": "Audiência solene na Catedral de Platina revelando que Aurica é a reencarnação da Deusa Tyria e que o sagrado Trio de Elemia descendeu em seu coração."
    },
    {
        "id": 6630,
        "speaker": "Lyner / Sistema",
        "description": "Execução precisa dos códigos fônicos de segurança ancestral Hymmnos para liberação das comportas e divisórias da superestrutura da Torre."
    },
    {
        "id": 6650,
        "speaker": "Misha / Lyner",
        "description": "Clímax da Cosmosfera onde Misha decide colapsar seu mundo falso e destruir seu avatar infantil para despertar como adulta ao lado de Lyner."
    },
    {
        "id": 6678,
        "speaker": "Don Leon / Aurica",
        "description": "Momento de emancipação e ternura na Cosmosfera de Aurica: Don Leon ensina a diferença entre consolo e dependência, selando a Magia Vermelha [Meu Herói]."
    },
    {
        "id": 6745,
        "speaker": "Shurelia / Lyner",
        "description": "Confissão comovente de Shurelia sobre os séculos de solidão desde o fim da Segunda Era e o pedido tímido para falar com Lyner como amiga a sós."
    }
]

# Novos termos mapeados
new_terms = {
    "Trio of Elemia": {
        "pt": "Trio de Elemia",
        "gender": "masculino",
        "number": "singular",
        "category": "Divindades / Mitologia de Sol Ciel",
        "note": "エレミア三謳神. As três Deusas do Canto ancestrais de Elemia: Eoria, Frelia e Tilia."
    },
    "Goddess Tyria": {
        "pt": "Deusa Tyria",
        "gender": "feminino",
        "number": "singular",
        "category": "Divindades / Reyvateil Origin",
        "note": "ティリア神. A terceira Reyvateil Origin ancestral reverenciada na mitologia de Sol Ciel."
    },
    "Falcon's Claw": {
        "pt": "Garra do Falcão",
        "gender": "feminino",
        "number": "singular",
        "category": "Localização / Topônimo",
        "note": "たかのつめあと. Região rochosa onde repousa o santuário com o Cristal Hymmnos Linker."
    },
    "My Hero": {
        "pt": "Meu Herói",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia / Reyvateil Craft",
        "note": "マイヒーロー. Magia Vermelha esculpida pela resolução de Aurica ao superar a dependência de Don Leon."
    },
    "FFT Spectrum": {
        "pt": "Espectro FFT",
        "gender": "masculino",
        "number": "singular",
        "category": "Tecnologia / Autenticação Fônica",
        "note": "FFTスペクトラム認証. Protocolo fônico de autenticação por transformada rápida de Fourier na Torre."
    }
}

# Matriz de tratamento atualizada
updated_address_matrix = {
    "Spica": {
        "Lyner": "Tratamento bem-humorado e zombeteiro ('Lyner', 'você'), implicando com suas companhias femininas.",
        "Misha": "Amizade calorosa, provocativa e afetuosa ('Misha'), fingindo não reconhecê-la para tirar sarro de seu crescimento repentino."
    },
    "Tastiella": {
        "Lyner": "Tratamento cerimonioso e solene de líder espiritual aos nobres cavaleiros ('Nobre Lyner / Lyner-dono', 'vós / vossa jornada').",
        "Aurica": "Benevolência pastoral reverente à reencarnação divina ('Aurica', 'jovem guardiã')."
    },
    "Don_Leon": {
        "Aurica": "Devoção cavalheiresca nobre e paternal ('Senhorita Aurica', 'vós'), guiando sua autoconfiança sem condescendência.",
        "Lyner": "Vigilância armada cômica e protetora ('velhacos atrevidos como vós'), garantindo o decoro com a senhorita."
    },
    "Shurelia": {
        "Lyner": "Tratamento em transição: deusa etérea e reverente em público ('Lyner', 'você'), evoluindo para amizade íntima e tímida a sós com tentativas comoventes de fala informal ('sem cerimônia')."
    },
    "Krusche": {
        "Lyner": "Parceria prática, rápida e despachada ('Lyner', 'você'), puxando-o para a ação exploratória nas ruínas."
    }
}

# Scene handoff para o próximo bloco
scene_handoff = {
    "resumo_dramatico": "O reencontro afetuoso e cômico no Porto Gaivota onde Spica zomba do estirão repentino de Misha adulta e alfineta Lyner; a revelação da moradora liberando o interior da embarcação no cais; a audiência solene na Catedral de Platina com o Bispo Tastiella celebrando a descida do sagrado Trio de Elemia no coração de Aurica e ordenando a expedição à Garra do Falcão pelo Cristal Hymmnos Linker; a precisão fônica ancestral na liberação das divisórias A7 e B1 nº 3 por comando Hymmnos; a catarse na Cosmosfera onde Misha destrói seu eu falso infantil para renascer como mulher ao lado de Lyner; o momento de sublime maturidade psicológica em que Don Leon liberta Aurica da dependência infantil e forja a Magia Vermelha [Meu Herói]; a despedida melancólica e resoluta de Jack nas docas de Platina rumo à Tenba; a tentativa de infiltração nos domínios corporativos barrada pela ausência de Ayano; o mergulho na Cosmosfera reprogramada por Shurelia para o resgate de Leila superando loops de Fim de Jogo; a revelação íntima e comovente de Shurelia partilhando três eras de solidão e selando um pacto de amizade secreta a sós com Lyner; e a incursão exploratória de Krusche e Lyner pelas ruínas desconhecidas.",
    "decisoes_terminologicas": {
        "Garra do Falcão": "[Garra do Falcão] (たかのつめあと, santuário rochoso do Cristal Linker)",
        "Trio de Elemia": "Trio de Elemia (エレミア三謳神, Três Deusas do Canto ancestrais)",
        "Deusa Tyria": "Deusa Tyria (ティリア神, divindade originária de Sol Ciel)",
        "Meu Herói": "[Meu Herói] (マイヒーロー, Magia Vermelha de Aurica)",
        "Espectro FFT": "Espectro FFT (FFTスペクトラム認証, autenticação fônica)",
        "Don Leon": "Don Leon (どんすけ, guardião samurai de pelúcia de Aurica)",
        "Bala de Gato": "Bala de Gato (猫飴, doce característico de Spica)",
        "Cristal Hymmnos": "Cristal Hymmnos (ヒュムネクリスタル, mídias sonoras ancestrais)"
    },
    "alertas_para_proximo_bloco": "Atenção ao desenrolar da expedição à Garra do Falcão para a recuperação do Cristal Hymmnos Linker, ao desfecho do salvamento de Leila no mergulho reconfigurado na Cosmosfera e à consolidação da cumplicidade íntima e descontraída entre Lyner e Shurelia em seus momentos a sós."
}

output_data = {
    "block_id": "BLK_EVD_026",
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

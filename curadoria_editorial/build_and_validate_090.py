# -*- coding: utf-8 -*-
import sys
import json
from pathlib import Path

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Carregar arquivo de entrada
input_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_090_input.json")
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

print(f"Loaded input data with {len(input_data['dialogues'])} dialogues.")

curated_translations = {
    # Event/124.evd (IDs 20210 to 20264)
    20210: {
        "pt": "Quantas vezes eu vou ter que repetir\npra você entender?!",
        "notes": "Freguês ríspido e preconceituoso gritando com Claire na taverna."
    },
    20211: {
        "pt": "Hã?",
        "notes": "Lyner surpreso ao ouvir o tumulto vindo da taverna."
    },
    20212: {
        "pt": "Pelo visto, tá rolando alguma confusão\nali na taverna.",
        "notes": "Krusche atenta e pragmática identificando a gritaria na taverna."
    },
    20213: {
        "pt": "Ah!...\nAquela ali é a...",
        "notes": "Aurica avistando Claire e reconhecendo sua amiga de infância."
    },
    20214: {
        "pt": "Dá o fora daqui!\nTer uma desgarrada feito você por perto\né um incômodo danado!",
        "notes": "Freguês preconceituoso destilando desprezo por uma Reyvateil sem afiliação institucional (hanpamon)."
    },
    20215: {
        "pt": "É verdade que sou uma Reyvateil independente.",
        "notes": "Claire mantendo a compostura com dignidade serena e altivez."
    },
    20216: {
        "pt": "No entanto, isso não significa\nque eu tenha causado qualquer transtorno a vocês.",
        "notes": "Claire rebatendo as acusações com lógica inabalável."
    },
    20217: {
        "pt": "Portanto, não tenho a menor razão\npara me retirar daqui.",
        "notes": "Claire afirmando seu direito legítimo de permanecer na taverna."
    },
    20218: {
        "pt": "Como é que é?!",
        "notes": "Freguês indignado com a firmeza inabalável de Claire."
    },
    20219: {
        "pt": "Se eu estivesse realmente incomodando alguém,\nme retiraria por conta própria.",
        "notes": "Claire estabelecendo sua conduta cívica impecável."
    },
    20220: {
        "pt": "Só que o que o senhor está fazendo\nnão passa de implicância infundada.",
        "notes": "Claire denunciando o preconceito gratuito e a provocação sem cabimento (iigakari)."
    },
    20221: {
        "pt": "Que perda de tempo!...\nPor hoje eu vou dar o fora daqui!!",
        "notes": "Freguês batendo em retirada furioso e humilhado."
    },
    20222: {
        "pt": "Mas o que foi que deu nele...?",
        "notes": "Lyner perplexo com a hostilidade gratuita do homem."
    },
    20223: {
        "pt": "...Que sujeito mais desprezível.",
        "notes": "Krusche sentenciando a baixeza moral do agressor (saitee da ne)."
    },
    20224: {
        "pt": "Uff...",
        "notes": "Claire soltando um longo suspiro de alívio sem rubricas artificiais."
    },
    20225: {
        "pt": "Parece que as coisas estavam bem tensas\npor aqui, hein?",
        "notes": "Lyner se aproximando em tom solidário e descontraído."
    },
    20226: {
        "pt": "É você?!\nPor onde andava esse tempo todo?\nFiquei tão preocupada!",
        "notes": "Claire surpresa e radiante ao reencontrar Lyner são e salvo."
    },
    20227: {
        "pt": "O Jack não está com você?\nEle passou um tempão te procurando, sabia?",
        "notes": "Claire indagando sobre o paradeiro de Jack e seu afeto protetor."
    },
    20228: {
        "pt": "Mas que alívio...\nver que você está são e salvo.",
        "notes": "Claire expressando afeto sincero pelo bem-estar de Lyner."
    },
    20229: {
        "pt": "......",
        "notes": "Aurica emocionada e hesitante perante a figura fraternal de Claire."
    },
    20230: {
        "pt": "Ué...?\nNão pode ser... Aurica?!\nÉ você mesma, não é?!",
        "notes": "Claire virando-se e reconhecendo Aurica com genuíno espanto."
    },
    20231: {
        "pt": "Mana Claire...",
        "notes": "Aurica chamando Claire pelo tratamento carinhoso canônico de irmã mais velha (Claire-oneechan)."
    },
    20232: {
        "pt": "Não acredito, que saudade!\nNunca imaginei te encontrar num lugar desses!",
        "notes": "Claire explodindo de alegria e afeto no reencontro fraterno."
    },
    20233: {
        "pt": "Quando o vilarejo foi destruído pelo fogo,\neu fiquei tão preocupada com você!\nMas que alívio...",
        "notes": "Claire recordando o trauma da queima de Skuwat e o alívio de ver Aurica viva."
    },
    20234: {
        "pt": "Vocês duas se conhecem de onde?",
        "notes": "Lyner curioso com a intimidade instantânea entre Aurica e Claire."
    },
    20235: {
        "pt": "Somos amigas de infância!\nNós crescemos juntas no mesmo vilarejo.",
        "notes": "Claire explicando a origem comum de ambas no vilarejo destruído."
    },
    20236: {
        "pt": "Ah, entendi...\nMas o que você quis dizer com o vilarejo destruído...?",
        "notes": "Lyner tocando com cautela no passado doloroso de Aurica."
    },
    20237: {
        "pt": "Já faz bastante tempo...\nmas o nosso vilarejo acabou destruído\npelas chamas da guerra.",
        "notes": "Aurica relembrando com melancolia a destruição de Skuwat durante o conflito bélico."
    },
    20238: {
        "pt": "Aurica, vamos tomar um chá mais tarde!\nTenho tanta coisa para colocar em dia com você!",
        "notes": "Claire quebrando o clima pesado e convidando Aurica para conversar e tomar chá."
    },
    20239: {
        "pt": "Sim...",
        "notes": "Aurica concordando com meiguice e carinho fraternal."
    },
    20240: {
        "pt": "Mas pensando bem, ver vocês dois viajando juntos\né que é uma baita surpresa para mim.",
        "notes": "Claire comentando com malícia e surpresa sobre a parceria de Lyner e Aurica."
    },
    20241: {
        "pt": "Bom, rolou bastante perrengue\naté as coisas chegarem a esse ponto.\nSe for ouvir a história, escute com atenção.",
        "notes": "Krusche pontuando de forma pragmática as provações que enfrentaram."
    },
    20242: {
        "pt": "Mas me diz uma coisa:\nmal te perco de vista e você já me volta\ncom um buquê em cada braço? Que conquistador, hein!",
        "notes": "Claire provocando Lyner com espirituosidade sobre estar escoltado por duas belas jovens (ryoute ni hana)."
    },
    20243: {
        "pt": "E-espera aí, Claire!\nNão tem nada a ver com isso...",
        "notes": "Lyner corando e gaguejando desesperado perante a provocação cômica de Claire."
    },
    20244: {
        "pt": "Hehehe, eu sei muito bem!\nÉ tão divertido te ver sem jeito.",
        "notes": "Claire caindo no riso ao constatar o acanhamento cândido de Lyner."
    },
    20245: {
        "pt": "Mas enfim, não vamos ficar aqui plantados em pé.\nQue tal jantarmos todos juntos?",
        "notes": "Claire convidando o grupo calorosamente para jantar na taverna."
    },
    20246: {
        "pt": "Hmm... Então quer dizer que a Aurica\né candidata a Donzela Sagrada da Igreja?\nO seu grande sonho de infância finalmente se realizou!",
        "notes": "Claire comentando com orgulho sobre o posto clerical almejado por Aurica."
    },
    20247: {
        "pt": "A lendária Donzela Sagrada que salvou o mundo outrora...\nSeria tão maravilhoso se você fosse escolhida\ncomo a Segunda Donzela Sagrada!",
        "notes": "Claire inspirando Aurica a se tornar a sucessora da santa protetora do mundo."
    },
    20248: {
        "pt": "Isso é impossível para mim.\nEu nunca vou conseguir virar a Donzela Sagrada...\nafinal, sou só uma Classe D.",
        "notes": "Aurica expondo sua profunda insegurança pelo baixo estrato de sua linhagem Reyvateil."
    },
    20249: {
        "pt": "Classe não tem a menor importância!\nSe mantiver a determinação e o ânimo firme,\nseu sonho com certeza vai se realizar!",
        "notes": "Claire encorajando Aurica com vigor fraternal e otimismo radiante."
    },
    20250: {
        "pt": "...Será mesmo...?",
        "notes": "Aurica hesitante, querendo acreditar nas palavras encorajadoras de Claire."
    },
    20251: {
        "pt": "...O que foi, Aurica?\nCadê esse ânimo? Vamos, levante essa cabeça!",
        "notes": "Claire puxando as orelhas de Aurica com carinho e exigindo postura erguida."
    },
    20252: {
        "pt": "Uhum...",
        "notes": "Aurica recuperando um fiapo de confiança perante a insistência da amiga."
    },
    20253: {
        "pt": "Mas bom, já entendi a situação toda.",
        "notes": "Claire concluindo seu panorama da missão do grupo."
    },
    20254: {
        "pt": "A Igreja concordou em dar uma força para o Lyner,\ne calhou de você estar lá no meio.",
        "notes": "Claire resumindo o acordo entre Lyner e o clero."
    },
    20255: {
        "pt": "Só que as ruínas da [Colina do Canto]\nficam bem longínquas.",
        "notes": "Claire alertando sobre a distância considerável do sítio arqueológico sagrado."
    },
    20256: {
        "pt": "...Ah, já sei!\nSe você for até a [Colina do Canto],\npoderia me fazer um pequeno favor?",
        "notes": "Claire tendo uma ideia oportunista e simpática para a expedição de Lyner."
    },
    20257: {
        "pt": "Dizem que lá na [Colina do Canto]\nexiste um material chamado [Fragmento de Yuteria].",
        "notes": "Claire mencionando o item de síntese e manufatura musical da Colina."
    },
    20258: {
        "pt": "Será que você não traria ao menos um para mim na volta?",
        "notes": "Claire pedindo graciosamente um espécime do fragmento acústico."
    },
    20259: {
        "pt": "Só isso? Tranquilo!\nAproveito que já estou a caminho e trago um para você.",
        "notes": "Lyner aceitando a missão secundária de coleta com presteza e companheirismo."
    },
    20260: {
        "pt": "Muito obrigada!",
        "notes": "Claire agradecendo com entusiasmo caloroso."
    },
    20261: {
        "pt": "Aah... De barriga tão cheia,\ncomeçou a me bater um soninho...",
        "notes": "Krusche bocejando saciada após o banquete noturno."
    },
    20262: {
        "pt": "Tem razão, é melhor encerrarmos\na nossa conversa por hoje.",
        "notes": "Claire propondo o término da ceia e o descanso de todos."
    },
    20263: {
        "pt": "Conto com você para trazer\no [Fragmento de Yuteria], viu?",
        "notes": "Claire reforçando a encomenda de síntese com um sorriso."
    },
    20264: {
        "pt": "Muito bem, hora de partirmos rumo à Igreja.",
        "notes": "Lyner convocando o grupo para a retomada dos deveres clericais."
    },

    # Event/449.evd (IDs 20265 to 20304)
    20265: {
        "pt": "Lyner! Mas não é que é você mesmo?!",
        "notes": "Radolf efusivo e surpreso ao rever Lyner na Igreja de Elemia no pós-jogo (Rota Misha)."
    },
    20266: {
        "pt": "Quanto tempo!\nRadolf, Aurica.",
        "notes": "Lyner cumprimentando calorosamente os velhos camaradas de batalha."
    },
    20267: {
        "pt": "Têm passado bem?!",
        "notes": "Radolf indagando com voz potente e fraterna sobre o bem-estar da dupla."
    },
    20268: {
        "pt": "Lyner, Misha... Quanto tempo!\nQue alívio ver vocês tão bem.",
        "notes": "Aurica acolhendo Lyner e Misha com maturidade, afeto e serenidade adquirida."
    },
    20269: {
        "pt": "Pelo que vejo, vocês dois têm trabalhado duro\npor aqui, hein?",
        "notes": "Lyner reconhecendo o empenho e a dedicação incansável da dupla na administração do templo."
    },
    20270: {
        "pt": "Pois é, graças aos céus.\nA verdade é que... depois de tudo aquilo,\nacabei sendo promovido a Bispo...",
        "notes": "Radolf revelando com modéstia bem-humorada sua sagração clerical inesperada."
    },
    20271: {
        "pt": "É sério?!\nMas isso é maravilhoso!",
        "notes": "Lyner comemorando com orgulho sincero a ascensão de seu valoroso mentor."
    },
    20272: {
        "pt": "Pois é. Pelo visto, nunca houve precedentes\nde um cavaleiro ingressar no clero...",
        "notes": "Radolf comentando o caráter inédito da transição de cavaleiro para sacerdote."
    },
    20273: {
        "pt": "Mas disseram que fui sagrado Bispo\npor salvar a Igreja inteira daquela crise terrível.",
        "notes": "Radolf explicando a justificativa oficial do episcopado para sua consagração."
    },
    20274: {
        "pt": "Meus parabéns, Radolf!",
        "notes": "Lyner congratulando Radolf com lealdade e afeto filial."
    },
    20275: {
        "pt": "Muitos parabéns, senhor Radolf!",
        "notes": "Misha prestando suas respeitosas e vibrantes homenagens ao novo Bispo."
    },
    20276: {
        "pt": "Não, por favor... Ouvir vocês falarem\ncom tanta cerimônia assim me deixa até sem jeito!",
        "notes": "Radolf encabulado com a pompa e a solenidade dos jovens."
    },
    20277: {
        "pt": "A Aurica também tem se desdobrado muito.",
        "notes": "Radolf destacando com orgulho o trabalho humanitário liderado por Aurica."
    },
    20278: {
        "pt": "Afinal, ela é a diretora do programa de assistência\na idosos e aos mais necessitados.",
        "notes": "Radolf detalhando o papel social crucial assumido por Aurica na comunidade."
    },
    20279: {
        "pt": "A-a Aurica?!\nTá falando sério?!",
        "notes": "Lyner chocado e desconcertado com a metamorfose da tímida garota em líder comunitária."
    },
    20280: {
        "pt": "Lyner...\nPrecisava ficar tão espantado assim?",
        "notes": "Aurica fazendo beicinho tímido diante do espanto desmedido de Lyner."
    },
    20281: {
        "pt": "Ah, mas se comparar com a Aurica de antigamente,\né uma mudança e tanto!",
        "notes": "Misha concordando em tom brincalhão e amoroso com a surpresa de Lyner."
    },
    20282: {
        "pt": "Pensando bem, acho que tem razão.\nSe hoje consigo enxergar a vida desse jeito,\né tudo graças a você, Lyner.",
        "notes": "Aurica reconhecendo com profunda gratidão e carinho a influência transformadora de Lyner em sua vida."
    },
    20283: {
        "pt": "Sendo assim, este lugar sagrado\njá não é mais uma igreja a serviço de Mir.",
        "notes": "Radolf afirmando a purificação da instituição e a ruptura definitiva com a tirania de Mir."
    },
    20284: {
        "pt": "Agora, ela pertence ao povo e existe para o povo.",
        "notes": "Radolf proclamando o ideal canônico da Igreja de Elemia como santuário popular."
    },
    20285: {
        "pt": "Então o seu sonho finalmente se realizou.",
        "notes": "Lyner celebrando a materialização do nobre propósito de vida de Radolf."
    },
    20286: {
        "pt": "Pois é. Só que isto aqui é apenas a linha de partida.\nO trabalho duro começa de verdade agora! Hahaha!",
        "notes": "Radolf rindo com otimismo e determinação estoica perante os desafios futuros."
    },
    20287: {
        "pt": "...",
        "notes": "Lyner hesitando em quebrar o clima festivo com o pedido solene."
    },
    20288: {
        "pt": "Lyner...\nConta para eles sobre aquele assunto.",
        "notes": "Misha incentivando Lyner a expor a missão de resgate de Shurelia."
    },
    20289: {
        "pt": "O que foi?\nPor acaso vocês dois pretendem se casar?",
        "notes": "Radolf brincando com malícia e perspicácia fraternal sobre o relacionamento dos dois."
    },
    20290: {
        "pt": "C-claro que não!...\nPoxa vida...",
        "notes": "Misha corando furiosamente e resmungando encabulada com a insinuação nupcial."
    },
    20291: {
        "pt": "Na verdade...\nTrata-se da Senhora Shurelia.",
        "notes": "Lyner revelando a gravidade do tema com solenidade e reverência."
    },
    20292: {
        "pt": "Compreendo! Então... isso quer dizer\nque ela talvez possa despertar de volta?!",
        "notes": "Radolf reagindo com comoção e esperança vibrante à possibilidade de retorno de Shurelia."
    },
    20293: {
        "pt": "Se encontrarmos o cristal chamado [RE Nation]...",
        "notes": "Lyner especificando a condição necessária para a reativação vital de Shurelia."
    },
    20294: {
        "pt": "Mas que esplêndida notícia!\nSendo sincero, eu também fiquei arrasado naquela ocasião...\nQue alívio imenso... que alívio!",
        "notes": "Radolf desabafando sobre o pesar da partida de Shurelia e vibrando com a chance de salvação."
    },
    20295: {
        "pt": "Por isso... pensamos se você não poderia\nnos ajudar na busca por esse cristal.",
        "notes": "Lyner fazendo o convite para que Radolf integre a expedição de busca."
    },
    20296: {
        "pt": "...Entendo. Então era isso.",
        "notes": "Radolf absorvendo a magnitude da convocação heroica."
    },
    20297: {
        "pt": "Perdoe-me.\nNenhum de nós dois pode deixar o posto agora.",
        "notes": "Radolf recusando com pesar gravoso, reconhecendo o dever inadiável com a Igreja e a população."
    },
    20298: {
        "pt": "...Radolf.",
        "notes": "Lyner sentindo o peso da recusa mas respeitando a dignidade da postura de Radolf."
    },
    20299: {
        "pt": "Nos velhos tempos, quando existia alguém acima de mim\ne eu só precisava cuidar dos meus próprios passos,\ntudo era mais simples.",
        "notes": "Radolf contrastando a leveza do soldado subordinado com o fardo monumental da liderança institucional."
    },
    20300: {
        "pt": "Só que agora é diferente.\nSe eu e a Aurica partirmos daqui, esta Igreja vai...",
        "notes": "Radolf evidenciando a dependência do povo e a fragilidade da nova ordem que depende deles."
    },
    20301: {
        "pt": "...Sinto muito.",
        "notes": "Radolf reiterando seu pedido sincero de desculpas por não poder empunhar a espada ao lado de Lyner."
    },
    20302: {
        "pt": "N-não se preocupe,\nvocê não precisa se culpar por isso.",
        "notes": "Lyner confortando Radolf com nobreza de espírito e empatia absoluta."
    },
    20303: {
        "pt": "Fui eu quem chegou de repente com esse pedido.\nDiante das suas novas responsabilidades...\né totalmente compreensível.",
        "notes": "Lyner compreendendo e validando a decisão madura e responsável do bispo."
    },
    20304: {
        "pt": "...Obrigado pela compreensão.",
        "notes": "Radolf selando com gravidade e afeto a despedida e a mútua lealdade inquebrantável."
    }
}

# Validação minuciosa de cada fala
total_dialogues = len(input_data["dialogues"])
assert total_dialogues == len(curated_translations), f"Expected {total_dialogues}, got {len(curated_translations)}"

hard_gate_errors = 0
lint_warnings = 0

dialogues_output = []
curated_lines_output = []

for d in input_data["dialogues"]:
    did = d["id"]
    jp = d["original_jp"]
    en = d["original_en"]
    cur_info = curated_translations[did]
    trad = cur_info["pt"]
    notes = cur_info["notes"]

    valido, erros = validador_editorial.validar_hard_gate(
        original=jp,
        traduzido=trad,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        hard_gate_errors += len(erros)
        for e in erros:
            print(f"[HARD GATE ERROR] ID {did}: {e}")

    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if avisos:
        lint_warnings += len(avisos)
        for a in avisos:
            print(f"[LINT WARNING] ID {did}: {a}")

    if "\r" in trad:
        print(f"[ERROR] ID {did}: Carriage return \\r found!")
        hard_gate_errors += 1

    parts = trad.split("\n")
    for part in parts[1:]:
        stripped = part.strip()
        if stripped.startswith((".", ",", "!", "?", ";", ":", "-", "—")):
            print(f"[ERROR] ID {did}: Line starts with orphan punctuation: {part!r}")
            hard_gate_errors += 1
        if part.startswith("..."):
            print(f"[ERROR] ID {did}: Line starts with reticencias: {part!r}")
            hard_gate_errors += 1

    match_frac = validador_editorial.SYNTACTIC_FRACTURE_NEWLINE_REGEX.search(trad)
    if match_frac:
        print(f"[ERROR] ID {did}: Syntactic fracture before \\n: {match_frac.group(0)!r}")
        hard_gate_errors += 1

    entry = {
        "id": did,
        "event_file": d["event_file"],
        "speaker_id": d["speaker_id"],
        "speaker": d["speaker"],
        "original_jp": jp,
        "original_en": en,
        "current_ptbr": d.get("curated_ptbr") or d.get("text_ptbr") or d.get("current_ptbr"),
        "review_status": "approved",
        "ptbr_text": trad,
        "text_ptbr": trad,
        "curated_ptbr": trad,
        "final_ptbr": trad,
        "texto_ptbr_curado": trad,
        "custom_text": trad,
        "reviewed": True,
        "notes": notes,
        "curation_notes": notes,
        "curadoria_notes": notes
    }
    dialogues_output.append(entry)
    curated_lines_output.append(entry)

print(f"\n--- Preliminary Validation Result ---")
print(f"Total lines: {total_dialogues}")
print(f"Hard Gate Errors: {hard_gate_errors}")
print(f"Lint Warnings: {lint_warnings}")

if hard_gate_errors == 0 and lint_warnings == 0:
    print("[SUCCESS] All 95 lines passed with ZERO errors and ZERO warnings!")
else:
    print("[FAIL] Please fix identified issues before generating output JSON.")
    sys.exit(1)

# Construir estrutura final de saída
output_obj = {
    "block_id": "BLK_EVD_090",
    "axis_id": input_data.get("axis_id", "AXIS_3"),
    "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
    "category": input_data.get("category", "Event Dialogue"),
    "line_count": total_dialogues,
    "id_range": input_data.get("id_range", [20210, 20304]),
    "stats": {
        "total_lines": total_dialogues,
        "lines_rewritten": total_dialogues,
        "lines_approved_as_is": 0,
        "new_terms_added": 3
    },
    "glossary_additions": {
        "Segunda Donzela Sagrada": {
            "pt": "Segunda Donzela Sagrada",
            "gender": "feminino",
            "number": "singular",
            "category": "Título / Profecia Clerical",
            "note": "第二の聖女 (Daini no Seijo). Título messiânico profetizado na Igreja de Elemia para a Reyvateil destinada a suceder a lendária Santa que salvou o mundo, assumido como o grande sonho de infância de Aurica Felchel."
        },
        "Programa de Assistência Social": {
            "pt": "Programa de Assistência Social da Igreja",
            "gender": "masculino",
            "number": "singular",
            "category": "Instituição / Ministério Social de Elemia",
            "note": "お年寄りや貧しい人を支援するプログラム. Ministério de caridade e auxílio comunitário a idosos e desvalidos instituído na nova Igreja de Elemia sob a liderança de Aurica Felchel no pós-guerra."
        },
        "Igreja Popular": {
            "pt": "Igreja do Povo",
            "gender": "feminino",
            "number": "singular",
            "category": "Conceito / Doutrina Clerical",
            "note": "民衆の為の、民衆の教会 (Minshuu no tame no, minshuu no kyoukai). Novo paradigma doutrinário proclamado pelo Bispo Radolf Schneider após a queda do Bispo Falss, refundando a Igreja de Elemia a serviço da população e rompendo com a adoração forçada a Mir."
        }
    },
    "scene_handoff": {
        "last_scene_id": "Event/449.evd",
        "last_line_id": 20304,
        "resumo_dramatico": "O bloco BLK_EVD_090 consagra o gran finale de todo o corpus de diálogos de eventos de Ar tonelico: Melody of Elemia, cobrindo dois momentos narrativos cruciais da jornada: (1) Em Event/124.evd, na taverna de Nemo, Lyner, Aurica e Krusche presenciam Claire ser agredida verbalmente por um frequentador preconceituoso que tenta expulsá-la da cidade por ser uma 'desgarrada' (Reyvateil sem afiliação institucional). Com firmeza e compostura digna, Claire rechaça as acusações infundadas e o agressor se retira humilhado. O grupo se aproxima e ocorre o reencontro emocionante de infância entre Claire e Aurica ('Mana Claire'), que cresceram no mesmo vilarejo destruído pelas chamas da guerra (Skuwat). Claire provoca Lyner em tom bem-humorado por voltar escoltado por duas belas jovens ('um buquê em cada braço'). Durante a ceia, Claire recorda o sonho de Aurica de se tornar a Segunda Donzela Sagrada da Igreja e encoraja a amiga com vigor filial, assegurando que o fato de ser Classe D em nada diminui seu valor. Claire então pede a Lyner que, em sua incursão às ruínas da [Colina do Canto], recolha um [Fragmento de Yuteria] para ela. (2) Em Event/449.evd, na Igreja de Elemia no pós-jogo (Rota de Misha pós-cântico do Suspend), Lyner e Misha visitam Radolf e Aurica. Radolf revela com orgulho bem-humorado que foi consagrado Bispo da Igreja de Elemia por salvar a instituição da catástrofe, estabelecendo um precedente histórico de um cavaleiro que ascende ao clero. Aurica, amadurecida e radiante, atua como diretora do programa comunitário de assistência a idosos e aos mais necessitados, refundando a Igreja como um templo 'do povo e para o povo', livre da influência opressora de Mir. Radolf faz piada perguntando se Lyner e Misha pretendem se casar, deixando Misha vermelha de vergonha. Em seguida, Lyner revela que a Senhora Shurelia poderá ser reativada de seu sono criogênico caso encontrem o cristal [RE Nation], convidando Radolf a se juntar à expedição. Comovido com a esperança de rever Shurelia viva, Radolf expressa sincero alívio, mas com nobreza e maturidade estoica recusa o convite, explicando que nos velhos tempos podia agir apenas como um guerreiro individual, mas agora carrega sobre os ombros a responsabilidade de liderar a Igreja e proteger a população ao lado de Aurica. Lyner compreende a grandeza do dever de Radolf, e os dois selam a despedida com mútua reverência e lealdade fraternal eterna.",
        "decisoes_terminologicas": {
            "Segunda Donzela Sagrada": "第二の聖女 (Daini no Seijo - título clerical e sonho de infância de Aurica)",
            "Colina do Canto": "謳う丘 (Utau Oka / Singing Hill - sítio sagrado canônico)",
            "Fragmento de Yuteria": "ユーテリア破片 (Fragment of Yuteria - material para instrumentos acústicos)",
            "Bispo Radolf": "ラードルフ司祭 (Radolf Shisai - sagração episcopal inédita)",
            "Igreja do Povo": "民衆の為の、民衆の教会 (Igreja a serviço da comunidade, expurgando a influência de Mir)",
            "Programa de Assistência": "お年寄りや貧しい人を支援するプログラム (Ministério comunitário gerido por Aurica)",
            "RE Nation": "リ・ネイション / EXEC_RE-NATION/.. (Cristal Hymmnos ancestral de reinicialização vital)",
            "Mana Claire": "クレアお姉ちゃん (Tratamento afetivo filial canônico usado por Aurica)"
        },
        "alertas_para_proximo_bloco": "FIM DO CORPUS DE EVENTOS (Gran Finale)! BLK_EVD_090 é o último bloco de história e eventos de Ar tonelico: Melody of Elemia, completando 100% de todas as 20.304 falas do roteiro do jogo!"
    },
    "curated_lines": curated_lines_output,
    "dialogues": dialogues_output
}

output_path = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_090_output.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_obj, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully generated and saved {output_path}!")

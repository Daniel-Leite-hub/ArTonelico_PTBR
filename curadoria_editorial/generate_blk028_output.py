# -*- coding: utf-8 -*-
"""Script gerador e validador da curadoria editorial do bloco BLK_EVD_028."""

import json
import sys
from pathlib import Path

# Adiciona o diretório de ferramentas ao sys.path para importar o validador oficial
sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\tools")
from curadoria_validate import validate_batch, validate_line

INPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_028_input.json")
OUTPUT_PATH = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_028_output.json")

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    input_data = json.load(f)

raw_dialogues = input_data["dialogues"]
assert len(raw_dialogues) == 198, f"Esperado 198 falas, obtido {len(raw_dialogues)}"

curations = {
    # =========================================================================
    # EVENT: Event/137.evd (IDs 7062 - 7098) [37 falas] - Avaliação da Nave e Subida da Torre
    # =========================================================================
    7062: (
        "Esse... é o seu dirigível?",
        "rewritten",
        "Krusche examinando os destroços da nave de Lyner pela primeira vez."
    ),
    7063: (
        "É. ...E então? O que acha?",
        "rewritten",
        "Lyner indagando a opinião técnica da engenheira."
    ),
    7064: (
        "Incrível...\nÉ bem diferente da nossa tecnologia...",
        "rewritten",
        "Krusche impressionada com o design e os componentes desconhecidos."
    ),
    7065: (
        "Se importa se eu der uma examinada nele?",
        "rewritten",
        "Krusche pedindo permissão entusiasmada para abrir o maquinário."
    ),
    7066: (
        "Uff...",
        "rewritten",
        "Krusche soltando o ar após a checagem técnica (sem rubrica *suspiro*)."
    ),
    7067: (
        "Descobriu alguma coisa?!",
        "rewritten",
        "Lyner ansioso pelo diagnóstico dos danos."
    ),
    7068: (
        "Descobri, sim.",
        "rewritten",
        "Krusche direta e pragmática."
    ),
    7069: (
        "Que vamos precisar de 18.326.991 Leaf\npara consertar essa belezinha.",
        "rewritten",
        "Krusche cravando o orçamento absurdo de 18 milhões de Leaf."
    ),
    7070: (
        "Q-que loucura é essa?!",
        "rewritten",
        "Lyner estupefato e boquiaberto diante da cifra astronômica."
    ),
    7071: (
        "Eu só dei uma olhada por cima,\nmas são coisas que eu jamais conseguiria arranjar sozinha.",
        "rewritten",
        "Krusche explicando a escassez dos componentes necessários."
    ),
    7072: (
        "Em teoria, consertar não é impossível,\nmas...",
        "rewritten",
        "Krusche ponderando os limites da engenharia local."
    ),
    7073: (
        "...Não tem jeito mesmo?",
        "rewritten",
        "Lyner insistindo por uma saída."
    ),
    7074: (
        "Você achou que aquele valor de antes\nera brincadeira, né?",
        "rewritten",
        "Krusche confrontando a descrença de Lyner."
    ),
    7075: (
        "É difícil de acreditar do nada.\nAchei que você tivesse inventado o maior número que veio à cabeça.",
        "rewritten",
        "Lyner justificando seu choque com bom humor defensivo."
    ),
    7076: (
        "Eu fiz as contas direitinho, viu?\nE digo mais: eu nem olhei tudo ainda.",
        "rewritten",
        "Krusche alertando que o valor real pode ser ainda mais salgado."
    ),
    7077: (
        "Não sei como as coisas funcionam em Platina,\nmas aqui embaixo isso exige uma tecnologia avançadíssima.",
        "rewritten",
        "Krusche destacando o abismo tecnológico entre Platina e o Mundo Inferior."
    ),
    7078: (
        "Para consertar isso, precisaríamos de fundidores\ne pesquisadores de ponta... em escala institucional.",
        "rewritten",
        "Krusche delineando a impossibilidade prática de conserto imediato."
    ),
    7079: (
        "......",
        "approved_as_is",
        "Pausa desolada de Lyner assimilando o veredito."
    ),
    7080: (
        "Entendi... Não tem como, então...\nDroga, eu estava tão esperançoso...",
        "rewritten",
        "Desilusão amarga de Lyner ao ver seu meio de transporte inviabilizado."
    ),
    7081: (
        "Acho que avisei para não criar expectativas.\nSinto muito, mas é melhor desistir disso.",
        "rewritten",
        "Krusche empática, porém firme ao cortar esperanças vãs."
    ),
    7082: (
        "O jeito é pensar em outro caminho...",
        "rewritten",
        "Lyner buscando alternativas para retornar a Platina."
    ),
    7083: (
        "Jack.",
        "approved_as_is",
        "Lyner chamando o veterano mercenário."
    ),
    7084: (
        "......",
        "approved_as_is",
        "Silêncio atento de Jack aguardando a fala do rapaz."
    ),
    7085: (
        "Ei, lembra daquela história de escalar a Torre\nque você comentou outro dia...? Não dava para tentar?",
        "rewritten",
        "Lyner cogitando a travessia vertical da Torre a pé."
    ),
    7086: (
        "Olha, eu andei pensando...\nSerá que a gente não consegue subir a Torre a pé?",
        "rewritten",
        "Lyner insistindo na ideia como única tábua de salvação restante."
    ),
    7087: (
        "O... o quê?! Escalar... a Torre?!",
        "rewritten",
        "Jack atônito diante da loucura da proposta."
    ),
    7088: (
        "...Não tem como mesmo, né?",
        "rewritten",
        "Lyner percebendo a reação atônita de Jack."
    ),
    7089: (
        "Não... não é que seja impossível.",
        "rewritten",
        "Jack admitindo que a rota existe em teoria."
    ),
    7090: (
        "Eu já devia imaginar que você viria com essa...",
        "rewritten",
        "Jack suspirando com o pragmatismo inconsequente do garoto."
    ),
    7091: (
        "Como já te avisei antes, no meio do caminho\nvive a [Tribo Teru]. E qualquer humano que tente subir...",
        "rewritten",
        "Jack reforçando a hostilidade territorial da Tribo Teru."
    ),
    7092: (
        "Eu sei.",
        "rewritten",
        "Lyner ciente dos perigos mortais."
    ),
    7093: (
        "......",
        "approved_as_is",
        "Jack encarando a determinação obstinada de Lyner."
    ),
    7094: (
        "A Tribo Teru vive bem na encosta da Torre\nexatamente para impedir que os humanos subam.",
        "rewritten",
        "Jack explicando a razão de ser da vigília dos Teru."
    ),
    7095: (
        "Eles não vão dar passagem nem a pau!",
        "rewritten",
        "Jack enfático e realista sobre a intransigência dos guardiões."
    ),
    7096: (
        "Mas... já não sobrou nenhuma outra alternativa.",
        "rewritten",
        "Lyner convicto de que não tem escolha senão arriscar tudo."
    ),
    7097: (
        "...Eu não recomendo, garoto.\nO mais prudente seria pensar em outra saída.",
        "rewritten",
        "Jack aconselhando cautela ao jovem cavaleiro."
    ),
    7098: (
        "......",
        "approved_as_is",
        "Lyner pensativo absorvendo a gravidade do dilema."
    ),

    # =========================================================================
    # EVENT: Event/150.evd (IDs 7099 - 7171) [73 falas] - Emboscada e Fim de Bourd
    # =========================================================================
    7099: (
        "Parem aí mesmo!",
        "rewritten",
        "Ordem imperativa e estridente barrando o caminho da comitiva."
    ),
    7100: (
        "Hã?!",
        "rewritten",
        "Lyner sobressaltado com a interrupção súbita."
    ),
    7101: (
        "...Bourd!!",
        "rewritten",
        "Lyner reconhecendo com repulsa o comandante da Tenba."
    ),
    7102: (
        "Ora, ora, nobre comitiva.\nQue coincidência nos encontrarmos num cafundó desses.",
        "rewritten",
        "Bourd com sua ironia peçonhenta e arrogante de sempre."
    ),
    7103: (
        "...Misha.",
        "approved_as_is",
        "Jack reconhecendo Misha ao lado de Bourd com preocupação velada."
    ),
    7104: (
        "...Miserável! Que palhaçada é essa?!",
        "rewritten",
        "Radolf indignado e em guarda diante do vilão."
    ),
    7105: (
        "Ora, nada de mais. Só recebi ordens\npara impedir que vocês subam a Torre.",
        "rewritten",
        "Bourd desdenhando da missão oficial da corporação."
    ),
    7106: (
        "O-o quê?!",
        "rewritten",
        "Lyner indignado com o bloqueio deliberado."
    ),
    7107: (
        "Droga... Baixamos a guarda demais\nlá na Placa Hexagonal...",
        "rewritten",
        "Radolf culpando-se pelo descuido na retaguarda."
    ),
    7108: (
        "...Que corja mais asquerosa...\nessa tal de Tenba não tem limites...",
        "rewritten",
        "Jack expressando seu asco profundo pela baixeza moral da Tenba."
    ),
    7109: (
        "Mas! Porém!!\nIsso tudo pouco me importa!",
        "rewritten",
        "Bourd rompendo com a fachada corporativa em surto de egolatria."
    ),
    7110: (
        "Assim que Mir ressuscitar,\nestorvos como a Tenba ou a Igreja vão sumir do mapa!",
        "rewritten",
        "Bourd expondo sua verdadeira aliança fanática com a deusa viral Mir."
    ),
    7111: (
        "...Mir?!",
        "rewritten",
        "Lyner estarrecido com a revelação da conspiração cósmica."
    ),
    7112: (
        "Mais importante do que isso...\no meu sangue está fervendo de ódio nas veias!",
        "rewritten",
        "Bourd cuspindo veneno pessoal contra Lyner."
    ),
    7113: (
        "Vocês pisotearem com gosto os meus planos!\nPor sua culpa, meu cronograma foi todo pro vinagre!",
        "rewritten",
        "Bourd furioso pelo fracasso sucessivo de suas maquinações."
    ),
    7114: (
        "Não é mesmo, Lyner Barsett?!",
        "rewritten",
        "Bourd vociferando o nome de seu arqui-inimigo com sanha assassina."
    ),
    7115: (
        "...!",
        "approved_as_is",
        "Reação tensa de Lyner empunhando a espada."
    ),
    7116: (
        "Se eu não esmagar você com as minhas próprias mãos,\nnunca vou ter paz...",
        "rewritten",
        "Bourd sedento de sangue prometendo execução sumária."
    ),
    7117: (
        "Hoje, aqui! Neste exato instante!\nVou acertar as contas com você de uma vez por todas!!",
        "rewritten",
        "Clímax da ameaça de Bourd declarando o combate decisivo."
    ),
    7118: (
        "E então, Lyner? Qual é a sensação de ver a Misha\nmostrando as presas para você...? Hehehe...",
        "rewritten",
        "Bourd tripudiando sadicamente com a suposta traição da Reyvateil."
    ),
    7119: (
        "Misha...",
        "approved_as_is",
        "Lyner dilacerado ao ver a amiga de infância usada como peão."
    ),
    7120: (
        "Misha!! O que deu em você?!",
        "rewritten",
        "Jack chamando Misha à razão em tom exasperado."
    ),
    7121: (
        "Entregou corpo e alma para a Tenba,\npor acaso?!",
        "rewritten",
        "Jack questionando indignado a subserviência dela."
    ),
    7122: (
        "Ora, vejo que você também\ntem uma história com ela.",
        "rewritten",
        "Bourd percebendo a ligação afetiva prévia entre Jack e Misha."
    ),
    7123: (
        "Interessante. Assim o espetáculo\nfica muito mais divertido!",
        "rewritten",
        "Bourd saboreando a dramaticidade sádica do reencontro."
    ),
    7124: (
        "...Enlouqueceu de vez.",
        "rewritten",
        "Radolf constatando a loucura patológica do rival."
    ),
    7125: (
        "Muito bem! Vou me deliciar com essa cara de desespero\nenquanto trucido cada um de vocês!",
        "rewritten",
        "Bourd partindo para o massacre com volúpia."
    ),
    7126: (
        "Guh... Miseráveis...",
        "rewritten",
        "Bourd acusando o golpe sob a retaliação do grupo (sem decalque teatral)."
    ),
    7127: (
        "Misha... a magia! Já acumulou poder suficiente!\nDispare de uma vez!!",
        "rewritten",
        "Bourd acuado exigindo que Misha solte a Magia da Canção."
    ),
    7128: (
        "...Ainda não.\nUma miséria dessas nem de longe é suficiente.",
        "rewritten",
        "Misha respondendo com frieza calculista e misteriosa."
    ),
    7129: (
        "O quê...? Sua pirralha...\nPretende desobedecer às minhas ordens?!",
        "rewritten",
        "Bourd tomado pelo choque e pela desconfiança repentina."
    ),
    7130: (
        "Misha!!",
        "approved_as_is",
        "Bourd berrando exasperado."
    ),
    7131: (
        "Eu já te avisei antes.\nJamais vou abaixar a cabeça pras suas ordens!",
        "rewritten",
        "Misha cravando sua insubordinação inegociável."
    ),
    7132: (
        "...Gah!! N-não me diga que...",
        "rewritten",
        "Bourd percebendo a arapuca mortal em que se meteu."
    ),
    7133: (
        "Olha aqui, Bourd...\nVocê achava mesmo que uma Reyvateil era tão boba assim?",
        "rewritten",
        "Misha desmascarando a arrogância míope do vilão."
    ),
    7134: (
        "Você não tem ideia do quanto engoli a seco...\ndo quanto tive que aguentar... só esperando por este segundo...",
        "rewritten",
        "Misha revelando a longa e dolorosa espera pelo momento da virada."
    ),
    7135: (
        "Ei, e-espera aí um segundo!",
        "rewritten",
        "Bourd apavorado implorando por clemência."
    ),
    7136: (
        "Adeus, Bourd...\nE que seja para todo o sempre!!",
        "rewritten",
        "Veredito implacável de Misha disparando a magia devastadora."
    ),
    7137: (
        "Gwaaaaaaargh...!!",
        "rewritten",
        "Bourd sendo engolido e obliterado pela explosão luminosa."
    ),
    7138: (
        "Misha!",
        "approved_as_is",
        "Lyner correndo em socorro da amiga exausta."
    ),
    7139: (
        "......",
        "approved_as_is",
        "Silêncio atônito de Misha sentindo a poeira baixar."
    ),
    7140: (
        "Misha! Você tá bem?!",
        "rewritten",
        "Lyner amparando-a com ternura e alívio incontido."
    ),
    7141: (
        "......",
        "approved_as_is",
        "Misha encarando os olhos de Lyner com lágrimas represadas."
    ),
    7142: (
        "Lyner... me perdoa...\nPor favor, me perdoa...",
        "rewritten",
        "Misha desmoronando em remorso pelas preocupações causadas."
    ),
    7143: (
        "...Misha?",
        "rewritten",
        "Lyner surpreso com o pedido sincero de desculpas."
    ),
    7144: (
        "Eu... fiz você se preocupar tanto comigo...",
        "rewritten",
        "Misha confessando o peso da culpa em seu coração."
    ),
    7145: (
        "Me desculpa, Lyner...\nMe desculpa de verdade...",
        "rewritten",
        "Misha derramando lágrimas e pedindo perdão."
    ),
    7146: (
        "...Misha, obrigado.",
        "rewritten",
        "Lyner respondendo com afeto transbordante em vez de repreensão."
    ),
    7147: (
        "...Hã?!",
        "rewritten",
        "Misha desconcertada e pega de surpresa pela gratidão dele."
    ),
    7148: (
        "Deve ter sido muito difícil aguentar isso tudo, né?",
        "rewritten",
        "Lyner reconhecendo o heroísmo silencioso e a dor solitária dela."
    ),
    7149: (
        "...Lyner!!",
        "rewritten",
        "Misha se desmanchando ao sentir a compreensão do amigo."
    ),
    7150: (
        "Bwaaaah... snif... hic...",
        "rewritten",
        "Choro convulso e pueril de alívio nos braços de Lyner (zero rubricas teatrais)."
    ),
    7151: (
        "......",
        "approved_as_is",
        "Aurica observando a cena em silêncio delicado e reflexivo."
    ),
    7152: (
        "Harm...",
        "approved_as_is",
        "Misha reconhecendo o velho amigo e protetor Teru."
    ),
    7153: (
        "Misha... É você mesma?\nNão cresceu nem um centímetro, garota?",
        "rewritten",
        "Jack com seu humor ranzinza disfarçando a emoção do reencontro."
    ),
    7154: (
        "...Ehehe, pois é.\nAconteceram muitas coisas. Depois eu te conto com calma.",
        "rewritten",
        "Misha sem graça desconversando sobre seu segredo de Reyvateil Origin."
    ),
    7155: (
        "Mas e você, Harm? O que aconteceu com o seu braço?!\nPor que virou uma máquina?!",
        "rewritten",
        "Misha notando o implante cibernético com espanto genuíno."
    ),
    7156: (
        "Hã? Ah, isso aqui?\nDigamos que tem história aí. Uma hora dessas eu conto.",
        "rewritten",
        "Jack devolvendo a desconversa no mesmo tom arrastado."
    ),
    7157: (
        "Ai, francamente...\nQue conversinha mais irritante de se ouvir.",
        "rewritten",
        "Krusche perdendo a paciência com os mistérios em série da dupla."
    ),
    7158: (
        "Krusche!",
        "approved_as_is",
        "Misha surpresa ao ver a engenheira diante de si."
    ),
    7159: (
        "Bem-vinda de volta, Misha.\nQue bom ter você aqui. Fiquei preocupada de verdade...",
        "rewritten",
        "Krusche demonstrando carinho espontâneo antes da provocação."
    ),
    7160: (
        "...Krusche.\nVocê... se preocupava tanto assim comigo...?",
        "rewritten",
        "Misha sensibilizada com a demonstração de afeto."
    ),
    7161: (
        "Mas é claro! Você tá me devendo 87 Combos Dokkoi,\n59 tigelas de Gelo Ralado, 9 peixes secos e 2 Megamilks!",
        "rewritten",
        "Krusche revelando a hilária lista de dívidas astronômicas de comida."
    ),
    7162: (
        "Ugh!! ...Mas você não toma jeito mesmo...",
        "rewritten",
        "Misha indignada com a cobrança mesquinha e descarada."
    ),
    7163: (
        "E vê se não esquece que você me deve 58 Combos Dokkoi,\n118 Balas de Gato e 21 Megamilks!!",
        "rewritten",
        "Misha contra-atacando na mesma moeda com seu caderninho de cobranças."
    ),
    7164: (
        "...!! B-bom, de qualquer forma,\no importante é que voltou sã e salva. Fufufu...",
        "rewritten",
        "Krusche desconversando com risinho travesso após ser enquadrada."
    ),
    7165: (
        "Digo o mesmo... Fufufu.",
        "rewritten",
        "Misha rindo cúmplice da rinha infantil de dívidas."
    ),
    7166: (
        "...D-do que é que vocês duas\nestão falando, afinal...?",
        "rewritten",
        "Jack atônito sem entender nada da matemática etílica/gastronômica."
    ),
    7167: (
        "......",
        "approved_as_is",
        "Lyner sorrindo aliviado com a volta da normalidade caótica."
    ),
    7168: (
        "Vamos, não estávamos com pressa?\nPodem continuar a conversa no caminho. Em marcha!",
        "rewritten",
        "Radolf convocando todos à ordem com autoridade militar e bom humor."
    ),
    7169: (
        "É, tem razão.\nAinda temos uma longa jornada pela frente.",
        "rewritten",
        "Lyner concordando em acelerar o passo rumo aos objetivos."
    ),
    7170: (
        ".........",
        "approved_as_is",
        "Aurica silenciosa, guardando no íntimo a complexidade daquele retorno."
    ),
    7171: (
        "Misha entrou para o grupo!",
        "rewritten",
        "Notificação canônica de sistema da reintegração de Misha à equipe."
    ),

    # =========================================================================
    # EVENT: Event/441.evd (IDs 7172 - 7206) [35 falas] - Despertar e o Destino de Shurelia
    # =========================================================================
    7172: (
        "Ah, Lyner! Bom dia!",
        "rewritten",
        "Misha cumprimentando Lyner com sua energia matinal radiante."
    ),
    7173: (
        "Ah... Bom dia.",
        "rewritten",
        "Lyner respondendo meio aéreo e pensativo."
    ),
    7174: (
        "...O que foi?\nVocê parece meio cabisbaixo...",
        "rewritten",
        "Misha atenta à postura sombria do companheiro."
    ),
    7175: (
        "Hum? Ah...",
        "rewritten",
        "Lyner hesitando em trazer à tona seus tormentos."
    ),
    7176: (
        "...Tudo bem com você?",
        "rewritten",
        "Misha insistindo com doçura e preocupação sincera."
    ),
    7177: (
        "Não fica com essa carinha tão triste.",
        "rewritten",
        "Lyner tentando aliviar o semblante pesaroso da garota."
    ),
    7178: (
        "...Olha, Misha.\nDesculpa te pedir isso, mas posso desabafar com você?",
        "rewritten",
        "Lyner abrindo o coração para pedir conselho à amiga de infância."
    ),
    7179: (
        "O que é isso!\nMas é claro que pode!",
        "rewritten",
        "Misha acolhendo-o com generosidade e prontidão imediatas."
    ),
    7180: (
        "...Entendo.\nVocê sonhou com a Senhora Shurelia...",
        "rewritten",
        "Misha assimilando a confissão sobre o sonho angustiante."
    ),
    7181: (
        "...Foi.",
        "rewritten",
        "Lyner confirmando a dor que ainda o assombra."
    ),
    7182: (
        "Quando olho ao redor,\ntodo mundo parece tão feliz...",
        "rewritten",
        "Lyner contrastando a festa da paz com o luto velado em seu peito."
    ),
    7183: (
        "A Mir sumiu, os vírus desapareceram...\nNão há mais nada para assombrar as pessoas.",
        "rewritten",
        "Lyner recapitulando o fim aparente da grande crise de Sol Ciel."
    ),
    7184: (
        "...Mas...",
        "rewritten",
        "Pausa densa carregada de inconformismo moral."
    ),
    7185: (
        "Eu simplesmente não consigo engolir...\nque aquele tenha sido o melhor desfecho...",
        "rewritten",
        "Lyner rejeitando a resignação com a perda da Administradora."
    ),
    7186: (
        "Não pode ser... Inacreditável...\nSe entoar esta Canção, você vai desaparecer junto comigo!",
        "rewritten",
        "Mir apavorada no flashback ao perceber o pacto de auto-aniquilação."
    ),
    7187: (
        "...Senhora Shurelia! Não pode ser!!",
        "rewritten",
        "Lyner em desespero no eco de sua memória presenciando o sacrifício."
    ),
    7188: (
        "Estou ciente do preço.\nMesmo assim, eu... este mundo...",
        "rewritten",
        "Shurelia sublime e serena abraçando o martírio sagrado."
    ),
    7189: (
        "Eu quero... salvar este mundo!!",
        "rewritten",
        "Grito heroico de amor universal da guardiã de Ar tonelico."
    ),
    7190: (
        "Eu quero tanto... salvar este mundo...",
        "rewritten",
        "Eco suave e etéreo da prece final de Shurelia se apagando."
    ),
    7191: (
        "Naquele momento, nós partimos\npara resgatar a Senhora Shurelia.",
        "rewritten",
        "Lyner rememorando a promessa de cavalaria que fizera."
    ),
    7192: (
        "Mas... não fomos capazes de salvá-la.",
        "rewritten",
        "Amarga admissão de impotência que rói a honra de Lyner."
    ),
    7193: (
        "...Lyner.",
        "approved_as_is",
        "Misha partilhando da dor daquele fardo com profundo respeito."
    ),
    7194: (
        "Pode ser que a Senhora Shurelia tenha nos confiado este mundo...",
        "rewritten",
        "Lyner reconhecendo o legado espiritual deixado pela Deusa."
    ),
    7195: (
        "Depois que a batalha acabou e descemos,\neu fiquei feliz em ver o mundo em paz...",
        "rewritten",
        "Lyner descrevendo o breve alívio que sentiu ao retornar ao solo."
    ),
    7196: (
        "Fiquei com a sensação de dever cumprido,\nmas não era verdade.",
        "rewritten",
        "Lucidez dolorosa de que a vitória foi incompleta e custosa demais."
    ),
    7197: (
        "...Eu entendo bem o que você sente.\nIsso também não me sai da cabeça.",
        "rewritten",
        "Misha validando a inquietação moral do cavaleiro."
    ),
    7198: (
        "Mas... se isso já ficou no passado...",
        "rewritten",
        "Misha apontando com prudência o peso da realidade consumada."
    ),
    7199: (
        "Talvez ainda exista um jeito de salvá-la.",
        "rewritten",
        "Centelha de esperança inabalável brilhando nos olhos de Lyner."
    ),
    7200: (
        "Hã?! ...E-espera um pouco...",
        "rewritten",
        "Misha sobressaltada diante da ousadia da ideia."
    ),
    7201: (
        "A Senhora Shurelia... morreu de verdade?\nAquilo foi mesmo o que chamamos de 'morte'?",
        "rewritten",
        "Questionamento filosófico profundo sobre a natureza existencial da deusa."
    ),
    7202: (
        "Não sei explicar direito... mas sinto\nque ainda resta algo que não tentamos.",
        "rewritten",
        "Intuição heroica de Lyner recusando o fatalismo cego."
    ),
    7203: (
        "......",
        "approved_as_is",
        "Misha refletindo sobre o mistério da condição de Shurelia."
    ),
    7204: (
        "Tem razão. Desistir agora talvez seja precipitado demais.",
        "rewritten",
        "Misha alinhando seu coração à coragem de Lyner."
    ),
    7205: (
        "Olha, Lyner.\nPor que não vamos conversar com o Leard?",
        "rewritten",
        "Misha sugerindo consultar a autoridade patriarcal e acadêmica de Leard."
    ),
    7206: (
        "Misha entrou para o grupo!",
        "rewritten",
        "Confirmação de sistema da renovação de parceria com Misha."
    ),

    # =========================================================================
    # EVENT: Event/266.evd (IDs 7207 - 7259) [53 falas] - Busca, Lição de Aurica e Power Cylinder
    # =========================================================================
    7207: (
        "Um beco sem saída...",
        "rewritten",
        "Lyner frustrado ao encontrar uma barreira intransponível."
    ),
    7208: (
        "A Misha também não tá por aqui...",
        "rewritten",
        "Krusche desapontada com a busca infrutífera."
    ),
    7209: (
        "Vamos fazer uma pausa por aqui.",
        "rewritten",
        "Jack sugerindo um respiro tático para reorganizar os pensamentos."
    ),
    7210: (
        "Ei, Lyner... Você fez algo com a Misha?\nPor acaso você pulou a cerca?",
        "rewritten",
        "Aurica soltando sua suspeita cândida e incisiva com cara lavada."
    ),
    7211: (
        "C-claro que não!",
        "rewritten",
        "Lyner em choque absoluto rechaçando a insinuação embaraçosa."
    ),
    7212: (
        "Quando a Aurica fala isso,\nsoa assustadoramente real...",
        "rewritten",
        "Krusche comentando com ironia ácida a gravidade de Aurica."
    ),
    7213: (
        "Na verdade...",
        "approved_as_is",
        "Lyner começando a relatar o desentendimento com Misha."
    ),
    7214: (
        "Entendo. Mas eu compreendo\no que a Misha tá sentindo.",
        "rewritten",
        "Aurica demonstrando empatia pura pela rival de infância."
    ),
    7215: (
        "A Misha é alguém que se sente solitária\ncom muita facilidade, sabe?",
        "rewritten",
        "Aurica desvendando a faceta vulnerável que Misha oculta com birras."
    ),
    7216: (
        "Por isso, quando você tenta deixá-la para trás,\nela deve ficar muito aflita.",
        "rewritten",
        "Aurica explicando a raiz da angústia da donzela cantora."
    ),
    7217: (
        "Mesmo sabendo que você faz isso\npor pura consideração.",
        "rewritten",
        "Aurica reconhecendo que a intenção de Lyner era nobre e protetora."
    ),
    7218: (
        "...É mesmo?",
        "rewritten",
        "Lyner surpreso diante daquela revelação psicológica."
    ),
    7219: (
        "Sim. Como posso dizer...\nCom quem não temos intimidade, a gente é cheio de dedos, né?",
        "rewritten",
        "Aurica traçando a brilhante analogia das convenções sociais."
    ),
    7220: (
        "Mas com quem é de casa, a gente reclama sem medo,\npede colo, até dá trabalho às vezes...",
        "rewritten",
        "Aurica definindo com sensibilidade o calor do convívio familiar."
    ),
    7221: (
        "Para a Misha, cada vez que você tenta protegê-la sendo educado,\nela sente você cada vez mais distante.",
        "rewritten",
        "Clímax da lição emocional de Aurica sobre o perigo do excesso de zelo."
    ),
    7222: (
        "Você devia confiar mais na Misha,\ne se permitir contar com o apoio dela também.",
        "rewritten",
        "Conselho amoroso e maduro para Lyner se deixar vulnerável diante dela."
    ),
    7223: (
        "É verdade... Acho que começo a entender.",
        "rewritten",
        "Lyner iluminado pela perspectiva clarividente de Aurica."
    ),
    7224: (
        "Além disso, ficar só esperando é doloroso demais...\nsem poder fazer nada para ajudar.",
        "rewritten",
        "Aurica falando de cadeira sobre o horror do desamparo e da espera."
    ),
    7225: (
        "Se estivermos juntos por perto,\nao menos podemos dar o nosso melhor.",
        "rewritten",
        "Manifesto de solidariedade e coragem das Reyvateils em batalha."
    ),
    7226: (
        "...Você tem toda a razão.\nPercebi isso na pele quando a Misha sumiu.",
        "rewritten",
        "Lyner assumindo plenamente o erro de tentar poupá-la à força."
    ),
    7227: (
        "Mas, Aurica, você entende tão bem dessas coisas...\nFiquei até surpreso.",
        "rewritten",
        "Lyner admirado com a maturidade emocional inesperada dela."
    ),
    7228: (
        "Afinal de contas... eu também...\nsou... uma mulher...",
        "rewritten",
        "Aurica murmurando com voz enfraquecida e respiração entrecortada."
    ),
    7229: (
        "...Aurica?",
        "rewritten",
        "Lyner percebendo a fraqueza súbita no tom dela."
    ),
    7230: (
        "Aurica?!",
        "rewritten",
        "Lyner em choque ao vê-la vacilar nos joelhos."
    ),
    7231: (
        "Ei, você tá bem?! Fica firme!",
        "rewritten",
        "Lyner amparando-a antes que caia desacordada no chão."
    ),
    7232: (
        "Lyner?!",
        "approved_as_is",
        "Misha chegando apressada ao ouvir os brados."
    ),
    7233: (
        "Aurica!",
        "approved_as_is",
        "Radolf acorrendo para prestar socorro à donzela da Igreja."
    ),
    7234: (
        "Misha! Radolf!\nSocorro, a Aurica...!",
        "rewritten",
        "Lyner em pânico pedindo auxílio imediato aos companheiros."
    ),
    7235: (
        "A Aurica acabou causando transtornos a você.\nPeço desculpas.",
        "rewritten",
        "Radolf, como superior e protetor sacerdotal, assumindo a responsabilidade."
    ),
    7236: (
        "Nós cuidaremos dela daqui em diante.\nNão se preocupe, Lyner, e cumpra a sua missão.",
        "rewritten",
        "Ayatane transmitindo serenidade e liberando o amigo para o dever."
    ),
    7237: (
        "A propósito, por que o Ayatane tá com você?",
        "rewritten",
        "Lyner intrigado com a presença repentina de Ayatane ali."
    ),
    7238: (
        "Pois é. Seja o estado da Aurica ou o Ayatane aqui...\né um mistério atrás do outro.",
        "rewritten",
        "Krusche pontuando as pontas soltas com seu ceticismo aguçado."
    ),
    7239: (
        "Ayatane, Radolf.\nObrigado por cuidarem da Misha.",
        "rewritten",
        "Lyner agradecendo o empenho e a lealdade dos dois cavalheiros."
    ),
    7240: (
        "Nós é que agradecemos por acudir a Aurica.",
        "rewritten",
        "Ayatane retribuindo a cortesia com nobreza e compostura."
    ),
    7241: (
        "Aurica... você tá bem?",
        "rewritten",
        "Lyner aproximando-se com carinho e apreensão do leito da jovem."
    ),
    7242: (
        "Sim, tô bem...\nDesculpa ter te preocupado tanto.",
        "rewritten",
        "Aurica esboçando um sorriso tímido e pedindo perdão pelo susto."
    ),
    7243: (
        "Felizmente, o nosso lado teve ótimos avanços.\nFalta apenas um passo para o despertar da Deusa Eoria.",
        "rewritten",
        "Ayatane trazendo o relatório auspicioso dos ritos sacerdotais."
    ),
    7244: (
        "Que bom, fico feliz por vocês...\nJá por aqui, estamos prestes a fazer uma aposta arriscadíssima.",
        "rewritten",
        "Lyner dividindo a apreensão diante do plano audacioso que planeja."
    ),
    7245: (
        "É mesmo...?\nVou aguardar ansioso pelas boas notícias.",
        "rewritten",
        "Ayatane depositando fé inabalável no triunfo de Lyner."
    ),
    7246: (
        "Boa sorte para nós dois.",
        "rewritten",
        "Lyner selando a aliança fraterna com o companheiro de armas."
    ),
    7247: (
        "Certo. Nós estamos com pressa,\nentão vamos indo na frente.",
        "rewritten",
        "Ayatane despedindo-se para conduzir os rituais com urgência."
    ),
    7248: (
        "Lyner, muito obrigada.\nDesculpa ter te preocupado ainda mais.",
        "rewritten",
        "Aurica reiterando sua gratidão terna antes de partir com a comitiva sacra."
    ),
    7249: (
        "Ora, ora.\nAo menos por enquanto, esse assunto tá resolvido.",
        "rewritten",
        "Jack respirando aliviado com a poeira que finalmente assentou."
    ),
    7250: (
        "Misha... que alívio ver que você tá a salvo.\nFiquei tão preocupado com você...",
        "rewritten",
        "Lyner voltando-se para Misha com o coração desarmado de censuras."
    ),
    7251: (
        "Lyner... me perdoa.\nEu não pensei nem um pouquinho no que você sentia...",
        "rewritten",
        "Misha comovida reconhecendo sua imaturidade no desentendimento."
    ),
    7252: (
        "Eu é que peço desculpas.\nQuis tanto te proteger que acabei foi te machucando.",
        "rewritten",
        "Lyner assumindo o aprendizado trazido pelas palavras de Aurica."
    ),
    7253: (
        "...Lyner.",
        "approved_as_is",
        "Misha comovida pela sinceridade do cavaleiro."
    ),
    7254: (
        "Ah, é mesmo! Adivinha só:\neu achei o [Power Cylinder]!",
        "rewritten",
        "Misha comemorando com orgulho radiante o achado do artefato."
    ),
    7255: (
        "Opa! Mandou bem, garota!",
        "rewritten",
        "Jack parabenizando Misha com entusiasmo sincero."
    ),
    7256: (
        "Mandou bem!\nAgora sim o trabalho de verdade começa.",
        "rewritten",
        "Krusche vibrando com a conquista técnica que destrava a aeronave."
    ),
    7257: (
        "Falou e disse. Bora voltar pro Beco Vagalume\ne botar pra quebrar!",
        "rewritten",
        "Jack animado chamando o bando de volta ao distrito comercial."
    ),
    7258: (
        "Você obteve o [Power Cylinder]!",
        "rewritten",
        "Mensagem de notificação canônica de obtenção do item-chave."
    ),
    7259: (
        "Aurica saiu do grupo.\nMisha entrou para o grupo!",
        "rewritten",
        "Atualização canônica de formação da equipe com saída de Aurica e entrada de Misha."
    )
}

print(f"Total de falas mapeadas: {len(curations)}")
assert len(curations) == 198, f"Esperado 198 falas mapeadas, obtido {len(curations)}"

curated_dialogues = []
translations_list = []
lines_rewritten = 0
lines_approved_as_is = 0

validation_errors = {}

for d in raw_dialogues:
    d_id = d["id"]
    orig_en = d.get("original_en", "")
    orig_jp = d.get("original_jp", "")
    current_ptbr = d.get("current_ptbr", "")
    speaker = d.get("speaker", "")
    event_file = d.get("event_file", "")
    speaker_id = d.get("speaker_id")
    
    curated_text, verdict, rationale = curations[d_id]
    
    # Validação determinística
    errs = validate_line(d_id, orig_en, curated_text)
    if errs:
        validation_errors[d_id] = errs
        
    if verdict == "rewritten":
        lines_rewritten += 1
    elif verdict == "approved_as_is":
        lines_approved_as_is += 1
        
    entry = {
        "id": d_id,
        "event_file": event_file,
        "speaker_id": speaker_id,
        "speaker": speaker,
        "original_jp": orig_jp,
        "original_en": orig_en,
        "current_ptbr": current_ptbr,
        "curated_ptbr": curated_text,
        "text": curated_text,
        "verdict": verdict,
        "rationale": rationale
    }
    curated_dialogues.append(entry)
    translations_list.append({
        "id": d_id,
        "text": curated_text
    })

if validation_errors:
    print(f"ERROS DE VALIDAÇÃO TÉCNICA DETECTADOS ({len(validation_errors)}):")
    for d_id, err_list in validation_errors.items():
        print(f"  ID {d_id}: {err_list}")
    sys.exit(1)
else:
    print("Todas as 198 falas passaram com 100% de sucesso no Hard Gate Técnico!")

highlights = [
    {
        "id": 7069,
        "speaker": "Krusche / Lyner",
        "description": "Krusche calcula com cinismo pragmático o orçamento estratosférico de 18.326.991 Leaf para consertar o dirigível avariado, forçando Lyner a considerar a escalada a pé da Torre através da temida Tribo Teru."
    },
    {
        "id": 7110,
        "speaker": "Bourd / Lyner / Radolf",
        "description": "Bourd embosca a comitiva e expõe seu delírio apocalíptico de que o despertar de Mir aniquilará tanto a Tenba quanto a Igreja, jurando vingança pessoal e sangrenta contra Lyner por arruinar seus planos."
    },
    {
        "id": 7134,
        "speaker": "Misha / Bourd",
        "description": "Clímax da emboscada onde Misha revela que acumulou Magia da Canção propositalmente para ludibriar Bourd e disparar um raio devastador que oblitera o comandante da Tenba para todo o sempre."
    },
    {
        "id": 7148,
        "speaker": "Lyner / Misha",
        "description": "Reencontro comovente e puro onde Lyner acolhe o choro convulsivo e as desculpas de Misha com profunda empatia, agradecendo pelo heroísmo solitário que ela suportou."
    },
    {
        "id": 7161,
        "speaker": "Krusche / Misha / Jack",
        "description": "Duelo cômico de cobranças gastronômicas onde Krusche e Misha disputam dívidas homéricas de dezenas de Combos Dokkoi, tigelas de Gelo Ralado, peixes secos, Balas de Gato e Megamilks sob o olhar atônito de Jack."
    },
    {
        "id": 7186,
        "speaker": "Mir / Shurelia / Lyner",
        "description": "Flashback dramático do sacrifício supremo da Senhora Shurelia entoando a Canção que a consome junto com Mir, desencadeando a recusa convicta de Lyner em aceitar o martírio dela como final."
    },
    {
        "id": 7221,
        "speaker": "Aurica / Lyner",
        "description": "Aula magistral de sensibilidade feminina onde Aurica explica a Lyner que a superproteção educada distancia as pessoas amadas e aconselha-o a confiar em Misha e a se deixar apoiar por ela."
    },
    {
        "id": 7254,
        "speaker": "Misha / Jack / Krusche",
        "description": "Misha revela radiante a recuperação do artefato crucial [Power Cylinder], abrindo caminho para a grande virada técnica e o retorno festivo da equipe ao Beco Vagalume."
    }
]

new_terms = {
    "Power Cylinder": {
        "pt": "Power Cylinder",
        "gender": "masculino",
        "number": "singular",
        "category": "Chave / Mecanismo",
        "note": "パワーシリンダー. Cilindro-chave para desligamento de emergência do gerador de força."
    },
    "Dokkoi Set": {
        "pt": "Combo Dokkoi",
        "gender": "masculino",
        "number": "singular",
        "category": "Culinária / Item",
        "note": "ドッコイ定食. Refeição substancial e tradicional consumida em Platina e Sol Ciel."
    },
    "Kitty Candy": {
        "pt": "Bala de Gato",
        "gender": "feminino",
        "number": "singular",
        "category": "Item / Alimento",
        "note": "猫飴. Doce tradicional felino apreciado por Misha em Sol Ciel."
    },
    "Shaved Ice": {
        "pt": "Gelo Ralado",
        "gender": "masculino",
        "number": "singular",
        "category": "Culinária / Doce",
        "note": "かちわり氷. Iguaria refrescante de gelo triturado consumida em Sol Ciel."
    },
    "Megamilk": {
        "pt": "Megamilk",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Bebida",
        "note": "メガミルク. Bebida láctea energizante consumida em grandes porções por Reyvateils."
    }
}

updated_address_matrix = {
    "Lyner": {
        "Misha": "Amizade íntima de infância e cumplicidade pura ('você / te'), acolhendo seu sofrimento e reconhecendo que tentar superprotegê-la foi um erro.",
        "Aurica": "Carinho fraterno e profunda gratidão pelas lições de maturidade emocional que ela transmitiu sobre a alma feminina.",
        "Krusche": "Parceria descontraída e bem-humorada ('você / te'), tolerando o choque do orçamento estratosférico da nave.",
        "Jack": "Respeito sincero ao calejado veterano Teru, buscando conselhos de sobrevivência na travessia da Torre."
    },
    "Misha": {
        "Lyner": "Ligação inseparável e arrependimento afetuoso ('Lyner', 'você'), chorando aliviada nos braços dele.",
        "Jack": "Tratamento de infância chamando-o pelo apelido familiar ('Harm'), admirando com espanto seu braço mecânico.",
        "Krusche": "Rivalidade doce e cômica trocando acusações de dívidas culinárias (Combos Dokkoi e Megamilks)."
    },
    "Aurica": {
        "Lyner": "Maturidade afetuosa e aconselhamento íntimo, ensinando-o a não afastar Misha por excesso de dedos e formalidade."
    }
}

scene_handoff = {
    "resumo_dramatico": "A constatação desoladora de Krusche sobre os custos estratosféricos (mais de 18 milhões de Leaf) para reparar a aeronave de Lyner, levando o grupo a cogitar a perigosa escalada a pé da Torre apesar dos alertas de Jack sobre a hostilidade da Tribo Teru; a emboscada covarde do comandante Bourd armada contra Lyner, frustrada pelo plano genial de Misha que acumulou energia mágica em segredo para aniquilar Bourd para todo o sempre; a emocionante reconciliação de infância entre Lyner e Misha, permeada pela cômica disputa de dívidas culinárias entre Misha e Krusche (dezenas de Combos Dokkoi, Megamilks e Balas de Gato); o despertar angustiado de Lyner após sonhar com o sacrifício supremo da Senhora Shurelia e a decisão resoluta de buscar Leard para resgatá-la; e a profunda lição de intimidade feminina de Aurica a Lyner sobre a necessidade de confiar em Misha, que culmina no resgate do [Power Cylinder] e no retorno triunfal rumo ao Beco Vagalume.",
    "decisoes_terminologicas": {
        "Power Cylinder": "[Power Cylinder] (パワーシリンダー, componente-chave de desligamento de emergência)",
        "Combo Dokkoi": "Combo Dokkoi (ドッコイ定食, refeição volumosa tradicional)",
        "Bala de Gato": "Bala de Gato (猫飴, guloseima felina de Sol Ciel)",
        "Gelo Ralado": "Gelo Ralado (かちわり氷, sobremesa triturada de gelo)",
        "Megamilk": "Megamilk (メガミルク, bebida láctea energizante)",
        "Beco Vagalume": "Beco Vagalume (ほたる横丁, distrito comercial de compras)"
    },
    "alertas_para_proximo_bloco": "Atenção ao retorno do grupo ao Beco Vagalume com o Power Cylinder em mãos, aos desdobramentos da consulta com Leard em Platina sobre a possibilidade de salvar a Senhora Shurelia e à continuidade das operações da Cerimônia de Despertar da Deusa Eoria."
}

output_data = {
    "block_id": "BLK_EVD_028",
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

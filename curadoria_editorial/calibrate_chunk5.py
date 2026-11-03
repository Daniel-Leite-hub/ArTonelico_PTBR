# -*- coding: utf-8 -*-
"""Calibração e redação editorial de Chunk 5 (IDs 31461 a 31508)."""
import json, sqlite3, sys
sys.path.insert(0, 'Ferramentas_Traducao')
sys.path.insert(0, 'Ferramentas_Traducao/tools')
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

dialogues = {d['id']: d for d in data['dialogues']}

CHUNK_5 = {
    31461: ("Como dizer... Parece que alguémCRestá se precipitando por aqui...", "Observação desconfiada sobre a pressa do parceiro (112B/144B)."),
    31462: ("O que tá dizendo?CRDá uma boa olhada.", "Lyner pedindo para olhar o objeto de perto eliminando o estouro de +4B (74B/96B)."),
    31463: ("...Ah, não é um Toko-Toko?", "Surpresa ao reconhecer o formato do brinquedo eliminando o estouro de +5B (56B/64B)."),
    31464: ("Toko-Toko? Fala do tamborim?", "Lyner decifrando o apelido infantil eliminando o estouro de +24B (64B/88B)."),
    31465: ("Ele faz esse barulho, aí chamoCRassim desde criança... É estranho?", "Justificativa meiga da infância eliminando o estouro de +6B (134B/192B)."),
    31466: ("Pronto, Gancho Giro concluído!", "Comemoração de Lyner ao terminar o Gancho Giro (60B/80B)."),
    31467: ("Precisa de coragem pra usar isso.CRNão dá medo de morder a língua?", "Receio de Aurica ao cantar depressa eliminando o estouro de +24B (124B/176B)."),
    31468: ("Eu não posso usar, nem sei...CRQuem canta sente esse medo todo?", "Dúvida de Lyner sobre a sensação do canto eliminando o estouro de +4B (123B/128B)."),
    31469: ("Mesmo sabendo que tá tudo bem, dá.CRChamam até de Gancho Corta-Língua.", "Explicação do apelido assustador eliminando o estouro de +69B (126B/168B)."),
    31470: ("Mas pra mim, cantar tão rápidoCRe tagarelar nem tem graça...", "Desabafo da Reyvateil sobre a pressa métrica eliminando o estouro de +7B (120B/128B)."),
    31471: ("Detesto o nome Gancho Giro,CRposso chamar de “Hymn Accella”?", "Pedido para rebatizar o gancho acelerador eliminando o estouro de +17B (122B/200B)."),
    31472: ("Você fazer Tranquilidade ajuda tanto!CRFico bem mais segura.", "Alívio com o calmante produzido por Lyner (96B/152B)."),
    31473: ("É o mínimo! Como a Misha cantaCRe me dá paz na luta, é minha obrigação.", "Lyner reconhecendo a parceria de canto com carinho (156B/256B)."),
    31474: ("É? Mas prefiro a que você fazCRdo que as compradas em loja.", "Preferência carinhosa pelo item artesanal de Lyner (118B/160B)."),
    31475: ("Cheinha do seu amor, Lyner!", "Provocação doce e afetuosa eliminando o estouro de +3B (55B/56B)."),
    31476: ("O que será que senteCRquem sofre esse efeito?", "Curiosidade sobre o efeito da poção esquiva eliminando o estouro de +8B (86B/96B)."),
    31477: ("Tentar acertar e só errar golpes...CRSerá que a pessoa fica em pânico?", "Reflexão sobre a frustração de errar tudo eliminando o estouro de +37B (128B/176B)."),
    31478: ("Pensando bem, é verdade. Você tentaCRatacar e o golpe vai pro nada.", "Lyner imaginando a frustração do oponente eliminando o estouro de +1B (138B/208B)."),
    31479: ("Protege da lâmina inimiga, né?CRQue tal “Desvia-Espada Maligna”?", "Batismo protetor da poção de esquiva eliminando o estouro de +25B (122B/176B)."),
    31480: ("Sofrer um Guardlezz dessesCRdeve ser um pesadelo, né?", "Empatia irônica com quem sofre a quebra de defesa eliminando o estouro de +10B (102B/112B)."),
    31481: ("Mesmo podendo bater, até o socoCRde uma criança vira um pavor!", "Comentário sobre a fragilidade total eliminando o estouro de +32B (118B/144B)."),
    31482: ("Pois é! Capaz de alguém apanharCRpra uma criancinha de verdade.", "Lyner achando graça do perigo eliminando o estouro de +22B (108B/136B)."),
    31483: ("Numa briga de casal, é só jogar istoCRe dar um tapa. Nocaute na certa!", "Piada hilária sobre discussões amorosas (135B/200B)."),
    31484: ("...Aí já passa de qualquer limite!", "Reação chocada de Lyner com a violência conjugal (69B/88B)."),
    31485: ("Pensando bem, dá medo...CRQue tal “Oculta-Guardião”?CRFaz o anjo da guarda sumir!", "Batismo sinistro da poção desarmante eliminando o estouro de +16B (160B/176B)."),
    31486: ("Mesmo que o monstro fique lento,CRnão quer dizer que erra os golpes, né?", "Dúvida tática sobre a mecânica de lentidão eliminando o estouro de +40B (126B/176B)."),
    31487: ("Não conseguir se esquivar de golpeCRde inimigo lerdo é meio bizarro, não?", "Estranhamento de não desviar de monstros lerdos eliminando o estouro de +15B (126B/168B)."),
    31488: ("Pois é, mas por incrívelCRque pareça, ainda acerta...", "Lyner admitindo o mistério do acerto eliminando o estouro de +20B (98B/104B)."),
    31489: ("Fica absurdamente lerdo,CRmas ainda acerta. Que coisa...", "Inconformismo cômico com o acerto do lerdo eliminando o estouro de +11B (99B/136B)."),
    31490: ("Fica lento, mas a mira continua a mesma.CRNão faz nada além do que tá escrito, né?", "Constatação prática dos limites do efeito eliminando o estouro de +38B (144B/248B)."),
    31491: ("Pelo efeito que dá, que tal o nomeCR“Água Vira-Tartaruga”?", "Batismo direto e cômico da lentidão (102B/176B)."),
    31492: ("Neo Hitlezz concluído!CRVai custar até pra matar formiga!", "Comemoração triunfal de Lyner eliminando o estouro de +45B (114B/176B)."),
    31493: ("É um nome bem direto, né?", "Comentário sobre a clareza do nome (51B/80B)."),
    31494: ("Mas ainda prefiroCR“Desvia-Lorde das Trevas”.", "Sugestão grandiloquente e pomposa eliminando o estouro de +20B (84B/96B)."),
    31495: ("Guardlezz High! Até picada de pernilongoCRvira motivo de pânico absoluto.", "Aviso de perigo sobre a versão aprimorada eliminando o estouro de +2B (136B/176B)."),
    31496: ("Com o efeito ativo,CRsó de estar vivo já dá medo.", "Observação da vulnerabilidade máxima eliminando o estouro de +4B (96B/104B)."),
    31497: ("Até um casal de mãos dadasCRjá vira um ataque!", "Lyner imaginando o toque virando agressão eliminando o estouro de +19B (86B/104B)."),
    31498: ("Dá pra viver um amor de alto risco!CREu tô fora dessa loucura...", "Recusa cômica ao amor suicida eliminando o estouro de +32B (118B/192B)."),
    31499: ("Vai ser a “Oculta-Deuses”.CRQue pavor...", "Batismo místico da poção suprema eliminando o estouro de +8B (81B/88B)."),
    31500: ("Mas isso não impedeCRos golpes de acertarem, né?", "Pergunta sobre a precisão dos golpes eliminando o estouro de +1B (87B/96B)."),
    31501: ("Claro. Só deixa o alvo lerdo,CRa mira dele continua igual.", "Explicação técnica de Lyner eliminando o estouro de +16B (120B/136B)."),
    31502: ("Sendo mais forte, que tal o nomeCR“Água de Esculpir Pedra”?", "Batismo metafórico da erosão lenta (101B/120B)."),
    31503: ("O que significa?", "Pergunta curiosa de Lyner (34B/48B)."),
    31504: ("Lento feito gota d’águaCRcorroendo a rocha.", "Explicação poética e lenta da metáfora eliminando o estouro de +24B (81B/96B)."),
    31505: ("Água dos Sonhos pronta! Quase dormiCRduas vezes no meio da fabricação.", "Relato sonolento de Lyner sobre o sonífero (128B/256B)."),
    31506: ("Sinal de que o efeito é potente!CRDá pra usar no dia a dia, tá ótimo.", "Aprovação prática da utilidade cotidiana do calmante (126B/200B)."),
    31507: ("Pois é. Excelente pra insônia.", "Concordância medicinal de Lyner (62B/96B)."),
    31508: ("Dar isso pro paqueraCRtambém é uma boa ideia, né?", "Provocação pícara e romântica eliminando o estouro de +15B (85B/104B).")
}

overflows = 0
validation_errors = 0

for d_id, (txt, note) in sorted(CHUNK_5.items()):
    c.execute('SELECT original_bytes FROM dialogues WHERE id = ?', (d_id,))
    ob = c.fetchone()[0]
    sz = encoded_size(txt)
    diff = sz - ob
    orig_en = dialogues[d_id]['original_en']
    errs = validate_line(d_id, orig_en, txt)
    if diff > 0:
        print(f"ERRO DE ESTOURO ID {d_id}: Cap {ob}B | Sz {sz}B (+{diff}B) | {txt}")
        overflows += 1
    if errs:
        print(f"ERRO DE VALIDAÇÃO ID {d_id}: {errs} | {txt}")
        validation_errors += 1

print(f"\n--- Resultado Chunk 5 ---")
print(f"Total de falas: {len(CHUNK_5)}")
print(f"Estouros de buffer: {overflows}")
print(f"Erros de validação: {validation_errors}")
if overflows == 0 and validation_errors == 0:
    print("[PERFEITO] Chunk 5 aprovado 100%!")

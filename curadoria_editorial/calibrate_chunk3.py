# -*- coding: utf-8 -*-
"""Calibração e redação editorial de Chunk 3 (IDs 31365 a 31412)."""
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

CHUNK_3 = {
    31365: ("Pronto! Divisor FFT feito!", "Exclamação de triunfo de Lyner ao terminar o Divisor FFT (68B/72B)."),
    31366: ("Hmm... Não entendo muito bem,CRmas é tão incrível assim?", "Curiosidade ingênua de Aurica sobre o componente (120B/128B)."),
    31367: ("Nem eu sei direito, mas dizem que,CRao combiná-lo com outra coisa, viraráCRmaterial para um superitem.", "Lyner explicando o potencial do componente eliminando o estouro de +1B (187B/216B)."),
    31368: ("Um superitem?", "Pergunta de Aurica (27B/32B)."),
    31369: ("Não sei bem. Dizem que ajuda na luta,CRmas também põe a gente em perigo.", "Aviso de Lyner sobre os riscos do item (153B/168B)."),
    31370: ("Não crie algo perigoso assim!CRPor garantia, que tal chamarCRde “O Início do Perigo”?", "Apelo temeroso e batismo preventivo de Aurica eliminando o estouro de +22B (168B/200B)."),
    31371: ("Hum... Como vai virar algo perigoso,CRacho que o nome serve.", "Concordância relutante de Lyner (142B/168B)."),
    31372: ("Quantizador pronto!", "Comemoração concisa de Lyner (39B/40B)."),
    31373: ("Tem toda cara de máquina, né?", "Observação visual de Aurica (60B/80B)."),
    31374: ("Com certeza. Combinando isso, pareceCRque criamos material pra algo incrível.", "Lyner detalhando o processo em cadeia (178B/208B)."),
    31375: ("Material do material...CRParece que a estrada é longa.", "Reflexão cansada de Aurica sobre os passos de síntese (115B/136B)."),
    31376: ("Mas ter essa meta fez ser bemCRdivertido enquanto eu criava.", "Entusiasmo de Lyner pelo processo eliminando o estouro de +19B (124B/144B)."),
    31377: ("É assim que o Grathmeld vicia.CRSó te peço: não vire um recluso...", "Preocupação meiga de Aurica para Lyner não se isolar eliminando o estouro de +1B (154B/176B)."),
    31378: ("Que preocupação é essa?!", "Indignação cômica de Lyner eliminando o estouro de +8B (51B/56B)."),
    31379: ("Plug Sinfônico pronto!", "Lyner apresentando o Plug Sinfônico eliminando o estouro de +5B (49B/72B)."),
    31380: ("Plug Sinfônico?CRNunca ouvi falar.", "Estranhamento de Aurica com o termo técnico eliminando o estouro de +10B (69B/72B)."),
    31381: ("O nome oficial de onde chamamosCRde “Altar dos Apóstolos”CRé, na verdade, “Plug Sinfônico”.", "Lyner explicando a nomenclatura técnica da lore eliminando o estouro de +5B (178B/200B)."),
    31382: ("Como este é uma versão míni,CRtambém se chama Plug Sinfônico.", "Lyner justificando a versão miniatura eliminando o estouro de +7B (129B/144B)."),
    31383: ("Hum... Dá uma sensação estranha...", "Desconforto sutil de Aurica eliminando o estouro de +14B (63B/64B)."),
    31384: ("Disco Grathnode DH concluído!!", "Celebração de Lyner (88B/88B)."),
    31385: ("DH? Nome meio complicado.", "Comentário de Aurica sobre a sigla (63B/64B)."),
    31386: ("Pois é. Nem eu sei o que significa...", "Admissão sincera de Lyner (94B/112B)."),
    31387: ("Não tem um nome mais fácil?", "Pedido de Lyner eliminando o estouro de +18B (62B/88B)."),
    31388: ("Se tivesse algum detalhe marcante...CRMas é só um disco. Bem pesado, aliás.", "Aurica procurando características no objeto (175B/216B)."),
    31389: ("Peso de Picles.", "Sugestão tosca de Lyner eliminando o estouro de +11B (29B/32B)."),
    31390: ("Recusado.CR...Horrível demais.", "Repulsa imediata de Aurica eliminando o estouro de +13B (51B/64B)."),
    31391: ("Pronto. Um Healy...", "Lyner começando a nomear o remédio (46B/72B)."),
    31392: ("Proibido esse nome!CRÉ o nome oficial, né?", "Aurica vetando o nome padrão eliminando o estouro de +1B (89B/112B)."),
    31393: ("B-bem, é sim...CRPor que a proibição?", "Lyner sem entender o veto eliminando o estouro de +2B (71B/88B)."),
    31394: ("Healy C é sem graça demais!CREu vou dar um nome lindo pra ele.", "Aurica desdenhando da frieza técnica eliminando o estouro de +26B (112B/128B)."),
    31395: ("Já sei! “Angel Heal”!", "Batismo angelical de Aurica eliminando o estouro de +16B (46B/48B)."),
    31396: ("Lyner, nem pense em dizerCRque este remédio é “Fullhealin D”.", "Aviso antecipado de Aurica eliminando o estouro de +14B (119B/128B)."),
    31397: ("M-mas é o nome oficial...", "Lyner tentando argumentar (61B/104B)."),
    31398: ("Nome tão sem graça!CREu escolho um bem melhor.", "Aurica insistindo no toque feminino eliminando o estouro de +14B (102B/112B)."),
    31399: ("Vejamos... Que talCR“Venus Heal”?", "Sugestão de Aurica eliminando o estouro de +9B (67B/104B)."),
    31400: ("B-bem, não ficou ruim...", "Aprovação tímida de Lyner (58B/72B)."),
    31401: ("Como esse Heal Cracker curaCRé um mistério sem fim...", "Lyner intrigado com a mecânica da bombinha eliminando o estouro de +13B (102B/112B)."),
    31402: ("Melhor não esquentar a cabeça.CRGrathmeld não é algo fácil de explicar.", "Conselho pragmático de Aurica eliminando o estouro de +3B (141B/152B)."),
    31403: ("E você não entenderia mesmo...", "Alfinetada carinhosa de Aurica (68B/104B)."),
    31404: ("Ei, tão me ofendendo aí?", "Indignação desconfiada de Lyner eliminando o estouro de +16B (52B/56B)."),
    31405: ("Não é isso! Mas curar comCRbombinhas é difícil de engolir, né?", "Aurica ponderando a estranheza do efeito curativo (135B/168B)."),
    31406: ("Mas como o poder de cura é alto...CRque tal “Canhão de Arcádia”?", "Batismo imponente de Aurica (134B/208B)."),
    31407: ("Sei que não dói, mas dá um medoCRusar um troço desses...", "Receio genuíno de Lyner com a explosão (108B/120B)."),
    31408: ("Pois é.CRExplode pra depois curar.", "Aurica concordando com o paradoxo eliminando o estouro de +6B (68B/96B)."),
    31409: ("Dá receio ter feito isso.CRSe eu tiver errado,CRvai todo mundo pelos ares!", "Medo de erro de fabricação de Lyner eliminando o estouro de +7B (141B/168B)."),
    31410: ("Não fala uma coisa tenebrosa dessas!CREm vez de descansar curada,CRvou é descansar em paz!", "Pavor cômico de Aurica de morrer na explosão (144B/264B)."),
    31411: ("Segui a receita certinho,CRentão vai ficar tudo bem.", "Lyner tentando se tranquilizar eliminando o estouro de +14B (99B/104B)."),
    31412: ("Se você diz, vou confiar.CRQue tal o nome “Elixir Bomb”?", "Aurica concedendo confiança e batizando o item eliminando o estouro de +5B (155B/184B).")
}

overflows = 0
validation_errors = 0

for d_id, (txt, note) in sorted(CHUNK_3.items()):
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

print(f"\n--- Resultado Chunk 3 ---")
print(f"Total de falas: {len(CHUNK_3)}")
print(f"Estouros de buffer: {overflows}")
print(f"Erros de validação: {validation_errors}")
if overflows == 0 and validation_errors == 0:
    print("[PERFEITO] Chunk 3 aprovado 100%!")

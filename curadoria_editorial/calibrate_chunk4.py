# -*- coding: utf-8 -*-
"""Calibração e redação editorial de Chunk 4 (IDs 31413 a 31460)."""
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

CHUNK_4 = {
    31413: ("Tranquilizante pronto!", "Apresentação do remédio calmante por Lyner (50B/64B)."),
    31414: ("O efeito é ótimo, eu sei,CRmas é tão amargo que não desce...", "Desabafo sincero de Aurica sobre o amargor do remédio (128B/168B)."),
    31415: ("Imaginei que alguém ia chiar,CRpor isso este aqui não é amargo!", "Lyner prevendo a reclamação com remédio aprimorado (129B/152B)."),
    31416: ("Sabor Tripas de Nyo?,CRpra beber com gosto!", "Lyner revelando o sabor bizarro eliminando o estouro de +21B (92B/96B)."),
    31417: ("Tripas de Nyo?!... Enfim.CREu chamo de “Legend Raiser”.", "Reação atônita e batismo de Aurica eliminando o estouro de +6B (117B/120B)."),
    31418: ("Não queria ter que usar isso,CRmas é bom ter guardado.", "Prudência tática de Lyner eliminando o estouro de +4B (102B/128B)."),
    31419: ("Verdade. Numa batalha,CRtudo pode acontecer.", "Concordância realista de Aurica (68B/112B)."),
    31420: ("Mas tomar isso é impressionante:CRo aliado caído estremeceCRe já pula de pé na hora!", "Aurica descrevendo o choque do reanimador (149B/216B)."),
    31421: ("Pois é. Parece até que o remédioCRdói mais do que a surra...", "Comentário irônico de Lyner sobre a descarga elétrica (107B/136B)."),
    31422: ("Decidido: “Electricules”.", "Batismo direto de Aurica eliminando o estouro de +5B (52B/56B)."),
    31423: ("O Míssil... Continuo sem saberCRcomo descrever essa forma bizarra.", "Estranhamento de Lyner com o artefato balístico (129B/144B)."),
    31424: ("Esse formato é meio tosco...CRDá vontade de pôr um nome fofo.", "Aurica querendo suavizar a bomba eliminando o estouro de +15B (114B/152B)."),
    31425: ("Que tal “Françoise-Anne”?CRNão é uma graça?", "Sugestão mimosa de Aurica eliminando o estouro de +9B (88B/104B)."),
    31426: ("Reconheço a fofura,CRmas nem parece nome de bomba...", "Lyner achando o batismo meigo demais (110B/152B)."),
    31427: ("Não é ventilador!CRToma cuidado!", "Alerta direto de Lyner eliminando o estouro de +5B (64B/72B)."),
    31428: ("Eu sei bem! Se apontar isso pra mim,CRnem com sete vidas eu escapava.", "Aurica ciente do perigo devastador da rajada (142B/192B)."),
    31429: ("...Mas não dá vontadeCRde ver se o ventinho é bom?", "Tentação imprudente de Aurica eliminando o estouro de +1B (99B/128B)."),
    31430: ("Em vez de frescor, uma ventaniaCRviolenta vai te arremessar longe!", "Lyner alertando sobre o impacto doloroso eliminando o estouro de +18B (134B/248B)."),
    31431: ("Mas se eu fincar o pé firme,CRvai que dá pra aguentar?CRNo verãozão ia ajudar tanto...", "Teimosia ingênua de Aurica eliminando o estouro de +6B (151B/224B)."),
    31432: ("Quem iria tão longe só pra se refrescar?", "Incredulidade prática de Lyner (75B/168B)."),
    31433: ("É verdade. Mas que o nome sejaCRrefrescante: que tal “Exobrisa”?", "Batismo refrescante de Aurica (115B/192B)."),
    31434: ("...Soa refrescante em vários sentidos.", "Ironia sutil de Lyner (60B/80B)."),
    31435: ("Esse Boltapolta é tão estranho.CRUm bastão desses soltar raios...", "Aurica intrigada com o bastão elétrico (122B/136B)."),
    31436: ("É porque usei Cogumelo-Trovão nele,CRe um tiquinho do efeito paralisanteCRdo Power Sourcer.", "Lyner explicando a mistura condutora (163B/240B)."),
    31437: ("Ah, esse era o truque?", "Aurica desvendando o mecanismo eliminando o estouro de +2B (50B/56B)."),
    31438: ("O truque é simples,CRmas fabricar deu trabalho.", "Lyner detalhando o trabalho de síntese (89B/104B)."),
    31439: ("Toquei no Cogumelo-Trovão duas vezesCRe levei choque...", "Relato cômico dos choques de Lyner (103B/120B)."),
    31440: ("Líquido Ionizante pronto!", "Apresentação do líquido inflamável eliminando o estouro de +5B (62B/88B)."),
    31441: ("Bom trabalho! Mas parece queCRvocê usou um monte de coisa aí.", "Aurica elogiando o esforço de síntese (115B/136B)."),
    31442: ("Pois é. Mas depois de tudo isso,CRo resultado final parece só uma garrafaCRd’água quadrada...", "Lyner desapontado com a aparência simples (179B/216B)."),
    31443: ("Ah... É só água aí dentro?CRCom essa quantia toda, a genteCRnunca vai passar sede.", "Aurica achando que é cantil comum (164B/248B)."),
    31444: ("...Se beber isso, congela por dentro.CRNa verdade, é uma bomba de gelo!", "Aviso apavorado de Lyner eliminando o estouro de +16B (134B/168B)."),
    31445: ("É mesmo? Mas se beber de levinho,CRvai que o estômago fica geladinhoCRe refrescante no verão!", "Ideia estapafúrdia de Aurica eliminando o estouro de +8B (167B/216B)."),
    31446: ("Ótima ideia! Faça o teste!CRSe ficar soprando ar gelado,CRrefresca todo mundo ao redor!", "Lyner devolvendo a provocação eliminando o estouro de +25B (168B/232B)."),
    31447: ("Boa ideia! No verãoCReu conto com você, Lyner!", "Aurica jogando a bronca nas costas dele eliminando o estouro de +4B (95B/112B)."),
    31448: ("Eu?!", "Reação indignada de Lyner eliminando o estouro de +1B (11B/16B)."),
    31449: ("Olha, a Pipocabomba!CREla fere quase todo tipo de monstro, né?", "Aurica reconhecendo a bomba eliminando o estouro de +2B (134B/160B)."),
    31450: ("Sim. Inimigo com ou sem atributo,CRleva um dano estrondoso!", "Lyner garantindo o estrago eliminando o estouro de +3B (118B/160B)."),
    31451: ("Mais do que dano alto, acho difícilCRalguém sair ileso disso aí...", "Aurica comentando o poder devastador (116B/136B)."),
    31452: ("Ataque físico devastador e danoCRmágico junto! Uma bomba incrível dessasCRmerece um nome incrível!", "Entusiasmo de Aurica eliminando o estouro de +3B (184B/264B)."),
    31453: ("B-bem... concordo, mas...CRnão pode ser “Pipocabomba” mesmo?", "Lyner defendendo o nome original eliminando o estouro de +28B (111B/128B)."),
    31454: ("De jeito nenhum! Nome tão bobo.CRNão faz jus ao poder! Que talCR“Meltiaskill”?", "Aurica vetando o nome e sugerindo Meltiaskill eliminando o estouro de +17B (146B/200B)."),
    31455: ("...Não entendi o significado,CRmas deu pra ver que soa poderoso.", "Lyner aceitando a imponência sonora (125B/160B)."),
    31456: ("Olha, porquinho de incenso!CRQue encanto!", "Aurica encantada com o artesanato eliminando o estouro de +71B (75B/80B)."),
    31457: ("Já que era um incenso,CRquis dar esse toque tradicional.", "Lyner orgulhoso do visual retrô (109B/136B)."),
    31458: ("Embora pareça que gastei esforçoCRnum detalhe meio inútil...", "Autocrítica bem-humorada de Lyner eliminando o estouro de +6B (109B/128B)."),
    31459: ("Nada disso! É mil vezes melhorCRdo que um incenso comum!", "Aurica valorizando o capricho estético eliminando o estouro de +18B (108B/128B)."),
    31460: ("Ouvir issoCRfaz valer o sufoco!", "Lyner agradecido pelo reconhecimento eliminando o estouro de +16B (71B/88B).")
}

overflows = 0
validation_errors = 0

for d_id, (txt, note) in sorted(CHUNK_4.items()):
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

print(f"\n--- Resultado Chunk 4 ---")
print(f"Total de falas: {len(CHUNK_4)}")
print(f"Estouros de buffer: {overflows}")
print(f"Erros de validação: {validation_errors}")
if overflows == 0 and validation_errors == 0:
    print("[PERFEITO] Chunk 4 aprovado 100%!")

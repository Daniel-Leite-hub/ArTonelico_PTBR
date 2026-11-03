# -*- coding: utf-8 -*-
"""Calibração e redação editorial de Chunk 2 (IDs 31317 a 31364)."""
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

CHUNK_2 = {
    31317: ("Ufa, terminei a duras penas...CRMas que canseira mental...", "Desabafo exausto de Lyner eliminando o estouro de +5B (62B/128B)."),
    31318: ("Bom trabalho.CRFoi tão difícil?", "Empatia de Aurica eliminando o estouro de +21B (65B/72B)."),
    31319: ("É que fiz a fonte de alta energiaCRpra aeronave cruzar a Blastline.CRSe explodisse, já era!", "Explicação técnica de Lyner eliminando o estouro de +4B (97B/208B)."),
    31320: ("A gente ia pelos ares?", "Pergunta tímida de Aurica eliminando o estouro de +1B (24B/48B)."),
    31321: ("Tudo aqui em volta viraria cinzas,CRe não tô brincando...", "Aviso sério de Lyner eliminando o estouro de +3B (57B/152B)."),
    31322: ("Isso não é perigoso demais?!", "Reação assustada de Aurica (30B/64B)."),
    31323: ("Por isso o sufoco.CRSe explode no meio,CRjá era pra gente!", "Lyner justificando a tensão eliminando o estouro de +43B (118B/144B)."),
    31324: ("É verdade... Mas num estaloCRnem dá tempo de assustar,CRtalvez seja até melhor...", "Raciocínio bizarro e conformista de Aurica eliminando o estouro de +16B (166B/192B)."),
    31325: ("(Melhor como assim, Aurica?!)", "Pensamento em pânico de Lyner eliminando o estouro de +11B (59B/72B)."),
    31326: ("Uff... Fazer isso é tão difícil.", "Exclamação cansada de Lyner eliminando o estouro de +12B (68B/72B)."),
    31327: ("Mas ficou uma ocarina tão fofa!", "Elogio carinhoso de Aurica ao instrumento (33B/64B)."),
    31328: ("O problema foram os ingredientes:CRusei Eufortíssimo, Lata de CantoCRde Sereia e outras coisas.", "Lyner listando os ingredientes complexos eliminando o estouro de +23B (99B/232B)."),
    31329: ("Hã?! L-Lata de Canto?!", "Pavor cômico de Aurica eliminando o estouro de +14B (46B/64B)."),
    31330: ("Aurica?", "Lyner surpreso no limite estrito do buffer (15B/16B)."),
    31331: ("Não põe Lata de Canto de Sereia!CREra tão fofa, agora virouCRum “Apito do Diabo”!", "Protesto exasperado de Aurica contra a Lata de Canto de Sereia (88B/208B)."),
    31332: ("Por favor, não fala isso na frenteCRda Misha, senão vira guerra mágica!", "Apelo desesperado de Lyner eliminando o estouro de +22B (74B/168B)."),
    31333: ("Incubadora Tripolar pronta!CRDeu um trabalhão!", "Apresentação da Incubadora Tripolar eliminando o estouro de +7B (94B/96B)."),
    31334: ("É pra pôr algo aí dentroCRe cultivar, né?", "Curiosidade de Aurica eliminando o estouro de +1B (87B/104B)."),
    31335: ("É sim. E agora, o que eu cultivo?", "Lyner animado com a nova máquina (34B/72B)."),
    31336: ("Que tal um homúnculo?", "Sugestão perturbadora e inocente de Aurica (23B/56B)."),
    31337: ("B-bem, até daria...CRmas prefiro não fazer.", "Recusa desconcertada de Lyner eliminando o estouro de +2B (89B/112B)."),
    31338: ("Mas você consegue criar!CRFez algo incrível!", "Aurica admirada com a capacidade de síntese de Lyner (91B/112B)."),
    31339: ("Não é o tipo bom de incrível...", "Comentário desconfiado de Lyner (33B/88B)."),
    31340: ("Fornalha de Alto Refino pronta!CRDerrete qualquer coisa!CRSem exagero!", "Lyner triunfante sobre a fornalha eliminando o estouro de +11B (141B/160B)."),
    31341: ("É tudo isso mesmo?CRPra mim parece só um fogão a gásCRchique demais...", "Ceticismo cômico de Aurica comparando a um fogão chique eliminando o estouro de +10B (84B/152B)."),
    31342: ("Misturei Coração de Dragão no fogoCRda Caixa de Fogo de Kant. Se bobear,CRderrete até a base de apoio!", "Lyner alertando sobre a potência absurda eliminando o estouro de +41B (111B/232B)."),
    31343: ("...Acho isso perigoso demais pra usar.", "Receio prudente de Aurica eliminando o estouro de +3B (39B/96B)."),
    31344: ("E eu não ia querer carregarCRalgo desse tamanho...", "Aurica recusando carregar o trambolho eliminando o estouro de +3B (102B/112B)."),
    31345: ("Sinapse Sinfônica pronta!CRTrabalho fino cansa demais.", "Lyner apresentando a Sinapse Sinfônica eliminando o estouro de +8B (110B/160B)."),
    31346: ("Sendo fina assim, natural ficar exausto.", "Consolo compreensivo de Aurica eliminando o estouro de +21B (41B/96B)."),
    31347: ("Mas isso é mesmo uma máquina?CRNem parece, né?", "Dúvida de Aurica sobre a aparência orgânica da peça (48B/120B)."),
    31348: ("Lembra um nervo biológico, né?CRMas por dentro é máquina pura.", "Lyner explicando a anatomia mecânica da sinapse (65B/184B)."),
    31349: ("Tão fininha e tão incrível...CRMas dessa cor parece macarrão,CRdá até vontade de comer...", "Fascínio gastronômico bizarro de Aurica com o cordão (95B/208B)."),
    31350: ("Se comer, é veneno puro!", "Aviso enfático de Lyner eliminando o estouro de +18B (26B/64B)."),
    31351: ("Célula D3... Tem umas coisas meioCRestranhas nela, sabe?", "Desconfiança de Lyner com a Célula D3 (57B/120B)."),
    31352: ("Ué, deu algum problema?", "Pergunta de Aurica (23B/48B)."),
    31353: ("É que usei Tripas de Nyo?CRna Célula D2 pra fazer...", "Lyner revelando os ingredientes nojentos eliminando o estouro de +10B (58B/128B)."),
    31354: ("...Tripas de Nyo??CRIsso não parece nada bom...", "Suspeita nojenta de Aurica com as tripas (96B/96B)."),
    31355: ("Eu só segui a receita.CRMas admito que essa cor tá esquisita...", "Lyner se defendendo da receita (74B/168B)."),
    31356: ("Parece venenosa mesmo.CRNão parece coisa boa não...", "Aurica julgando pela cor peçonhenta (57B/168B)."),
    31357: ("Mas como tem Tripas de Nyo?,CRvai que dá pra comer...", "Aurica cogitando provar a gororoba eliminando o estouro de +5B (62B/128B)."),
    31358: ("Se comer isso, vai dar muito ruim...", "Lyner prevendo a tragédia estomacal eliminando o estouro de +14B (38B/96B)."),
    31359: ("Átomo de Mercúrio concluído!CREle até leva Registro Akáshico!", "Celebração de Lyner pela síntese do elemento supremo (65B/152B)."),
    31360: ("Usou um item tão raro?!", "Espanto de Aurica com o gasto do item eliminando o estouro de +8B (48B/56B)."),
    31361: ("Sim! Um item super-raro feitoCRde outro super-raro!", "Orgulho alquímico de Lyner com o Átomo de Mercúrio (103B/120B)."),
    31362: ("Falando assim parece o máximo...CRMas pra que serve afinal?", "Ceticismo pragmático de Aurica sobre a utilidade real (61B/192B)."),
    31363: ("Pra combinar no Grathmeld!CRVai deixar qualquer coisa superforte!", "Lyner garantindo o poder do item no Grathmeld (73B/160B)."),
    31364: ("Então numa arma vai ser incrível!CRUm material de hiperaprimoramento!", "Empolgação de Aurica com o aprimoramento de armas eliminando o estouro de +7B (75B/144B).")
}

overflows = 0
validation_errors = 0

for d_id, (txt, note) in sorted(CHUNK_2.items()):
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

print(f"\n--- Resultado Chunk 2 ---")
print(f"Total de falas: {len(CHUNK_2)}")
print(f"Estouros de buffer: {overflows}")
print(f"Erros de validação: {validation_errors}")
if overflows == 0 and validation_errors == 0:
    print("[PERFEITO] Chunk 2 aprovado 100%!")

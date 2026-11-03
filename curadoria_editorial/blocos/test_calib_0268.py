import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0268 = {
    26594: ("...É, ser esquecida assimCRé um choque, né?", "Misha confessando a tristeza pelo esquecimento de Lyner."),
    26595: ("Urgh...", "Lyner gemendo sem graça com a cobrança justa."),
    26596: ("É quase impressionante como esqueceuCRtudo sem deixar nem rastro.", "Misha ironizando o esquecimento total de Lyner."),
    26597: ("Ah, bem... ob...", "Lyner gaguejando ao quase agradecer achando que era elogio."),
    26598: ("Não ache que é elogio,CRsenão uso magia vermelha!", "Misha repreendendo a audácia de Lyner com ameaça mágica."),
    26599: ("...ri...gado...", "Lyner gaguejando tentando completar o agradecimento que foi interrompido."),
    26600: ("Não achei que era elogio!CREu me sinto muito mal por isso!!", "Lyner se defendendo com culpa genuína."),
    26601: ("Uff... Vou contar por que deixeiCRum cara tão insensível mergulhar em mim.", "Misha suspendendo a mágoa e introduzindo seu segredo sem rubrica teatral."),
    26602: ("E não foi só por serCRum velho amigo de infância.", "Misha destacando que o vínculo vai além da amizade antiga."),
    26603: ("E por quê?", "Lyner curioso com a verdadeira razão do consentimento."),
    26604: ("Hehe~ O meu sonho é casar!", "Misha revelando seu sonho de infância de ser noiva de Lyner."),
    26605: ("Q-quê?!", "Lyner perplexo com a declaração romântica inesperada."),
    26606: ("É exatamente isso.CRE não falo mais nada!", "Misha encerrando o assunto com mistério e dengo."),
    26607: ("O Mundo Inferior tem tanta coisaCRcuriosa pra se ver.", "Lyner mudando de assunto e comentando sobre o Mundo Inferior."),
    26608: ("Acha? Como você viveu no Mundo Superior,CRé normal achar isso.", "Misha contextualizando a perspectiva de Lyner nascido em Platina."),
    26609: ("Quando vim aqui pra baixo,CRme senti igual a você.", "Misha compartilhando sua experiência inicial no Mundo Inferior."),
    26610: ("O Mundo Inferior parece mais vivoCRe divertido.", "Lyner elogiando a vivacidade e animação das cidades inferiores."),
    26611: ("É, o Beco VagalumeCRé animado de verdade.", "Misha concordando com o charme comercial de seu bairro."),
    26612: ("Quando der tempo,CRte levo pra passear.", "Misha prometendo guiar Lyner pelos recantos do beco."),
    26613: ("Ai, ai... Fazia tanto tempoCRque eu não vinha a Platina...", "Misha nostálgica ao revisitar sua cidade natal."),
    26614: ("Ficar em estalagem aqui em PlatinaCRé meio decepcionante.", "Misha lamentando a impessoalidade da pousada."),
    26615: ("Eu queria ficar na sua casa...", "Misha confessando o desejo de se hospedar na casa de Lyner."),
    26616: ("Q-quê?! Não cabe tanta genteCRlá em casa nem a pau!", "Lyner desesperado com a falta de espaço para o grupo."),
    26617: ("Mas podia ter sido só eu...", "Misha soltando a insinuação íntima mais doce e ousada da cena."),
}

max_map = {
    26594: 112, 26595: 16, 26596: 144, 26597: 40, 26598: 104, 26599: 32,
    26600: 120, 26601: 152, 26602: 112, 26603: 24, 26604: 80, 26605: 24,
    26606: 104, 26607: 112, 26608: 184, 26609: 104, 26610: 128, 26611: 96,
    26612: 88, 26613: 128, 26614: 136, 26615: 72, 26616: 128, 26617: 80
}

all_ok = True
for tid, val in calib_0268.items():
    txt = val[0] if isinstance(val, tuple) else val
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        errs = validate_line(tid, "", txt)
        if errs:
            all_ok = False
            print(f"ERRO VALIDACAO ID {tid}: {errs} -> {txt}")
        else:
            print(f"OK ID {tid}: {sz}B <= {maxb}B")

if all_ok:
    print("=== 0268 100% PERFEITO ===")

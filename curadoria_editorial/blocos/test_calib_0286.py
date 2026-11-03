import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0286 = {
    27026: 80, 27027: 120, 27028: 64, 27029: 168, 27030: 160, 27031: 168,
    27032: 168, 27033: 144, 27034: 88, 27035: 112, 27036: 128, 27037: 72,
    27038: 120, 27039: 96, 27040: 152, 27041: 72, 27042: 176, 27043: 88,
    27044: 168, 27045: 144, 27046: 136, 27047: 176, 27048: 64, 27049: 200
}

calib_0286 = {
    27026: ("...Não vai ensinar besteira pra ela.", "Misha alertando com ciúme para não corromper Shurelia. (74B <= 80B)"),
    27027: ("Você e Shurelia andam tãoCRpróximos... Que inveja.", "Misha expressando ciúme dengoso com CR. (104B <= 120B)"),
    27028: ("P-Parece tanto assim?", "Lyner ficando desconcertado diante da provocação. (43B <= 64B)"),
    27029: ("Sei que vocês conversam à noite,CRmas parece que andam se divertindoCRaté demais.", "Misha detalhando as conversas noturnas dos dois com CRs. (166B <= 168B)"),
    27030: ("Ué, já que estamos conversando,CReu também não quero ser chato, sabe?", "Lyner justificando seu empenho no diálogo com CR. (143B <= 160B)"),
    27031: ("Não acho que seja ruim, mas...CRé que... fico curiosa, sabe?", "Misha admitindo curiosidade e incômodo afetivo com CR. (123B <= 168B)"),
    27032: ("Tipo... se você e Shurelia não têmCRalgum casinho estranho ou algo assim...", "Misha insinuando medo de romance secreto com CR. (154B <= 168B)"),
    27033: ("Ultimamente você só conversaCRcom a Shurelia todo santo dia.", "Misha cobrando a atenção exclusiva de Lyner com CR. (123B <= 144B)"),
    27034: ("Eu quase nem falo com vocêCRultimamente!", "Misha reclamando da falta de tempo a dois com CR. (82B <= 88B)"),
    27035: ("Eu também quero conversarCRde montão com você...", "Misha revelando seu anseio por intimidade com CR. (100B <= 112B)"),
    27036: ("Er... D-Desculpa. Pensando bem,CRacho que você tem razão...", "Lyner reconhecendo sua falha de atenção com CR. (121B <= 128B)"),
    27037: ("A gente conversa bastante, Misha.", "Lyner prometendo compensar o tempo perdido. (67B <= 72B)"),
    27038: ("...Não, desculpa eu por serCRtão manhosa e egoísta.", "Misha se desculpando pela cobrança possessiva com CR. (106B <= 120B)"),
    27039: ("O que você e ShureliaCRcostumam conversar?", "Misha investigando os tópicos das conversas alheias com CR. (86B <= 96B)"),
    27040: ("Como assim?... Acho que a genteCRnão fala nada demais nemCRde outro mundo.", "Lyner minimizando os assuntos das conversas com CRs. (150B <= 152B)"),
    27041: ("Mas vocês se falam todo dia!", "Misha retrucando a frequência diária dos diálogos. (58B <= 72B)"),
    27042: ("Nunca conversei direito com ela,CRentão nem imagino como é.", "Misha comentando sobre o mistério da convivência com Shurelia com CR. (121B <= 176B)"),
    27043: ("Não é disso que eu queriaCRfalar, poxa!", "Misha cortando rodeios e voltando ao cerne afetivo com CR. (81B <= 88B)"),
    27044: ("Se tem tanto assunto com ela,CRcom certeza tem comigo também, né?", "Misha reivindicando paridade afetiva de assuntos com CR. (133B <= 168B)"),
    27045: ("Me dê mais atenção, ou vou invadirCRo seu quarto todo santo dia!", "Misha fazendo ultimato cômico e dengoso com CR. (130B <= 144B)"),
    27046: ("Sinto que ando usando o quimonoCRbranco com frequência demais...", "Misha estranhando o uso excessivo do quimono nupcial com CR. (130B <= 136B)"),
    27047: ("É?... Bem, só quem veste diretoCRdeve reparar nisso, imagino.", "Lyner ponderando sobre o costume de combate com CR. (125B <= 176B)"),
    27048: ("Não que eu não goste dele!", "Misha ressalvando seu apreço pelo traje cerimonial. (55B <= 64B)"),
    27049: ("É que, sabe... é um traje tão especial...CRE eu queria que o momento tambémCRfosse especial...", "Misha revelando o peso nupcial sagrado do shiromuku com CRs. (193B <= 200B)")
}

all_ok = True
for tid, (txt, rat) in calib_0286.items():
    maxb = max_map_0286[tid]
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
    print("=== 0286 100% PERFEITO ===")

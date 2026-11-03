import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0279 = {
    26858: 56, 26859: 160, 26860: 120, 26861: 48, 26862: 136, 26863: 80,
    26864: 104, 26865: 88, 26866: 88, 26867: 144, 26868: 96, 26869: 176,
    26870: 136, 26871: 120, 26872: 104, 26873: 216, 26874: 168, 26875: 64,
    26876: 136, 26877: 48, 26878: 128, 26879: 144, 26880: 112, 26881: 120
}

calib_0279 = {
    26858: ("Hehehe, é o meu tesouro!", "Misha acariciando a ocarina presenteada por Lyner."),
    26859: ("É? Se você ficou tão feliz,CRvaleu a pena o esforço pra fazer.", "Lyner feliz com a gratidão de Misha com CR."),
    26860: ("Valeu... Mas você fez issoCRquando era pequeno, né?", "Misha indagando sobre a confecção na infância com CR."),
    26861: ("É... acho que sim.", "Lyner respondendo com dúvida na memória."),
    26862: ("Lembro de te dar a ocarina,CRmas não lembro direito de criar ela.", "Lyner explicando a névoa em sua memória com CR."),
    26863: ("...Talvez alguém tenha me ajudado.", "Lyner cogitando ajuda externa na infância."),
    26864: ("É? Mas quem me deu a ocarinaCRfoi você, Lyner.", "Misha reafirmando que o presente veio de Lyner com CR."),
    26865: ("E dessa vez, você fez tudo sozinho!", "Misha valorizando o empenho exclusivo de Lyner."),
    26866: ("Isso já é mais que suficiente pra mim.", "Misha comovida com a dedicação de Lyner."),
    26867: ("Se eu que ganhei tô dizendo, é fato!CRObrigada de verdade, Lyner.", "Misha agradecendo comovida com quebra CR."),
    26868: ("Ei, Misha...CRJá curou o medo de altura?", "Lyner perguntando sobre a acrofobia de Misha com CR."),
    26869: ("Claro que não! Se curasse tão fácil,CReu não passava por tanto sufoco!", "Misha revoltada com a ideia de cura mágica com CR."),
    26870: ("É? Mas quando fomos ao Rinkernator,CRvocê tava super tranquila.", "Lyner citando a visita ao Rinkernator com CR."),
    26871: ("Até disse que a vista era linda,CRentão achei que...", "Lyner lembrando o elogio à paisagem com CR."),
    26872: ("Ah, mas claro!CRPara e pensa um pouco:", "Misha introduzindo a lógica de alturas extremas com CR."),
    26873: ("Era tão alto que nem dava pra ver o chão,CRsó o topo das nuvens lá embaixo!CRNão dava nem pra ter medo!", "Misha explicando que o excesso de altitude anula o medo com CR."),
    26874: ("Numa altura daquelas, o medo até someCRporque o cérebro nem processa!", "Misha detalhando a perda da sensação de perigo com CR."),
    26875: ("É... parando pra pensar...", "Lyner ponderando o ponto de vista inusitado."),
    26876: ("Mas logo abaixo da Blastline,CRaí eu ainda tremo na base.", "Misha admitindo pavor na zona da Blastline com CR."),
    26877: ("Que complicação...", "Lyner achando o medo seletivo de Misha enrolado."),
    26878: ("Ei, Lyner... Eu até entendoCRos seus fetiches e gostos, mas...", "Misha acusando Lyner de tarado por trajes com CR."),
    26879: ("Vestir esse traje Magical ShowerCRé constrangedor demais...", "Misha reclamando da sensualidade infantil do figurino com CR."),
    26880: ("Posso ser baixinha, mas jáCRtô com quase vinte anos!", "Misha reivindicando sua maturidade etária com CR."),
    26881: ("Desculpa pela roupa, mas... vocêCRchamou de fetiche meu?!", "Lyner indignado com a insinuação maldosa com CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0279.items():
    maxb = max_map_0279[tid]
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
    print("=== 0279 100% PERFEITO ===")

import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0276 = {
    26786: 80, 26787: 80, 26788: 88, 26789: 152, 26790: 80, 26791: 120,
    26792: 40, 26793: 88, 26794: 120, 26795: 48, 26796: 160, 26797: 144,
    26798: 192, 26799: 136, 26800: 176, 26801: 120, 26802: 128, 26803: 80,
    26804: 80, 26805: 168, 26806: 72, 26807: 128, 26808: 88, 26809: 112
}

calib_0276 = {
    26786: ("Não adianta nada usar isso aqui.", "Lyner alertando sobre a inutilidade do item fora de batalha."),
    26787: ("Esse item só funciona contra inimigos!", "Lyner explicando o escopo combativo de Peeka."),
    26788: ("Ah, quanto a isso tá sossegado!", "Misha descartando a restrição com humor."),
    26789: ("Quem atrapalha a gente a sósCRé inimigo sim! Quer chamar do quê?", "Misha definindo invasores do descanso como inimigos com CR."),
    26790: ("...Tem algo erradoCRnessa sua lógica.", "Lyner achando a dedução de Misha distorcida com CR."),
    26791: ("Olha, a Semente de Phebes!CRQue coisa nostálgica você tem.", "Misha reconhecendo o item clássico com quebra CR."),
    26792: ("Nostálgica como?", "Lyner perguntando sobre a nostalgia do item."),
    26793: ("Não sabia? É a comidaCRfavorita do Harm!", "Misha revelando o petisco predileto de Harm com CR."),
    26794: ("Antigamente ele comia tantoCRque parecia até viciado!", "Misha descrevendo a compulsão antiga de Harm com CR."),
    26795: ("...Bem a cara dele.", "Lyner achando típico da personalidade excêntrica de Jack."),
    26796: ("Mas hoje em dia ele quase nem tocaCRnisso. Será que aconteceu algo?", "Misha estranhando o abandono do petisco com CR."),
    26797: ("Certeza que não é grande coisa.CRAfinal de contas, é o Jack.", "Lyner desdenhando qualquer mistério profundo sobre Jack com CR."),
    26798: ("Ou ficou sem grana pra comprar,CRou só enjoou mesmo. Aposto que éCRuma bobagem dessas.", "Lyner elencando motivos fúteis para a mudança de hábito com CR."),
    26799: ("Ou o clássico: comeu tanto queCRteve uma bela dor de barriga.", "Lyner sugerindo a indigestão óbvia com CR."),
    26800: ("Ah, isso não é motivo. Dor de barrigaCRde tanto comer ele tinha direto,CRe nem ligava!", "Misha rebatendo que dores de estômago eram rotina para Harm com CR."),
    26801: ("...Como consegue repetir a mesmaCRbobagem tantas vezes?", "Lyner inconformado com a teimosia estúpida de Jack com CR."),
    26802: ("Lyner, o que vai fazer com essaCRviga de aço gigante aí?", "Misha questionando a posse do pesado item de síntese com CR."),
    26803: ("Ué, o que mais? Vou usar, claro!", "Lyner defendendo a utilidade da estrutura metálica."),
    26804: ("Então trata de usar isso logo!", "Misha exigindo agilidade no uso do item pesado."),
    26805: ("Ficar carregando um trambolho pesadoCRdesses pela viagem inteira é um atraso!", "Misha reclamando do peso morto na bagagem da equipe com CR."),
    26806: ("É... pensando bem, tem razão...", "Lyner admitindo o transtorno do peso."),
    26807: ("Decidido então! Usa logo issoCRnum Grathmeld!", "Misha intimando Lyner a sintetizar com o item com CR."),
    26808: ("Pensando bem, sobre a viga de aço...", "Misha puxando novamente o tópico da viga."),
    26809: ("Hã? Ah, desculpa...CRUma viga daquelas atrapalha, né?", "Lyner se desculpando pelo volume incômodo com CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0276.items():
    maxb = max_map_0276[tid]
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
    print("=== 0276 100% PERFEITO ===")

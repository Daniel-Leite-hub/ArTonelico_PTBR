import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0271 = {
    26666: 104, 26667: 152, 26668: 88, 26669: 24, 26670: 216, 26671: 168,
    26672: 120, 26673: 40, 26674: 160, 26675: 144, 26676: 80, 26677: 200,
    26678: 200, 26679: 112, 26680: 88, 26681: 72, 26682: 24, 26683: 72,
    26684: 72, 26685: 128, 26686: 64, 26687: 128, 26688: 128, 26689: 80
}

calib_0271 = {
    26666: ("É. A grade prateada do fundoCRparece bem firme.", "Lyner concordando sobre a solidez da grade prateada na Torre com CR."),
    26667: ("Talvez haja algum mecanismo vitalCRda Torre lá atrás.", "Lyner especulando sobre mecanismos vitais da Torre com quebra CR."),
    26668: ("...Será que é isso mesmo?", "Misha duvidando com tom misterioso e sagaz."),
    26669: ("Como assim?", "Lyner confuso com o ceticismo de Misha."),
    26670: ("É intuição, mas sinto que tem um baitaCRtesouro atrás daquelas portas.CRMeu faro não falha...", "Misha farejando tesouros secretos com quebras CR."),
    26671: ("Se quer tanto saber, por que não pedeCRpra Tastiella abrir pra você?", "Lyner sugerindo pedir permissão a Tastiella com CR."),
    26672: ("...Acho impossível.CRJá pedi isso pra ela uma vez.", "Misha descartando a ideia por experiência prévia com CR."),
    26673: ("Ela recusou?", "Lyner perguntando sobre a resposta de Tastiella."),
    26674: ("Uhum. Quando eu era pequena e curiosa,CRfui lá e pedi pra ela.", "Misha relembrando o pedido de infância com CR."),
    26675: ("Aí ela se descontrolou todinha,CRdizendo que era proibido ir lá...", "Misha relatando a reação transtornada de Tastiella com CR."),
    26676: ("...N-nem consigo imaginar ela assim.", "Lyner chocado ao imaginar Tastiella descontrolada."),
    26677: ("Foi a única vez na vida que vi ela daqueleCRjeito... E aí, ficou curioso, né?", "Misha instigando a curiosidade de Lyner com CR."),
    26678: ("Mas ela não vai abrir mesmo... Agora meCRarrependo de perguntar, porque vou morrerCRde curiosidade.", "Misha frustrada por atiçar a curiosidade em vão com CR."),
    26679: ("Ei, Lyner... Por acaso você tá comCRpeixe seco aí?", "Misha farejando o lanche de Lyner com CR."),
    26680: ("Hã? Tô sim... Mas como você adivinhou?", "Lyner surpreso com o faro afiado de Misha."),
    26681: ("Adivinhei nada!CRVocê nem percebeu?", "Misha indignada com a lerdeza de Lyner com CR."),
    26682: ("Hã? O quê?", "Lyner sem entender nada."),
    26683: ("O cheiro! GrudouCRno seu corpo.", "Misha apontando o odor de mirin entranhado com CR."),
    26684: ("Sério?! Nem noteiCRnada!", "Lyner surpreso por não sentir o próprio cheiro com CR."),
    26685: ("A gente nunca nota o próprio cheiro.CRToma um banho depois.", "Misha mandando Lyner se lavar com CR."),
    26686: ("Detesto vocêCRfedendo a peixe.", "Misha fazendo bico dengoso com quebra CR."),
    26687: ("Ah é, você foi na loja de cartas outroCRdia, né, Lyner?", "Misha puxando o assunto das cartas colecionáveis."),
    26688: ("Hum, fui. Tinha tanta carta láCRque me deu curiosidade.", "Lyner explicando seu interesse nas cartas com CR."),
    26689: ("É bom tomar cuidado com aquelas cartas.", "Misha dando um aviso sério sobre as cartas.")
}

all_ok = True
for tid, (txt, rat) in calib_0271.items():
    maxb = max_map_0271[tid]
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
    print("=== 0271 100% PERFEITO ===")

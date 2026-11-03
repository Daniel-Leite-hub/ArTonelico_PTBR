import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0282 = {
    26930: 16, 26931: 112, 26932: 88, 26933: 64, 26934: 88, 26935: 72,
    26936: 32, 26937: 144, 26938: 136, 26939: 80, 26940: 80, 26941: 184,
    26942: 120, 26943: 168, 26944: 104, 26945: 104, 26946: 200, 26947: 72,
    26948: 104, 26949: 136, 26950: 128, 26951: 136, 26952: 64, 26953: 168
}

calib_0282 = {
    26930: ("Ah, é?", "Lyner surpreso com a revelação da roupa."),
    26931: ("Como assim?! Me fez vestirCRsem nem saber o que era?!", "Misha perplexa com o desconhecimento de Lyner com CR."),
    26932: ("Achei que era um otakuCRde cosplay!", "Misha acusando Lyner de otaku por cosplay com CR."),
    26933: ("Nossa, já ficouCRbem tarde...", "Misha notando o avançar da hora no descanso com CR."),
    26934: ("É mesmo. Não tá ficandoCRcom sono?", "Lyner perguntando sobre o cansaço dela com CR."),
    26935: ("É verdade...CREntão, transformar!", "Misha anunciando a troca de roupa com CR."),
    26936: ("Prontinho!", "Misha vestida com o pijama."),
    26937: ("Não muda do nada!CRPor que colocou o Sheep Sweets?!", "Lyner assustado com a transformação repentina com CR."),
    26938: ("Se eu apagar no sono conversando,CRjá tô de pijama, ué!", "Misha justificando pragmaticamente a troca de roupa com CR."),
    26939: ("Mas eu já vou voltar pro meu quarto...", "Lyner anunciando sua retirada."),
    26940: ("Ah, fica aquiCRe dorme comigo hoje~!", "Misha convidando Lyner para dormir com ela dengosa com CR."),
    26941: ("Geralmente é o cara que fala isso, né?CRSendo você, até soa natural...", "Lyner achando o convite atípico mas característico de Misha com CR."),
    26942: ("Poxa! Por que sempre dáCRas respostas mais sem graça?!", "Misha frustrada com a falta de ousadia romântica de Lyner com CR."),
    26943: ("Sabe, Lyner... Queria parar de lutarCRvestindo só aquela camisa social...", "Misha pedindo para retirar a camisa reveladora com CR."),
    26944: ("Ué, por quê... Bom, que perguntaCRboba a minha...", "Lyner percebendo o absurdo de sua pergunta com CR."),
    26945: ("Pois é! Cheguei no limiteCRda vergonha!", "Misha afirmando seu limite de constrangimento com CR."),
    26946: ("E ultimamente, meu corpo tá... sabe...CRreagindo de um jeito meio perigosoCRem vários sentidos...", "Misha corando ao confessar sensações íntimas perigosas com quebras CR."),
    26947: ("Er... tá tão perigosoCRassim?", "Lyner nervoso com a insinuação física com CR."),
    26948: ("Tô falando sério,CRdá uma trégua pra mim...", "Misha pedindo misericórdia com CR."),
    26949: ("...Ou será que se acontecer algo,CRvocê assume a responsabilidade?", "Misha cobrando responsabilidade afetiva dengosa com CR."),
    26950: ("Mas olha, você é mesmo um prodígio,CRcomo todo mundo diz.", "Lyner elogiando o talento de Misha com CR."),
    26951: ("Tece tantas Canções num piscarCRde olhos que é de cair o queixo.", "Lyner admirado com a rapidez na tecelagem de Magias com CR."),
    26952: ("Sério, você é incrível!", "Lyner reafirmando sua admiração sincera."),
    26953: ("Hehehe... Pois é! Não sou qualquerCRReyvateil de esquina! O padrão aquiCRé outro!", "Misha ostentando orgulhosa sua qualidade superior como Reyvateil com quebras CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0282.items():
    maxb = max_map_0282[tid]
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
    print("=== 0282 100% PERFEITO ===")

import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0253 = {
    26234: "Não precisa se desculpar. CReu também tava preocupada com isso.", # 136
    26235: "E eu também não queria ficar com esseCRgosto amargo... Então agora vamosCRacabar com tudo de vez!", # 208
    26236: "Aí a gente vai poder voltarCRa ter uma vida normal...", # 104
    26237: "Queria abrir uma loja um dia,CRigualzinha à da Claire.", # 112
    26238: "Hã? Você vai abrir um barCRtambém?", # 80
    26239: "Bar não dá. Não bebo nada.", # 64
    26240: "Tem alguma loja em mente?", # 72
    26241: "Hã? Ah... a-ainda não decidi,CRmas queria muito ter uma.", # 152
    26242: "Legal! Já tô curioso pra verCRque tipo de loja vai ser.", # 120
    26243: "Sim, mas seria bem melhorCRse tivesse alguém pra me ajudar...", # 152
    26244: "Se alguém que me apoia ficasseCRao meu lado, tenho certeza de queCReu me esforçaria pra valer...", # 200
    26245: "Lyner... você já viu bastanteCRda minha Cosmosfera?", # 112
    26246: "É... acho que a metade.", # 56
    26247: "A metade!? Não achei que vocêCRjá tinha visto tanto assim...", # 144
    26248: "Mas depois de tantos Mergulhos,CRera de se esperar, né...", # 120
    26249: "A-ah... achou ruim?", # 56
    26250: "Não, imagina! Mas... você acabouCRvendo até o que eu tentava esconder, né?", # 152
    26251: "Não se desiludiu comigo?CRVendo as coisas que eu penso...", # 120
    26252: "Já te disse antes que não...CRNossa, é verdade! Você não lembraCRdo que rola na Cosmosfera, né?", # 224
    26253: "A-aconteceu algo lá dentro?", # 80
    26254: "Não é nada, não esquenta.", # 64
    26255: "Mas... dentro da minha mente...", # 64
    26256: "Eu nunca ia me desiludir nem te odiarCRpor isso. Já te falei issoCRna Cosmosfera também.", # 184
    26257: "Pelo contrário! Fico feliz emCRmergulhar tão fundo e ver esseCRseu lado de verdade.", # 152
}

max_map = {
    26234: 136, 26235: 208, 26236: 104, 26237: 112, 26238: 80, 26239: 64,
    26240: 72, 26241: 152, 26242: 120, 26243: 152, 26244: 200, 26245: 112,
    26246: 56, 26247: 144, 26248: 120, 26249: 56, 26250: 152, 26251: 120,
    26252: 224, 26253: 80, 26254: 64, 26255: 64, 26256: 184, 26257: 152
}

all_ok = True
for tid, txt in calib_0253.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0253:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

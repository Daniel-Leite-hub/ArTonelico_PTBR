import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0254 = {
    26258: "É verdade. Pra que eu iaCRmentir pra você?", # 88
    26259: "Eu nunca ia te odiar.CREntão não precisa se preocupar.", # 120
    26260: "Obrigada... Fico tão feliz.", # 64
    26261: "Mas é tão estranho... É a primeira vezCRque ouço isso aqui fora, mas sinto como seCRjá tivesse ouvido antes... Que bom...", # 248
    26262: "Você vem conversar comigoCRtoda noite ultimamente. Fico tão feliz...", # 136
    26263: "É mesmo? Nem achei que a genteCRfalava tanto assim.", # 104
    26264: "É? Então a gente precisaCRconversar muito mais ainda!", # 120
    26265: "Queria que falasse assimCRcomigo pra sempre...", # 96
    26266: "A pessoa que você admira,CRque me falou antes, é a Shurelia?", # 136
    26267: "É ela mesma. Foi ela quemCRme deu o Broche Hymne.", # 128
    26268: "É mesmo...? Ela era tão diferenteCRdo que eu imaginava que fiqueiCRaté surpresa.", # 168
    26269: "Diferente?CRDa Shurelia?", # 48
    26270: "Sim. Como disseram que era mulher,CRachei que fosse linda, mas o rosto delaCRtá coberto e nem dá pra ver.", # 216
    26271: "E ela é gigante! Ou seráCRque é a armadura que é enorme?", # 136
    26272: "Deve ser. Pra falar a verdade,CReu também nunca vi o rosto dela...", # 136
    26273: "A Espada Cortante dói bemCRmais do que magias comuns ou fogo, né?", # 160
    26274: "Pois é. Chove espada giganteCRdo céu! Pra quem leva o golpe,CRdeve ser um inferno.", # 176
    26275: "Por que você não pega uma daquelasCRespadas pra usar? Podia ficar bem forte!", # 160
    26276: "Nem pensar, elas são grandesCRdemais pra eu brandir...", # 120
    26277: "Quando usei essa magia,CRnem acreditei no que vi!", # 96
    26278: "Nunca imaginei sair um mundaréuCRde Don Leon! Fiquei tão feliz...", # 128
    26279: "Eu achei foi aterrorizante,CRisso sim.", # 88
    26280: "Mas pra mim, o meu verdadeiroCRherói... é outro...", # 136
    26281: "Hã? Falou alguma coisa?", # 56
}

max_map = {
    26258: 88, 26259: 120, 26260: 64, 26261: 248, 26262: 136, 26263: 104,
    26264: 120, 26265: 96, 26266: 136, 26267: 128, 26268: 168, 26269: 48,
    26270: 216, 26271: 136, 26272: 136, 26273: 160, 26274: 176, 26275: 160,
    26276: 120, 26277: 96, 26278: 128, 26279: 88, 26280: 136, 26281: 56
}

all_ok = True
for tid, txt in calib_0254.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0254:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

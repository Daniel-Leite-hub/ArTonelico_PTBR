import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0252 = {
    26210: "Assim!?", # 16
    26211: "Mas... e-essa roupa aí...?", # 56
    26212: "Hahaha... Vestir essa roupa só nósCRdois a sós dá uma vergonha danada.", # 168
    26213: "É, bem... eu também ficoCRmeio sem jeito.", # 96
    26214: "Mas por que vestiu issoCRdo nada?", # 80
    26215: "É que você só foca na lutaCRe nem olha direito pra mim.", # 128
    26216: "Eu sei que não tem jeito... Mas queriaCRque pelo menos agora você olhasseCRbem pra mim...", # 192
    26217: "A-ah... ficou super bemCRem você.", # 80
    26218: "Não tô mentindo! Mas dá uma vergonhaCRficar encarando fixamente...", # 144
    26219: "É, né... Eu também tôCRcom vergonha...", # 88
    26220: "Mas fico feliz! Vou vestir mais vezesCRaté você se acostumar a me ver assim.", # 160
    26221: "Sabe, Lyner...CRqueria te pedir um favor.", # 88
    26222: "Um favor?CRPode falar.", # 48
    26223: "Sim. Mas antes...CRTransformar!", # 64
    26224: "Por que mudar!?CRUou!! E-essa roupa!?", # 80
    26225: "Ué, você sempre me fazCRlutar vestida assim, não faz?", # 112
    26226: "Você já deve saber, mas...CRdá uma vergonha danada, sabia?", # 128
    26227: "O pessoal finge que nem vê,CRmas isso me deixa com mais vergonha ainda...", # 176
    26228: "Então... eu não queria ficarCRvestindo isso em público.", # 128
    26229: "Ugh... d-desculpa.", # 40
    26230: "Eu sou uma garota,CRsabia...?", # 56
    26231: "Mas... se for só nós dois a sós,CRnão ligo de vestir ela pra você...", # 144
    26232: "A gente tava relaxando tão bem,CRmas parece que vem outra correria danadaCRpela frente, né?", # 192
    26233: "É... Desculpa, parece queCRfoi por minha causa...", # 88
}

max_map = {
    26210: 16, 26211: 56, 26212: 168, 26213: 96, 26214: 80, 26215: 128,
    26216: 192, 26217: 80, 26218: 144, 26219: 88, 26220: 160, 26221: 88,
    26222: 48, 26223: 64, 26224: 80, 26225: 112, 26226: 128, 26227: 176,
    26228: 128, 26229: 40, 26230: 56, 26231: 144, 26232: 192, 26233: 88
}

all_ok = True
for tid, txt in calib_0252.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0252:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

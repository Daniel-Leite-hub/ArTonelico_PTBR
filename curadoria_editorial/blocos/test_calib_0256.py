import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0256 = {
    26306: "Bem, no caso da Shurelia,CRnão é uma Cosmosfera de verdade.", # 128
    26307: "Entendi... Não é que eu queiraCRcompetir com ela nem nada, sabe?", # 160
    26308: "Mas pra ser sincera... fiqueiCRcom um pouco de ciúmes.", # 104
    26309: "Se for você, Lyner, pode mergulharCRo quanto quiser que nunca vou recusar.", # 144
    26310: "Só quero que lembre disso.", # 72
    26311: "Ouvi dizer que a Shurelia é especialCRentre as Reyvateils, então nem sabiaCRque dava pra mergulhar nela.", # 192
    26312: "É que lá não tem uma CosmosferaCRpropriamente dita, sabe?", # 144
    26313: "Por isso é meio diferente de mergulharCRem você ou na Misha.", # 120
    26314: "Fiquei curiosa pra saberCRcomo é esse mundo.", # 96
    26315: "Nem pense nisso!CRContinua sendo um Mergulho!", # 88
    26316: "Eu sei.", # 16
    26317: "Ganhei mais uma rival...CRNão posso ficar pra trás...", # 128
    26318: "Conversar com você à noite assimCRjá virou rotina pra gente, né?", # 144
    26319: "É verdade, pensando bem.CRVocê tá cansada? Quer dormir mais cedo?", # 152
    26320: "Não, pelo contrário! Se não falar com você,CRSinto que o cansaço nem vai embora.", # 152
    26321: "Sei lá por quê... mas hoje...CReu queria ficar junto com vocêCRa noite inteira...", # 176
    26322: "Ué, que foi?", # 32
    26323: "N-não, nada! Não é nada!", # 56
    26324: "É? Hum... tá parecendo que vocêCRtá querendo fugir de mim...", # 144
    26325: "Imagina, nada a ver! Se quisesse fugir,CReu não estaria aqui conversandoCRcom você agora.", # 200
    26326: "Eu sei... mas dá uma sensaçãoCRde que você vai escapar a qualquerCRmomento...", # 152
    26327: "Fazer o quê... Quer que eu chegueCRmais perto?", # 88
    26328: "E-êêh!?", # 24
    26329: "No mundo real, você não vaiCRme amarrar que nem lá dentro, né?", # 144
}

max_map = {
    26306: 128, 26307: 160, 26308: 104, 26309: 144, 26310: 72, 26311: 192,
    26312: 144, 26313: 120, 26314: 96, 26315: 88, 26316: 16, 26317: 128,
    26318: 144, 26319: 152, 26320: 152, 26321: 176, 26322: 32, 26323: 56,
    26324: 144, 26325: 200, 26326: 152, 26327: 88, 26328: 24, 26329: 144
}

all_ok = True
for tid, txt in calib_0256.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0256:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

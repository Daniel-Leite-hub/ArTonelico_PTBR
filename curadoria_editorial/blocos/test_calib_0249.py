import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0249 = {
    26138: "Hahaha, bom, eu fiquei feliz,CRentão por mim tudo bem.", # 88
    26139: "Já que tenho um uniforme tão fofo,CRqueria tanto ir pra escola com você...", # 160
    26140: "Pra escola comigo?", # 40
    26141: "Sim! Mas como sou ruim nos estudos,CRia acabar sendo a fracassada da turma.", # 144
    26142: "É, eu odeio estudar, entãoCRia viver matando aula.", # 104
    26143: "Tamo junto, então! Mas imaginarCRisso não é divertido?", # 112
    26144: "Eu fazendo marmita todo diaCRpra você comer... coisa assim...", # 120
    26145: "A-ah... é, pensando bem...CRnão parece má ideia...", # 96
    26146: "Você anda conversando bastanteCRcom a Lady Shurelia, né?", # 88
    26147: "É. Mas às vezes sinto que elaCRfica meio inquieta, sei lá.", # 136
    26148: "Ela quase não falava com ninguém,CRe comigo era só deveres antes...", # 160
    26149: "Imaginei. Ela não me parecia falarCRmuito, por isso até me assustei.", # 176
    26150: "(Não posso falar que ela era igualCRà Aurica quando nos conhecemos...)", # 128
    26151: "Você tá bem chegado da ShureliaCRultimamente, né?", # 96
    26152: "É mesmo?", # 24
    26153: "É que vocês vivem conversando...", # 96
    26154: "Pra não perder, eu tambémCRvou arrumar altas conversas com você!", # 160
    26155: "Você tá íntimo demaisCRcom a Lady Shurelia.", # 88
    26156: "Prefere conversar com elaCRdo que comigo?", # 88
    26157: "Que isso, eu também adoroCRfalar com você!", # 72
    26158: "Mas você parece se divertirCRmuito mais com ela...", # 136
    26159: "N-não, impressão sua...", # 64
    26160: "Que inveja dela...", # 40
    26161: "N-não é isso... digo...", # 56
}

max_map = {
    26138: 88, 26139: 160, 26140: 40, 26141: 144, 26142: 104, 26143: 112,
    26144: 120, 26145: 96, 26146: 88, 26147: 136, 26148: 160, 26149: 176,
    26150: 128, 26151: 96, 26152: 24, 26153: 96, 26154: 160, 26155: 88,
    26156: 88, 26157: 72, 26158: 136, 26159: 64, 26160: 40, 26161: 56
}

all_ok = True
for tid, txt in calib_0249.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0249:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

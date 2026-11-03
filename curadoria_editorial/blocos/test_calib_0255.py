import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0255 = {
    26282: "Nada, hehe!", # 24
    26283: "Com a magia Análise, consigo verCRa durabilidade de um monteCRde coisas diferentes!", # 176
    26284: "Nossa, isso parece bem útil.", # 72
    26285: "Hum... mas dá um certo medo.", # 72
    26286: "Fica ativa o tempo todo! Na cidade,CRvejo até a resistência das casasCRdas pessoas.", # 184
    26287: "Casas tão grandes com umaCRresistência tão mixuruca...", # 120
    26288: "D-de que casa você tá falando,CRafinal?", # 88
    26289: "Invejo tanto a Misha...", # 56
    26290: "Ué, por que isso do nada?", # 88
    26291: "A Misha muda o tamanho do corpoCRquando quer, não é?", # 128
    26292: "Queria ser assim pra ficarCRdo jeito que você prefere.", # 128
    26293: "Ué, eu já falei o meu gostoCRpra alguém?", # 80
    26294: "E se eu ficasse pequenininha?", # 72
    26295: "Como assim? Se eu andasse com umaCRpequena Misha e uma pequena Aurica,CRiam achar com certeza que sou o pai...", # 216
    26296: "Não é isso, seu bobo...!", # 56
    26297: "Tô aprendendo magias cada vezCRmais poderosas, né?", # 104
    26298: "Pois é. Você usa magias tão fortesCRque nem eu aguentaria se levasseCRuma delas.", # 160
    26299: "Sim... É bom aprender magias fortes,CRmas fico meio preocupada também.", # 168
    26300: "E se eu ficar forte demais e vocêCRcomeçar a ter medo de mim...?", # 168
    26301: "Relaxa. Se você não usar pro mal,CRnão tem por que ter medo nenhum.", # 136
    26302: "Eu sei muito bem que você jamaisCRusaria seu poder de forma errada.", # 136
    26303: "Obrigada...CRSó de ouvir isso fico bem mais aliviada.", # 128
    26304: "Você e a Shurelia tãoCRíntimos demais ultimamente...", # 112
    26305: "Você mergulhou bastante nela...CRJá foi assim tão fundo?", # 152
}

max_map = {
    26282: 24, 26283: 176, 26284: 72, 26285: 72, 26286: 184, 26287: 120,
    26288: 88, 26289: 56, 26290: 88, 26291: 128, 26292: 128, 26293: 80,
    26294: 72, 26295: 216, 26296: 56, 26297: 104, 26298: 160, 26299: 168,
    26300: 168, 26301: 136, 26302: 136, 26303: 128, 26304: 112, 26305: 152
}

all_ok = True
for tid, txt in calib_0255.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0255:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

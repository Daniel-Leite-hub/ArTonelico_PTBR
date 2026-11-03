import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0248 = {
    26114: "Não é que não tinha, só esqueceu.CRPor isso me ajudou quando nos vimosCRe lá na Colina Cantante, não foi?", # 224
    26115: "Ah... é verdade, pensando bem.", # 88
    26116: "Não esquece disso, eu sou muitoCRgrato pela sua ajuda, viu?", # 136
    26117: "Desculpa...CRMas falando sério, acho que é a primeiraCRvez que sinto isso.", # 152
    26118: "Então decidi confiar em vocêCRe me esforçar pra te ajudarCRno que eu puder.", # 160
    26119: "Desde que passei a viajar com você,CRSinto que mudei bastante.", # 128
    26120: "Naquela época eu não me garantiaCRe vivia pedindo desculpasCRpor qualquer coisa...", # 168
    26121: "É verdade, você viviaCRse desculpando mesmo.", # 112
    26122: "Poxa, precisava serCRtão direto?", # 64
    26123: "Foi mal! Mas agora você mudou,CRnão é?", # 88
    26124: "Sim... até eu consigo perceber.", # 88
    26125: "E passei a pensar na genteCRcom mais otimismo...", # 104
    26126: "Hã? Pensar na gente?", # 56
    26127: "Hã? Não, nada! O cabeça-dura do LynerCRnão ia entender mesmo.", # 144
    26128: "Eu dizia que deixava você mergulharCRporque confiava em você, mas na verdadeCRnão era bem isso.", # 224
    26129: "Normal. Eu tava quase mortoCRquando a gente se conheceu.", # 144
    26130: "É que sempre fui meio largada, sabe?CRComo ninguém ligava pra mim, eu nuncaCRtive amarras com ninguém.", # 280
    26131: "Eu gosto de você, mas... achei que,CRquanto mais íntimos a gente ficasseCRpelos Mergulhos, menos liberdade eu teria...", # 256
    26132: "Quando pensei nisso, confesso queCRdeu um certo receio.", # 136
    26133: "Será que você viu issoCRquando mergulhou em mim?", # 120
    26134: "Hã? Mas agora você nãoCRpensa mais assim, né?", # 104
    26135: "Não. Posso ter menos liberdade só,CRmas quero achar coisas que a genteCRpossa fazer juntos.", # 200
    26136: "É... Mas você soltou uma confissãoCRbem atrevida aí...", # 112
    26137: "Hã?CR...Ah!", # 24
}

max_map = {
    26114: 224, 26115: 88, 26116: 136, 26117: 152, 26118: 160, 26119: 128,
    26120: 168, 26121: 112, 26122: 64, 26123: 88, 26124: 88, 26125: 104,
    26126: 56, 26127: 144, 26128: 224, 26129: 144, 26130: 280, 26131: 256,
    26132: 136, 26133: 120, 26134: 104, 26135: 200, 26136: 112, 26137: 24
}

all_ok = True
for tid, txt in calib_0248.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0248:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

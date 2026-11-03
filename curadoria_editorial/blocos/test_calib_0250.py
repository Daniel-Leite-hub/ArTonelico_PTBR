import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0250 = {
    26162: "...Brincadeira! Ficou todoCRnervoso, que engraçado.", # 96
    26163: "Tudo bem. A Shurelia sofreuCRtanto até hoje, né?", # 104
    26164: "Mas se ficar só dando bola pra ela,CRvou parar de gostar de você, ouviu?", # 152
    26165: "Ultimamente você só conversaCRcom a Lady Shurelia todo dia.", # 120
    26166: "Tô achando que vocêCRme deixou de lado.", # 80
    26167: "Hã? É mesmo?", # 32
    26168: "Poxa, que maldade!CRNem pensou em mim, né?", # 104
    26169: "N-não é isso!", # 40
    26170: "Eu também queria falarCRbastante com você...", # 80
    26171: "Desculpa... Eu não costumoCRreparar muito nessas coisas.", # 120
    26172: "Vamos conversarCRmais depois.", # 56
    26173: "Ueba!CRVou cobrar, hein!", # 56
    26174: "Parece que você e a ShureliaCRficaram superamigos, né?", # 112
    26175: "Vocês vivem conversandoCRjuntos à noite...", # 104
    26176: "Tem tanto assunto assim com ela?CRQue inveja...", # 120
    26177: "A gente só táCRconversando...", # 56
    26178: "Queria falar maisCRcom você...", # 64
    26179: "Desculpa, acabei te deixandoCRde lado, né?", # 80
    26180: "Se você quiser, a gente conversaCRo quanto você quiser.", # 128
    26181: "Sério!? Hehe,CRque bom...", # 64
    26182: "Ei, Lyner...CRé que...", # 40
    26183: "Que foi? Você parece meioCRinquieta desde antes.", # 112
    26184: "É que... o que você achou da minhaCRCosmosfera agora que viu tudo?", # 144
    26185: "Fiquei curiosa... Seria bomCRse você me contasse...", # 104
}

max_map = {
    26162: 96, 26163: 104, 26164: 152, 26165: 120, 26166: 80, 26167: 32,
    26168: 104, 26169: 40, 26170: 80, 26171: 120, 26172: 56, 26173: 56,
    26174: 112, 26175: 104, 26176: 120, 26177: 56, 26178: 64, 26179: 80,
    26180: 128, 26181: 64, 26182: 40, 26183: 112, 26184: 144, 26185: 104
}

all_ok = True
for tid, txt in calib_0250.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0250:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0258 = {
    26354: "Não seja modesto... Você me ajudouCRa me enturmar com o pessoal, e...", # 144
    26355: "Hã? V-você não tá perto demais,CRnão?", # 96
    26356: "Agora consigo até ficarCRpertinho de você...", # 80
    26357: "M-mas ainda tô com bastanteCRvergonha...", # 104
    26358: "Você demorou pra vir hoje,CRLyner.", # 72
    26359: "É? Achei que vim no horárioCRde sempre.", # 88
    26360: "Nada disso! Você sempre vem mais cedo!CRPor que demorou tanto hoje?", # 136
    26361: "Por acaso foi verCRoutra pessoa?", # 64
    26362: "Imagina! Se fosse isso,CReu teria chegado bem mais tarde...", # 120
    26363: "Hum, é? Então você ficaCRde papo até tarde com as outras, né~?", # 136
    26364: "Não fico falando tanto assim...", # 72
    26365: "Ultimamente acho que vocêCRé um baita mulherengo, sabia?", # 152
    26366: "Mulherengo?", # 24
    26367: "Será que você não finge ser indecisoCRsó pra tirar casquinha de todo mundoCRbem na surdina...?", # 208
    26368: "Isso não é mulherengo,CRé ser vilão!", # 80
    26369: "Mas pareceCRmuito~...", # 48
    26370: "Qual é, me dá um tempo,CRsério...", # 80
    26371: "Se não fizer isso,CRnão sossego.", # 72
    26372: "Hã? Quê!?", # 24
    26373: "S-se eu segurar sua mão assim,CRvocê não tem como fugir, né?", # 136
    26374: "É, não tem como, mas... eu tô aquiCRfalando com você, não vouCRfugir pra lugar nenhum!", # 184
    26375: "E além disso... como a gente vaiCRconversar direito desse jeito?", # 136
    26376: "É verdade... mas dá vontadeCRde não soltar... É um dilema difícil,CRmas bem gostoso.", # 176
    26377: "Falando nisso... a minha Cosmosfera...CRvocê já viu quase tudo, né?", # 136
}

max_map = {
    26354: 144, 26355: 96, 26356: 80, 26357: 104, 26358: 72, 26359: 88,
    26360: 136, 26361: 64, 26362: 120, 26363: 136, 26364: 72, 26365: 152,
    26366: 24, 26367: 208, 26368: 80, 26369: 48, 26370: 80, 26371: 72,
    26372: 24, 26373: 136, 26374: 184, 26375: 136, 26376: 176, 26377: 136
}

all_ok = True
for tid, txt in calib_0258.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0258:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

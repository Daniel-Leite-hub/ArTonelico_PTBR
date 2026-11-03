import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0251 = {
    26186: "Minha impressão? Bem... é meioCRdifícil resumir em poucas palavras.", # 160
    26187: "Rolou tanta coisa, e a cada vezCReu via um lado diferente seu.", # 136
    26188: "Um lado diferente meu?", # 72
    26189: "É, suas emoções, digamos assim.", # 88
    26190: "Entendi... Então... você já sabeCRo que eu sinto por você, né?", # 128
    26191: "...Bom, eu meio que vi tudo.", # 72
    26192: "Poxa... Sendo indeciso ou tímido,CRnão vai me fazer esperar muito, viu?", # 136
    26193: "Senão... eu mesma vou tomarCRuma atitude...", # 96
    26194: "Falando nisso, o que você achaCRda armadura SERAPH?", # 104
    26195: "Combina com você.CRE além disso, é maneira.", # 96
    26196: "Beleza! Então agora mesmoCReu me transformo pra você!", # 120
    26197: "Hã, aqui?", # 24
    26198: "Lá vou eu!", # 24
    26199: "Transforma!", # 24
    26200: "Uau!?", # 16
    26201: "Hehe, prontinho!CRFicou bom?", # 80
    26202: "É, fica irado não importaCRquantas vezes eu veja.", # 96
    26203: "É? Obrigada! Mas ouvir issoCRsó nós dois a sós dá uma vergonha...", # 136
    26204: "...Mas pensando bem agora...", # 72
    26205: "Mesmo ficando bem, usar armaduraCRsó nós dois a sós não combina nada...", # 168
    26206: "...Vou tirar ela.", # 48
    26207: "Tirar? Uou, de novo!?", # 48
    26208: "Ufa... No quarto é bem melhorCRficar assim mesmo.", # 112
    26209: "Agora, do nada...CRTransformar!!", # 96
}

max_map = {
    26186: 160, 26187: 136, 26188: 72, 26189: 88, 26190: 128, 26191: 72,
    26192: 136, 26193: 96, 26194: 104, 26195: 96, 26196: 120, 26197: 24,
    26198: 24, 26199: 24, 26200: 16, 26201: 80, 26202: 96, 26203: 136,
    26204: 72, 26205: 168, 26206: 48, 26207: 48, 26208: 112, 26209: 96
}

all_ok = True
for tid, txt in calib_0251.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0251:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

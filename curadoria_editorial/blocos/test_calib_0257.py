import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0257 = {
    26330: "A-amarrar!?", # 24
    26331: "Só pra avisar: eu não tenhoCResse tipo de fetiche!", # 104
    26332: "...É-é verdade. Que susto...CRVocê fala cada coisa estranha do nada!", # 160
    26333: "É que... esquece. Se eu falar mais,CRvai virar um baita mal-entendido.", # 152
    26334: "Hum... Então, Lyner...", # 56
    26335: "Sobre aquilo de antes... queria que vocêCRficasse mais pertinho pra conversar...", # 168
    26336: "Ei, a Aurica de agora tá muitoCRdiferente de quando nos conhecemos?", # 144
    26337: "Você sempre faz perguntasCRdifíceis de responder...", # 104
    26338: "Que maldade!", # 40
    26339: "Tô brincando! Mas falando sério,CRvocê mudou da água pro vinho.", # 168
    26340: "No começo, parecia que você mantinhaCRdistância de todo mundoCRquando falava com a gente.", # 176
    26341: "Se me enganei, desculpa.", # 64
    26342: "Não se enganou.CRÉ bem isso mesmo.", # 88
    26343: "Eu pesava o clima com frequência,CRné?", # 88
    26344: "Bem... só de vez em quando.", # 56
    26345: "Sabia. Devo ter incomodadoCRbastante todo mundo...", # 104
    26346: "Acha? Não lembro de vocêCRter incomodado ninguém.", # 112
    26347: "Claro que diria isso.CRVocê é gentil demais.", # 96
    26348: "Desde aquela época você iaCRno meu quarto falar comigo, né?", # 128
    26349: 'Hahaha... No começo, quando eu ia,CRvocê soltava um seco "Que foi?"...', # 144
    26350: "Eu era tão fria, né?CRNem sei como você não foi emboraCRde vez.", # 144
    26351: "Mas foi porque você cuidou de mimCRdesse jeito, além dos Mergulhos,CRque eu consegui mudar.", # 184
    26352: "Queria te agradecer, mas a únicaCRcoisa que sei fazer é cozinhar...", # 160
    26353: "A-ah... n-não esquenta com isso.", # 64
}

max_map = {
    26330: 24, 26331: 104, 26332: 160, 26333: 152, 26334: 56, 26335: 168,
    26336: 144, 26337: 104, 26338: 40, 26339: 168, 26340: 176, 26341: 64,
    26342: 88, 26343: 88, 26344: 56, 26345: 104, 26346: 112, 26347: 96,
    26348: 128, 26349: 144, 26350: 144, 26351: 184, 26352: 160, 26353: 64
}

all_ok = True
for tid, txt in calib_0257.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0257:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

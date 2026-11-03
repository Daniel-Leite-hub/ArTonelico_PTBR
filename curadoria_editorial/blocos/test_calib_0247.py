import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0247 = {
    26090: "Mas ultimamente comecei a terCRum pouco mais de confiança em mim.", # 136
    26091: "Sempre que mergulha, aprendoCRmais e mais magias...", # 104
    26092: "Ah, sim! Vou te contarCRsobre o Don Leon.", # 96
    26093: "É um bicho de pelúcia que a ClaireCRme deu, mas é super fofo e maneiro!", # 152
    26094: "É... fofo e maneiro... sei.", # 64
    26095: "Ué, o que foi?", # 40
    26096: "Não, nada. Você gostavaCRtanto assim dele?", # 96
    26097: "Sim. Ele sempre foiCRmeu grande apoio.", # 64
    26098: "Cuidei dele desde que ganhei...CRmas não tive coragemCRde trazer ele comigo...", # 192
    26099: "Mas ele ainda tá lá...CRna casa onde eu morava.", # 104
    26100: "Aurica, você não tá sentindoCRnada de ruim?", # 88
    26101: "Hã? Tô bem, por quê?", # 64
    26102: "É que a gente vive viajando,CRfiquei com medo de vocêCRacabar passando mal.", # 184
    26103: "Obrigada. Mas tô bem,CRnão esquenta.", # 72
    26104: "É? Que bom, então.", # 40
    26105: "Lyner, obrigada mesmoCRpor me dar o Don Leon de presente.", # 128
    26106: "Não foi nada.", # 32
    26107: "Mas não era esse o bonecoCRque você deixou na sua terraCRcomo lembrança?", # 160
    26108: "Fiquei até na dúvida se fiz bemCRem criar algo que você queria guardarCRsó na memória.", # 192
    26109: "Imagina! Fiquei tão feliz...", # 56
    26110: "Eu me sentia tão sozinha...CREntão quando você fez isso pra mim,CRfiquei feliz de verdade.", # 184
    26111: "E graças a isso... como posso dizer?CRSinto que mudei.", # 152
    26112: "Vontade de confiar em alguémCRe de ajudar os outros, sabe?", # 120
    26113: "Até pouco tempo, eu tinhaCResquecido isso... ou talvezCRnem sentisse nada...", # 176
}

max_map = {
    26090: 136, 26091: 104, 26092: 96, 26093: 152, 26094: 64, 26095: 40,
    26096: 96, 26097: 64, 26098: 192, 26099: 104, 26100: 88, 26101: 64,
    26102: 184, 26103: 72, 26104: 40, 26105: 128, 26106: 32, 26107: 160,
    26108: 192, 26109: 56, 26110: 184, 26111: 152, 26112: 120, 26113: 176
}

all_ok = True
for tid, txt in calib_0247.items():
    maxb = max_map[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        print(f"OK ID {tid}: {sz}B <= {maxb}B -> {txt}")

print("0247:", "TODOS OK!" if all_ok else "HÁ FALHAS!")

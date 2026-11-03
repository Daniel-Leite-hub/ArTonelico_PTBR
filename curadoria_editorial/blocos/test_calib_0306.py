import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0306 = {
    27506: 136, 27507: 184, 27508: 56, 27509: 112, 27510: 160, 27511: 184,
    27512: 216, 27513: 160, 27514: 88, 27515: 56, 27516: 128, 27517: 56,
    27518: 168, 27519: 208, 27520: 56, 27521: 72, 27522: 96, 27523: 56,
    27524: 112, 27525: 112, 27526: 112, 27527: 160, 27528: 168, 27529: 16
}

calib_0306 = {
    27506: ("Tem ideia do poder daquela bomba?CREla pode destruir o mundo todo!", "Shurelia alertando sobre o perigo catastrófico de 'Ar tonelico?' com CR. (133B <= 136B)"),
    27507: ("E fica carregando ela por aí!? Sendo um Cavaleiro de Elemia, tenha mais consciência!", "Shurelia exigindo responsabilidade profissional. (171B <= 184B)"),
    27508: ("S-Sim... Peço desculpas.", "Lyner acuado pedindo perdão. (50B <= 56B)"),
    27509: ("Portanto, vamos desmontarCRe descartar isso já.", "Shurelia ordenando o desmonte imediato com CR. (96B <= 112B)"),
    27510: ("M-Mas só de desmontar já é um perigo... É quase impossível... Hahaha!", "Lyner rindo de nervoso com a instabilidade do explosivo. (144B <= 160B)"),
    27511: ("Lyner... Desmonte isso no Altar dos Apóstolos. Vou selar as comportas até terminar.", "Shurelia propondo quarentena no Altar dos Apóstolos. (169B <= 184B)"),
    27512: ("Não faz isso...CRNão é melhor usar contra os inimigos?CRAssim não desperdiçamos material.", "Lyner defendendo a reciclagem bélica da bomba com CRs. (184B <= 216B)"),
    27513: ("Bem... é verdade, mas...CRHum... Parece que me convenceuCRna lábia...", "Shurelia admitindo que caiu na lábia dele com CRs. (141B <= 160B)"),
    27514: ("Lyner, você temCRa Água dos Sonhos, né?", "Shurelia interessada na Água dos Sonhos com CR. (82B <= 88B)"),
    27515: ("Hã? Sim, tenho. Por quê?", "Lyner confirmando a posse do frasco. (51B <= 56B)"),
    27516: ("Posso ficar com a garrafa?CRGostei muito do formato dela...", "Shurelia pedindo o frasco fofo com CR. (119B <= 128B)"),
    27517: ("Claro, pode pegar. Hum...", "Lyner concordando em entregar. (51B <= 56B)"),
    27518: ("Ah, achei! Aqui está.CRJogue fora o líquido dentro,CRpois é perigoso.", "Lyner avisando sobre o risco do conteúdo com CRs. (142B <= 168B)"),
    27519: ("A senhora também gosta de coisas fofas, né? No fundo, vejo que é uma garota comum.", "Lyner constatando o lado meigo e mortal de Shurelia. (168B <= 208B)"),
    27520: ("Não quero mais.", "Shurelia ofendida devolvendo na hora. (32B <= 56B)"),
    27521: ("Hã? Eu falei algo errado?", "Lyner sem entender a reação súbita. (52B <= 72B)"),
    27522: ("Não é isso. É que você...CRfalou bobagem...", "Shurelia envergonhada acusando Lyner de falar besteira com CR. (91B <= 96B)"),
    27523: ("Pensando bem... eu quero.", "Shurelia voltando atrás no mesmo instante. (51B <= 56B)"),
    27524: ("Diga... Você ainda temCRa Água dos Sonhos aí?", "Shurelia puxando assunto de novo sobre o frasco com CR. (94B <= 112B)"),
    27525: ("Será que posso...CRficar com aquela garrafa...?", "Shurelia pedindo com timidez extrema e CR. (96B <= 112B)"),
    27526: ("O quê!? Achei que tinhaCRdito que não queria...", "Lyner surpreso com a reviravolta com CR. (97B <= 112B)"),
    27527: ("Você falou aquilo...CRaí fiquei teimosa... e...", "Shurelia admitindo a teimosia infantil com CR. (97B <= 160B)"),
    27528: ("Aquilo de dizer que no fundoCRa senhora é uma garota comum?", "Lyner desvendando o motivo do bico com CR. (120B <= 168B)"),
    27529: ("...É.", "Shurelia concordando envergonhada com monossílabo fofo. (12B <= 16B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0306.items():
        maxb = max_map_0306[tid]
        sz = encoded_size(txt)
        diff = sz - maxb
        if diff > 0:
            all_ok = False
            print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
        else:
            errs = validate_line(tid, "", txt)
            if errs:
                all_ok = False
                print(f"ERRO VALIDACAO ID {tid}: {errs} -> {txt}")
            else:
                print(f"OK ID {tid}: {sz}B <= {maxb}B")
    if all_ok:
        print("=== 0306 100% PERFEITO ===")

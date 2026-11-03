import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0303 = {
    27434: 184, 27435: 128, 27436: 232, 27437: 64, 27438: 208, 27439: 64,
    27440: 40, 27441: 32, 27442: 24, 27443: 168, 27444: 128, 27445: 184,
    27446: 48, 27447: 32, 27448: 120, 27449: 120, 27450: 40, 27451: 104,
    27452: 80, 27453: 112, 27454: 32, 27455: 104, 27456: 56, 27457: 56
}

calib_0303 = {
    27434: ("Lyner... Quando me perdi outro dia... por que me deixou para trás?", "Shurelia cobrando satisfações por ter sido deixada para trás. (134B <= 184B)"),
    27435: ("Hã? Mas foi a senhora que sumiuCRsem ninguém perceber...", "Lyner explicando que ela se dispersou sozinha com CR. (115B <= 128B)"),
    27436: ("A culpa é minha!? Você é o líder do grupo, tem que prestar atenção em todos os membros!", "Shurelia transferindo a responsabilidade de liderança para Lyner. (179B <= 232B)"),
    27437: ("Eu tentei, mas...", "Lyner sem conseguir se defender. (35B <= 64B)"),
    27438: ("Se coloque no meu lugar, sendoCRprocurada em público. Que vergonha...", "Shurelia desabafando sobre o mico público com CR. (140B <= 208B)"),
    27439: ("...Desculpe, foi descuido meu.", "Lyner assumindo a falha com lealdade. (61B <= 64B)"),
    27440: ("Lady Shurelia...", "Lyner chamando a atenção dela respeitosamente. (33B <= 40B)"),
    27441: ("Você me odeia?", "Lyner perguntando com sincera insegurança. (30B <= 32B)"),
    27442: ("...Hã!?", "Shurelia surpresa com a pergunta direta. (16B <= 24B)"),
    27443: ("É que no Beco Vagalume a senhora falava com tanta calma com a Aurica...", "Lyner contrastando o carinho dela com Aurica no Beco Vagalume. (144B <= 168B)"),
    27444: ("Mas a sós comigo, do nadaCRfica brava por isso...", "Lyner apontando a rigidez exclusiva contra ele com CR. (100B <= 128B)"),
    27445: ("Acha minhas atitudes ruins, mas só guarda pra si na frente de todos?", "Lyner perguntando se é um peso reprimido em público. (138B <= 184B)"),
    27446: ("...Não, não é isso...", "Shurelia desmentindo com voz mansa. (46B <= 48B)"),
    27447: ("...Me perdoe.", "Shurelia se desculpando com nobreza sentida. (27B <= 32B)"),
    27448: ("N-Não, a senhora não precisaCRse desculpar...", "Lyner desconcertado com o pedido de desculpas com CR (expurga erro do EN). (93B <= 120B)"),
    27449: ("Com você... por que seráCRque acabo falando assim?", "Shurelia intrigada com a intimidade involuntária com CR. (103B <= 120B)"),
    27450: ("Mas você...", "Shurelia preparando o elogio sincero. (24B <= 40B)"),
    27451: ("Eu te acho exemplar, Lyner...CRe confio em você.", "Shurelia confessando sua alta estima e confiança com CR. (98B <= 104B)"),
    27452: ("Não pegou uma roupa bem cômica?", "Shurelia indagando sobre o traje bizarro. (65B <= 80B)"),
    27453: ("Hã? É que eu tinha um motivoCRpra usar aquilo.", "Lyner justificando a utilidade do adereço com CR. (95B <= 112B)"),
    27454: ("...Vai vestir?", "Shurelia perguntando na expectativa tímida. (29B <= 32B)"),
    27455: ("Que nada. Não tenho coragemCRde vestir algo assim.", "Lyner recusando por vergonha alheia com CR. (102B <= 104B)"),
    27456: ("...É mesmo? Que bom...", "Shurelia aliviada por ele não vestir. (46B <= 56B)"),
    27457: ("A senhora quer vestir?", "Lyner invertendo o jogo e perguntando se ela quer. (45B <= 56B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0303.items():
        maxb = max_map_0303[tid]
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
        print("=== 0303 100% PERFEITO ===")

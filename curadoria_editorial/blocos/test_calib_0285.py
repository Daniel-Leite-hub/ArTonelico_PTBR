import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0285 = {
    27002: 72, 27003: 144, 27004: 160, 27005: 168, 27006: 136, 27007: 96,
    27008: 176, 27009: 40, 27010: 152, 27011: 144, 27012: 136, 27013: 136,
    27014: 104, 27015: 80, 27016: 128, 27017: 200, 27018: 128, 27019: 120,
    27020: 24, 27021: 152, 27022: 136, 27023: 152, 27024: 176, 27025: 144
}

calib_0285 = {
    27002: ("Sendo franca...CRcansei disso tudo.", "Misha expressando cansaço visceral de imposições com CR. (71B <= 72B)"),
    27003: ("Nunca passei por isso, mas imaginoCRo quanto deve ter doídoCRem você.", "Lyner demonstrando empatia diante do sofrimento de Misha com CRs. (141B <= 144B)"),
    27004: ("Bem, quase ninguém passa por isso.CRO raro e cruel é passar.", "Misha refletindo sobre a crueldade da sina de Reyvateil com CR. (123B <= 160B)"),
    27005: ("Acho que por viver tão amarrada,CReu vivia implorando por liberdade.", "Misha explicando a origem de sua obsessão por liberdade com CR. (138B <= 168B)"),
    27006: ("Queria poder pra ser livre,CRentão precisava crescer e ser forte.", "Misha associando crescimento e poder à libertação com CR. (132B <= 136B)"),
    27007: ("...Se você me ajudasse,CRvaleria por cem...", "Misha insinuando o imenso valor do apoio de Lyner com CR. (88B <= 96B)"),
    27008: ("Mudei tanto desde a épocaCRda Crônica Crescente...CRAté eu fico surpresa.", "Misha notando sua maturidade desde a Crônica Crescente com CRs. (150B <= 176B)"),
    27009: ("É? Por exemplo?", "Lyner perguntando curioso por exemplos práticos. (32B <= 40B)"),
    27010: ("É. Naquela época, como já falei,CRminha liberdade vinha em primeiro lugar.", "Misha recapitulando seu egoísmo anterior com CR. (152B <= 152B)"),
    27011: ("Minha liberdade era tudo; o restoCRnão fazia a menor diferença.", "Misha enfatizando sua antiga mentalidade individualista com CR. (129B <= 144B)"),
    27012: ("Pra falar a verdade, fui assimCRaté bem pouco tempo atrás...", "Misha confessando a recente superação dessa postura com CR. (123B <= 136B)"),
    27013: ("Agora penso em tanta coisa nova...CRQue até eu me espanto.", "Misha maravilhada com a expansão de seus horizontes afetivos com CR. (118B <= 136B)"),
    27014: ("Você já viu quase todaCRa minha Cosmosfera, né?", "Misha constatando o avanço dos Mergulhos com termo canônico e CR. (98B <= 104B)"),
    27015: ("Hã? É, bem... já vi sim...", "Lyner sem jeito ao admitir a exploração mental profunda. (56B <= 80B)"),
    27016: ("Sabia... Não que eu queiraCRreclamar disso nem nada.", "Misha esclarecendo que não reprova as explorações íntimas com CR. (106B <= 128B)"),
    27017: ("É que, se for assim, você não vaiCRprecisar mais mergulhar em mim...CRE isso me deixa meio triste.", "Misha confessando a carência e o medo do fim da intimidade com CRs. (200B <= 200B)"),
    27018: ("Ficaria feliz se você aindaCRmergulhasse em mim às vezes...", "Misha pedindo carinhosamente novos Mergulhos com CR. (121B <= 128B)"),
    27019: ("Você anda falando muitoCRcom Shurelia ultimamente, né?", "Misha expressando ciúme dengoso com CR. (111B <= 120B)"),
    27020: ("É, pois é.", "Lyner respondendo de forma lacônica e descontraída. (23B <= 24B)"),
    27021: ("Hum... Achei que ShureliaCRnão fosse muito de conversar...", "Misha comentando sobre o temperamento reservado de Shurelia com CR. (118B <= 152B)"),
    27022: ("Mas é uma boa chance. Ela deve gostarCRde conversar com você.", "Misha reconhecendo o valor da aproximação com CR. (125B <= 136B)"),
    27023: ("Sinto que vocês dois andam íntimosCRaté demais ultimamente...", "Misha provocando com ciúme perceptível com CR. (126B <= 152B)"),
    27024: ("De fora parece muito isso...CRQuer dizer, é a única coisa que parece!", "Misha reforçando sua impressão sobre a proximidade dos dois com CR. (141B <= 176B)"),
    27025: ("Shurelia é meio ingênua comCRo mundo, então fico preocupada...", "Misha demonstrando apreensão com a ingenuidade de Shurelia com CR. (128B <= 144B)")
}

all_ok = True
for tid, (txt, rat) in calib_0285.items():
    maxb = max_map_0285[tid]
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
    print("=== 0285 100% PERFEITO ===")

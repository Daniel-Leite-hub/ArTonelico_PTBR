import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0290 = {
    27122: 184, 27123: 96, 27124: 104, 27125: 104, 27126: 96, 27127: 160,
    27128: 80, 27129: 168, 27130: 192, 27131: 96, 27132: 216, 27133: 160,
    27134: 128, 27135: 80, 27136: 32, 27137: 88, 27138: 24, 27139: 144,
    27140: 112, 27141: 128, 27142: 176, 27143: 168, 27144: 136, 27145: 104
}

calib_0290 = {
    27122: ("É que... ultimamente ando mergulhandoCRbem fundo, aí quis ver se você tava bem...", "Lyner demonstrando cuidado com os efeitos dos Mergulhos com CR. (166B <= 184B)"),
    27123: ("Ah... você tava preocupado comigo?CRQue fofo...", "Misha comovida com a preocupação carinhosa de Lyner com CR. (96B <= 96B)"),
    27124: ("Claro que tava. Ei...CRsua mão tá na minha...", "Lyner notando o contato físico sutil com CR. (93B <= 104B)"),
    27125: ("Não tô tocando, tô segurando.CRFiquei contente...", "Misha entrelaçando as mãos com doçura e afeto com CR. (102B <= 104B)"),
    27126: ("Eu tô ótima!CRMe preocupo é com você.", "Misha retribuindo o zelo protetor com CR. (79B <= 96B)"),
    27127: ("Dizem que quanto mais fundo você vaiCRna Cosmosfera, mais perigoso fica...", "Misha alertando sobre os perigos da Cosmosfera profunda com CR. (150B <= 160B)"),
    27128: ("Bem... não dá pra negar isso...", "Lyner admitindo a gravidade do perigo psíquico. (65B <= 80B)"),
    27129: ("Tenho medo de você mergulharCRe não acordar mais... Odeio sóCRde pensar nisso...", "Misha desabafando seu pavor de perder Lyner no abismo mental com CRs. (164B <= 168B)"),
    27130: ("Mas mesmo com esse medo,CRainda fico feliz demais quando vocêCRmergulha em mim...", "Misha expressando a ambivalência doce entre medo e intimidade com CRs. (164B <= 192B)"),
    27131: ("E além disso... er...CRLyner, tá me ouvindo?", "Misha percebendo a distração de Lyner com CR. (91B <= 96B)"),
    27132: ("Hã? Eu até tento ouvir...CRmas com você segurando a minha mão desse jeito, não consigo relaxar...", "Lyner sem conseguir manter o foco com o toque das mãos com CR. (200B <= 216B)"),
    27133: ("Fico tão nervoso que suas palavrasCRentram por um ouvido e saem pelo outro...", "Lyner admitindo a sobrecarga sensorial do toque com CR. (156B <= 160B)"),
    27134: ("D-Desculpa... Mas sinto queCRnão posso te soltar...", "Misha relutante em desfazer o entrelaçamento de mãos com CR. (104B <= 128B)"),
    27135: ("Se eu soltar, não vaiCRembora, né?", "Misha pedindo garantia de permanência com CR. (71B <= 80B)"),
    27136: ("Claro que não.", "Lyner tranquilizando Misha com firmeza carinhosa. (30B <= 32B)"),
    27137: ("Ah... queria tanto verCRa sua Cosmosfera...", "Misha manifestando curiosidade pela mente de Lyner com termo canônico e CR. (87B <= 88B)"),
    27138: ("A minha?!", "Lyner reagindo espantado à ideia. (19B <= 24B)"),
    27139: ("Fico curiosa pra saber o que senteCRao mergulhar na minha mente.", "Misha indagando sobre as sensações do Mergulho com CR. (129B <= 144B)"),
    27140: ("Só poder mergulhar em ReyvateilsCRé tão injusto...", "Misha questionando a via de mão única com termo canônico e CR. (104B <= 112B)"),
    27141: ("Bem, se desse pra você mergulharCRem mim, eu até deixaria...", "Lyner expressando generosidade e vulnerabilidade mútua com CR. (123B <= 128B)"),
    27142: ("Parece fácil, mas exige coragem!CRSem brincadeira, dá uma vergonhaCRde morrer!", "Misha descrevendo a entrega psíquica desnudada na Cosmosfera com CRs. (159B <= 176B)"),
    27143: ("Mas fico sem graça de só eu ver tudo.CRSe eu pudesse, deixaria você ver.", "Lyner compartilhando o sentimento de reciprocidade com CR. (148B <= 168B)"),
    27144: ("Talvez eu só fale isso por saberCRque é impossível, né...", "Lyner reconhecendo com humor autodepreciativo a impossibilidade com CR. (119B <= 136B)"),
    27145: ("...Só de você falar isso,CRjá fico bem feliz.", "Misha acolhendo a intenção com doçura e gratidão sincera com CR. (94B <= 104B)")
}

all_ok = True
for tid, (txt, rat) in calib_0290.items():
    maxb = max_map_0290[tid]
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
    print("=== 0290 100% PERFEITO ===")

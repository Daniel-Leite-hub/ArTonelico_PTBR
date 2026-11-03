import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0295 = {
    27242: 72, 27243: 216, 27244: 40, 27245: 56, 27246: 80, 27247: 152,
    27248: 184, 27249: 216, 27250: 112, 27251: 96, 27252: 40, 27253: 160,
    27254: 128, 27255: 184, 27256: 216, 27257: 32, 27258: 112, 27259: 160,
    27260: 32, 27261: 72, 27262: 128, 27263: 40, 27264: 96, 27265: 16
}

calib_0295 = {
    27242: ("Mas é só o que me vem à cabeça...", "Lyner sem jeito após o diálogo do Shampoo Hat. (38B <= 72B)"),
    27243: ("Se tem tempo pra criar coisas sem pé nem cabeça, use-o para sintetizar itens mais nobres e úteis.", "Shurelia repreendendo Lyner com sua seriedade aristocrática. (104B <= 216B)"),
    27244: ("O tempo é limitado.", "Shurelia lembrando a urgência de sua missão divina. (40B <= 40B)"),
    27245: ("S-Sim... Peço desculpas.", "Lyner acatando a bronca respeitosamente. (50B <= 56B)"),
    27246: ("Vou tentar o Grathmeld sozinha.", "Shurelia decidindo praticar síntese por conta própria. (63B <= 80B)"),
    27247: ("A senhora?CRVai criar algo bem mais incrívelCRque eu, com facilidade.", "Lyner admirado com a capacidade de Lady Shurelia com CRs. (140B <= 152B)"),
    27248: ("Mas é a primeira vez que vou criar algo...CRNão sei se vai dar certo.", "Shurelia revelando sua insegurança inicial com CR. (141B <= 184B)"),
    27249: ("Mas, como criadora do Grathmeld, quero sentir sua utilidade na prática... Por isso vou tentar.", "Shurelia explicando sua motivação científica. (190B <= 216B)"),
    27250: ("É mesmo?CRSe quiser, posso dar uma força.", "Lyner oferecendo ajuda com presteza e CR. (85B <= 112B)"),
    27251: ("...Não, tudo bem.CREu me viro sozinha.", "Shurelia recusando formalmente com altivez e CR. (78B <= 96B)"),
    27252: ("A-Ah, entendi...", "Lyner desconcertado pela recusa. (33B <= 40B)"),
    27253: ("Diga, Lyner...CRLembra de termos falado do Grathmeld?CRQuero que me ensine.", "Shurelia voltando atrás timidamente com CRs. (151B <= 160B)"),
    27254: ("Hã!? Mas daquela vez a senhoraCRdisse que faria sozinha...", "Lyner surpreso, expurgando o erro americano grotesco ('filthy help') com CR. (118B <= 128B)"),
    27255: ("Fui teimosa naquela época...CRMas queria que me ensinasse.CRNão pode ser...?", "Shurelia abrindo o coração com vulnerabilidade doce e CRs. (155B <= 184B)"),
    27256: ("Hã? De jeito nenhum! Por mim tudo bem, mas... tem certeza de que quer aprender com alguém como eu?", "Lyner solícito e humilde diante da mestra. (199B <= 216B)"),
    27257: ("Sim, por favor.", "Shurelia pedindo com candura nobre. (31B <= 32B)"),
    27258: ("Vamos começar pelo básico,CRo [Pó de Polimento].", "Lyner apresentando a síntese básica com colchetes preservados e CR. (100B <= 112B)"),
    27259: ("É fácil. É só moer esta pedra até virar pó. É num instante.", "Lyner explicando a técnica do Grathmeld. (126B <= 160B)"),
    27260: ("Hmm... É assim?", "Shurelia tentando moer pela primeira vez. (32B <= 32B)"),
    27261: ("Isso, continue moendo assim.", "Lyner encorajando Shurelia com naturalidade. (57B <= 72B)"),
    27262: ("Entendi. Logo vou conseguirCRfazer tudo sozinha de novo.", "Shurelia confiante com CR. (57B <= 128B)"),
    27263: ("...Assim tá bom?", "Shurelia checando o resultado com doçura. (18B <= 40B)"),
    27264: ("Ficou ótimo! Virou um pó bem fininho e...", "Lyner elogiando o pó fino da pedra. (43B <= 96B)"),
    27265: ("Atchim!", "Shurelia espirrando ao inalar o pó. (8B <= 16B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0295.items():
        maxb = max_map_0295[tid]
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
        print("=== 0295 100% PERFEITO ===")

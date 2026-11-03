import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0301 = {
    27386: 64, 27387: 48, 27388: 120, 27389: 72, 27390: 112, 27391: 112,
    27392: 88, 27393: 160, 27394: 112, 27395: 152, 27396: 96, 27397: 40,
    27398: 264, 27399: 288, 27400: 144, 27401: 136, 27402: 208, 27403: 96,
    27404: 216, 27405: 152, 27406: 80, 27407: 152, 27408: 64, 27409: 224
}

calib_0301 = {
    27386: ("Lady Shurelia?CRO que foi?", "Lyner percebendo a seriedade súbita de Shurelia com CR. (53B <= 64B)"),
    27387: ("...Eu também vou fazer.", "Shurelia decidida a cozinhar para Lyner. (48B <= 48B)"),
    27388: ("Vou cozinhar pra você, Lyner.CRAlgo bem saboroso...", "Shurelia prometendo uma refeição especial com CR. (104B <= 120B)"),
    27389: ("O quê!? Mas a senhoraCRcozinha!?", "Lyner surpreso com as habilidades domésticas dela com CR. (66B <= 72B)"),
    27390: ("Lembra do que cozinheiCRno Mergulho? Fica calmo.", "Shurelia referenciando o Mergulho na Cosmosfera com CR. (97B <= 112B)"),
    27391: ("E só vou usar coisas boas,CRentão não se preocupe.", "Shurelia tranquilizando Lyner com CR. (104B <= 112B)"),
    27392: ("(...Por que ninguém segue receita?)", "Lyner perplexo com o desprezo das heroínas pelas receitas. (72B <= 88B)"),
    27393: ("Andar por Platina com este visualCRme deixa um pouco inquieta.", "Shurelia expondo a estranheza sem a armadura com CR. (125B <= 160B)"),
    27394: ("Sempre usava aquela armadura,CRentão é meio estranho.", "Shurelia justificando o hábito com CR. (109B <= 112B)"),
    27395: ("Precisa se acostumar. Usar aquiloCRo tempo todo devia cansar.", "Lyner aconselhando com carinho e CR. (123B <= 152B)"),
    27396: ("Não cansa. Aquele trajeCRflutua sozinho.", "Shurelia esclarecendo a tecnologia do traje com CR. (82B <= 96B)"),
    27397: ("É só que...", "Shurelia hesitando antes do desabafo. (25B <= 40B)"),
    27398: ("Fazia tanto tempo que eu não sentia o mundo com meus olhos, ouvidos e pele... Por isso queria viajar por ele assim.", "Shurelia expressando o anseio poético de sentir o mundo real. (232B <= 264B)"),
    27399: ("Que ventos sopram aqui, como são as paisagens... e que gente vive aqui... Quero sentir tudo na própria pele...", "Shurelia contemplando o mundo vivo fora de sua prisão milenar. (223B <= 288B)"),
    27400: ("...Fique calma. Ninguém táCRolhando torto pra senhora.", "Lyner confortando a deusa com gentileza e CR. (111B <= 144B)"),
    27401: ("Para os outros, parece só uma garota comum e bem fofa.", "Lyner elogiando a aparência doce de Shurelia. (110B <= 136B)"),
    27402: ("...L-Lyner! Mesmo parecendo assim, ainda sou sua comandante! Me chamar de garota...", "Shurelia envergonhada e autoritária em protesto. (167B <= 208B)"),
    27403: ("Perdão! Foi descuidoCRda minha parte...", "Lyner pedindo desculpas rápido com CR. (80B <= 96B)"),
    27404: ("N-Não, tudo bem... Só tenha cuidado. Quando fala isso do nada, meu coração dispara...", "Shurelia confessando o descompasso cardíaco (restaura JP soberano). (173B <= 216B)"),
    27405: ("Diga, Lyner... Você estava comendoCRraspadinha outro dia, né?", "Shurelia mudando de assunto com CR. (125B <= 152B)"),
    27406: ("Sim. A senhora gostaCRde raspadinha?", "Lyner perguntando sobre a preferência dela com CR. (73B <= 80B)"),
    27407: ("...Gosto. Mas não fiquei contenteCRcom a que comeu outro dia.", "Shurelia manifestando descontentamento com CR. (124B <= 152B)"),
    27408: ("Ué? O que tinha de errado...?", "Lyner curioso com a exigência. (60B <= 64B)"),
    27409: ("Era só gelo puro sem nada por cima!CRNão é raspadinha. O povo de HorusCRestá te enganando.", "Shurelia indignada com o gelo sem calda com CRs. (185B <= 224B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0301.items():
        maxb = max_map_0301[tid]
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
        print("=== 0301 100% PERFEITO ===")

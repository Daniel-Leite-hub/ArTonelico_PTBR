import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0265 = {
    26522: ("Comeria Funbun nas três refeições!", "Lyner declarando seu amor incondicional pelo doce."),
    26523: ("...Eu dispenso.", "Misha rejeitando secamente o doce tradicional."),
    26524: ("O quê?!CRUm doce tão gostoso daqueles?!", "Lyner indignado com o desprezo de Misha pelo Funbun."),
    26525: ("Em Platina, um certo alguémCRme fazia comer aquilo todo dia!", "Misha revelando o trauma gastronômico da infância."),
    26526: ("Quê?!CRMisha, que vidão!", "Lyner invejando ingenuamente a fartura da infância de Misha."),
    26527: ("Do que você tá falando?CRFoi você que me obrigava a comer!", "Misha apontando Lyner como o culpado pela overdose de doce."),
    26528: ("Hã? ...Eu?", "Lyner em choque com a revelação do passado."),
    26529: ("Sim! Quando eu dizia que enjoei,CRvocê ameaçava não brincar comigoCRse eu não comesse tudo!", "Misha relembrando as chantagens infantis de Lyner."),
    26530: ("Me obrigava a comer FunbunCRsem eu querer...", "Misha detalhando a implicância comovente de infância."),
    26531: ("Fiz isso?", "Lyner sem memória e sem graça com a gafe passada."),
    26532: ("Por isso peguei birra de Funbun.CREntendeu agora, culpado?", "Misha cobrando a conta do trauma gastronômico."),
    26533: ("Foi mal...", "Lyner pedindo desculpas constrangido."),
    26534: ("Campos em Terraço são um inferno.CRSó de subir já fico morta.", "Misha reclamando da exaustão física da subida."),
    26535: ("Sério? Pra mim foi bem tranquilo.", "Lyner ostentando seu preparo físico atlético."),
    26536: ("A culpa é minha, eu sei.CRSempre vivi no Beco Vagalume,CRdeve ser por isso.", "Misha reconhecendo seu sedentarismo no beco comercial."),
    26537: ("Eu usava mais a cabeça que o corpo.CRAi, ai... devia ter treinadoCRum pouco os músculos.", "Misha lamentando a falta de condicionamento físico."),
    26538: ("Pelo menos você aprendeu a abrir trancasCRe fez contatos suspeitos, não é?", "Lyner destacando ironicamente as habilidades malandras de Misha."),
    26539: ("...Falando assim parece algo ruim.", "Misha desconfiada da ironia de Lyner."),
    26540: ("Lyner, na minha Cosmosfera...CRfoi tudo bem?", "Misha perguntando insegura sobre a experiência de Lyner em seu mundo mental."),
    26541: ("Hã? Foi tranquilo.", "Lyner tranquilizando Misha espontaneamente."),
    26542: ("É? Que bom...CRNão teve nada de estranho?", "Misha sondando se algo bizarro foi revelado."),
    26543: ("Estranho, bem... Como não éCRo mundo real, até que é normal...", "Lyner tentando justificar as loucuras metafóricas da mente."),
    26544: ("Tava estranho?!CRNão viu nada demais, né?!", "Misha entrando em pânico ao desconfiar do pior."),
    26545: ("Ruim não, mas...CRnão sei se posso falar.", "Lyner ficando sem jeito de admitir o que presenciou."),
}

max_map = {
    26522: 72, 26523: 64, 26524: 112, 26525: 136, 26526: 64, 26527: 136,
    26528: 24, 26529: 200, 26530: 96, 26531: 24, 26532: 128, 26533: 24,
    26534: 136, 26535: 88, 26536: 176, 26537: 184, 26538: 160, 26539: 80,
    26540: 96, 26541: 48, 26542: 96, 26543: 144, 26544: 88, 26545: 104
}

all_ok = True
for tid, (txt, rat) in calib_0265.items():
    maxb = max_map[tid]
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
    print("=== 0265 100% PERFEITO ===")

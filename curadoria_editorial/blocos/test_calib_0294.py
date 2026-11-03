import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0294 = {
    27218: 64, 27219: 104, 27220: 64, 27221: 144, 27222: 128, 27223: 128,
    27224: 152, 27225: 160, 27226: 72, 27227: 208, 27228: 112, 27229: 112,
    27230: 48, 27231: 88, 27232: 128, 27233: 160, 27234: 104, 27235: 128,
    27236: 56, 27237: 16, 27238: 104, 27239: 56, 27240: 112, 27241: 64
}

calib_0294 = {
    27218: ("Dez anos longeCRnão contam...", "Lyner justificando o lapso temporal de infância com CR. (60B <= 64B)"),
    27219: ("...Lyner. Não se entediaCRde conversar comigo?", "Shurelia revelando insegurança modesta no diálogo com CR. (94B <= 104B)"),
    27220: ("Hã? De onde tirouCRessa ideia?", "Lyner reagindo surpreso e respeitoso com CR. (62B <= 64B)"),
    27221: ("É que... eu não sei puxar paposCRdivertidos como a Aurica e a Misha.", "Shurelia comparando-se com as outras Reyvateils com CR. (139B <= 144B)"),
    27222: ("Gosto que venha me ver,CRmas temia que se entediasse...", "Shurelia temendo aborrecer Lyner com CR. (111B <= 128B)"),
    27223: ("Que nada! Pra ser franco,CRacho bem revigorante e divertido.", "Lyner elogiando a companhia de Shurelia com CR. (121B <= 128B)"),
    27224: ("Nunca tive a chance de falarCRa sós com a senhora antes, né?", "Lyner apreciando a intimidade inédita a sós com CR. (123B <= 152B)"),
    27225: ("Conversar e conhecer a senhoraCRpouco a pouco tá sendoCRmuito legal pra mim.", "Lyner expressando afeto e respeito sinceros com CRs. (154B <= 160B)"),
    27226: ("D-Desculpe... Falei demais?", "Lyner encabulado com sua efusividade. (55B <= 72B)"),
    27227: ("Não, de jeito nenhum... É queCRnunca me disseram algo assim,CRentão levei um sustinho...", "Shurelia tocada por ser valorizada como pessoa comum com CRs. (180B <= 208B)"),
    27228: ("...Mas não me incomodou nem nada,CRde verdade.", "Shurelia tranquilizando Lyner com ternura e CR. (94B <= 112B)"),
    27229: ("Além disso... eu também gostoCRde conversar com você.", "Shurelia confessando seu apreço pelos encontros noturnos com CR. (110B <= 112B)"),
    27230: ("É? Que alívio, então.", "Lyner respirando aliviado com naturalidade. (46B <= 48B)"),
    27231: ("Lyner, por que criou aqueleCRShampoo Hat?", "Shurelia indagando sobre o acessório bizarro com termo canônico e CR. (83B <= 88B)"),
    27232: ("Hã?... É que... calhou de eu acharCRa carta de receita dele...", "Lyner sem jeito ao admitir a síntese impulsiva com CR. (127B <= 128B)"),
    27233: ("Mas isso é pra banho, não é?CRPor acaso teremos combatesCRna banheira?", "Shurelia questionando com lógica cândida o uso militar do adorno com CRs. (144B <= 160B)"),
    27234: ("Bem, no uso normal...CRrealmente não faz sentido.", "Lyner concordando sobre a incongruência no cotidiano com CR. (100B <= 104B)"),
    27235: ("Mas esse Shampoo Hat tem efeitoCRespecial se usado em combate!", "Lyner revelando a utilidade tática com termo canônico e CR. (125B <= 128B)"),
    27236: ("O inimigo entra em pânico.", "Lyner propondo o primeiro palpite cômico sobre o item. (54B <= 56B)"),
    27237: ("...Não.", "Shurelia negando secamente a primeira hipótese. (16B <= 16B)"),
    27238: ("O inimigo ri tanto que desmaiaCRem pleno combate.", "Lyner arriscando o segundo palpite cômico com CR. (99B <= 104B)"),
    27239: ("...Tá errado!", "Shurelia refutando o segundo palpite com energia. (28B <= 56B)"),
    27240: ("Os aliados sofrem pra segurarCRo riso na batalha.", "Lyner sugerindo a derradeira hipótese cômica com CR. (99B <= 112B)"),
    27241: ("Não é nada disso!", "Shurelia encerrando a discussão com timing cômico perfeito. (37B <= 64B)")
}

all_ok = True
for tid, (txt, rat) in calib_0294.items():
    maxb = max_map_0294[tid]
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
    print("=== 0294 100% PERFEITO ===")

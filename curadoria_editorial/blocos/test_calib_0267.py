import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0267 = {
    26570: ("É prático, mas...CRé só por isso mesmo?", "Lyner desconfiando da motivação real por trás do aprendizado de arrombamento."),
    26571: ('Como assim, "só por isso"?', "Misha se fazendo de desentendida diante do questionamento."),
    26572: ("Achei que tava pensandoCRem virar ladra ou coisa assim...", "Lyner brincando sobre a utilidade criminosa da habilidade."),
    26573: ("...Falou alguma coisa?", "Misha fingindo ameaça com olhar fulminante."),
    26574: ("N-nada! É que você sabe tudo,CRdá pra contar com você pra tudo!", "Lyner se corrigindo às pressas para não levar bronca."),
    26575: ("Como conheceu a Spica?", "Lyner perguntando sobre a origem da amizade com a misteriosa comerciante Spica."),
    26576: ("A Spica?CRPor que quer saber?", "Misha curiosa sobre o interesse repentino de Lyner."),
    26577: ("Não é normal conhecer alguém que vendeCRitens e dados perigosos sob código secreto!", "Lyner apontando a natureza clandestina do comércio de Spica."),
    26578: ("Acho maneiro.CRFiquei curioso pra saber.", "Lyner admitindo que acha o estilo de Spica interessante."),
    26579: ("Não teve nada de incrívelCRna história.", "Misha minimizando o encontro casual."),
    26580: ("Fui comprar Bala de GatoCRe soltei aquelas palavras por acaso.", "Misha revelando a compra prosaica do doce felino."),
    26581: ("Aquilo...?", "Lyner espantado com a senha improvável."),
    26582: ('Disse: "Não ligo pro preço,CRsó quero comer um balde cheio!"', "A cômica senha de acesso ao mercado negro de Spica."),
    26583: ("Aí surgiram Cristais Grathnode incríveisCRdo nada. Foi assim que nos conhecemos.", "Misha narrando o desfecho absurdo do primeiro contato."),
    26584: ("Sério?! Acertar a senha por acaso...CRIsso é impressionante demais!", "Lyner acreditando boquiaberto na história."),
    26585: ("Brincadeirinha!", "Misha rindo da ingenuidade de Lyner."),
    26586: ("Quê?! Qual é, me dá um tempo...", "Lyner frustrado por cair na pegadinha."),
    26587: ("A verdade eu não posso contar.CRMas foi uma história cheia de drama,CRe eu até sei a cor natural do cabelo dela!", "Misha atiçando o mistério sobre o cabelo real de Spica."),
    26588: ("Falando assim,CRdá mais vontade de saber ainda...", "Lyner mordendo a isca da curiosidade."),
    26589: ("Ficou curioso? Mas não conto.CRFoi um encontro bem delicado...", "Misha mantendo o segredo trancado a sete chaves."),
    26590: ("Tá bom, chega, não fala mais nada!CRSenão fico curioso e não durmo!", "Lyner tapando os ouvidos para conseguir dormir."),
    26591: ("Pode ser tarde pra perguntar,CRmas fiz bem em mergulhar em você?", "Lyner abrindo o coração sobre a culpa de ter esquecido o passado."),
    26592: ("Você se lembrava de mim,CRmas eu não lembrava de nada...", "Lyner admitindo a dor de ter perdido as memórias de infância."),
    26593: ("Será que fez bem deixando alguém como euCRentrar na sua Cosmosfera...?", "Lyner questionando se era digno da intimidade da Cosmosfera."),
}

max_map = {
    26570: 96, 26571: 96, 26572: 144, 26573: 48, 26574: 136, 26575: 48,
    26576: 64, 26577: 208, 26578: 104, 26579: 88, 26580: 160, 26581: 24,
    26582: 152, 26583: 176, 26584: 144, 26585: 32, 26586: 72, 26587: 232,
    26588: 128, 26589: 144, 26590: 168, 26591: 160, 26592: 168, 26593: 160
}

all_ok = True
for tid, (txt, rat) in calib_0267.items():
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
    print("=== 0267 100% PERFEITO ===")

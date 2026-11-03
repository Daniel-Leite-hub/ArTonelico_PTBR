import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0300 = {
    27362: 72, 27363: 128, 27364: 168, 27365: 136, 27366: 104, 27367: 24,
    27368: 152, 27369: 136, 27370: 40, 27371: 184, 27372: 96, 27373: 176,
    27374: 48, 27375: 144, 27376: 184, 27377: 72, 27378: 184, 27379: 144,
    27380: 104, 27381: 200, 27382: 88, 27383: 160, 27384: 160, 27385: 192
}

calib_0300 = {
    27362: ("Q-Que lógica sem pé nem cabeça.", "Lyner embasbacado com o raciocínio dela. (66B <= 72B)"),
    27363: ("O dever do Cavaleiro de ElemiaCRnão é proteger a vida do povo?", "Shurelia cobrando o dever cavalheiresco com CR. (127B <= 128B)"),
    27364: ("S-Sim... Entendi.CRMas o que faço com a pelúciaCRdepois de comprar...?", "Lyner cedendo e perguntando o destino do brinquedo com CRs. (143B <= 168B)"),
    27365: ("Eu mesma recolho a pelúcia,CRentão não se preocupe.", "Shurelia prometendo confiscar o sapo com CR. (106B <= 136B)"),
    27366: ("...A senhora só queria elaCRpra você mesma...", "Lyner desmascarando o capricho da deusa com CR. (93B <= 104B)"),
    27367: ("N-Não é!", "Shurelia negando na defensiva. (19B <= 24B)"),
    27368: ("(Desde que falou informal,CRela ficou tão manhosa...)", "Lyner constatando o lado mimado e fofo de Shurelia com CR. (108B <= 152B)"),
    27369: ("Lyner. Fez algo na lojaCRda Travessa Hoshinose?", "Shurelia cobrando explicações sobre a vendedora com CR. (95B <= 136B)"),
    27370: ("...P-Por quê?", "Lyner gaguejando diante do interrogatório. (28B <= 40B)"),
    27371: ("A vendedora me lançou um olhar mortal.CRSerá impressão minha?", "Shurelia relatando a hostilidade da atendente com CR. (126B <= 184B)"),
    27372: ("Ah... Ela tem um históricoCRcomplicado...", "Lyner justificando o temperamento da moça com CR. (84B <= 96B)"),
    27373: ("A Aurica fez compras pro jantar lá,CRe soltou várias falasCRbem comprometedoras...", "Lyner relembrando as gafes da Aurica com CRs. (167B <= 176B)"),
    27374: ("Compras pro jantar?", "Shurelia repetindo com curiosidade e ponta de ciúme. (39B <= 48B)"),
    27375: ("A Aurica fez pra mim.CRFicou meio esquisito,CRmas tava uma delícia.", "Lyner elogiando a refeição caseira com CRs. (136B <= 144B)"),
    27376: ("Entendi... Ganhava comidinha da Aurica em plena missão, que divertido.", "Shurelia alfinetando a mordomia romântica (expurga erro do EN). (142B <= 184B)"),
    27377: ("Hã? Bem... Visto assim...", "Lyner sem saída diante da cobrança. (52B <= 72B)"),
    27378: ("Tanto faz. Eu fico sempre sozinha no Rinkernator, isso não tem a ver comigo.", "Shurelia amuada lembrando seu isolamento eterno. (154B <= 184B)"),
    27379: ("N-Não... Quer jantar comigoCRda próxima vez? Eu pago...", "Lyner tentando compensar com um convite a dois e CRs. (113B <= 144B)"),
    27380: ("...Não precisa.CRNão precisa ser por pena.", "Shurelia orgulhosa recusando caridade afetiva com CR. (87B <= 104B)"),
    27381: ("Sempre que passo na Travessa Hoshinose, lembro da comida da Aurica...", "Lyner puxando o assunto gastronômico nostálgico. (139B <= 200B)"),
    27382: ("É...? A Aurica cozinhaCRtão bem assim?", "Shurelia intrigada com a culinária da rival com CR. (79B <= 88B)"),
    27383: ("Fica boa, mas o preparoCRtem vários problemas...", "Lyner ressalvando as maluquices da receita com CR. (98B <= 160B)"),
    27384: ("Pra ela, cozinhar é só misturar qualquer coisa boa de qualquer jeito.", "Lyner explicando a teoria caótica da Aurica. (141B <= 160B)"),
    27385: ("Mas nunca fica intragável. De certa forma, ela é um gênio da cozinha.", "Lyner admirando a sorte culinária milagrosa de Aurica. (142B <= 192B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0300.items():
        maxb = max_map_0300[tid]
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
        print("=== 0300 100% PERFEITO ===")

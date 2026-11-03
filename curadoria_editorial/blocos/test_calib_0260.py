import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0260 = {
    26402: ("Lyner, você curtiu o LILIM?", "Aurica perguntando tímida sobre a vestimenta sensual LILIM."),
    26403: ("Hã?! D-do nada, o que cêCRtá falando?!", "Lyner reagindo surpreso à pergunta indiscreta sobre o traje."),
    26404: ("Você gosta tanto que viveCRme pondo pra lutar assim...", "Aurica notando a frequência de uso do traje LILIM em batalha."),
    26405: ("Mas... isso é tão vergonhoso.", "Aurica confessando o constrangimento de usar a roupa curta."),
    26406: ("U... foi mal...", "Lyner sem jeito se desculpando pela escolha do traje."),
    26407: ("...Mas se você gosta tanto,CRtudo bem.", "Aurica relevando a vergonha pelo carinho que tem por Lyner."),
    26408: ("Mas descobri uma coisa incrívelCRusando essa roupa.", "Aurica revelando sua inusitada constatação psicológica."),
    26409: ("Uma roupa tão reveladora dá muitoCRmais vergonha do que ficar pelada!", "A hilária constatação de Aurica sobre a semi-nudez do figurino."),
    26410: ("Né?! Não é incrível?!", "Aurica animada com a própria lógica inusitada."),
    26411: ("...Fico em dúvida se você táCRmesmo com vergonha.", "Lyner cético diante da animação contraditória de Aurica."),
    26412: ("Falando nisso, você tava meio estranhaCRno bar. Aconteceu alguma coisa?", "Lyner perguntando sobre o comportamento tenso de Misha na taverna."),
    26413: ("Hã? Ah, sim.CRSó tava um pouco em alerta.", "Misha explicando que estava vigiando o ambiente por cautela."),
    26414: ("Tem gente da TenbaCRque vive naquele bar.", "Misha revelando a presença de alguém perigoso da corporação Tenba."),
    26415: ("Bourd?", "Lyner indagando se a ameaça era o comandante Bourd."),
    26416: ("Não. Quem vive indo láCRé a presidente da Tenba.", "Misha revelando que a cliente frequente é a própria presidente da Tenba."),
    26417: ("A líder da Tenba?!CRPor que alguém assim iria num bar desses?!", "Lyner chocado ao saber que a presidente de Tenba frequenta um bar comum."),
    26418: ("Ela ama o Prato DokkoiCRque servem por lá.", "Misha explicando a obsessão gastronômica da presidente pelo Prato Dokkoi."),
    26419: ("E ela sempre pedeCRo tamanho grande!", "Misha descrevendo os hábitos peculiares da presidente de Tenba."),
    26420: ("Vive vagando atrás de diversão.CRQuando não aguenta de tédio, ela vai comer.", "Misha detalhando a personalidade imprevisível da líder corporativa."),
    26421: ("Ela é desse jeito.", "Misha concluindo o perfil excêntrico da presidente."),
    26422: ("...Ficou claro que prefiro evitar elaCRmais ainda que o Bourd.", "Lyner concluindo comicamente o receio de cruzar com a presidente."),
    26423: ("Misha, você gosta de ler livros, né?", "Lyner puxando assunto sobre o gosto de Misha por leitura."),
    26424: ("O armazém de Karulu tinha vários.CRQuer ir lá dar uma olhada depois?", "Lyner sugerindo um passeio tranquilo ao empório do Vilarejo Karulu."),
    26425: ("Ah, lá? Dei uma olhada,CRmas já li quase tudo o que tem lá.", "Misha demonstrando sua vasta bagagem de leitura prévia no vilarejo."),
}

max_map = {
    26402: 56, 26403: 96, 26404: 120, 26405: 64, 26406: 32, 26407: 104,
    26408: 112, 26409: 160, 26410: 48, 26411: 112, 26412: 152, 26413: 104,
    26414: 88, 26415: 16, 26416: 104, 26417: 152, 26418: 120, 26419: 80,
    26420: 168, 26421: 48, 26422: 136, 26423: 88, 26424: 144, 26425: 152
}

all_ok = True
for tid, (txt, rat) in calib_0260.items():
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
    print("=== 0260 100% PERFEITO ===")

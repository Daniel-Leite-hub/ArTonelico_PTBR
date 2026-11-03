"""Aplica as correções cirúrgicas de buffer em build_blk_sys_028.py
"""

import re
from pathlib import Path

BUILD_SCRIPT = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\build_blk_sys_028.py")

UPDATES = {
    28109: ('Shurelia?CRHouve algo? Está zangada?', 'rewritten', 'Pergunta respeitosa e afetuosa com CR e buffer ajustado (74B <= 80B).'),
    28111: ('...Demorou muitoCRa vir ao meu quarto!', 'rewritten', 'Reclamação dengosa de Shurelia com CR e buffer seguro (77B <= 80B).'),
    28115: ('É... tem razão.CRNem percebi... perdão.', 'rewritten', 'Reconhecimento sincero de Lyner com CR e buffer de 82B <= 88B.'),
    28117: ('Sou meio lerdo... Mesmo quando está cansada,CRquase nunca noto.CRDesculpe por ser tão insensível.', 'rewritten', 'Lyner se desculpando com humildade (198B <= 216B).'),
    28123: ('Não é que... eu esteja brava.CRSó que... nem sei bem o porquê...', 'rewritten', 'Hesitação tímida de Shurelia (133B <= 136B).'),
    28130: ('Eu... não te afastarei...', 'rewritten', 'Confissão terna de acolhimento irrestrito a Lyner (52B <= 56B).'),
    28134: ('Ah... entrando no climaCRda história, fica tudo ótimo!', 'rewritten', 'Lyner animando Shurelia sobre o mundo virtual (111B <= 112B).'),
    28135: ('E você parece tão diferente...CRÉ muito legal de ver!', 'rewritten', 'Lyner elogiando o lado inédito de Shurelia (110B <= 128B).'),
    28136: ('A-Aquilo foi tão embaraçoso!CRNem me lembre mais disso!', 'rewritten', 'Rubor de Shurelia com o bordão heroico (113B <= 120B).'),
    28138: ('N-Não é isso...CReu também me divirto muitoCRao seu lado...', 'rewritten', 'Shurelia confessando sua alegria a dois (122B <= 128B).'),
    28139: ('Que bom! Mas a senhoraCRno mundo mental é mesmo incrível!', 'rewritten', 'Lyner maravilhado com a Cosmosfera de Shurelia (117B <= 136B).'),
    28143: ('Aquilo foi legal, tudo bem!CRNão é disso que falo...', 'rewritten', 'Shurelia defendendo sua pose heroica (107B <= 112B).'),
    28146: ('A gente dá as mãos ao transformar,CRnão é? É que... fico com vergonha...', 'rewritten', 'A revelação do pudor de Shurelia ao segurar as mãos (150B <= 152B).'),
    28147: ('É... eu também ficoCRmeio sem graça...', 'rewritten', 'Lyner admitindo que também cora com o toque de mãos (80B <= 88B).'),
    28149: ('Aperto de mão é normal, mas...CRd-dar as mãos tem outro sentido.', 'rewritten', 'Diferenciação romântica do toque físico íntimo (132B <= 136B).'),
    28153: ('É verdade... A gente brincou muitoCRnaquele mundo virtual.', 'rewritten', 'Cumplicidade nostálgica dos momentos virtuais (118B <= 128B).'),
    28157: ('Sério?! Obrigado!CRMas me desculpe dar tanto trabalhoCRà senhora só por mim...', 'rewritten', 'Gratidão e consideração de Lyner (160B <= 176B).'),
    28159: ('E é a chance de ter você só pra mim...CRAinda me lembro de tudo depois!', 'rewritten', 'Shurelia valorizando a exclusividade e memória dos momentos juntos (146B <= 160B).'),
    28160: ('Só pra você?... No Mergulho,CRninguém mais consegue entrar mesmo.', 'rewritten', 'Constatação prática de Lyner sobre a Cosmosfera (134B <= 144B).'),
    28162: ('Estamos a sós, mas...CREspera, Shurelia? Não tá coladinhaCRdemais em mim?...', 'rewritten', 'Lyner surpreso com o aconchego físico íntimo de Shurelia (156B <= 168B).'),
    28163: ('...Mas eu nunca faria issoCRna frente dos outros...', 'rewritten', 'Pudor público versus intimidade a sós (103B <= 112B).'),
    28164: ('Se fizesse isso em público,CRseria uma confusão daquelas...', 'rewritten', 'Bom humor de Lyner sobre o escândalo social (121B <= 128B).'),
    28167: ('Não me olhe com essa carinha!CRÉ claro que você pode!', 'rewritten', 'Lyner cedendo imediatamente ao charme de Shurelia (110B <= 112B).'),
    28168: ('...Sim. Perdão pelo dengo...CRMas estou tão feliz!', 'rewritten', 'Doçura pura e contentamento de Shurelia (103B <= 104B).'),
    28169: ('É assim que a genteCRconversa!', 'rewritten', 'Explicação prática de Misha sobre a mecânica de conversa noturna (62B <= 72B).'),
    28174: ('Não me trateCRcomo criança!', 'rewritten', 'Misha protestando com bico adorável contra o excesso de zelo de Lyner (57B <= 64B).'),
    28176: ('Aurica, podemosCRconversar?', 'rewritten', 'Abordagem respeitosa de Lyner a Aurica (55B <= 56B).'),
    28180: ('Boa noite. Você vem sempre...CRGosta tanto assim de conversar comigo?', 'rewritten', 'Humildade tímida de Aurica ao notar o carinho de Lyner (140B <= 144B).'),
    28184: ('Lyner! Veio hoje também.CRVem cá, senta do meu lado...', 'rewritten', 'Acolhimento dócil de Aurica chamando para sentar pertinho (111B <= 120B).'),
    28187: ('Misha, podemosCRconversar?', 'rewritten', 'Abordagem amigável de Lyner a Misha (53B <= 56B).'),
    28190: ('Tarde da noite... que houve?CRMorrendo de saudade de mim? Brincadeira!', 'rewritten', 'Provocação carinhosa e descontraída de Misha (141B <= 152B).'),
    28194: ('Lyner! Demorou muito...CRCansei de te esperar!', 'rewritten', 'Reclamação manhosa de Misha pela demora (93B <= 96B).'),
    28197: ('Lyner... entra. Hoje você vaiCRficar a noite toda, né? Não me deixe só...', 'rewritten', 'Dengo apaixonado de Misha pedindo pernoite com Lyner (151B <= 152B).'),
    28199: ('O que houve?CRAconteceu algo?', 'rewritten', 'Shurelia preocupada com a visita tardia (59B <= 64B).'),
    28200: ('Lyner... Vir ao meu quarto tardeCRda noite não parece prudente...', 'rewritten', 'Recato inicial de Shurelia (132B <= 136B).'),
    28202: ('Lyner... entra...CRQuer que eu passe um chá?', 'rewritten', 'Hospitalidade acanhada de Shurelia servindo chá (90B <= 104B).'),
    28203: ('Lyner! Entra logo. Se você quiser...CReu queria que ficasse a noite toda comigo...', 'rewritten', 'Máxima intimidade de Shurelia no quarto noturno (166B <= 176B).'),
    28204: ('Entre!', 'rewritten', 'Permissão concisa de entrada no quarto (13B <= 24B).'),
    28206: ('Vou conversar com a Aurica.', 'rewritten', 'Opção do menu de conversa noturna com Aurica (55B <= 64B).'),
    28207: ('Vou conversar com a Misha.', 'rewritten', 'Opção do menu de conversa noturna com Misha (53B <= 64B).'),
    28242: ('Provar Suco Refeição', 'rewritten', 'Tópico de descanso sobre Foodjuice / Suco de Refeição (41B <= 48B).'),
    28279: ('Sonhos de Aurica para o futuro', 'rewritten', 'Tópico de descanso sobre aspirações pessoais de Aurica (61B <= 64B).'),
    28318: ('Ver o Card Center', 'rewritten', 'Tópico de descanso sobre visita ao Card Center na Torre (35B <= 48B).')
}

with open(BUILD_SCRIPT, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    m = re.match(r"^\s*(\d+):\s*\($", line)
    if m:
        d_id = int(m.group(1))
        if d_id in UPDATES:
            val = UPDATES[d_id]
            indent = " " * 8
            new_lines.append(line)
            new_lines.append(f'{indent}"{val[0]}",\n')
            new_lines.append(f'{indent}"{val[1]}",\n')
            new_lines.append(f'{indent}"{val[2]}"\n')
            new_lines.append(" " * 4 + "),\n")
            # pular as 4 linhas antigas
            i += 5
            continue
    new_lines.append(line)
    i += 1

with open(BUILD_SCRIPT, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("build_blk_sys_028.py atualizado com sucesso!")

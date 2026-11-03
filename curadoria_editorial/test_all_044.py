import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path("Ferramentas_Traducao").resolve()))
sys.path.insert(0, str(Path("Ferramentas_Traducao/tools").resolve()))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cfg = json.load(open("Ferramentas_Traducao/curadoria_editorial/curadoria_config.json", "r", encoding="utf-8"))
conn = sqlite3.connect(cfg["database_path"])
c = conn.cursor()
caps = {row[0]: row[1] for row in c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 32709 AND 32853").fetchall()}
conn.close()

data = json.load(open("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_044_input.json", "r", encoding="utf-8"))
dialogues = {d["id"]: d for d in data["dialogues"]}

# Propostas preliminares para teste
curated_proposals = {
    # 0541 - Síntese / Grathmeld na Oficina
    32709: {
        "pt": "Faltam itens. Vou ter que criar os ingredientes...",
        "notes": "Curadoria editorial concisa e eliminação de estouro de buffer (99B/128B)."
    },
    32710: {
        "pt": "Qual item devo criar primeiro?",
        "notes": "Adequação de verbo canônico de Grathmeld e buffer (61B/64B)."
    },
    32711: {
        "pt": "Qual cristal devo usar?",
        "notes": "Curadoria aprovada no buffer original (47B/56B)."
    },
    32712: {
        "pt": "Quantos devo criar?",
        "notes": "Harmonização de Grathmeld no buffer (39B/48B)."
    },
    32713: {
        "pt": "Tudo bem, vamos lá.",
        "notes": "Curadoria aprovada no buffer original (40B/48B)."
    },
    32714: {
        "pt": "Vou me esforçar!",
        "notes": "Determinação de Lyner (がんばるぞ) dentro do buffer (33B/40B)."
    },
    32715: {
        "pt": "Criei %s [%s].",
        "notes": "Curadoria aprovada com paridade de tags (29B/32B)."
    },
    32716: {
        "pt": "Preciso arrumar os itens que criei.",
        "notes": "Elegância concisa e adequação de buffer (71B/88B)."
    },
    32717: {
        "pt": "Faltam itens para criar %s.",
        "notes": "Soberania do japonês e eliminação de estouro de buffer (55B/80B)."
    },
    32718: {
        "pt": "Faltam itens. Quer preparar os ingredientes primeiro?",
        "notes": "Curadoria concisa e eliminação de estouro de buffer (109B/144B)."
    },
    32719: {
        "pt": "Qual item vai criar primeiro?",
        "notes": "Naturalidade em PT-BR e buffer (59B/64B)."
    },
    32720: {
        "pt": "Qual cristal você vai usar?",
        "notes": "Curadoria aprovada no buffer original (56B/72B)."
    },
    32721: {
        "pt": "Quantos vai criar?",
        "notes": "Concisão e ajuste de buffer (37B/48B)."
    },
    32722: {
        "pt": "Tudo bem assim?",
        "notes": "Curadoria aprovada no buffer original (31B/32B)."
    },
    32723: {
        "pt": "Força, Lyner♪",
        "notes": "Incentivo carinhoso da Reyvateil e nota musical dentro do buffer (27B/48B)."
    },
    32724: {
        "pt": "Feito %s [%s].",
        "notes": "Fidelidade a '%sが%s個できた' e ajuste ao limite físico estrito (29B/32B)."
    },
    32725: {
        "pt": "O que faremos com os itens criados?",
        "notes": "Elegância dramática e adequação de buffer (71B/88B)."
    },
    32726: {
        "pt": "Você não tem itens suficientes. Vai criar os ingredientes primeiro?",
        "notes": "Harmonização de síntese aprovada no buffer (137B/152B)."
    },
    32727: {
        "pt": "Qual cristal você vai usar?",
        "notes": "Curadoria aprovada no buffer original (56B/56B)."
    },
    32728: {
        "pt": "Vamos começar, Lyner.",
        "notes": "Curadoria aprovada no buffer original (44B/56B)."
    },
    32729: {
        "pt": "Sobre os itens que criamos, o que você quer fazer com eles?",
        "notes": "Curadoria aprovada no buffer original (120B/120B)."
    },
    32730: {
        "pt": "Parece que faltam itens para criar %s.",
        "notes": "Polidez de Shurelia e adequação de buffer (75B/96B)."
    },
    32731: {
        "pt": "Estão faltando itens. Gostaria de começar a preparar os ingredientes?",
        "notes": "Curadoria aprovada no buffer original (141B/144B)."
    },
    32732: {
        "pt": "Qual item gostaria de criar primeiro?",
        "notes": "Tom refinado de Shurelia e adequação de buffer (75B/88B)."
    },

    # 0542 - Síntese / Interação com Shurelia e Opções de Criação
    32733: {
        "pt": "Qual cristal você gostaria de usar?",
        "notes": "Curadoria aprovada no buffer original (72B/80B)."
    },
    32734: {
        "pt": "Quantos você gostaria?",
        "notes": "Curadoria aprovada no buffer original (46B/56B)."
    },
    32735: {
        "pt": "Está correto?",
        "notes": "Curadoria aprovada no buffer original (28B/40B)."
    },
    32736: {
        "pt": "Vamos em frente, Lyner.",
        "notes": "Incentivo sereno de Shurelia e adequação de buffer (47B/48B)."
    },
    32737: {
        "pt": "Feito %s [%s]♪",
        "notes": "Preservação da nota musical ♪ e adequação de buffer (29B/32B)."
    },
    32738: {
        "pt": "ItemIM06 OKIM00 VoltarIM01",
        "notes": "Curadoria aprovada com preservação de tags IM## (53B/68B)."
    },
    32739: {
        "pt": "Cristal GrathnodeIM04 OKIM00 VoltarIM01",
        "notes": "Curadoria aprovada com termo canônico e tags IM## (79B/96B)."
    },
    32740: {
        "pt": "QuantidadeIM05 OKIM00 VoltarIM01",
        "notes": "Curadoria aprovada com tags IM## (65B/72B)."
    },
    32741: {
        "pt": "Pronto! Vou chamá-lo de CR[%s]",
        "notes": "Curadoria aprovada com tag CR e variável [%s] (62B/64B)."
    },
    32742: {
        "pt": "Criar %s,",
        "notes": "Curadoria aprovada com variável (19B/24B)."
    },
    32743: {
        "pt": "AvançarIM00 PularIM01",
        "notes": "Curadoria aprovada com tags IM## (44B/48B)."
    },
    32744: {
        "pt": "Misturar antigo e novo",
        "notes": "Fidelidade direta ao JP (古いものと新しいものを混ぜる) e buffer (45B/48B)."
    },
    32745: {
        "pt": "Vender o antigo",
        "notes": "Opção concisa de menu e eliminação de estouro de buffer (31B/32B)."
    },
    32746: {
        "pt": "Vender o novo",
        "notes": "Opção concisa de menu e eliminação de estouro de buffer (27B/32B)."
    },
    32747: {
        "pt": "Itens unidos: %s qual. [%s] x%s.",
        "notes": "Preservação das variáveis e colchetes e adequação de buffer (65B/88B)."
    },
    32748: {
        "pt": "Vendeu o antigo por %s Leaf. Agora: qualidade %s [%s] x%s.",
        "notes": "Curadoria aprovada no buffer original (117B/128B)."
    },
    32749: {
        "pt": "Vendeu o novo por %s Leaf. Agora: qualidade %s [%s] x%s.",
        "notes": "Curadoria aprovada no buffer original (113B/128B)."
    },
    32750: {
        "pt": "Posso chamá-lo de %s?",
        "notes": "Curadoria aprovada com variável (44B/48B)."
    },
    32751: {
        "pt": "Sim",
        "notes": "Curadoria aprovada no buffer original (7B/8B)."
    },
    32752: {
        "pt": "Não",
        "notes": "Curadoria aprovada no buffer original (8B/8B)."
    },
    32753: {
        "pt": "ItemIM06 OKIM00",
        "notes": "Curadoria aprovada com tags IM## (31B/52B)."
    },
    32754: {
        "pt": "QuantidadeIM05 OKIM00",
        "notes": "Curadoria aprovada com tags IM## (43B/56B)."
    },
    32755: {
        "pt": "Cristal GrathnodeIM04 OKIM00",
        "notes": "Curadoria aprovada com termo canônico e tags IM## (57B/80B)."
    },

    # 0543 - Categorias de Equipamento
    32756: {
        "pt": "Traje",
        "notes": "Curadoria aprovada no buffer original (11B/16B)."
    },
    32757: {
        "pt": "Arma",
        "notes": "Curadoria aprovada no buffer original (9B/16B)."
    },
    32758: {
        "pt": "Armad.",
        "notes": "Abreviatura elegante de armadura no buffer original (13B/16B)."
    },
    32759: {
        "pt": "Acess.",
        "notes": "Curadoria aprovada no buffer original (13B/24B)."
    },
    32760: {
        "pt": "Remover",
        "notes": "Comando clássico de desequipar e adequação de buffer (15B/16B)."
    },
    32761: {
        "pt": "Remover",
        "notes": "Comando clássico de desequipar e adequação de buffer (15B/16B)."
    },
    32762: {
        "pt": "Remover Cristal Grathnode",
        "notes": "Curadoria aprovada no buffer original (51B/56B)."
    },
    32763: {
        "pt": "(Nada)",
        "notes": "Concisão com parênteses originais e adequação de buffer (13B/16B)."
    },

    # 0544 - Ações de Batalha e Itens
    32764: {
        "pt": "Parar Canto",
        "notes": "Interrupção de canto lírico e adequação de buffer (23B/24B)."
    },
    32765: {
        "pt": "(Nada)",
        "notes": "Concisão com parênteses originais e adequação de buffer (13B/16B)."
    },
    32766: {
        "pt": "Sem canto inicial",
        "notes": "Curadoria aprovada no buffer original (35B/40B)."
    },
    32767: {
        "pt": "(Nada)",
        "notes": "Concisão com parênteses originais e adequação de buffer (13B/16B)."
    },
    32768: {
        "pt": "Criar %s,",
        "notes": "Curadoria aprovada no buffer original (19B/24B)."
    },
    32769: {
        "pt": "Criar %s,",
        "notes": "Curadoria aprovada no buffer original (19B/24B)."
    },
    32770: {
        "pt": "Cristal Grathnode",
        "notes": "Curadoria aprovada com termo canônico (35B/40B)."
    },
    32771: {
        "pt": "Criar %s,",
        "notes": "Curadoria aprovada no buffer original (19B/24B)."
    },
    32772: {
        "pt": "Item novo",
        "notes": "Curadoria aprovada no buffer original (19B/24B)."
    },
    32773: {
        "pt": "Item antigo",
        "notes": "Extensão natural sem truncamento dentro do limite físico (23B/24B)."
    },

    # 0545 - Tutorial de Instalação de Cristais Grathnode (Aurica / Misha)
    32774: {
        "pt": "Personagem IM06 OKIM00 VoltarIM01",
        "notes": "Curadoria aprovada com tags de controle (67B/84B)."
    },
    32775: {
        "pt": "Instalar é bem o que disseram na Loja de Mergulho: pôr um Cristal Grathnode em mim.",
        "notes": "Clareza expositiva da lore e adequação de buffer (165B/200B)."
    },
    32776: {
        "pt": "Mas não dá para enfiar o Cristal Grathnode em qualquer lugar.",
        "notes": "Tom coloquial natural e adequação de buffer (121B/144B)."
    },
    32777: {
        "pt": "As Reyvateils têm no corpo a porta de instalação, que absorve o Cristal Grathnode.",
        "notes": "Fidelidade conceitual à fisiologia de Reyvateil e adequação de buffer (167B/264B)."
    },
    32778: {
        "pt": "No meu caso, fica perto da nuca...",
        "notes": "Confissão tímida de Aurica e adequação de buffer (71B/72B)."
    },
    32779: {
        "pt": "Hum... afaste meu cabelo e olhe minhas costas.",
        "notes": "Hesitação tímida de Aurica (えと...あの...) e adequação de buffer (93B/96B)."
    },
    32780: {
        "pt": "O... O quê! Tem certeza?",
        "notes": "Espanto de Lyner aprovado no buffer original (50B/56B)."
    },
    32781: {
        "pt": "D-dê só uma olhadinha, tá? Não fique me encarando ali!",
        "notes": "Curadoria aprovada no buffer original (113B/120B)."
    },
    32782: {
        "pt": "A-ah...",
        "notes": "Reação desconcertada de Lyner (あ、ああ...) e adequação de buffer (13B/16B)."
    },
    32783: {
        "pt": "O-o que é isso? Tem um desenho na sua pele!?",
        "notes": "Curadoria aprovada no buffer original (90B/104B)."
    },
    32784: {
        "pt": "Essa é a porta de instalação. Você vê o círculo no meio do padrão? Se você encostar um Cristal Grathnode nela, ela o absorverá.",
        "notes": "Curadoria aprovada no buffer original (262B/280B)."
    },
    32785: {
        "pt": "Tente.",
        "notes": "Comando direto e delicado de Aurica e adequação de buffer (13B/16B)."
    },
    32786: {
        "pt": "Minha porta de instalação fica perto da nuca.",
        "notes": "Curadoria aprovada no buffer original (91B/96B)."
    },
    32787: {
        "pt": "Vê o desenho nas minhas costas? O círculo no meio é minha porta de instalação.",
        "notes": "Curadoria aprovada no buffer original (160B/224B)."
    },
    32788: {
        "pt": "A minha fica no meu peito.",
        "notes": "Franqueza de Misha e adequação de buffer (53B/56B)."
    },
    32789: {
        "pt": "Aqui... vê como parece uma tatuagem entre meus seios...?",
        "notes": "Curadoria aprovada no buffer original (114B/128B)."
    },
    32790: {
        "pt": "Hum... bem, não sei se deveria estar olhando para isso...",
        "notes": "Curadoria aprovada no buffer original (116B/120B)."
    },
    32791: {
        "pt": "Tarado! Não vou mostrar meus seios pra você! ...Puxa...",
        "notes": "Reação tsundere clássica de Misha e adequação de buffer (113B/144B)."
    },
    32792: {
        "pt": "Desculpe...",
        "notes": "Desculpas constrangidas de Lyner e adequação de buffer (23B/24B)."
    },
    32793: {
        "pt": "Essa coisa perto do seu seio... é uma tatuagem?",
        "notes": "Curadoria aprovada no buffer original (96B/96B)."
    },
    32794: {
        "pt": "Essa é a minha porta de instalação. Vê o círculo no meio? Encoste um Cristal Grathnode nela e ela o absorve.",
        "notes": "Explicação fluida e adequação de buffer (217B/256B)."
    },
    32795: {
        "pt": "Minha porta de instalação é no colo.",
        "notes": "Elegância anatômica e adequação de buffer (73B/80B)."
    },
    32796: {
        "pt": "Vê o padrão entre meus seios? Ache o círculo no meio. Essa é a minha porta de instalação.",
        "notes": "Instrução de Misha e adequação de buffer (181B/208B)."
    },
    32797: {
        "pt": "Minha porta fica no quadril.",
        "notes": "Localização anatômica de Shurelia e adequação de buffer (57B/64B)."
    },

    # 0546 - Instalação e Tutorial Prático de Grathmeld
    32798: {
        "pt": "Viu? Está bem ali em cima da minha bunda...",
        "notes": "Curadoria aprovada no buffer original (88B/88B)."
    },
    32799: {
        "pt": "...? O que foi? Você não quer ver?",
        "notes": "Curadoria aprovada no buffer original (67B/88B)."
    },
    32800: {
        "pt": "Não, não é nada disso...",
        "notes": "Gaguejo de Lyner (あ、いえ、そういうワケじゃ...) e adequação de buffer (49B/72B)."
    },
    32801: {
        "pt": "Vê a marca no meu quadril? Bem ali.",
        "notes": "Direcionamento visual e adequação de buffer (71B/104B)."
    },
    32802: {
        "pt": "Instalar adiciona efeitos especiais à Magia da Canção.",
        "notes": "Concisão do sistema tutorial e adequação de buffer (109B/128B)."
    },
    32803: {
        "pt": "Por exemplo, instalar um Cristal Grathnode com efeito [Veneno] em um feitiço simples de dano adicionará dano de veneno à Canção.",
        "notes": "Curadoria aprovada com paridade de colchetes (260B/264B)."
    },
    32804: {
        "pt": "Instale e teste minhas Canções em batalha.",
        "notes": "Convite combativo da Reyvateil e adequação de buffer (85B/96B)."
    },
    32805: {
        "pt": "Primeiro, escolha o item que deseja criar.",
        "notes": "Instrução de síntese e adequação de buffer (85B/104B)."
    },
    32806: {
        "pt": "Como queremos o [Healy C], escolha este. Aperte o botão IM00.",
        "notes": "Preservação de termo e tag IM00 e adequação de buffer (123B/144B)."
    },
    32807: {
        "pt": "E então verifique seus ingredientes.",
        "notes": "Curadoria aprovada no buffer original (74B/80B)."
    },
    32808: {
        "pt": "Sem ingredientes, derrote inimigos ou compre-os para poder criar seu item.",
        "notes": "Instrução prática do vovô e adequação de buffer (151B/168B)."
    },
    32809: {
        "pt": "Desta vez, preparei os ingredientes só para você.",
        "notes": "Generosidade do mestre e adequação de buffer (99B/120B)."
    },
    32810: {
        "pt": "Recebeu [Pedra Azul]!",
        "notes": "Curadoria aprovada no buffer original (43B/48B)."
    },
    32811: {
        "pt": "Recebeu Cristal Grathnode [Canção +10%]!",
        "notes": "Item especial de síntese e adequação de buffer (81B/104B)."
    },
    32812: {
        "pt": "Agora pode continuar o Grathmeld.",
        "notes": "Termo canônico de síntese e adequação de buffer (67B/72B)."
    },
    32813: {
        "pt": "Quando você vir um Cristal Grathnode como material, terá que decidir qual cristal deseja usar.",
        "notes": "Curadoria aprovada no buffer original (191B/200B)."
    },
    32814: {
        "pt": "O valor de [Qualidade] do Cristal Grathnode tem um efeito enorme na qualidade do item.",
        "notes": "Curadoria aprovada no buffer original (173B/184B)."
    },
    32815: {
        "pt": "Criar itens com [Qualidade] alta traz muitas vantagens excelentes.",
        "notes": "Clareza expositiva do tutor e adequação de buffer (133B/168B)."
    },
    32816: {
        "pt": "Agora que você selecionou seus materiais, escolha quantos deseja fabricar.",
        "notes": "Curadoria aprovada no buffer original (150B/160B)."
    },
    32817: {
        "pt": "Agora só falta criar o item. Vá em frente e tente.",
        "notes": "Curadoria aprovada no buffer original (103B/120B)."
    },
    32818: {
        "pt": "Consegui!",
        "notes": "Curadoria aprovada no buffer original (19B/24B)."
    },
    32819: {
        "pt": "Sim, muito bem!",
        "notes": "Curadoria aprovada no buffer original (31B/32B)."
    },
    32820: {
        "pt": "Eis o seu [Healy C] pronto.",
        "notes": "Conclusão de item de síntese e adequação de buffer (55B/56B)."
    },
    32821: {
        "pt": "Certos itens passam a ser vendidos nas lojas após serem criados pela primeira vez.",
        "notes": "Mecânica de desbloqueio de lojas e adequação de buffer (165B/170B)."
    },

    # 0547 - Tipos de Habilidade e Custo
    32822: {
        "pt": "Hab. passiva",
        "notes": "Abreviatura canônica de menu e adequação de buffer (25B/32B)."
    },
    32823: {
        "pt": "Hab. de cura",
        "notes": "Abreviatura canônica de menu e adequação de buffer (25B/32B)."
    },
    32824: {
        "pt": "HP consumido",
        "notes": "Concordância gramatical enxuta no buffer (25B/28B)."
    },

    # 0548 a 0554 - Menus de Áudio, Confirmação e Fechamento Sistêmico Final
    32825: {"pt": "BGM", "notes": "Configuração de música no buffer original (7B/8B)."},
    32826: {"pt": "SSE", "notes": "Configuração de efeitos sonoros no buffer original (7B/16B)."},
    32827: {"pt": "Sim", "notes": "Confirmação afirmativa no buffer original (7B/8B)."},
    32828: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/16B)."},
    32829: {"pt": "Usar", "notes": "Ação de item no buffer original (9B/22B)."},
    32830: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/8B)."},
    32831: {"pt": "Bam", "notes": "Modo de execução imediata no buffer original (7B/8B)."},
    32832: {"pt": "DES", "notes": "Chave seletora desligada no buffer original (7B/8B)."},
    32833: {"pt": "LIG", "notes": "Chave seletora ligada no buffer original (7B/8B)."},
    32834: {"pt": "Sim", "notes": "Confirmação afirmativa no buffer original (7B/8B)."},
    32835: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/8B)."},
    32836: {"pt": "Sim", "notes": "Confirmação afirmativa no buffer original (7B/8B)."},
    32837: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/8B)."},
    32838: {"pt": "Sim", "notes": "Confirmação afirmativa no buffer original (7B/8B)."},
    32839: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/20B)."},
    32840: {"pt": "Cp.", "notes": "Abreviatura de comprar no buffer original (7B/8B)."},
    32841: {"pt": "Sim", "notes": "Confirmação afirmativa no buffer original (7B/8B)."},
    32842: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/20B)."},
    32843: {"pt": "DP", "notes": "Dive Points no buffer original (5B/14B)."},
    32844: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/11B)."},
    32845: {"pt": "DP", "notes": "Dive Points no buffer original (5B/8B)."},
    32846: {"pt": "Sim", "notes": "Confirmação afirmativa no buffer original (7B/8B)."},
    32847: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/16B)."},
    32848: {"pt": "Sim", "notes": "Confirmação afirmativa no buffer original (7B/8B)."},
    32849: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/8B)."},
    32850: {"pt": "Sim", "notes": "Confirmação afirmativa no buffer original (7B/8B)."},
    32851: {"pt": "Não", "notes": "Confirmação negativa no buffer original (8B/8B)."},
    32852: {"pt": "Sim", "notes": "Confirmação afirmativa no buffer original (7B/8B)."},
    32853: {"pt": "Não", "notes": "Confirmação negativa final da base executável (8B/11B)."}
}

print(f"Total propostas definidas: {len(curated_proposals)}")

# Teste de validação e de buffer para todas as 145 falas
overflows = []
val_errors = []

for lid in range(32709, 32854):
    d = dialogues[lid]
    orig_en = d.get("original_en", "")
    prop = curated_proposals.get(lid)
    if not prop:
        print(f"FALTA PROPOSTA PARA ID {lid}!")
        continue
    text = prop["pt"]
    cap = caps[lid]
    sz = encoded_size(text)
    if sz > cap:
        overflows.append((lid, sz, cap, sz - cap, text))
    errs = validate_line(lid, orig_en, text)
    if errs:
        val_errors.append((lid, errs, text))

print(f"Resultado do teste preliminar:")
print(f"Estouros de buffer: {len(overflows)}")
for ov in overflows:
    print(f"  ID {ov[0]}: {ov[1]}B > {ov[2]}B (+{ov[3]}B) -> '{ov[4]}'")

print(f"Erros de validação técnica: {len(val_errors)}")
for ve in val_errors:
    print(f"  ID {ve[0]}: {ve[1]} -> '{ve[2]}'")

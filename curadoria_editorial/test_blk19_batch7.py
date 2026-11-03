import json
import sys
from pathlib import Path

BASE_DIR = Path("Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "tools"))

from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

with open(BASE_DIR / "curadoria_editorial/limits_blk19.json", "r", encoding="utf-8") as f:
    limits = json.load(f)

# Batch 7: IDs 25741 to 25801 (61 lines)
# Desafio culinário entre Aurica e Lyner; O mascote Don Leon (どんすけ) contra pesadelos;
# Desejo romântico de presentes combinando na Fancy Shop (おそろいの物); Crise de ciúmes de Noelle (ナール) de Karulu.
batch7_curated = {
    25741: (
        "Hã? Ah, aquilo! É, o sabor vicia, né?",
        "Resolução de estouro (84B -> 80B <= 112B). Lyner elogiando a refeição peculiar de Aurica ('クセになる').",
        "rewritten"
    ),
    25742: (
        "Tinha um gosto esquisito, mas sim, tava gostoso!",
        "Resolução de estouro (111B -> 96B <= 112B). Elogio sincero e bem-humorado de Lyner.",
        "rewritten"
    ),
    25743: (
        "Que bom que gostou! Mas como só usei coisas gostosas, não tinha como ficar ruim!",
        "Resolução de estouro (242B -> 163B <= 192B). Lógica culinária hilária e infalível de Aurica.",
        "rewritten"
    ),
    25744: (
        "C-cozinhar desse jeito dá certo mesmo?",
        "Resolução de estouro (84B -> 77B <= 104B). Lyner incrédulo com o método gastronômico.",
        "rewritten"
    ),
    25745: (
        "Claro. É assim que sempre fiz.",
        "Aurica convicta de sua técnica (62B <= 88B).",
        "approved"
    ),
    25746: (
        "É mesmo...? Bem, mas tava gostoso, então quero que faça de novo pra mim.",
        "Resolução de estouro (190B -> 151B <= 192B). Lyner pedindo repeteco.",
        "rewritten"
    ),
    25747: (
        "...Se você atender a um pedido meu,CRposso fazer de novo com prazer.",
        "Resolução de estouro (151B -> 139B <= 152B). Aurica impondo uma condição doce com CR.",
        "rewritten"
    ),
    25748: (
        "Hã? Pedido?",
        "Lyner atento (24B <= 24B).",
        "approved"
    ),
    25749: (
        "Da próxima vez, você cozinha pra mim!CRDaí eu retribuo cozinhando pra você de novo.",
        "Resolução de estouro (209B -> 171B <= 192B). Desafio de troca gastronômica com CR.",
        "rewritten"
    ),
    25750: (
        "Eu!? Por mim tudo bem, mas não garanto o sabor, hein!",
        "Resolução de estouro (139B -> 108B <= 136B). Lyner aceitando sem prometer alta gastronomia.",
        "rewritten"
    ),
    25751: (
        "Só sei fazer gororoba de homem...",
        "Resolução de estouro (92B -> 70B <= 96B). Lyner descrevendo sua comida rústica ('男の料理').",
        "rewritten"
    ),
    25752: (
        "Sem problema! É só jogar o que achar gostoso que fica uma delícia!",
        "Resolução de estouro (165B -> 138B <= 176B). Aurica encorajando Lyner com sua teoria gastronômica.",
        "rewritten"
    ),
    25753: (
        "...Prefiro seguir um livro de receitas.",
        "Resolução de estouro (102B -> 79B <= 88B). Lyner preferindo métodos científicos e seguros.",
        "rewritten"
    ),
    25754: (
        "Ah, é, tenho uma coisa boa.",
        "Aurica anunciando um item especial (56B <= 64B).",
        "approved"
    ),
    25755: (
        "Algo bom? É comida ou algo assim?",
        "Lyner ainda pensando no estômago (68B <= 88B).",
        "approved"
    ),
    25756: (
        "Não. Aqui, é o Don Leon.",
        "Apresentação do amuleto/mascote Don Leon ('どんすけ') (51B <= 56B).",
        "approved"
    ),
    25757: (
        "...Não é comida.",
        "Resolução de estouro (45B -> 35B <= 40B). Constatação seca de Lyner ao ver o bicho de pelúcia.",
        "rewritten"
    ),
    25758: (
        "Não coma ele!CRSó vou emprestar por hoje à noite.",
        "Resolução de estouro (100B -> 102B <= 104B). Aurica fingindo proteger o mascote da fome de Lyner com CR.",
        "rewritten"
    ),
    25759: (
        "Se puser perto do travesseiro,CRnunca vai ter pesadelos!",
        "Resolução de estouro (145B -> 113B <= 128B). O poder anti-pesadelos lendário de Don Leon com CR.",
        "rewritten"
    ),
    25760: (
        "É...? Mas não era melhor você ficar com ele?",
        "Resolução de estouro (140B -> 92B <= 96B). Lyner sugerindo que Aurica precisa mais do amuleto.",
        "rewritten"
    ),
    25761: (
        "Uma noite não faz mal.CRQuero emprestar pra você.",
        "Resolução de estouro (114B -> 101B <= 112B). Gesto afetuoso de desapego com CR.",
        "rewritten"
    ),
    25762: (
        "Mas eu gosto da sensação de alívio ao acordar de um pesadelo...",
        "Gosto peculiar de Lyner pela adrenalina pós-pesadelo (125B <= 160B).",
        "approved"
    ),
    25763: (
        "É mais saudável ter um sono tranquilo e acordar revigorado.",
        "Aurica defendendo a higiene do sono (121B <= 128B).",
        "approved"
    ),
    25764: (
        "Você vai ter um sonho bom!",
        "Bênção carinhosa de Aurica (54B <= 56B).",
        "approved"
    ),
    25765: (
        "...B-bem, então eu levo ele...",
        "Resolução de estouro (74B -> 62B <= 64B). Lyner aceitando a companhia de Don Leon com hesitação cômica.",
        "rewritten"
    ),
    25766: (
        "Oba! Agora vai dormir em paz!",
        "Resolução de estouro (98B -> 59B <= 80B). Comemoração doce de Aurica.",
        "rewritten"
    ),
    25767: (
        "(Acho que vai ter o efeito oposto em mim...)",
        "Pensamento cômico de Lyner encarando o boneco (89B <= 104B).",
        "approved"
    ),
    25768: (
        "Sabe... não precisa ser logo, mas queria ir à Fancy Shop de novo...",
        "Resolução de estouro (163B -> 137B <= 160B). Aurica voltando ao seu maior desejo.",
        "rewritten"
    ),
    25769: (
        "Ah, aquela em Platina. Você gosta mesmo de lá, né?",
        "Lyner notando o fascínio dela (104B <= 120B).",
        "approved"
    ),
    25770: (
        "É. Não tem nada parecido no Mundo Inferior.",
        "O encanto das novidades de Platina (89B <= 104B).",
        "approved"
    ),
    25771: (
        "Haha, tá bom. E o que você quer dessa vez?",
        "Resolução de estouro (99B -> 87B <= 96B). Lyner disposto a agradar.",
        "rewritten"
    ),
    25772: (
        "Hum... bem...",
        "Hesitação tímida de Aurica (27B <= 32B).",
        "approved"
    ),
    25773: (
        "Não é que eu queira comprar algo específico...",
        "Resolução de estouro (106B -> 96B <= 104B). Aurica preparando o terreno para o pedido especial.",
        "rewritten"
    ),
    25774: (
        "Quer só ficar olhando as vitrines?",
        "Resolução de estouro (93B -> 70B <= 88B). Lyner tentando adivinhar.",
        "rewritten"
    ),
    25775: (
        "Não, também não é isso...",
        "Negação tímida de Aurica (55B <= 64B).",
        "approved"
    ),
    25776: (
        "...Quero que você escolha alguma coisa.",
        "O desejo de ter algo escolhido pessoalmente por Lyner (80B <= 80B).",
        "approved"
    ),
    25777: (
        "Hã!? Eu!?",
        "Resolução de estouro (26B -> 20B <= 24B). Lyner pego de surpresa com a responsabilidade.",
        "rewritten"
    ),
    25778: (
        "Queria que você escolhesse e me desse de presente...",
        "Resolução de estouro (164B -> 106B <= 136B). A confissão fofa do presente dos sonhos de Aurica.",
        "rewritten"
    ),
    25779: (
        "...Mas não sei o que você gostaria.",
        "Lyner inseguro com seu bom gosto (73B <= 80B).",
        "approved"
    ),
    25780: (
        "Se for escolhido por você, vou amar...",
        "Resolução de estouro (108B -> 78B <= 88B). Declaração romântica pura de Aurica ('ライナーが選んでくれると、嬉しいな...').",
        "rewritten"
    ),
    25781: (
        "...Tudo bem. Compro algo na próxima vez que formos.",
        "Resolução de estouro (142B -> 104B <= 120B). Promessa solene de Lyner.",
        "rewritten"
    ),
    25782: (
        "Uhu! Fico no aguardo!",
        "Resolução de estouro (57B -> 43B <= 48B). Aurica radiante de felicidade.",
        "rewritten"
    ),
    25783: (
        "Ei, Lyner, quando vamos para Platina?",
        "Ansiedade de Aurica pelo passeio romântico (75B <= 88B).",
        "approved"
    ),
    25784: (
        "Hã? Bem... acho que vamos em breve.",
        "Resolução de estouro (101B -> 72B <= 88B). Lyner respondendo com calma.",
        "rewritten"
    ),
    25785: (
        "...Posso te pedir um favor?",
        "Resolução de estouro (70B -> 55B <= 64B). Aurica introduzindo a surpresa do casal.",
        "rewritten"
    ),
    25786: (
        "Já sei. Quer ir na Fancy Shop, né?",
        "Lyner adivinhando de primeira (69B <= 104B).",
        "approved"
    ),
    25787: (
        "É... como você sabia?",
        "Aurica sem graça por ser tão previsível (45B <= 48B).",
        "approved"
    ),
    25788: (
        "É só um palpite. Tudo bem, tem algo que você quer, certo?",
        "Lyner sendo compreensivo (118B <= 136B).",
        "approved"
    ),
    25789: (
        "É... mas queria que você comprasse.",
        "Resolução de estouro (91B -> 73B <= 80B). Aurica reforçando o pedido de presente.",
        "rewritten"
    ),
    25790: (
        "...Quer um presente meu, né?",
        "Resolução de estouro (78B -> 58B <= 72B). Lyner confirmando o óbvio.",
        "rewritten"
    ),
    25791: (
        "Sim... mas tem que comprar um pra você também!",
        "Resolução de estouro (112B -> 95B <= 104B). A exigência romântica de comprar itens para os dois.",
        "rewritten"
    ),
    25792: (
        "Sabe... queria presentes combinando... pode ser?",
        "Resolução de estouro (95B -> 97B <= 112B). O desejo mais doce de Aurica: itens de casal combinando ('おそろいの物').",
        "rewritten"
    ),
    25793: (
        "C-combinando!?",
        "Resolução de estouro (39B -> 29B <= 32B). Choque e rubor de Lyner diante da proposta de casal.",
        "rewritten"
    ),
    25794: (
        "Fico feliz quando as pessoas dão presentes assim... então, tudo bem?",
        "Aurica pedindo com olhar pidão (139B <= 144B).",
        "approved"
    ),
    25795: (
        "T-tá... Mas eu que escolho os dois?",
        "Resolução de estouro (71B -> 71B <= 88B). Lyner atordoado com a missão.",
        "rewritten"
    ),
    25796: (
        "Hehehe... Conto com você!",
        "Resolução de estouro (58B -> 52B <= 56B). Aurica rindo satisfeita ('えへへ...期待してるよ').",
        "rewritten"
    ),
    25797: (
        "Aquela garota da loja de Karulu parecia bem íntima de você, né?",
        "Crise de ciúmes de Aurica sobre Noelle ('ナール') (124B <= 176B).",
        "approved"
    ),
    25798: (
        "Vila de Karulu...? Tá falando da Noelle?",
        "Resolução de estouro (115B -> 82B <= 88B). Lyner inocente tentando entender a quem ela se refere.",
        "rewritten"
    ),
    25799: (
        "Não sei o nome dela!CRÉ aquela garota da loja no topo da coluna.",
        "Aurica disfarçando o ciúme com biquinho e se recusando a falar o nome da rival com CR (126B <= 160B).",
        "approved"
    ),
    25800: (
        "É que ela me ajudou demais naquela loja.",
        "Resolução de estouro (105B -> 82B <= 96B). Lyner se explicando sem perceber a crise de ciúmes.",
        "rewritten"
    ),
    25801: (
        "Foi lá que ela me ensinou Grathmeld.",
        "Lyner revelando a mentora de Grathmeld (74B <= 80B).",
        "approved"
    )
}

if __name__ == "__main__":
    assert len(batch7_curated) == 61, f"Esperado 61, obtido {len(batch7_curated)}"
    errs = []
    for did, (text, rat, verd) in batch7_curated.items():
        lim = limits[str(did)]
        enc = encoded_size(text)
        if enc > lim:
            errs.append(f"ID {did}: enc {enc}B > limit {lim}B (+{enc - lim})")
        v_errs = validate_line(did, "", text)
        if v_errs:
            errs.append(f"ID {did} validação: {v_errs}")

    if errs:
        print(f"Erros em Batch 7 ({len(errs)}):")
        for e in errs:
            print(" ", e)
        sys.exit(1)
    else:
        print("Batch 7: 100% OK! 61 falas validadas com 0 estouros e 0 erros técnicos.")

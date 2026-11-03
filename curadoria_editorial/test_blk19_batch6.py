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

# Batch 6: IDs 25701 to 25740 (40 lines)
# Vida no Silvaplate; o Templo de Em Pheyna cheio de monstros; pedidos para a Fancy Shop;
# Crítica à loja da Alameda Hoshinose; introdução à comida caseira de Aurica.
batch6_curated = {
    25701: (
        "Mas como loja de variedades, é bem divertida.",
        "Resolução de estouro (154B -> 92B <= 112B). Lyner elogiando a diversidade da Fancy Shop.",
        "rewritten"
    ),
    25702: (
        "É que você é menino, né?CRNão liga muito para fofuras.",
        "Resolução de estouro (162B -> 114B <= 144B). Aurica provocando Lyner por não se encantar com bibelôs fofos com CR.",
        "rewritten"
    ),
    25703: (
        "Você gostou mesmo tanto assim da loja?",
        "Lyner percebendo a empolgação genuína dela (78B <= 80B).",
        "approved"
    ),
    25704: (
        "É. Quero voltar lá algum dia.",
        "Aurica confirmando o encanto (61B <= 72B).",
        "approved"
    ),
    25705: (
        "Fiquei um pouco surpresa quando descobri que havia pessoas morando no Silvaplate.",
        "Aurica impressionada com a civilização em Silvaplate (163B <= 176B).",
        "approved"
    ),
    25706: (
        "É, isso me surpreendeu também. Principalmente aquelas pessoas que moravam lá no alto.",
        "Lyner compartilhando o espanto sobre os vilarejos elevados (174B <= 176B).",
        "approved"
    ),
    25707: (
        "É. A vida deles parece difícil. Mas tinham jardins e tal, então tudo bem.",
        "Aurica refletindo sobre o estilo de vida agrícola nas alturas (150B <= 200B).",
        "approved"
    ),
    25708: (
        "Mas não é difícil viver sem lojas e essas coisas?",
        "Lyner pensando no isolamento comercial (102B <= 104B).",
        "approved"
    ),
    25709: (
        "E não tem uns guardiões bem fortes nessa área?",
        "Perigo constante dos monstros em Silvaplate (96B <= 120B).",
        "approved"
    ),
    25710: (
        "É, tem muitos...",
        "Aurica confirmando o perigo (34B <= 48B).",
        "approved"
    ),
    25711: (
        "Eles lutam?",
        "Lyner indagando se os moradores enfrentam as feras (23B <= 32B).",
        "approved"
    ),
    25712: (
        "Nem imagino...",
        "Resolução de estouro (48B -> 29B <= 40B). Aurica não conseguindo visualizar os camponeses em combate.",
        "rewritten"
    ),
    25713: (
        "Mas é tão bizarro.",
        "Resolução de estouro (54B -> 39B <= 40B). Aurica mudando de assunto para outra bizarrice do mundo.",
        "rewritten"
    ),
    25714: (
        "O que foi?",
        "Lyner curioso (21B <= 24B).",
        "approved"
    ),
    25715: (
        "O templo de Em Pheyna. É um templo, mas está cheio de inimigos.",
        "Crítica lúcida de Aurica sobre o templo sagrado infestado (129B <= 136B).",
        "approved"
    ),
    25716: (
        "Você não acha estranho ter que lutar contra inimigos num lugar assim?",
        "Indignação com o contrassenso de um santuário perigoso (141B <= 144B).",
        "approved"
    ),
    25717: (
        "Pensando bem, é verdade.",
        "Resolução de estouro (82B -> 50B <= 72B). Lyner concordando com a contradição.",
        "rewritten"
    ),
    25718: (
        "É mais um covil do que um templo...",
        "Definição cômica e certeira de Aurica sobre Em Pheyna ('あれじゃ寺院ていうより、巣窟だよ') (72B <= 80B).",
        "approved"
    ),
    25719: (
        "É, bem, você está certa.",
        "Lyner rindo sem jeito (52B <= 56B).",
        "approved"
    ),
    25720: (
        "Parece que usam o treinamento como desculpa para a gente eliminar os inimigos.",
        "Aurica desmascarando as missões e provações da Igreja (157B <= 176B).",
        "approved"
    ),
    25721: (
        "...Não dá para negar, é verdade.",
        "Resolução de estouro (79B -> 68B <= 72B). Lyner admitindo que viraram faxineiros de monstros.",
        "rewritten"
    ),
    25722: (
        "Ei, quero voltar na Fancy Shop.",
        "Resolução de estouro (82B -> 63B <= 88B). Aurica voltando ao seu assunto favorito: a Fancy Shop.",
        "rewritten"
    ),
    25723: (
        "Em Platina? Claro, por mim tudo bem.",
        "Resolução de estouro (87B -> 73B <= 80B). Lyner topando o passeio.",
        "rewritten"
    ),
    25724: (
        "Lá tem um monte de coisas fofas que as garotas adoram.",
        "Resolução de estouro (170B -> 110B <= 144B). Lyner compreendendo o gosto feminino.",
        "rewritten"
    ),
    25725: (
        "É. Tem uma coisa que eu quero muito comprar.",
        "Aurica insinuando um desejo especial (90B <= 104B).",
        "approved"
    ),
    25726: (
        "Beleza. Vai comprar quando a gente for lá?",
        "Resolução de estouro (124B -> 86B <= 112B). Lyner inocente perguntando se ela vai pagar.",
        "rewritten"
    ),
    25727: (
        "Não, você vai comprar pra mim.",
        "Resolução de estouro (75B -> 63B <= 72B). Aurica cobrando o agrado ('ううん、ライナーに買ってもらう').",
        "rewritten"
    ),
    25728: (
        "Quero que me dê de presente, Lyner!",
        "Resolução de estouro (123B -> 72B <= 96B). Aurica declarando abertamente o mimo desejado.",
        "rewritten"
    ),
    25729: (
        "Bem, Aurica, hum...",
        "Lyner desconcertado com o pedido direto (39B <= 40B).",
        "approved"
    ),
    25730: (
        "Compra pra mim, Lyner...",
        "Resolução de estouro (70B -> 49B <= 56B). Charme irresistível de Aurica ('ライナーに買ってもらいたいな...').",
        "rewritten"
    ),
    25731: (
        "...Tudo bem. Mas é melhor não ser muito caro, tá?",
        "Lyner cedendo com cautela financeira (102B <= 112B).",
        "approved"
    ),
    25732: (
        "Hehe... vamos ver isso.",
        "Risadinha marota de Aurica (47B <= 64B).",
        "approved"
    ),
    25733: (
        "Falando nisso, viu a loja da Alameda Hoshinose?",
        "Resolução de estouro (123B -> 95B <= 128B). Aurica puxando assunto sobre a Alameda Hoshinose (ほしのせ通り).",
        "rewritten"
    ),
    25734: (
        "Hã? Ah, sim. E daí?",
        "Lyner sem entender (41B <= 64B).",
        "approved"
    ),
    25735: (
        "A variedade de produtos é péssima, não acha?",
        "Crítica feroz de Aurica ao estoque do armazém (92B <= 120B).",
        "approved"
    ),
    25736: (
        "É péssimo. Eu nem pensaria em comprar nada lá.",
        "Exigência de consumidora de Aurica (96B <= 128B).",
        "approved"
    ),
    25737: (
        "Só vou lá por ser a loja mais perto de casa, mas é bem irritante.",
        "Resolução de estouro (200B -> 134B <= 176B). Aurica reclamando da falta de opções práticas perto de casa.",
        "rewritten"
    ),
    25738: (
        "É mesmo...? Então não vou esperar grande coisa quando for lá.",
        "Resolução de estouro (191B -> 127B <= 152B). Lyner ajustando suas expectativas.",
        "rewritten"
    ),
    25739: (
        "(Pra mim, parecia uma lojinha bem normal...)",
        "Resolução de estouro (108B -> 89B <= 104B). Pensamento sincero de Lyner sobre lojas comuns.",
        "rewritten"
    ),
    25740: (
        "Diz aí... você gostou da comida que fiz?",
        "Resolução de estouro (119B -> 83B <= 88B). Aurica perguntando sobre seus dotes culinários.",
        "rewritten"
    )
}

if __name__ == "__main__":
    assert len(batch6_curated) == 40, f"Esperado 40, obtido {len(batch6_curated)}"
    errs = []
    for did, (text, rat, verd) in batch6_curated.items():
        lim = limits[str(did)]
        enc = encoded_size(text)
        if enc > lim:
            errs.append(f"ID {did}: enc {enc}B > limit {lim}B (+{enc - lim})")
        v_errs = validate_line(did, "", text)
        if v_errs:
            errs.append(f"ID {did} validação: {v_errs}")

    if errs:
        print(f"Erros em Batch 6 ({len(errs)}):")
        for e in errs:
            print(" ", e)
        sys.exit(1)
    else:
        print("Batch 6: 100% OK! 40 falas validadas com 0 estouros e 0 erros técnicos.")

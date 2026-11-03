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

# Batch 4: IDs 25621 to 25660 (40 lines)
# Apelidos de Radolf e Misha; a escolha da Igreja vs Tenba na Equipe de Busca;
# Gratidão na Colina Cantante e o medo de Aurica de perder Lyner.
batch4_curated = {
    25621: (
        "É, porque quando o vi pela primeira vez, achei que ele fosse um robô.",
        "Aurica confessando sua primeira impressão sobre Jack (141B <= 144B).",
        "approved"
    ),
    25622: (
        "É... entendo seu ponto.CRPra falar a verdade, eu também me assustei no começo.",
        "Resolução de estouro (199B -> 147B <= 184B). Lyner admitindo surpresa semelhante com CR.",
        "rewritten"
    ),
    25623: (
        "...D-devemos parar?",
        "Aurica hesitante (39B <= 48B).",
        "approved"
    ),
    25624: (
        "...Não, só faltam Radolf e Misha. Vamos continuar.",
        "Lyner incentivando a terminar a lista de membros (103B <= 128B).",
        "approved"
    ),
    25625: (
        "Tá... E pro Radolf...",
        "Resolução de estouro (72B -> 44B <= 56B). Aurica pensando no apelido de Radolf.",
        "rewritten"
    ),
    25626: (
        "...Velhote.",
        "Tradução precisa de '老け顔' (rosto envelhecido / velhote) (23B <= 24B).",
        "approved"
    ),
    25627: (
        "Putz... Mal aí, Radolf, mas não posso negar.",
        "Resolução de estouro (102B -> 86B <= 96B). Lyner rindo da precisão cruel do apelido.",
        "rewritten"
    ),
    25628: (
        "Isso quer dizer que é um bom nome?",
        "Aurica ingênua achando que acertou em cheio (70B <= 72B).",
        "approved"
    ),
    25629: (
        "Descreve bem ele, mas não fala isso na cara dele de jeito nenhum!",
        "Resolução de estouro (208B -> 133B <= 192B). Lyner alertando para a própria segurança deles.",
        "rewritten"
    ),
    25630: (
        "...Eu também achei esse bom.",
        "Aurica chateada que não pode usar o apelido (58B <= 96B).",
        "approved"
    ),
    25631: (
        "Mas vamos dar um nome legal pra Misha, tá?",
        "Resolução de estouro (120B -> 86B <= 104B). Lyner pedindo piedade para Misha.",
        "rewritten"
    ),
    25632: (
        "Sim... mas eu já tenho um perfeito pra ela!",
        "Resolução de estouro (116B -> 86B <= 112B). Aurica animada com sua ideia.",
        "rewritten"
    ),
    25633: (
        "O nome perfeito, né? Qual é?",
        "Lyner curioso (59B <= 72B).",
        "approved"
    ),
    25634: (
        "Garota precoce.",
        "Apelido de Misha ('おませ娘' - garota precoce / que quer bancar a adulta) (31B <= 40B).",
        "approved"
    ),
    25635: (
        "...Isso não é exatamente um apelido...",
        "Lyner desarmado pela constatação pura (79B <= 88B).",
        "approved"
    ),
    25636: (
        "...Eu falei que não queria fazer isso!",
        "Resolução de estouro (95B -> 76B <= 80B). Aurica fazendo biquinho defensivo.",
        "rewritten"
    ),
    25637: (
        "Mas será que foi o certo?",
        "Resolução de estouro (70B -> 52B <= 64B). Aurica mudando o tom para algo sério.",
        "rewritten"
    ),
    25638: (
        "Hm? O que foi?",
        "Resolução de estouro (56B -> 31B <= 48B). Lyner percebendo a mudança de clima.",
        "rewritten"
    ),
    25639: (
        "A Equipe de Busca...CRNão queria mesmo ter ido com eles?",
        "Resolução de estouro (156B -> 106B <= 128B). Aurica perguntando sobre a escolha de rota com CR.",
        "rewritten"
    ),
    25640: (
        "Ah, isso...",
        "Lyner compreendendo a dúvida (23B <= 24B).",
        "approved"
    ),
    25641: (
        "Mesmo que tenha prometido, a situação mudou. Não precisava ir tão longe só para me proteger.",
        "Resolução de estouro (215B -> 188B <= 208B). Aurica ponderando a promessa de proteção.",
        "rewritten"
    ),
    25642: (
        "...Ou será por causa do que eu disse na Reunião?",
        "Resolução de estouro (104B -> 99B <= 104B). Aurica insegura sobre o que falou no Gather.",
        "rewritten"
    ),
    25643: (
        "Não, não é isso.",
        "Lyner negando prontamente (36B <= 40B).",
        "approved"
    ),
    25644: (
        "É que a Igreja realmente me ajudou demais.",
        "Resolução de estouro (106B -> 86B <= 104B). Lyner explicando a dívida de honra com a Igreja.",
        "rewritten"
    ),
    25645: (
        "E você também me socorreu ferido quando caí na Ala de Hórus, Aurica.",
        "Resolução de estouro (200B -> 140B <= 168B). Lyner lembrando do carinho de Aurica ao encontrá-lo.",
        "rewritten"
    ),
    25646: (
        "Mas a Misha tá do outro lado, sabia? Não se preocupa com ela?",
        "Resolução de estouro (159B -> 124B <= 144B). Aurica com ciúmes e preocupação sobre a amiga de infância.",
        "rewritten"
    ),
    25647: (
        "Bem... até me preocupo, mas...",
        "Resolução de estouro (77B -> 65B <= 72B). Honestidade de Lyner.",
        "rewritten"
    ),
    25648: (
        "Se eu tivesse ido com ela, acho que a Misha me diria o mesmo sobre você.",
        "Resolução de estouro (184B -> 147B <= 176B). Lyner equilibrando com carinho as duas donzelas.",
        "rewritten"
    ),
    25649: (
        "Eu escolhi retribuir à Igreja.CRNão me arrependo disso nem um pouco.",
        "Resolução de estouro (231B -> 146B <= 192B). Convencimento resoluto de Lyner com CR.",
        "rewritten"
    ),
    25650: (
        "...Desculpa perguntar isso.",
        "Resolução de estouro (83B -> 55B <= 56B). Aurica pedindo desculpas com ternura.",
        "rewritten"
    ),
    25651: (
        "Tudo bem.",
        "Lyner tranquilo (19B <= 32B).",
        "approved"
    ),
    25652: (
        "A propósito, você me resgatou lá na Colina Cantante.",
        "Lyner relembrando o momento crucial na Colina Cantante (108B <= 120B).",
        "approved"
    ),
    25653: (
        "Se não tivesse tecido aquele Canto por mim, nem sei o que teria sido de mim.",
        "Resolução de estouro (186B -> 154B <= 168B). Agradecimento pelo Canto tecido por Aurica.",
        "rewritten"
    ),
    25654: (
        "Sério...? Mesmo sem mim, você teria dado um jeito.",
        "Resolução de estouro (159B -> 101B <= 136B). Modéstia comovida de Aurica.",
        "rewritten"
    ),
    25655: (
        "E no fim, foi você quem acabou me salvando.",
        "Resolução de estouro (115B -> 87B <= 112B). Aurica destacando a bravura de Lyner.",
        "rewritten"
    ),
    25656: (
        "Bem, tudo deu certo. Conseguimos o cristal e todo mundo saiu ileso. É isso que importa.",
        "Otimismo de Lyner (176B <= 216B).",
        "approved"
    ),
    25657: (
        "Hã? O que foi?",
        "Lyner notando a expressão de Aurica (30B <= 40B).",
        "approved"
    ),
    25658: (
        "...E se você tivesse morrido lá?",
        "Resolução de estouro (102B -> 67B <= 88B). Angústia dolorosa de Aurica.",
        "rewritten"
    ),
    25659: (
        "Se tivesse morrido, como traria o cristal?",
        "Resolução de estouro (147B -> 86B <= 120B). O desespero racionalizado de Aurica.",
        "rewritten"
    ),
    25660: (
        "A missão era crucial, mas quem levaria o cristal a Platina se você morresse?",
        "Resolução de estouro (188B -> 157B <= 176B). Aurica confrontando a imprudência heroica de Lyner.",
        "rewritten"
    )
}

if __name__ == "__main__":
    assert len(batch4_curated) == 40, f"Esperado 40, obtido {len(batch4_curated)}"
    errs = []
    for did, (text, rat, verd) in batch4_curated.items():
        lim = limits[str(did)]
        enc = encoded_size(text)
        if enc > lim:
            errs.append(f"ID {did}: enc {enc}B > limit {lim}B (+{enc - lim})")
        v_errs = validate_line(did, "", text)
        if v_errs:
            errs.append(f"ID {did} validação: {v_errs}")

    if errs:
        print(f"Erros em Batch 4 ({len(errs)}):")
        for e in errs:
            print(" ", e)
        sys.exit(1)
    else:
        print("Batch 4: 100% OK! 40 falas validadas com 0 estouros e 0 erros técnicos.")

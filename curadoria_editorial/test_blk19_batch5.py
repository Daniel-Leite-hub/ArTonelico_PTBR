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

# Batch 5: IDs 25661 to 25700 (40 lines)
# Devolução do lenço de Aurica; Insegurança da Cosmosfera e ternura de Lyner;
# Comparativo de medos (altura x escuro); Fascínio pela Fancy Shop.
batch5_curated = {
    25661: (
        "Ah...",
        "Hesitação reflexiva de Aurica (11B <= 16B).",
        "approved"
    ),
    25662: (
        "Além disso, não dá garantia de que conseguirei tecer um Canto se algo acontecer de novo...",
        "Aurica expressando a fragilidade e incerteza de seu poder musical (175B <= 192B).",
        "approved"
    ),
    25663: (
        "...Queria que se cuidasse mais.",
        "Resolução de estouro (86B -> 63B <= 80B). Súplica afetuosa de Aurica para Lyner preservar a própria vida.",
        "rewritten"
    ),
    25664: (
        "D-desculpa falar assim sem saber de nada...",
        "Resolução de estouro (91B -> 87B <= 88B). Aurica tímida se desculpando pela intromissão.",
        "rewritten"
    ),
    25665: (
        "Ah, quase esqueci de te devolver isto.",
        "Resolução de estouro (90B -> 77B <= 88B). Lyner puxando o lenço do bolso.",
        "rewritten"
    ),
    25666: (
        "Hã? Ah, esse lenço...",
        "Aurica reconhecendo o objeto pessoal (45B <= 64B).",
        "approved"
    ),
    25667: (
        "Como você não o levou antes, ele ficou comigo esse tempo todo. Só me lembrei dele agora.",
        "Lyner explicando por que guardou o lenço de Aurica (180B <= 184B).",
        "approved"
    ),
    25668: (
        "D-desculpa... Naquele dia fingi que nem te conhecia...",
        "Resolução de estouro (127B -> 109B <= 112B). Aurica envergonhada por sua frieza no primeiro encontro.",
        "rewritten"
    ),
    25669: (
        "Não esquenta. Você me ajudou, e sou grato por isso.",
        "Resolução de estouro (118B -> 105B <= 112B). Cavalheirismo acolhedor de Lyner.",
        "rewritten"
    ),
    25670: (
        "Mas esse é o seu lenço, certo?",
        "Confirmação carinhosa (63B <= 80B).",
        "approved"
    ),
    25671: (
        "...Sim. Obrigada por guardar com tanto carinho.",
        "Resolução de estouro (111B -> 95B <= 96B). Gratidão sussurrada e emocionada de Aurica.",
        "rewritten"
    ),
    25672: (
        "Eu é que devo te agradecer.",
        "Resolução de estouro (75B -> 56B <= 72B). Modéstia de Lyner.",
        "rewritten"
    ),
    25673: (
        "E olha... me desculpa.",
        "Resolução de estouro (52B -> 45B <= 48B). Aurica introduzindo o assunto da Cosmosfera.",
        "rewritten"
    ),
    25674: (
        "Hã? Por que tá se desculpando?",
        "Resolução de estouro (78B -> 63B <= 64B). Lyner pego de surpresa.",
        "rewritten"
    ),
    25675: (
        "Minha Cosmosfera era estranha. Devo ter te dado mais trabalho...",
        "Insegurança profunda de Aurica sobre o caos de seu mundo mental (129B <= 144B).",
        "approved"
    ),
    25676: (
        "Que nada.",
        "Resolução de estouro (64B -> 19B <= 32B). Negação imediata e reconfortante de Lyner ('そんなことないって').",
        "rewritten"
    ),
    25677: (
        "Tudo bem. Sei que meu mundo mental é estranho.",
        "Resolução de estouro (105B -> 94B <= 96B). Aurica conformada e vulnerável.",
        "rewritten"
    ),
    25678: (
        "Como pode dizer isso se você mesma nunca esteve lá?",
        "Resolução de estouro (139B -> 105B <= 136B). Raciocínio de Lyner para animá-la.",
        "rewritten"
    ),
    25679: (
        "É parte de mim, eu sei bem.CRNem eu mesma teria coragem de entrar lá.",
        "Resolução de estouro (95B -> 141B <= 152B). Restauração da fala comovente de Aurica sobre ter medo do próprio íntimo com CR.",
        "rewritten"
    ),
    25680: (
        "O que você acha? Como era minha Cosmosfera?",
        "Curiosidade e medo da avaliação de Lyner (91B <= 104B).",
        "approved"
    ),
    25681: (
        "...É um lugar onde eu gostaria de voltar sempre.",
        "Declaração terna de Lyner, valorizando o íntimo de Aurica (98B <= 112B).",
        "approved"
    ),
    25682: (
        "...Sério?",
        "Surpresa corada de Aurica (19B <= 24B).",
        "approved"
    ),
    25683: (
        "Mas se você não quiser, acho que não vou mais lá.",
        "Respeito absoluto de Lyner pelo consentimento de Aurica (101B <= 120B).",
        "approved"
    ),
    25684: (
        "...Você é estranho.CRMas pode entrar lá de novo...",
        "Resolução de estouro (109B -> 104B <= 104B). Aurica disfarçando a timidez com biquinho e dando permissão para o Mergulho com CR.",
        "rewritten"
    ),
    25685: (
        "S-sério?",
        "Lyner animado (17B <= 24B).",
        "approved"
    ),
    25686: (
        "Sim... mas...",
        "Hesitação tímida de Aurica (27B <= 32B).",
        "approved"
    ),
    25687: (
        "Se você não se importa, Lyner... por mim pode mergulhar.",
        "Resolução de estouro (191B -> 115B <= 120B). Permissão formal e doce para mergulhar em sua psique.",
        "rewritten"
    ),
    25688: (
        "Aurica, você não tem medo de altura nem do escuro?",
        "Resolução de estouro (137B -> 103B <= 120B). Lyner mudando de assunto para medos cotidianos.",
        "rewritten"
    ),
    25689: (
        "Por quê?",
        "Resolução de estouro (27B -> 18B <= 24B). Aurica curiosa com a pergunta.",
        "rewritten"
    ),
    25690: (
        "Bem, como a Misha tem medo de altura, fiquei me perguntando se você também tinha.",
        "Lyner comparando as fobias das garotas (165B <= 168B).",
        "approved"
    ),
    25691: (
        "Até eu fiquei meio assustado na Colina Cantante.",
        "Resolução de estouro (134B -> 98B <= 112B). Lyner admitindo vertigem.",
        "rewritten"
    ),
    25692: (
        "...Não gosto muito delas, mas não tenho medo, acho...",
        "Aurica avaliando sua coragem (109B <= 120B).",
        "approved"
    ),
    25693: (
        "Eu nunca tive medo do escuro... nem de alturas...",
        "Aurica explicando suas reações (99B <= 112B).",
        "approved"
    ),
    25694: (
        "...Nada se compara a quando caímos da aeronave.",
        "Resolução de estouro (133B -> 96B <= 128B). O ponto de referência de terror extremo de Aurica.",
        "rewritten"
    ),
    25695: (
        "Ah... bem, acho que nada se compara a isso.",
        "Lyner concordando rindo de nervoso (87B <= 88B).",
        "approved"
    ),
    25696: (
        "Quem sabe a Misha não se cura se despencar uma vez?",
        "Resolução de estouro (128B -> 104B <= 112B). Sugestão cômica e implacável de terapia de choque de Aurica.",
        "rewritten"
    ),
    25697: (
        "Pode só piorar as coisas. E não dá pra arriscar uma queda...",
        "Lyner zelando pela integridade física de Misha (124B <= 136B).",
        "approved"
    ),
    25698: (
        "Aquela loja, digo, a Fancy Shop, tinha tanta coisa fofa! Foi muito divertido.",
        "Resolução de estouro (213B -> 155B <= 176B). Aurica se empolgando com a loja chique de Platina.",
        "rewritten"
    ),
    25699: (
        "Sério? Bem, eu entendo a parte do “fofo”, mas...",
        "Lyner achando graça do entusiasmo feminino (98B <= 104B).",
        "approved"
    ),
    25700: (
        "Você não acha divertido só de olhar para essas coisas?",
        "Aurica tentando convencer Lyner do prazer das vitrines (112B <= 112B).",
        "approved"
    )
}

if __name__ == "__main__":
    assert len(batch5_curated) == 40, f"Esperado 40, obtido {len(batch5_curated)}"
    errs = []
    for did, (text, rat, verd) in batch5_curated.items():
        lim = limits[str(did)]
        enc = encoded_size(text)
        if enc > lim:
            errs.append(f"ID {did}: enc {enc}B > limit {lim}B (+{enc - lim})")
        v_errs = validate_line(did, "", text)
        if v_errs:
            errs.append(f"ID {did} validação: {v_errs}")

    if errs:
        print(f"Erros em Batch 5 ({len(errs)}):")
        for e in errs:
            print(" ", e)
        sys.exit(1)
    else:
        print("Batch 5: 100% OK! 40 falas validadas com 0 estouros e 0 erros técnicos.")

import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cands = {
    29025: (136, "A Deusa da Torre está furiosa... Misericórdia, misericórdia..."),
    29026: (120, "Uff... Parece que a fúria da Deusa ainda não se acalmou."),
    29027: (112, "A Deusa guardiã nos perdoou. Que grande bênção..."),
    29028: (120, "Ei, ei! Não entrem na plantação, isso me prejudica!"),
    29029: (168, "Viu aquele frango ali? Vou assar ele no churrasco hoje à noite. Que tal?"),
    29030: (176, "Agora há pouco subiu um batalhão da Igreja. O que pretendem aprontar?"),
    29031: (128, "Vocês vêm direto aqui ultimamente. Tem algo lá em cima?"),
    29032: (168, "Pode até ser perigoso aqui, mas vivo há tanto tempo que não quero sair..."),
    29033: (64, "Agora viveremos em paz de novo."),
    29034: (24, "Cocoricó!"),
    29035: (80, "Mora gente acima do céu, né?"),
    29036: (184, "Fico achando que estou olhando a sola dos pés deles.CRNão gosto muito disso..."),
    29037: (144, "Ouvi um montão de passos há pouco. Pareciam estar subindo..."),
    29038: (112, "Ficou calmo de novo.CRAgora posso olhar o céu em paz."),
    29039: (152, "Ah, que calor... Moramos tão alto, por que faz tanto calor aqui...?"),
    29040: (144, "Que houve? O pessoal da Igreja vai armar uma guerra lá em cima?"),
    29041: (152, "Não consigo aguentar esse calor. Talvez eu suba um pouquinho mais..."),
    29042: (192, "Achei que estaria fresco na torre, mas quase fui atacado por um Guardião..."),
    29043: (56, "Mas lá era bem mais fresco."),
    29044: (176, "Os guardiões voltaram ao normal. Agora posso me refrescar na torre à vontade."),
    29045: (56, "Có, có, có, có, có..."),
    29046: (56, "Assim meu filho cresce..."),
    29047: (104, "Pessoas da Igreja? Muitas subiram lá em cima."),
    29048: (96, "Afinal, o que o pessoal da Igreja queria?"),
}

all_ok = True
for did, (cap, text) in cands.items():
    sz = encoded_size(text)
    diff = cap - sz if sz is not None else -999
    errs = validate_line(did, "", text)
    if diff < 0 or errs:
        all_ok = False
        print(f"FAIL [{did}] cap={cap} sz={sz} diff={diff} errs={errs} -> {text}")
    else:
        print(f"OK [{did}] {sz}/{cap}B (sobra {diff}B) -> {text}")

print("0378 ALL OK?", all_ok)

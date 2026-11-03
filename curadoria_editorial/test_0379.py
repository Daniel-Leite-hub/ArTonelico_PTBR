import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cands = {
    29049: (112, "Parece que muita coisa aconteceu no Mundo Inferior."),
    29050: (120, "Decidi descer ao Mundo Inferior algum dia, pelo meu filho."),
    29051: (56, "Meu filho tem que aprender."),
    29052: (144, "Vocês vão subir por aqui? Acho que não vai adiantar nada..."),
    29053: (160, "Não sei o que vai começar, mas acho melhor me abrigar em casa..."),
    29054: (136, "Aqui ficou perigoso ultimamente. Talvez eu deva me mudar..."),
    29055: (96, "Se nada acontecer, talvez seja até melhor..."),
    29056: (32, "Cocoricó!"),
    29057: (80, "Hm? Vocês vão subir por aqui?"),
    29058: (120, "Melhor não irem. Mesmo que subam, não dá em lugar nenhum."),
    29059: (96, "Tanto calor e eles de uniforme? Francamente..."),
    29060: (120, "Você sobe e desce muito por aqui, mas não sente calor?"),
    29061: (120, "De tanto reclamar do calor, até acabei me acostumando."),
    29062: (96, "Ah? Vocês vão subir agora? Eu acabei de descer."),
    29063: (128, "Achei que dava para subir, mas me mandaram de volta..."),
    29064: (120, "Quem subiu agora há pouco disse que ia abrir o portão."),
    29065: (96, "Sinceramente, pensei em ir junto, mas..."),
    29066: (72, "Disseram que o portão ali abriu..."),
    29067: (96, "...Será que tento subir lá de novo?"),
    29068: (176, "O céu... está mais escuro do que o normal. O que estará havendo lá em cima?"),
    29069: (112, "O céu voltou ao normal. Está sereno como de costume."),
    29070: (152, "Sou Solius da Tempestade. Apareço com a tempestade e sumo com ela..."),
    29071: (104, "Uma grande tempestade varre este mundo agora."),
    29072: (112, "Eu vejo tudo.CRDeste mirante, enxergo o mundo inteiro..."),
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

print("0379 ALL OK?", all_ok)

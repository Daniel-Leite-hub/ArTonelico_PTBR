import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cands = {
    29145: (128, "Se souber como, poderia congelar a água daquele copo?"),
    29146: (128, "Incrível... Congelou mesmo! Ficou tão frio e lindo..."),
    29147: (136, "Obrigada por me mostrar. Agora pode fazer o que quiser com ele."),
    29148: (72, "Se quiser, pode levar com você."),
    29149: (112, "Nossa, estou num apuro! Ganhei frutas demais da conta."),
    29150: (112, "Mas nem eu e o Cococó damos conta de comer tudo isso."),
    29151: (48, "Có, có, có..."),
    29152: (104, "Será que dá para conservar essas frutas?"),
    29153: (128, "Nossa! Que frutas secas lindas você fez aí!"),
    29154: (64, "Rapaz, estou impressionada!"),
    29155: (32, "...Hum, sim."),
    29156: (96, "Agora vai durar.CRAceite um pouco de brinde!"),
    29157: (88, "Se quiser, pegue um pouco das frutas secas."),
    29158: (32, "Porto Gaivota"),
    29159: (40, "Ruínas do Subsolo"),
    29160: (24, "Rua Central"),
    29161: (32, "Reator Central"),
    29162: (32, "Pous. Fu-Rai-Bo"),
    29163: (48, "Loja Geral de Karulu"),
    29164: (32, "Mergulho Nemo"),
    29165: (40, "Mergulho Vagalume"),
    29166: (40, "Mergulho Platina"),
    29167: (32, "Dirigível Tenba"),
    29168: (32, "Nave da Igreja"),
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

print("0383 ALL OK?", all_ok)

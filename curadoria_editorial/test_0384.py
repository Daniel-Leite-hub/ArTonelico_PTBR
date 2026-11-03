import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cands = {
    29169: (32, "Barca Krusche"),
    29170: (48, "Encosta do Cais"),
    29171: (24, "Pq. Karulu"),
    29172: (32, "Câmara Elemia"),
    29173: (40, "Feira Livre Karulu"),
    29174: (32, "Igreja Elemia"),
    29175: (32, "Pq. Cantapedra"),
    29176: (48, "Pq. Cantapedra: Noite"),
    29177: (32, "Av. Hoshinose"),
    29178: (40, "[Lua Cantante]"),
    29179: (24, "Ponte Aérea"),
    29180: (24, "Pous. Torre"),
    29181: (32, "Casa da Aurica"),
    29182: (24, "Entrada"),
    29183: (40, "Sala da Presidente"),
    29184: (40, "Oficina Reyvateil"),
    29185: (40, "Casa de Garzburn"),
    29186: (24, "P. Pheyna"),
    29187: (24, "Magecure"),
    29188: (32, "Pous. Restoire"),
    29189: (32, "Grande Templo"),
    29190: (32, "Ninho do Dragão"),
    29191: (32, "Sala das Chaves"),
    29192: (40, "Controle Climático"),
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

print("0384 ALL OK?", all_ok)

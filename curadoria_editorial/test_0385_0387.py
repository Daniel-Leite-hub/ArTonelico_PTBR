import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

test_map = [
    # 0385
    (29193, 24, "Apsaranika"),
    (29194, 24, "O Gather"),
    (29195, 40, "Loja de Departam."),
    (29196, 32, "Pous. [Linkage]"),
    (29197, 40, "Altar dos Apóstolos"),
    (29198, 24, "Mirante"),
    (29199, 24, "Rinkernator"),
    (29200, 24, "Catedral"),
    (29201, 40, "Crônica Crescente"),
    (29202, 32, "Colina Canto 1F"),
    (29203, 32, "Colina Canto S1"),
    (29204, 32, "Colina Canto S2"),
    (29205, 32, "Colina Canto S3"),
    (29206, 32, "Colina Canto S4"),
    (29207, 40, "Silvaplate Setor L"),
    (29208, 40, "Túnel Inf. Silva"),
    (29209, 40, "Silvaplate Setor M"),
    (29210, 40, "Túnel Sup. Silva"),
    (29211, 48, "Silva U - Portão D"),
    (29212, 40, "Silvaplate Setor U"),
    (29213, 40, "Placa Íons Setor L"),
    (29214, 40, "Túnel Inferior Ion"),
    (29215, 40, "Placa Íons Nuvens"),
    (29216, 40, "Túnel Superior Ion"),

    # 0386
    (29217, 40, "Túnel Sup. Ion P-D"),
    (29218, 16, "Inferia"),
    (29219, 40, "Blastplate Setor L"),
    (29220, 40, "Túnel Inf. Blast"),
    (29221, 40, "Blastplate Setor M"),
    (29222, 40, "Túnel Sup. Blast"),
    (29223, 40, "Blastplate Setor U"),
    (29224, 24, "Templo 1F"),
    (29225, 24, "Templo 2F"),
    (29226, 24, "Sala Templo"),
    (29227, 32, "Sala do Fundo"),
    (29228, 24, "Templo 3F"),
    (29229, 32, "Sala Ornamentos"),
    (29230, 32, "Floresta D-Nest"),
    (29231, 40, "Duto Silver Horn"),
    (29232, 40, "Píer Silver Horn"),
    (29233, 40, "Silver Horn Sup. A"),
    (29234, 40, "Silver Horn Sup. B"),
    (29235, 40, "Silver Horn Sup. C"),
    (29236, 40, "Silver Horn Inf. A"),
    (29237, 40, "Silver Horn Inf. B"),
    (29238, 40, "Silver Horn Inf. C"),
    (29239, 48, "Silver Horn Fuga A"),
    (29240, 48, "Silver Horn Fuga B"),

    # 0387
    (29241, 48, "Silver Horn Fuga C"),
    (29242, 48, "Duto Mestre Silver Horn"),
    (29243, 32, "Ala da Princesa"),
    (29244, 40, "Duto Silver Horn A"),
    (29245, 40, "Duto Silver Horn B"),
    (29246, 40, "Duto Silver Horn C"),
    (29247, 24, "Veronica"),
    (29248, 40, "FPG [Base Terrena]"),
    (29249, 32, "FPG [Rota Rato]"),
    (29250, 40, "FPG [Dep. Fundos]"),
    (29251, 32, "FPG [Duto Ar]"),
    (29252, 32, "FPG [Pista C]"),
    (29253, 40, "FPG [Entrada C]"),
    (29254, 24, "Tubulação"),
    (29255, 40, "FPG [Viga Inferior]"),
    (29256, 32, "FPG [Reator]"),
    (29257, 40, "FPG [Controle]"),
    (29258, 32, "FPG [Segurança]"),
    (29259, 48, "Tenba Lab [3º Segredo]"),
    (29260, 48, "Tenba Lab [2º Segredo]"),
    (29261, 32, "Tenba Lab 2F"),
    (29262, 32, "Tenba Lab 1F"),
    (29263, 32, "Tenba Tower B1"),
    (29264, 32, "Tenba Tower B2"),
]

all_ok = True
for did, cap, text in test_map:
    sz = encoded_size(text)
    diff = cap - sz if sz is not None else -999
    errs = validate_line(did, "", text)
    if diff < 0 or errs:
        all_ok = False
        print(f"FAIL [{did}] cap={cap} sz={sz} diff={diff} errs={errs} -> {text}")
    else:
        print(f"OK [{did}] {sz}/{cap}B (sobra {diff}B) -> {text}")

print("0385-0387 ALL OK?", all_ok)

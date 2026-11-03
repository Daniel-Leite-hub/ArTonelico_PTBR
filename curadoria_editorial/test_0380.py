import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cands = {
    29073: (120, "Nossa! Subiram um bocado, hein? Fico impressionada!"),
    29074: (88, "Nossa! Tem vindo tanta gente por aqui."),
    29075: (144, "Opa, aconteceu algo? Não fico sabendo muito das coisas do mundo."),
    29076: (120, "Será que eu devia prestar mais atenção nas notícias?"),
    29077: (24, "Cocoricó!"),
    29078: (176, "Mesmo subindo o Silvaplate, só vão dar de cara com o Portão Pheyna fechado."),
    29079: (144, "A Tribo Teru do portão não deixa o povo daqui subir ao Mundo Superior."),
    29080: (128, "Não adianta nada continuar subindo. Melhor darem meia-volta."),
    29081: (136, "Vão deter o pessoal da Igreja? Então é bom se apressarem."),
    29082: (128, "Mas eles são muitos. Vocês dão conta disso sozinhos?"),
    29083: (104, "Dizem que o Portão Pheyna abriu recentemente."),
    29084: (88, "Talvez eu cruze aquele portão algum dia..."),
    29085: (96, "Queria ser mais amiga do pessoal da Tribo Teru."),
    29086: (120, "E aprender com eles várias coisas que ainda não sei."),
    29087: (88, "Tava gostoso... mas ainda fico triste."),
    29088: (72, "Veio um monte de gente assustadora."),
    29089: (96, "O que tem lá em cima? Eu nunca fui lá."),
    29090: (64, "Bem-vindos à Igreja de Elemia."),
    29091: (96, "Os sacerdotes foram purificar os hereges."),
    29092: (112, "No fim, éramos apenas fantoches do Bispo Falss..."),
    29093: (88, "O bispo atual da igreja é o Sir Radolf."),
    29094: (88, "O senhor bispo acabou de sair."),
    29095: (120, "Continuaremos nos dedicando a esta cidade e a seu povo!"),
    29096: (80, "A viagem será longa, cuidem-se..."),
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

print("0380 ALL OK?", all_ok)

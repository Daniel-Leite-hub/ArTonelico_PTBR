import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cands = {
    29097: (64, "Confio este mundo... a vocês."),
    29098: (152, "Fazer coisas erradasCRnão compensa...CRVou voltar pro interior..."),
    29099: (120, "A patroa saiu agora. Por favor, volte daqui a pouco."),
    29100: (48, "...Estarei esperando..."),
    29101: (56, "...Voltem sãos e salvos!"),
    29102: (40, "Podem passar."),
    29103: (176, "Procuro materiais que possam ajudar no avanço tecnológico da Tenba."),
    29104: (104, "Esta instalação está isolada. Queiram se retirar."),
    29105: (152, "Então é assim a estrutura da Torre. Vale muito a pena pesquisar!"),
    29106: (96, "Ah, Chefe Krusche! A presidente está fora."),
    29107: (88, "Estamos investigando este setor no momento."),
    29108: (104, "Pararam o Ikaruga aprimorado... Impressionante."),
    29109: (96, "Chefe Krusche, tudo corre muito bem por aqui!"),
    29110: (136, "Na Tenba, pesquisamos para pôr essa tecnologia a serviço de todos."),
    29111: (152, "Ao enriquecer a vida do povo, a Tenba recebe apoio e cresce junto."),
    29112: (136, "Ou seja, a Tenba e as pessoas formam um único e grande círculo."),
    29113: (160, "A tecnologia da Torre é formidável. Quando analisarmos os dados..."),
    29114: (56, "Dará para aproveitar bem."),
    29115: (128, "Concluir este projeto até amanhã é um absurdo sem tamanho..."),
    29116: (144, "Com tantos dados coletados, vai ser difícil redigir o relatório..."),
    29117: (168, "No Ikaruga III... precisaremos pôr defesa contra controle remoto."),
    29118: (88, "Retomaremos a busca assim que tudo acalmar."),
    29119: (152, "Meu sonho é criar uma rota aérea daqui até as Asas de Hórus."),
    29120: (120, "...Atualizando combate... Enviando dados de batalha..."),
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

print("0381 ALL OK?", all_ok)

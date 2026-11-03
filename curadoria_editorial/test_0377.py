import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cands = {
    29001: (120, "Não sei como foi resolvido, mas agora está tudo ótimo."),
    29002: (128, "Já conheceu o novo bispo? Se não, devia ir falar com ele."),
    29003: (168, "A fama da Claire como cantora se espalhou, e os clientes aumentaram."),
    29004: (136, "Vem clientes até da Vila de Karulu e do Beco Vagalume."),
    29005: (168, "Esta pousada é tão elegante, né? Dá até vontadeCRde se hospedar aqui."),
    29006: (120, "Ainda bem que fiquei aqui... Minha casa ficou em ruínas."),
    29007: (120, "Consertaram a casa, mas... este lugar é bem mais cômodo."),
    29008: (104, "Meu bairro é perigoso, então acabei de voltar."),
    29009: (160, "Com a paz de volta, penso em viajar até o Mundo Inferior."),
    29010: (128, "Em Platina só se fala da bela cantora na cidade de Nemo."),
    29011: (24, "Grmiau..."),
    29012: (128, "Tô ocupado agora.CRVá logo dominar o Grathmeld com o velho."),
    29013: (184, "Perdão, senhorita. Que interrupção tola. Aliás, aceita jantar comigo hoje...?"),
    29014: (16, "Céus..."),
    29015: (48, "Cuidado, Lyner..."),
    29016: (120, "Deu vontade de comer churrasco... Hoje tem carne assada!"),
    29017: (144, "O que você está dizendo? Comemos churrasco ontem e anteontem..."),
    29018: (64, "Comida de homem é bem difícil."),
    29019: (64, "Foi uma tempestade bem forte."),
    29020: (160, "Parece que algo aconteceu na Torre. Será que esta área está bem..."),
    29021: (160, "O céu está agitado ultimamente. Será que algo grande vai acontecer de novo?"),
    29022: (72, "Entendi o segredo do churrasco!"),
    29023: (88, "Ah? É raro ver jovens vindo até aqui."),
    29024: (128, "Vivo há muitos anos, mas nunca vi tempestade tão forte."),
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

print("0377 ALL OK?", all_ok)

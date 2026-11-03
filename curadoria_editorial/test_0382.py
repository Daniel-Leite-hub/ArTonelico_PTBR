import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cands = {
    29121: (120, "...Analisando código. Aguarde até o término do envio..."),
    29122: (24, "...Zzz zzz."),
    29123: (40, "Está... dormindo?"),
    29124: (48, "Lyner, cuidado...!"),
    29125: (128, "Puxa, que problema. Quero fazer churrasco, mas o fogo apagou."),
    29126: (200, "Se alguma boa alma acendesse o fogo, seria ótimo... Ai, que dilema."),
    29127: (160, "Oh! A carne assou! Não sei quem foi, mas agradeço de coração!"),
    29128: (104, "Em agradecimento, por favor, sirva-se também."),
    29129: (120, "Nossa, o frango abatido ontem ficou bom demais da conta."),
    29130: (40, "É, entendi... Haha."),
    29131: (144, "Criamos o frango para comer, mas meu filho se apegou a ele."),
    29132: (176, "Na hora de acender o fogo, ele abriu o berreiro... e não pude acender."),
    29133: (72, "Oh... Você acendeu o fogo para mim."),
    29134: (128, "Muito obrigado. Assim meu filho não vai guardar rancor de mim."),
    29135: (168, "Esse gosto amargo será inesquecível para o meu filho. Aceite um pouco."),
    29136: (72, "Snif... Meu frango virou carne!"),
    29137: (120, "Snif... Ué... Que cheirinho bom... Tá tão apetitoso!"),
    29138: (112, "...Vou comer! O franguinho não pode ter morrido à toa!"),
    29139: (144, "Tento fazer peixe seco com mirin, mas não consigo secar direito."),
    29140: (80, "Se desse para criar um vendaval..."),
    29141: (120, "I-isso é...!? Você secou toda a umidade num instante!?"),
    29142: (208, "Hum, era exatamente esse peixe seco que eu buscava! O sabor e o brilho estão perfeitos!"),
    29143: (176, "Nossa, foi maravilhoso ver isso. Fique com um pouco desse peixe seco também."),
    29144: (184, "Dizem que se você congela água, ela vira um troço bem frio chamado 'gelo'..."),
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

print("0382 ALL OK?", all_ok)

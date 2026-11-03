import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

cands = {
    28977: (112, "Após o incidente das deusas, a Igreja trocou de bispo."),
    28978: (136, "A Igreja de agora ajuda o povo da cidade, o que é ótimo."),
    28979: (120, "O bispo é bem atraente...CRFiquei até interessada."),
    28980: (48, "Ah... senhor bispo..."),
    28981: (136, "Ei! Estamos num encontro, dá para fazer silêncio?"),
    28982: (184, "Só rezo para a tempestade não atingir aqui. Se não, adeus encontros."),
    28983: (128, "Agora posso namorar todo dia sem preocupação! Hahaha!"),
    28984: (144, "Descida da Deusa? Só me importo com ela, o resto não me interessa."),
    28985: (120, "Hã? Não houve nada no final das contas? Que alarde à toa."),
    28986: (136, "Hã, um bispo novo? Não sei dizer, nunca sequer fui à igreja."),
    28987: (152, "Humpf, o que o bispo novo tem demais? Eu sou bem mais bonito!"),
    28988: (160, "Ela só tem olhos pro bispo ultimamente. Assim tô perdido... Ai, ai..."),
    28989: (128, "Hã? Ah! Não me assuste! ...Estava rolando um clima..."),
    28990: (128, "Uau! Ei! O clima tá bom, não venha atrapalhar agora!"),
    28991: (80, "Aquele gato ali está me encarando..."),
    28992: (16, "Miau?"),
    28993: (24, "Fumiau..."),
    28994: (152, "Vale a pena ouvir o canto da Claire. Devia escutar ao menos uma vez."),
    28995: (144, "Quem ficou preso pela tempestade veio correndo para a estalagem."),
    28996: (112, "Tem muita gente aqui, mas você também pode ficar."),
    28997: (144, "Quem não pode voltar por causa da tempestade está lotando a pousada."),
    28998: (96, "Passada a tempestade, todos foram logo embora."),
    28999: (48, "A pousada esvaziou."),
    29000: (152, "Herege ou não, acho um absurdo ficar brandindo armas desse jeito..."),
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

print("0376 ALL OK?", all_ok)

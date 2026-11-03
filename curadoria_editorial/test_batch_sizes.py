import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = [
    (24069, "Muito usada em construções. Mas quem em sã consciência carrega vigas de aço por aí...?", 184),
    (24071, "Essencial para máquinas de precisão. É tão miúda que, se você perder, nem percebe.", 176),
    (24073, "Engrenagem grande e maciça. Nem pense em jogar feito frisbee!", 136),
    (24075, "Pedra misteriosa que soa bonito ao ser golpeada. Dá para comprar sem esforço nas lojas.", 192),
    (24079, "O metal especial: Airmetal. Rígido e resistente, mas tão leve que parece ar puro.", 208),
    (24081, "Pedra do memorial na Cauda das Lembranças. Só existe lá... De onde terá vindo?!", 192),
    (24085, "Pelo nome, devia servir para aspirar tudo no passado.", 128),
    (24087, "Placas das paredes da Placa Iônica. Carregar isso nos bolsos é meio sem noção, não acha?", 224),
    (24089, "Estilhaços do Disco Grathnode que flutuam na Blastline, sobre Platina. Bem bonitos.", 176),
    (24091, "Material bem necessário para montar máquinas. Às vezes, também serve para criar armas.", 184),
    (24093, "Peça essencial para criar máquinas. Como já é um mecanismo delicado, manuseie com cautela.", 232),
    (24095, "Como o nome e a cara dizem: uma célula. Se alguém tentar implantar em humanos... Nem pense nisso!", 224),
    (24097, "Dizem que é uma máquina, mas não parece mecanismo à primeira vista...", 160),
    (24099, "Item absurdamente raro. Quando você precisa de um, tem que caçar feito louco, e a chance ainda é mínima.", 256),
    (24101, "Fácil de comprar, mas varia muito de preço conforme a loja. Fique de olho!", 184),
    (24103, "Empréstimo da Senhora Shurelia. Guarda o projeto tridimensional de Purger.", 176),
    (24105, "Lenço que achei onde desmaiei. Acho que pertence àquela garota...", 168),
    (24107, "Pedaço de Yuteria. É um material muito usado em paredes e construções.", 168),
    (24110, "Corda de instrumento feita de Yuteria. Preciso dela para consertar o alaúde da Claire.", 200),
    (24115, "Permite viajar do mundo real ao plano de dados da Torre e voltar. Só que só funciona uma vez.", 216),
    (24117, "Chave para cortar a força do gerador. O estrondo quando a energia cai dá um susto danado.", 208),
    (24119, "Um Cristal Hymmnos. Pensando bem, minha jornada começou na busca por ele.", 176),
    (24123, "Primeira canção de Mir. Ayatane a tocou na Sala da Chave, passando os dados à Misha.", 208),
    (24125, "Cristal Hymmnos roubado pelo ex-Apóstolo de Elemia, Kayel Clancey.", 144),
    (24127, "Se duas mentes dividem um corpo, isto expulsa a intrusa. Será tipo um antivírus?", 232),
    (24239, "Vai, Jack!", 24),
    (24323, "Obrigado!CRDeseja mais alguma coisa?", 80),
]

for d_id, s, cap in tests:
    sz = encoded_size(s)
    diff = sz - cap if sz is not None else "ERROR"
    status = "OK" if sz and sz <= cap else f"OVERFLOW +{diff}B"
    print(f"ID {d_id}: {sz}B / {cap}B -> {status} : {s[:45]}...")

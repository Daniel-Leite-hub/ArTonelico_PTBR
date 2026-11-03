import json
import sys
from pathlib import Path

BASE_DIR = Path("Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "tools"))

from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

with open(BASE_DIR / "curadoria_editorial/limits_blk19.json", "r", encoding="utf-8") as f:
    limits = json.load(f)

# Batch 2: IDs 25551 to 25585 (35 lines)
# Tópicos de acampamento: a garota do gato na estalagem de Nemo (Puffball),
# a monumental Pedra da Canção no Parque de Nemo, sonhos de Grathmeld e introdução à Lata de Canto de Sereia.
batch2_curated = {
    25551: (
        "Sim, conheço. Como sabia?",
        "Resolução de estouro (60B -> 52B <= 56B). Aurica respondendo com naturalidade.",
        "rewritten"
    ),
    25552: (
        "Ela ficou te encarando quando entramos. Só por isso imaginei.",
        "Resolução de estouro (223B -> 124B <= 176B). Lyner explicando como reparou nos olhares.",
        "rewritten"
    ),
    25553: (
        "Nem reparei. Tomara que não esteja brava...",
        "Resolução de estouro (116B -> 88B <= 104B). Aurica preocupada em ter sido indelicada sem querer.",
        "rewritten"
    ),
    25554: (
        "Da próxima vez que formos lá, dá um oi pra ela.",
        "Resolução de estouro (115B -> 98B <= 112B). Conselho prático e amigável de Lyner.",
        "rewritten"
    ),
    25555: (
        "Você brinca muito com ela?",
        "Resolução de estouro (73B -> 54B <= 56B). Curiosidade de Lyner sobre a amizade delas.",
        "rewritten"
    ),
    25556: (
        "Às vezes. Eu dei o nome do gato dela,CRaí a gente virou amiga desde então.",
        "Resolução de estouro (171B -> 146B <= 152B). Aurica explicando o vínculo por batizar o bichano com CR.",
        "rewritten"
    ),
    25557: (
        "Nome? Então foi você quem batizou o gato?",
        "Resolução de estouro (105B -> 85B <= 104B). Lyner surpreso.",
        "rewritten"
    ),
    25558: (
        "Sim. Ela não sabia que nome dar,CRaí ajudei e ficamos amigas.",
        "Resolução de estouro (183B -> 118B <= 160B). Aurica orgulhosa de sua ajuda com CR.",
        "rewritten"
    ),
    25559: (
        "E que nome você colocou?",
        "Resolução de estouro (71B -> 50B <= 56B). Lyner perguntando o nome.",
        "rewritten"
    ),
    25560: (
        "Puffball.",
        "O nome peculiar que Aurica deu ao gato (19B <= 24B).",
        "approved"
    ),
    25561: (
        "...O quê?",
        "Reação perplexa de Lyner (20B <= 24B).",
        "approved"
    ),
    25562: (
        "Puffball, ué! O pelo dele é todo fofinho.",
        "Resolução de estouro (149B -> 84B <= 144B). Aurica justificando a lógica do nome pelo pelo fofo.",
        "rewritten"
    ),
    25563: (
        "P... Puffball, é...?CRPor um instante nem pareceu um nome.",
        "Resolução de estouro (105B -> 116B <= 120B). Lyner achando cômico e estranho com CR.",
        "rewritten"
    ),
    25564: (
        "Pensei em outros nomes também, mas ela gostou mais desse. Quer ouvir os outros?",
        "Aurica toda animada querendo listar suas outras ideias bizarras (160B <= 184B).",
        "approved"
    ),
    25565: (
        "Até queria saber, mas deixa para uma próxima vez.",
        "Resolução de estouro (131B -> 101B <= 120B). Lyner escapando educadamente por medo das ideias.",
        "rewritten"
    ),
    25566: (
        "(Até queria saber, mas dá um certo medo...)",
        "Resolução de estouro (98B -> 88B <= 96B). Monólogo interno cômico de Lyner.",
        "rewritten"
    ),
    25567: (
        "A Pedra da Canção em Nemo é enorme!",
        "Resolução de estouro (86B -> 72B <= 80B). Aurica puxando assunto sobre o marco de Nemo.",
        "rewritten"
    ),
    25568: (
        "Ah, aquela grandona? Dizem que é o símbolo de Nemo, né?",
        "Lyner confirmando o marco da cidade (116B <= 144B).",
        "approved"
    ),
    25569: (
        "Sim. Uma Pedra da Canção assim não se vê todo dia.",
        "Resolução de estouro (197B -> 104B <= 112B). Aurica comentando a raridade.",
        "rewritten"
    ),
    25570: (
        "Verdade. Mesmo se achássemos uma na viagem, não daria para carregar.",
        "Resolução de estouro (188B -> 138B <= 160B). Realismo prático de Lyner.",
        "rewritten"
    ),
    25571: (
        "Pois é... Quantas Pedras da Canção normaisCRseriam necessárias para igualar aquela?",
        "Resolução de estouro (251B -> 171B <= 184B). Aurica calculando o tamanho descomunal com CR.",
        "rewritten"
    ),
    25572: (
        "Hã? Bem... daquele tamanho, com certeza mais de 100.",
        "Resolução de estouro (144B -> 108B <= 136B). Estimativa modesta de Lyner.",
        "rewritten"
    ),
    25573: (
        "Falta uns zeros aí! Ia precisar de muito mais.",
        "Resolução de estouro (132B -> 92B <= 120B). Aurica corrigindo a conta por ordens de grandeza.",
        "rewritten"
    ),
    25574: (
        "Pois é. Como será que ficaria se usássemos a pedra inteira no Grathmeld?",
        "Lyner sonhando alto com a síntese de Grathmeld (148B <= 176B).",
        "approved"
    ),
    25575: (
        "Daquele tamanho, com certeza criaria algo incrível!",
        "Resolução de estouro (148B -> 108B <= 136B). Empolgação de Aurica com o potencial alquímico.",
        "rewritten"
    ),
    25576: (
        "Acho que nem precisaria misturar mais nada para criar algo poderoso.",
        "Lyner imaginando o poder puro do cristal (140B <= 176B).",
        "approved"
    ),
    25577: (
        "Sim! Espada ou Armadura de Pedra da Canção!",
        "Resolução de estouro (151B -> 89B <= 104B). Aurica listando equipamentos lendários imaginários.",
        "rewritten"
    ),
    25578: (
        "Daria pra fazer dez de cada e ainda sobrar...",
        "Resolução de estouro (127B -> 92B <= 120B). Lyner viajando na fartura de materiais.",
        "rewritten"
    ),
    25579: (
        "...Bem, é o monumento da cidade. Melhor não falar uma coisa dessas.",
        "Resolução de estouro (177B -> 139B <= 168B). Lyner caindo na real de que queriam derreter o marco histórico.",
        "rewritten"
    ),
    25580: (
        "É verdade... Afinal, eu moro em Nemo...",
        "Resolução de estouro (105B -> 82B <= 96B). Aurica lembrando que é cidadã local com vergonha cômica.",
        "rewritten"
    ),
    25581: (
        "Ah, sim, preciso te contar uma coisa muito importante.",
        "Transição repentina para um assunto sério e misterioso (109B <= 112B).",
        "approved"
    ),
    25582: (
        "Hã? Algo importante?",
        "Lyner ficando alerta (42B <= 56B).",
        "approved"
    ),
    25583: (
        "Sim... Está com ela? A Lata de Canto de Sereia.",
        "Aurica perguntando pelo item perigoso 'Lata de Canto de Sereia' (人魚のウタ缶) (94B <= 96B).",
        "approved"
    ),
    25584: (
        "Hã? Ah, tá aqui. Deixa ver...",
        "Resolução de estouro (70B -> 61B <= 64B). Lyner procurando o item na sacola.",
        "rewritten"
    ),
    25585: (
        "...Ah, aqui está. Toma.",
        "Lyner entregando a lata sem saber do perigo (48B <= 64B).",
        "approved"
    )
}

if __name__ == "__main__":
    assert len(batch2_curated) == 35, f"Esperado 35, obtido {len(batch2_curated)}"
    errs = []
    for did, (text, rat, verd) in batch2_curated.items():
        lim = limits[str(did)]
        enc = encoded_size(text)
        if enc > lim:
            errs.append(f"ID {did}: enc {enc}B > limit {lim}B (+{enc - lim})")
        v_errs = validate_line(did, "", text)
        if v_errs:
            errs.append(f"ID {did} validação: {v_errs}")

    if errs:
        print(f"Erros em Batch 2 ({len(errs)}):")
        for e in errs:
            print(" ", e)
        sys.exit(1)
    else:
        print("Batch 2: 100% OK! 35 falas validadas com 0 estouros e 0 erros técnicos.")

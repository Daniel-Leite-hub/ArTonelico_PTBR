import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "tools"))

from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line
import sqlite3, json

with open(BASE_DIR / "curadoria_editorial" / "curadoria_config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

conn = sqlite3.connect(cfg["database_path"])
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25426 AND 25465").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

batch6_curated = {
    25426: ("Senhora Shurelia? O que houve?", "Resolução de estouro (76B -> 54B <= 64B). Lyner surpreso.", "rewritten"),
    25427: ("...Nada em especial. Nem sei por quê...", "Shurelia tímida e sem jeito na visita noturna (62B <= 88B).", "rewritten"),
    25428: ("Não tenho assunto em especial... Só vim te visitar.", "Shurelia revelando desejo de ver Lyner (99B <= 128B).", "rewritten"),
    25429: ("Posso ficar aqui um tempinho?...", "Resolução de estouro (110B -> 58B <= 96B). Pedido delicado de Shurelia.", "rewritten"),
    25430: ("Senhora Shurelia? Está feliz?", "Resolução de estouro (74B -> 60B <= 64B). Lyner notando bom humor.", "rewritten"),
    25431: ("É por sua causa, Lyner.", "Shurelia apontando a fonte de sua alegria (41B <= 48B).", "rewritten"),
    25432: ("Minha culpa!? Desculpe!", "Susto cômico e desculpas estabanadas de Lyner (40B <= 48B).", "rewritten"),
    25433: ("Não era pra se desculpar... Mas é bem a sua cara agir assim.", "Resolução de estouro (166B -> 106B <= 160B). Doçura nobre de Shurelia.", "rewritten"),
    25434: ("Lyner... tem um minuto?", "Resolução de estouro (62B -> 45B <= 56B). Pergunta carinhosa de Shurelia.", "rewritten"),
    25435: ("Hehe, sabe por quê?", "Resolução de estouro (111B -> 33B <= 80B). Enigma meigo de Shurelia.", "rewritten"),
    25436: ("Hã? Não sei.", "Lyner sem entender (27B <= 40B).", "rewritten"),
    25437: ("Porque você cuida de mim. Obrigada.", "Gratidão pura e afetuosa de Shurelia (61B <= 80B).", "rewritten"),
    25438: ("Senhora Shurelia?CREstá feliz?", "Resolução de estouro (83B -> 62B <= 72B). Observação atenciosa de Lyner com CR.", "rewritten"),
    25439: ("Acha? Desde a última instalação me sinto ótima!", "Resolução de estouro (148B -> 94B <= 128B). Efeito revigorante do cristal.", "rewritten"),
    25440: ("Você instalou com carinho.", "Resolução de estouro (84B -> 59B <= 72B). Elogio terno de Shurelia ao cuidado de Lyner.", "rewritten"),
    25441: ("Hã? Eu não fiz nada de especial...", "Modéstia de Lyner diante do elogio (54B <= 80B).", "rewritten"),
    25442: ("Faz muita diferença quando quem instala se importa com a Reyvateil.", "Resolução de estouro (182B -> 122B <= 176B). Elo espiritual da instalação.", "rewritten"),
    25443: ("Sim. Me sinto ótima desde que instalou em mim.", "Resolução de estouro (139B -> 81B <= 112B). Bem-estar de Shurelia.", "rewritten"),
    25444: ("Você instala muito bem, Lyner.", "Elogio carinhoso de Shurelia (51B <= 88B).", "rewritten"),
    25445: ("Hã? Não fiz nada de especial...", "Lyner sem jeito (51B <= 88B).", "rewritten"),
    25446: ("Lyner.CRTem um tempinho agora?", "Resolução de estouro (86B -> 57B <= 80B). Shurelia chamando com CR.", "rewritten"),
    25447: ("Senhora Shurelia... Tá cansada?", "Resolução de estouro (91B -> 57B <= 72B). Lyner notando a fadiga.", "rewritten"),
    25448: ("Dá pra notar? É só um pouco, estou bem.", "Resolução de estouro (149B -> 76B <= 144B). Shurelia disfarçando o cansaço.", "rewritten"),
    25449: ("Foi por causa da instalação?", "Resolução de estouro (77B -> 57B <= 64B). Preocupação de Lyner.", "rewritten"),
    25450: ("Em parte sim, mas isso nem cansaço é.", "Resolução de estouro (86B -> 65B <= 80B). Minimização nobre de Shurelia.", "rewritten"),
    25451: ("E assim posso cantar mais forte, não se preocupe.", "Resolução de estouro (182B -> 92B <= 136B). Foco no poder da Magia da Canção.", "rewritten"),
    25452: ("Se diz isso, fico aliviado...", "Resolução de estouro (67B -> 53B <= 64B). Lyner confortado.", "rewritten"),
    25453: ("(Mas preciso ter mais cuidado ao instalar...)", "Pensamento protetor de Lyner (78B <= 96B).", "rewritten"),
    25454: ("Shurelia... Tá meio cansada?", "Resolução de estouro (71B -> 50B <= 64B). Pergunta delicada de Lyner.", "rewritten"),
    25455: ("Tô cansada.", "Resolução de estouro (36B -> 19B <= 32B). Admissão sucinta e meiga de Shurelia.", "rewritten"),
    25456: ("Foi por causa da instalação?", "Resolução de estouro (66B -> 57B <= 64B). Lyner receoso.", "rewritten"),
    25457: ("Sim, mas não é nada. Aguento isso fácil.", "Resolução de estouro (91B -> 67B <= 88B). Firmeza de Shurelia.", "rewritten"),
    25458: ("Assim sinto mais prazer ao cantar.", "Resolução de estouro (122B -> 69B <= 88B). Shurelia valorizando a sensação pós-instalação.", "rewritten"),
    25459: ("Se você diz, fico mais aliviado...", "Resolução de estouro (75B -> 60B <= 72B). Alívio de Lyner.", "rewritten"),
    25460: ("(Mas preciso ter mais cuidado ao instalar...)", "Resolução de estouro (116B -> 78B <= 96B). Resolução interna de Lyner.", "rewritten"),
    25461: ("Aurica!? O que houve!?", "Resolução de estouro (74B -> 41B <= 56B). Espanto de Lyner com a visita noturna.", "rewritten"),
    25462: ("B-bem... deixa pra lá...CRNão quero incomodar...", "Timidez de Aurica quase desistindo com quebra CR (99B <= 112B).", "rewritten"),
    25463: ("Espera! Não atrapalha nada.CRSó estranhei você me visitar por conta própria.", "Resolução de estouro (233B -> 132B <= 192B). Lyner acolhendo Aurica com CR.", "rewritten"),
    25464: ("Pois é...CREu nunca fiz isso antes...", "Hesitação fofa de Aurica com CR (60B <= 96B).", "rewritten"),
    25465: ("Lyner... Obrigada por me salvar quando caí da aeronave.", "Resolução de estouro (173B -> 106B <= 144B). Gratidão emocionante pelo resgate épico.", "rewritten")
}

errors = []
for did, (text, rat, verd) in batch6_curated.items():
    orig_en = next(d["original_en"] for d in input_data["dialogues"] if d["id"] == did)
    limit = limits[did]
    enc = encoded_size(text)
    if enc > limit:
        errors.append(f"OVERFLOW ID {did}: {enc}B > {limit}B (+{enc - limit})")
    val_err = validate_line(did, orig_en, text)
    if val_err:
        errors.append(f"GATE ERR ID {did}: {val_err}")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print(" ", e)
else:
    print("BATCH 6: 100% OK! All 40 lines fit within limits and pass technical gate.")

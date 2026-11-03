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
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25346 AND 25385").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

batch4_curated = {
    25346: ("Posso falar com você um instante?", "Aproximação suave de Misha (68B <= 72B).", "approved"),
    25347: ("Claro, Misha. O que foi?", "Lyner atencioso (49B <= 56B).", "approved"),
    25348: ("Lyner, instalou mesmo em mim?", "Resolução de estouro (90B -> 61B <= 80B). Dúvida ingênua de Misha.", "rewritten"),
    25349: ("Hã? O que quer dizer?", "Resolução de estouro (63B -> 46B <= 56B). Confusão de Lyner.", "rewritten"),
    25350: ("Não senti mudança no corpo.", "Resolução de estouro (83B -> 55B <= 64B). Misha intrigada.", "rewritten"),
    25351: ("...Não ficou só olhando pro meu decote, né!?", "Resolução de estouro (104B -> 92B <= 96B). Provocação cômica de Misha.", "rewritten"),
    25352: ("Fiz bem na sua frente! É coincidência, juro!", "Lyner se defendendo exasperado com juramento (89B <= 152B).", "rewritten"),
    25353: ("Oi, Misha! O que houve?", "Saudação alegre de Lyner (46B <= 48B).", "rewritten"),
    25354: ("Só queria conversar um pouco.", "Resolução de estouro (91B -> 60B <= 72B). Visita afetuosa de Misha.", "rewritten"),
    25355: ("E como ficou após a última instalação?", "Resolução de estouro (92B -> 77B <= 80B). Preocupação de Lyner.", "rewritten"),
    25356: ("Tô ótima, não se preocupe.", "Resolução de estouro (63B -> 52B <= 56B). Misha tranquilizando Lyner.", "rewritten"),
    25357: ("É a prova de que cuidou de mim.CRAté gosto de sentir isso.", "Resolução de estouro (141B -> 116B <= 120B). Confissão carinhosa de Misha com CR.", "rewritten"),
    25358: ("Lyner... tem um minuto?", "Resolução de estouro (58B -> 45B <= 56B). Misha chamando hesitante.", "rewritten"),
    25359: ("Meu corpo tá pesado...CRVim falar com você pra me animar.", "Resolução de estouro (164B -> 113B <= 136B). Misha buscando apoio em Lyner com CR.", "rewritten"),
    25360: ("Pesado?... Exagerei na instalação?", "Lyner preocupado com a sobrecarga de cristais (71B <= 88B).", "rewritten"),
    25361: ("Imagina, tô ótima!CRAté aguentaria receber mais...", "Resolução de estouro (205B -> 101B <= 168B). Bravata fofa de Misha com CR.", "rewritten"),
    25362: ("E se isso ajuda você... vale a pena.", "Misha disposta a se sacrificar por Lyner (73B <= 112B).", "rewritten"),
    25363: ("É mesmo?CRMas chega de instalar por enquanto.", "Cuidado protetor de Lyner com quebra CR (89B <= 128B).", "rewritten"),
    25364: ("(Acho que devia tirar alguns cristais dela...)", "Pensamento responsável de Lyner (89B <= 96B).", "rewritten"),
    25365: ("Lyner.CRTem um momento agora?", "Shurelia formal solicitando audiência com CR (57B <= 64B).", "rewritten"),
    25366: ("Sim. Senhora Shurelia, o que houve?", "Resposta respeitosa de Lyner (70B <= 80B).", "rewritten"),
    25367: ("Minha Magia explodiu na luta passada.", "Resolução de estouro (87B -> 74B <= 80B). Shurelia admitindo falha mágica.", "rewritten"),
    25368: ("Lyner... Como parceiro,CRprecisa dar ordens melhores no canto.", "Resolução de estouro (137B -> 122B <= 128B). Shurelia cobrando melhor regência com CR.", "rewritten"),
    25369: ("Como Cavaleiro de Elemia,CRtenha mais postura. Entendeu?", "Shurelia mantendo a autoridade de Administradora com CR (113B <= 120B).", "rewritten"),
    25370: ("Claro, Senhora Shurelia.", "Lyner acatando prontamente (49B <= 56B).", "approved"),
    25371: ("Minha Magia falhou na luta.", "Resolução de estouro (79B -> 55B <= 72B). Shurelia admitindo o revés.", "rewritten"),
    25372: ("Fiquei sem energia e desperdicei a Magia...", "Resolução de estouro (92B -> 83B <= 88B). Remorso de Shurelia.", "rewritten"),
    25373: ("Vou cuidar melhor, mas você também precisa tomar cuidado.", "Resolução de estouro (160B -> 116B <= 144B). Apelo mútuo de prudência em combate.", "rewritten"),
    25374: ("Pois não, Senhora?", "Resolução de estouro (45B -> 38B <= 40B). Prontidão respeitosa de Lyner.", "rewritten"),
    25375: ("Meu canto anda ótimo porque me dá espaço.", "Elogio de Shurelia ao suporte espaçoso de Lyner (86B <= 104B).", "rewritten"),
    25376: ("Eu não fiz nada. Sua Magia da Canção fica colossal com tempo.", "Lyner modesto elogiando o poder supremo de Shurelia (123B <= 200B).", "rewritten"),
    25377: ("Mantendo esse ritmo, ficarei na minha melhor forma.", "Resolução de estouro (163B -> 101B <= 152B). Shurelia confiante.", "rewritten"),
    25378: ("Entendido.", "Resolução de estouro (35B -> 21B <= 32B). Aquiescência de Lyner.", "rewritten"),
    25379: ("Cantar tão à vontade nas lutas é uma delícia.CRGrata.", "Shurelia agradecendo com doçura e nobreza com CR (102B <= 112B).", "rewritten"),
    25380: ("É meu único talento.", "Lyner humilde (41B <= 56B).", "approved"),
    25381: ("Senhora Shurelia, que foi?", "Pergunta respeitosa de Lyner (53B <= 56B).", "rewritten"),
    25382: ("A luta terminou antes de eu conseguir cantar.", "Resolução de estouro (128B -> 90B <= 120B). Shurelia surpresa.", "rewritten"),
    25383: ("Não imaginei que você ficasse tão forte em tão pouco tempo. Fiquei muito feliz!", "Resolução de estouro (217B -> 157B <= 184B). Elogio caloroso de Shurelia.", "rewritten"),
    25384: ("É mesmo? O inimigo só era fraco.", "Resolução de estouro (113B -> 67B <= 112B). Modéstia de Lyner.", "rewritten"),
    25385: ("Mesmo assim, fiquei contente. Continuo contando com você, Lyner.", "Resolução de estouro (167B -> 126B <= 152B). Vínculo de confiança de Shurelia.", "rewritten")
}

errors = []
for did, (text, rat, verd) in batch4_curated.items():
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
    print("BATCH 4: 100% OK! All 40 lines fit within limits and pass technical gate.")

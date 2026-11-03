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
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25466 AND 25513").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

batch7_curated = {
    25466: ("Ah, aquilo... Só fico feliz por nós dois termos escapado com vida. Foi um milagre!", "Lyner relembrando o resgate aéreo quase milagroso (152B <= 168B).", "rewritten"),
    25467: ("Devemos muito à Krusche. Se qualquer um tivesse agido diferente, aquele milagre não aconteceria.", "Resolução de estouro (233B -> 195B <= 216B). Reconhecimento de Aurica ao trio.", "rewritten"),
    25468: ("Você vai viver muito!", "Resolução de estouro (49B -> 44B <= 48B). Lyner reconfortando Aurica com bom humor ('長生きするぜ').", "rewritten"),
    25469: ("Hum...", "Hesitação de Aurica (13B <= 16B).", "approved"),
    25470: ("Desculpe pelo horário...", "Resolução de estouro (65B -> 50B <= 64B). Aurica tímida.", "rewritten"),
    25471: ("Será que posso voltar outra hora?", "Aurica pedindo para retornar no futuro (67B <= 72B).", "rewritten"),
    25472: ("É tão mais fácil conversar a sós com você...", "Aurica revelando seu conforto emocional com Lyner (89B <= 104B).", "rewritten"),
    25473: ("Claro, venha sempre. Também te procuro se precisar.", "Resolução de estouro (149B -> 104B <= 112B). Hospitalidade carinhosa de Lyner.", "rewritten"),
    25474: ("...Hã?", "Surpresa de Aurica (14B <= 16B).", "approved"),
    25475: ("Se for incômodo, é só me avisar.", "Resolução de estouro (118B -> 68B <= 96B). Lyner respeitando o espaço de Aurica.", "rewritten"),
    25476: ("N-não é isso... Mas já tá tarde, vim só agradecer. Melhor eu ir pro quarto.", "Resolução de estouro (181B -> 156B <= 168B). Despedida afetuosa de Aurica.", "rewritten"),
    25477: ("S-Shurelia!? O que aconteceu?", "Lyner surpreso com a visita solene da Administradora à noite (61B <= 72B).", "rewritten"),
    25478: ("Perdoe-me pelo adiantado da hora. Queria dizer algo a você...", "Shurelia iniciando audiência noturna com nobreza (120B <= 136B).", "rewritten"),
    25479: ("O que foi?", "Lyner solícito (21B <= 24B).", "approved"),
    25480: ("Lyner, sobre ter me reativado... não posso aprovar isso.", "Resolução de estouro (167B -> 114B <= 144B). Repreensão severa de Shurelia.", "rewritten"),
    25481: ("O quê?", "Choque de Lyner (14B <= 16B).", "approved"),
    25482: ("Fiquei feliz na hora, mas...", "Resolução de estouro (84B -> 57B <= 72B). Shurelia reconhecendo a alegria inicial.", "rewritten"),
    25483: ("Ainda acho que me acordar foi um erro.", "Resolução de estouro (82B -> 77B <= 80B). Dilema do despertar de Mir.", "rewritten"),
    25484: ("Mir despertou e o mundo corre grande perigo.", "Consequência apocalíptica da quebra do selo (86B <= 112B).", "rewritten"),
    25485: ("Mas não aceito sacrificar ninguém!", "Resolução de estouro (147B -> 71B <= 120B). Convicção inabalável de Lyner.", "rewritten"),
    25486: ("Lyner...", "Shurelia tocada pela nobreza do cavaleiro (17B <= 24B).", "approved"),
    25487: ("Respeito sua visão, mas foi errado.", "Resolução de estouro (135B -> 72B <= 120B). Firmeza de Shurelia.", "rewritten"),
    25488: ("Tudo bem, assumo total responsabilidade.", "Resolução de estouro (120B -> 81B <= 112B). Determinação heróica de Lyner.", "rewritten"),
    25489: ("O que passou, passou...", "Resolução de estouro (72B -> 47B <= 56B). Shurelia encerrando o debate.", "rewritten"),
    25490: ("Senhora Shurelia...", "Lyner comovido (39B <= 40B).", "rewritten"),
    25491: ("Tudo bem... Eu não devia ser tão dura.", "Resolução de estouro (127B -> 79B <= 104B). Abrandamento de Shurelia.", "rewritten"),
    25492: ("Fiquei feliz quando me disse que sou importante.", "Resolução de estouro (129B -> 97B <= 112B). Shurelia revelando seu coração tocado.", "rewritten"),
    25493: ("Voltarei se houver algo. Até mais.", "Resolução de estouro (76B -> 70B <= 72B). Despedida cerimoniosa de Shurelia.", "rewritten"),
    25494: ("Lyner...CRVim falar com você.", "Início do momento culminante de Shurelia com quebra CR (60B <= 64B).", "rewritten"),
    25495: ("Lyner... posso ser um pouco egoísta?", "Shurelia pedindo timidamente para despir a couraça de Administradora (70B <= 80B).", "rewritten"),
    25496: ("S-sim... claro.", "Consentimento gentil de Lyner (31B <= 40B).", "rewritten"),
    25497: ("Bem...", "Hesitação de Shurelia (13B <= 16B).", "approved"),
    25498: ("Comigo...", "Abertura tímida do coração correspondendo a '私と' (19B <= 24B).", "rewritten"),
    25499: ("Conversar... como amigos.", "Pedido de igualdade e intimidade sem formalidades de Shurelia (51B <= 56B).", "rewritten"),
    25500: ("S-Senhora Shurelia!?CRDo nada...!?", "Resolução de estouro (91B -> 69B <= 88B). Lyner estupefato com CR.", "rewritten"),
    25501: ("Lyner... OuviriaCRo que sinto agora?...", "Resolução de estouro (92B -> 79B <= 88B). Súplica comovente de Shurelia com CR.", "rewritten"),
    25502: ("Eu...", "Shurelia respirando fundo (11B <= 16B).", "approved"),
    25503: ("Vivi sozinha por séculos após o fim da Segunda Era...", "Shurelia revelando a extensão temporal de seu sofrimento (101B <= 112B).", "rewritten"),
    25504: ("Na Primeira Era, eu tinha uma figura paterna. Na Segunda Era, tive companheiros valorosos para reconstruir o mundo.", "Resolução de estouro (259B -> 231B <= 240B). Restauração solene das Eras canônicas de Sol Ciel.", "rewritten"),
    25505: ("Mas na Terceira Era vivi só. Sem ninguém pra confiar...", "Resolução de estouro (147B -> 113B <= 120B). O drama do isolamento de Shurelia na Terceira Era.", "rewritten"),
    25506: ("Fui traída no fim da Segunda Era... e na calamidade, deixei de confiar em todos...", "Traição humana que culminou no Second Disaster preservada fielmente (166B <= 168B).", "rewritten"),
    25507: ("Evitei contato humano e proibi sentimentos pessoais.", "Resolução de estouro (125B -> 105B <= 112B). O tabu de misturar dever e sentimento.", "rewritten"),
    25508: ("Entendo...CRPor isso agia de forma tão formal.", "Resolução de estouro (125B -> 94B <= 96B). Lyner compreendendo a frieza burocrática.", "rewritten"),
    25509: ("...Sim.", "Afirmação sussurrada de Shurelia (13B <= 16B).", "approved"),
    25510: ("Não aguento mais...CRCom você, esse fardo pesou...", "Resolução de estouro (133B -> 103B <= 112B). Desmoronamento doloroso das defesas com CR.", "rewritten"),
    25511: ("Não quero ficar sozinha...", "O choro confessional mais tocante de Shurelia ('やっぱり独りはいやです') (54B <= 56B).", "approved"),
    25512: ("Senhora Shurelia... Estarei sempre ao seu lado, não se preocupe.", "Resolução de estouro (156B -> 130B <= 136B). Promessa eterna de amizade e proteção de Lyner.", "rewritten"),
    25513: ("Obrigada...CRMas quero me aproximar... só mais um pouco.", "Resolução de estouro (122B -> 114B <= 120B). Desejo sussurrado de proximidade terna com CR.", "rewritten")
}

errors = []
for did, (text, rat, verd) in batch7_curated.items():
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
    print("BATCH 7: 100% OK! All 48 lines fit within limits and pass technical gate.")

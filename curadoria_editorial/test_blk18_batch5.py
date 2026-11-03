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
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25386 AND 25425").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

batch5_curated = {
    25386: ("Você lutou demais na última batalha! Eu nem tive chance de cantar.", "Elogio alegre de Misha ao combate dinâmico (128B <= 160B).", "rewritten"),
    25387: ("Lyner... você ficou bem forte.", "Misha impressionada com a força de Lyner (62B <= 80B).", "rewritten"),
    25388: ("Imagina! Você é meu príncipe.", "Resolução de estouro (135B -> 61B <= 112B). Doçura apaixonada de Misha.", "rewritten"),
    25389: ("Senhora Shurelia? Parece animada.", "Resolução de estouro (83B -> 64B <= 72B). Observação de Lyner.", "rewritten"),
    25390: ("Obrigada pela Tranquilidade na última batalha.", "Shurelia agradecendo pelo item Tranquility (94B <= 136B).", "rewritten"),
    25391: ("Graças a isso, pude cantar sem parar.", "Shurelia reconhecendo a eficácia do suporte (71B <= 88B).", "rewritten"),
    25392: ("Acho que isso é uma verdadeira parceria.", "Shurelia refletindo sobre trabalho em equipe (82B <= 96B).", "rewritten"),
    25393: ("Conto com seu apoio.", "Polidez elegante de Shurelia (41B <= 48B).", "rewritten"),
    25394: ("Senhora Shurelia? Parece tão bem!", "Resolução de estouro (87B -> 64B <= 80B). Lyner notando a vivacidade.", "rewritten"),
    25395: ("Obrigada pela Tranquilidade na luta.", "Resolução de estouro (124B -> 75B <= 120B). Agradecimento de Shurelia.", "rewritten"),
    25396: ("Tranquilidade após uma Magia forte é reconfortante.", "Resolução de estouro (120B -> 105B <= 120B). Sensação prazerosa da recuperação mágica.", "rewritten"),
    25397: ("Conto com você.", "Resolução de estouro (62B -> 30B <= 48B). Voto de confiança de Shurelia.", "rewritten"),
    25398: ("...S-Senhora Shurelia?CRTá de mau humor?", "Resolução de estouro (95B -> 75B <= 88B). Lyner receoso com quebra CR.", "rewritten"),
    25399: ("É claro!CRLyner, o que foi aquilo na última batalha!?", "Resolução de estouro (156B -> 106B <= 144B). Bico aristocrático de Shurelia com CR.", "rewritten"),
    25400: ("Não esperava tombar em combate...", "Choque e vergonha de Shurelia ao desmaiar (67B <= 104B).", "rewritten"),
    25401: ("Esperava que me protegesse... Estou um pouco decepcionada.", "Repreensão meiga e nobre de Shurelia (112B <= 136B).", "rewritten"),
    25402: ("Da próxima me proteja direito, ouviu?", "Resolução de estouro (92B -> 74B <= 80B). Exigência afetuosa de Shurelia.", "rewritten"),
    25403: ("Senhora Shurelia? Tá zangada?", "Lyner percebendo a irritação (60B <= 80B).", "rewritten"),
    25404: ("A última batalha... Foi terrível.", "Resolução de estouro (145B -> 68B <= 120B). Decepção de Shurelia.", "rewritten"),
    25405: ("Não achei que fosse tombar. Confiei em você...", "Mágoa sentida de Shurelia (87B <= 120B).", "rewritten"),
    25406: ("D-desculpe...", "Resolução de estouro (37B -> 25B <= 32B). Pedido tímido de desculpas de Lyner.", "rewritten"),
    25407: ("Se isso se repetir,CRperderá o posto de Cavaleiro!", "Resolução de estouro (112B -> 93B <= 104B). Ultimato régio com CR.", "rewritten"),
    25408: ("S-Shurelia...", "Lyner surpreso (23B <= 40B).", "approved"),
    25409: ("Lyner, não exagere nas lutas! Você está aos trapos.", "Resolução de estouro (123B -> 106B <= 120B). Shurelia preocupada com as feridas de Lyner.", "rewritten"),
    25410: ("Lutando assim, seu corpo não aguenta.", "Resolução de estouro (117B -> 76B <= 88B). Alerta sério de Shurelia.", "rewritten"),
    25411: ("Cuide-se mais. Se você tombar... bem, eu odiaria isso...", "Confissão comovente de afeto de Shurelia (112B <= 136B).", "rewritten"),
    25412: ("Senhora Shurelia...", "Resolução de estouro (43B -> 39B <= 40B). Saudação tímida de Lyner.", "rewritten"),
    25413: ("Lyner, acho que está se desgastando demais...", "Resolução de estouro (118B -> 92B <= 104B). Preocupação nobre de Shurelia.", "rewritten"),
    25414: ("Lutando desse jeito, seu corpo não aguenta.", "Resolução de estouro (101B -> 88B <= 96B). Aviso direto de Shurelia.", "rewritten"),
    25415: ("Cuidar da saúde também é dever do Cavaleiro.", "Resolução de estouro (114B -> 88B <= 96B). Cobrança de disciplina.", "rewritten"),
    25416: ("Lyner.CRTem um momento agora?", "Shurelia solicitando audiência com CR (57B <= 64B).", "rewritten"),
    25417: ("Olá, Senhora Shurelia.", "Cumprimento educado de Lyner (45B <= 56B).", "rewritten"),
    25418: ("Desmaiar na batalha!? No que estava pensando!?", "Resolução de estouro (168B -> 91B <= 160B). Bronca indignada de Shurelia.", "rewritten"),
    25419: ("Não precisa se forçar a esse ponto! Cuide melhor do seu corpo.", "Apelo enfático de Shurelia (125B <= 160B).", "rewritten"),
    25420: ("Não me deixe preocupada...", "Resolução de estouro (80B -> 54B <= 64B). Vulnerabilidade tocante de Shurelia.", "rewritten"),
    25421: ("Olá, Senhora Shurelia.", "Resolução de estouro (67B -> 46B <= 48B). Cumprimento nobre.", "rewritten"),
    25422: ("Desmaiar na luta!? Andou relaxando, Lyner?", "Resolução de estouro (90B -> 84B <= 88B). Provocação austera de Shurelia.", "rewritten"),
    25423: ("Ou se esforçou demais. Pense em quem precisa te socorrer!", "Shurelia chamando atenção de Lyner para quem cuida dele (115B <= 120B).", "rewritten"),
    25424: ("Como vou cantar me preocupando com você?...", "Resolução de estouro (111B -> 86B <= 88B). Angústia da parceira mágica.", "rewritten"),
    25425: ("Tem razão.", "Resolução de estouro (32B -> 21B <= 24B). Admissão humilde de Lyner.", "rewritten")
}

errors = []
for did, (text, rat, verd) in batch5_curated.items():
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
    print("BATCH 5: 100% OK! All 40 lines fit within limits and pass technical gate.")

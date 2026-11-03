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
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25226 AND 25265").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

batch1_curated = {
    25226: ("Eu só queria ver você...", "Ajuste delicado da visita noturna de Aurica (51B <= 56B).", "approved"),
    25227: ("Lyner, quer uma massagem nos ombros?", "Fidelidade a '肩もんであげよっか' de Aurica (45B <= 96B).", "rewritten"),
    25228: ("P-por que essa pergunta do nada? O que houve?", "Resolução de estouro (101B -> 53B <= 96B). Espanto surpreso de Lyner.", "rewritten"),
    25229: ("Hehe, é segredo!", "Aurica guardando segredo com graça (22B <= 48B).", "approved"),
    25230: ("E aí, Aurica?", "Resolução de estouro (40B -> 28B <= 32B). Saudação casual de Lyner.", "rewritten"),
    25231: ("Ei, Lyner!CRVocê fez algo diferente na instalação de hoje!?", "Fidelidade com quebra CR sobre instalação (71B <= 144B).", "rewritten"),
    25232: ("O que foi tão de repente!?CRFiz tudo como de costume... eu acho.", "Lyner confuso com quebra CR (74B <= 192B).", "rewritten"),
    25233: ("É que a carga mágica ficou tão leve!CRO que fez? Usou magia!?CRLyner, você é demais!", "Aurica empolgada com alívio da carga com CR (95B <= 176B).", "rewritten"),
    25234: ("...Ou seria tolice minha se você só tiver tirado Cristais Grathnode.", "Resolução de estouro e correção do sentido original invertido no EN (80B <= 152B).", "rewritten"),
    25235: ("É que... lembra da instalação outro dia? Descobri algo incrível!", "Resolução de estouro (163B -> 76B <= 160B). Revelação de Aurica.", "rewritten"),
    25236: ("O-o que você descobriu?", "Gaguejo curioso de Lyner (30B <= 56B).", "approved"),
    25237: ("Não mudou nada após a instalação. Incrível, né?", "Fidelidade ao japonês sobre ausência de alteração na carga (99B <= 112B).", "rewritten"),
    25238: ("Deve ter sido pura coincidência.", "Lyner pragmático (39B <= 72B).", "approved"),
    25239: ("Não tenho nada de especial para contar.", "Aurica tímida na visita noturna (47B <= 96B).", "approved"),
    25240: ("Entendi...CRMas e a última instalação, ficou bem? Parecia meio doloroso...", "Resolução de estouro (193B -> 88B <= 176B). Preocupação de Lyner com CR.", "rewritten"),
    25241: ("Tô bem! Fiquei feliz em ver que precisa de mim.", "Resolução de estouro (157B -> 96B <= 120B). Devoção afetuosa de Aurica.", "rewritten"),
    25242: ("Vou dar o meu melhor, Lyner!", "Resolução de estouro (76B -> 57B <= 64B). Promessa sincera de Aurica.", "rewritten"),
    25243: ("Obrigado.", "Agradecimento afetuoso de Lyner (19B <= 24B).", "approved"),
    25244: ("Aurica, o que houve? Você parece tão pálida!", "Resolução de estouro (112B -> 53B <= 96B). Lyner notando a palidez ('顔色悪い').", "rewritten"),
    25245: ("Tô bem... Só queria ficar um pouco com você...", "Resolução de estouro (130B -> 96B <= 128B). Vulnerabilidade terna de Aurica.", "rewritten"),
    25246: ("...! Peguei pesado na instalação!?", "Resolução de estouro (91B -> 69B <= 80B). Remorso e choque de Lyner.", "rewritten"),
    25247: ("N-não, não é isso! Meu poder é baixo... Eu é que tenho que me esforçar mais...", "Resolução de estouro (205B -> 163B <= 168B). Autodepreciação dolorosa de Aurica Classe D.", "rewritten"),
    25248: ("Não é isso. Se estiver doendo, me avisa, tá?", "Lyner zeloso orientando Aurica a avisar (92B <= 112B).", "rewritten"),
    25249: ("...Obrigada. Você é tão bom...", "Resolução de estouro (70B -> 64B <= 64B). Gratidão sussurrada de Aurica.", "rewritten"),
    25250: ("(É melhor eu tirar alguns Cristais Grathnode dela...)", "Pensamento protetor de Lyner (60B <= 120B).", "rewritten"),
    25251: ("...Lyner.", "Misha chamando hesitante (13B <= 24B).", "approved"),
    25252: ("Ué, o que houve? Parece meio desanimada...", "Resolução de estouro (98B -> 51B <= 96B). Lyner notando desânimo ('元気ない').", "rewritten"),
    25253: ("Lembra que minha energia esgotou na última batalha?", "Resolução de estouro (118B -> 61B <= 112B). Misha relembrando perda de vigor.", "rewritten"),
    25254: ("Eu tava cansada, mas não achei que acabaria tão rápido...CRDesculpa atrapalhar.", "Resolução de estouro (222B -> 93B <= 208B). Pesar de Misha com CR.", "rewritten"),
    25255: ("Não! Foi descuido meu não notar.", "Resolução de estouro (90B -> 67B <= 72B). Assunção de culpa de Lyner.", "rewritten"),
    25256: ("Você juntou poder e eu desperdicei... Desculpe, vou tomar cuidado.", "Resolução de estouro (167B -> 134B <= 144B). Desculpas sinceras de Lyner.", "rewritten"),
    25257: ("...Obrigada. Suas palavras me dão forças pra continuar!", "Resolução de estouro (142B -> 113B <= 120B). Misha reanimada.", "rewritten"),
    25258: ("Lyner, tem um minuto agora?", "Resolução de estouro (70B -> 35B <= 64B). Pergunta de Misha.", "rewritten"),
    25259: ("Oi, Misha. O que foi?", "Resolução de estouro (49B -> 27B <= 48B). Recepção calorosa de Lyner.", "rewritten"),
    25260: ("Tava meio cansada, aí vim ver seu rosto pra recuperar o ânimo.", "Misha buscando conforto na presença de Lyner (72B <= 144B).", "rewritten"),
    25261: ("É mesmo?CRAs batalhas recentes têm sido bem pesadas.", "Resolução de estouro (131B -> 61B <= 120B). Concordância de Lyner com CR.", "rewritten"),
    25262: ("É. Eu cantando direto e você brandindo a espada.", "Resolução de estouro (126B -> 99B <= 104B). Parceria dinâmica em combate.", "rewritten"),
    25263: ("Mas saber que ajudo você me faz querer continuar.", "Resolução de estouro (117B -> 100B <= 112B). Determinação afetuosa de Misha.", "rewritten"),
    25264: ("Obrigado. Vou ficar mais forte pra poupar você de tanto esforço.", "Resolução de estouro (145B -> 131B <= 136B). Promessa de cavaleiro de Lyner.", "rewritten"),
    25265: ("Lyner. Boa noite!", "Saudação alegre de Misha (23B <= 48B).", "approved")
}

errors = []
for did, (text, rat, verd) in batch1_curated.items():
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
    print("BATCH 1: 100% OK! All 40 lines fit within limits and pass technical gate.")

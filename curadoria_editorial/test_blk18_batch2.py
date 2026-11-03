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
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25266 AND 25305").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

batch2_curated = {
    25266: ("Ah, oi, Misha. E aí?", "Recepção amigável de Lyner (42B <= 56B).", "approved"),
    25267: ("Hehe, só passei por aqui.CRMas sabe, tô me divertindo cantando nas batalhas!", "Resolução de estouro (194B -> 149B <= 160B). Misha empolgada com quebra CR.", "rewritten"),
    25268: ("Você me deixa carregar bastante, né? Liberar no limite máximo é tão revigorante!", "Resolução de estouro (179B -> 149B <= 176B). Sensação de êxtase ao descarregar Burst.", "rewritten"),
    25269: ("Vou cantar com tudo!CREntão carrega bastante!", "Resolução de estouro (159B -> 92B <= 112B). Apelo vibrante de Misha com CR.", "rewritten"),
    25270: ("Claro! Pode deixar comigo.", "Resolução de estouro (57B -> 50B <= 56B). Apoio convicto de Lyner.", "rewritten"),
    25271: ("Lyner, posso falar com você?", "Resolução de estouro (82B -> 58B <= 80B). Abordagem de Misha.", "rewritten"),
    25272: ("O que houve? Você parece insatisfeita.", "Resolução de estouro (108B -> 77B <= 88B). Percepção de Lyner ('不満そうな顔').", "rewritten"),
    25273: ("Lyner, você não tá se contendo comigo?", "Resolução de estouro (83B -> 76B <= 80B). Cobrança de Misha ('遠慮してる').", "rewritten"),
    25274: ("Usar tão pouca força mágica...CRTenho bastante energia, sabia?", "Resolução de estouro (157B -> 118B <= 136B). Misha querendo cantar magias mais fortes.", "rewritten"),
    25275: ("Pode confiar em mim!", "Resolução de estouro (68B -> 41B <= 56B). Desejo genuíno de Misha.", "rewritten"),
    25276: ("Quanta energia! Da próxima vez, vou pedir uma Canção bem grandiosa.", "Resolução de estouro (172B -> 139B <= 160B). Promessa bem-humorada de Lyner.", "rewritten"),
    25277: ("Pode contar comigo!", "Resolução de estouro (64B -> 39B <= 56B). Entusiasmo de Misha.", "rewritten"),
    25278: ("E aí, Misha?", "Cumprimento direto (26B <= 40B).", "approved"),
    25279: ("A última batalha foi incrível!CRNem precisei cantar pra você vencer.", "Resolução de estouro (177B -> 129B <= 176B). Elogio de Misha com quebra CR.", "rewritten"),
    25280: ("Pensando bem, você é forte demais, Lyner.", "Resolução de estouro (141B -> 81B <= 112B). Reconhecimento sincero de Misha.", "rewritten"),
    25281: ("Com alguém forte me protegendo, canto tranquila.", "Confiança mútua em batalha (86B <= 168B).", "rewritten"),
    25282: ("A última luta foi demais!CREu guardei tanta magia, mas você venceu antes de eu usar...", "Resolução de estouro (291B -> 173B <= 288B). Frustração cômica de Misha com CR.", "rewritten"),
    25283: ("...Bem, pelo menos vencemos.", "Resolução de estouro (88B -> 57B <= 72B). Conformismo bem-humorado de Misha.", "rewritten"),
    25284: ("Desculpe não usar a magia.CRNa próxima eu uso, prometo.", "Resolução de estouro (142B -> 106B <= 136B). Pedido de desculpas de Lyner com CR.", "rewritten"),
    25285: ("Combinado! Vou mandar ver!", "Resolução de estouro (113B -> 53B <= 56B). Promessa travessa de Misha.", "rewritten"),
    25286: ("Lyner... Posso falar com você?", "Abordagem tímida de Misha (60B <= 72B).", "rewritten"),
    25287: ("Obrigada por usar Tranquilidade na luta outro dia. Foi na hora certa.", "Misha grata pelo uso tático do item Tranquility (135B <= 160B).", "rewritten"),
    25288: ("Você usou bem quando comecei a cansar!", "Resolução de estouro (114B -> 75B <= 80B). Alívio imediato no canto.", "rewritten"),
    25289: ("Isso prova que cuidava de mim na luta. Fico tão feliz!", "Resolução de estouro (157B -> 109B <= 136B). Gratidão terna de Misha.", "rewritten"),
    25290: ("Lyner, podemos conversar?", "Resolução de estouro (58B -> 52B <= 56B). Pergunta delicada.", "rewritten"),
    25291: ("Claro.", "Consentimento gentil de Lyner (13B <= 24B).", "approved"),
    25292: ("Hehe, obrigada por usar tanta Tranquilidade em mim outro dia!", "Reconhecimento do suporte com itens (122B <= 144B).", "rewritten"),
    25293: ("Sei que dá trabalho sintetizar tantos itens.", "Misha compreendendo a dedicação de Lyner em Grathmeld (87B <= 112B).", "rewritten"),
    25294: ("Não é tão difícil.CRSó quero que consiga se concentrar no canto.", "Cuidado cavalheiresco de Lyner com quebra CR (115B <= 176B).", "rewritten"),
    25295: ("Seu canto ajuda demais a gente!", "Elogio ao valor das canções de Misha (57B <= 64B).", "rewritten"),
    25296: ("Hehe, sério? Valeu!CRVou me esforçar ainda mais!", "Resolução de estouro (115B -> 99B <= 104B). Misha motivada com CR.", "rewritten"),
    25297: ("E aí, Misha, tudo bem?", "Saudação afável de Lyner (46B <= 48B).", "approved"),
    25298: ("Provou o Sorvete Natural? Gostou?", "Misha ansiosa pelo veredito sobre Daishizen Ice (67B <= 88B).", "approved"),
    25299: ("Tava muito bom! Você manda bem na cozinha.", "Elogio sincero aos dotes culinários de Misha (84B <= 120B).", "rewritten"),
    25300: ("Bem, só usei os ingredientes certos. Difícil dar errado.", "Resolução de estouro (166B -> 109B <= 160B). Misha modesta.", "rewritten"),
    25301: ("Se gostou, preparo mais pra você!", "Resolução de estouro (82B -> 68B <= 80B). Oferta carinhosa de mais sorvete.", "rewritten"),
    25302: ("Gostou da Soda Capri? É meu xodó!", "Misha orgulhosa de sua criação de Grathmeld Capri Soda (69B <= 88B).", "rewritten"),
    25303: ("Tava ótima.CRMas ainda tenho dúvidas sobre os ingredientes...", "Desconfiança cômica de Lyner sobre os ingredientes da bebida (117B <= 152B).", "rewritten"),
    25304: ("Não ligue pra isso! Ficou bom e é o que vale, esqueça o processo.", "Filosofia culinária pragmática de Misha (124B <= 216B).", "rewritten"),
    25305: ("O que preparo na próxima?~", "Resolução de estouro (79B -> 55B <= 64B). Misha matutando novas receitas.", "rewritten")
}

errors = []
for did, (text, rat, verd) in batch2_curated.items():
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
    print("BATCH 2: 100% OK! All 40 lines fit within limits and pass technical gate.")

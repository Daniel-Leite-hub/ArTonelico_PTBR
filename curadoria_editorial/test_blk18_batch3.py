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
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25306 AND 25345").fetchall())
conn.close()

with open(BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

batch3_curated = {
    25306: ("Misha? Por que essa cara fechada?", "Resolução de estouro (85B -> 67B <= 72B). Pergunta de Lyner ('機嫌悪そう').", "rewritten"),
    25307: ("Eu já não disse que fico indefesa enquanto canto?", "Resolução de estouro (112B -> 94B <= 104B). Reclamação justa de Misha.", "rewritten"),
    25308: ("E ainda levei um baita golpe...", "Resolução de estouro (72B -> 63B <= 72B). Misha chateada com o dano sofrido.", "rewritten"),
    25309: ("Mentiroso! Se rolar de novo,CRnão vou te perdoar!", "Resolução de estouro e ritmo teatral de birra de Misha com CR (100B <= 104B).", "rewritten"),
    25310: ("Lyner... posso falar com você?", "Aproximação de Misha (58B <= 64B).", "approved"),
    25311: ("Ué? Que foi?", "Reação casual de Lyner (26B <= 32B).", "rewritten"),
    25312: ("Ai, ai... Ainda dói tudo...", "Resolução de estouro (73B -> 56B <= 64B). Dores remanescentes de Misha.", "rewritten"),
    25313: ("Pudera, tomei um ataque terrível!", "Resolução de estouro (121B -> 66B <= 120B). Frustração com o golpe recebido.", "rewritten"),
    25314: ("Sendo atacada indefesa, claro que ia tombar.", "Resolução de estouro (111B -> 84B <= 104B). Misha explicando a fragilidade da cantora.", "rewritten"),
    25315: ("Eu... sinto muito.", "Resolução de estouro (49B -> 37B <= 40B). Remorso sincero de Lyner.", "rewritten"),
    25316: ("Vê se me protege direito!", "Resolução de estouro (89B -> 52B <= 80B). Cobrança birrenta e carinhosa de Misha.", "rewritten"),
    25317: ("Lyner, tem um minutinho?", "Resolução de estouro (84B -> 49B <= 80B). Pergunta gentil de Misha.", "rewritten"),
    25318: ("Misha, que houve?", "Pergunta direta de Lyner (34B <= 40B).", "rewritten"),
    25319: ("Você lutou tanto e quase nem se machucou, né?", "Resolução de estouro (149B -> 88B <= 104B). Admiração de Misha pela força de Lyner.", "rewritten"),
    25320: ("Achei que fosse se desgastar mais tendo que lutar e me proteger ao mesmo tempo.", "Misha refletindo sobre a carga do combate (154B <= 184B).", "rewritten"),
    25321: ("Mas pareceu que você tirou de letra!", "Elogio ao vigor de Lyner (72B <= 120B).", "rewritten"),
    25322: ("Assim canto sem preocupação. Continuo contando com você, Lyner!", "Resolução de estouro (149B -> 126B <= 144B). Parceria renovada.", "rewritten"),
    25323: ("O-oi, Misha... que houve?", "Resolução de estouro (66B -> 50B <= 56B). Hesitação de Lyner.", "rewritten"),
    25324: ("Não lute até cair em pedaços!", "Resolução de estouro (67B -> 62B <= 64B). Misha preocupada com o desgaste de Lyner.", "rewritten"),
    25325: ("Se continuar lutando com tanta imprudência, vai acabar caindo de vez!", "Alerta protetor de Misha (136B <= 144B).", "rewritten"),
    25326: ("Cuide melhor de si mesmo, entendeu?", "Cobrança carinhosa de Misha (69B <= 88B).", "rewritten"),
    25327: ("Lyner!", "Chamado enérgico (13B <= 16B).", "approved"),
    25328: ("No que estava pensando ao lutar até desmaiar!?", "Repreensão exasperada de Misha (87B <= 120B).", "rewritten"),
    25329: ("Se continuar lutando assim, vai morrer!", "Resolução de estouro (90B -> 74B <= 88B). Angústia de Misha diante do perigo.", "rewritten"),
    25330: ("Não me preocupe assim! Desse jeito não consigo focar no meu canto...", "Resolução de estouro (177B -> 137B <= 160B). Misha desabafando seu medo.", "rewritten"),
    25331: ("Lyner... tem um minuto?", "Misha chamando casualmente (45B <= 64B).", "rewritten"),
    25332: ("O que houve, precisa de algo?", "Resolução de estouro (73B -> 58B <= 72B). Prontidão de Lyner.", "rewritten"),
    25333: ("É que... como posso dizer?...", "Resolução de estouro (74B -> 58B <= 64B). Timidez e hesitação de Misha.", "rewritten"),
    25334: ("Não é nada demais...CRSó queria ver seu rosto um pouco.", "Visita afetuosa noturna com quebra CR (88B <= 136B).", "rewritten"),
    25335: ("D-desculpa. Mas vou voltar a fazer isso, me aguente, tá?", "Desculpas tímidas e meigas de Misha (114B <= 128B).", "rewritten"),
    25336: ("Lyner♪ Tem um minuto?", "Chamado cantarolado de Misha (41B <= 64B).", "rewritten"),
    25337: ("O que houve? Parece tão feliz!", "Lyner notando o bom humor ('ご機嫌') de Misha (62B <= 64B).", "rewritten"),
    25338: ("Não senti dor alguma na última instalação!", "Resolução de estouro (117B -> 83B <= 112B). Alívio pós-instalação.", "rewritten"),
    25339: ("Meu corpo ficou tão leve depois! Você é genial.", "Resolução de estouro (136B -> 93B <= 112B). Elogio caloroso de Misha.", "rewritten"),
    25340: ("Obrigada♪", "Gratidão doce de Misha (17B <= 24B).", "approved"),
    25341: ("Lyner♪ Posso falar com você?", "Abordagem saltitante de Misha (54B <= 64B).", "rewritten"),
    25342: ("Lyner... o que fez na última instalação?", "Resolução de estouro (115B -> 79B <= 104B). Curiosidade de Misha.", "rewritten"),
    25343: ("Meu corpo ficou leve e meu canto tá ótimo! É vidente ou o quê!? Que demais!", "Empolgação pura de Misha com o resultado da instalação (155B <= 168B).", "rewritten"),
    25344: ("Que bom saber disso.", "Resolução de estouro (53B -> 41B <= 48B). Alívio modesto de Lyner.", "rewritten"),
    25345: ("...A menos que você só tenha tirado Cristais Grathnode, aí seria piada.", "Resolução de estouro (186B -> 146B <= 152B). Ironia espirituosa de Misha.", "rewritten")
}

errors = []
for did, (text, rat, verd) in batch3_curated.items():
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
    print("BATCH 3: 100% OK! All 40 lines fit within limits and pass technical gate.")

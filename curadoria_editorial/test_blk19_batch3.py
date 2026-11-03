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

# Batch 3: IDs 25586 to 25620 (35 lines)
# O pânico cômico da Lata de Canto de Sereia (人魚のウタ缶), a Tigela de Gato e os apelidos bizarros de Aurica (Krusche e Jack).
batch3_curated = {
    25586: (
        "N-não! Guarde isso!",
        "Pânico histérico de Aurica ao ver a lata perigosa (40B <= 40B).",
        "approved"
    ),
    25587: (
        "Hã? Como assim, “Guarde isso”?",
        "Lyner sem entender nada do susto repentino (62B <= 80B).",
        "approved"
    ),
    25588: (
        "Guarda logo, com cuidado! Rápido!",
        "Resolução de estouro (85B -> 68B <= 72B). Aurica aos berros mandando guardar a lata com extremo cuidado.",
        "rewritten"
    ),
    25589: (
        "Quanta pressa... Pronto, já guardei.",
        "Resolução de estouro (135B -> 73B <= 112B). Lyner confuso guardando a lata de volta na sacola.",
        "rewritten"
    ),
    25590: (
        "Não tire isso de novo sem pensar, tá? É muito perigoso!",
        "Aurica dando uma bronca muito séria sobre o perigo do item (114B <= 136B).",
        "approved"
    ),
    25591: (
        "É mesmo tão perigoso assim?",
        "Lyner intrigado com o terror de Aurica (57B <= 64B).",
        "approved"
    ),
    25592: (
        "Sim! Tenho lembranças bem ruins por causa disso...",
        "Aurica relembrando com calafrios seu trauma infantil (102B <= 104B).",
        "approved"
    ),
    25593: (
        "Trauma? Com a lata de canto?",
        "Resolução de estouro (78B -> 57B <= 72B). Lyner incrédulo que uma lata possa causar traumas.",
        "rewritten"
    ),
    25594: (
        "Sim... Quando eu era criança e morava em casa...",
        "Resolução de estouro (149B -> 98B <= 136B). Aurica iniciando seu relato de infância.",
        "rewritten"
    ),
    25595: (
        "A lata estava em um dos armários.",
        "Aurica contando onde achou o objeto (68B <= 72B).",
        "approved"
    ),
    25596: (
        "Uma lata de canto de sereia!?",
        "Lyner chocado ao imaginar a cena (59B <= 64B).",
        "approved"
    ),
    25597: (
        "Sim... mas eu não sabia o que era...CRachei que era lata de doce e abri.",
        "Resolução de estouro (194B -> 143B <= 184B). O erro trágico e hilário de abrir a lata achando que era guloseima com CR.",
        "rewritten"
    ),
    25598: (
        "Aí a lata pulou e veio voando na minha cara...",
        "Resolução de estouro (118B -> 92B <= 104B). O ataque repentino da lata enfeitiçada.",
        "rewritten"
    ),
    25599: (
        "Nossa... que sufoco, hein.",
        "Resolução de estouro (79B -> 53B <= 64B). Lyner demonstrando empatia assustada.",
        "rewritten"
    ),
    25600: (
        "Corri pela vila chorando. Se não tivessem derrubado com um tapa, minha cabeça teria afundado!",
        "Resolução de estouro (248B -> 189B <= 208B). O clímax cômico da lata perseguindo a pobre Aurica.",
        "rewritten"
    ),
    25601: (
        "O que eu quero saber é por que você teria algo assim em casa?",
        "Lyner questionando como um artefato tão perigoso foi parar no armário da família (125B <= 160B).",
        "approved"
    ),
    25602: (
        "Sei lá! Mas tome muito cuidado ao usar. Não quero aquela lata voando em mim de novo!",
        "Resolução de estouro (231B -> 171B <= 200B). O pavor de Aurica de reviver o pesadelo.",
        "rewritten"
    ),
    25603: (
        "Pode deixar. Até porque acertar você de novo seria quase impossível...",
        "Resolução de estouro (163B -> 144B <= 144B). Lyner tentando acalmar a garota com lógica.",
        "rewritten"
    ),
    25604: (
        "Mas chamar o Circula de Tigela de Gato?CRSeu jeito de dar nomes me impressiona.",
        "Resolução de estouro (196B -> 159B <= 192B). Lyner lembrando do apelido 'Tigela de Gato' (猫どんぶり) com CR.",
        "rewritten"
    ),
    25605: (
        "R, sério? Mas parece meio que uma tigela, e até a Tastiella...",
        "Aurica defendendo sua lógica visual comparando o teletransportador com louça (127B <= 136B).",
        "approved"
    ),
    25606: (
        "É, eu sei, mas... CROh, já sei!",
        "Lyner tendo uma ideia brilhante com tag CR preservada (65B <= 72B).",
        "approved"
    ),
    25607: (
        "Por que não dá um apelido pra todo mundo?",
        "Resolução de estouro (114B -> 85B <= 96B). Lyner desafiando o talento cômico de Aurica.",
        "rewritten"
    ),
    25608: (
        "O quê!? Não! Todo mundo vai ficar uma fera comigo!",
        "Resolução de estouro (131B -> 103B <= 104B). Aurica morrendo de medo das reações dos companheiros.",
        "rewritten"
    ),
    25609: (
        "Não esquenta, não conto pra ninguém. Vai ficar só entre a gente.",
        "Resolução de estouro (154B -> 133B <= 144B). Lyner prometendo segredo absoluto.",
        "rewritten"
    ),
    25610: (
        "Mas...",
        "Hesitação fofa de Aurica (13B <= 16B).",
        "approved"
    ),
    25611: (
        "Tudo bem. Vamos começar com... Krusche.",
        "Lyner escolhendo o primeiro alvo (80B <= 104B).",
        "approved"
    ),
    25612: (
        "...Se for estranho, nada de ficar bravo ou me dedurar, tá?",
        "Resolução de estouro (139B -> 118B <= 136B). Aurica negociando imunidade diplomática.",
        "rewritten"
    ),
    25613: (
        "Pode deixar. E a Krusche?",
        "Resolução de estouro (63B -> 51B <= 56B). Lyner ansioso pelo apelido.",
        "rewritten"
    ),
    25614: (
        "...Maníaca linguaruda.",
        "Resolução de estouro (76B -> 46B <= 48B). Apelido certeiro de Krusche ('毒舌飛空挺マニア').",
        "rewritten"
    ),
    25615: (
        "D-desculpa! Não é por mal! Só tentei descrever o jeito dela no dia a dia...",
        "Resolução de estouro (234B -> 152B <= 208B). Aurica se retratando desesperadamente com medo da vingança de Krusche.",
        "rewritten"
    ),
    25616: (
        "E-eu sei! Mas acho que resumiu bem o jeito dela.",
        "Resolução de estouro (154B -> 95B <= 120B). Lyner concordando que o apelido foi perfeito.",
        "rewritten"
    ),
    25617: (
        "Se você diz... então menos mal.",
        "Resolução de estouro (90B -> 63B <= 80B). Aurica aliviada.",
        "rewritten"
    ),
    25618: (
        "E quanto ao Jack?",
        "Resolução de estouro (42B -> 35B <= 40B). Próximo alvo da lista.",
        "rewritten"
    ),
    25619: (
        "...Mecha verde.",
        "Resolução de estouro (38B -> 31B <= 32B). O apelido bizarro de Jack ('メカミドリ').",
        "rewritten"
    ),
    25620: (
        "M-mecha!?",
        "Lyner perplexo com a comparação robótica de Jack (19B <= 24B).",
        "approved"
    )
}

if __name__ == "__main__":
    assert len(batch3_curated) == 35, f"Esperado 35, obtido {len(batch3_curated)}"
    errs = []
    for did, (text, rat, verd) in batch3_curated.items():
        lim = limits[str(did)]
        enc = encoded_size(text)
        if enc > lim:
            errs.append(f"ID {did}: enc {enc}B > limit {lim}B (+{enc - lim})")
        v_errs = validate_line(did, "", text)
        if v_errs:
            errs.append(f"ID {did} validação: {v_errs}")

    if errs:
        print(f"Erros em Batch 3 ({len(errs)}):")
        for e in errs:
            print(" ", e)
        sys.exit(1)
    else:
        print("Batch 3: 100% OK! 35 falas validadas com 0 estouros e 0 erros técnicos.")

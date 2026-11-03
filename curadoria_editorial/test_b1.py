import json
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

b1 = [
    {
        "id": 3464,
        "curated_ptbr": "Gostaria de travar outro combate corporal comigo?\nFiquei ainda mais forte desde a nossa última luta.",
        "verdict": "rewritten",
        "rationale": "Confere tom mecânico e polido ao autômato de combate, desfazendo o decalque e equilibrando a quebra de linha."
    },
    {
        "id": 3465,
        "curated_ptbr": "Sendo assim, em guarda!",
        "verdict": "rewritten",
        "rationale": "Resgata a solene postura de combate de artes marciais do autômato (参ります)."
    },
    {
        "id": 3466,
        "curated_ptbr": "Impressionante como sempre, Lyner.\nFoi um confronto magnífico.",
        "verdict": "rewritten",
        "rationale": "Eufonia natural e cortesia robótica (さすがですね), eliminando a simplicidade rasa do inglês."
    },
    {
        "id": 3467,
        "curated_ptbr": "Contudo, também não fiquei para trás.\nTodos os seus movimentos foram gravados em minha memória.",
        "verdict": "rewritten",
        "rationale": "Ajuste refinado da dicção da máquina analítica que registra dados de combate."
    },
    {
        "id": 3468,
        "curated_ptbr": "No próximo confronto, usarei esses dados para me aprimorar.\nAguarde com grande expectativa!",
        "verdict": "rewritten",
        "rationale": "Tradução fiel a ご期待ください e remoção do prolixo desvio da NISA."
    },
    {
        "id": 3469,
        "curated_ptbr": "Fala sério...\nQuanto mais a gente luta, mais você melhora?\nAssim vou acabar perdendo a vontade de lutar contigo...",
        "verdict": "rewritten",
        "rationale": "Expressividade coloquial espontânea de Lyner reagindo à evolução infinita da máquina."
    },
    {
        "id": 3470,
        "curated_ptbr": "Se vencer cinco vezes seguidas,\nreceberá um prêmio fabuloso.",
        "verdict": "rewritten",
        "rationale": "Fluidez natural de desafio esportivo/treinamento de RPG sem quebras órfãs."
    },
    {
        "id": 3471,
        "curated_ptbr": "Entendido.\nEstarei sempre aqui ao seu dispor.",
        "verdict": "rewritten",
        "rationale": "Resgata a reverência cortês de serviço (お待ちしております)."
    },
    {
        "id": 3472,
        "curated_ptbr": "O Gather não fica por aqui.",
        "verdict": "rewritten",
        "rationale": "Frase concisa e natural de navegação em Sol Ciel."
    },
    {
        "id": 3473,
        "curated_ptbr": "Lyner... Escalar a Torre...",
        "verdict": "rewritten",
        "rationale": "Pontuação hesitante e tom grave de preocupação militar de Radolf."
    },
    {
        "id": 3474,
        "curated_ptbr": "É... Procurei e quebrei a cabeça de todo jeito,\nmas essa acabou sendo a nossa única opção.",
        "verdict": "rewritten",
        "rationale": "Dicção calorosa e desabafo autêntico de Lyner perante o dilema (色々手段を探したり考えたりしたんだけど)."
    },
    {
        "id": 3475,
        "curated_ptbr": "Compreendo...",
        "verdict": "rewritten",
        "rationale": "Sobriedade cavalheiresca de Radolf."
    },
    {
        "id": 3476,
        "curated_ptbr": "Se tivéssemos tempo, certamente haveria outra saída...\nMas, diante da nossa urgência, não temos escolha.",
        "verdict": "rewritten",
        "rationale": "Retórica equilibrada e nobre de Radolf, eliminando o ritmo truncado."
    },
    {
        "id": 3477,
        "curated_ptbr": "Ainda assim, a Tribo Teru é deveras perigosa.\nDevemos agir com a máxima cautela.",
        "verdict": "rewritten",
        "rationale": "Aplica o termo canônico Tribo Teru e reforça o aviso tático de Radolf."
    },
    {
        "id": 3478,
        "curated_ptbr": "É, eu sei... Desculpem por arrastar\ntodos vocês para uma enrascada dessas.",
        "verdict": "rewritten",
        "rationale": "Coloquialismo sincero e fraternal de Lyner."
    },
    {
        "id": 3479,
        "curated_ptbr": "Ora, não se preocupe com isso.",
        "verdict": "rewritten",
        "rationale": "Cavalheirismo generoso de Radolf (なに、気にするな)."
    },
    {
        "id": 3480,
        "curated_ptbr": "...",
        "verdict": "rewritten",
        "rationale": "Padronização canônica de reticências reflexivas."
    },
    {
        "id": 3481,
        "curated_ptbr": "Aqui é o Anteparo A2.\nO portador da autorização deve dar um passo à frente.",
        "verdict": "rewritten",
        "rationale": "Adota o termo oficial do glossário 'Anteparo A2' (A2隔壁) e instrução militar protocolar."
    },
    {
        "id": 3482,
        "curated_ptbr": "Autenticação por Espectro FFT: Lyner Barsett.\nPor favor, transmita o comando.",
        "verdict": "rewritten",
        "rationale": "Resgata o termo técnico 'Espectro FFT' e o comando formal da inteligência da porta."
    },
    {
        "id": 3483,
        "curated_ptbr": "Abrir o Anteparo A2.",
        "verdict": "rewritten",
        "rationale": "Comando militar claro conforme termo canônico 'Anteparo A2'."
    },
    {
        "id": 3484,
        "curated_ptbr": "#0Ma paks ga exec guol A2 al noes.",
        "verdict": "rewritten",
        "rationale": "RESTAURAÇÃO CRÍTICA: código de comando original em Hymmnos (#0...) que estava apagado no PTBR anterior."
    },
    {
        "id": 3485,
        "curated_ptbr": "Código autenticado com sucesso.",
        "verdict": "rewritten",
        "rationale": "Linguagem formal de sistema de segurança da Torre."
    },
    {
        "id": 3486,
        "curated_ptbr": "Abertura do anteparo em dois segundos.\nStatus: permissão de trânsito concedida.",
        "verdict": "rewritten",
        "rationale": "Rigor terminológico militar e eliminação de numerais arábicos soltos na prosódia falada."
    },
    {
        "id": 3487,
        "curated_ptbr": "Ora, vejam só! Que saudade, rapaz!\nTem passado bem?!",
        "verdict": "rewritten",
        "rationale": "Entusiasmo caloroso de reencontro informal (懐かしいなぁ)."
    },
    {
        "id": 3488,
        "curated_ptbr": "É, vou levando...\nGraças à sua torcida, continuo inteiro.",
        "verdict": "rewritten",
        "rationale": "Desfaz o literalismo de 'obrigado a você', traduzindo com eufonia a expressão idiomática お陰様で."
    },
    {
        "id": 3489,
        "curated_ptbr": "Mas olha, hoje é um dia festivo!\nE devemos tudo a você.",
        "verdict": "rewritten",
        "rationale": "Celebração alegre com ritmo coloquial brasileiro."
    },
    {
        "id": 3490,
        "curated_ptbr": "Falando nisso, a Misha ainda não deu as caras por aqui...?",
        "verdict": "rewritten",
        "rationale": "Naturalidade expressiva oral para a ausência de Misha (まだ出てこないのか)."
    },
    {
        "id": 3491,
        "curated_ptbr": "Entrei sem pedir licença... Será que não tem problema?\nA Aurica também não está por aqui...",
        "verdict": "rewritten",
        "rationale": "Tom hesitante e monólogo interior de Lyner ao invadir o espaço íntimo."
    },
    {
        "id": 3492,
        "curated_ptbr": "...Hum? O que é aquilo ali?\nParece estar carregando um vestido branco...",
        "verdict": "rewritten",
        "rationale": "CORREÇÃO CRÍTICA DO ERRO DA NISA: Lyner fala consigo mesmo ao observar uma criatura ao longe, sem se dirigir a ela."
    },
    {
        "id": 3493,
        "curated_ptbr": "...",
        "verdict": "rewritten",
        "rationale": "Padronização de reticências canônicas."
    },
    {
        "id": 3494,
        "curated_ptbr": "Ei, quem é você?",
        "verdict": "rewritten",
        "rationale": "Tom direto e surpreso de Lyner ao ver a criaturinha alada."
    },
    {
        "id": 3495,
        "curated_ptbr": "...!!!",
        "verdict": "rewritten",
        "rationale": "Preserva o susto súbito da fadinha fugindo com o vestido."
    },
    {
        "id": 3496,
        "curated_ptbr": "...E lá se foi ela.",
        "verdict": "rewritten",
        "rationale": "Expressividade coloquial brasileira para a fuga repentina."
    },
    {
        "id": 3497,
        "curated_ptbr": "Aaaah, que banho gostoso!",
        "verdict": "rewritten",
        "rationale": "Expressão viva de alívio pós-banho de Aurica (サッパリした)."
    },
    {
        "id": 3498,
        "curated_ptbr": "Uaaah?!",
        "verdict": "rewritten",
        "rationale": "Vocalização espontânea de susto ao dar de cara com Aurica."
    },
    {
        "id": 3499,
        "curated_ptbr": "...Ué?",
        "verdict": "rewritten",
        "rationale": "Reação inocente e surpresa de Aurica ao notar alguém no quarto."
    },
    {
        "id": 3500,
        "curated_ptbr": "Ly... Lyner...?!",
        "verdict": "rewritten",
        "rationale": "Choque gaguejado ao reconhecer Lyner no seu quarto."
    },
    {
        "id": 3501,
        "curated_ptbr": "N-não, espera! Não é nada do que você tá pensando!\nNão tive nenhuma segunda intenção, foi um puro acidente...",
        "verdict": "rewritten",
        "rationale": "Pânico hilário de Lyner tentando se justificar com afobação e gagueira."
    },
    {
        "id": 3502,
        "curated_ptbr": "Lyner! Você veio mesmo!\nQue alegria enorme!!",
        "verdict": "rewritten",
        "rationale": "Pureza e entusiasmo desmedido de Aurica (嬉しいー!!)."
    },
    {
        "id": 3503,
        "curated_ptbr": "Eu juro que não vim espiar por maldade...\n... Hã?",
        "verdict": "rewritten",
        "rationale": "DESFAZ DECALQUE DA NISA: Lyner ainda tentando completar a desculpa de não ter segundas intenções (下心), percebendo que ela nem desconfiou."
    },
    {
        "id": 3504,
        "curated_ptbr": "Lyner... Nunca imaginei que você conseguiria chegar tão fundo...\nÉ incrível ter chegado até aqui!",
        "verdict": "rewritten",
        "rationale": "Admiração meiga de Aurica pelo avanço de Lyner nas profundezas de sua Cosmosfera."
    },
    {
        "id": 3505,
        "curated_ptbr": "B-bom, passei por um bocado de apuros...\nÀs vezes nem eu acredito que ainda estou inteiro por aqui...",
        "verdict": "rewritten",
        "rationale": "Modéstia bem-humorada e risonha de Lyner."
    },
    {
        "id": 3506,
        "curated_ptbr": "...Tem razão, né?\nÉ que no fundo sou bem caprichosa e egoísta, muito mais do que aparento...",
        "verdict": "rewritten",
        "rationale": "Confissão tímida e vulnerável de Aurica sobre os seus defeitos íntimos."
    },
    {
        "id": 3507,
        "curated_ptbr": "...",
        "verdict": "rewritten",
        "rationale": "Silêncio empático de Lyner ouvindo o desabafo."
    },
    {
        "id": 3508,
        "curated_ptbr": "Ah, é mesmo! Queria te pedir um favor, Lyner.\nLogo mais vou ter que participar de um ritual.",
        "verdict": "rewritten",
        "rationale": "Transição meiga e afetuosa de Aurica (儀式)."
    },
    {
        "id": 3509,
        "curated_ptbr": "E pensei se... se você não poderia me acompanhar nessa cerimônia...",
        "verdict": "rewritten",
        "rationale": "Hesitação dengosa e tímida de Aurica convidando Lyner."
    },
    {
        "id": 3510,
        "curated_ptbr": "Hã? Eu...?",
        "verdict": "rewritten",
        "rationale": "Espanto espontâneo de Lyner."
    },
    {
        "id": 3511,
        "curated_ptbr": "Sim. Me disseram que esse rito serve para extrair\num poder ainda maior deste mundo.",
        "verdict": "rewritten",
        "rationale": "Tom explicativo suave sobre o propósito da cerimônia na mente."
    },
    {
        "id": 3512,
        "curated_ptbr": "Mas foi você quem me guiou até este nível...\nPor isso, queria muito que estivesse ao meu lado.",
        "verdict": "rewritten",
        "rationale": "Doçura e cumplicidade emocional de Aurica para com Lyner."
    },
    {
        "id": 3513,
        "curated_ptbr": "...Entendi o recado.\nPode deixar, eu vou com você.",
        "verdict": "rewritten",
        "rationale": "Resposta calorosa, cavalheira e protetora de Lyner."
    },
    {
        "id": 3514,
        "curated_ptbr": "Que alívio... Muito obrigada!",
        "verdict": "rewritten",
        "rationale": "Gratidão pura e aliviada de Aurica (よかった...。ありがと!)."
    },
    {
        "id": 3515,
        "curated_ptbr": "...M-mas mudando de assunto,\nvocê não ia se vestir agora?",
        "verdict": "rewritten",
        "rationale": "Desconforto pudico e simpático de Lyner ao lembrar da situação do quarto."
    },
    {
        "id": 3516,
        "curated_ptbr": "Ah, é verdade! Eu tinha deixado bem aqui...\n... Ué?",
        "verdict": "rewritten",
        "rationale": "Espanto inocente ao procurar a roupa."
    },
    {
        "id": 3517,
        "curated_ptbr": "Sumiu! O meu vestido branco sumiu!!",
        "verdict": "rewritten",
        "rationale": "Desespero cômico e afobado de Aurica."
    },
    {
        "id": 3518,
        "curated_ptbr": "Vestido branco?! Uma garotinha com asas\nacabou de passar correndo com ele nos braços!",
        "verdict": "rewritten",
        "rationale": "Esclarecimento ágil de Lyner desfazendo a bizarra tradução da NISA ('feathered, little girl')."
    },
    {
        "id": 3519,
        "curated_ptbr": "Mentira! Não é possível!\nSem aquele vestido, não vou conseguir realizar o ritual!!",
        "verdict": "rewritten",
        "rationale": "Pânico expressivo de Aurica com eufonia natural."
    },
    {
        "id": 3520,
        "curated_ptbr": "Calma, ela não deve ter ido muito longe ainda.\nVamos atrás dela!",
        "verdict": "rewritten",
        "rationale": "Iniciativa resoluta de Lyner acalmando Aurica e liderando a busca."
    }
]

# Load input for original comparison
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_014_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)
inp_map = {d["id"]: d for d in input_data["dialogues"]}

hard_gate_errors = 0
lint_warnings = 0

for item in b1:
    orig = inp_map[item["id"]]
    valido, erros = validador_editorial.validar_hard_gate(
        original=orig["original_jp"],
        traduzido=item["curated_ptbr"],
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        for e in erros:
            print(f"[HARD GATE] ID {item['id']}: {e}")
            hard_gate_errors += 1
    avisos = validador_editorial.auditar_estilo_editorial(item["curated_ptbr"])
    if avisos:
        for a in avisos:
            print(f"[LINT] ID {item['id']}: {a}")
            lint_warnings += 1

print(f"Batch 1 check complete: {len(b1)} items, {hard_gate_errors} hard gate errors, {lint_warnings} lint warnings.")

if hard_gate_errors == 0 and lint_warnings == 0:
    out_file = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_014.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(b1, f, indent=2, ensure_ascii=False)
    print(f"Saved {out_file}")

import json
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

b6 = [
    {
        "id": 3697,
        "curated_ptbr": "Não tem ninguém aqui...?!",
        "verdict": "rewritten",
        "rationale": "Espanto com o vazio repentino das dependências da Igreja."
    },
    {
        "id": 3698,
        "curated_ptbr": "...Mas que barbaridade é esta?!",
        "verdict": "rewritten",
        "rationale": "Indignação grave e solene de Radolf (何ということだ)."
    },
    {
        "id": 3699,
        "curated_ptbr": "Caímos feito patos na armadilha\nurzida pelo Bispo Falss, pelo visto.",
        "verdict": "rewritten",
        "rationale": "Perspicácia irônica refinada de Ayatane (まんまと引っかかったってワケだね)."
    },
    {
        "id": 3700,
        "curated_ptbr": "Droga! Para onde foram\ntodos os clérigos da Igreja?!",
        "verdict": "rewritten",
        "rationale": "Fúria de Radolf perante a deserção total do clero conspirador."
    },
    {
        "id": 3701,
        "curated_ptbr": "Vamos até a cidade averiguar com o povo!",
        "verdict": "rewritten",
        "rationale": "Proatividade ágil de Lyner em busca de testemunhas."
    },
    {
        "id": 3702,
        "curated_ptbr": "...",
        "verdict": "rewritten",
        "rationale": "Reticências padronizadas."
    },
    {
        "id": 3703,
        "curated_ptbr": "Bom... Eu já desconfio muito bem\ndo que está prestes a acontecer.",
        "verdict": "rewritten",
        "rationale": "Olhar enigmático e perspicaz de Ayatane antecipando a tragédia."
    },
    {
        "id": 3704,
        "curated_ptbr": "Aqui é a Krusche, líder do Projeto Shoga.\nA presidente Ayano se encontra?",
        "verdict": "rewritten",
        "rationale": "Mantém o nome canônico do Projeto Shoga (翔雅 - aeronave Gungnir) e a atitude direta de Krusche."
    },
    {
        "id": 3705,
        "curated_ptbr": "A senhora presidente saiu em expedição\nde exploração pela Torre no momento.",
        "verdict": "rewritten",
        "rationale": "Fiel ao japonês 塔探索 (expedição de exploração pela Torre)."
    },
    {
        "id": 3706,
        "curated_ptbr": "Como imaginei... Tinha que estar fora...",
        "verdict": "rewritten",
        "rationale": "Suspiro resignado e sarcástico de Krusche (やっぱりいないか)."
    },
    {
        "id": 3707,
        "curated_ptbr": "Quinze minutos adiantado... Cheguei cedo demais.\nAcho que vou entrar numa livraria para matar o tempo...",
        "verdict": "rewritten",
        "rationale": "Monólogo casual e jovem de Lyner em sua memória escolar."
    },
    {
        "id": 3708,
        "curated_ptbr": "...",
        "verdict": "rewritten",
        "rationale": "Reticências padronizadas."
    },
    {
        "id": 3709,
        "curated_ptbr": "Ah... Togasaki?!",
        "verdict": "rewritten",
        "rationale": "Surpresa tímida de Lyner ao encontrar a colega."
    },
    {
        "id": 3710,
        "curated_ptbr": "...Olá.",
        "verdict": "rewritten",
        "rationale": "Saudação seca e formal de colegial tímida/reservada."
    },
    {
        "id": 3711,
        "curated_ptbr": "V-você chegou cedo, hein...",
        "verdict": "rewritten",
        "rationale": "Constrangimento adolescente de Lyner gaguejando."
    },
    {
        "id": 3712,
        "curated_ptbr": "Detesto me atrasar para compromissos.",
        "verdict": "rewritten",
        "rationale": "Personalidade metódica e austera da garota."
    },
    {
        "id": 3713,
        "curated_ptbr": "A-ah, entendi...",
        "verdict": "rewritten",
        "rationale": "Concordância sem graça tentando quebrar o gelo."
    },
    {
        "id": 3714,
        "curated_ptbr": "...",
        "verdict": "rewritten",
        "rationale": "Pausa reflexiva e constrangida."
    },
    {
        "id": 3715,
        "curated_ptbr": "(Nossa... Mas que clima mais pesado e sem jeito...\nO silêncio entre nós tá insuportável...)",
        "verdict": "rewritten",
        "rationale": "Fiel a 間が持たない (não conseguir manter o assunto / silêncio constrangedor)."
    },
    {
        "id": 3716,
        "curated_ptbr": "E então, para onde vamos?\nNão conheço este lugar, portanto me guie.",
        "verdict": "rewritten",
        "rationale": "Postura direta exigindo a iniciativa do rapaz."
    },
    {
        "id": 3717,
        "curated_ptbr": "A-ah, claro! Vamos nessa, então.\nAcabou de ser inaugurado, é um lugar super bonito, sabia?",
        "verdict": "rewritten",
        "rationale": "Entusiasmo desajeitado de Lyner recuperando o fôlego (出来たばっかりだから綺麗なところだぜ)."
    },
    {
        "id": 3718,
        "curated_ptbr": "...Compreendo...",
        "verdict": "rewritten",
        "rationale": "Resposta lacônica mantendo o mistério da projeção escolar da Cosmosfera."
    },
    {
        "id": 3719,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3720,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3721,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3722,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3723,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3724,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3725,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3726,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3727,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3728,
        "curated_ptbr": "",
        "verdict": "approved_as_is",
        "rationale": "Entrada nula original da tabela de eventos preservada para paridade binária."
    },
    {
        "id": 3729,
        "curated_ptbr": "“Nova Autobiografia de Kyle, Volume 6”.\nO diário secreto do Bispo Falss...",
        "verdict": "rewritten",
        "rationale": "Padronização canônica do título do tomo confidencial de Falss."
    },
    {
        "id": 3730,
        "curated_ptbr": "Radolf, que abomina injustiças e discursos desonestos,\nvoltou a vomitar seus nobres sermões moralistas.",
        "verdict": "rewritten",
        "rationale": "CORREÇÃO CRÍTICA DO DESVIO GROTESCO DA NISA: restaura o desprezo ácido de Falss contra a retidão de Radolf (曲がったこと、不誠実な発言が大嫌いなラードルフがまたりっぱな事を言い始める)."
    },
    {
        "id": 3731,
        "curated_ptbr": "Ele parece estar furioso de verdade pelo fato de a Igreja\nnão ter contido o tumulto em frente ao armazém da esquina.",
        "verdict": "rewritten",
        "rationale": "CORREÇÃO CRÍTICA DO DESVIO DA NISA: Falss relata a revolta de Radolf pela omissão proposital da Igreja no motim."
    },
    {
        "id": 3732,
        "curated_ptbr": "Afinal, estender a mão à plebe ignorante não tem valor algum.\nE ele ainda exige priorizar essa escória perante a Magna Aparição...",
        "verdict": "rewritten",
        "rationale": "CORREÇÃO CRÍTICA DO DESVIO DA NISA: Falss expõe seu ódio elitista e sua indiferença sociopata pelo povo comum (愚民へ施した所でなんの価値もない)."
    },
    {
        "id": 3733,
        "curated_ptbr": "Detesto gente obstinada e intrometida.\nQuero vê-lo destituído e arruinado o mais rápido possível.",
        "verdict": "rewritten",
        "rationale": "Malevolência calculada de Falss contra seu subordinado incômodo (押しが強い奴は嫌いだ。すぐにでも失脚させたい)."
    },
    {
        "id": 3734,
        "curated_ptbr": "Recebi o informe de que obtiveram o Cristal Hymmnos Linker.\nCom isso, todas as peças-chave estão reunidas.",
        "verdict": "rewritten",
        "rationale": "Adota 'Cristal Hymmnos Linker' sem colchetes perigosos."
    },
    {
        "id": 3735,
        "curated_ptbr": "Aurica, a suposta reencarnação da Deusa Tyria, e o cristal Linker.",
        "verdict": "rewritten",
        "rationale": "Esclarece a conexão conspiratória entre a garota e o cristal de ligação (オリカとリンカ)."
    },
    {
        "id": 3736,
        "curated_ptbr": "Visto que esta será a bênção derradeira de Aurica,\npretendo celebrá-la com a mais grandiosa pompa fúnebre.",
        "verdict": "rewritten",
        "rationale": "Subtexto cínico e sinistro de Falss preparando o sacrifício de Aurica (最後の祝福となる故、盛大に行ってやろう)."
    },
    {
        "id": 3737,
        "curated_ptbr": "O único revés é a trapalhada do incompetente do Bourd:\nparece que a presidente da Tenba descobriu toda a sua conspiração.",
        "verdict": "rewritten",
        "rationale": "Desprezo pelo comparsa trapalhão e ajuste de gênero (a presidente Ayano)."
    },
    {
        "id": 3738,
        "curated_ptbr": "Ele jura ter destruído a Chronicle Key, mas, diante\ndos seus fiascos passados, prefiro não botar fé alguma.",
        "verdict": "rewritten",
        "rationale": "Desconfiança fria e calculista do conspirador perante os erros de Bourd."
    },
    {
        "id": 3739,
        "curated_ptbr": "Quanto aos próximos passos, primeiro preciso conter\no avanço daquela corja dos Apóstolos de Elemia.",
        "verdict": "rewritten",
        "rationale": "Ódio visceral pelos Apóstolos (エレミアの使徒共)."
    },
    {
        "id": 3740,
        "curated_ptbr": "Vou armar uma cilada a partir desse ponto.\nFeito isso, poderei manipular a Aurica exatamente como bem entender.",
        "verdict": "rewritten",
        "rationale": "Arrogância manipuladora sobre a vulnerabilidade psicológica de Aurica."
    },
    {
        "id": 3741,
        "curated_ptbr": "Afinal de contas, uma sonhadora fracassada é o espécime\nmais facilmente manipulável da face da terra.",
        "verdict": "rewritten",
        "rationale": "Frieza desumana e crueldade de Falss reduzindo Aurica a um espécime biológico manipulável (落ちこぼれの妄想家などは、最も操りやすい傾向の生物に位置するのだから)."
    },
    {
        "id": 3742,
        "curated_ptbr": "Minha última providência foi concluída com êxito:\nescolhi o túmulo definitivo de Radolf e dos Apóstolos de Elemia.",
        "verdict": "rewritten",
        "rationale": "Vocabulário fúnebre solene do assassino conspirador (墓場を決定したのである)."
    },
    {
        "id": 3743,
        "curated_ptbr": "Uma queda fatal provocada pelo desabamento das ruínas nas entranhas da Colina Cantante.\nE os agentes sabotadores serão recrutados entre os próprios subordinados de Radolf.",
        "verdict": "rewritten",
        "rationale": "Planejamento minucioso do assassinato premeditado na Colina Cantante com traidores internos."
    },
    {
        "id": 3744,
        "curated_ptbr": "Se esta operação triunfar, não restará uma única alma viva\npara atrapalhar ou frustrar os meus desígnios.",
        "verdict": "rewritten",
        "rationale": "Expressão idiomática para 水を差す (jogar água fria / sabotar / frustrar planos)."
    },
    {
        "id": 3745,
        "curated_ptbr": "Haveria, porventura, regozijo mais esplêndido do que este?",
        "verdict": "rewritten",
        "rationale": "Pergunta retórica de triunfo sádico de Falss (これほど喜ばしい事が、他にあるだろうか)."
    },
    {
        "id": 3746,
        "curated_ptbr": "Resta apenas decidir como descartar o incompetente do Bourd...\nDe que maneira devo sepultá-lo...?",
        "verdict": "rewritten",
        "rationale": "Frio cálculo de descarte e execução de seu próprio cúmplice (どうやって葬ろうか)."
    },
    {
        "id": 3747,
        "curated_ptbr": "Na próxima vez em que eu registrar estas páginas,\neu terei o mundo inteiro sob o meu controle absoluto.",
        "verdict": "rewritten",
        "rationale": "Ambição megalomaníaca e tirânica de dominação global (この世界の全てを掌握している事だろう)."
    },
    {
        "id": 3748,
        "curated_ptbr": "A Guerra Santa está prestes a eclodir.\nA minha Guerra Santa contra Platina... a pátria que me baniu para o exílio.",
        "verdict": "rewritten",
        "rationale": "Ressentimento biográfico que move todas as ações de Falss contra sua terra natal."
    },
    {
        "id": 3749,
        "curated_ptbr": "Toda essa farsa ridícula do Trio de Elemia\nchegará ao seu fim definitivo no dia de hoje.",
        "verdict": "rewritten",
        "rationale": "Desprezo pelo culto religioso que ele próprio lidera como bispo falso (くだらない偽り事)."
    },
    {
        "id": 3750,
        "curated_ptbr": "Abençoada seja a Era de Mir,\nque despontará triunfante junto à alvorada de amanhã...",
        "verdict": "rewritten",
        "rationale": "Clímax arrepiante do diário de Falss profetizando o domínio do vírus de Mir."
    }
]

# Load input for original comparison
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_014_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)
inp_map = {d["id"]: d for d in input_data["dialogues"]}

hard_gate_errors = 0
lint_warnings = 0

for item in b6:
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

print(f"Batch 6 check complete: {len(b6)} items, {hard_gate_errors} hard gate errors, {lint_warnings} lint warnings.")

if hard_gate_errors == 0 and lint_warnings == 0:
    out_file = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch6_014.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(b6, f, indent=2, ensure_ascii=False)
    print(f"Saved {out_file}")

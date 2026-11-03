import json
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

b2 = [
    {
        "id": 3521,
        "curated_ptbr": "Que foi? Quer ouvir sobre a síntese Grathmeld outra vez?",
        "verdict": "rewritten",
        "rationale": "Adota 'síntese Grathmeld' conforme glossário mestre e tom de mestre alquimista veterano (なんじゃ)."
    },
    {
        "id": 3522,
        "curated_ptbr": "Muito bem, vou te ensinar usando\no [Healy C] como exemplo prático.",
        "verdict": "rewritten",
        "rationale": "Fluidez natural de Pombad instruindo seu pupilo."
    },
    {
        "id": 3523,
        "curated_ptbr": "Primeiro, selecione o item que deseja sintetizar.",
        "verdict": "rewritten",
        "rationale": "Precisão terminológica com 'sintetizar' no contexto de Grathmeld."
    },
    {
        "id": 3524,
        "curated_ptbr": "Neste caso, queremos o [Healy C], então é este aqui.\nPressione o botão IM00 para confirmar.",
        "verdict": "rewritten",
        "rationale": "BLINDAGEM DE TOKEN: preserva rigorosamente o botão IM00 com instrução didática viva."
    },
    {
        "id": 3525,
        "curated_ptbr": "Em seguida, vamos conferir os ingredientes.",
        "verdict": "rewritten",
        "rationale": "Eufonia de manual de alquimia (材料 = ingredientes/materiais)."
    },
    {
        "id": 3526,
        "curated_ptbr": "Se faltar algum ingrediente, terá que juntar mais\ncomprando nas lojas ou derrotando inimigos.",
        "verdict": "rewritten",
        "rationale": "Ritmo oral dinâmico de tutorial sem sobrecarga de orações intercaladas."
    },
    {
        "id": 3527,
        "curated_ptbr": "Desta vez abrirei uma exceção:\neu mesmo preparei os ingredientes para você.",
        "verdict": "rewritten",
        "rationale": "Generosidade paternalista típica do ancião Pombad (特別に、ワシが材料を用意してやった)."
    },
    {
        "id": 3528,
        "curated_ptbr": "Obteve o item [Pedra Azul]!",
        "verdict": "rewritten",
        "rationale": "Padronização canônica de caixas de aquisição de itens do sistema."
    },
    {
        "id": 3529,
        "curated_ptbr": "Obteve o Cristal Grathnode [Canção +10%]!",
        "verdict": "rewritten",
        "rationale": "Nomenclatura canônica e concisa de cristal Grathnode, evitando quebra truncada."
    },
    {
        "id": 3530,
        "curated_ptbr": "Pronto, agora já podemos dar prosseguimento à síntese.",
        "verdict": "rewritten",
        "rationale": "Dicção acadêmica do veterano de Grathmeld."
    },
    {
        "id": 3531,
        "curated_ptbr": "Sempre que a receita exigir um Cristal Grathnode,\nvocê deve escolher qual cristal específico utilizará.",
        "verdict": "rewritten",
        "rationale": "Clareza didática sem repetições viciosas de 'quando você...'."
    },
    {
        "id": 3532,
        "curated_ptbr": "Afinal, o atributo de pureza e qualidade do Cristal Grathnode\ninfluencia diretamente o resultado final da peça.",
        "verdict": "rewritten",
        "rationale": "Evita repetição cacofônica de 'qualidade do item' e confere elegância explicativa."
    },
    {
        "id": 3533,
        "curated_ptbr": "Muito bem, cristal escolhido!\nPor fim, basta definir quantas unidades deseja fabricar.",
        "verdict": "rewritten",
        "rationale": "Sequenciamento didático de menu sem truncamentos."
    },
    {
        "id": 3534,
        "curated_ptbr": "Feito isso, resta apenas iniciar a criação!\nVamos, experimente!",
        "verdict": "rewritten",
        "rationale": "Incentivo jovial do mestre Pombad."
    },
    {
        "id": 3535,
        "curated_ptbr": "Consegui!",
        "verdict": "approved_as_is",
        "rationale": "Exclamação precisa e canônica de sucesso de Lyner."
    },
    {
        "id": 3536,
        "curated_ptbr": "Oh, esplêndido trabalho!!",
        "verdict": "rewritten",
        "rationale": "Admiração efusiva de Pombad (見事じゃ)."
    },
    {
        "id": 3537,
        "curated_ptbr": "E assim temos o seu primeiro [Healy C] concluído.",
        "verdict": "rewritten",
        "rationale": "Conclusão didática harmoniosa."
    },
    {
        "id": 3538,
        "curated_ptbr": "Se bater qualquer dúvida no futuro,\nvenha me procurar quando quiser.",
        "verdict": "rewritten",
        "rationale": "Acolhimento caloroso de Pombad."
    },
    {
        "id": 3539,
        "curated_ptbr": "Hum...",
        "verdict": "rewritten",
        "rationale": "Padronização de interjeição de curiosidade do idoso."
    },
    {
        "id": 3540,
        "curated_ptbr": "Vejamos... Como terá ficado o gostinho?",
        "verdict": "rewritten",
        "rationale": "Fiel ao contexto japonês (出来の方はどうかの?), no qual Pombad examina o resultado para provar a poção."
    },
    {
        "id": 3541,
        "curated_ptbr": "Ei, espera aí!",
        "verdict": "rewritten",
        "rationale": "Reação imediata de susto de Lyner ao ver o velho tomar o frasco da sua mão."
    },
    {
        "id": 3542,
        "curated_ptbr": "Glub, glub... Aaaah! Hum, até que não ficou ruim!",
        "verdict": "rewritten",
        "rationale": "HARD GATE CRÍTICO: EXPURGO TOTAL DE RUBRICA TEATRAL (*glug*). Converte em onomatopeias e vocalizações orais naturais brasileiras."
    },
    {
        "id": 3543,
        "curated_ptbr": "Ah, é verdade! Na síntese Grathmeld, procure sempre utilizar\nCristais Grathnode da mais alta qualidade possível.",
        "verdict": "rewritten",
        "rationale": "Fluidez natural de conselho de alquimia sem repetições pesadas."
    },
    {
        "id": 3544,
        "curated_ptbr": "Pois quanto mais puro for o cristal,\nmais potente e refinado será o artefato produzido.",
        "verdict": "rewritten",
        "rationale": "Elimina o eco deselegante de 'qualidade... qualidade', mantendo a lição conceitual de síntese."
    },
    {
        "id": 3545,
        "curated_ptbr": "Grave bem isso na sua cabeça, rapaz.",
        "verdict": "rewritten",
        "rationale": "Dicção ranzinza e experiente de Pombad."
    },
    {
        "id": 3546,
        "curated_ptbr": "Mas era o Healy C que eu acabei de criar...",
        "verdict": "rewritten",
        "rationale": "Lamento cômico e desolado de Lyner vendo sua primeira poção bebida por outro."
    },
    {
        "id": 3547,
        "curated_ptbr": "Cala a boca! Os ingredientes eram meus!\nO que tem de errado em eu tomar o meu próprio remédio?!",
        "verdict": "rewritten",
        "rationale": "Explosão caricata de indignação do velho Pombad (カーッ!)."
    },
    {
        "id": 3548,
        "curated_ptbr": "Ai, ai... Ninguém merece...",
        "verdict": "rewritten",
        "rationale": "Resgata o clássico lamento de derrota cômica de anime (トホホ...), superando o raso 'hum... não'."
    },
    {
        "id": 3549,
        "curated_ptbr": "Muuu~!",
        "verdict": "rewritten",
        "rationale": "Onomatopeia bovina canônica em português brasileiro."
    },
    {
        "id": 3550,
        "curated_ptbr": "Deseja ordenhar e colher o leite?",
        "verdict": "rewritten",
        "rationale": "Fiel ao japonês técnico ミルクを採取しますか? (coleta de matéria-prima de síntese)."
    },
    {
        "id": 3551,
        "curated_ptbr": "Obteve o item Megamilk!",
        "verdict": "rewritten",
        "rationale": "Padronização canônica de obtenção de itens."
    },
    {
        "id": 3552,
        "curated_ptbr": "Muuu~",
        "verdict": "rewritten",
        "rationale": "Mugido dócil e satisfeito da vaca."
    },
    {
        "id": 3553,
        "curated_ptbr": "Com licença, posso te fazer uma pergunta...?",
        "verdict": "rewritten",
        "rationale": "Abordagem educada e oralidade natural de Lyner."
    },
    {
        "id": 3554,
        "curated_ptbr": "Eu só sirvo para pegar pesado, amigo.\nNão entendo patavina dessas coisas complicadas!",
        "verdict": "rewritten",
        "rationale": "Expressividade viva do trabalhador braçal (力仕事勝負 / サッパリだ)."
    },
    {
        "id": 3555,
        "curated_ptbr": "Aquele poder...",
        "verdict": "rewritten",
        "rationale": "Ajuste dêitico correto (あの力 = aquele poder distante que testemunhou)."
    },
    {
        "id": 3556,
        "curated_ptbr": "Heh... A sorte finalmente sorriu para mim.",
        "verdict": "rewritten",
        "rationale": "Frase estilosa de quem fareja uma grande oportunidade (ツキが回ってきたぜ)."
    },
    {
        "id": 3557,
        "curated_ptbr": "Com licença, posso te pedir uma informação...?",
        "verdict": "rewritten",
        "rationale": "Polidez investigativa em busca de componentes para o Dive Shop."
    },
    {
        "id": 3558,
        "curated_ptbr": "Hum... Energia condutiva, é?",
        "verdict": "rewritten",
        "rationale": "Adota o conceito canônico de condução de ondas sonoras (導力)."
    },
    {
        "id": 3559,
        "curated_ptbr": "Se estamos falando de um item que emite energia condutiva,\no primeiro que me vem à mente é o Power Sourcer...",
        "verdict": "rewritten",
        "rationale": "Termo técnico Power Sourcer mantido em destaque com fraseado elegante."
    },
    {
        "id": 3560,
        "curated_ptbr": "Mas o pessoal comenta que a potência dele\né fraca demais para dar conta do recado...",
        "verdict": "rewritten",
        "rationale": "Conclusão conversacional fluida e cética da vendedora experiente."
    }
]

# Load input for original comparison
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_014_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)
inp_map = {d["id"]: d for d in input_data["dialogues"]}

hard_gate_errors = 0
lint_warnings = 0

for item in b2:
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

print(f"Batch 2 check complete: {len(b2)} items, {hard_gate_errors} hard gate errors, {lint_warnings} lint warnings.")

if hard_gate_errors == 0 and lint_warnings == 0:
    out_file = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_014.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(b2, f, indent=2, ensure_ascii=False)
    print(f"Saved {out_file}")

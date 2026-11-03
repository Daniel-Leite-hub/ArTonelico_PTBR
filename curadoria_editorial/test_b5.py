import json
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

b5 = [
    {
        "id": 3659,
        "curated_ptbr": "Este lugar é...",
        "verdict": "rewritten",
        "rationale": "Ajuste dêitico de localização física espacial (ここは...)."
    },
    {
        "id": 3660,
        "curated_ptbr": "Parece que adentramos um novo setor da Torre.",
        "verdict": "rewritten",
        "rationale": "Vocabulário militar preciso de Radolf (新しい区画)."
    },
    {
        "id": 3661,
        "curated_ptbr": "Então este é o Jardim dos Prismas...?",
        "verdict": "rewritten",
        "rationale": "Adota 'Jardim dos Prismas' (プリズムガーデン - Prism Garden) com tom contemplativo."
    },
    {
        "id": 3662,
        "curated_ptbr": "Se não me engano... Era esta porta aqui...",
        "verdict": "rewritten",
        "rationale": "Hesitação investigativa de Misha procurando o esconderijo antigo."
    },
    {
        "id": 3663,
        "curated_ptbr": "Mas que porta velha, hein...",
        "verdict": "rewritten",
        "rationale": "Observação direta e espontânea de Lyner."
    },
    {
        "id": 3664,
        "curated_ptbr": "Dizem que era a passagem de serviço usada\nna época em que o Beco Vagalume recém havia flutuado nos céus.",
        "verdict": "rewritten",
        "rationale": "Lore histórica sobre a elevação flutuante de Sol Ciel e Beco Vagalume sem colchetes colidentes."
    },
    {
        "id": 3665,
        "curated_ptbr": "Por isso ficou abandonada. E é exatamente por esse motivo\nque virou um esconderijo perfeito... Entendeu o raciocínio?",
        "verdict": "rewritten",
        "rationale": "Orgulho brincalhão e sagaz de Misha (故に穴場...というわけです)."
    },
    {
        "id": 3666,
        "curated_ptbr": "Até tem um trinco, mas é só para inglês ver...",
        "verdict": "rewritten",
        "rationale": "Expressão idiomática brasileira rica para お情け程度 (por mera formalidade / para inglês ver)."
    },
    {
        "id": 3667,
        "curated_ptbr": "Vamos, depressa! Se alguém nos flagrar aqui, estamos fritos!",
        "verdict": "rewritten",
        "rationale": "Urgência conspiratória fofa e enérgica de Misha."
    },
    {
        "id": 3668,
        "curated_ptbr": "Não tenho nada para resolver lá fora agora...",
        "verdict": "rewritten",
        "rationale": "Naturalidade de pensamento de exploração (外に出る用事は無いな)."
    },
    {
        "id": 3669,
        "curated_ptbr": "Ah, senhorita Misha!\nVeio aqui para ficar grandona de novo?",
        "verdict": "rewritten",
        "rationale": "Cortesia alegre e afetuosa do operador da máquina (大きくなりに来たんですか)."
    },
    {
        "id": 3670,
        "curated_ptbr": "Compreendido!\nVamos iniciar o processo imediatamente!",
        "verdict": "rewritten",
        "rationale": "Disposição enérgica e profissional de operador técnico."
    },
    {
        "id": 3671,
        "curated_ptbr": "Preparar para acionamento!\nTerceiro Reator, ativar!",
        "verdict": "rewritten",
        "rationale": "Comando técnico formal de ativação de reator da Torre (三号炉、起動!)."
    },
    {
        "id": 3672,
        "curated_ptbr": "Quando quiser voltar a ser pequenininha, é só passar aqui!\nHehehe.",
        "verdict": "rewritten",
        "rationale": "Risinho cúmplice e simpático ao concluir a alternância de forma."
    },
    {
        "id": 3673,
        "curated_ptbr": "Vou ficar vadiando por aqui mais um pouco.\nSe pintar qualquer bronca, é só me dar um grito.",
        "verdict": "rewritten",
        "rationale": "Estilo malandro e despojado inconfundível de Jack (ブラブラしてる / 呼んでくれ)."
    },
    {
        "id": 3674,
        "curated_ptbr": "Bem... Fico contente que venha me visitar tantas vezes, mas...\nJuro que não tem nada de novo por aqui, sabia?",
        "verdict": "rewritten",
        "rationale": "Desconcerto meigo e fofo de Shurelia perante a insistência do jogador/Lyner."
    },
    {
        "id": 3675,
        "curated_ptbr": "Mil perdões... É que acabo entrando aqui sem nem perceber...",
        "verdict": "rewritten",
        "rationale": "Timidez desajeitada e simpática de Lyner (ついつい入っちゃって)."
    },
    {
        "id": 3676,
        "curated_ptbr": "A-ah, compreendo...",
        "verdict": "rewritten",
        "rationale": "Reação tímida e atônita de Shurelia (は、はあ...)."
    },
    {
        "id": 3677,
        "curated_ptbr": "Primeiro, precisamos instalar a canção Re-Nation na Aurica.",
        "verdict": "rewritten",
        "rationale": "Adequação ao vocabulário de instalação/download de canções de Ar tonelico sem colchetes perigosos."
    },
    {
        "id": 3678,
        "curated_ptbr": "Vamos até a Catedral pedir autorização\npara realizar a cerimônia.",
        "verdict": "rewritten",
        "rationale": "Contexto sagrado da Igreja de Elemia (大聖堂)."
    },
    {
        "id": 3679,
        "curated_ptbr": "Ora, olá, Lyner! Uma boa noite para você.",
        "verdict": "rewritten",
        "rationale": "Cortesia etérea e graciosa da guardiã floral."
    },
    {
        "id": 3680,
        "curated_ptbr": "Continua esperando o navio ancorar, pelo visto.",
        "verdict": "rewritten",
        "rationale": "Cumprimento amigável e observador de Lyner no cais mental."
    },
    {
        "id": 3681,
        "curated_ptbr": "Sim, claro! Afinal de contas,\nnunca se sabe quando ele pode despontar no horizonte.",
        "verdict": "rewritten",
        "rationale": "Ajuste de gênero (o navio / 船) e cadência suave."
    },
    {
        "id": 3682,
        "curated_ptbr": "Mas não posso negar que ficar aqui plantada é um tédio só...",
        "verdict": "rewritten",
        "rationale": "Trocadilho sutil e fofo de planta entediada (暇なことは暇なのよね)."
    },
    {
        "id": 3683,
        "curated_ptbr": "...Já sei! Tive uma ideia brilhante!\nLyner, o que acha de cultivar uma plantinha comigo?",
        "verdict": "rewritten",
        "rationale": "Entusiasmo repentino e proposta engenhosa."
    },
    {
        "id": 3684,
        "curated_ptbr": "...Uma flor?",
        "verdict": "approved_as_is",
        "rationale": "Pergunta curta e pontual mantida íntegra."
    },
    {
        "id": 3685,
        "curated_ptbr": "Sim, veja só esta florzinha!",
        "verdict": "rewritten",
        "rationale": "Apresentação animada da plantinha."
    },
    {
        "id": 3686,
        "curated_ptbr": "...",
        "verdict": "rewritten",
        "rationale": "Reticências padronizadas."
    },
    {
        "id": 3687,
        "curated_ptbr": "Ué?! V-você tem certeza de que isso é uma flor?!",
        "verdict": "rewritten",
        "rationale": "Reação cômica de choque ao ver a forma bizarra da brotadeira."
    },
    {
        "id": 3688,
        "curated_ptbr": "Ué, como não? Olha para ela, é uma florzinha cuspida e escarrada!\nEu a encontrei num canto do distrito dos armazéns outro dia e trouxe para cá.",
        "verdict": "rewritten",
        "rationale": "Teimosia divertida e admissão cândida de apropriação (倉庫街の一角に置いてあったのを持って来ちゃったの)."
    },
    {
        "id": 3689,
        "curated_ptbr": "M-mas você podia fazer isso?!\nPegar as coisas dos outros assim sem pedir...",
        "verdict": "rewritten",
        "rationale": "Repreensão moral embaraçada de Lyner (勝手に持って来ちゃって)."
    },
    {
        "id": 3690,
        "curated_ptbr": "Sempre foi minha, para começo de conversa! Fique tranquilo.",
        "verdict": "rewritten",
        "rationale": "Despreocupação descarada e reconfortante (元々私のよ)."
    },
    {
        "id": 3691,
        "curated_ptbr": "E o que eu tenho que fazer, afinal?",
        "verdict": "rewritten",
        "rationale": "Pragmatismo cooperativo de Lyner."
    },
    {
        "id": 3692,
        "curated_ptbr": "Venha regá-la com água de vez em quando.\nMas não basta só molhar, viu? Precisa regar com uma dose caprichada de amor!",
        "verdict": "rewritten",
        "rationale": "Lição carinhosa e metafórica sobre os vínculos da Cosmosfera."
    },
    {
        "id": 3693,
        "curated_ptbr": "Entendi o recado. Tudo bem, vamos cuidar dela.\nBasta eu passar aqui para regar de tempos em tempos, certo?",
        "verdict": "rewritten",
        "rationale": "Aceitação simpática e calorosa de Lyner."
    },
    {
        "id": 3694,
        "curated_ptbr": "Isso mesmo! Conto com você.",
        "verdict": "rewritten",
        "rationale": "Confirmação alegre do trato."
    },
    {
        "id": 3695,
        "curated_ptbr": "O navio já atracou no porto, mas você preferiu continuar aqui, né?",
        "verdict": "rewritten",
        "rationale": "Constatação serena do afeto da fadinha pelo local."
    },
    {
        "id": 3696,
        "curated_ptbr": "Sim... É que no fim das contas, tenho um apego especial por este cais.",
        "verdict": "rewritten",
        "rationale": "Doçura reflexiva e sentimental da guardiã espiritual da mente de Misha."
    }
]

# Load input for original comparison
with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_014_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)
inp_map = {d["id"]: d for d in input_data["dialogues"]}

hard_gate_errors = 0
lint_warnings = 0

for item in b5:
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

print(f"Batch 5 check complete: {len(b5)} items, {hard_gate_errors} hard gate errors, {lint_warnings} lint warnings.")

if hard_gate_errors == 0 and lint_warnings == 0:
    out_file = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_014.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(b5, f, indent=2, ensure_ascii=False)
    print(f"Saved {out_file}")

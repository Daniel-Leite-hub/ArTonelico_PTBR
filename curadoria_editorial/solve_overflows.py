import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

proposals = {
    # 24354 (lim 64B) -> JP: もう欲しいものは無いよ。
    24354: [
        "Não quero mais nada de você.",
        "Não há mais nada que eu queira",
        "Não tenho mais nada a querer.",
        "Não quero mais nada por hoje.",
    ],
    # 24369 (lim 80B) -> JP: おいおい、金が足りてねえよ。
    24369: [
        "Ei, ei, sua grana não dá nem pro gasto!",
        "Ei, ei, sua grana não dá!",
        "Ei, ei, você não tem dinheiro!",
        "Ei, a sua grana não dá!",
    ],
    # 24396 (lim 72B) -> JP: おいおい、もう持てないじゃないか。
    24396: [
        "Ei, você não aguenta levar mais!",
        "Ei, você já não aguenta levar mais!",
        "Ei, ei, não cabe mais nada aí!",
    ],
    # 24481 (lim 104B) -> JP: ここに入るにはCR%sDP必要です。CRアクセスしますか?
    24481: [
        "Custa CR%s DP para entrar.CRDeseja acessar?",
        "Requer CR%s DP para entrar.CRAcessar?",
        "Requer CR%s DP para entrar.CRDeseja acessar?",
    ],
    # 24500 (lim 144B) -> JP: 何を今更!CR拙者はオリカさんの心の護だと言っているであろう!
    24500: [
        "Que pergunta!CRJá disse que sou o Guardião da Mentedela!",
        "Que pergunta!CRJá cansei de dizer que sou o Guardiãoda Mente de Aurica!",
        "Que pergunta!CRJá disse: sou o Guardião da Mente daAurica!",
        "Que pergunta!CRSou o Guardião da Mente da Aurica!",
    ],
    # 24504 (lim 168B) -> JP: ...ふん。拙者は確かにぬいぐるみだ。CRオリカさんが大切にしてくれていたCRぬいぐるみである。
    24504: [
        "...Hmph. Sou de pelúcia, sim!CRUm bicho que a senhorita Auricasempre guardou com carinho.",
        "...Hmph. Sou de pelúcia, sim!CRA pelúcia favorita da Aurica!",
        "...Hmph. Sou de pelúcia, sim!CRUm bichinho que Aurica cuidavacom todo carinho.",
        "...Hmph. Sou mesmo uma pelúcia!CRUm bichinho que Aurica guardavacom todo o carinho.",
    ],
    # 24505 (lim 136B) -> JP: な、本当にそうだったのか!CRなぜぬいぐるみが心の護に...。
    24505: [
        "E-era verdade?!CRMas por que uma pelúcia virariaGuardião...?",
        "E-era verdade?!CRMas como uma pelúcia vira Guardião?",
        "E-era verdade?!CRMas por que um bicho de pelúcia virouGuardião da Mente...?",
    ],
    # 24506 (lim 160B) -> JP: それくらい自分で解き明かせバカモノ。CR一つ言えることは、それだけオリカさんにCRとって、拙者は大切な存在だということだ。
    24506: [
        "Descubra só, tolo!CRSó digo isto: sou a criatura maisimportante para ela!",
        "Descubra só, tolo!CRSó digo isto: sou importantíssimo paraa senhorita Aurica!",
        "Descubra só, tolo!CRSó digo uma coisa: sou importantíssimopara Aurica!",
    ],
    # 24509 (lim 104B) -> JP: そういえば...どんすけは、いつ頃からCRオリカの心の護なんだ?
    24509: [
        "E há quanto tempo você é o Guardiãoda Mente dela?",
        "Há quanto tempo você é o Guardião daMente dela?",
        "Don Leon... há quanto tempo é oGuardião dela?",
    ],
    # 24523 (lim 144B) -> JP: しかし貴様...よくまあこれだけ頻繁にオリカさんの心にダイブしてくるモンだ。CR何故そこまでする!
    24523: [
        "Você mergulha tanto na mente dela...Por que faz isso?!",
        "Mergulha na mente dela com tantafrequência... Por que faz isso?!",
        "Você mergulha tanto na mente dela!Por que faz isso, afinal?!",
    ],
    # 24525 (lim 104B) -> JP: 何故そこまでオリカさんの心にCRダイブするのか、と聞いているのだ!
    24525: [
        "Perguntei por que você mergulhatanto na mente dela!",
        "Estou perguntando por que vocêmergulha tanto nela!",
        "Perguntei por que você mergulhatanto nela!",
    ],
    # 24528 (lim 112B) -> JP: ...ふ、ふん。CRそれしきのことで、オリカさんが貴様に振り向くなどと思うなよ!
    24528: [
        "...H-hmph! Não pense que ela vaigostar de você só por isso!",
        "...Hmph! Não ache que ela vai tegostar só por isso!",
        "...Hmph! Não pense que ela vai teamar só por isso!",
    ],
    # 24530 (lim 80B) -> JP: まあいい。CR...せいぜい頑張るんだな。
    24530: [
        "Tanto faz.CR...Dê o seu melhor, então.",
        "Tanto faz.CR...Esforce-se, então.",
        "Seja como for.CR...Boa sorte, então.",
    ],
    # 24533 (lim 216B) -> JP: ...しかし、アレだ。CR拙者がこう言うのも何だが...オリカさんは他のレーヴァテイルよりも心の傷が深い。
    24533: [
        "...Mas escute. Não cabe a mim falar,mas Aurica tem feridas bem maisfundas que as outras Reyvateils.",
        "...Mas escute. Não cabe a mim falar,mas Aurica tem feridas no coraçãobem mais fundas que as outras.",
        "...Mas escute. Não cabe a mim dizer,mas Aurica tem feridas na mente maisprofundas que as outras.",
    ],
    # 24534 (lim 112B) -> JP: それ故、強い魔法を紡ぐのにも多大な労力がいるんじゃないか?
    24534: [
        "Por isso, tecer magias fortes custatanto, não acha?",
        "Por isso, tecer magias fortes exigeum esforço enorme, né?",
        "Por isso é tão difícil tecer magiaspoderosas, não acha?",
    ],
    # 24537 (lim 88B) -> JP: ...というか、貴様...そもそも他のレーヴァテイルにもダイブしてるのか?
    24537: [
        "...Você mergulha em outras garotastambém?",
        "...Você mergulha em outrasReyvateils?",
        "...Diga, você mergulha em outrasReyvateils?",
    ],
    # 24550 (lim 40B) -> JP: オリカさんは面食いなのだ!
    24550: [
        "Aurica só quer galãs!",
        "Ela só quer galãs!",
        "Ela prefere galãs!",
        "Ela só curte galãs!",
    ],
    # 24557 (lim 64B) -> JP: しかし、悪いヤツではない...。
    24557: [
        "Mas... você não é um cara mau.",
        "Mas... você não é má pessoa.",
        "Mas... você até que é legal.",
    ],
    # 24567 (lim 128B) -> JP: なんで自重しないといけないんだ?CRオリカが嫌がってるのか?CRそれなら自重するけどさ...
    24567: [
        "Por que parar? Aurica reclamou?CRSe for o caso, eu me afasto...",
        "Por que parar? Ela reclamou?CRSe for o caso, eu dou um tempo...",
        "Por que evitar? Ela reclamou?CRSe for o caso, eu me afasto...",
    ],
    # 24573 (lim 152B) -> JP: 貴様に拙者の何がわかるというのだ!CR心の護は、いかなる手段をとろうとも、CR心を護らなければならない!
    24573: [
        "O que você sabe sobre mim?! O Guardiãodeve protegê-la a qualquer custo!",
        "O que você sabe de mim?! O Guardiãodeve protegê-la a qualquer custo!",
        "O que sabe de mim?! O Guardião deveproteger a mente a todo custo!",
    ],
    # 24575 (lim 24B) -> JP: 過去...!?
    24575: [
        "Passado...?",
        "Passado...?!",  # test
        "Passado?!",
        "O passado?",
    ],
    # 24582 (lim 104B) -> JP: お前自身も、すごい大きな心の傷を持ってCRいるんだな...。
    24582: [
        "Você também carrega feridas fundasno peito, né...?",
        "Você também carrega uma ferida enormeno peito, né?",
        "Você também tem feridas fundas nocoração, né...?",
    ],
    # 24591 (lim 112B) -> JP: 俺の力じゃないよ。オリカが自分の力でここまで来たんだ。
    24591: [
        "Não foi por mim. Aurica chegou aquipor conta própria.",
        "Não foi por mim. Aurica chegou aquipela própria força.",
        "Não foi por mim. Aurica chegou aquicom sua própria força.",
    ],
    # 24626 (lim 112B) -> JP: 貴様、最近オリカさんが寝不足気味なのをCR知っているか?
    24626: [
        "Sabia que Aurica tem tido crisesde insônia ultimamente?!",
        "Sabia que Aurica anda sem dormirultimamente?!",
        "Sabia que Aurica anda com insôniaultimamente?!",
    ],
    # 24629 (lim 72B) -> JP: そ、そんなこと無いって!CRでも、何が原因なんだろう...。
    24629: [
        "C-claro que cuido!CRQual será a causa...?",
        "C-claro que cuido!CRE por que será...?",
        "C-claro que cuido!CRMas o que houve...?",
    ],
}

limits = {
    24354: 64, 24369: 80, 24396: 72, 24481: 104, 24500: 144, 24504: 168,
    24505: 136, 24506: 160, 24509: 104, 24523: 144, 24525: 104, 24528: 112,
    24530: 80, 24533: 216, 24534: 112, 24537: 88, 24550: 40, 24557: 64,
    24567: 128, 24573: 152, 24575: 24, 24582: 104, 24591: 112, 24626: 112,
    24629: 72
}

for d_id, opts in proposals.items():
    lim = limits[d_id]
    print(f"=== ID {d_id} (Limit: {lim}B) ===")
    for opt in opts:
        sz = encoded_size(opt)
        diff = sz - lim
        status = "OK" if diff <= 0 else f"OVERFLOW (+{diff}B)"
        print(f"  [{status:15s}] (sz {sz:3d}B) -> '{opt}'")

extra_tests = [
    (24528, 112, "...Hmph! Não pense que ela vai teolhar só por isso!"),
    (24528, 112, "...Hmph! Não pense que ela vai tegostar só por isso!"),
    (24528, 112, "...Hmph! Não pense que ela vai darbola pra você só por isso!"),
    (24528, 112, "...Hmph! Não pense que Aurica vaigostar de você só por isso!"),
    (24528, 112, "...H-hmph! Não pense que ela vaite dar bola só por isso!"),
    (24528, 112, "...Hmph! Não pense que ela vaite dar moral só por isso!"),
    (24629, 72, "Eu cuido, sim!CRMas o que houve...?"),
    (24629, 72, "Eu cuido, sim!CRQual é o motivo...?"),
    (24629, 72, "Eu cuido, sim!CRE por que será...?"),
    (24629, 72, "C-claro que cuido!CRE por quê...?"),
    (24629, 72, "C-claro que cuido!CRPor que será?"),
]

print("\n--- EXTRA TESTS ---")
for d_id, lim, txt in extra_tests:
    sz = encoded_size(txt)
    diff = sz - lim
    status = "OK" if diff <= 0 else f"OVERFLOW (+{diff}B)"
    print(f"[{status:15s}] ID {d_id} ({sz:3d}B <= {lim}B) -> '{txt}'")

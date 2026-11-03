import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

lines_0247 = {
    # 26090: Max 136
    # JP: それでも、最近は少しだけ自身がCR持てるようになってきてはいるんだけどね。
    # EN: But lately, I’m starting to feel a little more confident in myself.
    26090: ("Mas ultimamente comecei a terCRum pouco mais de confiança em mim.", 136),

    # 26091: Max 104
    # JP: ライナーがダイブする度に、どんどん魔法を使えるようになっているから、ね...。
    # EN: Every time you dive, I learn more and more Songs.
    26091: ("Sempre que mergulha, aprendoCRmais e mais Magias da Canção...", 104),

    # 26092: Max 96
    # JP: そうだ、どんすけの話をしてあげるよ。
    # EN: Oh yeah, I’ll tell you a little about Don Leon.
    26092: ("Ah, sim! Vou te contarCRum pouco sobre o Don Leon.", 96),

    # 26093: Max 152
    # JP: あたしがクレアお姉ちゃんからもらったCRぬいぐるみなんだけどね、凄く可愛くてCRかっこいいんだよ!
    # EN: He’s a stuffed animal that Claire gave me, but he’s so cute and handsome!
    26093: ("É um bicho de pelúcia que a ClaireCRme deu, mas é super fofo e maneiro!", 152),

    # 26094: Max 64
    # JP: へ、へえ...可愛くてかっこいい、ね...。
    # EN: ...Cute and handsome...right.
    26094: ("É... fofo e maneiro... sei.", 64),

    # 26095: Max 40
    # JP: ん、どうしたの?
    # EN: Huh, what’s wrong?
    26095: ("Ué, o que foi?", 40),

    # 26096: Max 96
    # JP: あ、いや、なんでもないって。CRそんなに好きだったのか?
    # EN: Oh, no, nothing. You really like him that much?
    26096: ("Não, nada. Você gostavaCRtanto assim dele?", 96),

    # 26097: Max 64
    # JP: うん。だって、ずっとあたしの心の支えにCRなってくれてたんだもん。
    # EN: Yeah, he really supported me.
    26097: ("Sim. Ele sempre foiCRo meu porto seguro.", 64),

    # 26098: Max 192
    # JP: お姉ちゃんにもらってから、CRずっと大事にしてたんだけどね...CRやっぱり持ってくる気にはなれなくて...。
    # EN: I took care of him ever since Claire gave him to me. But, I just couldn’t bring him along...
    26098: ("Cuidei dele com carinho desde que a ClaireCRme deu... mas não tive coragemCRde trazer ele comigo...", 192),

    # 26099: Max 104
    # JP: でも、今もちゃんとあるんだよ...CRあたしの昔住んでいた家にだけどね。
    # EN: ...I still have him. I keep him at my old house.
    26099: ("Mas ele ainda tá lá...CRna casa onde eu morava.", 104),

    # 26100: Max 88
    # JP: そういやオリカ、なんか具合悪いところとかそういうの、無いか?
    # EN: By the way Aurica, are you feeling okay?
    26100: ("Aurica, você não tá se sentindoCRmal nem nada?", 88),

    # 26101: Max 64
    # JP: え?別になんとも無いけど、どうかしたの?
    # EN: Huh? I feel fine, what’s wrong?
    26101: ("Hã? Tô ótima, por que a pergunta?", 64),

    # 26102: Max 184
    # JP: あ、いやさ、こんな旅生活だからCR体調不良とか起こしてないかなってCR思っただけだよ。
    # EN: Uh, well, we travel so much and I was worried that you might be feeling sick or something.
    26102: ("É que a gente vive viajando,CRfiquei com medo de vocêCRacabar passando mal.", 184),

    # 26103: Max 72
    # JP: ...ありがと。でも、あたしは全然平気だから大丈夫だよ。
    # EN: ...Thanks, but I’m perfectly fine.
    26103: ("Obrigada. Mas eu tô bem,CRnão se preocupe.", 72),

    # 26104: Max 40
    # JP: そ、そうか?それだったら良いんだけどさ。
    # EN: Okay. That’s good.
    26104: ("É? Que bom, então.", 40),

    # 26105: Max 128
    # JP: ライナー、どんすけをプレゼントしてくれて、本当にありがとうね。
    # EN: Lyner, thank you so much for giving me a Don Leon as a present.
    26105: ("Lyner, muito obrigada mesmoCRpor me dar um Don Leon de presente.", 128),

    # 26106: Max 32
    # JP: いや、良いってこれくらい。
    # EN: Oh, no problem.
    26106: ("Que isso, imagina.", 32),

    # 26107: Max 160
    # JP: ってか、わざわざ思い出として自分の故郷に置いてきた人形だろ、これ?
    # EN: But didn’t you leave him in Skuwat so that he wouldn’t remind you of your past?
    26107: ("Mas não era esse o bonecoCRque você deixou na sua terraCRcomo lembrança?", 160),

    # 26108: Max 192
    # JP: そんな思い出にしたいと思ってるものをCR作って本当に良かったのか、正直不安CRだったよ。
    # EN: Honestly, I was worried about making something that you wanted to stay deep in your memories.
    26108: ("Fiquei até na dúvida se fiz bemCRem criar algo que você queria guardarCRsó na memória.", 192),

    # 26109: Max 56
    # JP: そんなことないよ。あたし、凄い嬉しい。
    # EN: Oh, no. I’m really happy.
    26109: ("Imagina! Eu fiquei tão feliz...", 56),

    # 26110: Max 184
    # JP: 本当はあたし、ずっと寂しかったから...CRだからライナーがこれを作ってくれたとき、本当に嬉しかった。
    # EN: I was actually feeling a little lonely...so when you made this for me, I was really happy.
    26110: ("Eu me sentia tão sozinha...CREntão quando você fez isso pra mim,CRfiquei feliz de verdade.", 184),

    # 26111: Max 152
    # JP: それに、そのおかげであたし...なんだろう?変わった気がするの。
    # EN: And maybe because of that...how can I put this? I feel like I’ve changed.
    26111: ("E graças a isso... como posso dizer?CRSinto que mudei.", 152),

    # 26112: Max 120
    # JP: 誰かを信じよう、誰かになにかしてあげよう、って気持ちって言えばいいのかな?
    # EN: I want to believe in someone, and do things to help people.
    26112: ("Vontade de confiar em alguémCRe de ajudar os outros, sabe?", 120),

    # 26113: Max 176
    # JP: ちょっと前までそんな気持ちなんてCR忘れてたし...ううん、無かったのかもCRしれない...。
    # EN: I’d forgotten about those emotions. No, I probably just never felt those emotions...
    26113: ("Até pouco tempo atrás, eu tinhaCResquecido isso... ou talvez nemCRtivesse isso em mim...", 176),
}

for tid, (txt, maxb) in lines_0247.items():
    sz = encoded_size(txt)
    diff = sz - maxb
    status = "OK" if diff <= 0 else f"OVERFLOW (+{diff})"
    errs = validate_line(tid, "", txt)
    print(f"ID {tid}: {sz}B <= {maxb}B [{status}] {errs}")

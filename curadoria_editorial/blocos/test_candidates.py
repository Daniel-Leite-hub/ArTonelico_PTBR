# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size

tests = [
    (25804, 112, "Não, nada! É que cuidaram bem de mim.", "あ、いや、なんでも...とにかく、CR色々と世話になったからさ、それでだよ。"),
    (25812, 144, "Hahaha... Só não esquece deCRtirar o veneno do Babango...", "は、ははは...ババンゴとかいうやつのCR毒だけは、取り忘れないでくれよ...。"),
    (25813, 96, "O telescópio de lá era enorme, né?", "あの天文台にあった望遠鏡、大きいよね。"),
    (25823, 96, "Lyner...CRSabe o que significam as estátuas?", "ねえ、ライナー。CRあの像の意味知ってる?"),
    (25825, 112, "Acha que fariam estátuasCRsem nenhum motivo?", "そんな何の意味も無く像を建てるとCR思ったの?"),
    (25840, 32, "Ah... sim...", "あ...そっか...。"),
    (25855, 64, "Lá em cima deve ser mais seguro...", "やっぱり上の世界の方が安全なのかなぁ...。"),
    (25858, 96, "E enorme daquele jeito... Fiquei boba.", "それもあんなに大きいのが見れるだなんて、少し感激かな。"),
    (25864, 120, "Pensar nisso tudo no meio da crise já é ótimo.", "まあ、あの状況でそれだけ考えられたならCR良いんじゃないかな?"),
    (25870, 40, "E mais... ah...", "それにね...あ...。"),
    (25873, 56, "Chega, deu por hoje!", "も、もういいの、おしまい!"),
    (25877, 184, "Senti o mesmo ao descer aqui. Só via coisas que nunca vi lá em cima.", "俺が初めて下の世界に降りたときと同じだな。上の世界では見かけないような珍しいものCRばかりだったし。"),
    (25882, 104, "Sim... Queria te mostrar minha terra...", "うん...出来ることなら、今度はお返しにあたしの故郷を案内してあげたいんだけどね...。"),
    (25898, 16, "...É.", "...そっか。"),
    (25899, 104, "Logo você se acostuma com as Lojas.", "ま、まあ、そのうちあのダイブ屋のCR雰囲気にも慣れるよ。"),
    (25914, 112, "Só a Lady Shurelia... Mas ela não usa.", "い、いや...シュレリア様くらいかな?CR宿を利用することは無いけどさ...。"),
    (25918, 64, "O Suco de Comida é bom!", "あのメシジュースって、凄い美味しいよね。"),
    (25920, 40, "Por quê? É bom!", "どうして?あんなに美味しい食べ物なのに。"),
    (25925, 112, "Se você diz... É um mundo estranho.", "...そ、そうっすか...俺にはよくわからない世界だな、本当。"),
    (25927, 104, "Para! Só de pensar já me dá calafrio!", "やめてくれ、想像するだけでも怖いから、マジで!"),
    (25928, 88, "A Soda Churrasco... tava boa?", "前にあたしが作った焼肉ソーダ、CR美味しかった?"),
    (25938, 80, "Meus olhos doem.CRNão doeram, Lyner?", "目が痛くなっちゃったよ、あたし。CRライナーは大丈夫なの?"),
    (25951, 128, "Mas sendo Classe D sem parceiro, quase não ia.", "でも、あたしみたいなクラスDはパートナーなんかいなかったから、ミッションなんかCR無いに等しかったけどね。"),
    (25962, 24, "...Sim, senhora.", "...りょ、了解っす。"),
    (25992, 184, "A pessoa que eu queria conhecer era eu mesma... Que piada sem graça.", "いつか会いたいと思っていた人が実は自分でした、だなんて、笑えないよ...。"),
    (25994, 88, "É... Não acho ruim, no fim das contas.", "うん...まあ、悪いことではないとはCR思うけどね。"),
    (26007, 48, "N-não posso fazer isso!", "そ、そんなの出来ないよ。"),
    (26017, 96, "Lyner... Por que me faz usar Cerimônia?", "ねえ、ライナー...ライナーってあの、CRどうしてあたしにセレモニー着させるの?"),
    (26033, 104, "Então nunca usou uniforme na vida.", "そうか。じゃあ、学校の制服なんてCR本当に着たこと無かったんだな。"),
    (26035, 80, "Até treinei a fala de colegial!", "だから、勉強以外にも喋り方とかもいっぱい勉強したんだ。"),
    (26037, 104, "Tipo assim~?CRProfessor mó chato! Supernojento!", "っていうか~?CRあの先公マジ死ねって感じぃ?CRチョーキモッ!!みたいな?"),
    (26040, 144, "Falei que tava \"mó bafo\" na Igreja e levei bronca.", "うん。前に一度だけ、教会でチョベリバ~、って言ってみたら、同じように怒られたよ。"),
    (26041, 184, "A Igreja é careta! Se fossem descolados, o povo se sentiria mais próximo...", "教会ってちょっと頭固すぎるよ。CR少しくらい弾けていた方がCRみんなも親しみやすいと思うのに...。"),
    (26045, 112, "Vai ter que se responsabilizar depois!", "まあ、あとでライナーには色々と責任をCR取ってもらうからよろしくね。"),
    (26046, 32, "R-responsável!?", "せ、責任!?"),
    (26052, 40, "...Falou sério?", "...それ、本気で言ってるのかな~?"),
    (26071, 64, "Pois é... A culpa foi do Bourd.", "アレなんだけど...実はその原因がね、CRボルドにあったんだよ。"),
    (26084, 32, "Hum... acho que sim.", "ん...そう、かな?"),
    (26086, 56, "Invejo tanto a Misha...", "あたし、ミシャちゃんが凄く羨ましいんだ。"),
    (26089, 64, "Sempre me chamaram de fracasso.", "あたしなんか、昔からずっと落ちこぼれって言われ続けてきたんだもん。")
]

all_ok = True
for tid, maxb, cand, jp in tests:
    sz = encoded_size(cand)
    ok = (sz <= maxb)
    if not ok:
        all_ok = False
        print(f"FALHA: ID {tid} [{sz}B > {maxb}B] -> {cand}")
    else:
        print(f"OK: ID {tid} [{sz}B <= {maxb}B] -> {cand}")

print(f"\nResultado geral: {'TODOS OK!' if all_ok else 'HÁ FALHAS!'}")

import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

variants = [
    # 25269: lim 112
    # JP: これからもガンガン謳うからね!CRバンバン溜めさせてよね!
    (25269, 112, "Vou cantar com tudo!CRMe ajuda a carregar bem!"),
    (25269, 112, "Vou cantar com tudo!CREntão carrega bastante!"),
    (25269, 112, "Vou cantar demais!CREntão carrega bastante!"),
    # 25275: lim 56
    # JP: 少しは頼りなよ。CRそれに私も、もっとライナーを助けてCRあげたいしさ...
    # EN: You should trust me more.
    (25275, 56, "Confia em mim..."),
    (25275, 56, "Pode confiar em mim!"),
    (25275, 56, "Conta comigo, viu?"),
    (25275, 56, "Quero te ajudar mais!"),
    # 25277: lim 56
    # JP: 任せなさいって!うんと大きいの溜めて、CRビックリさせちゃうんだからね!
    # EN: You can always count on me!
    (25277, 56, "Deixa comigo!"),
    (25277, 56, "Pode contar comigo!"),
    (25277, 56, "Vou te surpreender!"),
    # 25283: lim 72
    # JP: ...ま、勝てたから良いんだけどね。
    # EN: ...Oh well, at least we won.
    (25283, 72, "...Mas o importante é vencer."),
    (25283, 72, "...Bem, pelo menos vencemos."),
    (25283, 72, "...Bom, pelo menos vencemos."),
    # 25285: lim 56
    # JP: うん、約束だよ。次こそはドカーンとCR一発、お見舞いしてあげるんだから! / えへへ、約束だよ。次こそはドカーンとCR一発、お見舞いしてあげるんだから!
    # EN: Promise? Next time, I’m going to sing a big one!
    (25285, 56, "Promete? Vou mandar ver!"),
    (25285, 56, "Combinado! Vou mandar ver!"),
    (25285, 56, "Promete? Vou arrasar!"),
    # 25296: lim 104
    # JP: えへへ、ほんと?CRありがと!CRそれじゃ、もっと頑張っちゃおうかな。
    (25296, 104, "Hehe, é? Obrigada!CRVou me esforçar ainda mais!"),
    (25296, 104, "Hehe, sério? Valeu!CRVou me esforçar ainda mais!"),
    (25296, 104, "Hehe, sério? Obrigada!CRVou dar ainda mais de mim!"),
    # 25301: lim 80
    # JP: あのくらいでよければ、また作ってあげるから期待してなさいって。
    (25301, 80, "Se gostou, posso fazer mais depois!"),
    (25301, 80, "Se gostou tanto, faço mais depois!"),
    (25301, 80, "Se gostou, preparo mais pra você!"),
    # 25302: lim 88
    # JP: カプリソーダ、美味しかったでしょ?CR結構自信作なんだよ、あれ。
    # EN: How was the Capri Soda? Did you like it?
    (25302, 88, "A Soda Capri tava boa? É meu xodó!"),
    (25302, 88, "Gostou da Soda Capri? É meu xodó!"),
    (25302, 88, "A Soda Capri tava boa? Fiz com carinho!"),
]

for did, lim, text in variants:
    enc = encoded_size(text)
    diff = enc - lim
    status = "OK" if enc <= lim else f"OVERFLOW +{diff}"
    print(f"ID {did} (lim {lim}): enc={enc} [{status}] -> '{text}'")

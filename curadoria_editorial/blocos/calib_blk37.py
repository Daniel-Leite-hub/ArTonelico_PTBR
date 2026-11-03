import sys
sys.path.insert(0, 'Ferramentas_Traducao')
sys.path.insert(0, 'Ferramentas_Traducao/curadoria_editorial/blocos')
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

# Dictionary of refined phrasings to replace in CURATION_DATA
CALIBRATED_FIXES = {
    # 30717 (max 152B): JP: でも中身は単なる「くすり」なんだよね。CR普通に「くすり」でいいんじゃないかな...。
    30717: (
        "Por dentro é só remédio comum, né?CRPodíamos chamar só de \"Remédio\"...",
        "Aurica sugerindo de forma simples e direta chamar o item apenas de 'Remédio' (148B/152B)."
    ),
    # 30725 (max 136B): JP: ...あの材料からどうやってこれがCR出来たのかが謎だよね?
    30725: (
        "...Como os ingredientes viraramCRessa coisa é um mistério, né?",
        "Aurica perplexa com a transmutação inusitada dos componentes originais (128B/136B)."
    ),
    # 30727 (max 136B): JP: まあな。パーティーでもするのかとCR間違われるかもな。
    30727: (
        "Pois é. Vão achar que a gente vaiCRfazer uma festa ou coisa assim.",
        "Lyner concordando que o artefato parece um adereço festivo (135B/136B)."
    ),
    # 30739 (max 144B): JP: なんてのは冗談で、実は苦いものが苦手なCR人のことも考えてにょ?ギモ味にしてある。
    30739: (
        "Brincadeira! Pensei em quem odeia amargoCRe fiz no sabor Miolo Nyo?.",
        "Lyner revelando o sabor especial para quem detesta o gosto amargo (137B/144B)."
    ),
    # 30744 (max 144B): JP: そうだね...。CR死んでも復活できるんでしょ...。CRそれなら「コンティニュー」だね。
    30744: (
        "Verdade... Revive da morte, né?CREntão o nome é \"Continue\"!",
        "Aurica batizando o item de reviver com o termo clássico dos videogames (122B/144B)."
    ),
    # 30753 (max 64B): JP: うわぁ...なんだか、凄くゴツイ扇風機だね...。
    30753: (
        "Nossa... que ventilador bruto!",
        "Aurica admirando o porte rústico do cata-vento explosivo (61B/64B)."
    ),
    # 30761 (max 136B): JP: まあ、相当不注意な真似をしなければ、CRそんなことにはならないと思うけど。
    30761: (
        "Bem, a menos que seja muito descuidado,CRduvido que isso aconteça.",
        "Lyner ponderando que com prudência ninguém toma choque (134B/136B)."
    ),
    # 30765 (max 120B): JP: この中の水を?CRふ~ん...普通の水にしか見えないんだけど?
    30765: (
        "Essa água aí? Hum...CRSó parece água comum pra mim.",
        "Aurica estranhando o aspecto límpido do líquido inflamável (107B/120B)."
    ),
    # 30769 (max 56B): JP: でも、爆弾に変わりはないんだよね?
    30769: (
        "Mas ainda é uma bomba, né?",
        "Aurica questionando com objetividade a natureza do artefato (55B/56B)."
    ),
    # 30770 (max 56B): JP: そ、そりゃまあそうだけどさ...。
    30770: (
        "B-Bem, é verdade, mas...",
        "Lyner sem argumentos para rebater a lógica dela (50B/56B)."
    ),
    # 30772 (max 104B): JP: あ、蚊取り線香...。CRしかもブタさん。
    30772: (
        "Espiral de mosquito...CREm forma de porquinho!",
        "Aurica apontando o formato tradicional de porquinho fumegante (93B/104B)."
    ),
    # 30774 (max 80B): JP: あ、そうなんだ。CR敵除け線香なんだね?
    30774: (
        "Ah, entendi!CRIncenso contra monstros?",
        "Aurica deduzindo com clareza o propósito repelente do porquinho (77B/80B)."
    ),
    # 30775 (max 88B): JP: うっ...ま、間違ってないからCR何も言い返せない...。
    30775: (
        "Ai... Pior que não posso rebater...",
        "Lyner admitindo que não tem como rebater a lógica irrefutável de Aurica (72B/88B)."
    ),
    # 30780 (max 48B): JP: いや、まあ確かにそうなんだけどさ...。
    30780: (
        "É, pior que é isso...",
        "Lyner aceitando sem graça a analogia do tambor de chamar inimigos (45B/48B)."
    ),
    # 30782 (max 32B): JP: なんだ、知ってるのか?
    30782: (
        "Já conhece?",
        "Lyner surpreso com o conhecimento prévio de Aurica sobre o gancho (24B/32B)."
    ),
    # 30784 (max 88B): JP: レーヴァテイルの間では「舌切りフック」CRなんて名前で呼ばれてるよ。
    30784: (
        "Nós chamamos deCR\"Gancho Corta-Língua\".",
        "Aurica contando o apelido cruel do acessório entre as Reyvateils (81B/88B)."
    ),
    # 30790 (max 64B): JP: アタラズ?CRどんなお薬なの?
    30790: (
        "Hitlezz? Que remédio é?",
        "Aurica perguntando sobre o efeito do frasco desacelerador (49B/64B)."
    ),
    # 30791 (max 96B): JP: 相手にかけて使う技なんだ。CR命中率が下がって、相手の攻撃がCR当たり辛くなるんだよ。
    30791: (
        "Lança no alvo: a mira caiCRe os golpes erram!",
        "Lyner resumindo a mecânica de evasão garantida contra ataques rivais (92B/96B)."
    ),
    # 30814 (max 64B): JP: じゃあ、名前は「ル・マモレーニョ」で決定だね!
    30814: (
        "Então é \"Le Guardelinho\"!",
        "Aurica formalizando o batismo sofisticado com prefixo francês (53B/64B)."
    ),
    # 30822 (max 144B): JP: ...それは中身のことじゃなくて、CR外側の瓶のことを褒めてるんだよな?
    30822: (
        "...Você tá elogiando o frasco,CRe não o remédio aí dentro, né?",
        "Lyner percebendo que ela gostou somente do recipiente de vidro (131B/144B)."
    ),
    # 30824 (max 112B): JP: でもな、中身だって結構苦労したんだぞ?
    30824: (
        "Mas olha, fazer o líquidoCRdeu muito trabalho também!",
        "Lyner defendendo o suor derramado no preparo do líquido da poção (109B/112B)."
    ),
    # 30828 (max 128B): JP: このパワーソーサーって、パッと見よくCRわからないよね?
    30828: (
        "Olhando assim, não dá pra saberCRo que é o Power Sourcer, né?",
        "Aurica achando a aparência do Power Sourcer pouco evidente (127B/128B)."
    ),
    # 30834 (max 40B): JP: だ、だから、俺に聞くなって!CR知るかよ!そんなこと!大体お前...
    30834: (
        "Não sei, ué!",
        "Lyner dando um basta impaciente nas indagações de Aurica (27B/40B)."
    ),
    # 30837 (max 104B): JP: や、やだ、近づけないで!CRその「悪魔の缶詰」!!
    30837: (
        "Afasta isso de mim!CREssa \"Lata Diabólica\"!!",
        "Aurica em choque exigindo distância da Lata de Canto de Sereia (90B/104B)."
    ),
    # 30838 (max 104B): JP: あ、悪魔って...別にとって食うわけじゃないだろ?
    30838: (
        "Diabólica?...CREla não vai te comer!",
        "Lyner tentando acalmar o pavor desproporcional de Aurica (75B/104B)."
    ),
    # 30842 (max 72B): JP: 私の近くでは絶対に使わないでよね。
    30842: (
        "Nunca use isso perto de mim!",
        "Aurica proibindo terminantemente o uso da lata em seu raio de visão (57B/72B)."
    ),
    # 30860 (max 120B): JP: だって、零音なんたらじゃ言いにくいし、CR難しいだろ?
    30860: (
        "Falar \"Zero Som sei-lá-o-quê\"CRé difícil e enrolado, né?",
        "Lyner descartando o nome técnico enrolado do amplificador (118B/120B)."
    ),
    # 30862 (max 88B): JP: ていうか、なんだかこれ、よくわからないCRよね?
    30862: (
        "Mas isso é meio esquisito, né?",
        "Aurica encarando com estranheza a silhueta retorcida da engenhoca (63B/88B)."
    ),
    # 30865 (max 72B): JP: でもさ、まさかガラクタなんて名前じゃCRマズイだろ?
    30865: (
        "Mas chamar de sucata não dá, né?",
        "Lyner ponderando que nenhum cliente compraria um item chamado sucata (68B/72B)."
    ),
    # 30867 (max 64B): JP: (...聞く相手を間違えたな)
    30867: (
        "(...Escolhi a pessoa errada.)",
        "Lyner se arrependendo amargamente de ter consultado Aurica (59B/64B)."
    ),
    # 30870 (max 104B): JP: 正直、そこまでサラリと言われるとはCR思ってなかったよ...。
    30870: (
        "Não achei que ia falarCRna lata desse jeito...",
        "Lyner desconcertado com a franqueza desinibida da Reyvateil (94B/104B)."
    ),
    # 30871 (max 112B): JP: 名前もわけわからないけど、別に棺じゃないし、これ...
    30871: (
        "Nome sem sentido,CRe isso nem é um caixão...",
        "Aurica apontando a total inadequação funerária do objeto (91B/112B)."
    ),
    # 30872 (max 112B): JP: 棺の形してるだけで、実際には入れないしね。
    30872: (
        "Tem forma de caixão,CRmas ninguém cabe nele.",
        "Aurica frisando que as dimensões do baú não comportam uma pessoa (91B/112B)."
    ),
    # 30878 (max 240B): JP: な、なんだよ健康マニアって。CRこれは特殊な回復剤なんだよ。一晩寝ればCR全員HPも詩魔法も全快なんだぜ?
    30878: (
        "Que mania de saúde o quê!CRÉ um remédio especial: se dormir,CRo HP e a Magia Canção de todos se curam!",
        "Lyner esclarecendo o poder de cura integral proporcionado pelo repouso noturno (209B/240B)."
    ),
    # 30881 (max 48B): JP: 一匹残らずイチコロ!
    30881: (
        "Morte instantânea!",
        "Aurica comparando a fumaça de cura ao efeito fulminante de veneno (38B/48B)."
    ),
    # 30891 (max 144B): JP: もう負けそうになった時とか、一か八かこれを持って敵にアタックさ!
    30891: (
        "Se for perder, arrisque tudoCRe corra pra cima com ela!",
        "Lyner instigando a jogada de desespero final em situações críticas (111B/144B)."
    ),
    # 30895 (max 112B): JP: あのな...まあ、確かに威力的には微妙なCR感じだけどな。
    30895: (
        "Bem... O ataque delaCRrealmente é meio fraco, mas...",
        "Lyner assumindo o baixo desempenho combativo da lâmina básica (106B/112B)."
    ),
    # 30897 (max 112B): JP: ...それって、剣としての価値ないんじゃないかな?
    30897: (
        "...Então não tem valorCRcomo espada, né?",
        "Aurica sintetizando que o artefato é inútil para o combate direto (84B/112B)."
    ),
    # 30902 (max 120B): JP: ああ。そんなアイテムを混ぜた覚えはCR無いんだけどな...。
    30902: (
        "Sim. Pior que nem lembroCRde misturar nada disso nela...",
        "Lyner sem entender como os bônus de vida se manifestaram na receita (113B/120B)."
    ),
    # 30904 (max 112B): JP: それでラードルフの喜びが半減しなければCRいいんだけどな...。
    30904: (
        "Só espero que não estragueCRa alegria do Radolf...",
        "Lyner torcendo para que a reverência do cardeal permaneça intacta (103B/112B)."
    ),
    # 30909 (max 96B): JP: でも、ジャックさんも緑だからCRちょうどいいかも。
    30909: (
        "O Jack veste verde,CRentão combina bem!",
        "Aurica encontrando harmonia entre a cor da arma e o visual de Jack (80B/96B)."
    ),
    # 30910 (max 72B): JP: 妙なところに落ち着いたな...。
    30910: (
        "Conclusão bem estranha...",
        "Lyner surpreso com o rumo peculiar do raciocínio de Aurica (52B/72B)."
    ),
    # 30911 (max 104B): JP: 自分で作っておいてなんだけど、CR凄い凶悪だよな、これ?
    30911: (
        "Fui eu quem fiz, mas issoCRé brutal demais, né?",
        "Lyner impressionado com a letalidade visceral do mecanismo dentado (97B/104B)."
    ),
    # 30915 (max 176B): JP: でもまあ、確かに凶悪だよな。CR少し柔らかい感じにしたほうがいいかな?
    30915: (
        "Mas é brutal mesmo. Será que deviaCRdeixar com uma cara mais suave?",
        "Lyner cogitando amenizar a agressividade visual da arma forjada (137B/176B)."
    ),
    # 30916 (max 56B): JP: 「クルクルズバズバ」ってのはどうかな?
    30916: (
        "Que tal \"Gira-Corta\"?",
        "Aurica sugerindo um apelido sonoro e infantil para a motosserra (43B/56B)."
    ),
    # 30917 (max 152B): JP: 可愛らしい名前だけど、実際に使った時のCRギャップが天と地ほどあるよな...。
    30917: (
        "Nome fofo, mas o contrasteCRna hora de usar é do céu ao inferno...",
        "Lyner notando o abismo entre o nome meigo e o banho de sangue em batalha (135B/152B)."
    ),
    # 30918 (max 144B): JP: 朱雀&青龍。二刀で一つだから時間掛かるよ、まったく...。
    30918: (
        "Suzaku & Seiryuu. Duas lâminas em uma,CRdeu um trabalhão danado...",
        "Lyner relatando o esforço hercúleo para forjar o par de katanas gêmeas (135B/144B)."
    ),
    # 30919 (max 144B): JP: ていうか、これ、本当に刀?CRなんだか凄く凶悪なデザインしてるんだけど。
    30919: (
        "Mas isso é katana mesmo?CRO visual parece tão vilanesco...",
        "Aurica desconfiando que o formato sombrio pertence a um grande vilão (119B/144B)."
    ),
    # 30920 (max 104B): JP: ま、まあ、そういうレシピだったんだからCRしょうがないだろ。
    30920: (
        "B-Bem, a receita era assim,CRfazer o quê...",
        "Lyner justificando que apenas seguiu o diagrama clássico dos pergaminhos (88B/104B)."
    ),
    # 30921 (max 88B): JP: でもさ、これ、どう見ても悪役の刀だよね?
    30921: (
        "Mas parece a lâmina de um vilão!",
        "Aurica enfatizando que o fio de corte tem traços puramente malignos (67B/88B)."
    ),
    # 30922 (max 80B): JP: いや、デザインで判断すればそうだけどさ...。
    30922: (
        "Pelo visual até parece, mas...",
        "Lyner concordando relutante que o aspecto estético intimida (62B/80B)."
    ),
    # 30923 (max 120B): JP: 作ってる時にどうにかすればよかったのに...。
    30923: (
        "Podia ter mudado issoCRenquanto forjava...",
        "Aurica repreendendo Lyner por não ter suavizado a linha da espada (85B/120B)."
    ),
    # 30924 (max 144B): JP: シエロセラミクスをイオン板とCRパワードビスで補強してみたんだ。
    30924: (
        "Reforcei a Cierocerâmica com placa de íonsCRe parafuso energizado.",
        "Lyner detalhando o processo metalúrgico de fortalecimento da liga (135B/144B)."
    ),
    # 30925 (max 104B): JP: 見た目はあんまり変わってないけど、CRどこか変わったところあるの?
    30925: (
        "O visual mal mudou,CRmas tem algo diferente?",
        "Aurica analisando minuciosamente a peça sem enxergar mudanças óbvias (89B/104B)."
    ),
    # 30926 (max 184B): JP: まあ、少し効果が強くなっただけだよ。CR正直、それ以外の特殊な効果はないしな。
    30926: (
        "Só aumentou um pouco a força.CRNão tem outros efeitos especiais.",
        "Lyner explicando que o upgrade foi puramente numérico e funcional (132B/184B)."
    ),
    # 30927 (max 120B): JP: じゃあてんこ盛りに更に足したんだから、CR「特盛りソード」で決定だね!
    30927: (
        "Já que reforçou mais, tá decidido:CR\"Espada Super Combo\"!",
        "Aurica batizando a lâmina com o clássico termo culinário de porção farta (118B/120B)."
    ),
    # 30928 (max 104B): JP: ...それ、頼むから人前でだけは言わないでCRくれよ?
    30928: (
        "...Só não fala esse nomeCRna frente dos outros!",
        "Lyner implorando para que ela guarde segredo sobre a alcunha vergonhosa (97B/104B)."
    ),
    # 30929 (max 160B): JP: 作っておいてなんだけど、これ、どうしてCR炎の追加ダメージがあるんだろうな?
    30929: (
        "Eu que fiz, mas por que issoCRtem dano adicional de fogo?",
        "Lyner perplexo com o surgimento espontâneo de labaredas na lâmina (115B/160B)."
    ),
    # 30932 (max 120B): JP: 作った本人がそんなこと言っちゃCRダメだと思うけど?
    30932: (
        "Quem forjou não devia ficarCRcom essa cara de dúvida, viu?",
        "Aurica cobrando firmeza profissional de quem assina a fabricação da arma (119B/120B)."
    ),
    # 30940 (max 112B): JP: いつの間にか銃も当たり前のようにCR作れるようになってきてるな、俺。
    30940: (
        "Sem notar, já forjo pistolasCRcom a maior calma.",
        "Lyner surpreso com sua proficiência mecânica na manufatura bélica (98B/112B)."
    ),
    # 30941 (max 64B): JP: そうだね。CRでもライナーって銃は使わないもんね?
    30941: (
        "É, mas você não usa arma, né?",
        "Aurica pontuando a predileção exclusiva de Lyner por armas brancas (63B/64B)."
    ),
    # 30943 (max 128B): JP: そうだったんだ...。CRでも、そのわりにこんな強そうな拳銃CR作れるよね?
    30943: (
        "Entendi... Mas mesmo assim,CRvocê forja uma pistola tão boa!",
        "Aurica admirada com a excelência do revólver de alta potência gerado (123B/128B)."
    ),
    # 30945 (max 176B): JP: 実はこれ、素人にはとても使えないくらいCR強くてさ、試し撃ちしてないんだよ。
    30945: (
        "O coice é forte demais pra amadores,CRentão nem fiz tiro de teste ainda.",
        "Lyner revelando o recuo colossal que o impediu de disparar munição real (147B/176B)."
    ),
    # 30948 (max 192B): JP: ...ジャックさん...ぶっつけ本番で使うんだね。後ろで謳いながら祈ってるよ。
    30948: (
        "...O sr. Jack vai ter que usar direto na hora H.CRVou rezar por ele cantando lá atrás.",
        "Aurica dedicando hinos e preces para a segurança do atirador Jack em combate (175B/192B)."
    ),
    # 30950 (max 112B): JP: た、試さなくていいってば!CRそんなうるさそうな物。
    30950: (
        "N-Não precisa ligar isso!CRParece barulhento demais!",
        "Aurica implorando desesperada para Lyner não dar partida no motor (106B/112B)."
    ),
    # 30958 (max 264B): JP: 作ってる最中に何度か指を切りそうになって慌てたよ。しかし、何でそんなに指を切りそうになったんだろう...。
    30958: (
        "Quase cortei os dedos várias vezesCRenquanto forjava, que susto! Mas por queCRserá que quase cortei os dedos tantas vezes?...",
        "Lyner recapitulando os incidentes quase fatais durante o forjamento da katana amaldiçoada (253B/264B)."
    ),
    # 30964 (max 96B): JP: そうか。じゃあ、オリカに名前を決めてCRもらおうかな?
    30964: (
        "É? Então que tal vocêCRdar um nome, Aurica?",
        "Lyner transferindo com carinho a decisão batismal para Aurica (90B/96B)."
    ),
    # 30967 (max 40B): JP: うん...えっと、それじゃあね...。
    30967: (
        "Vejamos...",
        "Aurica pensando concentrada com todo o afeto infantil (21B/40B)."
    ),
    # 30971 (max 72B): JP: ...つ、作るの、メチャクチャ苦労したのに...。
    30971: (
        "...D-Deu tanto trabalho...",
        "Lyner desabafando desolado com o desfecho cômico da Cantora Prateada (53B/72B)."
    ),
    # 30974 (max 112B): JP: 全部付いてるの!?CR武器なのに防御まで!?
    30974: (
        "Resiste a tudo!? Uma armaCRque defende desse jeito!?",
        "Aurica maravilhada com o escudo elemental impenetrável da lança (105B/112B)."
    ),
    # 30978 (max 136B): JP: そうじゃないけどさ、せっかくなんだからCRもっとかっこいい名前の方がいいよ。
    30978: (
        "Não é isso, mas sendo tão boa,CRmerecia um nome bem imponente!",
        "Aurica argumentando que a excelência da lança exige uma alcunha grandiosa (128B/136B)."
    )
}

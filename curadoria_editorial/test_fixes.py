# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

cases = [
    (
        "私たちのような『想い』の生命体は、CRこの塔の中に入れるのよ。CRでも、ライナーはダメなのよ。",
        "Entidades nascidas dos sentimentos, como nós,\npodem entrar nessa torre.\nMas você não pode de jeito nenhum, Lyner."
    ),
    (
        "塔の中にいるウイルスは、私たちのようなCR『想い』の生命体を、自由にねつ造することができるのよ。",
        "Os vírus que infectam a Torre conseguem fabricar livremente\nentidades nascidas dos sentimentos, como nós!"
    ),
    (
        "『ミシャの分離試験によるCR 影響と変化の報告...』",
        '"Relatório sobre os Efeitos e Alterações\ndo Experimento de Separação de Misha..."'
    ),
    (
        "『容態は良好...しかし、CR 想定された思考の変化はCR 見られない...』",
        '"Quadro clínico estável... No entanto,\nnão foram observadas as alterações cognitivas esperadas..."'
    ),
    (
        "『MULEプロジェクトでCR 言う「ケーシー野」までの 分離は困難...』",
        '"A separação até o \'Campo KC\',\nconforme previsto no Projeto MULE, mostrou-se inviável..."'
    ),
    (
        "オリカさんのヒュムネコードはCR「#1MULE_TEIWAZ_ARTONELICO」だ。",
        'O Código Hymmnos da senhorita Aurica é:\n"#1MULE_TEIWAZ_ARTONELICO".'
    ),
    (
        "「新・カイエル自伝5巻」。ファルス司祭の日記か...。",
        '"Nova Autobiografia de Kyle, Volume 5"...\nÉ o diário pessoal do Bispo Falss...'
    ),
    (
        "勝てるか否かは『エレミアの使徒』である証、『ハーモニクス』にかかっている。",
        "A sua vitória dependerá do Harmonics,\na prova viva de quem porta o título de Cavaleiro de Elemia."
    ),
    (
        "『ラードルフ』がCR仲間になった。",
        "Radolf entrou para o grupo!"
    ),
    (
        "『クルシェ』がCR仲間になった。",
        "Krusche entrou para o grupo!"
    ),
    (
        "『ジャック』がCR仲間になった。",
        "Jack entrou para o grupo!"
    ),
    (
        "『ヒュムネクリスタル・クロ ニクルキー調査の結果...』",
        '"Resultados da investigação sobre\no Cristal Hymmnos Chronicle Key..."'
    ),
    (
        "『呪文列の取り出しは成功、 しかしその書込にはまだCR 難アリ...』",
        '"A extração da sequência do feitiço foi bem-sucedida,\nporém a sua gravação ainda apresenta falhas críticas..."'
    ),
    (
        "「どんすけ」ってヤツで、CRオリカにとってかなり大切な存在になってます。",
        'O nome dele é "Don Leon", e ele se tornou\numa presença imensamente preciosa para ela.'
    ),
    (
        "ありがと。CRそのアイテムはCR「ボルタポルタ」よ。",
        'Muito obrigada!\nO artefato que você procura é o "Boltapolta".'
    ),
    (
        "アイテム「ボルタポルタ」を手に入れた!",
        'Você obteve o item "Boltapolta"!'
    )
]

all_passed = True
for orig, trad in cases:
    valido, erros = validador_editorial.validar_hard_gate(
        orig, trad, ignorar_quebras=True, permitir_colisao_variavel=True
    )
    avisos = validador_editorial.auditar_estilo_editorial(trad)
    if not valido or avisos:
        all_passed = False
        print("FAIL:")
        print("  Orig:", orig)
        print("  Trad:", trad)
        print("  Erros:", erros)
        print("  Avisos:", avisos)

if all_passed:
    print("ALL TEST CASES PASSED WITH 0 HARD GATE ERRORS AND 0 LINT WARNINGS!")

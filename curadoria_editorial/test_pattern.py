# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

for test in [
    'Misha teceu a Magia Vermelha [Trovoada]!',
    'Misha teceu a Magia Vermelha [ Trovoada ]!',
    'Misha teceu a Magia Vermelha [Canção Trovoada]!',
    'Misha teceu a Magia Vermelha «Trovoada»!',
    'Misha teceu a Magia Vermelha [Trovoada ]!',
    'Misha teceu a Magia Vermelha [Relâmpago Trovoada]!',
    'Você obteve a [Espada Yuteroid]!',
    'Você obteve a espada [Yuteroid]!',
    'Você obteve a [espada Yuteroid]!'
]:
    ok, err = validador_editorial.validar_hard_gate('赤魔法【疾風迅雷】を紡ぎ出した!', test, ignorar_quebras=True, permitir_colisao_variavel=True)
    print(f"{test!r:45} -> ok={ok}, err={err}")

# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

jp = "青魔法【クリニクル】を紡ぎ出した!"

candidates = [
    'Você teceu a Magia Azul "Chronicle"!',
    'Você teceu a Magia Azul 【Chronicle】!',
    'Você teceu a Magia Azul [Crônica]!',
    'Você teceu a Magia Azul: Chronicle!',
    'Magia Azul [Chronicle] tecida!',
]

for c in candidates:
    val, err = validador_editorial.validar_hard_gate(jp, c, ignorar_quebras=True, permitir_colisao_variavel=True)
    lint = validador_editorial.auditar_estilo_editorial(c)
    print(f"{c:42} -> Valid: {val:5} | Errors: {err} | Lint: {lint}")

# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

test = "Você ainda tem o seu dever no Esquadrão de Busca, não é?\nVá em frente... e boa sorte na sua missão."
ok, err = validador_editorial.validar_hard_gate("ライナーは捜索隊のお仕事があるんだよね。CR...行ってらっしゃい。", test, ignorar_quebras=True, permitir_colisao_variavel=True)
avisos = validador_editorial.auditar_estilo_editorial(test)
print(f"ok={ok}, err={err}, avisos={avisos}")

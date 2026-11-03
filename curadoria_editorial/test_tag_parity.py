import sys
sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

# Test line 19807
jp = "赤魔法【ELMA-DS】を紡ぎ出した!"
pt1 = "Você teceu a Magia Vermelha [ELMA-DS]!"
pt2 = "Você teceu a Magia Vermelha 【ELMA-DS】!"
pt3 = "Você teceu a Magia Vermelha «ELMA-DS»!"

for pt in [pt1, pt2, pt3]:
    v, err = validador_editorial.validar_hard_gate(jp, pt, ignorar_quebras=True, permitir_colisao_variavel=True)
    print(f"PT: {pt!r} -> Valid: {v}, Errors: {err}")

# Test line 19584
jp = "お店、「UNI-Q」でいいわよね。安いし、すぐそこだから。"
pt1 = "A loja... pode ser a [UNI-Q], né? É barata e fica logo ali."
pt2 = "A loja... pode ser a «UNI-Q», né? É barata e fica logo ali."
for pt in [pt1, pt2]:
    v, err = validador_editorial.validar_hard_gate(jp, pt, ignorar_quebras=True, permitir_colisao_variavel=True)
    print(f"PT: {pt!r} -> Valid: {v}, Errors: {err}")

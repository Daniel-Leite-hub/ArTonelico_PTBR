# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

print('Linker with «»:', validador_editorial.validar_hard_gate('ヒュムネクリスタル「リンカ」', 'Cristal Hymmnos «Linker»'))
print('Linker with “”: ', validador_editorial.validar_hard_gate('ヒュムネクリスタル「リンカ」', 'Cristal Hymmnos “Linker”'))
print('Booster with «»:', validador_editorial.validar_hard_gate('青魔法【ブースター】を紡ぎ出した!', 'Você teceu a Magia Azul «Booster»!'))
print('Booster with “”: ', validador_editorial.validar_hard_gate('青魔法【ブースター】を紡ぎ出した!', 'Você teceu a Magia Azul “Booster”!'))
print('Templo without []:', validador_editorial.validar_hard_gate('『寺院』に行けるようになった!', 'O acesso ao Templo foi liberado!'))

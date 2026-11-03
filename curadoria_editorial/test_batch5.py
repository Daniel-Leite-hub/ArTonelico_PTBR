# -*- coding: utf-8 -*-
import sys
import json
import os

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
sys.path.insert(0, r"Ferramentas_Traducao\tools")
sys.path.insert(0, r"Ferramentas_Traducao\curadoria_editorial")
import validador_editorial
from curadoria_validate import validate_line
from batch5_044 import dialogues

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_044_input.json', 'r', encoding='utf-8') as f:
    inp_data = json.load(f)

inp_map = {d['id']: d for d in inp_data['dialogues']}

all_ok = True
for d in dialogues:
    lid = d['id']
    pt = d['pt_curated']
    inp = inp_map[lid]
    jp = inp['original_jp']
    en = inp['original_en']

    errs = validate_line(lid, en, pt)
    if errs:
        print(f"[curadoria_validate ERROR] ID {lid}: {errs}")
        all_ok = False

    valido, erros_hg = validador_editorial.validar_hard_gate(
        original=jp,
        traduzido=pt,
        ignorar_quebras=True,
        permitir_colisao_variavel=True
    )
    if not valido:
        print(f"[validador_editorial HG ERROR] ID {lid}: {erros_hg}")
        all_ok = False

    avisos = validador_editorial.auditar_estilo_editorial(pt)
    if avisos:
        print(f"[validador_editorial LINT WARN] ID {lid}: {avisos}")

if all_ok:
    print(f"Batch 5: All {len(dialogues)} dialogues passed perfectly!")
else:
    print("Batch 5 had errors!")

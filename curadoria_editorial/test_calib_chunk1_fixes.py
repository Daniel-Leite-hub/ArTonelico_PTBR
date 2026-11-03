# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

tests = {
    31290: [
        'Foi bem difícil fazer isso...',
        'Fazer isso foi tão difícil...',
        'Isso foi bem difícil...',
        'Até que foi bem difícil...',
        'Nossa, como é difícil...'
    ],
    31292: [
        'Esses remendos deram um trabalhão!CRMas usei bastante coisa aí.',
        'Esses remendos deram um trabalhão!CRMas olha quanta coisa usei.'
    ],
    31295: [
        'Os materiais são ótimos,CRmas parece tão pobrezinho...CR“Pano Esfarrapado”...',
        'O material é ótimo,CRmas parece tão pobrezinho...CR“Pano Esfarrapado”...',
        'Materiais ótimos,CRmas que visual pobrezinho...CR“Pano Esfarrapado”...'
    ],
    31302: [
        'Já sei! O nome deleCRvai ser “Don Leon Lyner”!',
        'Já sei! Vamos chamarCRde “Don Leon Lyner”!',
        'Já sei! Esse vai ser oCR“Don Leon Lyner”!'
    ],
    31315: [
        'Até dá, mas só se controlaCRcom a Bússola de Gravard...',
        'Dá pra usar, mas só se controlaCRcom a Bússola de Gravard...'
    ],
    31316: [
        'Mas este já tem a BússolaCRde Gravard, então tá seguro.',
        'Mas este já tem a BússolaCRde Gravard, então tá tudo bem.'
    ]
}

caps = {31290: 48, 31292: 152, 31295: 152, 31302: 104, 31315: 128, 31316: 112}

for d_id, variants in tests.items():
    print(f"=== ID {d_id} (Cap: {caps[d_id]}B) ===")
    for v in variants:
        sz = encoded_size(v)
        diff = sz - caps[d_id]
        print(f"  {sz}B ({diff:+3d}B) | {v}")

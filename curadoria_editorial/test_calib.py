import sys
import sqlite3

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

tests = {
    31845: [
        "Pelo tamanho, acho que dáCRum bom colar, né?",
        "Pelo tamanho, daria um bomCRcolar, não acha?",
        "Pelo tamanho, fica ótimoCRpara um colar, né?",
        "Pelo tamanho, daria certoCRpara um colar, né?"
    ],
    31846: [
        "Viu?CREntão capricha aí!",
        "Viu só?CREntão boa sorte!",
        "Viu só?CRMãos à obra!"
    ],
    31848: [
        "Quando tiver tempo.CRAssim ela não passa de umaCRpedrinha qualquer.",
        "Quando tiver tempo.CRDo jeito que tá, não passaCRde uma joia comum.",
        "Quando tiver tempo.CRAssim ela não passa de umaCRpedra qualquer."
    ],
    31850: [
        'E daí? E nada de termos friosCRcomo "Cristal". Vamos pôr um nomeCRde joia, tipo "Joias Ardel"!',
        'E daí? Sem termos técnicos comoCR"Cristal". Vamos botar um nomeCRde joia, tipo "Joias Ardel"!'
    ],
    31864: [
        "...Esse anel tá com uma caraCRsupervenenosa, sabia?",
        "...O visual desse anel tá bemCRvenenoso, não acha?"
    ],
    31865: [
        "O design todo parece deCRum anel de veneno puro!",
        "O design parece até de umCRanel de veneno mortal!"
    ]
}

limits = {31845: 96, 31846: 56, 31848: 120, 31850: 200, 31864: 104, 31865: 104}

for did, opts in tests.items():
    print(f"=== ID {did} (Limit {limits[did]}) ===")
    for opt in opts:
        sz = encoded_size(opt)
        print(f"  [{sz}b] {opt} -> {'OK' if sz <= limits[did] else 'FAIL'}")

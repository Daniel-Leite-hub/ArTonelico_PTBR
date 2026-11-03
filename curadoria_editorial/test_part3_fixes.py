import sys
from pathlib import Path
BASE_DIR = Path("Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = [
    (32630, 152, [
        "Usou tanta coisa... Uma pilha de peçasCRque nem deveria caber aqui dentro.",
        "Usou tanto material... Jamais penseiCRque caberia numa ocarina tão pequena.",
        "Usou tanta coisa... Nem parece caberCRnuma peça tão pequena."
    ]),
    (32633, 80, [
        "Tripolar?! Lyner, por queCRfoi fazer logo isso?!",
        "Tripolar?! Por que vocêCRfez uma coisa dessas?!",
        "Tripolar?! Lyner, por queCRfez um desses?!",
        "Tripolar?! Por que foiCRfazer logo isso?!"
    ]),
    (32636, 64, [
        "D-Desculpe... É tão perigoso assim?",
        "Perdão... Mas é tão perigoso?",
        "D-Desculpe... É tão grave?",
        "Desculpe... Mas é tão perigoso?"
    ]),
    (32641, 120, [
        "Mas por que você reagiuCRcomo se fosse algo proibido...?",
        "Mas por que reagiu como seCReu tivesse feito algo proibido...?",
        "Mas por que você reagiuCRcomo se fosse algo terrível...?"
    ]),
    (32649, 128, [
        "Até me surpreende eu ter conseguidoCRcriar uma coisa dessas...",
        "Até eu me surpreendo por conseguirCRcriar uma coisa dessas...",
        "Até eu fico surpreso de conseguirCRcriar algo assim..."
    ]),
    (32664, 96, [
        "Céus... Você anda bem estranhoCRultimamente, Lyner...",
        "Nossa... Você anda muito estranhoCRultimamente...",
        "Nossa... Você anda bem estranhoCRultimamente, Lyner...",
        "Puxa... Você anda bem estranhoCRultimamente, Lyner..."
    ]),
    (32666, 88, [
        "Por que forjou partesCRdo meu próprio corpo?",
        "Por que está forjando partesCRdo meu próprio corpo?",
        "Por que recriou partesCRdo meu próprio corpo?"
    ]),
    (32676, 144, [
        'Chame de "Cuidado Extremo" para queCRtodos saibam que é perigoso.',
        'Chame de "Perigo Extremo" paraCRtodos saberem que é perigoso.',
        'Chame de "Perigo Extremo" para queCRtodos saibam que é perigoso.'
    ]),
    (32679, 152, [
        "Não entro nessa aposta! É óbvioCRque não sei o que é.",
        "Nem aposto nisso! É óbvio queCRnão faço ideia do que seja.",
        "Não entro nessa aposta! Nem imaginoCRo que isso seja."
    ]),
    (32706, 104, [
        'Pensando bem, "Inferior Petit"CRsoa bem mais fofo...',
        'Pensando bem, "Grathnode Petit"CRsoa mais bonitinho...',
        'Pensando bem, "Mini-Inferior"CRsoa mais bonitinho...'
    ])
]

for did, cap, cands in tests:
    print(f"=== ID {did} (CAP: {cap}B) ===")
    for c in cands:
        sz = encoded_size(c)
        diff = sz - cap
        status = "OK" if diff <= 0 else f"FAIL (+{diff})"
        print(f"  {sz}B/{cap}B [{status}] -> {c}")

import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

test_map = [
    # 29169 (Cap: 32)
    (29169, 32, ["Barca Krusche", "Bote da Krusche", "Nau da Krusche"]),
    # 29170 (Cap: 48)
    (29170, 48, ["Encosta do Cais", "Encosta do Cais Flutuante"]),
    # 29171 (Cap: 24)
    (29171, 24, ["Praça Karulu", "Parque Karulu", "Vila Karulu", "Karulu Park"]),
    # 29172 (Cap: 32)
    (29172, 32, ["Câmara de Elemia", "Sala de Elemia"]),
    # 29173 (Cap: 40)
    (29173, 40, ["Feira de Karulu", "Mercado de Karulu", "Feira Livre Karulu"]),
    # 29174 (Cap: 32)
    (29174, 32, ["Igreja Elemia", "Igreja de Elemia"]),
    # 29175 (Cap: 32)
    (29175, 32, ["Pq. Cantapedra", "Cantapedra", "Pq Cantapedra"]),
    # 29176 (Cap: 48)
    (29176, 48, ["Pq. Cantapedra: Noite", "Cantapedra: Noite"]),
    # 29177 (Cap: 32)
    (29177, 32, ["Av. Hoshinose", "Rua Hoshinose", "Via Hoshinose"]),
    # 29178 (Cap: 40)
    (29178, 40, ["[Lua Cantante]", "Pous. Lua Cantante", "Inn [Lua Cantante]"]),
    # 29179 (Cap: 24)
    (29179, 24, ["Ponte Alta", "Passarela", "Sky Bridge", "Ponte Aérea", "Ponte Céu"]),
    # 29180 (Cap: 24)
    (29180, 24, ["Pous. Torre", "[Tower Inn]", "Casa Torre", "Inn Torre"]),
    # 29181 (Cap: 32)
    (29181, 32, ["Casa da Aurica", "Casa de Aurica"]),
    # 29182 (Cap: 24)
    (29182, 24, ["Entrada"]),
    # 29183 (Cap: 40)
    (29183, 40, ["Sala da Presidente", "Sala da presidente"]),
    # 29184 (Cap: 40)
    (29184, 40, ["Oficina Reyvateil", "Ateliê Reyvateil"]),
    # 29185 (Cap: 40)
    (29185, 40, ["Casa de Garzburn", "Casa do Garzburn"]),
    # 29186 (Cap: 24)
    (29186, 24, ["P. Pheyna", "Pheyna Gate", "Portão Feena", "Portão Pheyna"]),
    # 29187 (Cap: 24)
    (29187, 24, ["Magecure"]),
    # 29188 (Cap: 32)
    (29188, 32, ["Pous. Restoire", "Inn [Restoire]", "[Restoire]"]),
    # 29189 (Cap: 32)
    (29189, 32, ["Grande Templo", "Templo Central", "Pátio do Templo"]),
    # 29190 (Cap: 32)
    (29190, 32, ["Ninho do Dragão", "Vila Dragão", "Vila D-Nest"]),
    # 29191 (Cap: 32)
    (29191, 32, ["Sala das Chaves", "Horn: Chaves", "Horn [Chaves]"]),
    # 29192 (Cap: 40)
    (29192, 40, ["Controle Climático", "Controles Climáticos", "Controle do Clima"]),
]

for did, cap, options in test_map:
    print(f"--- ID {did} (Cap {cap}B) ---")
    for opt in options:
        sz = encoded_size(opt)
        ok = sz <= cap if sz else False
        print(f"  {'[OK]' if ok else '[FAIL]'} {sz}B: {opt}")

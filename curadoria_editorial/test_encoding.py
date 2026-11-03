import sys
from pathlib import Path
BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

s = "Eu só... queria ver você. É só isso..."
print("len:", len(s), "encoded:", encoded_size(s))
s2 = "Obrigado."
print("len:", len(s2), "encoded:", encoded_size(s2))
s3 = "A"
print("len:", len(s3), "encoded:", encoded_size(s3))
for ch in "Aáàãâéêíóôõúüç":
    print(f"ch '{ch}': {encoded_size(ch)}")

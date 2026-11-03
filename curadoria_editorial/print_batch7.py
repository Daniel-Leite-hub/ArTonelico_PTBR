import sys
from pathlib import Path
BASE_DIR = Path("Ferramentas_Traducao")

with open(BASE_DIR / "curadoria_editorial/blk19_overview.txt", "r", encoding="utf-8") as f:
    text = f.read()

entries = text.split("=== ID ")
for e in entries:
    if not e.strip(): continue
    did = int(e.split(" ")[0])
    if 25741 <= did <= 25801:
        print("=== ID " + e.strip() + "\n")

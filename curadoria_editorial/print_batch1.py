import sys
from pathlib import Path
BASE_DIR = Path("Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

with open(BASE_DIR / "curadoria_editorial/blk19_overview.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's extract entries for 25514 to 25550
entries = text.split("=== ID ")
for e in entries:
    if not e.strip(): continue
    did = int(e.split(" ")[0])
    if 25514 <= did <= 25550:
        print("=== ID " + e.strip() + "\n")

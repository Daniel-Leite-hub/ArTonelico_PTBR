from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
lines = open(BASE_DIR / "curadoria_editorial" / "blk18_overview.txt", encoding="utf-8").read().split("\n")

current_id = None
for line in lines:
    if line.startswith("=== ID "):
        current_id = line
    elif line.startswith("JP: ") and any(marker in line for marker in ["オリカ", "ミシャ", "シュレリア", "マッサージ", "インストール", "第一紀", "大惨事", "アイス", "ソーダ"]):
        print(current_id)
        print(line[:100])

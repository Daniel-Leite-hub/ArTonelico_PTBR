# -*- coding: utf-8 -*-
import json

with open("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_054_input.json", "r", encoding="utf-8") as f:
    d = json.load(f)

lines = d["dialogues"]

def dump_range(s, e, out_name):
    subset = [l for l in lines if s <= l["id"] <= e]
    print(f"=== {out_name}: {len(subset)} lines ({s} to {e}) ===")
    for l in subset:
        spk = l.get("speaker")
        jp = l.get("original_jp", "")
        en = l.get("original_en", "")
        pt = l.get("current_ptbr", "")
        print(f"[{l['id']}] {spk}")
        print(f"  JP: {jp}")
        print(f"  EN: {en}")
        print(f"  PT: {pt}")
        print()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        dump_range(int(sys.argv[1]), int(sys.argv[2]), f"IDs {sys.argv[1]}-{sys.argv[2]}")
    else:
        print("Usage: python inspect_blk054.py start_id end_id")

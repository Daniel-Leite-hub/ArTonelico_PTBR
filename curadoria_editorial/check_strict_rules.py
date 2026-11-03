# -*- coding: utf-8 -*-
import sys
import re

from curated_lines_054_p1 import CURATED_LINES as P1
from curated_lines_054_p2 import CURATED_LINES as P2
from curated_lines_054_p3 import CURATED_LINES as P3

ALL_LINES = {}
ALL_LINES.update(P1)
ALL_LINES.update(P2)
ALL_LINES.update(P3)

print("Checking CR (\\r)...")
for item_id, data in ALL_LINES.items():
    text = data["ptbr"]
    if "\r" in text:
        print(f"ERROR: Line {item_id} contains \\r!")

print("Checking lines starting with punctuation after \\n...")
for item_id, data in ALL_LINES.items():
    text = data["ptbr"]
    for idx, line in enumerate(text.split("\n")):
        if idx > 0 and line and line[0] in ".,;:?!-–—…":
            print(f"WARNING: Line {item_id} subline {idx} starts with punctuation: {line[:10]}")

print("Checking stage directions (rubricas)...")
for item_id, data in ALL_LINES.items():
    text = data["ptbr"]
    if re.search(r"\*.*?\*", text) or re.search(r"\(.*?(?:suspiro|risos|tosse).*?\)", text, re.IGNORECASE):
        print(f"ERROR: Line {item_id} contains stage directions: {text}")

print("Check completed successfully!")

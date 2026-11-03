# -*- coding: utf-8 -*-
import sys
from curated_data_blk078 import CURATED_LINES

for k, v in CURATED_LINES.items():
    text = v['text']
    parts = text.split('\n')
    for p in parts[1:]:
        p_strip = p.strip()
        if not p_strip:
            print(f"Empty line in {k}")
        elif not p_strip[0].isalnum() and p_strip[0] not in ('"', '“', '«'):
            print(f"Line {k} starts with non-alnum after newline: {p!r}")
print("Check completed.")

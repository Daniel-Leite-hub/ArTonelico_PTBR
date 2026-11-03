# -*- coding: utf-8 -*-
import json
import sqlite3
import sys

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for f_idx in range(481, 493):
    fn = f"SLUS/TEXT/{f_idx:04d}"
    group = [d for d in data['dialogues'] if d['event_file'] == fn]
    print(f"\n==================== {fn} ({len(group)} lines, {group[0]['id']}..{group[-1]['id']}) ====================")
    for d in group:
        # Check any name mention in jp or en
        jp = d['original_jp']
        en = d['original_en']
        names = [n for n in ['オリカ', 'Aurica', 'ミシャ', 'Misha', 'シュレリア', 'Shurelia', 'クルシェ', 'Krusche', 'ラードルフ', 'Radolf', 'ジャック', 'Jack'] if n in jp or n in en]
        first_person = [p for p in ['私', '俺', 'あたし', 'ボク', '自分'] if p in jp]
        sentence_end = [e for e in ['わよ', 'わね', 'わ', 'かしら', 'のよ', 'のね', 'ねえ', 'なの', 'よな', 'だろ', 'ぜ', 'ぞ', 'なさい', 'でしょ'] if e in jp]
        if names or len(group) <= 5:
            print(f"[{d['id']}] Names: {names} | JP: {jp}")

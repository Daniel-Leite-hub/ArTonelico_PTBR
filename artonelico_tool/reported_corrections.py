"""Reproducible corrections derived from in-game screenshots and runtime QA."""

from __future__ import annotations

import sqlite3
from collections import Counter

from .evd import encode_game_text


# These remain automatic/editorial bases, never human-approved final reviews.
CORRECTIONS = {
    "Dragon Fillet": ("Filé dragão", "curadoria_local"),
    "A burnt, blackened root of a tree. Even these kind of things become useful.": (
        "Raiz de árvore queimada e carbonizada. Até isso pode ser útil.",
        "curadoria_local",
    ),
    "A ridiculously high place, on the edge of Seagull Port...what were you thinking!?": (
        "Uma altura absurda, à beira do Porto Seagull... no que você estava pensando!?",
        "DeepL+adaptação_local",
    ),
    "How Misha needs to work out": (
        "Como Misha se exercita",
        "DeepL+adaptação_local",
    ),
    "About Misha being very talented": (
        "Sobre o talento de Misha",
        "DeepL+adaptação_local",
    ),
}


def apply_reported_corrections(db: sqlite3.Connection) -> Counter:
    """Apply exact, non-approved corrections while preserving originals."""
    result: Counter = Counter()
    for original, (target, provider) in CORRECTIONS.items():
        rows = db.execute(
            "SELECT id,original_bytes,reviewed FROM dialogues WHERE original=?",
            (original,),
        ).fetchall()
        if not rows:
            result["missing"] += 1
            continue
        for row in rows:
            if row["reviewed"].strip():
                result["review_preserved"] += 1
                continue
            size = len(encode_game_text(target))
            db.execute(
                "UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,"
                "size_ok=?,provider=?,error='' WHERE id=?",
                (target, target, size, int(size <= row["original_bytes"]), provider, row["id"]),
            )
            result["updated"] += 1
    db.commit()
    return result

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from artonelico_tool.rpk import extract


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("rpk", type=Path)
    parser.add_argument("executable", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--suffix")
    args = parser.parse_args()
    entries = extract(args.rpk, args.executable, args.output, args.suffix)
    selected = [x for x in entries if not args.suffix or x.name.casefold().endswith(args.suffix.casefold())]
    print(f"Index: {len(entries)} files; extracted: {len(selected)}")


if __name__ == "__main__":
    main()

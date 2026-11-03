from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from artonelico_tool.patcher import build_iso


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "release" / "ArTonelico_PTBR.atproj"
DEFAULT_OUTPUT = (
    ROOT / "testes pt br" /
    "Ar tonelico PTBR fonte nativa dados apenas 20260926.iso"
)


def main() -> None:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    result = build_iso(PROJECT, output, "native-menu-font")
    print(output)
    print(result["output_sha256"])
    print(f"textos verificados: {result['verified_lines']}")


if __name__ == "__main__":
    main()

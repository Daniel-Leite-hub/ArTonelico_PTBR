from __future__ import annotations

import sys
from pathlib import Path

from artonelico_tool.gui import run


def startup_project(args=None):
    args = sys.argv[1:] if args is None else args
    if args:
        return Path(args[0])
    directory = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent / 'release'
    adapted = directory / 'ArTonelico_PTBR_adaptado_108_20260926.atproj'
    # Keep the master untouched; explicit command-line choices always win.
    return adapted if adapted.is_file() else None


if __name__ == "__main__":
    run(startup_project())

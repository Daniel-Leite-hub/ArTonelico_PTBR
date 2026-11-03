"""Apply screenshot/runtime corrections to one or more project databases."""

from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from artonelico_tool.project import connect
from artonelico_tool.reported_corrections import apply_reported_corrections


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("projects", nargs="+", type=Path)
    args = parser.parse_args()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    for project in args.projects:
        if not project.is_file():
            raise FileNotFoundError(project)
        backup = (
            project.parent / "backups" / project.stem /
            f"{project.stem}.antes_correcoes_runtime_{stamp}.atproj"
        )
        backup.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(project) as source, sqlite3.connect(backup) as destination:
            source.backup(destination)
        with connect(project) as db:
            result = apply_reported_corrections(db)
        print(f"{project}: {dict(result)}; backup={backup}")


if __name__ == "__main__":
    main()

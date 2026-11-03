"""Apply curated UI/item/skill terminology without touching dialogue or reviews."""

from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from artonelico_tool.catalog_localization import apply_catalog_localization
from artonelico_tool.project import connect, ensure_source_identity


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("projects", nargs="+", type=Path)
    args = parser.parse_args()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    for project in args.projects:
        if not project.is_file():
            raise FileNotFoundError(project)
        backup = project.parent / "backups" / project.stem / f"{project.stem}.antes_curadoria_{stamp}.atproj"
        backup.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(project) as source, sqlite3.connect(backup) as destination:
            source.backup(destination)
        with connect(project) as db:
            ensure_source_identity(db)
            result = apply_catalog_localization(db)
            tracks = dict(db.execute("SELECT translation_track,count(*) FROM dialogues GROUP BY translation_track"))
        print(f"{project}: {dict(result)}; trilhas={tracks}; backup={backup}")


if __name__ == "__main__":
    main()
